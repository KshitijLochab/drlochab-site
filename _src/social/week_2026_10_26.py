"""Social content for the week of 26 Oct to 1 Nov 2026 (Karwa Chauth on Thu 29 Oct).
Instagram: "Myth or fact?" carousel (EN, Myth Buster entry of Mon 26 Oct: loose motions and antibiotics),
Karwa Chauth post (HI), indigestion carousel (EN, the week's new answer page).
Google Business Profile: indigestion (1200x900). WhatsApp Status: 3 images (1080x1920). Captions and messages as .txt.
Original drawings only. No doses, no brand names, no phone number in the Google post text.
Run from anywhere: python3 _src/social/week_2026_10_26.py  -> _src/out/week-2026-10-26/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, SRC, STOM
from new_tools_promo import phone
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-10-26"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/indigestion-heaviness-after-meals"

# ---------------- original drawings ----------------
def capsule(w=520, q=True):
    """A giant antibiotic capsule with a question mark (viewBox 0 0 520 520)."""
    qm = ('<g transform="translate(400 96)"><circle r="70" fill="#12302C"/><text x="0" y="34" text-anchor="middle" font-family="YS" font-size="104" fill="#F3B84A">?</text></g>' if q else "")
    return (f'<svg viewBox="0 0 520 520" style="width:{w}px;height:{w}px" xmlns="http://www.w3.org/2000/svg">'
            '<defs><filter id="cs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="16" stdDeviation="16" flood-color="#5A3A0A" flood-opacity=".3"/></filter></defs>'
            '<g transform="rotate(-38 260 280)" filter="url(#cs)">'
            '<rect x="60" y="200" width="400" height="160" rx="80" fill="#FFFFFF" stroke="#12302C" stroke-width="8"/>'
            '<path d="M260 200 H380 A80 80 0 0 1 380 360 H260 Z" fill="#E0503D" stroke="#12302C" stroke-width="8"/>'
            '<rect x="100" y="224" width="120" height="26" rx="13" fill="#FFFFFF" opacity=".0"/>'
            '<path d="M110 236 Q140 222 190 226" fill="none" stroke="#D3E0DC" stroke-width="12" stroke-linecap="round"/>'
            '<path d="M290 234 Q330 222 370 228" fill="none" stroke="#F49A8C" stroke-width="12" stroke-linecap="round"/></g>'
            + qm + "</svg>")

def virus(cx, cy, r, col="#6E9A3A", face=True):
    spikes = "".join(f'<g transform="rotate({a} {cx} {cy})"><path d="M{cx} {cy-r} V{cy-r-r*.45}" stroke="{col}" stroke-width="{r*.16}" stroke-linecap="round"/>'
                     f'<circle cx="{cx}" cy="{cy-r-r*.5}" r="{r*.14}" fill="{col}"/></g>' for a in range(0, 360, 45))
    f = (f'<circle cx="{cx-r*.32}" cy="{cy-r*.1}" r="{r*.1}" fill="#12302C"/><circle cx="{cx+r*.32}" cy="{cy-r*.1}" r="{r*.1}" fill="#12302C"/>'
         f'<path d="M{cx-r*.3} {cy+r*.3} Q{cx} {cy+r*.5} {cx+r*.3} {cy+r*.3}" fill="none" stroke="#12302C" stroke-width="{r*.08}" stroke-linecap="round"/>' if face else "")
    return f'{spikes}<circle cx="{cx}" cy="{cy}" r="{r}" fill="#AFD27E" stroke="{col}" stroke-width="{r*.12}"/>{f}'

def virus_shield(w=640):
    """A virus with an umbrella-like shield; antibiotic capsules bounce off it."""
    pills = "".join(f'<g transform="translate({x} {y}) rotate({a})"><rect x="-46" y="-18" width="92" height="36" rx="18" fill="#fff" stroke="#12302C" stroke-width="5"/>'
                    f'<path d="M0 -18 H28 A18 18 0 0 1 28 18 H0 Z" fill="#E0503D" stroke="#12302C" stroke-width="5"/></g>'
                    for x, y, a in [(110, 150, 30), (500, 120, -25), (540, 420, 60)])
    bounce = "".join(f'<path d="{d}" fill="none" stroke="#F3B84A" stroke-width="7" stroke-linecap="round" stroke-dasharray="2 16"/>' for d in
                     ["M170 190 Q230 250 250 300", "M450 160 Q400 230 390 280", "M480 400 Q440 380 420 360"])
    return (f'<svg viewBox="0 0 640 560" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">{bounce}{pills}{virus(320, 360, 110)}</svg>')

def ors_glass(w=300):
    return (f'<svg viewBox="0 0 200 240" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M40 30 H160 L146 220 Q145 230 134 230 H66 Q55 230 54 220 Z" fill="#FFFFFF" stroke="#0D7466" stroke-width="7" stroke-linejoin="round"/>'
            '<path d="M48 80 H152 L142 216 Q141 222 134 222 H66 Q59 222 58 216 Z" fill="#F7D48A"/>'
            '<path d="M60 104 q14 -8 28 0 t28 0 t28 0" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>'
            '<rect x="118" y="2" width="12" height="110" rx="6" fill="#E0503D" transform="rotate(14 124 60)"/>'
            '<g transform="translate(150 150) rotate(12)"><rect x="0" y="0" width="58" height="74" rx="8" fill="#0D7466"/><text x="29" y="46" text-anchor="middle" font-family="FT" font-weight="600" font-size="22" fill="#fff">ORS</text></g></svg>')

def bowl(w=200):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px" xmlns="http://www.w3.org/2000/svg"><path d="M6 30 H58 C58 46 46 56 32 56 C18 56 6 46 6 30 Z" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<path d="M10 30 C12 18 52 18 54 30 Z" fill="#F6E3A8"/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3.2" ry="1.7" fill="#E2C46E"/>' for x, y in [(20, 25), (28, 22), (36, 23), (44, 26), (32, 27), (24, 28)])
            + '<path d="M24 14 q-3 -5 0 -9 M32 13 q-3 -5 0 -9 M40 14 q-3 -5 0 -9" fill="none" stroke="#9FB8B2" stroke-width="2" stroke-linecap="round"/></svg>')

def cal3(w=200):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px" xmlns="http://www.w3.org/2000/svg"><rect x="6" y="12" width="52" height="46" rx="8" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<path d="M6 24 H58" stroke="#0D7466" stroke-width="3.5"/><rect x="17" y="6" width="5" height="12" rx="2.5" fill="#12302C"/><rect x="42" y="6" width="5" height="12" rx="2.5" fill="#12302C"/>'
            '<text x="32" y="50" text-anchor="middle" font-family="YS" font-size="22" fill="#0D7466">2–3</text></svg>')

def warn_icon(kind, w=120):
    """Small icons for the doctor slide: drop of blood, thermometer, glass (little urine), calendar."""
    body = dict(
        blood='<path d="M32 6 C44 24 52 34 52 42 A20 20 0 0 1 12 42 C12 34 20 24 32 6 Z" fill="#B0362B"/><path d="M22 42 a10 10 0 0 0 8 10" fill="none" stroke="#F8C9C2" stroke-width="4" stroke-linecap="round"/>',
        fever='<rect x="26" y="4" width="12" height="40" rx="6" fill="#fff" stroke="#12302C" stroke-width="3.5"/><circle cx="32" cy="48" r="11" fill="#B0362B" stroke="#12302C" stroke-width="3.5"/><rect x="29.5" y="18" width="5" height="28" fill="#B0362B"/>',
        dizzy='<circle cx="32" cy="32" r="24" fill="#fff" stroke="#12302C" stroke-width="3.5"/><path d="M32 32 m-4 0 a4 4 0 1 1 8 0 a8 8 0 1 1 -16 0 a12 12 0 1 1 24 0" fill="none" stroke="#B0362B" stroke-width="3.5" stroke-linecap="round"/>',
        days='<rect x="6" y="12" width="52" height="46" rx="8" fill="#fff" stroke="#12302C" stroke-width="3.5"/><path d="M6 24 H58" stroke="#12302C" stroke-width="3.5"/><text x="32" y="50" text-anchor="middle" font-family="YS" font-size="22" fill="#B0362B">3+</text>')[kind]
    return f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def heavy_stomach(w=560):
    """The stomach (same outline as the bloating balloon) dragged down by an iron weight (viewBox 0 0 600 700)."""
    return f"""<svg viewBox="0 0 600 700" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="hs" cx="38%" cy="34%" r="70%"><stop offset="0" stop-color="#FBD0C8"/><stop offset=".6" stop-color="#F4B6AE"/><stop offset="1" stop-color="#D9776B"/></radialGradient>
