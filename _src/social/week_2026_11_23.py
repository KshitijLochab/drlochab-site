"""Social content for the week of 23 to 29 Nov 2026 (Guru Nanak Jayanti / Gurpurab, Tue 24 Nov; wedding season).
Instagram: "Myth or fact?" carousel (EN, Myth Buster entry of Mon 23 Nov: a biopsy makes cancer spread),
nausea and vomiting carousel (EN, the week's new answer page), Gurpurab "lessons from the langar" post (HI).
Google Business Profile: nausea and vomiting (1200x900). WhatsApp Status: 3 images (1080x1920). Captions and messages as .txt.
Original drawings only. No doses, no brand names, no phone number in the Google post text.
Run from anywhere: python3 _src/social/week_2026_11_23.py  -> _src/out/week-2026-11-23/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC, STOM
from week_2026_11_02 import dot_list
from week_2026_10_26 import ors_glass, bowl, no_pill
from week_2026_11_09 import clock_small, glass_between, render
from new_tools_promo import phone
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-11-23"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/nausea-and-vomiting"
ANS_HI = "drlochab.com/hi/answers/nausea-and-vomiting"
MYTH_LINK = "drlochab.com/procedures/upper-gi-endoscopy"
WED_HI = "drlochab.com/hi/guides/winter-wedding-season-guide"
SIGN = ("Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Fellowship in EUS and ERCP), Gurugram. "
        "HMC Reg. No. HN-23524. Prepared with AI assistance and reviewed by Dr. Lochab.")
SIGN_HI = ("डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP फ़ेलोशिप), गुरुग्राम। "
           "HMC रजि. नं. HN-23524। AI की सहायता से तैयार और डॉ. लोचब द्वारा समीक्षित।")

# ---------------- original drawings ----------------
def biopsy_view(w=600, q=True, rice=False):
    """Endoscope view of the stomach lining with biopsy forceps taking a tiny piece (viewBox 0 0 600 600)."""
    folds = "".join(f'<path d="M{70+i*80} 80 C{110+i*80} 250 {40+i*80} 360 {90+i*80} 540" fill="none" stroke="#E58E86" stroke-width="22" stroke-linecap="round" opacity=".65"/>' for i in range(6))
    qm = ('<g transform="translate(500 96)"><circle r="66" fill="#12302C"/><text x="0" y="33" text-anchor="middle" font-family="YS" font-size="96" fill="#F3B84A">?</text></g>' if q else "")
    rc = ('<g transform="translate(110 488)"><circle r="100" fill="#FFFFFF" stroke="#12302C" stroke-width="6"/>'
          '<ellipse cx="-26" cy="-14" rx="44" ry="16" fill="#FBF5EA" stroke="#C9B48A" stroke-width="4" transform="rotate(-20 -26 -14)"/>'
          '<ellipse cx="44" cy="-14" rx="10" ry="8" fill="#E58E86" stroke="#9C4A42" stroke-width="3"/>'
          '<text x="-26" y="40" text-anchor="middle" font-family="FT" font-weight="600" font-size="24" fill="#4A615D">rice</text>'
          '<text x="44" y="40" text-anchor="middle" font-family="FT" font-weight="600" font-size="24" fill="#B0362B">biopsy</text></g>' if rice else "")
    return f"""<svg viewBox="0 0 600 600" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="bvc"><circle cx="300" cy="300" r="250"/></clipPath>
<radialGradient id="bvl" cx=".45" cy=".42" r=".65"><stop offset="0" stop-color="#FFD9D2"/><stop offset=".6" stop-color="#F4A99F"/><stop offset="1" stop-color="#9C4A42"/></radialGradient>
<filter id="bvs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#12302C" flood-opacity=".3"/></filter></defs>
<g filter="url(#bvs)"><circle cx="300" cy="300" r="276" fill="#12302C"/></g>
<g clip-path="url(#bvc)"><rect width="600" height="600" fill="url(#bvl)"/>{folds}
<ellipse cx="330" cy="330" rx="70" ry="52" fill="#D9776C" opacity=".8"/><ellipse cx="318" cy="320" rx="18" ry="12" fill="#FFF0EC" opacity=".7"/>
<g transform="translate(372 292) rotate(45)">
 <rect x="-15" y="-340" width="30" height="300" rx="15" fill="#C8D3D0" stroke="#7C8C88" stroke-width="5"/>
 <rect x="-15" y="-60" width="30" height="24" fill="#7C8C88"/>
 <path d="M-14 -40 C-36 -16 -30 18 -4 30 L-2 -8 Z" fill="#E9EEED" stroke="#5E6C69" stroke-width="5" stroke-linejoin="round"/>
 <path d="M14 -40 C36 -16 30 18 4 30 L2 -8 Z" fill="#E9EEED" stroke="#5E6C69" stroke-width="5" stroke-linejoin="round"/>
 <ellipse cx="0" cy="6" rx="9" ry="8" fill="#C2453A"/></g></g>
