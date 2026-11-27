"""Lure brand scenes for Reels, recorded from animated HTML (1080x1920, 30 fps).

  python3 tools/ig/scenes.py scenes.json

scenes.json: {"dir": "ig/jobs/<name>", "scenes": [
  {"id": "map",   "type": "phone",   "shot": "appstore/lure-appstore-1-map.png",     "dur": 3.0, "title": "Lure shows you.", "sub": "Every spot. Every friend. Live."},
  {"id": "scan",  "type": "phone",   "shot": "appstore/lure-appstore-2-friends.png", "dur": 2.0, "title": "Scan. Add. Done."},
  {"id": "end",   "type": "end",     "dur": 2.3, "title": "Plan. Post. Meet.", "sub": "Free on iPhone"},
  {"id": "t1",    "type": "overlay", "title": "Your friends are\nout tonight.", "pos": "bottom"},  # transparent PNG for an AI shot
  {"id": "zoom",  "type": "mapzoom", "shot": "appstore/lure-appstore-1-map.png", "dur": 1.8, "title": "Both on the [Lure map]", "sub": "..."},  # phone fills the screen, camera pushes in
  {"id": "ab",    "type": "ab", "dur": 2.0, "a": "A", "b": "B", "title": "Comment the [letter]", "sub": "..."},  # kinetic comment prompt
  {"id": "h1",    "type": "hud", "big": "Top text", "mission": "Pick tonight's spot", "letter": "A", "name": "Spot", "tip": "tip"},  # own game-style HUD, real Lure map as minimap
  {"id": "lA",    "type": "label", "letter": "A", "name": "Spot", "tip": "tip", "hook": "optional hook box"}  # transparent PNG
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


def caption_html(s):
    """Interview layer: question on top, name tag lower third, optional subtitle line."""
    q = f'<div class="q">{esc(s["question"])}</div>' if s.get("question") else ""
    tag = (f'<div class="tag"><b>{esc(s["name"])}</b><span>{esc(s.get("role", ""))}</span></div>' if s.get("name") else "")
    sub = f'<div class="sub">{esc(s["sub"])}</div>' if s.get("sub") else ""
    return f"""<html><head><style>{BASE}
