"""Story (1080x1920): 'Chai on an empty stomach?' python3 _src/social/story_chai.py -> _src/out/stories/chai.png"""
import base64, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "stories"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
LOGO = "data:image/png;base64," + base64.b64encode(open(f"{SRC}/brand/logo-mark.png", "rb").read()).decode()

STOMACH = "M124 98 C150 84 192 98 190 128 C188 154 160 168 138 160 C120 154 122 134 138 130 C152 126 152 112 128 112 Z"

def scene():
    flame = lambda x, y, s: (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C-14 -14 -10 -30 0 -44 C2 -32 14 -28 12 -12 C12 -4 6 2 0 0Z" fill="#F08A2C"/>'
                             f'<path d="M0 -2 C-6 -8 -5 -18 0 -26 C2 -18 7 -14 6 -7 C5 -3 3 -1 0 -2Z" fill="#F7D46B"/></g>')
    return f"""<svg viewBox="0 0 900 640" xmlns="http://www.w3.org/2000/svg">
<defs>
 <linearGradient id="chai" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D9A066"/><stop offset="1" stop-color="#A9672F"/></linearGradient>
 <linearGradient id="glass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".9"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".25"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".8"/></linearGradient>
 <radialGradient id="st" cx="45%" cy="40%" r="70%"><stop offset="0" stop-color="#F7C2B5"/><stop offset="1" stop-color="#E58C78"/></radialGradient>
 <filter id="sh"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#5A3410" flood-opacity=".25"/></filter>
</defs>
<!-- cutting chai glass -->
<g transform="translate(60 120)" filter="url(#sh)">
 <path d="M30 400 C20 400 14 394 13 386 L0 30 H200 L187 386 C186 394 180 400 170 400 Z" fill="#FFFFFF" fill-opacity=".55" stroke="#CDB79C" stroke-width="5"/>
 <path d="M14 120 H186 L176 380 C175 388 170 392 162 392 H38 C30 392 25 388 24 380 Z" fill="url(#chai)"/>
 <path d="M14 120 H186" stroke="#F1D2A8" stroke-width="10" stroke-linecap="round"/>
 <path d="M8 60 L192 60 M10 90 L190 90" stroke="#CDB79C" stroke-width="3" opacity=".6"/>
 <path d="M0 30 H200 L187 386 C186 394 180 400 170 400 H30 C20 400 14 394 13 386 Z" fill="url(#glass)" opacity=".45"/>
 <g fill="none" stroke="#B88A5A" stroke-width="7" stroke-linecap="round" opacity=".55">
  <path d="M60 10 c-16 -26 16 -40 0 -70"/><path d="M104 0 c-16 -26 16 -40 0 -70"/><path d="M148 10 c-16 -26 16 -40 0 -70"/>
 </g>
</g>
<!-- arrow -->
<path d="M290 330 C340 300 390 300 440 320" fill="none" stroke="#12302C" stroke-width="8" stroke-linecap="round" stroke-dasharray="4 16"/>
<path d="M428 296 L456 324 L420 340" fill="none" stroke="#12302C" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
<!-- empty stomach with flames -->
<g transform="translate(160 -30) scale(3.1)">
 <path d="M126 20 V100" stroke="#E58C78" stroke-width="13" stroke-linecap="round"/>
 <path d="M126 20 V100" stroke="#F7C2B5" stroke-width="8" stroke-linecap="round"/>
 <path d="{STOMACH}" fill="url(#st)" stroke="#C9604B" stroke-width="2"/>
</g>
{flame(650,440,1.7)}{flame(598,424,1.2)}{flame(700,412,1.15)}{flame(626,384,0.85)}
<text x="650" y="560" text-anchor="middle" font-family="FT" font-weight="600" font-size="30" fill="#B0362B">Empty stomach</text>
</svg>"""

ICONS = {
 "Soaked almonds": '<g>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="16" ry="26" fill="#C98A4E" stroke="#9C6420" stroke-width="3" transform="rotate({r} {x} {y})"/>' for x, y, r in [(56,86,-30),(82,74,0),(108,88,30),(70,112,-10),(98,114,15)]) + '</g>',
 "A fruit": '<circle cx="80" cy="88" r="50" fill="#F28A2E"/><circle cx="64" cy="72" r="12" fill="#F9B867" opacity=".7"/><path d="M80 38 q4 -14 16 -20" stroke="#5B3A1E" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M86 36 q20 -14 30 2 q-20 8 -30 -2" fill="#4E9A32"/>',
 "Then chai": '<path d="M44 40 H116 L110 128 C109 134 104 138 98 138 H62 C56 138 51 134 50 128 Z" fill="#FFFFFF" stroke="#CDB79C" stroke-width="5"/><path d="M47 70 H113 L109 126 C108 131 104 134 99 134 H61 C56 134 52 131 51 126 Z" fill="#C88A4F"/><g fill="none" stroke="#B88A5A" stroke-width="5" stroke-linecap="round" opacity=".6"><path d="M66 30 c-8 -12 8 -20 0 -32"/><path d="M94 30 c-8 -12 8 -20 0 -32"/></g>',
}
def icon(k): return f'<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">{ICONS[k]}</svg>'

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:"FT",sans-serif;color:#12302C;
 background:radial-gradient(110% 70% at 50% 35%,#FFF7EC 0%,#F9E6CC 60%,#F1D2A8 100%)}}
.kick{{font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
h1{{font-family:"YS",serif;font-weight:400;line-height:1.02}}
em{{font-style:normal;color:#B0362B}}
</style></head><body>
 <div style="position:absolute;top:140px;left:70px;right:70px;text-align:center">
  <div class="kick" style="font-size:30px;color:#0D7466">Today's gut tip</div>
  <h1 style="font-size:96px;margin-top:22px">Chai on an<br><em>empty stomach?</em></h1>
 </div>
 <div style="position:absolute;top:470px;left:90px;width:900px">{scene()}</div>
 <p style="position:absolute;top:1150px;left:90px;right:90px;text-align:center;font-size:38px;line-height:1.4">For people prone to acidity, it can bring on<br>burning and nausea.</p>
 <div style="position:absolute;top:1330px;left:70px;right:70px">
  <div class="kick" style="font-size:26px;color:#4A615D;text-align:center;margin-bottom:22px">Try this order instead</div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:18px">
   {''.join(f'<div style="position:relative;background:#fff;border-radius:36px;padding:26px 10px 24px;text-align:center"><span style="position:absolute;top:-18px;left:50%;transform:translateX(-50%);width:44px;height:44px;border-radius:50%;background:#0D7466;color:#fff;font-weight:600;font-size:26px;display:grid;place-items:center">{i}</span><div style="width:150px;height:150px;margin:0 auto">{icon(k)}</div><div style="font-size:30px;font-weight:600;margin-top:4px">{k}</div></div>' for i, k in enumerate(ICONS, 1))}
  </div>
 </div>
 <div style="position:absolute;left:80px;right:80px;bottom:70px;display:flex;align-items:center;gap:18px">
  <img src="{LOGO}" style="width:74px;height:74px">
  <div><b style="font-family:YS;font-weight:400;font-size:32px;display:block">Dr. Kshitij Lochab</b><span style="font-size:23px;color:#4A615D">Gastroenterologist · drlochab.com</span></div>
 </div>
</body></html>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        open(f"{OUT}/tmp.html", "w").write(HTML); pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(300)
        pg.screenshot(path=f"{OUT}/chai.png"); b.close()
    os.remove(f"{OUT}/tmp.html"); print("done")