<circle cx="300" cy="300" r="250" fill="none" stroke="#0D7466" stroke-width="12"/>
{rc}{qm}</svg>"""

def queasy(w=600, waves=True):
    """The stomach as a queasy little boat on rolling waves, with dizzy swirls (viewBox 0 0 600 640)."""
    wv = ""
    if waves:
        wv = ('<clipPath id="qwc"><rect x="20" y="470" width="560" height="160" rx="48"/></clipPath><g clip-path="url(#qwc)"><path d="M0 520 C60 490 120 550 180 520 S300 490 360 520 S480 550 540 520 S600 500 640 520 V640 H0 Z" fill="#0D7466" opacity=".9"/>'
              '<path d="M0 560 C70 530 130 590 200 560 S330 530 400 560 S520 590 600 560 V640 H0 Z" fill="#0B6A5E"/>'
              '<path d="M40 530 q20 -14 40 0 M250 518 q20 -14 40 0 M450 534 q20 -14 40 0" fill="none" stroke="#E6F2EF" stroke-width="6" stroke-linecap="round" opacity=".8"/></g>')
    sw = "".join(f'<path d="M{x} {y} m-4 0 a4 4 0 1 1 8 0 a9 9 0 1 1 -18 0 a14 14 0 1 1 28 0" fill="none" stroke="#12302C" stroke-width="6" stroke-linecap="round"/>' for x, y in ((150, 120), (470, 150)))
    return f"""<svg viewBox="0 0 600 640" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="qg" cx="38%" cy="34%" r="70%"><stop offset="0" stop-color="#E4F2B8"/><stop offset=".6" stop-color="#BFDB7A"/><stop offset="1" stop-color="#93B655"/></radialGradient>
