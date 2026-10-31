"""Social content for the week of 2 to 8 Nov 2026 (Dhanteras Fri 6 Nov, Diwali Sun 8 Nov).
Instagram: "Myth or fact?" carousel (EN, Myth Buster entry of Mon 2 Nov: a normal ultrasound and the stomach),
pain under the right ribs carousel (EN, the week's new answer page), Diwali "5 days, 5 diyas" post (HI).
Google Business Profile: pain under the right ribs (1200x900). WhatsApp Status: 3 images (1080x1920). Captions and messages as .txt.
Original drawings only (organ outlines reuse hub.py). No doses, no brand names, no phone number in the Google post text.
Run from anywhere: python3 _src/social/week_2026_11_02.py  -> _src/out/week-2026-11-02/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC
from week_2026_10_26 import plate_small, no_pill
from new_tools_promo import phone
from diwali_mithai_box import DEFS, diya
import hub
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-11-02"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/pain-under-right-ribs"
SIGN = ("Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Fellowship in EUS and ERCP), Gurugram. "
        "HMC Reg. No. HN-23524. Prepared with AI assistance and reviewed by Dr. Lochab.")
SIGN_HI = ("डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP फ़ेलोशिप), गुरुग्राम। "
           "HMC रजि. नं. HN-23524। AI की सहायता से तैयार और डॉ. लोचब द्वारा समीक्षित।")

# ---------------- original drawings ----------------
def usg(w=600, q=True, labels=False):
    """Ultrasound: a probe on top, the fan-shaped scan below. The liver shows clearly; the stomach is hidden behind gas bubbles (viewBox 0 0 600 620)."""
    bub = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F4F8F7" stroke="#C9D9D5" stroke-width="3"/><circle cx="{x-r*.35:.0f}" cy="{y-r*.35:.0f}" r="{r*.25:.0f}" fill="#fff"/>'
                  for x, y, r in [(372, 330, 46), (420, 300, 38), (446, 360, 42), (398, 392, 40), (350, 384, 30), (470, 318, 26), (430, 420, 28)])
    speck = "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#7FA19A" opacity=".55"/>' for x, y in
                    [(170, 300), (196, 330), (150, 350), (220, 300), (182, 380), (236, 352), (206, 408), (160, 410), (250, 400), (226, 440)])
    lab = ""
    if labels:
        lab = ('<g font-family="FT" font-weight="600" font-size="30">'
               '<rect x="40" y="520" width="210" height="56" rx="28" fill="#0D7466"/><text x="145" y="558" text-anchor="middle" fill="#fff">Liver: seen</text>'
               '<rect x="290" y="520" width="270" height="56" rx="28" fill="#B0362B"/><text x="425" y="558" text-anchor="middle" fill="#fff">Stomach: hidden</text></g>')
    qm = ('<g transform="translate(500 160)"><circle r="64" fill="#12302C"/><text x="0" y="32" text-anchor="middle" font-family="YS" font-size="96" fill="#F3B84A">?</text></g>' if q else "")
    return f"""<svg viewBox="0 0 600 620" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="fan"><path d="M300 150 L80 470 A330 330 0 0 0 520 470 Z"/></clipPath>
<filter id="us" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#062F2A" flood-opacity=".3"/></filter></defs>
<path d="M300 150 L80 470 A330 330 0 0 0 520 470 Z" fill="#163A35" filter="url(#us)"/>
<g clip-path="url(#fan)">
 <path d="M300 150 L80 470 A330 330 0 0 0 520 470 Z" fill="url(#none)" opacity="0"/>
 {"".join(f'<path d="M{300-r*0.69:.0f} {150+r*0.72:.0f} A{r} {r} 0 0 0 {300+r*0.69:.0f} {150+r*0.72:.0f}" fill="none" stroke="#2C5A53" stroke-width="3" stroke-dasharray="6 12"/>' for r in range(80, 360, 60))}
 <path d="M120 300 C150 250 250 250 290 280 C300 330 270 400 230 440 C190 470 130 450 116 400 C108 360 108 330 120 300 Z" fill="#9CB8B1"/>{speck}
 <path d="M340 290 C380 270 460 280 480 330 C500 390 460 440 400 446 C360 450 330 420 330 380 Z" fill="none" stroke="#E79A8E" stroke-width="7" stroke-dasharray="14 10"/>
 {bub}