<filter id="hsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#062F2A" flood-opacity=".3"/></filter></defs>
<g transform="translate(0 20) rotate(8 300 300)">
<path d="M246 0 V60" stroke="#D9776B" stroke-width="40" stroke-linecap="round"/>
<g filter="url(#hsh)"><path d="{STOM}" fill="url(#hs)" stroke="#B0544A" stroke-width="6"/></g>
<ellipse cx="300" cy="250" rx="44" ry="20" fill="#FFFFFF" opacity=".5" transform="rotate(-30 300 250)"/>
<path d="M286 372 q24 -16 48 0" fill="none" stroke="#7A2E25" stroke-width="7" stroke-linecap="round"/>
<path d="M276 318 l18 8 M352 318 l-18 8" stroke="#7A2E25" stroke-width="7" stroke-linecap="round"/>
<path d="M300 470 V540" stroke="#12302C" stroke-width="7" stroke-dasharray="14 8"/></g>
<g transform="translate(234 548)"><path d="M18 0 H114 L132 112 Q134 128 118 128 H14 Q-2 128 0 112 Z" fill="#12302C"/>
<path d="M50 0 Q50 -34 66 -34 Q82 -34 82 0" fill="none" stroke="#12302C" stroke-width="12"/>
<text x="66" y="84" text-anchor="middle" font-family="YS" font-size="46" fill="#F3B84A">kg</text></g>
<path d="M120 690 H480" stroke="#0B6A5E" stroke-width="6" stroke-linecap="round" opacity=".35"/></svg>"""

def plate_small(w=150):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="34" r="24" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<circle cx="32" cy="34" r="14" fill="#E6F2EF"/><circle cx="27" cy="33" r="5" fill="#9CCB6B"/><circle cx="37" cy="36" r="4" fill="#F3B84A"/>'
            '<path d="M6 10 V24 M3 10 V18 Q3 22 6 22 Q9 22 9 18 V10" fill="none" stroke="#12302C" stroke-width="2.5" stroke-linecap="round"/></svg>')

def moon_clock(w=150):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="30" cy="36" r="22" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<path d="M30 22 V36 L39 41" fill="none" stroke="#12302C" stroke-width="3.5" stroke-linecap="round"/>'
            '<path d="M52 4 A11 11 0 1 0 60 20 A9 9 0 1 1 52 4 Z" fill="#F3B84A"/></svg>')

def no_pill(w=150):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#B0362B" stroke-width="4"/>'
            '<g transform="rotate(-35 32 32)"><rect x="14" y="24" width="36" height="16" rx="8" fill="#fff" stroke="#12302C" stroke-width="3"/><path d="M32 24 H42 A8 8 0 0 1 42 40 H32 Z" fill="#F3B84A" stroke="#12302C" stroke-width="3"/></g>'
            '<path d="M13 51 L51 13" stroke="#B0362B" stroke-width="4.5" stroke-linecap="round"/></svg>')

def karwa_night(w=820):
    """Karwa Chauth: crescent moon seen through a sieve (chalni), a clay karwa and a glass of water (viewBox 0 0 820 640)."""
    stars = "".join(f'<path d="M{x} {y-s} L{x+s*.3} {y-s*.3} L{x+s} {y} L{x+s*.3} {y+s*.3} L{x} {y+s} L{x-s*.3} {y+s*.3} L{x-s} {y} L{x-s*.3} {y-s*.3} Z" fill="#FFE6A8"/>'
                    for x, y, s in [(90, 80, 16), (720, 60, 12), (760, 230, 9), (140, 260, 10), (640, 300, 8)])
    mesh = "".join(f'<path d="M{150+i*26} 40 V340" stroke="#B9761A" stroke-width="2.5" opacity=".55"/><path d="M150 {40+i*26} H450" stroke="#B9761A" stroke-width="2.5" opacity=".55"/>' for i in range(12))
    return f"""<svg viewBox="0 0 820 640" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="sv"><circle cx="300" cy="190" r="130"/></clipPath>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFF4D6" stop-opacity=".9"/><stop offset="1" stop-color="#FFF4D6" stop-opacity="0"/></radialGradient></defs>
{stars}
<circle cx="300" cy="190" r="190" fill="url(#glow)"/>
<g clip-path="url(#sv)"><rect x="150" y="40" width="300" height="300" fill="#0E3E38"/>
<path d="M330 110 A84 84 0 1 0 380 250 A66 66 0 1 1 330 110 Z" fill="#FFE6A8"/>{mesh}</g>
<circle cx="300" cy="190" r="130" fill="none" stroke="#C9851F" stroke-width="22"/>
<circle cx="300" cy="190" r="143" fill="none" stroke="#8A5A12" stroke-width="5"/>
{"".join(f'<circle cx="{300+143*__import__("math").cos(a/8*6.2832):.1f}" cy="{190+143*__import__("math").sin(a/8*6.2832):.1f}" r="9" fill="#F3B84A" stroke="#8A5A12" stroke-width="3"/>' for a in range(8))}
<g transform="translate(470 330)">
 <path d="M60 40 Q20 60 22 140 Q26 220 130 226 Q234 220 238 140 Q240 60 200 40 Z" fill="#C8643C" stroke="#7A3A1E" stroke-width="7"/>
 <path d="M60 40 H200 V18 Q130 0 60 18 Z" fill="#B0532E" stroke="#7A3A1E" stroke-width="7" stroke-linejoin="round"/>
 <path d="M230 108 Q290 86 300 50" fill="none" stroke="#7A3A1E" stroke-width="22" stroke-linecap="round"/>
 <path d="M230 108 Q290 86 300 50" fill="none" stroke="#C8643C" stroke-width="12" stroke-linecap="round"/>
 <path d="M40 120 Q130 150 220 120" fill="none" stroke="#F3B84A" stroke-width="10"/>
 {"".join(f'<circle cx="{x}" cy="{136+((x-60)//40)%2*6}" r="7" fill="#FFFFFF"/>' for x in range(60, 210, 30))}
 <path d="M70 180 Q130 200 190 180" fill="none" stroke="#7A3A1E" stroke-width="5" opacity=".6"/></g>
