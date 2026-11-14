"""Social content for the week of 16 to 22 Nov 2026 (World Toilet Day Thu 19 Nov, Dev Uthani Ekadashi Fri 20 Nov,
Tulsi Vivah Sat 21 Nov and the start of the wedding season).
Instagram: "Myth or fact?" carousel (EN, Myth Buster entry of Mon 16 Nov: piles always need an operation),
undigested food in stool carousel (EN, the week's new answer page, for World Toilet Day), Dev Uthani Ekadashi post (HI).
Google Business Profile: undigested food in stool (1200x900). WhatsApp Status: 3 images (1080x1920). Captions and messages as .txt.
Original drawings only. No doses, no brand names, no phone number in the Google post text.
Run from anywhere: python3 _src/social/week_2026_11_16.py  -> _src/out/week-2026-11-16/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC
from week_2026_11_02 import dot_list
from week_2026_11_09 import clock_small, glass_between, render
from new_tools_promo import phone
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-11-16"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/undigested-food-in-stool"
ANS_HI = "drlochab.com/hi/answers/undigested-food-in-stool"
MYTH_LINK = "drlochab.com/answers/piles-fissure-fistula"
WED_HI = "drlochab.com/hi/guides/winter-wedding-season-guide"
SIGN = ("Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Fellowship in EUS and ERCP), Gurugram. "
        "HMC Reg. No. HN-23524. Prepared with AI assistance and reviewed by Dr. Lochab.")
SIGN_HI = ("डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP फ़ेलोशिप), गुरुग्राम। "
           "HMC रजि. नं. HN-23524। AI की सहायता से तैयार और डॉ. लोचब द्वारा समीक्षित।")

# ---------------- original drawings ----------------
def toilet_scalpel(w=600, q=True, cross=False):
    """A toilet with a surgeon's scalpel hovering over it and a question mark (viewBox 0 0 600 640)."""
    qm = ('<g transform="translate(480 120)"><circle r="62" fill="#12302C"/><text x="0" y="31" text-anchor="middle" font-family="YS" font-size="92" fill="#F3B84A">?</text></g>' if q else "")
    cr = ('<path d="M150 70 L470 330" stroke="#B0362B" stroke-width="22" stroke-linecap="round"/>' if cross else "")
    return f"""<svg viewBox="0 0 600 640" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="por" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCE7E4"/></linearGradient>
<filter id="ts" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#12302C" flood-opacity=".22"/></filter></defs>
<ellipse cx="300" cy="610" rx="220" ry="22" fill="#12302C" opacity=".12"/>
<g filter="url(#ts)">
<rect x="170" y="300" width="260" height="120" rx="22" fill="url(#por)" stroke="#9FB8B2" stroke-width="6"/>
<rect x="196" y="282" width="208" height="28" rx="12" fill="#fff" stroke="#9FB8B2" stroke-width="6"/>
<path d="M120 420 H480 C480 500 420 540 360 548 L380 600 H220 L240 548 C180 540 120 500 120 420 Z" fill="url(#por)" stroke="#9FB8B2" stroke-width="6" stroke-linejoin="round"/>
<rect x="104" y="404" width="392" height="34" rx="17" fill="#0D7466"/>
<circle cx="408" cy="340" r="12" fill="#C9D9D5"/></g>
<g transform="translate(300 170) rotate(-28)">
<rect x="-30" y="-14" width="200" height="28" rx="10" fill="#7C8C88"/><rect x="-30" y="-14" width="200" height="10" rx="5" fill="#A7B5B1"/>
<path d="M-30 -10 L-180 -4 C-200 -2 -206 10 -186 14 L-30 14 Z" fill="#E9EEED" stroke="#7C8C88" stroke-width="5" stroke-linejoin="round"/>
<path d="M-60 -6 L-170 -2" stroke="#fff" stroke-width="5" stroke-linecap="round"/></g>
{cr}{qm}</svg>"""