</g>
<g transform="translate(300 150)">
 <path d="M-90 0 Q-90 -26 -64 -26 H64 Q90 -26 90 0 Z" fill="#0D7466"/>
 <rect x="-56" y="-120" width="112" height="100" rx="30" fill="#E6F2EF" stroke="#0D7466" stroke-width="8"/>
 <path d="M0 -120 C0 -150 40 -150 80 -140 C120 -130 150 -130 170 -150" fill="none" stroke="#12302C" stroke-width="10" stroke-linecap="round"/>
 <rect x="-30" y="-92" width="60" height="10" rx="5" fill="#9CB8B1"/></g>
{qm}{lab}</svg>"""

def scope_view(w=420):
    """Looking through an endoscope: the pink stomach lining with folds and a small ulcer, seen clearly (viewBox 0 0 420 420)."""
    folds = "".join(f'<path d="M{40+i*60} 60 C{70+i*60} 180 {20+i*60} 260 {60+i*60} 380" fill="none" stroke="#E58E86" stroke-width="16" stroke-linecap="round" opacity=".7"/>' for i in range(6))
    return f"""<svg viewBox="0 0 420 420" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><clipPath id="sc"><circle cx="210" cy="210" r="180"/></clipPath>
<radialGradient id="lin" cx=".45" cy=".42" r=".65"><stop offset="0" stop-color="#FFD9D2"/><stop offset=".6" stop-color="#F4A99F"/><stop offset="1" stop-color="#9C4A42"/></radialGradient></defs>
<circle cx="210" cy="210" r="200" fill="#12302C"/>
<g clip-path="url(#sc)"><rect width="420" height="420" fill="url(#lin)"/>{folds}
<ellipse cx="250" cy="250" rx="40" ry="30" fill="#C2453A"/><ellipse cx="250" cy="250" rx="26" ry="18" fill="#FFF6E6"/></g>
<circle cx="210" cy="210" r="180" fill="none" stroke="#0D7466" stroke-width="10"/>
<circle cx="250" cy="250" r="58" fill="none" stroke="#F3B84A" stroke-width="7" stroke-dasharray="12 9"/></svg>"""

def torso(w=600, burst=True):
    """Front view of the trunk with the rib cage over the liver, gallbladder and stomach (hub.py outlines) and a pain burst under the right ribs.
    The person's right side is on the viewer's left, as in an anatomy chart (viewBox 0 40 320 400)."""
    ribs = ""
    for i in range(5):
        y = 92 + i * 30
        ribs += (f'<path d="M156 {y} C120 {y-6} 70 {y+4} 50 {y+40}" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".8"/>'
                 f'<path d="M164 {y} C200 {y-6} 250 {y+4} 270 {y+40}" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".8"/>')
    ribs += ('<path d="M160 84 V180" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" opacity=".85"/>'
             '<path d="M156 182 C130 220 90 236 58 246 M164 182 C190 220 230 236 262 246" fill="none" stroke="#FFFFFF" stroke-width="8" stroke-linecap="round" opacity=".8"/>')
    rings = ("".join(f'<circle cx="112" cy="232" r="{r}" fill="none" stroke="#E0503D" stroke-width="4" opacity="{o}"/>' for r, o in [(30, .9), (44, .55), (58, .3)])
             + '<path d="M112 206 L118 224 L136 220 L124 234 L136 248 L118 244 L112 262 L106 244 L88 248 L100 234 L88 220 L106 224 Z" fill="#F3B84A" stroke="#B0362B" stroke-width="3" stroke-linejoin="round"/>') if burst else ""
    return f"""<svg viewBox="0 40 320 400" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<path d="M70 50 C110 40 210 40 250 50 C290 70 300 120 296 200 C292 280 280 360 270 430 H50 C40 360 28 280 24 200 C20 120 30 70 70 50 Z" fill="#F6CDB5" stroke="#CF8B62" stroke-width="5"/>