<g transform="translate(150 410)">
 <path d="M0 0 H120 L108 196 Q107 206 96 206 H24 Q13 206 12 196 Z" fill="#FFFFFF" fill-opacity=".9" stroke="#CFE5E0" stroke-width="7" stroke-linejoin="round"/>
 <path d="M8 54 H112 L104 196 Q103 200 96 200 H24 Q17 200 16 196 Z" fill="#9BD3EA"/>
 <path d="M24 80 q12 -8 24 0 t24 0 t24 0" fill="none" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/></g>
<g transform="translate(330 560)"><path d="M0 20 Q60 60 120 20 Q60 34 0 20 Z" fill="#C8643C" stroke="#7A3A1E" stroke-width="5"/>
 <path d="M60 22 C44 -6 56 -24 60 -34 C64 -24 76 -6 60 22 Z" fill="#F3B84A"/><path d="M60 16 C54 4 58 -6 60 -12 C62 -6 66 4 60 16 Z" fill="#FFF4D6"/></g>
</svg>"""

# ---------------- Instagram 1: Myth or fact? (EN, 5 slides) ----------------
N1 = 5
def m1(n=1):
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:28px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px;max-width:900px">Loose motions need <em>antibiotics.</em></h1>
 <div style="position:absolute;left:240px;top:520px">{capsule(600)}</div>
 <div style="position:absolute;left:84px;top:1110px;font-size:34px;font-weight:600;color:#B5542C">Guess first, then swipe →</div>
 {foot(n, total=N1)}</div>"""