def corn_mag(w=600):
    """A corn cob with one loose kernel under a magnifying glass (viewBox 0 0 600 600)."""
    k = ""
    for r in range(9):
        for c in range(5):
            x = 150 + c * 34 + (17 if r % 2 else 0); y = 140 + r * 40
            if x < 300:
                k += f'<ellipse cx="{x}" cy="{y}" rx="16" ry="18" fill="#F6C93E" stroke="#C9921A" stroke-width="3"/><ellipse cx="{x-5}" cy="{y-6}" rx="5" ry="6" fill="#FFF1B0"/>'
    return f"""<svg viewBox="0 0 600 600" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="cs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#12302C" flood-opacity=".25"/></filter>
<clipPath id="lens"><circle cx="420" cy="380" r="104"/></clipPath></defs>
<g filter="url(#cs)" transform="rotate(-14 230 320)">
<path d="M150 520 C80 460 70 300 120 160 L150 520 Z" fill="#8DBE5A" stroke="#5E8B3A" stroke-width="5"/>
<path d="M310 520 C380 460 380 300 330 170 L310 520 Z" fill="#A8D06E" stroke="#5E8B3A" stroke-width="5"/>
<rect x="130" y="110" width="190" height="420" rx="95" fill="#E9B23A"/>
{k}
<path d="M230 530 C220 560 236 580 256 590" stroke="#5E8B3A" stroke-width="10" fill="none" stroke-linecap="round"/></g>
<g filter="url(#cs)">
<circle cx="420" cy="380" r="104" fill="#E6F2EF"/>
<g clip-path="url(#lens)"><g transform="translate(420 380) scale(3.2)"><ellipse rx="16" ry="18" fill="#F6C93E" stroke="#C9921A" stroke-width="2"/><ellipse cx="-5" cy="-6" rx="5" ry="6" fill="#FFF1B0"/>
<path d="M-12 10 Q0 22 12 10" stroke="#C9921A" stroke-width="2" fill="none"/></g></g>
<circle cx="420" cy="380" r="104" fill="none" stroke="#12302C" stroke-width="18"/>
<path d="M494 454 L566 526" stroke="#12302C" stroke-width="34" stroke-linecap="round"/>
<path d="M360 320 A76 76 0 0 1 410 300" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" opacity=".8"/></g>
</svg>"""

def mini(kind, w=120):
    """Small food icons whose skins or seeds pass whole (viewBox 0 0 140 140)."""
    body = dict(
        corn='<rect x="46" y="14" width="48" height="112" rx="24" fill="#E9B23A"/>' +
             "".join(f'<ellipse cx="{58+c*12+(6 if r%2 else 0)}" cy="{28+r*14}" rx="6" ry="7" fill="#F6C93E" stroke="#C9921A" stroke-width="1.5"/>' for r in range(7) for c in range(3) if 58+c*12+(6 if r%2 else 0) < 88) +
             '<path d="M46 120 C20 100 18 60 34 30 L46 120 Z" fill="#8DBE5A"/>',
        peas='<path d="M14 84 C30 40 100 30 128 52 C110 92 50 108 14 84 Z" fill="#8DBE5A" stroke="#5E8B3A" stroke-width="4"/>' +
             "".join(f'<circle cx="{x}" cy="{y}" r="13" fill="#B5DB7A" stroke="#5E8B3A" stroke-width="3"/>' for x, y in [(42, 76), (70, 68), (98, 60)]),
        tomato='<circle cx="70" cy="74" r="50" fill="#E0503D" stroke="#A8352A" stroke-width="4"/><circle cx="70" cy="74" r="36" fill="#F07A64"/>' +
               "".join(f'<ellipse cx="{x}" cy="{y}" rx="5" ry="8" fill="#FFE29A" transform="rotate({a} {x} {y})"/>' for x, y, a in [(56, 60, -30), (86, 62, 30), (52, 88, 30), (88, 90, -30), (70, 74, 0)]) +
               '<path d="M60 22 q10 -12 20 0" stroke="#5E8B3A" stroke-width="6" fill="none"/>',
        seeds='<path d="M70 18 C110 30 124 78 104 108 C88 130 52 130 36 108 C16 78 30 30 70 18 Z" fill="#9CCB6B" stroke="#5E8B3A" stroke-width="4"/>'
              '<path d="M70 34 C98 44 106 80 92 100 C80 116 60 116 48 100 C34 80 42 44 70 34 Z" fill="#F7B3B8"/>' +
              "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#FFF6E6" stroke="#B5863A" stroke-width="1.5"/>' for x, y in [(60, 60), (80, 60), (70, 76), (58, 88), (82, 88), (70, 100)]))[kind]
    return f'<svg viewBox="0 0 140 140" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def bowl_fibre(w=130):
    """A katori of dal with a spoon, and a guava: fibre (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M6 30 H46 Q44 52 26 54 Q8 52 6 30 Z" fill="#fff" stroke="#0D7466" stroke-width="3.5"/><ellipse cx="26" cy="30" rx="20" ry="5" fill="#F3B84A"/>'
            '<circle cx="48" cy="44" r="11" fill="#9CCB6B" stroke="#5E8B3A" stroke-width="2.5"/><path d="M48 33 q2 -5 6 -6" stroke="#5E8B3A" stroke-width="2.5" fill="none"/></svg>')

def teeth(w=130):
    """A smiling mouth with teeth: chew well (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M8 24 Q32 14 56 24 Q54 52 32 54 Q10 52 8 24 Z" fill="#D9473A" stroke="#12302C" stroke-width="3"/>'
            '<path d="M12 25 Q32 18 52 25 L50 33 Q32 28 14 33 Z" fill="#fff" stroke="#12302C" stroke-width="2"/>'
            '<path d="M22 22 V30 M32 20 V29 M42 22 V30" stroke="#12302C" stroke-width="1.6"/>'
            '<path d="M18 44 Q32 50 46 44" stroke="#F3B84A" stroke-width="3" fill="none" stroke-linecap="round"/></svg>')

def pot_soft(w=130):
    """A cooking pot with steam: cook vegetables soft (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M10 30 H54 V48 Q54 56 46 56 H18 Q10 56 10 48 Z" fill="#0D7466"/><rect x="6" y="26" width="52" height="8" rx="4" fill="#12302C"/>'
            '<path d="M4 38 H10 M54 38 H60" stroke="#12302C" stroke-width="4" stroke-linecap="round"/>'
            '<path d="M22 20 q-4 -6 0 -12 M32 20 q-4 -6 0 -12 M42 20 q-4 -6 0 -12" stroke="#F3B84A" stroke-width="3" fill="none" stroke-linecap="round"/></svg>')

def no_enzyme(w=130):
    """A tablet strip crossed out: no enzyme tablets on your own (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#B0362B" stroke-width="4"/>'
            '<rect x="16" y="20" width="32" height="24" rx="4" fill="#DCE7E4" stroke="#12302C" stroke-width="2.5"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="4" fill="#F3B84A" stroke="#12302C" stroke-width="1.5"/>' for x in (24, 32, 40) for y in (28, 37)) +
            '<path d="M13 51 L51 13" stroke="#B0362B" stroke-width="4.5" stroke-linecap="round"/></svg>')

