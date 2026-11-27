"""Cut a lively Reel locally (after the media is fetched into the repo with a *.fetch.json job).

  python3 tools/ig/compose_local.py ig/jobs/<name>/compose.json

compose.json:
{"out": "ig/<name>",
 "segments": [
   {"src": "ig/jobs/<name>/kling.mp4", "start": 0.0, "dur": 4.0, "audio": true, "gain": 1.0,
    "overlays": [{"png": "ig/jobs/<name>/h0.png", "from": 0.0, "to": 1.9}],   # times inside the segment; appear instantly
    "punch": 1.08},                                                            # optional slow push-in (end scale)
   {"src": "ig/jobs/<name>/zoom.mp4", "dur": 1.9}],
 "music": "ig/jobs/<name>/music.mp3", "music_vol": [[0, 0.18], [4.0, 0.55]],    # volume steps over the whole Reel
 "whoosh_at": [4.0, 6.3], "blip_at": [0.1, 0.5], "cover_at": 0.5}
Every 1-2 s something changes: that is the point (Jordy, 27 Nov 2026: "more life").
"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run(args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def has_audio(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries", "stream=index", "-of", "csv=p=0", path],
                       capture_output=True, text=True)
    return bool(r.stdout.strip())


def main(path):
    job = json.load(open(path))
    os.chdir(ROOT)
    with tempfile.TemporaryDirectory() as tmp:
        parts, t = [], 0.0
        for i, seg in enumerate(job["segments"]):
            dur, start = float(seg["dur"]), float(seg.get("start", 0))
            inputs = ["-ss", str(start), "-t", str(dur), "-i", seg["src"]]
            fc = (f"[0:v]setpts=PTS-STARTPTS,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30")
            if seg.get("punch"):
                z = float(seg["punch"])
                fc += (f",scale=w='trunc(1080*(1+({z}-1)*t/{dur})/2)*2':h='trunc(1920*(1+({z}-1)*t/{dur})/2)*2':eval=frame,"
                       "crop=1080:1920")
            fc += "[v0]"
            last = "v0"
            for k, ov in enumerate(seg.get("overlays", [])):
                inputs += ["-loop", "1", "-t", str(dur), "-i", ov["png"]]
                nxt = f"v{k + 1}"
                fc += f";[{last}][{k + 1}:v]overlay=0:0:enable='between(t,{ov.get('from', 0)},{ov.get('to', dur)})'[{nxt}]"
                last = nxt
            fc += f";[{last}]format=yuv420p[v]"
            if seg.get("audio") and has_audio(seg["src"]):
                fc += f";[0:a]asetpts=PTS-STARTPTS,aresample=48000,volume={seg.get('gain', 1.0)},apad,atrim=0:{dur}[a]"
            else:
                fc += f";anullsrc=r=48000:cl=stereo,atrim=0:{dur}[a]"
            part = os.path.join(tmp, f"p{i}.mp4")
            run([*inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast",
                 "-crf", "18", "-c:a", "aac", "-b:a", "192k", "-ac", "2", "-ar", "48000", "-t", str(dur), part])
            parts.append(part)
            t += dur
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
        cut = os.path.join(tmp, "cut.mp4")
        run(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", cut])
        total = t
        # music with volume steps + synthetic whooshes (made here, no third-party audio)
        mix_in, fc, labels = ["-i", cut], "", ["[0:a]"]
        n = 1
        if job.get("music"):
            steps = job.get("music_vol", [[0, 0.3]])
            expr = str(steps[0][1])
            for at, v in steps[1:]:
                expr = f"if(gte(t,{at}),{v},{expr})"
            mix_in += ["-stream_loop", "-1", "-i", job["music"]]
            fc += (f"[{n}:a]atrim=0:{total},asetpts=PTS-STARTPTS,aresample=48000,volume='{expr}':eval=frame,"
                   f"afade=t=out:st={total - 0.7}:d=0.7[m];")
            labels.append("[m]")
            n += 1
        for k, at in enumerate(job.get("whoosh_at", [])):
            mix_in += ["-f", "lavfi", "-t", "0.45", "-i", "anoisesrc=color=pink:amplitude=0.6:r=48000"]
            fc += (f"[{n}:a]highpass=f=600,lowpass=f=5000,afade=t=in:d=0.3,afade=t=out:st=0.3:d=0.15,volume=0.5,"
                   f"aformat=channel_layouts=stereo,adelay={int(max(0, at - 0.3) * 1000)}|{int(max(0, at - 0.3) * 1000)}[w{k}];")
            labels.append(f"[w{k}]")
            n += 1
        for k, at in enumerate(job.get("blip_at", [])):
            # short message 'pop' (synthetic sine), e.g. when a chat bubble appears
            mix_in += ["-f", "lavfi", "-t", "0.07", "-i", "sine=frequency=1320:sample_rate=48000"]
            fc += (f"[{n}:a]afade=t=out:st=0.02:d=0.05,volume=0.35,aformat=channel_layouts=stereo,"
                   f"adelay={int(at * 1000)}|{int(at * 1000)}[b{k}];")
            labels.append(f"[b{k}]")
            n += 1
        fc += "".join(labels) + f"amix=inputs={len(labels)}:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]"
        run([*mix_in, "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
             "-movflags", "+faststart", job["out"] + ".mp4"])
        run(["-ss", str(job.get("cover_at", 0.5)), "-i", job["out"] + ".mp4", "-frames:v", "1", "-q:v", "3", job["out"] + ".jpg"])
    print("made", job["out"] + ".mp4", round(total, 2), "s")


if __name__ == "__main__":
    main(sys.argv[1])