def m2(n=2):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;border:8px solid #F3B84A;color:#F3B84A;border-radius:22px;padding:6px 36px;transform:rotate(-6deg);font-family:YS;font-size:120px;line-height:1.1">MYTH</div>
 <h1 style="font-size:78px;margin-top:46px;max-width:920px">Most loose motions settle <em>without antibiotics.</em></h1>
 <div style="position:absolute;left:220px;top:560px">{virus_shield(640)}</div>
 <p style="position:absolute;left:84px;right:84px;top:1110px;font-size:34px;line-height:1.35;color:#DCEFEA">Most are caused by viruses. Antibiotics can't kill viruses.</p>
 {foot(n, total=N1, light=True)}</div>"""

def m3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:26px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:52px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What to do instead</div>
 <h2 style="font-size:84px;margin:14px 0 44px">Fluids, food, <em>time</em></h2>
 <div style="display:grid;gap:24px">
  {row(ors_glass(150), "ORS", "after every loose stool")}
  {row(bowl(170), "Light home food", "khichdi, curd rice, banana, dal")}
  {row(cal3(160), "2 to 3 days", "most bouts settle on their own")}
 </div>
 {foot(n, total=N1)}</div>"""

def m4(n=4):
    item = lambda k, t: f'<div style="display:flex;align-items:center;gap:30px;font-size:40px;line-height:1.25">{warn_icon(k, 110)}<span>{t}</span></div>'
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor if</div>
 <h2 style="font-size:84px;margin:14px 0 50px">When it's <em>more than a bug</em></h2>
 <div style="display:grid;gap:34px">{item("blood", "Blood in the stool")}{item("fever", "High fever")}{item("dizzy", "Very little urine, or dizziness")}{item("days", "It lasts more than 3 days")}</div>
 <p style="font-size:32px;line-height:1.35;margin-top:46px">Older people, small children and pregnant women need care sooner. <b>Very unwell? Call 112.</b></p>
 {foot(n, total=N1)}</div>"""

def mb_screen():
    return ('<div style="font-size:15px;font-weight:600;letter-spacing:.12em;color:#0D7466">MYTH BUSTER · NEW</div>'
            '<div style="font-family:YS;font-size:30px;color:#12302C;line-height:1.15;margin:14px 0 18px">A normal ultrasound means my stomach is fine.</div>'
            '<div style="display:flex;gap:10px"><span style="flex:1;text-align:center;background:#0D7466;color:#fff;border-radius:999px;padding:12px;font-size:20px;font-weight:600">Myth</span>'
            '<span style="flex:1;text-align:center;background:#fff;border:2px solid #0D7466;color:#0D7466;border-radius:999px;padding:12px;font-size:20px;font-weight:600">Fact</span></div>'
            '<div style="margin-top:26px;display:flex;gap:8px;justify-content:center">' + "".join(f'<i style="width:12px;height:12px;border-radius:50%;background:{"#0D7466" if i == 0 else "#CFE0DC"}"></i>' for i in range(8)) + '</div>'
            '<div style="margin-top:26px;background:#FAEED8;border-radius:18px;padding:16px;font-size:18px;color:#12302C">New myth every Monday and Thursday</div>')

def m5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">Your turn</div>
 <h1 style="font-size:92px;margin-top:18px;max-width:560px">Play more <em>Myth or fact?</em></h1>
 <p style="font-size:36px;line-height:1.35;color:#DCEFEA;margin-top:30px;max-width:520px">A new one every Monday and Thursday. Guess, then see the answer.</p>
 <div style="display:inline-block;margin-top:56px;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
 <p style="font-size:28px;color:#CFE5E0;margin-top:24px;max-width:520px">English and हिंदी · free</p>
 <div style="position:absolute;right:84px;top:300px">{phone(mb_screen(), w=380, tilt=5)}</div>
 {foot(n, total=N1, light=True)}</div>"""