<path d="{hub.COLON}" fill="none" stroke="#CF8B62" stroke-width="14" stroke-linecap="round" opacity=".5"/>
<path d="{hub.SMALL}" fill="none" stroke="#E7A987" stroke-width="9" stroke-linecap="round" opacity=".6"/>
<path d="{hub.PANC}" fill="#F3CF7A" stroke="#C49A35" stroke-width="3"/>
<path d="{hub.STOM}" fill="#F4B6AE" stroke="#D9776B" stroke-width="4"/>
<path d="{hub.LIVER}" fill="#D98C72" stroke="#A9523D" stroke-width="4"/>
<path d="{hub.GB}" fill="#AFD27E" stroke="#6E9A3A" stroke-width="4"/>
{ribs}{rings}
<g font-family="FT" font-weight="600" font-size="15" fill="#4A615D"><text x="34" y="424">RIGHT</text><text x="286" y="424" text-anchor="end">LEFT</text></g></svg>"""

def mini(kind, w=120):
    """Small icons for the four usual causes."""
    body = dict(
        gb=f'<g transform="translate(-311 -650) scale(3)"><path d="{hub.GB}" fill="#AFD27E" stroke="#6E9A3A" stroke-width="1.5"/></g>'
           '<circle cx="74" cy="80" r="11" fill="#F3B84A" stroke="#8A5A12" stroke-width="3"/><circle cx="62" cy="102" r="9" fill="#F3B84A" stroke="#8A5A12" stroke-width="3"/><circle cx="82" cy="104" r="7" fill="#F3B84A" stroke="#8A5A12" stroke-width="3"/>',
        liver=f'<g transform="translate(-45.6 -96.6) scale(.85)"><path d="{hub.LIVER}" fill="#D98C72" stroke="#A9523D" stroke-width="4"/></g>',
        stomach=f'<g transform="translate(-145 -154) scale(1.05)"><path d="{hub.STOM}" fill="#F4B6AE" stroke="#D9776B" stroke-width="4"/></g>',
        rib=''.join(f'<path d="M20 {30+i*26} C60 {18+i*26} 100 {22+i*26} 124 {44+i*26}" fill="none" stroke="#FFFFFF" stroke-width="11" stroke-linecap="round"/>' for i in range(3))
            + '<path d="M80 56 L88 74 L106 70 L92 84 L100 102 L84 92 L70 104 L74 86 L58 78 L76 74 Z" fill="#F3B84A"/>')[kind]
    return f'<svg viewBox="0 0 140 140" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def notebook(w=140):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><rect x="12" y="6" width="40" height="52" rx="6" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<path d="M20 20 H44 M20 30 H44 M20 40 H36" stroke="#9FB8B2" stroke-width="3" stroke-linecap="round"/>'
            '<g transform="rotate(35 46 44)"><rect x="42" y="22" width="9" height="30" rx="2" fill="#F3B84A" stroke="#12302C" stroke-width="2.5"/><path d="M42 52 L46.5 60 L51 52 Z" fill="#12302C"/></g></svg>')

def no_drop(w=140):
    """A 'stone-dissolving' bottle crossed out."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#B0362B" stroke-width="4"/>'
            '<rect x="24" y="22" width="16" height="26" rx="4" fill="#C9D98A" stroke="#12302C" stroke-width="2.5"/><rect x="27" y="14" width="10" height="9" rx="2" fill="#12302C"/>'
            '<circle cx="30" cy="36" r="3" fill="#8A5A12"/><circle cx="35" cy="41" r="2.4" fill="#8A5A12"/>'
            '<path d="M13 51 L51 13" stroke="#B0362B" stroke-width="4.5" stroke-linecap="round"/></svg>')

def dot_list(items, size=40, col="#B0362B", gap=22):
    return "".join(f'<div style="display:flex;gap:22px;align-items:center;font-size:{size}px;line-height:1.25;margin-top:{gap}px"><span style="flex:none;width:22px;height:22px;border-radius:50%;background:{col}"></span>{s}</div>' for s in items)

# ---------------- Instagram 1: Myth or fact? (EN, 5 slides) ----------------
N1 = 5
def m1(n=1):
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:28px">Myth or fact?</span></div>
 <h1 style="font-size:96px;margin-top:40px;max-width:920px">My ultrasound is normal, so my <em>stomach is fine.</em></h1>
 <div style="position:absolute;left:250px;top:500px">{usg(580)}</div>
 <div style="position:absolute;left:84px;top:1120px;font-size:34px;font-weight:600;color:#B5542C">Guess first, then swipe →</div>
 {foot(n, total=N1)}</div>"""

def m2(n=2):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;border:8px solid #F3B84A;color:#F3B84A;border-radius:22px;padding:6px 36px;transform:rotate(-6deg);font-family:YS;font-size:120px;line-height:1.1">MYTH</div>
 <h1 style="font-size:76px;margin-top:44px;max-width:920px">An ultrasound <em>can't see</em> the stomach lining.</h1>
 <div style="position:absolute;left:270px;top:500px;background:#E6F2EF;border-radius:48px;padding:20px 20px 4px">{usg(500, q=False, labels=True)}</div>
 <p style="position:absolute;left:84px;right:84px;top:1080px;font-size:32px;line-height:1.35;color:#DCEFEA">Gas in the gut blocks the view. Ulcers and gastritis can be missed.</p>
 {foot(n, total=N1, light=True)}</div>"""