def tulsi_scene(w=900):
    """Dev Uthani Ekadashi and Tulsi Vivah: a decorated tulsi pot under an arch of sugarcane, marigold garland, diyas,
    and a small wedding plate at the side (viewBox 0 0 900 600)."""
    leaves = "".join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="12" fill="{c}" transform="rotate({a} {x} {y})"/>'
                     for x, y, a, c in [(430, 250, -30, "#5E9A3A"), (472, 236, 25, "#6FAE45"), (410, 210, -40, "#6FAE45"), (492, 196, 35, "#5E9A3A"),
                                        (440, 176, -20, "#7DBE52"), (470, 160, 20, "#5E9A3A"), (450, 130, 0, "#7DBE52"), (420, 280, -15, "#5E9A3A"), (482, 276, 15, "#6FAE45")])
    mari = "".join(f'<circle cx="{x}" cy="{90 + 40 * ((x - 450) / 300) ** 2 * 2:.0f}" r="15" fill="{"#F39C2E" if i % 2 else "#F6C93E"}" stroke="#C26A12" stroke-width="2"/>'
                   for i, x in enumerate(range(180, 731, 30)))
    diya = lambda x: (f'<g transform="translate({x} 520)"><path d="M-46 0 Q0 40 46 0 Z" fill="#C0702E" stroke="#8A4A1A" stroke-width="3"/>'
                      f'<path d="M0 -6 C-14 -26 -4 -46 0 -60 C4 -46 14 -26 0 -6 Z" fill="#FFC23A"/><path d="M0 -12 C-6 -22 -2 -32 0 -40 C2 -32 6 -22 0 -12 Z" fill="#FFF1B0"/></g>')
    cane = lambda x, s: (f'<path d="M{x} 560 Q{x + s * 40} 300 {450 - s * 40} 70" fill="none" stroke="#5E8B3A" stroke-width="22" stroke-linecap="round"/>'
                         f'<path d="M{x} 560 Q{x + s * 40} 300 {450 - s * 40} 70" fill="none" stroke="#9CCB6B" stroke-width="10" stroke-dasharray="44 12" stroke-linecap="round"/>')
    return f"""<svg viewBox="0 0 900 600" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="tsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#5A2A10" flood-opacity=".3"/></filter></defs>
<circle cx="450" cy="300" r="250" fill="#FFE7B8" opacity=".55"/>
{cane(200, 1)}{cane(700, -1)}
<path d="M430 340 Q450 230 450 120" stroke="#5E7A2E" stroke-width="8" fill="none"/>{leaves}
<g filter="url(#tsh)"><path d="M330 330 H570 L548 520 H352 Z" fill="#D9573A" stroke="#8A2E1A" stroke-width="5" stroke-linejoin="round"/>
<rect x="316" y="312" width="268" height="34" rx="10" fill="#F3B84A" stroke="#8A5A12" stroke-width="4"/>
<path d="M392 380 L450 420 L508 380 L450 470 Z" fill="#FFF1D6" stroke="#8A2E1A" stroke-width="4"/>
<circle cx="450" cy="420" r="16" fill="#F3B84A"/><circle cx="370" cy="470" r="9" fill="#FFF1D6"/><circle cx="530" cy="470" r="9" fill="#FFF1D6"/></g>
{mari}
{diya(250)}{diya(650)}
<g transform="translate(780 470)"><ellipse rx="80" ry="22" fill="#E7DCC8"/><ellipse rx="64" ry="15" fill="#fff"/>
<circle cx="-24" cy="-10" r="13" fill="#F3B84A"/><circle cx="4" cy="-14" r="13" fill="#F6C93E"/><rect x="18" y="-24" width="24" height="18" rx="4" fill="#FFF6E6" stroke="#C9A35A" stroke-width="2"/></g>
<g transform="translate(120 470)"><path d="M-30 -60 H30 L24 20 H-24 Z" fill="#BFE3F0" stroke="#0D7466" stroke-width="4"/><path d="M-27 -20 H27 L24 20 H-24 Z" fill="#9AD0E4"/></g>
</svg>"""

