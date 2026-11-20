"""Lure brand scenes for Reels, recorded from animated HTML (1080x1920, 30 fps).

  python3 tools/ig/scenes.py scenes.json

scenes.json: {"dir": "ig/jobs/<name>", "scenes": [
  {"id": "map",   "type": "phone",   "shot": "appstore/lure-appstore-1-map.png",     "dur": 3.0, "title": "Lure shows you.", "sub": "Every spot. Every friend. Live."},
  {"id": "scan",  "type": "phone",   "shot": "appstore/lure-appstore-2-friends.png", "dur": 2.0, "title": "Scan. Add. Done."},
  {"id": "end",   "type": "end",     "dur": 2.3, "title": "Plan. Post. Meet.", "sub": "Free on iPhone"},
  {"id": "t1",    "type": "overlay", "title": "Your friends are\nout tonight.", "pos": "bottom"}   # transparent PNG for an AI shot
]}
Phone scenes use the real App Store screenshots (the phone part is cropped out and animated).
Writes <dir>/<id>.mp4 (phone/end) or <dir>/<id>.png (overlay).
"""
import html
import json
import os
import subprocess
import sys
import tempfile

from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ICON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")
W, H = 1080, 1920

BASE = """*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:'Poppins',sans-serif;color:#fff;position:relative}
h1{font-weight:700;letter-spacing:-2.5px;line-height:1.02}
@keyframes up{from{opacity:0;transform:translateY(60px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
"""


def esc(t):
    return html.escape(t or "").replace("\n", "<br>")


def crop_phone(src):
    """Cut the phone mockup out of an App Store screenshot (1320x2868) and save it as PNG."""
    im = Image.open(os.path.join(ROOT, src)).convert("RGB")
    w, h = im.size
    box = (int(w * 0.128), int(h * 0.308), int(w * 0.872), h)
    out = os.path.join(tempfile.gettempdir(), os.path.basename(src))
    im.crop(box).save(out)
    return out


def phone_html(s):
    img = crop_phone(s["shot"])
    return f"""<html><head><style>{BASE}
body{{background:radial-gradient(900px 900px at 50% 38%,rgba(255,106,61,.55),transparent 65%),radial-gradient(700px 700px at 10% 100%,rgba(61,214,196,.25),transparent 60%),#0C0B12}}
.top{{position:absolute;top:150px;left:0;right:0;text-align:center;padding:0 70px}}
h1{{font-size:104px;animation:up .55s .05s both}}
.sub{{margin-top:22px;font-size:40px;opacity:.85;animation:up .55s .25s both}}
.ph{{position:absolute;left:50%;top:{560 if s.get('sub') else 470}px;width:820px;transform:translateX(-50%);animation:rise 0.7s cubic-bezier(.2,.9,.25,1) both}}
.ph img{{width:100%;display:block;animation:zoom {s['dur']}s linear both;transform-origin:50% 30%;border-radius:112px 112px 0 0;box-shadow:0 60px 140px rgba(0,0,0,.6)}}
@keyframes rise{{from{{opacity:0;transform:translate(-50%,220px) scale(.92)}}to{{opacity:1;transform:translate(-50%,0) scale(1)}}}}
@keyframes zoom{{from{{transform:scale(1)}}to{{transform:scale(1.07)}}}}
</style></head><body>
<div class="top"><h1>{esc(s.get('title'))}</h1>{f'<div class="sub">{esc(s.get("sub"))}</div>' if s.get('sub') else ''}</div>
<div class="ph"><img src="file://{img}"></div></body></html>"""


def end_html(s):
    return f"""<html><head><style>{BASE}
body{{background:radial-gradient(1000px 1000px at 50% 45%,rgba(255,106,61,.6),transparent 65%),#0C0B12;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
img{{width:250px;height:250px;border-radius:60px;box-shadow:0 30px 90px rgba(255,106,61,.55);animation:pop .6s cubic-bezier(.2,1.4,.4,1) both}}
h1{{margin-top:70px;font-size:112px;animation:up .5s .25s both}}
.sub{{margin-top:30px;font-size:44px;font-weight:700;color:#FF6A3D;animation:up .5s .45s both}}
.url{{margin-top:16px;font-size:34px;opacity:.75;animation:fade .5s .6s both}}
@keyframes pop{{from{{opacity:0;transform:scale(.6)}}to{{opacity:1;transform:scale(1)}}}}
</style></head><body><img src="file://{ICON}"><h1>{esc(s.get('title'))}</h1>
<div class="sub">{esc(s.get('sub'))}</div><div class="url">lureapp.nl</div></body></html>"""


def overlay_html(s):
    bottom = s.get("pos", "bottom") == "bottom"
    shade = ("linear-gradient(180deg,rgba(12,11,18,.45) 0%,rgba(12,11,18,0) 18%,rgba(12,11,18,0) 50%,rgba(12,11,18,.85) 100%)" if bottom
             else "linear-gradient(180deg,rgba(12,11,18,.85) 0%,rgba(12,11,18,0) 45%,rgba(12,11,18,0) 82%,rgba(12,11,18,.45) 100%)")
    place = "bottom:230px" if bottom else "top:230px"
    return f"""<html><head><style>{BASE}
body{{background:transparent}}
.shade{{position:absolute;inset:0;background:{shade}}}
.brand{{position:absolute;top:96px;left:84px;display:flex;align-items:center;gap:16px;font-weight:700;font-size:38px}}
.brand img{{width:64px;height:64px;border-radius:16px}}
.t{{position:absolute;{place};left:80px;right:80px}}
h1{{font-size:{s.get('size', 112)}px;text-shadow:0 6px 30px rgba(0,0,0,.45)}}
h1 em{{font-style:normal;color:#FF6A3D}}
</style></head><body><div class="shade"></div>
<div class="brand"><img src="file://{ICON}">Lure</div>
<div class="t"><h1>{esc(s.get('title')).replace('[', '<em>').replace(']', '</em>')}</h1></div></body></html>"""


def main(path):
    spec = json.load(open(path))
    outdir = os.path.join(ROOT, spec["dir"])
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        b = p.chromium.launch(channel="chrome") if os.path.exists("/usr/bin/google-chrome") else p.chromium.launch()
        for s in spec["scenes"]:
            page_file = os.path.join(tmp, s["id"] + ".html")
            if s["type"] == "overlay":
                open(page_file, "w").write(overlay_html(s))
                pg = b.new_page(viewport={"width": W, "height": H})
                pg.goto("file://" + page_file)
                pg.wait_for_timeout(500)
                pg.screenshot(path=os.path.join(outdir, s["id"] + ".png"), omit_background=True)
                pg.close()
                continue
            open(page_file, "w").write(phone_html(s) if s["type"] == "phone" else end_html(s))
            ctx = b.new_context(viewport={"width": W, "height": H}, record_video_dir=tmp, record_video_size={"width": W, "height": H})
            pg = ctx.new_page()
            pg.goto("file://" + page_file)
            pg.wait_for_timeout(int(s["dur"] * 1000) + 700)
            vid = pg.video.path()
            ctx.close()
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.25", "-i", vid, "-t", str(s["dur"]),
                            "-vf", "fps=30,format=yuv420p", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-an",
                            os.path.join(outdir, s["id"] + ".mp4")], check=True)
        b.close()
    print("scenes in", outdir)


if __name__ == "__main__":
    main(sys.argv[1])
