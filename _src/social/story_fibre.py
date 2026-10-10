"""Instagram/WhatsApp story (1080x1920): 'Is your gut running on empty?' fibre fuel gauge.
python3 _src/social/story_fibre.py -> _src/out/stories/fibre.png"""
import base64, math, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "stories"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
LOGO = "data:image/png;base64," + base64.b64encode(open(f"{SRC}/brand/logo-mark.png", "rb").read()).decode()

def gauge():
    cx, cy, r = 400, 400, 300
    def arc(a0, a1, rr):
        p = lambda a: (cx + rr * math.cos(math.radians(a)), cy - rr * math.sin(math.radians(a)))
        (x0, y0), (x1, y1) = p(a0), p(a1)
        return f"M{x0:.1f} {y0:.1f} A{rr} {rr} 0 0 1 {x1:.1f} {y1:.1f}"
    ticks = "".join(
        f'<line x1="{cx + 250*math.cos(math.radians(a)):.1f}" y1="{cy - 250*math.sin(math.radians(a)):.1f}" '
        f'x2="{cx + 226*math.cos(math.radians(a)):.1f}" y2="{cy - 226*math.sin(math.radians(a)):.1f}" stroke="#12302C" stroke-width="6" stroke-linecap="round"/>'
        for a in range(180, -1, -30))
    na = 148  # needle angle: low
    nx, ny = cx + 220 * math.cos(math.radians(na)), cy - 220 * math.sin(math.radians(na))
    return f"""<svg viewBox="0 0 800 520" xmlns="http://www.w3.org/2000/svg">
 <path d="{arc(180, 0, r)}" fill="none" stroke="#FFFFFF" stroke-width="64" stroke-linecap="round"/>
 <path d="{arc(180, 120, r)}" fill="none" stroke="#E9A090" stroke-width="64" stroke-linecap="round"/>
 <path d="{arc(120, 60, r)}" fill="none" stroke="#F3C66B" stroke-width="64"/>
 <path d="{arc(60, 0, r)}" fill="none" stroke="#2E9C86" stroke-width="64" stroke-linecap="round"/>
 {ticks}
 <text x="100" y="510" text-anchor="middle" font-family="YS" font-size="54" fill="#B0362B">E</text>
 <text x="700" y="510" text-anchor="middle" font-family="YS" font-size="54" fill="#0D7466">F</text>
 <line x1="{cx}" y1="{cy}" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#12302C" stroke-width="16" stroke-linecap="round"/>
 <circle cx="{cx}" cy="{cy}" r="34" fill="#12302C"/><circle cx="{cx}" cy="{cy}" r="12" fill="#F3C66B"/>
</svg>"""

ICONS = {
 "Sprouts": '<path d="M20 80 h120 a60 48 0 0 1 -120 0 z" fill="#D7DEE0" stroke="#9AA6A9" stroke-width="5"/>' + "".join(f'<g transform="translate({x} {y}) rotate({r})"><ellipse rx="12" ry="8" fill="#9CCB5A"/><path d="M8 -2 q14 -10 18 -24" stroke="#F4F1D8" stroke-width="4" fill="none" stroke-linecap="round"/></g>' for x, y, r in [(50,74,10),(76,68,-20),(102,72,30),(124,78,-10),(62,90,-30),(90,88,15),(114,92,-5)]),
 "Guava": '<circle cx="80" cy="88" r="50" fill="#9CCB5A"/><circle cx="64" cy="72" r="14" fill="#C4E28C" opacity=".8"/><path d="M80 38 q2 -16 14 -22" stroke="#5B3A1E" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M86 36 q22 -14 32 4 q-20 8 -32 -4" fill="#4E9A32"/>',
 "Dal": '<circle cx="80" cy="84" r="58" fill="#D7DEE0" stroke="#9AA6A9" stroke-width="5"/><circle cx="80" cy="84" r="46" fill="#E8A92E"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="3.5" fill="#7A3B12"/>' for x, y in [(66,72),(92,70),(98,92),(70,98),(82,84)]),
 "Chokar roti": '<circle cx="80" cy="82" r="58" fill="#E3BE7B" stroke="#B88A45" stroke-width="4"/><g fill="#8E5A26" opacity=".65">' + "".join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in [(58,62),(70,50),(96,58),(106,78),(90,98),(64,100),(52,84),(80,74),(98,108),(74,114),(112,94),(46,70)]) + "</g>",
}
def icon(k): return f'<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">{ICONS[k]}</svg>'

HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:"FT",sans-serif;color:#12302C;
 background:radial-gradient(110% 70% at 50% 40%,#FFF6E4 0%,#FCEBD0 60%,#F6DDB4 100%)}}
.kick{{font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
h1{{font-family:"YS",serif;font-weight:400;line-height:1.02}}
em{{font-style:normal;color:#B0362B}}
</style></head><body>
 <div style="position:absolute;top:150px;left:80px;right:80px;text-align:center">
  <div class="kick" style="font-size:30px;color:#0D7466">Today's gut tip</div>
  <h1 style="font-size:112px;margin-top:22px">Is your gut<br>running on <em>empty?</em></h1>
 </div>
 <div style="position:absolute;top:600px;left:140px;width:800px">{gauge()}</div>
 <div style="position:absolute;top:1150px;left:80px;right:80px;text-align:center">
  <p style="font-size:40px;line-height:1.35">Most of us eat too little fibre.<br>Aim for <b style="font-family:YS;font-weight:400;font-size:56px;color:#0D7466">25–30 g</b> a day.</p>
 </div>
 <div style="position:absolute;top:1360px;left:60px;right:60px">
  <div class="kick" style="font-size:26px;color:#4A615D;text-align:center;margin-bottom:22px">Fill up with</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
   {''.join(f'<div style="background:#fff;border-radius:36px;padding:18px 10px 22px;text-align:center"><div style="width:150px;height:150px;margin:0 auto">{icon(k)}</div><div style="font-size:28px;font-weight:600;margin-top:6px">{k}</div></div>' for k in ICONS)}
  </div>
  <p style="font-size:28px;color:#4A615D;text-align:center;margin-top:22px">Add fibre slowly, and drink more water with it.</p>
 </div>
 <div style="position:absolute;left:80px;right:80px;bottom:70px;display:flex;align-items:center;gap:18px">
  <img src="{LOGO}" style="width:74px;height:74px">
  <div><b style="font-family:YS;font-weight:400;font-size:32px;display:block">Dr. Kshitij Lochab</b><span style="font-size:23px;color:#4A615D">Gastroenterologist · drlochab.com</span></div>
 </div>
</body></html>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1920})
        open(f"{OUT}/tmp.html", "w").write(HTML)
        pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(300); pg.screenshot(path=f"{OUT}/fibre.png"); b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done")