# ---------------- Instagram 1: Myth or fact? piles (EN, 5 slides) ----------------
N1 = 5
def m1(n=1):
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:28px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px;max-width:920px">Piles always need <em>an operation.</em></h1>
 <div style="position:absolute;left:190px;top:420px">{toilet_scalpel(700)}</div>
 <div style="position:absolute;left:84px;top:1150px;font-size:34px;font-weight:600;color:#B5542C">Guess first, then swipe →</div>
 {foot(n, total=N1)}</div>"""

def m2(n=2):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;border:8px solid #F3B84A;color:#F3B84A;border-radius:22px;padding:6px 36px;transform:rotate(-6deg);font-family:YS;font-size:120px;line-height:1.1">MYTH</div>
 <h1 style="font-size:80px;margin-top:44px;max-width:920px">Most piles get better <em>without surgery.</em></h1>
 <div style="position:absolute;left:300px;top:610px;background:#E6F2EF;border-radius:48px;padding:10px 20px">{toilet_scalpel(440, q=False, cross=True)}</div>
 <p style="position:absolute;left:84px;right:84px;top:1110px;font-size:34px;line-height:1.4;color:#DCEFEA">Softer stools and a short toilet routine settle most. Only a few people need an operation.</p>
 {foot(n, total=N1, light=True)}</div>"""

def m3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:22px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:46px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What helps</div>
 <h2 style="font-size:84px;margin:14px 0 40px">Make stools <em>soft</em></h2>
 <div style="display:grid;gap:22px">
  {row(bowl_fibre(120), "More fibre", "dal, sabzi, fruit, whole grains")}
  {row(glass_between(120), "Enough water", "through the day")}
  {row(clock_small(120), "Short toilet visits", "no straining, no phone on the seat")}
  {row(no_enzyme(120), "Get it diagnosed", "not months of creams and home remedies")}
 </div>
 {foot(n, total=N1)}</div>"""

def m4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor for</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Bleeding from <em>the back passage</em></h2>
 {dot_list(["Especially after age 45", "With a change in bowel habit", "With weight loss or weakness", "A painful, hard lump"], size=50, gap=36)}
 <div style="margin-top:56px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Heavy bleeding, dizziness or fainting? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N1)}</div>"""