# ---------------- Instagram 2: Karwa Chauth (HI, single post) ----------------
KC = ["सरगी: दही, फल, मेवे, कम तला", "व्रत खोलें: पहले पानी के घूँट, फिर हल्का खाना", "डायबिटीज़, गर्भावस्था या पेट की बीमारी? पहले डॉक्टर से पूछें"]

def kc_chips(size, gap, w=None):
    return "".join(f'<div style="display:flex;align-items:center;gap:20px;background:rgba(255,255,255,.1);border-radius:26px;padding:16px 26px;font-size:{size}px;line-height:1.3;margin-bottom:{gap}px">'
                   f'<span style="flex:none;width:52px;height:52px;border-radius:50%;background:#F3B84A;color:#12302C;font-family:YS;font-size:30px;display:grid;place-items:center">{i}</span>{t}</div>'
                   for i, t in enumerate(KC, 1))

def kc_post():
    return f"""<div class="s teal hi" style="width:1080px;height:1350px;padding:70px 72px;background:radial-gradient(120% 80% at 50% 25%,#13574F 0%,#0B3F39 55%,#072B27 100%)">
 <div class="kick" style="font-size:30px;color:#F3B84A;text-align:center">करवा चौथ · 29 अक्टूबर</div>
 <h1 style="font-size:82px;margin-top:8px;text-align:center">व्रत खोलें <em>आराम से</em></h1>
 <div style="position:absolute;left:150px;top:250px">{karwa_night(780)}</div>
 <div style="position:absolute;left:72px;right:72px;top:860px">{kc_chips(34, 14)}</div>
 {foot(light=True, hi=True)}</div>"""

