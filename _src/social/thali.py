"""Figurative Instagram carousel + story: 'The gut-friendly plate' (an illustrated Indian thali).
Run from anywhere: python3 _src/social/thali.py  -> _src/out/thali/"""
import base64, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "thali"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = "data:image/png;base64," + b64(f"{SRC}/brand/logo-mark.png")

# ---------- the thali (viewBox 0 0 600 600) ----------
def thali(hl=None, labels=False):
    """hl: one of veg, protein, grain, curd, or None for everything at full strength."""
    op = lambda k: "1" if hl in (None, k) else "0.16"
    cuc = "".join(f'<g transform="translate({x} {y})"><circle r="22" fill="#5E9B4B"/><circle r="18" fill="#D9EDB8"/>'
                  f'<g fill="#F2F8E4">' + "".join(f'<ellipse cx="{dx}" cy="{dy}" rx="2.4" ry="4" transform="rotate({r} {dx} {dy})"/>' for dx, dy, r in [(0,-7,0),(6,4,60),(-6,4,-60)]) + "</g></g>"
                  for x, y in [(118,352),(150,392),(112,404),(178,428),(146,446)])
    tom = "".join(f'<path d="M{x} {y} a26 26 0 0 1 26 26 h-26 z" fill="#E0503D" transform="rotate({r} {x} {y})"/><circle cx="{x+9}" cy="{y+14}" r="2.4" fill="#F7D46B" transform="rotate({r} {x} {y})"/>'
                  for x, y, r in [(196,360,20),(206,404,140),(96,436,-40)])
    onion = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#C98BB9" stroke-width="3"/>' for x, y, r in [(172,470,16),(172,470,10)])
    peas = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="url(#pea)"/>' for x, y in
                   [(120,196),(138,184),(156,194),(176,184),(196,196),(212,212),(130,214),(150,212),(170,206),(190,216),(110,232),(130,236),(150,232),(172,230),(196,236),(214,240),(124,256),(146,258),(166,252),(188,258),(208,262),(140,276),(162,278),(184,280)])
    beans = "".join(f'<rect x="{x}" y="{y}" width="34" height="9" rx="4.5" fill="#3F8A3A" transform="rotate({r} {x} {y})"/>' for x, y, r in [(100,268,-20),(190,170,30),(212,276,-60),(96,206,50),(160,290,10)])
    carrot = "".join(f'<rect x="{x}" y="{y}" width="12" height="12" rx="2" fill="#F08A2C" transform="rotate({r} {x} {y})"/>' for x, y, r in [(132,224,15),(178,246,-20),(160,196,40),(118,248,5),(198,226,30)])
    paneer = "".join(f'<g transform="translate({x} {y}) rotate({r})"><rect x="-15" y="-15" width="30" height="30" rx="5" fill="#FBF3DF" stroke="#E8D6AE" stroke-width="2"/><path d="M-9 -6 l6 3 M2 6 l7 -2" stroke="#D9A85B" stroke-width="2.5" stroke-linecap="round"/></g>'
                     for x, y, r in [(452,236,12),(486,262,-18),(442,272,30)])
    roti_spots = lambda cx, cy: "".join(f'<ellipse cx="{cx+dx}" cy="{cy+dy}" rx="{a}" ry="{b}" fill="#B4793C" opacity=".55"/>' for dx, dy, a, b in [(-20,-14,7,4),(16,-22,5,3),(24,10,8,5),(-8,20,6,4),(-30,8,4,3),(4,-2,5,3)])
    rice = "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="2.2" fill="#FFFFFF" transform="rotate({r} {x} {y})"/>' for x, y, r in
                   [(456,438,20),(470,428,-30),(484,440,60),(462,452,-10),(478,456,40),(494,450,-50),(448,450,70),(470,444,0),(486,428,10),(500,438,-20),(458,426,-60),(474,466,30)])
    lbl = ""
    if labels:
        def pill(x, y, t, anchor="start"):
            w = 18 * len(t) + 34
            x0 = x if anchor == "start" else x - w
            return f'<g><rect x="{x0}" y="{y-26}" width="{w}" height="48" rx="24" fill="#12302C"/><text x="{x0 + w/2}" y="{y+7}" text-anchor="middle" font-family="FT" font-weight="600" font-size="26" fill="#fff">{t}</text></g>'
        lbl = pill(30, 120, "½ Vegetables") + pill(570, 120, "¼ Protein", "end") + pill(570, 560, "¼ Grains", "end") + pill(30, 560, "+ Curd")
    return f"""<svg viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
<defs>
 <radialGradient id="steel" cx="42%" cy="38%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#E4E9EA"/><stop offset="1" stop-color="#B9C3C6"/></radialGradient>
 <radialGradient id="rim" cx="50%" cy="50%" r="50%"><stop offset=".86" stop-color="#C8D0D2"/><stop offset=".93" stop-color="#F6F8F8"/><stop offset="1" stop-color="#9AA6A9"/></radialGradient>
 <radialGradient id="pea" cx="35%" cy="35%" r="70%"><stop offset="0" stop-color="#A8D86C"/><stop offset="1" stop-color="#4E9A32"/></radialGradient>
 <radialGradient id="dal" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#F6C44C"/><stop offset="1" stop-color="#DE9A22"/></radialGradient>
 <radialGradient id="roti" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#F1D49A"/><stop offset="1" stop-color="#D9AE68"/></radialGradient>
 <radialGradient id="curd" cx="40%" cy="35%" r="65%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EEF0EA"/></radialGradient>
 <filter id="sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#0B2A26" flood-opacity=".35"/></filter>
 <filter id="sh2"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0B2A26" flood-opacity=".25"/></filter>
</defs>
<circle cx="300" cy="300" r="276" fill="url(#rim)" filter="url(#sh)"/>
<circle cx="300" cy="300" r="246" fill="url(#steel)"/>
<path d="M300 58 V542 M300 300 H542" stroke="#C3CCCE" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>
<g opacity="{op('veg')}" filter="url(#sh2)">{beans}{peas}{carrot}{cuc}{tom}{onion}</g>
<g opacity="{op('protein')}" filter="url(#sh2)">
 <circle cx="390" cy="200" r="74" fill="#D7DEE0" stroke="#AEB9BC" stroke-width="4"/><circle cx="390" cy="200" r="60" fill="url(#dal)"/>
 <g fill="#7A3B12">{''.join(f'<circle cx="{x}" cy="{y}" r="2.6"/>' for x, y in [(372,186),(400,182),(410,206),(380,214),(392,198),(366,204)])}</g>
 <path d="M396 186 q8 -6 14 0" stroke="#3B7D2F" stroke-width="3" fill="none"/><ellipse cx="404" cy="214" rx="7" ry="3" fill="#C33A26"/>
 {paneer}
</g>
<g opacity="{op('grain')}" filter="url(#sh2)">
 <circle cx="388" cy="408" r="66" fill="url(#roti)" stroke="#C99A55" stroke-width="2"/>{roti_spots(388,408)}
 <circle cx="372" cy="388" r="66" fill="url(#roti)" stroke="#C99A55" stroke-width="2"/>{roti_spots(372,388)}
 <path d="M436 470 q36 -54 72 0 z" fill="#F4F2EA"/>{rice}
</g>
<g opacity="{op('curd')}" filter="url(#sh)">
 <circle cx="520" cy="96" r="62" fill="#D7DEE0" stroke="#AEB9BC" stroke-width="4"/><circle cx="520" cy="96" r="50" fill="url(#curd)"/>
 <path d="M496 90 q24 -14 48 4" stroke="#E2E5DD" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="532" cy="108" r="3" fill="#7A9A45"/><circle cx="510" cy="104" r="2.5" fill="#7A9A45"/>
</g>
{lbl}
</svg>"""

