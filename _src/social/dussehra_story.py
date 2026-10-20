"""Dussehra 2026 (20 Oct) greeting story for Instagram and WhatsApp, 1080x1920, EN and HI.
Original drawing: bow with a flaming arrow, a burning effigy silhouette, fireworks and a marigold toran.
Run: python3 _src/social/dussehra_story.py -> _src/out/dussehra-2026/"""
import os, sys, math, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "dussehra-2026"); os.makedirs(OUT, exist_ok=True)

def toran():
    """Marigold garland swags with mango leaves across the top (viewBox 0 0 1080 260)."""
    out = []
    for k in range(4):
        x0, x1 = k * 270, (k + 1) * 270
        for i in range(15):
            t = i / 14
            x = x0 + (x1 - x0) * t
            y = 40 + 90 * math.sin(math.pi * t)
            col = ["#F28C1E", "#F9B233", "#E8641B"][i % 3]
            out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="17" fill="{col}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="7" fill="#C2410C" opacity=".55"/>')
        for x in (x0 + 90, x0 + 180):
            out.append(f'<path d="M{x} 128 c-14 30 -10 60 0 80 c10 -20 14 -50 0 -80z" fill="#3F8A3A"/><path d="M{x} 132 v72" stroke="#2C6A2A" stroke-width="2"/>')
    beads = "".join(f'<circle cx="{x}" cy="34" r="9" fill="#F9B233"/>' for x in range(0, 1081, 30))
    return f'<svg viewBox="0 0 1080 260" style="position:absolute;left:0;top:0;width:1080px">{beads}{"".join(out)}</svg>'

def burst(cx, cy, r, col):
    rays = "".join(f'<line x1="{cx + r*.3*math.cos(a):.0f}" y1="{cy + r*.3*math.sin(a):.0f}" x2="{cx + r*math.cos(a):.0f}" y2="{cy + r*math.sin(a):.0f}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
                   for a in [i * math.pi / 8 for i in range(16)])
    dots = "".join(f'<circle cx="{cx + r*1.12*math.cos(a):.0f}" cy="{cy + r*1.12*math.sin(a):.0f}" r="6" fill="{col}"/>' for a in [i * math.pi / 8 + .2 for i in range(16)])
    return f'<g opacity=".9">{rays}{dots}</g>'

def scene():
    """Burning effigy, bow and flaming arrow (viewBox 0 0 1080 900)."""
    random.seed(7)
    sparks = "".join(f'<circle cx="{random.randint(560, 960)}" cy="{random.randint(80, 520)}" r="{random.choice([3,4,5])}" fill="#FFD36B" opacity="{random.choice([.5,.7,.9])}"/>' for _ in range(40))
    flame = lambda x, y, s: (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0 C-60 -40 -50 -120 -10 -170 C-20 -110 20 -100 10 -160 C60 -110 70 -40 0 0Z" fill="#F28C1E"/>'
                             '<path d="M0 -6 C-34 -30 -30 -80 -6 -112 C-8 -76 16 -70 8 -104 C40 -74 40 -30 0 -6Z" fill="#FFD36B"/></g>')
    effigy = ('<g transform="translate(760 640)">'
              '<rect x="-70" y="-260" width="140" height="300" rx="20" fill="#3A1D2E"/>'
              '<path d="M-70 -200 L-150 -80 M70 -200 L150 -80" stroke="#3A1D2E" stroke-width="36" stroke-linecap="round"/>'
              '<rect x="-48" y="-360" width="96" height="104" rx="30" fill="#3A1D2E"/>'
              + "".join(f'<rect x="{dx-30}" y="-350" width="60" height="70" rx="22" fill="#4A2638"/>' for dx in (-120, -190, 120, 190)) +
              '<path d="M-56 -360 L-40 -420 L-16 -380 L0 -440 L16 -380 L40 -420 L56 -360Z" fill="#F3B84A"/>'
              '<path d="M-70 40 L-50 240 M70 40 L50 240" stroke="#3A1D2E" stroke-width="40" stroke-linecap="round"/></g>')
    flames = flame(700, 700, 1.1) + flame(820, 690, 1.3) + flame(760, 470, .9) + flame(640, 520, .7) + flame(880, 520, .75)
    bow = ('<g transform="translate(300 560) rotate(-8)">'
           '<path d="M-20 -300 C140 -200 140 200 -20 300" fill="none" stroke="#F3B84A" stroke-width="22" stroke-linecap="round"/>'
           '<path d="M-20 -300 C140 -200 140 200 -20 300" fill="none" stroke="#C98A2A" stroke-width="6" stroke-linecap="round" opacity=".6"/>'
           '<path d="M-20 -300 L-20 300" stroke="#FFF1C2" stroke-width="4"/>'
           '<path d="M-60 0 L330 0" stroke="#FFF1C2" stroke-width="8" stroke-linecap="round"/>'
           '<path d="M330 -20 L380 0 L330 20Z" fill="#F3B84A"/>'
           '<path d="M-60 0 l-30 -18 M-60 0 l-30 18 M-44 0 l-30 -18 M-44 0 l-30 18" stroke="#E8641B" stroke-width="6" stroke-linecap="round"/>'
           '<g transform="translate(390 0) rotate(90)"><path d="M0 0 C-22 -16 -20 -50 -4 -70 C-6 -46 10 -44 6 -66 C26 -46 28 -16 0 0Z" fill="#FFD36B"/></g></g>')
    ground = '<path d="M0 860 C300 820 780 820 1080 860 L1080 900 L0 900Z" fill="#2A1422"/>'
    glow = '<ellipse cx="760" cy="560" rx="360" ry="300" fill="#F28C1E" opacity=".18"/>'
    fw = burst(170, 110, 80, '#F9B233') + burst(470, 60, 52, '#FFD36B') + burst(990, 120, 64, '#F28C1E')
    return f'<svg viewBox="0 0 1080 900" style="width:1080px;height:780px;display:block">{fw}{glow}{sparks}{effigy}{flames}{bow}{ground}</svg>'

