"""Lure Instagram content renderer.

Usage:
  python3 tools/ig/render.py spec.json

spec.json:
{
  "kind": "image" | "video",          # image = 1080x1350 JPEG feed post, video = 1080x1920 MP4 reel (~8 s)
  "out": "ig/2026-11-23",             # path without extension, relative to the repo root
  "kicker": "NEW CITY",               # small label at the top (optional)
  "title": "Purmerend is live",        # big headline, use \n for line breaks
  "subtitle": "40 spots on the map",   # optional
  "items": ["Brasserie 1434", "..."],  # optional list (max 6)
  "cta": "Download Lure. Free on iPhone",  # optional bottom line
  "photo": "https://...",              # optional background photo URL (e.g. from Higgsfield)
  "size": 104                          # optional headline font size (smaller for long titles)
}
AI media: add "media_url": "<Higgsfield result URL>" -> only the text layer is rendered here; push, and the GitHub
Action .github/workflows/compose.yml downloads the media, adds the text and commits <out>.mp4/.jpg (+ cover .jpg for video).
Carousel: {"out": "ig/2026-11-24", "slides": [{...image keys...}, {...}]} -> ig/2026-11-24-1.jpg, -2.jpg, ...
Writes <out>.jpg (always; for video it is the cover) and <out>.mp4 for video.
"""
import html
import json
import os
import subprocess
import sys
import tempfile

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ICON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.png")