def mb_screen():
    return ('<div style="font-size:15px;font-weight:600;letter-spacing:.12em;color:#0D7466">MYTH BUSTER · THURSDAY</div>'
            '<div style="font-family:YS;font-size:28px;color:#12302C;line-height:1.15;margin:14px 0 18px">Food sticking in the chest can be a serious sign.</div>'
            '<div style="display:flex;gap:10px"><span style="flex:1;text-align:center;background:#0D7466;color:#fff;border-radius:999px;padding:12px;font-size:20px;font-weight:600">Myth</span>'
            '<span style="flex:1;text-align:center;background:#fff;border:2px solid #0D7466;color:#0D7466;border-radius:999px;padding:12px;font-size:20px;font-weight:600">Fact</span></div>'
            '<div style="margin-top:26px;display:flex;gap:8px;justify-content:center">' + "".join(f'<i style="width:12px;height:12px;border-radius:50%;background:{"#0D7466" if i == 0 else "#CFE0DC"}"></i>' for i in range(8)) + '</div>'
            '<div style="margin-top:26px;background:#FAEED8;border-radius:18px;padding:16px;font-size:18px;color:#12302C">New myth every Monday and Thursday</div>')

def m5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">Your turn</div>
 <h1 style="font-size:92px;margin-top:18px;max-width:560px">Play more <em>Myth or fact?</em></h1>
 <p style="font-size:36px;line-height:1.35;color:#DCEFEA;margin-top:30px;max-width:520px">Next one on Thursday. Guess, then see the answer.</p>
 <div style="display:inline-block;margin-top:56px;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
 <p style="font-size:28px;color:#CFE5E0;margin-top:24px;max-width:520px">English and हिंदी · free</p>
 <div style="position:absolute;right:84px;top:300px">{phone(mb_screen(), w=380, tilt=5)}</div>
 {foot(n, total=N1, light=True)}</div>"""

# ---------------- Instagram 2: Undigested food in stool (EN, 5 slides) ----------------
N2 = 5
def u1(n=1):
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">World Toilet Day · 19 Nov</div>
 <h1 style="font-size:100px;margin-top:16px;max-width:900px">Spotted <em>corn</em> in your stool?</h1>
 <p style="font-size:36px;line-height:1.35;color:#4A615D;margin-top:22px;max-width:820px">Usually normal. Here is why, and when to check.</p>
 <div style="position:absolute;left:220px;top:560px">{corn_mag(640)}</div>
 {foot(n, total=N2)}</div>"""

def u2(n=2):
    tile = lambda k, a, b: (f'<div style="background:rgba(255,255,255,.1);border-radius:30px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;gap:12px">{mini(k, 120)}'
                            f'<div style="font-family:YS;font-size:44px;color:#F3B84A;line-height:1.05">{a}</div><div style="font-size:29px;color:#DCEFEA;line-height:1.3">{b}</div></div>')
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">Usually normal</div>
 <h2 style="font-size:80px;margin:14px 0 40px">Skins and seeds <em>pass whole</em></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {tile("corn", "Corn", "the outer skin")}{tile("peas", "Peas, chana", "the skins")}
  {tile("tomato", "Tomato", "skin and seeds")}{tile("seeds", "Guava, til", "small seeds")}</div>
 <p style="font-size:31px;line-height:1.35;color:#DCEFEA;margin-top:34px">The goodness inside is still absorbed. It's fibre, not weak digestion.</p>
 {foot(n, total=N2, light=True)}</div>"""

def u3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:22px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:46px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What helps</div>
 <h2 style="font-size:84px;margin:14px 0 40px">Chew it, <em>cook it soft</em></h2>
 <div style="display:grid;gap:22px">
  {row(teeth(120), "Chew well", "eat slowly, away from screens")}
  {row(pot_soft(120), "Cook soft", "vegetables, dal, chana, rajma")}
  {row(bowl_fibre(120), "Keep the fibre", "don't drop vegetables")}
  {row(no_enzyme(120), "No enzyme tablets", "not on your own")}
 </div>
 {foot(n, total=N2)}</div>"""

