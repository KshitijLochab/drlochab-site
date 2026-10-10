"""Social content for the week of 12 Oct 2026 (Navratri week), in the visual-first brand style.
Instagram: gas and bloating carousel (EN), Navratri vrat post (HI), hepatitis B post (EN).
Google Business Profile: gas and bloating (1200x900). WhatsApp Status: 3 images (1080x1920).
Run from anywhere: python3 _src/social/week_2026_10_12.py  -> _src/out/week-2026-10-12/"""
import base64, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "week-2026-10-12"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = "data:image/png;base64," + b64(f"{SRC}/brand/logo-mark.png")

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
@font-face{{font-family:"MK";src:url("file://{F}/Mukta-400.woff2");font-weight:400}}
@font-face{{font-family:"MK";src:url("file://{F}/Mukta-600.woff2");font-weight:600}}
@font-face{{font-family:"TD";src:url("file://{F}/TiroDevanagariHindi.woff2")}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:"FT",sans-serif;overflow:hidden}}
.s{{position:relative;overflow:hidden}}
.teal{{background:radial-gradient(120% 80% at 50% 30%,#0F7D6E 0%,#0B6A5E 45%,#084A42 100%);color:#fff}}
.cream{{background:#FBF5EA;color:#12302C}}
.mint{{background:#E6F2EF;color:#12302C}}
.saffron{{background:#FCEBD0;color:#12302C}}
.rose{{background:#F8E4E1;color:#12302C}}
h1{{font-family:"YS",serif;font-weight:400;line-height:1.04;letter-spacing:-.01em}}
h2{{font-family:"YS",serif;font-weight:400;line-height:1.08}}
em{{font-style:normal;color:#F3B84A}}
.cream em,.mint em,.saffron em{{color:#0D7466}} .rose em{{color:#B0362B}}
.kick{{font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
.big{{font-family:"YS",serif;line-height:.9}}
.hi{{font-family:"MK","FT",sans-serif}} .hi h1,.hi h2{{font-family:"TD","YS",serif;line-height:1.25;letter-spacing:0}} .hi .kick{{letter-spacing:.02em}}
.foot{{position:absolute;left:0;right:0;bottom:0;display:flex;align-items:center;justify-content:space-between}}
.brand{{display:flex;align-items:center;gap:16px}}
.brand b{{font-family:"YS",serif;font-weight:400;display:block}}
.hi .brand b{{font-family:"TD","YS",serif}}
.dots{{display:flex;gap:10px}} .dots i{{width:12px;height:12px;border-radius:50%;background:currentColor;opacity:.25}} .dots i.on{{opacity:1}}
.chip{{display:flex;align-items:center;gap:20px;border-radius:999px;padding:20px 32px;font-weight:600}}
"""

def foot(n=None, total=5, light=False, pad=72, size=1, hi=False):
    col = "#FFFFFF" if light else "#12302C"; sub = "#CFE5E0" if light else "#4A615D"
    d = "" if n is None else '<div class="dots" style="color:' + col + '">' + "".join(f'<i class="{"on" if i == n else ""}"></i>' for i in range(1, total + 1)) + "</div>"
    name = "डॉ. क्षितिज लोचब" if hi else "Dr. Kshitij Lochab"
    role = "गैस्ट्रोएंटेरोलॉजिस्ट · drlochab.com/hi" if hi else "Gastroenterologist · drlochab.com"
    return (f'<div class="foot" style="padding:0 {pad}px {int(56*size)}px"><div class="brand"><img src="{LOGO}" style="width:{int(64*size)}px;height:{int(64*size)}px">'
            f'<div><b style="font-size:{int(28*size)}px;color:{col}">{name}</b><span style="font-size:{int(20*size)}px;color:{sub}">{role}</span></div></div>{d}</div>')

# ---------- original drawings ----------
STOM = "M228 70 C228 40 286 40 286 72 L286 128 C286 168 360 150 420 196 C496 254 498 392 410 446 C330 496 206 470 178 380 C162 326 196 292 224 250 C236 230 228 200 228 160 Z"

def balloon(puffs=True):
    """The stomach as an over-filled balloon (viewBox 0 0 600 640)."""
    pf = ""
    if puffs:
        pf = "".join(f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-width="9" stroke-linecap="round" opacity=".85"/>' for d in
                     ["M520 210 q26 -14 44 4", "M532 270 q30 -6 46 14", "M118 300 q-30 -12 -48 6", "M110 360 q-32 0 -46 20", "M500 140 q16 -26 40 -24"])
    return f"""<svg viewBox="0 0 600 640" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="bl" cx="38%" cy="34%" r="70%"><stop offset="0" stop-color="#FFD98A"/><stop offset=".6" stop-color="#F3B84A"/><stop offset="1" stop-color="#D99223"/></radialGradient>
<filter id="bs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#062F2A" flood-opacity=".35"/></filter></defs>
<path d="M300 482 C296 530 330 556 312 596 C302 616 318 630 330 636" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".9"/>
<g filter="url(#bs)"><path d="{STOM}" fill="url(#bl)" stroke="#B9761A" stroke-width="5"/></g>
<path d="M288 470 l12 18 l14 -20 z" fill="#D99223" stroke="#B9761A" stroke-width="4" stroke-linejoin="round"/>
<ellipse cx="300" cy="250" rx="46" ry="22" fill="#FFFFFF" opacity=".55" transform="rotate(-30 300 250)"/>
<ellipse cx="262" cy="296" rx="12" ry="8" fill="#FFFFFF" opacity=".5"/>
<path d="M300 360 q20 18 40 0" fill="none" stroke="#8A5A12" stroke-width="7" stroke-linecap="round"/>
<circle cx="296" cy="320" r="7" fill="#8A5A12"/><circle cx="350" cy="320" r="7" fill="#8A5A12"/>
{pf}</svg>"""

ICON = dict(
 fizzy="""<path d="M44 40 H116 L106 146 H54 Z" fill="#E8F4F1" stroke="#0D7466" stroke-width="5" stroke-linejoin="round"/>
  <path d="M50 70 H110 L104 140 H56 Z" fill="#B5482F" opacity=".85"/>
  <path d="M92 40 L112 8" stroke="#E0503D" stroke-width="7" stroke-linecap="round"/>
  """ + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#FFFFFF" stroke-width="3"/>' for x, y, r in [(70,120,5),(88,104,4),(78,90,6),(96,128,4),(66,96,3),(92,80,3)]),
 clock="""<circle cx="80" cy="84" r="58" fill="#FFFFFF" stroke="#0D7466" stroke-width="6"/>
  <path d="M80 50 V84 L104 98" fill="none" stroke="#12302C" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M60 18 h40" stroke="#0D7466" stroke-width="8" stroke-linecap="round"/>""",
 rajma="""<path d="M18 78 H142 C140 120 114 146 80 146 C46 146 20 120 18 78 Z" fill="#FFFFFF" stroke="#0D7466" stroke-width="5"/>
  """ + "".join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="8" fill="#8E2A22" transform="rotate({r} {x} {y})"/><ellipse cx="{x-3}" cy="{y-3}" rx="4" ry="2" fill="#C8584A" transform="rotate({r} {x} {y})"/>'
                for x, y, r in [(40,72,20),(62,66,-15),(86,70,30),(110,66,-20),(126,74,10),(52,82,-30),(98,80,15),(74,80,40)]),
 cabbage="""<circle cx="130.0" cy="84.0" r="24" fill="#5E9B4B"/><circle cx="115.36941345835999" cy="119.3412590552683" r="24" fill="#5E9B4B"/><circle cx="80.03981633553666" cy="133.99998414659171" r="24" fill="#5E9B4B"/><circle cx="44.68691775899974" cy="119.39754543242161" r="24" fill="#5E9B4B"/><circle cx="30.000063413623025" cy="84.07963264582435" r="24" fill="#5E9B4B"/><circle cx="44.57434504038636" cy="48.71511696657616" r="24" fill="#5E9B4B"/><circle cx="79.88055109438592" cy="34.000142680614104" r="24" fill="#5E9B4B"/><circle cx="115.25666145042115" cy="48.54625797788916" r="24" fill="#5E9B4B"/><circle cx="80" cy="84" r="54" fill="#9CCB6B"/><path d="M80 30 C60 60 60 110 80 140 M80 30 C100 60 100 110 80 140 M30 70 C55 80 60 110 52 132 M130 70 C105 80 100 110 108 132" fill="none" stroke="#DCEFC2" stroke-width="5" stroke-linecap="round"/>""",
 walk="""<circle cx="88" cy="26" r="15" fill="#12302C"/>
  <path d="M84 46 L72 92 M78 60 L52 78 M80 58 L106 76 M72 92 L50 140 M72 92 L100 112 L96 146" fill="none" stroke="#12302C" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M20 152 H140" stroke="#0D7466" stroke-width="5" stroke-linecap="round"/>""",
 water="""<path d="M48 30 H112 L104 146 H56 Z" fill="#E8F4F1" stroke="#0D7466" stroke-width="5" stroke-linejoin="round"/><path d="M52 62 H108 L102 140 H58 Z" fill="#9BD3EA"/><path d="M64 80 q8 -6 16 0 t16 0" fill="none" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>""",
)
def icon(k, w=180): return f'<svg viewBox="0 0 160 160" style="width:{w}px;height:{w}px" xmlns="http://www.w3.org/2000/svg">{ICON[k]}</svg>'

def vrat_thali():
    """Navratri vrat plate (viewBox 0 0 600 600): makhana, fruit, curd, sabudana khichdi, with marigolds and a diya."""
    makhana = "".join(f'<circle cx="{x}" cy="{y}" r="15" fill="#FFF9EE" stroke="#E2D2B4" stroke-width="2"/><circle cx="{x+4}" cy="{y+4}" r="4" fill="#C9A77A" opacity=".6"/>' for x, y in
                      [(150,180),(178,166),(204,180),(164,206),(192,204),(218,206),(140,226),(176,232),(206,232),(160,254),(192,256)])
    sabu = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#FBF6EA" stroke="#E7DCC4" stroke-width="1.5"/>' for x, y in
                   [(400,180),(414,170),(428,182),(442,172),(456,186),(408,196),(424,200),(440,194),(456,206),(470,196),(398,214),(416,220),(432,216),(450,222),(466,216),(412,238),(430,240),(448,240),(462,234),(426,258),(444,258)])
    nuts = "".join(f'<ellipse cx="{x}" cy="{y}" rx="9" ry="6" fill="#C98A4A" transform="rotate({r} {x} {y})"/>' for x, y, r in [(420,188,20),(452,212,-30),(410,226,60),(440,250,10),(470,226,-10)])
    leaves = "".join(f'<ellipse cx="{x}" cy="{y}" rx="12" ry="5" fill="#3F8A3A" transform="rotate({r} {x} {y})"/>' for x, y, r in [(434,176,-20),(462,244,40),(400,204,70)])
    banana = '<path d="M150 380 C180 470 290 480 330 430 C300 450 220 450 176 372 Z" fill="#F7D046" stroke="#C9A21F" stroke-width="4" stroke-linejoin="round"/><path d="M150 380 l-10 -12" stroke="#7A5A1A" stroke-width="7" stroke-linecap="round"/>'
    apple = "".join(f'<g transform="translate({x} {y}) rotate({r})"><path d="M-34 0 A34 34 0 0 1 34 0 Z" fill="#FFF3D9" stroke="#D2372C" stroke-width="7"/><circle cx="-8" cy="-12" r="3" fill="#5A3A1A"/><circle cx="8" cy="-12" r="3" fill="#5A3A1A"/></g>'
                    for x, y, r in [(232,330,-10),(270,350,20)])
    curd = '<circle cx="430" cy="410" r="74" fill="#C8D0D2"/><circle cx="430" cy="410" r="62" fill="url(#vcurd)"/><path d="M398 400 q16 -14 32 0 t32 0" fill="none" stroke="#E2E6DE" stroke-width="5" stroke-linecap="round"/><circle cx="446" cy="388" r="6" fill="#3F8A3A"/>'
    marigold = lambda x, y, s: f'<g transform="translate({x} {y}) scale({s})">' + "".join(f'<circle cx="{14*__import__("math").cos(a/6*3.1416)}" cy="{14*__import__("math").sin(a/6*3.1416)}" r="12" fill="#F28C1E"/>' for a in range(12)) + '<circle r="14" fill="#F9B233"/><circle r="6" fill="#E46F10"/></g>'
    diya = '<g transform="translate(520 520)"><path d="M-54 0 C-40 34 40 34 54 0 Z" fill="#B5542C" stroke="#8A3A1A" stroke-width="4"/><path d="M-54 0 H54" stroke="#8A3A1A" stroke-width="5" stroke-linecap="round"/><path d="M0 -6 C-14 -26 -6 -46 0 -60 C6 -46 14 -26 0 -6 Z" fill="#F9B233"/><path d="M0 -10 C-6 -22 -2 -34 0 -42 C2 -34 6 -22 0 -10 Z" fill="#FFF1C2"/></g>'
    return f"""<svg viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
<defs>
 <radialGradient id="vsteel" cx="42%" cy="38%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#E4E9EA"/><stop offset="1" stop-color="#B9C3C6"/></radialGradient>
 <radialGradient id="vrim" cx="50%" cy="50%" r="50%"><stop offset=".86" stop-color="#C8D0D2"/><stop offset=".93" stop-color="#F6F8F8"/><stop offset="1" stop-color="#9AA6A9"/></radialGradient>
 <radialGradient id="vcurd" cx="40%" cy="35%" r="65%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#EEF0EA"/></radialGradient>
 <filter id="vsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#0B2A26" flood-opacity=".3"/></filter>
</defs>
<g filter="url(#vsh)"><circle cx="300" cy="300" r="262" fill="url(#vrim)"/></g>
<circle cx="300" cy="300" r="236" fill="url(#vsteel)"/>
<circle cx="180" cy="216" r="86" fill="#C8D0D2"/><circle cx="180" cy="216" r="74" fill="#F3EEE2"/>{makhana}
<circle cx="432" cy="214" r="86" fill="#C8D0D2"/><circle cx="432" cy="214" r="74" fill="#F6E7C4"/>{sabu}{nuts}{leaves}
{banana}{apple}{curd}
{marigold(70,80,1.2)}{marigold(530,70,1)}{marigold(60,520,1)}{diya}
</svg>"""

def shield():
    """Hepatitis B: a shield guarding the liver (viewBox 0 0 600 600)."""
    liver = "M28 114 C32 90 96 80 130 96 C126 104 120 108 114 112 C112 134 92 152 62 154 C40 156 24 138 28 114 Z"
    return f"""<svg viewBox="0 0 600 600" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#17A08C"/><stop offset="1" stop-color="#0B6A5E"/></linearGradient>
<filter id="ss" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#062F2A" flood-opacity=".3"/></filter></defs>
<g filter="url(#ss)"><path d="M300 40 L510 110 V280 C510 420 410 510 300 560 C190 510 90 420 90 280 V110 Z" fill="url(#sg)" stroke="#FFFFFF" stroke-width="14" stroke-linejoin="round"/></g>
<path d="M300 78 L478 138 V282 C478 400 396 478 300 522" fill="none" stroke="#FFFFFF" stroke-width="4" opacity=".35"/>
<g transform="translate(110 92) scale(2.6)"><path d="{liver}" fill="#E7A58E" stroke="#B8604A" stroke-width="1.6"/><ellipse cx="66" cy="110" rx="14" ry="6" fill="#FFFFFF" opacity=".4" transform="rotate(-12 66 110)"/></g>
<g transform="translate(420 430)"><circle r="62" fill="#F3B84A" stroke="#FFFFFF" stroke-width="10"/><path d="M-28 2 L-8 22 L30 -20" fill="none" stroke="#12302C" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></g>
</svg>"""

# ---------- Instagram 1: gas and bloating carousel (5 slides, English) ----------
def cause(n, bg, num, title, line, icons):
    ic = "".join(f'<div style="width:300px;height:300px;background:#FFFFFF;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(11,42,38,.10)">{icon(k, 210)}</div>' for k in icons)
    return f"""<div class="s {bg}" style="width:1080px;height:1350px;padding:84px 72px">
 <div style="display:flex;align-items:flex-end;gap:28px"><div class="big" style="font-size:220px;color:#0D7466">{num}</div>
  <div style="padding-bottom:30px"><div class="kick" style="font-size:24px;color:#4A615D">Common cause</div><h2 style="font-size:84px">{title}</h2></div></div>
 <div style="position:absolute;left:0;right:0;top:420px;display:flex;justify-content:center;gap:56px">{ic}</div>
 <div style="position:absolute;left:72px;right:72px;top:820px"><p style="font-size:48px;line-height:1.3;max-width:900px">{line}</p></div>
 {foot(n)}</div>"""

GAS = [
 f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:26px;color:#9FD8CC">Gas &amp; bloating</div>
  <h1 style="font-size:116px;margin-top:22px">Feel like a<br><em>balloon</em><br>after meals?</h1>
  <div style="position:absolute;right:30px;top:500px;width:560px;height:597px">{balloon()}</div>
  <p style="position:absolute;left:72px;top:1000px;font-size:38px;color:#CFE5E0;max-width:500px">Usually harmless. Here is what causes it.</p>
  {foot(1, light=True)}</div>""",
 cause(2, "mint", "1", "Swallowed air", "Eating fast and fizzy drinks fill you with air. <b style='font-weight:600'>Eat slowly.</b>", ["clock", "fizzy"]),
 cause(3, "cream", "2", "Gassy foods", "Rajma, chana, cabbage, onion. <b style='font-weight:600'>Find your own triggers</b> with a 1-week food diary.", ["rajma", "cabbage"]),
 cause(4, "saffron", "3", "Constipation", "Hard stool traps gas. <b style='font-weight:600'>Water, slow fibre and a walk</b> after meals help.", ["water", "walk"]),
 f"""<div class="s rose" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:24px;color:#B0362B">Not just gas if there is</div>
  <h2 style="font-size:88px;margin-top:14px">See a doctor<br>for <em>these signs</em></h2>
  <div style="margin-top:70px;display:grid;grid-template-columns:1fr 1fr;gap:26px">
   {''.join(f'<div class="chip" style="background:#FFFFFF;font-size:44px;padding:40px 36px;border-radius:36px"><span style="width:22px;height:22px;border-radius:50%;background:#B0362B;flex:none"></span>{t}</div>' for t in ["Weight loss", "Vomiting", "Blood or black stool", "A belly that keeps growing"])}
  </div>
  <p style="margin-top:70px;font-size:42px;line-height:1.35;color:#12302C"><b style="font-weight:600">Severe pain with a hard belly?</b> Call 112 or go to the nearest emergency department.</p>
  <div style="margin-top:60px;display:inline-block;background:#0D7466;color:#fff;font-weight:600;font-size:32px;padding:22px 36px;border-radius:999px">Read: drlochab.com/answers/gas-and-bloating</div>
  {foot(5)}</div>""",
]

# ---------- Instagram 2: Navratri vrat (Hindi, single post) ----------
VRAT_TIPS_HI = [("🍳", "तला कम, भुना ज़्यादा"), ("⏱", "हर 3–4 घंटे में थोड़ा खाएँ"), ("💧", "पानी, छाछ, नारियल पानी")]
def vrat_chips(size=40, gap=20):
    marks = ["1", "2", "3"]
    return "".join(f'<div class="chip" style="background:#FFFFFF;color:#12302C;font-size:{size}px;margin-bottom:{gap}px;padding:14px 32px"><span style="font-family:YS;color:#0D7466;font-size:{size+6}px;min-width:36px">{m}</span>{t}</div>'
                   for m, (_, t) in zip(marks, VRAT_TIPS_HI))

VRAT_POST = f"""<div class="s saffron hi" style="width:1080px;height:1350px;padding:76px 72px">
 <div class="kick" style="font-size:30px;color:#B5542C;text-align:center">नवरात्रि व्रत</div>
 <h1 style="font-size:88px;margin-top:4px;text-align:center">व्रत में भी पेट रहे <em>हल्का</em></h1>
 <div style="position:absolute;left:290px;top:270px;width:500px;height:500px">{vrat_thali()}</div>
 <div style="position:absolute;left:150px;right:150px;top:800px">{vrat_chips(38, 14)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1135px;font-size:32px;line-height:1.35;color:#4A615D;text-align:center">डायबिटीज़, प्रेगनेंसी या पेट की बीमारी है? <b style="font-weight:600;color:#12302C">व्रत से पहले डॉक्टर से पूछें।</b></p>
 {foot(hi=True)}</div>"""

# ---------- Instagram 3: hepatitis B (English, single post) ----------
HEPB_POST = f"""<div class="s mint" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:26px;color:#0D7466">Protect your liver</div>
 <h1 style="font-size:100px;margin-top:18px">Hepatitis B is<br><em>preventable</em></h1>
 <div style="position:absolute;left:290px;top:400px;width:500px;height:500px">{shield()}</div>
 <div style="position:absolute;left:72px;right:72px;top:940px;display:grid;grid-template-columns:1fr 1fr;gap:22px">
  <div class="chip" style="background:#FFFFFF;font-size:36px;border-radius:36px;padding:28px 32px;align-items:flex-start;flex-direction:column;gap:6px"><span class="kick" style="font-size:20px;color:#0D7466">Step 1</span>One blood test<br>(HBsAg)</div>
  <div class="chip" style="background:#FFFFFF;font-size:36px;border-radius:36px;padding:28px 32px;align-items:flex-start;flex-direction:column;gap:6px"><span class="kick" style="font-size:20px;color:#0D7466">Step 2</span>Negative? Get<br>the vaccine</div>
 </div>
 {foot()}</div>"""

# ---------- Google Business Profile (1200x900) ----------
GBP = f"""<div class="s teal" style="width:1200px;height:900px;padding:80px 72px">
 <div class="kick" style="font-size:24px;color:#9FD8CC">Gas &amp; bloating</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:640px">Common, usually harmless, <em>sometimes worth a check</em></h1>
 <p style="font-size:30px;margin-top:26px;color:#CFE5E0;max-width:560px">Causes, simple fixes and the warning signs, on drlochab.com</p>
 <div style="position:absolute;right:30px;top:60px;width:500px;height:533px">{balloon()}</div>
 {foot(light=True, pad=72, size=1.05)}</div>"""

# ---------- WhatsApp Status (1080x1920) ----------
WA = [
 ("status-1-gas", f"""<div class="s teal" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:30px;color:#9FD8CC;text-align:center">Bloated after meals?</div>
  <h1 style="font-size:104px;text-align:center;margin-top:22px">3 quick <em>fixes</em></h1>
  <div style="position:absolute;left:190px;top:480px;width:700px;height:747px">{balloon()}</div>
  <div style="position:absolute;left:80px;right:80px;top:1230px;display:flex;flex-direction:column;gap:20px">
   {''.join(f'<div class="chip" style="background:rgba(255,255,255,.12);font-size:44px"><span style="font-family:YS;color:#F3B84A;font-size:50px;min-width:44px">{n}</span>{t}</div>' for n, t in [("1","Eat slowly"),("2","Skip fizzy drinks"),("3","Walk 15 minutes after meals")])}
  </div>
  <div style="position:absolute;left:0;right:0;top:1640px;text-align:center;font-size:34px;color:#CFE5E0">More: drlochab.com/answers/gas-and-bloating</div>
  {foot(light=True, pad=80, size=1.15)}</div>"""),
 ("status-2-navratri-hi", f"""<div class="s saffron hi" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:36px;color:#B5542C;text-align:center">नवरात्रि व्रत</div>
  <h1 style="font-size:104px;text-align:center;margin-top:16px">पेट रहे <em>हल्का</em></h1>
  <div style="position:absolute;left:170px;top:480px;width:740px;height:740px">{vrat_thali()}</div>
  <div style="position:absolute;left:150px;right:150px;top:1290px">{vrat_chips(44, 20)}</div>
  {foot(pad=80, size=1.15, hi=True)}</div>"""),
 ("status-3-hepatitis-b", f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:30px;color:#0D7466;text-align:center">Protect your liver</div>
  <h1 style="font-size:100px;text-align:center;margin-top:22px">Know your<br><em>hepatitis B</em> status</h1>
  <div style="position:absolute;left:240px;top:620px;width:600px;height:600px">{shield()}</div>
  <div style="position:absolute;left:80px;right:80px;top:1300px;display:flex;flex-direction:column;gap:20px">
   {''.join(f'<div class="chip" style="background:#FFFFFF;font-size:44px"><span style="font-family:YS;color:#0D7466;font-size:50px;min-width:44px">{n}</span>{t}</div>' for n, t in [("1","One blood test (HBsAg)"),("2","Negative? Get vaccinated")])}
  </div>
  <div style="position:absolute;left:0;right:0;top:1580px;text-align:center;font-size:32px;color:#4A615D">drlochab.com/conditions/hepatitis-b-c</div>
  {foot(pad=80, size=1.15)}</div>"""),
]

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html, w, h, path):
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()
        for i, s in enumerate(GAS, 1):
            shot(s, 1080, 1350, f"{OUT}/ig1-gas-bloating-slide-{i}.png")
        shot(VRAT_POST, 1080, 1350, f"{OUT}/ig2-navratri-vrat-hi.png")
        shot(HEPB_POST, 1080, 1350, f"{OUT}/ig3-hepatitis-b.png")
        shot(GBP, 1200, 900, f"{OUT}/gbp-gas-bloating.png")
        for name, s in WA:
            shot(s, 1080, 1920, f"{OUT}/wa-{name}.png")
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