# ---------- simple swap icons (viewBox 0 0 160 160) ----------
ICON = {
 "bread": '<rect x="34" y="40" width="92" height="88" rx="14" fill="#F3E2BE" stroke="#C9A66A" stroke-width="6"/><path d="M34 62 a24 24 0 0 1 24 -26 h44 a24 24 0 0 1 24 26" fill="#E2BE7E" stroke="#C9A66A" stroke-width="6"/>',
 "roti": '<circle cx="80" cy="80" r="56" fill="#E9C786" stroke="#C99A55" stroke-width="4"/><g fill="#B4793C" opacity=".55"><ellipse cx="62" cy="66" rx="9" ry="5"/><ellipse cx="96" cy="60" rx="6" ry="4"/><ellipse cx="100" cy="94" rx="10" ry="6"/><ellipse cx="70" cy="102" rx="7" ry="4"/></g>',
 "juice": '<path d="M48 34 h64 l-8 96 a8 8 0 0 1 -8 7 h-32 a8 8 0 0 1 -8 -7 z" fill="#FFFFFF" stroke="#9AA6A9" stroke-width="5"/><path d="M53 64 h54 l-5 64 h-44 z" fill="#F59E2E"/><rect x="88" y="16" width="7" height="60" rx="3" fill="#E0503D" transform="rotate(12 92 46)"/>',
 "fruit": '<circle cx="80" cy="88" r="46" fill="#F28A2E"/><circle cx="66" cy="74" r="10" fill="#F9B867" opacity=".7"/><path d="M80 42 q4 -16 18 -20" stroke="#5B3A1E" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M84 40 q22 -16 34 2 q-22 10 -34 -2" fill="#4E9A32"/>',
 "samosa": '<path d="M80 26 L134 128 H26 Z" fill="#E1A64B" stroke="#B87A2A" stroke-width="6" stroke-linejoin="round"/><path d="M80 52 L110 112 M80 52 L50 112" stroke="#B87A2A" stroke-width="3" opacity=".5"/><g fill="#F6E27A" opacity=".8"><circle cx="70" cy="96" r="3"/><circle cx="94" cy="104" r="3"/><circle cx="82" cy="80" r="3"/></g>',
 "chana": '<path d="M24 82 h112 a56 46 0 0 1 -112 0 z" fill="#D7DEE0" stroke="#9AA6A9" stroke-width="5"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#C98A3E" stroke="#9C6420" stroke-width="2"/>' for x, y in [(50,78),(72,72),(94,74),(116,78),(62,90),(84,88),(106,90)]),
}
def icon(k): return f'<svg viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">{ICON[k]}</svg>'

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:"FT",sans-serif;overflow:hidden}}
.s{{position:relative;overflow:hidden;display:flex;flex-direction:column}}
.teal{{background:radial-gradient(120% 80% at 50% 30%,#0F7D6E 0%,#0B6A5E 45%,#084A42 100%);color:#fff}}
.cream{{background:#FBF5EA;color:#12302C}}
.mint{{background:#E6F2EF;color:#12302C}}
.saffron{{background:#FCEBD0;color:#12302C}}
h1{{font-family:"YS",serif;font-weight:400;line-height:1.02;letter-spacing:-.01em}}
h2{{font-family:"YS",serif;font-weight:400;line-height:1.06}}
em{{font-style:normal;color:#F3B84A}}
.cream em,.mint em,.saffron em{{color:#0D7466}}
.kick{{font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
.big{{font-family:"YS",serif;line-height:.9}}
.foot{{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:space-between}}
.brand{{display:flex;align-items:center;gap:16px}}
.brand b{{font-family:"YS",serif;font-weight:400;display:block}}
.dots{{display:flex;gap:10px}} .dots i{{width:12px;height:12px;border-radius:50%;background:currentColor;opacity:.25}} .dots i.on{{opacity:1}}
"""

def foot(n=None, total=6, light=False, pad=72, size=1):
    col = "#FFFFFF" if light else "#12302C"; sub = "#CFE5E0" if light else "#4A615D"
    d = "" if n is None else '<div class="dots" style="color:' + col + '">' + "".join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, total + 1)) + "</div>"
    return (f'<div class="foot" style="padding:0 {pad}px {int(56*size)}px"><div class="brand"><img src="{LOGO}" style="width:{int(64*size)}px;height:{int(64*size)}px">'
            f'<div><b style="font-size:{int(28*size)}px;color:{col}">Dr. Kshitij Lochab</b><span style="font-size:{int(20*size)}px;color:{sub}">Gastroenterologist · drlochab.com</span></div></div>{d}</div>')

def portion(n, bg, big, word, title, line, hl):
    return f"""<div class="s {bg}" style="width:1080px;height:1350px;padding:80px 72px">
 <div style="display:flex;align-items:flex-end;gap:28px">
   <div class="big" style="font-size:230px;color:#0D7466">{big}</div>
   <div style="padding-bottom:26px"><div class="kick" style="font-size:24px;color:#4A615D">of your plate</div><h2 style="font-size:76px">{word}</h2></div>
 </div>
 <div style="position:absolute;left:210px;top:350px;width:660px;height:660px">{thali(hl)}</div>
 <div style="position:absolute;left:72px;right:72px;bottom:190px">
   <h2 style="font-size:50px;margin-bottom:12px">{title}</h2><p style="font-size:34px;line-height:1.35;color:#4A615D;max-width:880px">{line}</p>
 </div>{foot(n)}</div>"""

SLIDES = [
 f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:26px;color:#9FD8CC">Save this for your next meal</div>
  <h1 style="font-size:118px;margin-top:22px">The gut-<br>friendly <em>thali</em></h1>
  <p style="font-size:36px;margin-top:22px;color:#CFE5E0;max-width:760px">One simple way to fill your plate for better digestion and a healthier liver.</p>
  <div style="position:absolute;left:250px;top:500px;width:764px;height:764px">{thali()}</div>
  {foot(1, light=True)}</div>""",
 portion(2, "mint", "½", "Vegetables", "Sabzi, salad, a little fruit", "Fibre keeps you regular and feeds the good bacteria in your gut.", "veg"),
 portion(3, "cream", "¼", "Protein", "Dal, paneer, eggs, fish or chicken", "Protein keeps you full for longer, so you snack less.", "protein"),
 portion(4, "saffron", "¼", "Grains", "Roti, millets or a little rice", "Choose atta with chokar, bajra or ragi over maida.", "grain"),
 f"""<div class="s cream" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:24px;color:#0D7466">3 easy swaps</div>
  <h2 style="font-size:84px;margin-top:14px">Small changes,<br><em>big difference</em></h2>
  <div style="margin-top:60px;display:flex;flex-direction:column;gap:40px">
   {''.join(f'''<div style="display:grid;grid-template-columns:190px 100px 190px 1fr;align-items:center;gap:12px;background:#fff;border-radius:40px;padding:26px 36px">
     <div style="width:180px;height:180px;opacity:.55">{icon(a)}</div>
     <svg viewBox="0 0 90 40" style="width:80px"><path d="M6 20 H74 M58 6 L78 20 L58 34" fill="none" stroke="#0D7466" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
     <div style="width:180px;height:180px">{icon(b)}</div>
     <div style="font-size:40px;line-height:1.25;padding-left:14px"><span style="color:#4A615D;text-decoration:line-through;text-decoration-color:#B0362B">{x}</span><br><b style="font-weight:600">{y}</b></div></div>''' for a, b, x, y in [("bread","roti","White bread","Atta roti"),("juice","fruit","Packaged juice","Whole fruit"),("samosa","chana","Fried snacks","Roasted chana")])}
  </div>{foot(5)}</div>""",
 f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
  <div style="position:absolute;right:-220px;top:-160px;width:760px;height:760px;opacity:.95">{thali()}</div>
  <div style="position:absolute;left:72px;right:72px;top:600px">
   <div class="kick" style="font-size:24px;color:#9FD8CC">A good plate is step one</div>
   <h2 style="font-size:72px;margin-top:16px">Acidity, fatty liver or bloating that won't settle?</h2>
   <p style="font-size:34px;margin-top:24px;color:#CFE5E0">Get it checked. Consultations at Arcura Clinic, Sector 51, Gurugram, and by video.</p>
   <div style="margin-top:36px;display:inline-flex;gap:16px;align-items:center;background:#F3B84A;color:#12302C;font-weight:600;font-size:34px;padding:20px 36px;border-radius:999px">WhatsApp +91 96671 04882</div>
  </div>{foot(6, light=True)}</div>""",
]

STORY = f"""<div class="s teal" style="width:1080px;height:1920px;padding:140px 80px">
 <div class="kick" style="font-size:30px;color:#9FD8CC;text-align:center">Quick check</div>
 <h1 style="font-size:100px;text-align:center;margin-top:22px">Does your plate<br>look like <em>this?</em></h1>
 <div style="position:absolute;left:170px;top:560px;width:740px;height:740px">{thali()}</div>
 <div style="position:absolute;left:80px;right:80px;top:1360px;display:grid;grid-template-columns:1fr 1fr;gap:18px">
  {''.join(f'<div style="display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.1);border-radius:999px;padding:18px 28px;font-size:38px;font-weight:600"><span style="font-family:YS;font-size:46px;color:#F3B84A;min-width:56px">{a}</span>{b}</div>' for a, b in [("½","Vegetables"),("¼","Protein"),("¼","Whole grains"),("+","Curd")])}
 </div>
 {foot(light=True, pad=80, size=1.15)}</div>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    def shot(html, w, h, path):
        pg = b.new_page(viewport={"width": w, "height": h})
        open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
        pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(300); pg.screenshot(path=path); pg.close()
    for i, s in enumerate(SLIDES, 1):
        shot(s, 1080, 1350, f"{OUT}/post-slide-{i}.png")
    shot(STORY, 1080, 1920, f"{OUT}/story.png")
    b.close()
os.remove(f"{OUT}/tmp.html")
print("done")