# ---------------- Instagram 3: Indigestion (EN, 5 slides) ----------------
N3 = 5
def d1(n=1):
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Indigestion</div>
 <h1 style="font-size:104px;margin-top:16px;max-width:620px">Heavy after <em>every meal?</em></h1>
 <p style="font-size:36px;line-height:1.35;color:#4A615D;margin-top:28px;max-width:470px">Full after a few bites, burning above the navel, lots of burping?</p>
 <div style="position:absolute;right:40px;top:400px">{heavy_stomach(560)}</div>
 {foot(n, total=N3)}</div>"""

def d2(n=2):
    causes = [("Sensitive stomach", "the commonest cause: no damage, but it feels more"), ("H. pylori", "a stomach infection, found with a simple test"),
              ("Painkillers or alcohol", "can cause gastritis or an ulcer")]
    rows = "".join(f'<div style="background:rgba(255,255,255,.1);border-radius:28px;padding:24px 30px"><div style="font-family:YS;font-size:46px;color:#F3B84A">{a}</div>'
                   f'<div style="font-size:30px;color:#DCEFEA;margin-top:6px;line-height:1.3">{b}</div></div>' for a, b in causes)
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">Good news first</div>
 <h2 style="font-size:80px;margin:14px 0 40px">Most often, <em>nothing serious</em> is found</h2>
 <div style="display:grid;gap:20px">{rows}</div>
 <p style="font-size:30px;line-height:1.35;color:#CFE5E0;margin-top:30px">Doctors call the first one functional dyspepsia. It is real, and it is treatable.</p>
 {foot(n, total=N3, light=True)}</div>"""

def d3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:24px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:50px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What helps</div>
 <h2 style="font-size:84px;margin:14px 0 44px">Lighten the <em>load</em></h2>
 <div style="display:grid;gap:24px">
  {row(plate_small(140), "Smaller meals", "at regular times; don't skip breakfast")}
  {row(moon_clock(140), "Early dinner", "2 to 3 hours before you lie down")}
  {row(no_pill(140), "Fewer painkillers", "ask your doctor for a safer option")}
 </div>
 <p style="font-size:30px;line-height:1.35;color:#4A615D;margin-top:34px">Less fried food, alcohol and smoking. Better sleep helps too.</p>
 {foot(n, total=N3)}</div>"""

def d4(n=4):
    signs = ["Weight loss without trying", "Repeated vomiting", "Black stools or anaemia", "Difficulty swallowing", "New indigestion after 45 to 50"]
    li = "".join(f'<div style="display:flex;gap:22px;align-items:center;font-size:40px;line-height:1.25;margin-top:22px"><span style="flex:none;width:22px;height:22px;border-radius:50%;background:#B0362B"></span>{s}</div>' for s in signs)
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">Don't wait if you have</div>
 <h2 style="font-size:84px;margin:14px 0 26px">These need an <em>endoscopy</em></h2>
 {li}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Sudden severe belly pain, or chest pain with sweating? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N3)}</div>"""