def story(hi=False):
    bg = "radial-gradient(90% 60% at 70% 62%,#7A2E2A 0%,#4A1C2E 45%,#1E1430 100%)"
    title = "शुभ दशहरा" if hi else "Happy<br>Dussehra"
    line = "बुराई पर अच्छाई की जीत का पर्व" if hi else "The victory of good over evil"
    tip_h = "इस त्योहार, अच्छी आदतों की जीत हो" if hi else "This festive season, let good habits win too"
    tips = (["मिठाई थोड़ी, खाने के बाद", "दावत के बाद 15 मिनट टहलें", "रात का खाना जल्दी, पानी भरपूर"] if hi else
            ["Mithai in small portions, after a meal", "A 15-minute walk after the feast", "An early dinner and plenty of water"])
    cls = "s hi" if hi else "s"
    tip_html = "".join(f'<div style="display:flex;gap:14px;align-items:center;font-size:32px;line-height:1.3"><span style="flex:none;width:16px;height:16px;border-radius:50%;background:#F9B233"></span>{t}</div>' for t in tips)
    return f"""<div class="{cls}" style="width:1080px;height:1920px;background:{bg};color:#fff">
 {toran()}
 <div style="position:absolute;left:84px;right:84px;top:300px">
  <div class="kick" style="font-size:30px;color:#F9B233">{"दशहरा 2026" if hi else "Dussehra 2026"}</div>
  <h1 style="font-size:{170 if hi else 160}px;margin-top:10px;color:#FFF1C2">{title}</h1>
  <div style="font-size:44px;color:#F6D9C7;margin-top:18px">{line}</div>
 </div>
 <div style="position:absolute;left:0;top:{690 if hi else 760}px">{scene()}</div>
 <div style="position:absolute;left:60px;right:60px;top:1520px;background:rgba(30,20,48,.72);border:2px solid rgba(249,178,51,.5);border-radius:32px;padding:24px 34px;display:flex;flex-direction:column;gap:10px">
  <div style="font-family:{'TD' if hi else 'YS'},serif;font-size:38px;color:#F9B233;line-height:1.2">{tip_h}</div>{tip_html}
 </div>
 {foot(None, light=True, pad=84, size=1.0, hi=hi)}</div>"""

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for hi in (False, True):
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            tmp = f"{OUT}/tmp.html"
            open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{story(hi)}</body></html>")
            pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500)
            name = f"{OUT}/dussehra-story-{'hi' if hi else 'en'}"
            pg.screenshot(path=name + ".png"); pg.close()
            Image.open(name + ".png").convert("RGB").save(name + ".jpg", quality=92)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done")