def u4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor if</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Food in stool <em>with</em></h2>
 {dot_list(size=46, gap=30, items=["Loose motions for 2 to 4 weeks", "Pale, oily stools, hard to flush", "Weight loss or anaemia", "Blood, or black stools", "Belly pain that keeps coming back"])}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Heavy bleeding, or black stools with dizziness? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N2)}</div>"""

def u5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on the website</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:900px">Undigested food in stool: <em>the full answer</em></h1>
 <p style="font-size:34px;line-height:1.4;color:#DCEFEA;margin-top:30px;max-width:880px">Why it happens, when it's a problem, tests and what to eat. In English and हिंदी.</p>
 <div style="position:absolute;right:60px;top:640px;background:#E6F2EF;border-radius:40px;padding:20px">{corn_mag(340)}</div>
 <div style="position:absolute;left:84px;top:860px">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
  <p style="font-size:28px;color:#CFE5E0;margin-top:22px">Link in bio · Answers</p></div>
 {foot(n, total=N2, light=True)}</div>"""

# ---------------- Instagram 3: Dev Uthani Ekadashi (HI, single post) ----------------
EK = [("एकादशी व्रत", "साबूदाना, कुट्टू तलें नहीं, भूनें"),
      ("थोड़ा-थोड़ा", "हर 3 से 4 घंटे में; पानी, छाछ लें"),
      ("शादी की दावत", "पहले सलाद और दाल, मिठाई एक"),
      ("रात का खाना", "देर रात भारी नहीं, थोड़ा टहलें")]
WARM = "background:radial-gradient(120% 75% at 50% 20%,#FFF4DE 0%,#FCE3B6 60%,#F7CF8C 100%);color:#12302C"

def ek_rows(size=34, gap=14, lw=300):
    return "".join(f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.72);border-radius:24px;padding:14px 24px;margin-bottom:{gap}px">'
                   f'<span style="flex:none;width:{lw}px;font-family:TD;font-size:{size+2}px;color:#B5542C;line-height:1.25">{d}</span><span style="font-size:{size}px;line-height:1.3">{t}</span></div>'
                   for d, t in EK)

