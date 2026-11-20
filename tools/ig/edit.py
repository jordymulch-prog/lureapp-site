"""Cut a Lure Reel from AI shots, brand scenes and music. Runs in the GitHub Action (it can download from Higgsfield).

  python3 tools/ig/edit.py ig/jobs/<name>.edit.json

edit.json:
{"out": "ig/<name>",
 "music": "<Higgsfield audio URL or repo path>",
 "segments": [
   {"src": "<Higgsfield video URL>", "dur": 2.95, "skip": 0.3, "overlay": "ig/jobs/<name>/t1.png"},
   {"src": "ig/jobs/<name>/map.mp4", "dur": 2.95},
   ...]}
Writes <out>.mp4 (1080x1920, 30 fps, H.264, AAC) and <out>.jpg (cover).
"""
import json
import os
import subprocess
import sys
import tempfile
import urllib.request

ALLOWED = ("https://d8j0ntlcm91z4.cloudfront.net/",)


def fetch(src, tmp, name):
    if src.startswith("http"):
        if not src.startswith(ALLOWED):
            raise SystemExit(f"url not allowed: {src}")
        dst = os.path.join(tmp, name)
        urllib.request.urlretrieve(src, dst)
        return dst
    return src


def run(args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def main(path):
    job = json.load(open(path))
    out = job["out"]
    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for i, seg in enumerate(job["segments"]):
            src = fetch(seg["src"], tmp, f"in{i}.mp4")
            dur = float(seg["dur"])
            part = os.path.join(tmp, f"p{i}.mp4")
            base = (f"[0:v]trim=start={seg.get('skip', 0)}:duration={dur},setpts=PTS-STARTPTS,"
                    "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,fps=30")
            if seg.get("grade", True) and src.startswith(tmp):
                # light, consistent grade for AI footage: a touch more contrast and warmth
                base += ",eq=contrast=1.06:saturation=1.08,colorbalance=rm=0.03:bm=-0.02"
            if seg.get("overlay"):
                # text slides up 50 px and fades in over 0.35 s
                fc = (f"{base}[bg];[1:v]format=rgba,fade=in:st=0.05:d=0.35:alpha=1[ov];"
                      f"[bg][ov]overlay=x=0:y='if(lt(t,0.4),50*(1-t/0.4),0)':shortest=1,format=yuv420p[v]")
                run(["-i", src, "-loop", "1", "-t", str(dur), "-i", seg["overlay"], "-filter_complex", fc,
                     "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", part])
            else:
                run(["-i", src, "-filter_complex", base + ",format=yuv420p[v]", "-map", "[v]", "-an",
                     "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", part])
            parts.append(part)
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
        silent = os.path.join(tmp, "silent.mp4")
        run(["-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent])
        total = sum(float(s["dur"]) for s in job["segments"])
        if job.get("music"):
            music = fetch(job["music"], tmp, "music.audio")
            run(["-i", silent, "-i", music, "-filter_complex",
                 f"[1:a]atrim=0:{total},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={total - 0.8}:d=0.8,"
                 "loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                 "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                 "-movflags", "+faststart", out + ".mp4"])
        else:
            run(["-i", silent, "-c", "copy", "-movflags", "+faststart", out + ".mp4"])
        run(["-ss", str(job.get("cover_at", 0.8)), "-i", out + ".mp4", "-frames:v", "1", "-q:v", "3", out + ".jpg"])
    print("made", out + ".mp4")


if __name__ == "__main__":
    main(sys.argv[1])