body{{background:transparent}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,11,18,.55) 0%,rgba(12,11,18,0) 22%,rgba(12,11,18,0) 62%,rgba(12,11,18,.7) 100%)}}
.brand{{position:absolute;top:96px;left:84px;display:flex;align-items:center;gap:16px;font-weight:700;font-size:38px}}
.brand img{{width:64px;height:64px;border-radius:16px}}
.q{{position:absolute;top:210px;left:70px;right:70px;text-align:center;font-weight:700;font-size:66px;line-height:1.1;
   background:#fff;color:#0C0B12;border-radius:28px;padding:26px 34px;box-shadow:0 18px 50px rgba(0,0,0,.35)}}
.tag{{position:absolute;left:70px;bottom:330px;background:#FF6A3D;color:#1A0B05;border-radius:22px;padding:18px 30px;display:flex;flex-direction:column}}
.tag b{{font-size:52px;line-height:1.05}}
.tag span{{font-size:32px;font-weight:600;opacity:.85}}
.sub{{position:absolute;left:70px;right:70px;bottom:170px;text-align:center;font-weight:700;font-size:46px;line-height:1.2;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
</style></head><body><div class="shade"></div><div class="brand"><img src="file://{ICON}">Lure HQ</div>{q}{tag}{sub}</body></html>"""


def mapzoom_html(s):
    """Lively app moment: the real phone fills the screen and the camera pushes into the map, a pin pulses."""
    img = crop_phone(s["shot"])
    return f"""<html><head><style>{BASE}
body{{background:radial-gradient(900px 900px at 50% 45%,rgba(255,106,61,.6),transparent 65%),#0C0B12;overflow:hidden}}
.ph{{position:absolute;left:50%;top:150px;width:900px;transform-origin:50% 45%;animation:push {s['dur']}s cubic-bezier(.3,.0,.2,1) both}}
.ph img{{width:100%;display:block;border-radius:120px 120px 0 0;box-shadow:0 60px 140px rgba(0,0,0,.6)}}
@keyframes push{{0%{{transform:translateX(-50%) translateY(260px) scale(.9);opacity:0}}18%{{opacity:1;transform:translateX(-50%) translateY(0) scale(1)}}100%{{transform:translateX(-50%) translateY(0) scale(1.4)}}}}
.pin{{position:absolute;left:50%;top:860px;width:90px;height:90px;margin-left:-45px;border-radius:50%;background:#FF6A3D;border:10px solid #fff;box-shadow:0 0 0 0 rgba(255,106,61,.7);animation:fade .2s .45s both,pulse .8s .5s infinite}}
@keyframes pulse{{0%{{box-shadow:0 0 0 0 rgba(255,106,61,.75)}}100%{{box-shadow:0 0 0 70px rgba(255,106,61,0)}}}}
.top{{position:absolute;bottom:0;left:0;right:0;padding:120px 60px 170px;text-align:center;background:linear-gradient(180deg,rgba(12,11,18,0),rgba(12,11,18,.92) 35%,#0C0B12);z-index:5}}
h1{{font-size:92px;animation:slam .35s .05s cubic-bezier(.2,1.5,.4,1) both;text-shadow:0 8px 30px rgba(0,0,0,.5)}}
h1 em{{font-style:normal;color:#FF6A3D}}
.sub{{margin-top:16px;font-size:42px;font-weight:600;animation:up .4s .3s both}}
@keyframes slam{{from{{opacity:0;transform:scale(1.6)}}to{{opacity:1;transform:scale(1)}}}}
</style></head><body><div class="ph"><img src="file://{img}"></div><div class="pin"></div>
<div class="top"><h1>{esc(s.get('title')).replace('[', '<em>').replace(']', '</em>')}</h1>{f'<div class="sub">{esc(s.get("sub"))}</div>' if s.get('sub') else ''}</div></body></html>"""


def ab_html(s):
    """Kinetic comment prompt: A and B slam in on the beat, then the ask."""
    a, b = s.get("a", "A"), s.get("b", "B")
    return f"""<html><head><style>{BASE}
body{{background:#0C0B12;overflow:hidden;animation:flash {s['dur']}s steps(1) both}}
@keyframes flash{{0%{{background:#FF6A3D}}12%{{background:#0C0B12}}30%{{background:#3DD6C4}}42%{{background:#0C0B12}}}}
.row{{position:absolute;top:470px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:40px}}
.l{{font-size:420px;font-weight:700;line-height:1}}
.a{{color:#fff;animation:slam .3s .0s cubic-bezier(.2,1.6,.4,1) both}}
.b{{color:#fff;animation:slam .3s .36s cubic-bezier(.2,1.6,.4,1) both}}
.or{{font-size:110px;font-weight:700;color:#FF6A3D;animation:fade .2s .3s both}}
.ask{{position:absolute;top:1080px;left:70px;right:70px;text-align:center;font-size:84px;font-weight:700;line-height:1.08;animation:up .4s .7s both}}
.ask em{{font-style:normal;color:#FF6A3D}}
.hint{{position:absolute;top:1330px;left:0;right:0;text-align:center;font-size:44px;opacity:.85;animation:up .4s 1.0s both}}
@keyframes slam{{from{{opacity:0;transform:scale(2.2) rotate(-8deg)}}to{{opacity:1;transform:none}}}}
</style></head><body><div class="row"><div class="l a">{esc(a)}</div><div class="or">or</div><div class="l b">{esc(b)}</div></div>
<div class="ask">{esc(s.get('title')).replace('[', '<em>').replace(']', '</em>')}</div><div class="hint">{esc(s.get('sub'))}</div></body></html>"""


def label_html(s):
    """Transparent label for an AI shot: a big letter badge + spot name, top of frame; optional hook box."""
    hook = f'<div class="hook">{esc(s["hook"])}</div>' if s.get("hook") else ""
    badge = (f'<div class="lab"><div class="badge" style="background:{s.get("color", "#FF6A3D")}">{esc(s["letter"])}</div>'
             f'<div><b>{esc(s.get("name"))}</b><span>{esc(s.get("tip"))}</span></div></div>') if s.get("letter") else ""
    return f"""<html><head><style>{BASE}
body{{background:transparent}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,11,18,.6) 0%,rgba(12,11,18,0) 26%,rgba(12,11,18,0) 75%,rgba(12,11,18,.35) 100%)}}
.hook{{position:absolute;top:200px;left:60px;right:60px;text-align:center;font-weight:700;font-size:80px;line-height:1.05;background:#fff;color:#0C0B12;border-radius:30px;padding:28px 30px;box-shadow:0 18px 50px rgba(0,0,0,.35)}}
.lab{{position:absolute;top:210px;left:60px;right:60px;display:flex;align-items:center;gap:30px}}
.badge{{width:190px;height:190px;border-radius:44px;display:flex;align-items:center;justify-content:center;font-size:150px;font-weight:700;color:#0C0B12;flex:none;box-shadow:0 16px 40px rgba(0,0,0,.4)}}
.lab b{{display:block;font-size:74px;line-height:1.02;text-shadow:0 6px 24px rgba(0,0,0,.6)}}
.lab span{{display:block;margin-top:10px;font-size:40px;font-weight:600;text-shadow:0 4px 18px rgba(0,0,0,.8)}}
</style></head><body><div class="shade"></div>{hook}{badge}</body></html>"""


def minimap_png(shot):
    """Square crop of the map area of a real App Store screenshot, used as a game-style minimap."""
    im = Image.open(crop_phone(shot))
    w, h = im.size
    cx, cy, r = int(w * 0.49), int(h * 0.53), int(w * 0.34)
    out = os.path.join(tempfile.gettempdir(), "minimap_" + os.path.basename(shot))
    im.crop((cx - r, cy - r, cx + r, cy + r)).save(out)
    return out


def hud_html(s):
    """Own open-world-game HUD (no third-party game assets): mission box, real Lure map as minimap,
    optional big top text and an A/B choice label."""
    mm = minimap_png(s.get("shot", "appstore/lure-appstore-1-map.png"))
    big = (f'<div class="big">{esc(s["big"]).replace("[", "<em>").replace("]", "</em>")}</div>') if s.get("big") else ""
    mission = (f'<div class="mis"><small>{esc(s.get("mission_label", "NEW MISSION"))}</small>{esc(s["mission"])}</div>') if s.get("mission") else ""
    choice = (f'<div class="ch"><div class="badge" style="background:{s.get("color", "#FF6A3D")}">{esc(s["letter"])}</div>'
              f'<div><b>{esc(s.get("name"))}</b><span>{esc(s.get("tip"))}</span></div></div>') if s.get("letter") else ""
    return f"""<html><head><style>{BASE}
body{{background:transparent}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 30%,rgba(0,0,0,0) 62%,rgba(0,0,0,.55) 100%)}}
.big{{position:absolute;top:170px;left:60px;right:60px;text-align:center;font-weight:700;font-size:{s.get('size', 96)}px;line-height:1.04;
  -webkit-text-stroke:3px #000;paint-order:stroke fill;text-shadow:0 8px 0 rgba(0,0,0,.55),0 0 40px rgba(0,0,0,.5)}}
.big em{{font-style:normal;color:#FF6A3D}}
.mis{{position:absolute;top:{s.get('mission_top', 170)}px;left:56px;max-width:720px;background:rgba(10,10,14,.72);border-left:12px solid #FF6A3D;border-radius:10px;padding:20px 30px;font-weight:700;font-size:50px;line-height:1.1}}
.mis small{{display:block;font-size:30px;letter-spacing:6px;color:#FF6A3D;margin-bottom:6px}}
.ch{{position:absolute;top:{s.get('choice_top', 420)}px;left:56px;right:56px;display:flex;align-items:center;gap:28px}}
.badge{{width:170px;height:170px;border-radius:40px;display:flex;align-items:center;justify-content:center;font-size:132px;font-weight:700;color:#0C0B12;flex:none;border:6px solid #fff;box-shadow:0 14px 40px rgba(0,0,0,.5)}}
.ch b{{display:block;font-size:72px;line-height:1.02;-webkit-text-stroke:2px #000;paint-order:stroke fill;text-shadow:0 6px 0 rgba(0,0,0,.5)}}
.ch span{{display:block;margin-top:10px;font-size:40px;font-weight:600;text-shadow:0 3px 14px rgba(0,0,0,.95)}}
.mm{{position:absolute;left:56px;bottom:150px;width:300px;height:300px;border-radius:50%;overflow:hidden;border:8px solid rgba(255,255,255,.92);box-shadow:0 0 0 6px rgba(0,0,0,.55),0 20px 50px rgba(0,0,0,.5)}}
.mm img{{width:100%;height:100%;object-fit:cover}}
.arrow{{position:absolute;left:50%;top:50%;width:0;height:0;margin:-30px 0 0 -20px;border-left:20px solid transparent;border-right:20px solid transparent;border-bottom:50px solid #FF6A3D;filter:drop-shadow(0 0 4px #fff)}}
.mmlabel{{position:absolute;left:56px;bottom:100px;width:300px;text-align:center;font-weight:700;font-size:30px;letter-spacing:3px;text-shadow:0 2px 10px #000}}
</style></head><body><div class="shade"></div>{big}{mission}{choice}
<div class="mm"><img src="file://{mm}"><div class="arrow"></div></div><div class="mmlabel">LURE MAP</div></body></html>"""


def main(path):
    spec = json.load(open(path))
    outdir = os.path.join(ROOT, spec["dir"])
    os.makedirs(outdir, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        b = p.chromium.launch(channel="chrome") if os.path.exists("/usr/bin/google-chrome") else p.chromium.launch()
        for s in spec["scenes"]:
            page_file = os.path.join(tmp, s["id"] + ".html")
            if s["type"] in ("overlay", "caption", "label", "hud"):
                open(page_file, "w").write({"overlay": overlay_html, "caption": caption_html, "label": label_html, "hud": hud_html}[s["type"]](s))
                pg = b.new_page(viewport={"width": W, "height": H})
                pg.goto("file://" + page_file)
                pg.wait_for_timeout(500)
                pg.screenshot(path=os.path.join(outdir, s["id"] + ".png"), omit_background=True)
                pg.close()
                continue
            open(page_file, "w").write({"phone": phone_html, "end": end_html, "mapzoom": mapzoom_html, "ab": ab_html}[s["type"]](s))
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