def page_html(s: dict, w: int, h: int, animate: bool) -> str:
    e = lambda t: html.escape(t or "").replace("\n", "<br>")
    items = "".join(
        f'<div class="it" style="animation-delay:{1.2 + i * 0.35:.2f}s"><span class="pin"></span>{e(x)}</div>'
        for i, x in enumerate((s.get("items") or [])[:6])
    )
    photo = s.get("photo")
    if s.get("transparent"):
        bg = "background:transparent;"
    else:
      bg = (
        f"background:linear-gradient(180deg,rgba(12,11,18,.35) 0%,rgba(12,11,18,.55) 45%,rgba(12,11,18,.95) 100%),url('{html.escape(photo)}') center/cover;"
        if photo
        else "background:radial-gradient(1200px 900px at 85% 10%,rgba(255,106,61,.38),transparent 60%),radial-gradient(900px 700px at 0% 100%,rgba(61,214,196,.22),transparent 60%),#0C0B12;"
      )
    anim = "" if animate else "h1,.sub,.it,.cta{animation:none!important;opacity:1!important;transform:none!important}"
    scale = w / 1080
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:local('Poppins Bold'),local('Poppins-Bold');font-weight:700}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{w}px;height:{h}px;overflow:hidden}}
body{{{bg}color:#fff;font-family:'Poppins','DM Sans',sans-serif;position:relative}}
.grid{{position:absolute;inset:0;opacity:{0 if photo else .13};background-image:
  linear-gradient(115deg,transparent 48%,#fff 49%,#fff 50%,transparent 51%),
  linear-gradient(25deg,transparent 48%,#fff 49.4%,#fff 50%,transparent 51%);
  background-size:{int(260*scale)}px {int(260*scale)}px,{int(340*scale)}px {int(340*scale)}px}}
.wrap{{position:absolute;inset:0;padding:{int(90*scale)}px {int(84*scale)}px;display:flex;flex-direction:column}}
.top{{display:flex;align-items:center;gap:{int(18*scale)}px}}
.top img{{width:{int(70*scale)}px;height:{int(70*scale)}px;border-radius:{int(18*scale)}px}}
.brand{{font-weight:700;font-size:{int(40*scale)}px;letter-spacing:.5px}}
.kick{{margin-left:auto;background:#FF6A3D;color:#1A0B05;font-weight:700;font-size:{int(26*scale)}px;padding:{int(10*scale)}px {int(22*scale)}px;border-radius:999px;letter-spacing:1.5px}}
.mid{{margin-top:auto}}
h1{{font-weight:700;font-size:{int((s.get('size') or 104)*scale)}px;line-height:1.02;letter-spacing:-2px;animation:up .7s .2s both}}
h1 em{{font-style:normal;color:#FF6A3D}}
.sub{{margin-top:{int(26*scale)}px;font-size:{int(40*scale)}px;color:#E9E3F2;opacity:.9;animation:up .7s .6s both;line-height:1.25}}
.list{{margin-top:{int(40*scale)}px;display:flex;flex-direction:column;gap:{int(16*scale)}px}}
.it{{display:flex;align-items:center;gap:{int(18*scale)}px;font-size:{int(36*scale)}px;font-weight:700;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);border-radius:{int(24*scale)}px;padding:{int(18*scale)}px {int(26*scale)}px;animation:up .6s both}}
.pin{{width:{int(22*scale)}px;height:{int(22*scale)}px;border-radius:50%;background:#3DD6C4;box-shadow:0 0 0 {int(8*scale)}px rgba(61,214,196,.22);flex:none}}
.cta{{margin-top:{int(54*scale)}px;font-size:{int(32*scale)}px;font-weight:700;color:#FF6A3D;animation:up .7s 1s both}}
.shade{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,11,18,.6) 0%,rgba(12,11,18,0) 20%,rgba(12,11,18,0) 42%,rgba(12,11,18,.9) 75%,#0C0B12 100%)}}
@keyframes up{{from{{opacity:0;transform:translateY({int(40*scale)}px)}}to{{opacity:1;transform:none}}}}
{anim}
</style></head><body>{'<div class="shade"></div>' if s.get("transparent") else '<div class="grid"></div>'}<div class="wrap">
<div class="top"><img src="file://{ICON}"><div class="brand">Lure</div>{f'<div class="kick">{e(s.get("kicker"))}</div>' if s.get("kicker") else ''}</div>
<div class="mid"><h1>{e(s.get('title')).replace('*', '')}</h1>
{f'<div class="sub">{e(s.get("subtitle"))}</div>' if s.get('subtitle') else ''}
{f'<div class="list">{items}</div>' if items else ''}
{f'<div class="cta">{e(s.get("cta"))}</div>' if s.get('cta') else ''}</div></div></body></html>"""


def main(path: str) -> None:
    s = json.load(open(path))
    # Carousel: "slides": [{...}, {...}] -> <out>-1.jpg, <out>-2.jpg, ... (each slide uses the same keys as an image post)
    if s.get("slides"):
        for i, slide in enumerate(s["slides"], 1):
            one = os.path.join(tempfile.gettempdir(), f"slide{i}.json")
            json.dump({**slide, "kind": "image", "out": f"{s['out']}-{i}"}, open(one, "w"))
            main(one)
        return
    out = os.path.join(ROOT, s["out"])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    video = s.get("kind") == "video"
    w, h = (1080, 1920) if video else (1080, 1350)
    if s.get("media_url"):
        # AI photo/video from Higgsfield: render only the text layer (transparent PNG) and queue a GitHub
        # Actions job that downloads the media and puts the text on top (.github/workflows/compose.yml).
        s["transparent"] = True
        name = os.path.basename(out)
        jobs = os.path.join(ROOT, "ig", "jobs")
        os.makedirs(jobs, exist_ok=True)
        with sync_playwright() as p:
            b = p.chromium.launch(channel="chrome") if os.path.exists("/usr/bin/google-chrome") else p.chromium.launch()
            pg = b.new_page(viewport={"width": w, "height": h})
            tmp_html = os.path.join(tempfile.gettempdir(), "overlay.html")
            open(tmp_html, "w").write(page_html(s, w, h, animate=False))
            pg.goto("file://" + tmp_html)
            pg.wait_for_timeout(600)
            pg.screenshot(path=os.path.join(jobs, name + "-overlay.png"), omit_background=True)
            b.close()
        json.dump({"media_url": s["media_url"], "type": "video" if video else "image", "overlay": f"ig/jobs/{name}-overlay.png", "out": s["out"]},
                  open(os.path.join(jobs, name + ".json"), "w"), indent=1)
        print("queued", os.path.join(jobs, name + ".json"), "-> push, then wait for", s["out"] + (".mp4" if video else ".jpg"))
        return
    with tempfile.TemporaryDirectory() as tmp, sync_playwright() as p:
        b = p.chromium.launch(channel="chrome") if os.path.exists("/usr/bin/google-chrome") else p.chromium.launch()
        still = os.path.join(tmp, "still.html")
        open(still, "w").write(page_html(s, w, h, animate=False))
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto("file://" + still)
        pg.wait_for_timeout(600)
        png = os.path.join(tmp, "still.png")
        pg.screenshot(path=png)
        pg.close()
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", png, "-q:v", "3", out + ".jpg"], check=True)
        if video:
            moving = os.path.join(tmp, "move.html")
            open(moving, "w").write(page_html(s, w, h, animate=True))
            ctx = b.new_context(viewport={"width": w, "height": h}, record_video_dir=tmp, record_video_size={"width": w, "height": h})
            pg = ctx.new_page()
            pg.goto("file://" + moving)
            pg.wait_for_timeout(8500)
            vid = pg.video.path()
            ctx.close()
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-ss", "0.3", "-i", vid, "-t", "8", "-vf", "fps=30,format=yuv420p",
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-movflags", "+faststart", "-an", out + ".mp4"],
                check=True,
            )
        b.close()
    print(out + ".jpg", out + ".mp4" if video else "")


if __name__ == "__main__":
    main(sys.argv[1])