def d5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on the website</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:900px">Indigestion and heaviness after meals: <em>the full answer</em></h1>
 <p style="font-size:34px;line-height:1.4;color:#DCEFEA;margin-top:30px;max-width:880px">Causes, tests, what to eat, and when to see a doctor. In English and हिंदी.</p>
 <div style="position:absolute;right:40px;top:640px;opacity:.95">{heavy_stomach(360)}</div>
 <div style="position:absolute;left:84px;top:820px">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
  <p style="font-size:28px;color:#CFE5E0;margin-top:22px">Link in bio · Answers · Indigestion</p></div>
 {foot(n, total=N3, light=True)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:76px 80px">
 <div class="kick" style="font-size:26px;color:#0D7466">Indigestion</div>
 <h1 style="font-size:82px;margin-top:14px;max-width:640px">Heavy after <em>every meal?</em></h1>
 <p style="font-size:32px;line-height:1.35;color:#4A615D;margin-top:24px;max-width:580px">Usually treatable. Know the causes, what helps, and the warning signs that need a check-up.</p>
 <div style="position:absolute;right:70px;top:90px">{heavy_stomach(420)}</div>
 {foot(pad=80)}</div>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_myth():
    return f"""<div class="s saffron" style="width:1080px;height:1920px;padding:150px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:30px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px">Loose motions need <em>antibiotics.</em></h1>
 <div style="position:absolute;left:200px;top:640px">{capsule(560, q=False)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1180px">
  <div style="display:inline-block;border:7px solid #B0362B;color:#B0362B;border-radius:20px;padding:4px 30px;transform:rotate(-5deg);font-family:YS;font-size:88px">MYTH</div>
  <p style="font-size:42px;line-height:1.35;margin-top:30px">Most are viral. Drink <b>ORS</b> after every loose stool, eat light home food, give it 2 to 3 days.</p>
  <p style="font-size:32px;line-height:1.35;margin-top:22px;color:#4A615D">Blood in stool, high fever or very little urine? See a doctor.</p></div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Play more at drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_karwa():
    return f"""<div class="s teal hi" style="width:1080px;height:1920px;padding:150px 72px;background:radial-gradient(120% 80% at 50% 25%,#13574F 0%,#0B3F39 55%,#072B27 100%)">
 <div class="kick" style="font-size:34px;color:#F3B84A;text-align:center">करवा चौथ · 29 अक्टूबर</div>
 <h1 style="font-size:100px;margin-top:14px;text-align:center">व्रत खोलें <em>आराम से</em></h1>
 <div style="position:absolute;left:110px;top:420px">{karwa_night(860)}</div>
 <div style="position:absolute;left:72px;right:72px;top:1130px">{kc_chips(40, 18)}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#F3B84A;color:#12302C;font-family:YS;font-size:60px;padding:14px 44px;border-radius:999px">drlochab.com/hi</span></div>
 {foot(light=True, pad=72, hi=True)}</div>"""

def st_indig():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">Indigestion</div>
 <h1 style="font-size:112px;margin-top:16px">Heavy after <em>every meal?</em></h1>
 <div style="position:absolute;left:250px;top:560px">{heavy_stomach(580)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1290px;display:grid;gap:16px">
  {"".join(f'<div style="background:#fff;border-radius:999px;padding:18px 32px;font-size:38px;display:flex;gap:18px;align-items:center"><span style="width:18px;height:18px;border-radius:50%;background:#0D7466;flex:none"></span>{t}</div>' for t in ("Smaller, regular meals", "Dinner 2 to 3 hours before bed", "Weight loss or vomiting? Get checked"))}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Read more: drlochab.com</span></div>
 {foot(pad=84)}</div>"""

# ---------------- text ----------------
CAP_MYTH = """Myth or fact? "Loose motions need antibiotics." 💊

Guess first, then swipe 👉

❌ MYTH. Most loose motions are caused by viruses, and antibiotics cannot kill viruses. Antibiotics you don't need can upset your gut bacteria and cause side effects of their own.

What to do instead:
🥤 ORS after every loose stool
🍚 Keep eating light home food: khichdi, curd rice, banana, dal
⏳ Give it 2 to 3 days

See a doctor for blood in the stool, high fever, very little urine or dizziness, or if it lasts more than 3 days. Older people, small children and pregnant women need care sooner. Very unwell? Call 112.

🎮 A new Myth or fact? goes up every Monday and Thursday on my website. Play them all at drlochab.com (link in bio), in English and Hindi.

#MythOrFact #LooseMotions #Diarrhoea #ORS #AntibioticResistance #GutHealth #Gastroenterologist #Gurugram"""

CAP_KC = """करवा चौथ (गुरुवार, 29 अक्टूबर): व्रत खोलें आराम से 🌙

निर्जला व्रत के बाद पेट ख़ाली और नाज़ुक होता है। तीन आसान बातें:

1️⃣ सरगी में: दही, फल, मेवे, और कम तला खाना। बहुत मीठा या बहुत तला खाने से दिन में एसिडिटी और प्यास बढ़ती है।
2️⃣ चाँद देखने के बाद: पहले पानी के कुछ घूँट, फिर हल्का खाना, जैसे दाल-चावल, खिचड़ी या रोटी-सब्ज़ी। एक साथ भारी, तला खाना न खाएँ।
3️⃣ डायबिटीज़, गर्भावस्था, अल्सर, किडनी की बीमारी या पेट की कोई बीमारी हो, तो व्रत से पहले डॉक्टर से पूछें। चक्कर, बेहोशी या बहुत कमज़ोरी लगे तो व्रत तोड़ दें।

व्रत में पेट हल्का रखने की पूरी गाइड (हिंदी): drlochab.com/hi/guides/navratri-fasting-guide (लिंक बायो में)

सभी को करवा चौथ की शुभकामनाएँ 🪔

#करवाचौथ #KarwaChauth #व्रत #एसिडिटी #पेटकीसेहत #GutHealth #Gurugram #DrLochab"""

CAP_INDIG = """Heavy after every meal? You're not alone. 🍽️

Indigestion (dyspepsia) means heaviness after meals, feeling full after a few bites, or burning above the navel, often with nausea or burping.

✅ The good news: most often, no serious cause is found. A sensitive stomach (functional dyspepsia) is the commonest reason. H. pylori infection, and gastritis or ulcers from painkillers or alcohol, are other causes.

What helps:
🥣 Smaller meals at regular times, without skipping breakfast
🌙 Dinner 2 to 3 hours before you lie down
💊 Avoid painkillers you don't need, and ask your doctor for a safer option
😴 Less fried food, alcohol and smoking; better sleep and less stress

🚩 Don't wait for weight loss, repeated vomiting, black stools, anaemia, difficulty swallowing, or indigestion that starts after 45 to 50. These need an endoscopy. Sudden severe belly pain, or chest pain with sweating, is an emergency: call 112.

📖 New on my website: the full answer, with what to eat and common questions, in English and Hindi. drlochab.com/answers/indigestion-heaviness-after-meals (link in bio)

#Indigestion #Dyspepsia #Acidity #GutHealth #DigestiveHealth #Gastroenterologist #Gurugram #DrLochab"""

GBP_TEXT = """Heavy after every meal? Feeling full after a few bites, or burning above the navel?

This is indigestion (dyspepsia), and it is very common. Most often no serious cause is found: a sensitive stomach is the usual reason, and it is treatable. H. pylori infection and gastritis or ulcers from painkillers or alcohol are other causes.

What helps: smaller meals at regular times, dinner 2 to 3 hours before lying down, less fried food, alcohol and smoking, and avoiding painkillers you do not need.

See a doctor soon for weight loss, repeated vomiting, black stools, anaemia, difficulty swallowing, or indigestion that starts after 45 to 50, as these need an endoscopy. Sudden severe belly pain or chest pain with sweating is an emergency: call 112.

Read the full answer, with a diet guide and common questions, in English and Hindi.

Button: Learn more → https://drlochab.com/answers/indigestion-heaviness-after-meals/"""

WA_EN = """🍽️ *Heavy after every meal?*

Indigestion (heaviness, early fullness, burning above the navel) is very common, and most often nothing serious is found. I've written a short, plain answer on the causes, the tests, what to eat, and the warning signs that need a check-up:

👉 https://drlochab.com/answers/indigestion-heaviness-after-meals/
हिंदी में: https://drlochab.com/hi/answers/indigestion-heaviness-after-meals/

Please share it with anyone who keeps reaching for a digestive churan.
– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)"""

WA_HI = """🍽️ *हर बार खाने के बाद पेट भारी?*

बदहज़मी (भारीपन, जल्दी पेट भरना, नाभि के ऊपर जलन) बहुत आम है, और ज़्यादातर कोई गंभीर वजह नहीं मिलती। वजहें, जाँचें, क्या खाएँ, और कब जाँच ज़रूरी है, यह सब आसान भाषा में यहाँ पढ़ें:

👉 https://drlochab.com/hi/answers/indigestion-heaviness-after-meals/

जो रोज़ चूर्ण लेते हैं, उनके साथ ज़रूर शेयर करें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, गुरुग्राम (drlochab.com/hi)"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([m1, m2, m3, m4, m5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig1-myth-{i}.png", b)
        render(kc_post, 1080, 1350, f"{OUT}/ig2-karwa-chauth-hi.png", b)
        for i, f in enumerate([d1, d2, d3, d4, d5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig3-indigestion-{i}.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business-indigestion.png", b)
        render(st_myth, 1080, 1920, f"{OUT}/wa-status-1-myth.png", b)
        render(st_karwa, 1080, 1920, f"{OUT}/wa-status-2-karwa-chauth-hi.png", b)
        render(st_indig, 1080, 1920, f"{OUT}/wa-status-3-indigestion.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("ig1-caption.txt", CAP_MYTH), ("ig2-caption-hi.txt", CAP_KC), ("ig3-caption.txt", CAP_INDIG),
                      ("google-business-post.txt", GBP_TEXT), ("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