<filter id="qs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#062F2A" flood-opacity=".3"/></filter></defs>
{sw}
<g transform="rotate(-12 300 300) translate(0 10)" filter="url(#qs)"><path d="{STOM}" fill="url(#qg)" stroke="#6E8F38" stroke-width="6"/>
<ellipse cx="300" cy="250" rx="44" ry="20" fill="#FFFFFF" opacity=".5" transform="rotate(-30 300 250)"/>
<path d="M262 318 q10 -10 20 0 M330 318 q10 -10 20 0" fill="none" stroke="#3E5A1E" stroke-width="7" stroke-linecap="round"/>
<path d="M276 378 q12 -12 24 0 q12 12 24 0 q12 -12 24 0" fill="none" stroke="#3E5A1E" stroke-width="7" stroke-linecap="round"/>
<path d="M420 300 C430 320 434 334 426 344 A12 12 0 0 1 410 330 C410 322 414 312 420 300 Z" fill="#BFE3F0" stroke="#0D7466" stroke-width="4"/></g>
{wv}</svg>"""

def upright(w=130):
    """A person sitting upright in a chair after a meal (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M14 8 V56 M14 34 H44 V56" fill="none" stroke="#0D7466" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
            '<circle cx="28" cy="12" r="7" fill="#F3B84A" stroke="#12302C" stroke-width="2.5"/>'
            '<path d="M26 20 V34 H40 V52" fill="none" stroke="#12302C" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
            '<path d="M48 14 V30 M43 19 L48 13 L53 19" fill="none" stroke="#F3B84A" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def cause_icon(kind, w=120):
    """Small icons for usual causes of nausea (viewBox 0 0 64 64)."""
    body = dict(
        bug='<circle cx="32" cy="34" r="16" fill="#8DBE5A" stroke="#4E7A2A" stroke-width="3"/>' + "".join(f'<path d="M32 34 L{32+24*c} {34+24*s}" stroke="#4E7A2A" stroke-width="3" stroke-linecap="round"/><circle cx="{32+24*c}" cy="{34+24*s}" r="3.5" fill="#4E7A2A"/>' for c, s in ((1, 0), (-1, 0), (0, 1), (0, -1), (.7, .7), (-.7, .7), (.7, -.7), (-.7, -.7))) + '<circle cx="27" cy="31" r="2.5" fill="#12302C"/><circle cx="37" cy="31" r="2.5" fill="#12302C"/>',
        flame='<path d="M32 6 C44 20 50 30 48 42 A16 16 0 0 1 16 42 C14 32 22 26 24 16 C28 24 30 26 32 6 Z" fill="#F08A3C" stroke="#B5542C" stroke-width="3"/><path d="M32 30 C38 36 40 42 36 48 A6 6 0 0 1 26 46 C26 40 30 38 32 30 Z" fill="#F6C93E"/>',
        car='<rect x="8" y="28" width="48" height="16" rx="6" fill="#0D7466"/><path d="M16 28 L22 18 H42 L48 28 Z" fill="#BFE3F0" stroke="#0D7466" stroke-width="3"/><circle cx="20" cy="46" r="6" fill="#12302C"/><circle cx="44" cy="46" r="6" fill="#12302C"/><path d="M6 58 q8 -5 16 0 t16 0 t16 0" fill="none" stroke="#F3B84A" stroke-width="3" stroke-linecap="round"/>',
        pill='<g transform="rotate(-35 32 32)"><rect x="10" y="22" width="44" height="20" rx="10" fill="#fff" stroke="#12302C" stroke-width="3"/><path d="M32 22 H44 A10 10 0 0 1 44 42 H32 Z" fill="#F3B84A" stroke="#12302C" stroke-width="3"/></g><circle cx="50" cy="12" r="8" fill="#B0362B"/><text x="50" y="16" text-anchor="middle" font-family="FT" font-weight="700" font-size="12" fill="#fff">+</text>')[kind]
    return f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def tick_doc(kind, w=120):
    """Small icons for the biopsy 'what to do' slide (viewBox 0 0 64 64)."""
    body = dict(
        yes='<circle cx="32" cy="32" r="26" fill="#0D7466"/><path d="M20 33 L29 42 L45 23" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
        cal='<rect x="8" y="12" width="48" height="44" rx="8" fill="#fff" stroke="#0D7466" stroke-width="3.5"/><path d="M8 24 H56" stroke="#0D7466" stroke-width="3.5"/><rect x="18" y="6" width="5" height="12" rx="2.5" fill="#12302C"/><rect x="41" y="6" width="5" height="12" rx="2.5" fill="#12302C"/><circle cx="40" cy="42" r="7" fill="#F3B84A"/>',
        report='<path d="M14 6 H40 L50 16 V58 H14 Z" fill="#fff" stroke="#0D7466" stroke-width="3.5" stroke-linejoin="round"/><path d="M22 26 H42 M22 34 H42 M22 42 H34" stroke="#9FB8B2" stroke-width="3.5" stroke-linecap="round"/><circle cx="46" cy="48" r="10" fill="#F3B84A" stroke="#12302C" stroke-width="2.5"/><path d="M41 48 l3 3 l6 -6" fill="none" stroke="#12302C" stroke-width="2.5" stroke-linecap="round"/>',
        plan='<rect x="12" y="10" width="40" height="48" rx="6" fill="#fff" stroke="#0D7466" stroke-width="3.5"/><rect x="24" y="5" width="16" height="10" rx="3" fill="#12302C"/>' + "".join(f'<path d="M19 {26+i*10} l3 3 l5 -5" fill="none" stroke="#0D7466" stroke-width="3" stroke-linecap="round"/><path d="M31 {27+i*10} H45" stroke="#9FB8B2" stroke-width="3" stroke-linecap="round"/>' for i in range(3)))[kind]
    return f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def langar(w=900):
    """A simple langar meal: steel thali with dal, sabzi, rotis and kheer on a striped durrie, with marigolds and diyas (viewBox 0 0 900 560)."""
    stripes = "".join(f'<rect x="0" y="{330+i*34}" width="900" height="17" fill="{c}"/>' for i, c in enumerate(("#1D4E89", "#F3B84A", "#1D4E89", "#F3B84A", "#1D4E89", "#F3B84A", "#1D4E89")))
    mg = lambda x, y, r=22: (f'<g transform="translate({x} {y})">' + "".join(f'<circle cx="{r*0.55*__import__("math").cos(a/6*6.283):.1f}" cy="{r*0.55*__import__("math").sin(a/6*6.283):.1f}" r="{r*0.6:.1f}" fill="#F08A3C"/>' for a in range(6)) + f'<circle r="{r*0.55:.1f}" fill="#F6B13A"/><circle r="{r*0.2:.1f}" fill="#C9711A"/></g>')
    diya = lambda x, y: (f'<g transform="translate({x} {y})"><path d="M-46 0 C-40 30 40 30 46 0 Z" fill="#C9711A" stroke="#8A4A12" stroke-width="4"/>'
                         '<path d="M0 -6 C10 -24 6 -40 0 -54 C-6 -40 -10 -24 0 -6 Z" fill="#F6C93E"/><path d="M0 -10 C4 -20 3 -28 0 -36 C-3 -28 -4 -20 0 -10 Z" fill="#FFF1B0"/></g>')
    return f"""<svg viewBox="0 0 900 560" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="steel" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#DCE4E2"/><stop offset="1" stop-color="#A9B6B3"/></radialGradient>
<filter id="lsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#12302C" flood-opacity=".3"/></filter></defs>
<rect x="0" y="320" width="900" height="240" rx="0" fill="#1D4E89"/>{stripes}
<path d="M0 320 H900" stroke="#12302C" stroke-width="3" opacity=".3"/>
<g filter="url(#lsh)"><ellipse cx="450" cy="380" rx="300" ry="150" fill="url(#steel)" stroke="#8C9A97" stroke-width="6"/>
<ellipse cx="450" cy="380" rx="262" ry="126" fill="none" stroke="#B9C5C2" stroke-width="4"/></g>
<g transform="translate(330 340)"><ellipse rx="78" ry="40" fill="#C9D3D0" stroke="#8C9A97" stroke-width="4"/><ellipse rx="66" ry="31" fill="#F3B84A"/><ellipse cx="-18" cy="-6" rx="14" ry="5" fill="#FFE3A0"/></g>
<g transform="translate(560 340)"><ellipse rx="78" ry="40" fill="#C9D3D0" stroke="#8C9A97" stroke-width="4"/><ellipse rx="66" ry="31" fill="#8DBE5A"/>
 <circle cx="-22" cy="-4" r="10" fill="#F6C93E"/><circle cx="8" cy="6" r="10" fill="#E9B23A"/><rect x="20" y="-14" width="16" height="14" rx="3" fill="#5E8B3A"/></g>
<g transform="translate(450 446)"><ellipse rx="66" ry="32" fill="#C9D3D0" stroke="#8C9A97" stroke-width="4"/><ellipse rx="54" ry="24" fill="#FFF6E6"/>
 <circle cx="-14" cy="-2" r="4" fill="#C9921A"/><circle cx="10" cy="4" r="4" fill="#5E8B3A"/></g>
<g transform="translate(450 270)">
 <ellipse cx="0" cy="40" rx="96" ry="30" fill="#E7C08A" stroke="#B5823F" stroke-width="4"/><ellipse cx="0" cy="26" rx="96" ry="30" fill="#F0CF98" stroke="#B5823F" stroke-width="4"/>
 <ellipse cx="0" cy="12" rx="96" ry="30" fill="#F6DCAA" stroke="#B5823F" stroke-width="4"/>
 <circle cx="-30" cy="6" r="7" fill="#C98A3E" opacity=".6"/><circle cx="26" cy="16" r="6" fill="#C98A3E" opacity=".6"/><circle cx="8" cy="0" r="5" fill="#C98A3E" opacity=".6"/></g>
{diya(110, 300)}{diya(790, 300)}
{"".join(mg(x, 40 + (i % 2) * 18, 24) for i, x in enumerate(range(40, 900, 70)))}
<path d="M0 30 Q450 110 900 30" fill="none" stroke="#5E8B3A" stroke-width="4"/>
</svg>"""

# ---------------- Instagram 1: Myth or fact? biopsy (EN, 5 slides) ----------------
N1 = 5
def m1(n=1):
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:28px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px;max-width:920px">A biopsy makes <em>cancer spread.</em></h1>
 <div style="position:absolute;left:230px;top:470px">{biopsy_view(640)}</div>
 <div style="position:absolute;left:84px;top:1170px;font-size:34px;font-weight:600;color:#B5542C">Guess first, then swipe →</div>
 {foot(n, total=N1)}</div>"""

def m2(n=2):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;border:8px solid #F3B84A;color:#F3B84A;border-radius:22px;padding:6px 36px;transform:rotate(-6deg);font-family:YS;font-size:120px;line-height:1.1">MYTH</div>
 <h1 style="font-size:84px;margin-top:44px;max-width:920px">A biopsy doesn't spread cancer. <em>Delay does harm.</em></h1>
 <div style="position:absolute;left:330px;top:620px">{biopsy_view(440, q=False, rice=True)}</div>
 <p style="position:absolute;left:84px;right:84px;top:1090px;font-size:34px;line-height:1.4;color:#DCEFEA">A few pieces smaller than a grain of rice, taken in seconds. Refusing it can lose months while a treatable growth grows.</p>
 {foot(n, total=N1, light=True)}</div>"""

ROW = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:22px 34px">{art}'
                           f'<div><div style="font-family:YS;font-size:46px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')