def m3(n=3):
    chip = lambda big, t: (f'<div style="background:#fff;border-radius:28px;padding:22px 30px"><div style="font-family:YS;font-size:46px;line-height:1.05">{big}</div>'
                           f'<div style="font-size:30px;color:#4A615D;margin-top:6px">{t}</div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What to do</div>
 <h2 style="font-size:78px;margin:14px 0 20px;max-width:900px">Symptoms keep <em>coming back?</em></h2>
 <p style="font-size:34px;line-height:1.35;color:#4A615D;max-width:880px">Acidity, upper belly pain or vomiting: ask your doctor about a look from inside.</p>
 <div style="position:absolute;left:84px;top:520px">{scope_view(440)}</div>
 <div style="position:absolute;left:560px;right:84px;top:560px;display:grid;gap:22px">
  {chip("Endoscopy", "sees the lining directly")}{chip("H. pylori test", "breath or stool")}</div>
 {foot(n, total=N1)}</div>"""

def m4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor soon for</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Signs that need <em>a check</em></h2>
 {dot_list(["Difficulty swallowing", "Vomiting blood", "Black, sticky stools", "Weight loss without trying", "New symptoms after 50"])}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Vomiting blood or feeling faint? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N1)}</div>"""

def mb_screen():
    return ('<div style="font-size:15px;font-weight:600;letter-spacing:.12em;color:#0D7466">MYTH BUSTER · THURSDAY</div>'
            '<div style="font-family:YS;font-size:28px;color:#12302C;line-height:1.15;margin:14px 0 18px">Upper belly pain spreading to the back can mean pancreatitis.</div>'
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

# ---------------- Instagram 2: Pain under the right ribs (EN, 5 slides) ----------------
N2 = 5
def r1(n=1):
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Right upper belly</div>
 <h1 style="font-size:100px;margin-top:16px;max-width:900px">Pain under the <em>right ribs?</em></h1>
 <p style="font-size:36px;line-height:1.35;color:#4A615D;margin-top:22px;max-width:800px">Liver, gallbladder, or something else?</p>
 <div style="position:absolute;left:260px;top:490px">{torso(560)}</div>
 {foot(n, total=N2)}</div>"""

def r2(n=2):
    tile = lambda k, a, b: (f'<div style="background:rgba(255,255,255,.1);border-radius:30px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;gap:12px">{mini(k, 120)}'
                            f'<div style="font-family:YS;font-size:44px;color:#F3B84A;line-height:1.05">{a}</div><div style="font-size:29px;color:#DCEFEA;line-height:1.3">{b}</div></div>')
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">The usual suspects</div>
 <h2 style="font-size:80px;margin:14px 0 40px">Four common <em>causes</em></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {tile("gb", "Gallstones", "attacks, often after a heavy meal")}{tile("liver", "Liver", "hepatitis or abscess, often with fever")}
  {tile("stomach", "Stomach", "ulcer or gastritis: burning, linked to meals")}{tile("rib", "Muscle or rib", "worse on pressing or twisting")}</div>
 {foot(n, total=N2, light=True)}</div>"""

def r3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:22px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:48px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Until you see a doctor</div>
 <h2 style="font-size:84px;margin:14px 0 40px">Keep it <em>simple</em></h2>
 <div style="display:grid;gap:22px">
  {row(notebook(130), "Note it down", "when it comes, how long, what you ate")}
  {row(plate_small(130), "Lighter meals", "skip heavy, fried food and alcohol")}
  {row(no_pill(130), "No painkillers on your own", "some cause ulcers or harm the liver")}
  {row(no_drop(130), "No stone-dissolving cures", "they don't work")}
 </div>
 <p style="font-size:30px;line-height:1.35;color:#4A615D;margin-top:30px">The usual first test is an ultrasound of the abdomen.</p>
 {foot(n, total=N2)}</div>"""

def r4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor the same day</div>
 <h2 style="font-size:84px;margin:14px 0 26px">When the pain <em>comes with</em></h2>
 {dot_list(["Pain for more than 4 to 6 hours", "Fever or shivering", "Yellow eyes or dark urine", "Repeated vomiting", "Pain going through to the back"])}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Severe pain with fainting, or chest pain with sweating? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N2)}</div>"""

def r5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on the website</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:900px">Pain under the right ribs: <em>the full answer</em></h1>
 <p style="font-size:34px;line-height:1.4;color:#DCEFEA;margin-top:30px;max-width:880px">Causes, clues, tests, what to eat, and when to worry. In English and हिंदी.</p>
 <div style="position:absolute;right:60px;top:600px;background:#E6F2EF;border-radius:40px;padding:16px">{torso(340)}</div>
 <div style="position:absolute;left:84px;top:820px">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
  <p style="font-size:28px;color:#CFE5E0;margin-top:22px">Link in bio · Answers</p></div>
 {foot(n, total=N2, light=True)}</div>"""

# ---------------- Instagram 3: Diwali, 5 days 5 diyas (HI, single post) ----------------
DAYS = [("धनतेरस", "कुछ खाकर ही बाज़ार निकलें"), ("छोटी दिवाली", "मीठे पेय कम, पानी और छाछ ज़्यादा"),
        ("दिवाली", "थाली में पहले सलाद और दाल"), ("गोवर्धन पूजा", "बचा खाना 2 घंटे में फ्रिज में"), ("भाई दूज", "एक दिन हल्का: खिचड़ी, दाल, फल")]
NIGHT = "background:radial-gradient(120% 70% at 50% 18%,#13574F 0%,#0B3F39 55%,#072B27 100%)"

def diya_row(size=150, step=186, top=0):
    lift = [40, 12, 0, 12, 40]
    return "".join(diya(size, f"left:{i * step}px;top:{top + lift[i]}px") for i in range(5))

def dw_rows(size=34, gap=14, lw=200):
    return "".join(f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.08);border-radius:24px;padding:14px 24px;margin-bottom:{gap}px">'
                   f'<span style="flex:none;width:{lw}px;font-family:TD;font-size:{size+4}px;color:#F3B84A">{d}</span><span style="font-size:{size}px;line-height:1.3">{t}</span></div>'
                   for d, t in DAYS)

def dw_post():
    return f"""<div class="s teal hi" style="width:1080px;height:1350px;padding:64px 72px;{NIGHT}">{DEFS}
 <div class="kick" style="font-size:30px;color:#F3B84A;text-align:center">दिवाली · रविवार 8 नवंबर</div>
 <h1 style="font-size:78px;margin-top:6px;text-align:center">पाँच दिन, पाँच दीये, <em>पेट रहे ख़ुश</em></h1>
 <div style="position:absolute;left:110px;top:250px;width:880px;height:240px">{diya_row(160, 180)}</div>
 <div style="position:absolute;left:72px;right:72px;top:540px">{dw_rows(36, 16)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1075px;font-size:31px;line-height:1.35;color:#F7DCC0">पीठ तक जाता तेज़ पेट दर्द और उल्टी? घर पर इलाज न करें, 112 पर कॉल करें।</p>
 {foot(light=True, hi=True)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:76px 80px">
 <div class="kick" style="font-size:26px;color:#0D7466">Right upper belly</div>
 <h1 style="font-size:80px;margin-top:14px;max-width:620px">Pain under the <em>right ribs?</em></h1>
 <p style="font-size:32px;line-height:1.35;color:#4A615D;margin-top:24px;max-width:560px">Gallstones, liver, stomach or muscle: the clues, the tests, and when to worry.</p>
 <div style="position:absolute;right:70px;top:110px">{torso(440)}</div>
 {foot(pad=80)}</div>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_myth():
    return f"""<div class="s saffron" style="width:1080px;height:1920px;padding:150px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:30px">Myth or fact?</span></div>
 <h1 style="font-size:96px;margin-top:40px">Normal ultrasound, so my <em>stomach is fine.</em></h1>
 <div style="position:absolute;left:290px;top:560px">{usg(500, q=False, labels=True)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1120px">
  <div style="display:inline-block;border:7px solid #B0362B;color:#B0362B;border-radius:20px;padding:4px 30px;transform:rotate(-5deg);font-family:YS;font-size:88px">MYTH</div>
  <p style="font-size:40px;line-height:1.35;margin-top:30px">Gas hides the stomach lining. Symptoms keep coming back? Ask about an <b>endoscopy</b> or an <b>H. pylori test</b>.</p></div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Play more at drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_diwali():
    return f"""<div class="s teal hi" style="width:1080px;height:1920px;padding:150px 72px;{NIGHT}">{DEFS}
 <div class="kick" style="font-size:34px;color:#F3B84A;text-align:center">दिवाली · रविवार 8 नवंबर</div>
 <h1 style="font-size:76px;margin-top:10px;text-align:center">पाँच दिन, पाँच दीये, <em>पेट रहे ख़ुश</em></h1>
 <div style="position:absolute;left:60px;top:400px;width:960px;height:260px">{diya_row(180, 195)}</div>
 <div style="position:absolute;left:72px;right:72px;top:720px">{dw_rows(42, 22, 270)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1470px;font-size:36px;line-height:1.35;color:#F7DCC0">पीठ तक जाता तेज़ पेट दर्द और उल्टी? 112 पर कॉल करें।</p>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#F3B84A;color:#12302C;font-family:YS;font-size:56px;padding:14px 44px;border-radius:999px">drlochab.com/hi</span></div>
 {foot(light=True, pad=72, hi=True)}</div>"""

def st_ribs():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">Right upper belly</div>
 <h1 style="font-size:108px;margin-top:16px">Pain under the <em>right ribs?</em></h1>
 <div style="position:absolute;left:260px;top:570px">{torso(560)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1300px;display:grid;gap:16px">
  {"".join(f'<div style="background:#fff;border-radius:999px;padding:18px 32px;font-size:36px;display:flex;gap:18px;align-items:center"><span style="width:18px;height:18px;border-radius:50%;background:{c};flex:none"></span>{t}</div>' for c, t in (("#0D7466", "Attacks after heavy meals? Think gallstones"), ("#0D7466", "Usual first test: an ultrasound"), ("#B0362B", "Fever or yellow eyes? Same-day check")))}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Read more: drlochab.com</span></div>
 {foot(pad=84)}</div>"""

# ---------------- text ----------------
CAP_MYTH = f"""Myth or fact? "My ultrasound is normal, so my stomach is fine." 🩻

Guess first, then swipe 👉

❌ MYTH. An ultrasound is very good for the liver, gallbladder and kidneys. But gas in the stomach and intestines blocks the view of their inner lining, so ulcers, gastritis, damage from H. pylori and even early stomach cancer can be missed on a normal ultrasound.

What to do:
🔁 If acidity, upper belly pain or vomiting keep coming back, ask your doctor whether you need an endoscopy (it sees the lining directly) or an H. pylori test (breath or stool).

🚩 See a doctor soon for difficulty swallowing, vomiting blood, black stools, weight loss without trying, or new symptoms after 50. Vomiting blood or feeling faint? Call 112.

🎮 Next Myth or fact? goes up on Thursday. Play them all at drlochab.com (link in bio), in English and Hindi.

{SIGN}

#MythOrFact #Ultrasound #Endoscopy #Acidity #HPylori #GutHealth #Gastroenterologist #Gurugram"""

CAP_RIBS = f"""Pain under the right ribs? Here's how doctors think about it. 🩺

The right upper belly holds the liver and the gallbladder, close to the stomach, and all of it sits under the ribs. The four usual suspects:

🟢 Gallstones: attacks of pain, often after a heavy or fried meal or at night, sometimes going to the right shoulder or back
🟤 Liver: hepatitis or a liver abscess, often with fever (fatty liver rarely causes real pain)
🔴 Stomach: an ulcer or gastritis, a burning pain linked to meals
⚪ Muscle or rib: worse when you press one spot, twist or breathe deeply

Until you see a doctor: note when it comes and what you ate, keep meals light, skip alcohol, don't take painkillers on your own, and don't try "stone-dissolving" remedies. The usual first test is an ultrasound of the abdomen.

🚩 Same-day check for pain lasting more than 4 to 6 hours, fever or shivering, yellow eyes or dark urine, repeated vomiting, or pain going through to the back. Severe pain with fainting, or chest pain with sweating, is an emergency: call 112.

📖 New on my website, in English and Hindi: {ANS} (link in bio)

{SIGN}

#AbdominalPain #Gallstones #LiverHealth #FattyLiver #GutHealth #Gastroenterologist #Gurugram #DrLochab"""

CAP_DIWALI = f"""दिवाली के पाँच दिन, पाँच दीये, और पेट रहे ख़ुश 🪔

धनतेरस (शुक्रवार 6 नवंबर) से भाई दूज तक, हर दिन के लिए एक छोटी-सी बात:

🪔 धनतेरस: बाज़ार कुछ खाकर निकलें, ताकि भूख में चाट-समोसे पर टूट न पड़ें
🪔 छोटी दिवाली: कोल्ड ड्रिंक और मीठे पेय कम, पानी, नींबू पानी और छाछ ज़्यादा
🪔 दिवाली (रविवार 8 नवंबर): पूजा के बाद थाली में पहले सलाद और दाल, फिर बाकी खाना और थोड़ी मिठाई
🪔 गोवर्धन पूजा: अन्नकूट का बचा खाना 2 घंटे के अंदर फ्रिज में रखें
🪔 भाई दूज: त्योहार के बाद एक दिन हल्का खाना: खिचड़ी, दाल, दही, फल

🚩 पेट के ऊपर तेज़ दर्द जो पीठ तक जाए, साथ में उल्टी हो, तो घर पर गैस की दवा लेते न रहें: 112 पर कॉल करें या नज़दीकी इमरजेंसी में जाएँ।

मिठाई, डायबिटीज़ और पूरे दिन के प्लान के साथ दिवाली गाइड (हिंदी): drlochab.com/hi/guides/diwali-food-guide (लिंक बायो में)

आप सभी को दीपावली की शुभकामनाएँ ✨

{SIGN_HI}

#दिवाली #Diwali2026 #धनतेरस #पेटकीसेहत #एसिडिटी #GutHealth #Gurugram #DrLochab"""

GBP_TEXT = f"""Pain under the right ribs? It is a common worry, and the cause can usually be found with a simple check-up.

The right upper belly holds the liver and the gallbladder, close to the stomach. The usual causes are gallstones (attacks of pain, often after a heavy meal), the liver (hepatitis or an abscess, often with fever), an ulcer or gastritis (burning linked to meals), and a strained muscle or rib. The usual first test is an ultrasound of the abdomen, with blood tests.

Until you see a doctor, note when the pain comes, keep meals light, avoid alcohol, and do not take painkillers or "stone-dissolving" remedies on your own.

See a doctor the same day for pain lasting more than 4 to 6 hours, fever, yellow eyes, dark urine or repeated vomiting. Severe pain with fainting, or chest pain with sweating, is an emergency: call 112.

Read the full answer, with a diet guide and common questions, in English and Hindi.

Button: Learn more → https://{ANS}/"""

WA_EN = f"""🩺 *Pain under the right ribs?*

It's one of the commonest worries I hear about: is it the liver, the gallbladder, or just gas? I've written a short, plain answer on the usual causes, the clues from the type of pain, the tests, what to eat, and the signs that need a same-day check:

👉 https://{ANS}/
हिंदी में: https://drlochab.com/hi/answers/pain-under-right-ribs/

Wishing you and your family a happy and healthy Diwali 🪔
– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)"""

WA_HI = """🩺 *दाईं पसलियों के नीचे दर्द?*

यह सबसे आम सवालों में से है: लिवर है, पित्ताशय है, या बस गैस? आम वजहें, दर्द के तरीक़े से मिलने वाले संकेत, जाँचें, क्या खाएँ, और कब उसी दिन दिखाना ज़रूरी है, यह सब आसान भाषा में यहाँ पढ़ें:

👉 https://drlochab.com/hi/answers/pain-under-right-ribs/

आपको और आपके परिवार को दीपावली की शुभकामनाएँ 🪔
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
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig1-myth-ultrasound-{i}.png", b)
        for i, f in enumerate([r1, r2, r3, r4, r5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig2-right-ribs-{i}.png", b)
        render(dw_post, 1080, 1350, f"{OUT}/ig3-diwali-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business-right-ribs.png", b)
        render(st_myth, 1080, 1920, f"{OUT}/wa-status-1-myth-ultrasound.png", b)
        render(st_diwali, 1080, 1920, f"{OUT}/wa-status-2-diwali-hi.png", b)
        render(st_ribs, 1080, 1920, f"{OUT}/wa-status-3-right-ribs.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("ig1-caption.txt", CAP_MYTH), ("ig2-caption.txt", CAP_RIBS), ("ig3-caption-hi.txt", CAP_DIWALI),
                      ("google-business-post.txt", GBP_TEXT), ("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