def ek_post():
    return f"""<div class="s cream hi" style="width:1080px;height:1350px;padding:60px 72px;{WARM}">
 <div class="kick" style="font-size:30px;color:#B5542C;text-align:center">देवउठनी एकादशी · तुलसी विवाह</div>
 <h1 style="font-size:72px;margin-top:4px;text-align:center">व्रत भी, शादियाँ भी: <em style="color:#0D7466">पेट रहे हल्का</em></h1>
 <div style="position:absolute;left:180px;top:240px">{tulsi_scene(720)}</div>
 <div style="position:absolute;left:72px;right:72px;top:715px">{ek_rows(32, 12)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1075px;font-size:29px;line-height:1.35;color:#4A615D">डायबिटीज़ या गर्भावस्था में व्रत से पहले डॉक्टर से पूछें। ऊपरी पेट में तेज़ दर्द पीठ तक जाए, साथ में उल्टी? 112 पर कॉल करें।</p>
 {foot(hi=True)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:76px 80px">
 <div class="kick" style="font-size:26px;color:#0D7466">World Toilet Day · 19 Nov</div>
 <h1 style="font-size:80px;margin-top:14px;max-width:620px">Spotted <em>corn</em> in your stool?</h1>
 <p style="font-size:32px;line-height:1.35;color:#4A615D;margin-top:24px;max-width:560px">Usually just fibre. Get checked if it comes with weeks of loose motions or weight loss.</p>
 <div style="position:absolute;right:70px;top:110px">{corn_mag(480)}</div>
 {foot(pad=80)}</div>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_myth():
    return f"""<div class="s saffron" style="width:1080px;height:1920px;padding:150px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:30px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px">Piles always need <em>an operation.</em></h1>
 <div style="position:absolute;left:290px;top:560px">{toilet_scalpel(500, q=False, cross=True)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1140px">
  <div style="display:inline-block;border:7px solid #B0362B;color:#B0362B;border-radius:20px;padding:4px 30px;transform:rotate(-5deg);font-family:YS;font-size:88px">MYTH</div>
  <p style="font-size:40px;line-height:1.35;margin-top:30px">Most piles settle with <b>softer stools</b> and <b>no straining</b>. Bleeding from the back passage still needs a doctor's check.</p></div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Play more at drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_corn():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">World Toilet Day · 19 Nov</div>
 <h1 style="font-size:108px;margin-top:16px">Spotted <em>corn</em> in your stool?</h1>
 <div style="position:absolute;left:200px;top:640px">{corn_mag(660)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1330px;display:grid;gap:16px">
  {"".join(f'<div style="background:#fff;border-radius:999px;padding:18px 32px;font-size:36px;display:flex;gap:18px;align-items:center"><span style="width:18px;height:18px;border-radius:50%;background:{c};flex:none"></span>{t}</div>' for c, t in (("#0D7466", "Skins and seeds pass whole: normal"), ("#0D7466", "Chew well, cook vegetables soft"), ("#B0362B", "Weeks of loose motions? Get checked")))}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Read more: drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_ek():
    return f"""<div class="s cream hi" style="width:1080px;height:1920px;padding:150px 72px;{WARM}">
 <div class="kick" style="font-size:34px;color:#B5542C;text-align:center">देवउठनी एकादशी · तुलसी विवाह</div>
 <h1 style="font-size:76px;margin-top:10px;text-align:center">व्रत भी, शादियाँ भी: <em style="color:#0D7466">पेट रहे हल्का</em></h1>
 <div style="position:absolute;left:90px;top:420px">{tulsi_scene(900)}</div>
 <div style="position:absolute;left:72px;right:72px;top:1050px">{ek_rows(36, 16, 290)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1500px;font-size:34px;line-height:1.35;color:#4A615D">डायबिटीज़ या गर्भावस्था में व्रत से पहले डॉक्टर से पूछें।</p>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 44px;border-radius:999px">drlochab.com/hi</span></div>
 {foot(pad=72, hi=True)}</div>"""

# ---------------- text ----------------
CAP_MYTH = f"""Myth or fact? "Piles always need an operation." 🚽

Guess first, then swipe 👉

❌ MYTH. Piles are swollen veins at the back passage, and most flare up because of hard stools and straining. Softer stools, a short toilet routine and, when needed, a quick clinic treatment such as banding settle the large majority. Only a few people need an operation.

What helps:
🥗 More fibre: dal, sabzi, fruit and whole grains
💧 Enough water through the day
⏱️ Short toilet visits: no straining, no scrolling on the seat
🩺 Get the diagnosis confirmed by a doctor, instead of months of creams and home remedies

🚩 See a doctor for bleeding from the back passage, especially after 45, or with a change in bowel habit, weight loss or weakness, or for a painful hard lump. Heavy bleeding, dizziness or fainting: call 112 or go to the nearest emergency department.

🎮 The next Myth or fact? goes up on Thursday. Play them all at drlochab.com (link in bio), in English and Hindi. More on piles, fissure and fistula: {MYTH_LINK}

{SIGN}

#MythOrFact #Piles #Haemorrhoids #Constipation #GutHealth #Gastroenterologist #Gurugram #DrLochab"""

CAP_CORN = f"""Spotted corn in your stool? 🌽 It's World Toilet Day (19 Nov), so let's talk about what we see in the toilet.

Seeing bits of corn, peas, seeds, tomato skin or leafy vegetables is normal. The tough outer fibre of some foods can't be digested by anyone, and pieces that aren't chewed well come out looking whole, even though most of the goodness inside has been absorbed. It's a sign of fibre, not of weak digestion.

What helps:
😁 Chew well and eat slowly, away from screens
🍲 Cook vegetables soft; soak and cook dal, chana and rajma well
🥗 Keep eating fibre: don't drop vegetables
🚫 No digestive enzyme tablets on your own: they help only when tests show the pancreas isn't making enough

🚩 See a doctor if food in the stool comes with loose motions for more than 2 to 4 weeks, pale, oily stools that are hard to flush, weight loss, anaemia, blood or black stools, or belly pain that keeps coming back. Heavy bleeding, or black stools with dizziness: call 112.

📖 New on my website, in English and Hindi: {ANS} (link in bio)

{SIGN}

#WorldToiletDay #GutHealth #Digestion #Fibre #StoolHealth #Gastroenterologist #Gurugram #DrLochab"""

CAP_EK = f"""देवउठनी एकादशी और तुलसी विवाह: व्रत भी, शादियाँ भी, पेट रहे हल्का 🪔

शुक्रवार 20 नवंबर को देवउठनी एकादशी है और शनिवार 21 नवंबर को तुलसी विवाह। इसके साथ शादियों का मौसम भी शुरू हो रहा है। कुछ छोटी बातें:

🪔 एकादशी व्रत में साबूदाना, कुट्टू और आलू तलने की जगह भूनें या उबालें
🪔 लंबे समय भूखे न रहें: हर 3 से 4 घंटे में थोड़ा खाएँ, पानी, छाछ और नारियल पानी लेते रहें
🪔 शादी की दावत में प्लेट की शुरुआत सलाद और दाल से करें; मिठाई एक, तली चीज़ें कम
🪔 देर रात भारी खाना न खाएँ; खाने के बाद थोड़ा टहलें
🪔 डायबिटीज़, गर्भावस्था, या पेट की कोई बीमारी हो तो व्रत से पहले अपने डॉक्टर से पूछें; दवाएँ अपने आप न छोड़ें

🚩 भारी दावत के बाद ऊपरी पेट में तेज़ दर्द जो पीठ तक जाए, साथ में उल्टी हो, तो देर न करें: 112 पर कॉल करें या नज़दीकी इमरजेंसी में जाएँ।

शादियों के मौसम में पेट और लिवर की पूरी गाइड (हिंदी): {WED_HI} (लिंक बायो में)

सबको देवउठनी एकादशी की शुभकामनाएँ 🙏

{SIGN_HI}

#देवउठनीएकादशी #तुलसीविवाह #एकादशीव्रत #शादीकामौसम #पेटकीसेहत #Gurugram #DrLochab"""

GBP_TEXT = f"""Spotted bits of corn, peas or seeds in your stool? On World Toilet Day (19 November), a common question: is it normal?

Usually, yes. The tough outer skin of corn, peas, chana, tomato and some seeds is fibre that no one can digest, so it passes whole, even though the goodness inside has been absorbed. Food that is not chewed well, or that moves through quickly during loose motions, can also show.

What helps: chew well and eat slowly, cook vegetables soft, keep eating fibre, and do not start digestive enzyme tablets without a doctor's advice.

See a doctor if it comes with loose motions for more than 2 to 4 weeks, pale, oily stools that are hard to flush, weight loss, blood or black stools. Heavy bleeding, or black stools with dizziness, is an emergency: call 112.

Read the full answer, with a diet guide and common questions, in English and Hindi.

Button: Learn more → https://{ANS}/"""

WA_EN = f"""🩺 *Seen undigested food in your stool?*

Bits of corn, peas, seeds or vegetable skins in the stool are usually normal: it's fibre that no one can digest. It needs a check only when it comes with loose motions for weeks, pale oily stools, weight loss or belly pain. For World Toilet Day (19 Nov), I've written a short, plain answer on why it happens, what helps, and when to get checked:

👉 https://{ANS}/
हिंदी में: https://{ANS_HI}/

– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)"""

WA_HI = f"""🩺 *पॉटी में बिना पचा खाना दिखा?*

मल में मक्का, मटर, बीज या सब्ज़ियों के छिलके दिखना आमतौर पर सामान्य है: यह ऐसा रेशा है जिसे कोई नहीं पचा सकता। जाँच तभी ज़रूरी है जब साथ में हफ़्तों से दस्त, चिकना हल्के रंग का मल, वज़न घटना या पेट दर्द हो। यह क्यों होता है, क्या मदद करता है, और कब डॉक्टर को दिखाएँ, आसान भाषा में यहाँ पढ़ें:

👉 https://{ANS_HI}/

देवउठनी एकादशी की शुभकामनाएँ 🪔 व्रत और शादियों की दावत में पेट का ध्यान रखें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, गुरुग्राम (drlochab.com/hi)"""

if __name__ == "__main__":
    import week_2026_11_09 as w9
    w9.OUT = OUT   # render() writes its temporary page into OUT
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([m1, m2, m3, m4, m5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig1-myth-piles-{i}.png", b)
        for i, f in enumerate([u1, u2, u3, u4, u5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig2-undigested-food-in-stool-{i}.png", b)
        render(ek_post, 1080, 1350, f"{OUT}/ig3-dev-uthani-ekadashi-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business-undigested-food.png", b)
        render(st_myth, 1080, 1920, f"{OUT}/wa-status-1-myth-piles.png", b)
        render(st_corn, 1080, 1920, f"{OUT}/wa-status-2-undigested-food.png", b)
        render(st_ek, 1080, 1920, f"{OUT}/wa-status-3-ekadashi-hi.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("ig1-caption.txt", CAP_MYTH), ("ig2-caption.txt", CAP_CORN), ("ig3-caption-hi.txt", CAP_EK),
                      ("google-business-post.txt", GBP_TEXT), ("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