def m3(n=3):
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">If a biopsy is advised</div>
 <h2 style="font-size:76px;margin:14px 0 40px">Say yes, <em>then follow up</em></h2>
 <div style="display:grid;gap:22px">
  {ROW(tick_doc("yes", 120), "Agree to it", "it is quick and painless")}
  {ROW(tick_doc("cal", 120), "Ask the date", "when will the report be ready?")}
  {ROW(tick_doc("report", 120), "Collect the report", "and take it back to your doctor")}
  {ROW(tick_doc("plan", 120), "Plan treatment", "most growths are named only by biopsy")}
 </div>
 {foot(n, total=N1)}</div>"""

def m4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor without delay for</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Signs that need <em>a look inside</em></h2>
 {dot_list(["Trouble swallowing", "Black stools or blood in the stool", "Weight loss you can't explain", "Vomiting blood"], size=50, gap=36)}
 <div style="margin-top:56px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Vomiting blood, or black stools with dizziness? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N1)}</div>"""

def mb_screen():
    return ('<div style="font-size:15px;font-weight:600;letter-spacing:.12em;color:#0D7466">MYTH BUSTER · THURSDAY</div>'
            '<div style="font-family:YS;font-size:28px;color:#12302C;line-height:1.15;margin:14px 0 18px">Normal liver tests mean my liver is healthy.</div>'
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

# ---------------- Instagram 2: Nausea and vomiting (EN, 5 slides) ----------------
N2 = 5
def v1(n=1):
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Ji machlana</div>
 <h1 style="font-size:104px;margin-top:16px;max-width:900px">Feeling <em>queasy?</em></h1>
 <p style="font-size:36px;line-height:1.35;color:#4A615D;margin-top:22px;max-width:820px">Usually it passes in a day or two. Here's when it doesn't.</p>
 <div style="position:absolute;left:240px;top:480px">{queasy(600)}</div>
 {foot(n, total=N2)}</div>"""

def v2(n=2):
    tile = lambda k, a, b: (f'<div style="background:rgba(255,255,255,.1);border-radius:30px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;gap:12px">{cause_icon(k, 120)}'
                            f'<div style="font-family:YS;font-size:44px;color:#F3B84A;line-height:1.05">{a}</div><div style="font-size:29px;color:#DCEFEA;line-height:1.3">{b}</div></div>')
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">The usual reasons</div>
 <h2 style="font-size:80px;margin:14px 0 40px">Mostly <em>short-lived</em></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {tile("bug", "A stomach bug", "often with loose motions")}{tile("flame", "Acidity", "or a heavy, oily meal")}
  {tile("car", "Travel", "motion sickness, strong smells")}{tile("pill", "A new medicine", "check with your doctor")}</div>
 <p style="font-size:31px;line-height:1.35;color:#DCEFEA;margin-top:34px">Nausea with yellow eyes can be the first sign of hepatitis.</p>
 {foot(n, total=N2, light=True)}</div>"""

def v3(n=3):
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What helps</div>
 <h2 style="font-size:84px;margin:14px 0 40px">Sip, nibble, <em>sit up</em></h2>
 <div style="display:grid;gap:22px">
  {ROW(glass_between(120), "Small sips", "ORS, water, coconut water")}
  {ROW(bowl(120), "Bland food", "khichdi, toast, idli, banana")}
  {ROW(clock_small(120), "Small meals", "every 2 to 3 hours")}
  {ROW(upright(120), "Stay upright", "2 to 3 hours after eating")}
 </div>
 {foot(n, total=N2)}</div>"""

def v4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor the same day</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Nausea <em>with</em></h2>
 {dot_list(size=46, gap=30, items=["Vomiting for more than a day", "No fluids staying down, little urine", "Severe belly pain or yellow eyes", "Swollen belly, no wind or stool", "Weight loss, or weeks of it"])}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Blood in the vomit, chest pain with sweating, or a severe headache? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N2)}</div>"""

def v5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on the website</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:900px">Nausea and vomiting: <em>the full answer</em></h1>
 <p style="font-size:34px;line-height:1.4;color:#DCEFEA;margin-top:30px;max-width:880px">Causes, what to eat, tests and warning signs. In English and हिंदी.</p>
 <div style="position:absolute;right:60px;top:620px;background:#E6F2EF;border-radius:40px;padding:20px">{queasy(360)}</div>
 <div style="position:absolute;left:84px;top:860px">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
  <p style="font-size:28px;color:#CFE5E0;margin-top:22px">Link in bio · Answers</p></div>
 {foot(n, total=N2, light=True)}</div>"""

# ---------------- Instagram 3: Gurpurab, lessons from the langar (HI, single post) ----------------
LG = [("सादा खाना", "दाल, सब्ज़ी, रोटी: पूरी थाली"),
      ("बैठकर, धीरे", "पंगत में आराम से, चबाकर"),
      ("उतना ही लें", "जितना खा सकें, थाली में न छोड़ें"),
      ("सेवा में", "चलते-फिरते पानी पीते रहें")]
WARM = "background:radial-gradient(120% 75% at 50% 20%,#FFF4DE 0%,#FCE3B6 60%,#F7CF8C 100%);color:#12302C"

def lg_rows(size=34, gap=14, lw=260):
    return "".join(f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.72);border-radius:24px;padding:14px 24px;margin-bottom:{gap}px">'
                   f'<span style="flex:none;width:{lw}px;font-family:TD;font-size:{size+2}px;color:#1D4E89;line-height:1.25">{d}</span><span style="font-size:{size}px;line-height:1.3">{t}</span></div>'
                   for d, t in LG)

def lg_post():
    return f"""<div class="s cream hi" style="width:1080px;height:1350px;padding:60px 72px;{WARM}">
 <div class="kick" style="font-size:30px;color:#B5542C;text-align:center">गुरु नानक जयंती · गुरुपर्व</div>
 <h1 style="font-size:76px;margin-top:4px;text-align:center">लंगर की सीख, <em style="color:#0D7466">पेट के लिए भी</em></h1>
 <div style="position:absolute;left:150px;top:230px">{langar(780)}</div>
 <div style="position:absolute;left:72px;right:72px;top:730px">{lg_rows(32, 12)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1090px;font-size:29px;line-height:1.35;color:#4A615D">डायबिटीज़ हो तो मीठे का ध्यान रखें और दवाएँ समय पर लें।</p>
 {foot(hi=True)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:76px 80px">
 <div class="kick" style="font-size:26px;color:#0D7466">Ji machlana</div>
 <h1 style="font-size:84px;margin-top:14px;max-width:620px">Feeling <em>queasy?</em></h1>
 <p style="font-size:32px;line-height:1.35;color:#4A615D;margin-top:24px;max-width:560px">Sips, bland food, small meals. See a doctor if it lasts, or with pain or yellow eyes.</p>
 <div style="position:absolute;right:70px;top:90px">{queasy(470)}</div>
 {foot(pad=80)}</div>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_myth():
    return f"""<div class="s saffron" style="width:1080px;height:1920px;padding:150px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:30px">Myth or fact?</span></div>
 <h1 style="font-size:104px;margin-top:40px">A biopsy makes <em>cancer spread.</em></h1>
 <div style="position:absolute;left:290px;top:560px">{biopsy_view(500, q=False)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1140px">
  <div style="display:inline-block;border:7px solid #B0362B;color:#B0362B;border-radius:20px;padding:4px 30px;transform:rotate(-5deg);font-family:YS;font-size:88px">MYTH</div>
  <p style="font-size:40px;line-height:1.35;margin-top:30px">A biopsy takes a few <b>tiny pieces</b> in seconds and does not spread cancer. <b>Delay</b> is what does harm.</p></div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Play more at drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_nausea():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">Ji machlana</div>
 <h1 style="font-size:112px;margin-top:16px">Feeling <em>queasy?</em></h1>
 <div style="position:absolute;left:230px;top:560px">{queasy(620)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1330px;display:grid;gap:16px">
  {"".join(f'<div style="background:#fff;border-radius:999px;padding:18px 32px;font-size:36px;display:flex;gap:18px;align-items:center"><span style="width:18px;height:18px;border-radius:50%;background:{c};flex:none"></span>{t}</div>' for c, t in (("#0D7466", "Small sips of ORS or water"), ("#0D7466", "Bland food, small meals, sit up"), ("#B0362B", "Lasts a day or more? See a doctor")))}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Read more: drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_gurpurab():
    return f"""<div class="s cream hi" style="width:1080px;height:1920px;padding:150px 72px;{WARM}">
 <div class="kick" style="font-size:34px;color:#B5542C;text-align:center">गुरु नानक जयंती · गुरुपर्व</div>
 <h1 style="font-size:80px;margin-top:10px;text-align:center">लंगर की सीख, <em style="color:#0D7466">पेट के लिए भी</em></h1>
 <div style="position:absolute;left:90px;top:420px">{langar(900)}</div>
 <div style="position:absolute;left:72px;right:72px;top:1010px">{lg_rows(36, 16, 260)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1470px;font-size:36px;line-height:1.35;color:#4A615D;text-align:center">गुरुपर्व की लख-लख बधाइयाँ 🙏</p>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 44px;border-radius:999px">drlochab.com/hi</span></div>
 {foot(pad=72, hi=True)}</div>"""

# ---------------- text ----------------
CAP_MYTH = f"""Myth or fact? "A biopsy makes cancer spread." 🔬

Guess first, then swipe 👉

❌ MYTH. During an endoscopy or colonoscopy, the doctor takes a few tiny pieces of tissue, each only a few millimetres, in a matter of seconds. This does not push cancer cells into the body. The real harm comes from delay: people who refuse a biopsy can lose months while a treatable growth keeps growing.

If a biopsy is advised:
✅ Agree to it. It is quick, and the lining has no pain nerves
📅 Ask when the report will be ready
📄 Collect it and take it back to your doctor
🩺 Most ulcers, growths and polyps can be named and treated properly only once the biopsy result is known

🚩 See a doctor without delay for trouble swallowing, vomiting blood, black stools, blood in the stool or weight loss you can't explain. Vomiting blood, or black stools with dizziness: call 112 or go to the nearest emergency department.

🎮 The next Myth or fact? goes up on Thursday. Play them all at drlochab.com (link in bio), in English and Hindi. What happens in an endoscopy: {MYTH_LINK}

{SIGN}

#MythOrFact #Biopsy #Endoscopy #CancerAwareness #GutHealth #Gastroenterologist #Gurugram #DrLochab"""

CAP_NAUSEA = f"""Feeling queasy? 🤢 Ji machlana is one of the commonest reasons people feel unwell, and most of the time it passes on its own.

The usual reasons: a stomach bug, acidity or a heavy, oily meal, travel and strong smells, or a new medicine. It usually settles in a day or two.

What helps:
💧 Small sips of ORS, water or coconut water every few minutes, not a big glass at once
🍚 Bland food once the vomiting settles: khichdi, toast, idli, banana, curd rice
⏱️ Small meals every 2 to 3 hours
🪑 Stay upright for 2 to 3 hours after eating
💊 Don't keep taking anti-vomiting tablets on your own for days; they can hide the cause

🚩 See a doctor the same day for vomiting for more than a day, not keeping fluids down or passing very little urine, severe belly pain, yellow eyes, a swollen belly with no wind or stool, or nausea with weight loss. Blood in the vomit, chest pain with sweating, or a severe headache with a stiff neck: call 112 or go to the nearest emergency department.

Children under 12 should be seen by their paediatrician, and if you are pregnant and can't keep fluids down, see your doctor the same day.

📖 New on my website, in English and Hindi: {ANS} (link in bio)

{SIGN}

#Nausea #Vomiting #Acidity #StomachBug #GutHealth #Gastroenterologist #Gurugram #DrLochab"""

CAP_GURPURAB = f"""गुरु नानक जयंती: लंगर की सीख, पेट के लिए भी 🙏

मंगलवार 24 नवंबर को गुरुपर्व है। लंगर की परंपरा में सेहत की भी कई सीखें छिपी हैं:

🍲 सादा खाना: दाल, सब्ज़ी और रोटी मिलकर एक पूरी, संतुलित थाली बनाते हैं
🪷 बैठकर, धीरे: पंगत में आराम से बैठकर, अच्छी तरह चबाकर खाने से पेट हल्का रहता है
🤲 उतना ही लें: जितना खा सकें उतना ही लेना, यानी ज़रूरत से ज़्यादा न खाना
💧 सेवा में: लंबे समय खड़े रहकर सेवा करते हुए पानी पीते रहें और भूखे न रहें

डायबिटीज़ हो तो मीठे का ध्यान रखें और अपनी दवाएँ समय पर लें। शादियों के मौसम में पेट और लिवर का ध्यान रखने की पूरी गाइड (हिंदी): {WED_HI} (लिंक बायो में)

सबको गुरुपर्व की लख-लख बधाइयाँ 🙏

{SIGN_HI}

#गुरुपर्व #GuruNanakJayanti #Gurpurab #लंगर #पेटकीसेहत #Gurugram #DrLochab"""

GBP_TEXT = f"""Feeling queasy (ji machlana) or vomiting? Most of the time it comes from a stomach bug, acidity, a heavy meal, travel or a new medicine, and settles in a day or two.

What helps: small sips of ORS or water every few minutes, bland food such as khichdi, toast or idli once the vomiting settles, small meals every 2 to 3 hours, and staying upright after eating. Avoid taking anti-vomiting tablets on your own for days.

See a doctor the same day if vomiting lasts more than a day, fluids do not stay down, there is severe belly pain or yellow eyes, or nausea keeps coming back with weight loss. Blood in the vomit, chest pain with sweating, or a severe headache is an emergency: call 112.

Read the full answer, with what to eat and common questions, in English and Hindi.

Button: Learn more → https://{ANS}/"""

WA_EN = f"""🩺 *Feeling queasy (ji machlana)?*

Nausea and vomiting usually come from a stomach bug, acidity, a heavy meal, travel or a new medicine, and settle in a day or two with small sips of fluid and light food. I've written a short, plain answer on what helps at home, what to eat, and the warning signs that need a doctor the same day:

👉 https://{ANS}/
हिंदी में: https://{ANS_HI}/

– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)"""

WA_HI = f"""🩺 *जी मिचलाना या उल्टी?*

ज़्यादातर यह पेट के इंफ़ेक्शन, एसिडिटी, भारी खाने, सफ़र या किसी नई दवा से होता है, और घूँट-घूँट पानी और हल्के खाने से एक-दो दिन में ठीक हो जाता है। घर पर क्या मदद करता है, क्या खाएँ, और कब उसी दिन डॉक्टर को दिखाएँ, आसान भाषा में यहाँ पढ़ें:

👉 https://{ANS_HI}/

गुरुपर्व की लख-लख बधाइयाँ 🙏
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, गुरुग्राम (drlochab.com/hi)"""

if __name__ == "__main__":
    import week_2026_11_09 as w9
    w9.OUT = OUT   # render() writes its temporary page into OUT
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([m1, m2, m3, m4, m5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig1-myth-biopsy-{i}.png", b)
        for i, f in enumerate([v1, v2, v3, v4, v5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig2-nausea-vomiting-{i}.png", b)
        render(lg_post, 1080, 1350, f"{OUT}/ig3-gurpurab-langar-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business-nausea.png", b)
        render(st_myth, 1080, 1920, f"{OUT}/wa-status-1-myth-biopsy.png", b)
        render(st_gurpurab, 1080, 1920, f"{OUT}/wa-status-2-gurpurab-hi.png", b)
        render(st_nausea, 1080, 1920, f"{OUT}/wa-status-3-nausea.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("ig1-caption.txt", CAP_MYTH), ("ig2-caption.txt", CAP_NAUSEA), ("ig3-caption-hi.txt", CAP_GURPURAB),
                      ("google-business-post.txt", GBP_TEXT), ("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
