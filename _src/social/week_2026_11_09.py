"""Social content for the week of 9 to 15 Nov 2026 (Govardhan Puja Tue 10, Bhai Dooj Wed 11, Chhath Puja Fri 13 to Mon 16 Nov).
Instagram: "Myth or fact?" carousel (EN, Myth Buster entry of Mon 9 Nov: chest pain after a heavy meal is just gas),
loss of appetite carousel (EN, the week's new answer page), Chhath Puja nirjala fast post (HI).
Google Business Profile: loss of appetite (1200x900). WhatsApp Status: 3 images (1080x1920). Captions and messages as .txt.
Original drawings only (stomach outline reuses hub.py). No doses, no brand names, no phone number in the Google post text.
Run from anywhere: python3 _src/social/week_2026_11_09.py  -> _src/out/week-2026-11-09/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC
from week_2026_10_26 import plate_small, no_pill
from week_2026_11_02 import dot_list
from new_tools_promo import phone
from diwali_mithai_box import DEFS, diya
import hub
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-11-09"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/loss-of-appetite"
ANS_HI = "drlochab.com/hi/answers/loss-of-appetite"
MYTH_LINK = "drlochab.com/answers/when-is-acidity-serious"
FAST_HI = "drlochab.com/hi/guides/navratri-fasting-guide"
SIGN = ("Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Fellowship in EUS and ERCP), Gurugram. "
        "HMC Reg. No. HN-23524. Prepared with AI assistance and reviewed by Dr. Lochab.")
SIGN_HI = ("डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP फ़ेलोशिप), गुरुग्राम। "
           "HMC रजि. नं. HN-23524। AI की सहायता से तैयार और डॉ. लोचब द्वारा समीक्षित।")

# ---------------- original drawings ----------------
HEART = "M300 520 C230 460 120 390 120 280 C120 210 170 170 225 170 C262 170 288 190 300 220 C312 190 338 170 375 170 C430 170 480 210 480 280 C480 390 370 460 300 520 Z"

def heart_gas(w=600, q=True, stamp=False):
    """A heart half-hidden behind a cloud of gas bubbles, above a heavy plate (viewBox 0 0 600 640)."""
    bub = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" fill-opacity=".82" stroke="#C9D9D5" stroke-width="4"/>'
                  f'<circle cx="{x-r*.35:.0f}" cy="{y-r*.35:.0f}" r="{r*.22:.0f}" fill="#fff"/>'
                  for x, y, r in [(150, 360, 70), (230, 410, 62), (110, 450, 46), (300, 455, 48), (190, 300, 44), (370, 470, 34)])
    qm = ('<g transform="translate(470 150)"><circle r="62" fill="#12302C"/><text x="0" y="31" text-anchor="middle" font-family="YS" font-size="92" fill="#F3B84A">?</text></g>' if q else "")
    st = ('<g transform="translate(300 330) rotate(-8)"><rect x="-150" y="-50" width="300" height="100" rx="18" fill="none" stroke="#B0362B" stroke-width="10"/>'
          '<text x="0" y="28" text-anchor="middle" font-family="YS" font-size="78" fill="#B0362B">HEART?</text></g>' if stamp else "")
    return f"""<svg viewBox="0 0 600 640" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="hg" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#F28C7E"/><stop offset=".6" stop-color="#D9473A"/><stop offset="1" stop-color="#9E2A22"/></radialGradient>
<filter id="hs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="12" flood-color="#5A1A14" flood-opacity=".3"/></filter></defs>
<path d="{HEART}" fill="url(#hg)" filter="url(#hs)"/>
<path d="M190 250 C200 220 225 205 250 208" fill="none" stroke="#fff" stroke-width="12" stroke-linecap="round" opacity=".55"/>
<path d="M330 330 H370 L392 280 L420 390 L442 330 H480" fill="none" stroke="#FFF6E6" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
{bub}
<g transform="translate(300 580)"><ellipse rx="230" ry="44" fill="#E7DCC8"/><ellipse rx="196" ry="32" fill="#fff"/>
<ellipse cx="-90" cy="-6" rx="56" ry="20" fill="#E9B44C"/><ellipse cx="0" cy="-10" rx="62" ry="22" fill="#C0702E"/><ellipse cx="96" cy="-6" rx="52" ry="19" fill="#F1E2B8"/>
<ellipse cx="-30" cy="-26" rx="40" ry="14" fill="#E39B3A"/><ellipse cx="50" cy="-26" rx="36" ry="13" fill="#B85C24"/></g>
{qm}{st}</svg>"""

def ecg(w=900, col="#B0362B", bg="#FFFFFF"):
    """An ECG strip on graph paper (viewBox 0 0 900 260)."""
    grid = "".join(f'<path d="M{x} 0 V260" stroke="#F2C9C3" stroke-width="2"/>' for x in range(0, 901, 30)) + \
           "".join(f'<path d="M0 {y} H900" stroke="#F2C9C3" stroke-width="2"/>' for y in range(0, 261, 30))
    beat = lambda x: f"L{x} 150 L{x+20} 150 L{x+35} 130 L{x+50} 150 L{x+70} 150 L{x+82} 170 L{x+100} 40 L{x+118} 200 L{x+132} 150 L{x+170} 150 L{x+195} 118 L{x+220} 150"
    d = "M0 150 " + " ".join(beat(x) for x in (40, 320, 600)) + " L900 150"
    return (f'<svg viewBox="0 0 900 260" style="width:{w}px;border-radius:24px;background:{bg}" xmlns="http://www.w3.org/2000/svg">{grid}'
            f'<path d="{d}" fill="none" stroke="{col}" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/></svg>')

def hunger_meter(w=600, needle=-62):
    """A hunger gauge with the needle near empty, above a plate with one small piece of roti (viewBox 0 0 600 600)."""
    segs = ""
    cols = ["#B0362B", "#E0703D", "#F3B84A", "#9CCB6B", "#0D7466"]
    import math
    for i, c in enumerate(cols):
        a0, a1 = math.pi * (1 - i / 5), math.pi * (1 - (i + 1) / 5)
        x0, y0 = 300 + 220 * math.cos(a0), 300 - 220 * math.sin(a0)
        x1, y1 = 300 + 220 * math.cos(a1), 300 - 220 * math.sin(a1)
        segs += f'<path d="M{x0:.1f} {y0:.1f} A220 220 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{c}" stroke-width="54"/>'
    return f"""<svg viewBox="0 0 600 600" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
{segs}
<g font-family="YS" font-size="40" fill="#12302C"><text x="62" y="360">E</text><text x="514" y="360">F</text></g>
<g transform="translate(300 300) rotate({needle})"><path d="M-12 0 L0 -196 L12 0 Z" fill="#12302C"/></g>
<circle cx="300" cy="300" r="26" fill="#12302C"/><circle cx="300" cy="300" r="10" fill="#F3B84A"/>
<g transform="translate(300 480)"><ellipse rx="240" ry="70" fill="#E7DCC8"/><ellipse rx="204" ry="54" fill="#fff"/>
<path d="M-40 -6 A44 26 0 0 1 40 -6 L28 8 L10 0 L-6 10 L-22 2 Z" fill="#E9B44C" stroke="#B9761A" stroke-width="3"/>
<circle cx="-12" cy="-10" r="4" fill="#B9761A"/><circle cx="14" cy="-14" r="3" fill="#B9761A"/>
<g transform="translate(150 -10) rotate(20)"><rect x="-10" y="-60" width="20" height="90" rx="10" fill="#9FB8B2"/><ellipse cx="0" cy="-70" rx="22" ry="30" fill="#9FB8B2"/></g></g>
</svg>"""

def ic(kind, w=120):
    """Small icons for the short-lived causes (viewBox 0 0 140 140)."""
    body = dict(
        fever='<rect x="56" y="14" width="28" height="84" rx="14" fill="#fff" stroke="#12302C" stroke-width="5"/>'
              '<circle cx="70" cy="106" r="22" fill="#E0503D" stroke="#12302C" stroke-width="5"/><rect x="64" y="40" width="12" height="62" rx="6" fill="#E0503D"/>'
              '<path d="M96 34 H112 M96 52 H108 M96 70 H112" stroke="#12302C" stroke-width="5" stroke-linecap="round"/>',
        stomach=f'<g transform="translate(-145 -154) scale(1.05)"><path d="{hub.STOM}" fill="#F4B6AE" stroke="#D9776B" stroke-width="4"/></g>'
                '<path d="M104 30 q10 -10 20 0 q10 10 0 20" fill="none" stroke="#F3B84A" stroke-width="6" stroke-linecap="round"/>',
        sleep='<path d="M80 18 A48 48 0 1 0 124 84 A38 38 0 1 1 80 18 Z" fill="#F3B84A"/>'
              '<g font-family="YS" fill="#fff"><text x="22" y="44" font-size="30">z</text><text x="40" y="24" font-size="22">z</text></g>',
        pill='<g transform="rotate(-35 70 70)"><rect x="24" y="50" width="92" height="40" rx="20" fill="#fff" stroke="#12302C" stroke-width="5"/>'
             '<path d="M70 50 H96 A20 20 0 0 1 96 90 H70 Z" fill="#F3B84A" stroke="#12302C" stroke-width="5"/></g>')[kind]
    return f'<svg viewBox="0 0 140 140" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def clock_small(w=130):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="34" r="25" fill="#fff" stroke="#0D7466" stroke-width="3.5"/>'
            '<path d="M32 18 V34 L42 40" fill="none" stroke="#12302C" stroke-width="3.5" stroke-linecap="round"/>'
            '<g fill="#F3B84A"><circle cx="32" cy="12" r="2.6"/><circle cx="54" cy="34" r="2.6"/><circle cx="32" cy="56" r="2.6"/><circle cx="10" cy="34" r="2.6"/></g></svg>')

def egg_dal(w=130):
    """A katori of dal with an egg and a cube of paneer: protein (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M8 30 H56 Q54 54 32 56 Q10 54 8 30 Z" fill="#fff" stroke="#0D7466" stroke-width="3.5"/><ellipse cx="32" cy="30" rx="24" ry="6" fill="#F3B84A"/>'
            '<ellipse cx="22" cy="18" rx="9" ry="11" fill="#fff" stroke="#12302C" stroke-width="2.5"/><circle cx="22" cy="20" r="4.5" fill="#F3B84A"/>'
            '<rect x="36" y="12" width="13" height="13" rx="2" fill="#FFF6E6" stroke="#12302C" stroke-width="2.5"/></svg>')

def glass_between(w=130):
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg">'
            '<path d="M18 10 H46 L42 56 H22 Z" fill="#fff" stroke="#0D7466" stroke-width="3.5" stroke-linejoin="round"/>'
            '<path d="M20.5 30 H43.5 L42 54 H22 Z" fill="#BFE3F0"/><path d="M26 36 q2 -3 4 0" stroke="#fff" stroke-width="2.5" fill="none"/></svg>')

def no_tonic(w=130):
    """A tonic bottle with a spoon, crossed out (viewBox 0 0 64 64)."""
    return (f'<svg viewBox="0 0 64 64" style="width:{w}px;height:{w}px;flex:none" xmlns="http://www.w3.org/2000/svg"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#B0362B" stroke-width="4"/>'
            '<rect x="22" y="22" width="20" height="28" rx="4" fill="#C9711A" stroke="#12302C" stroke-width="2.5"/><rect x="26" y="14" width="12" height="9" rx="2" fill="#12302C"/>'
            '<rect x="25" y="30" width="14" height="10" rx="2" fill="#FFF6E6"/>'
            '<path d="M13 51 L51 13" stroke="#B0362B" stroke-width="4.5" stroke-linecap="round"/></svg>')

def chhath_scene(w=900, h_=560):
    """Chhath at sunset: the sun touching the river, ripples, a bamboo soop with fruit, sugarcane and thekua, and two diyas (viewBox 0 0 900 560)."""
    rip = "".join(f'<path d="M{450-l} {372+i*30} H{450+l}" stroke="#FFD88A" stroke-width="7" stroke-linecap="round" opacity="{0.9-i*0.15:.2f}"/>'
                  for i, l in enumerate([150, 120, 92, 66, 44]))
    weave = "".join(f'<path d="M{190+i*34} 430 L{176+i*36} 520" stroke="#B9852E" stroke-width="3" opacity=".55"/>' for i in range(14)) + \
            "".join(f'<path d="M170 {448+j*20} H{730}" stroke="#B9852E" stroke-width="3" opacity=".45"/>' for j in range(4))
    thekua = "".join(f'<g transform="translate({x} {y})"><circle r="30" fill="#D9963C" stroke="#9C5E1C" stroke-width="3"/>'
                     f'<path d="M-16 -8 Q0 -18 16 -8 M-18 4 Q0 -6 18 4 M-14 15 Q0 6 14 15" stroke="#9C5E1C" stroke-width="3" fill="none"/></g>' for x, y in [(330, 438), (392, 452), (560, 440)])
    return f"""<svg viewBox="0 0 900 560" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7B267"/><stop offset=".6" stop-color="#F48C5F"/><stop offset="1" stop-color="#E36C5A"/></linearGradient>
<linearGradient id="riv" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B85A57"/><stop offset="1" stop-color="#5B3A55"/></linearGradient>
<clipPath id="win"><rect width="900" height="560" rx="48"/></clipPath></defs>
<g clip-path="url(#win)">
<rect width="900" height="360" fill="url(#sky)"/><rect y="350" width="900" height="210" fill="url(#riv)"/>
<circle cx="450" cy="352" r="110" fill="#FFE29A"/><circle cx="450" cy="352" r="150" fill="#FFE29A" opacity=".25"/>
<rect y="352" width="900" height="208" fill="url(#riv)" opacity=".92"/>
{rip}
<path d="M0 300 Q80 280 160 300 T320 296 L320 352 H0 Z" fill="#7E4A4A" opacity=".55"/><path d="M620 302 Q720 278 900 296 V352 H620 Z" fill="#7E4A4A" opacity=".55"/>
<path d="M150 420 Q450 400 750 420 L720 530 Q450 556 180 530 Z" fill="#E8C27A" stroke="#9C6B22" stroke-width="5"/>
{weave}
<g stroke-linecap="round"><path d="M200 470 L120 120" stroke="#5E8B3A" stroke-width="16"/><path d="M200 470 L120 120" stroke="#8DBE5A" stroke-width="7" stroke-dasharray="40 14"/>
<path d="M118 130 q-40 -20 -70 -10 M122 150 q30 -40 70 -40 M126 180 q-46 0 -66 20" stroke="#6E9A3A" stroke-width="9" fill="none"/></g>
<g transform="translate(470 428)"><path d="M-70 0 C-60 -60 0 -100 40 -110 C30 -60 0 -10 -70 0 Z" fill="#F3CF3A" stroke="#B98A1A" stroke-width="4"/>
<path d="M-40 6 C-20 -50 30 -80 70 -84 C60 -36 20 6 -40 6 Z" fill="#F7DB4A" stroke="#B98A1A" stroke-width="4"/></g>
<g transform="translate(640 420)"><circle r="46" fill="#8A5A2E"/><path d="M-30 -30 Q0 -50 30 -30" stroke="#5E3A1A" stroke-width="5" fill="none"/>
<path d="M0 -46 C-10 -80 -40 -96 -66 -96 M0 -46 C10 -84 40 -100 66 -100" stroke="#6E9A3A" stroke-width="7" fill="none" stroke-linecap="round"/></g>
{thekua}
<circle cx="250" cy="430" r="26" fill="#F48A3C" stroke="#B5542C" stroke-width="3"/><circle cx="244" cy="422" r="6" fill="#FFC27A"/>
</g></svg>"""

# ---------------- Instagram 1: Myth or fact? (EN, 5 slides) ----------------
N1 = 5
def m1(n=1):
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:28px">Myth or fact?</span></div>
 <h1 style="font-size:96px;margin-top:40px;max-width:920px">Chest pain after a heavy meal is <em>just gas.</em></h1>
 <div style="position:absolute;left:250px;top:470px">{heart_gas(600)}</div>
 <div style="position:absolute;left:84px;top:1150px;font-size:34px;font-weight:600;color:#B5542C">Guess first, then swipe →</div>
 {foot(n, total=N1)}</div>"""

def m2(n=2):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div style="display:inline-block;border:8px solid #F3B84A;color:#F3B84A;border-radius:22px;padding:6px 36px;transform:rotate(-6deg);font-family:YS;font-size:120px;line-height:1.1">MYTH</div>
 <h1 style="font-size:76px;margin-top:44px;max-width:920px">Chest pain after eating <em>can come from the heart.</em></h1>
 <div style="position:absolute;left:84px;right:84px;top:640px">{ecg(912, bg="#FFFFFF")}</div>
 <p style="position:absolute;left:84px;right:84px;top:960px;font-size:36px;line-height:1.4;color:#DCEFEA">A heavy meal makes the heart work harder. A heart attack can feel like burning, pressure or indigestion.</p>
 {foot(n, total=N1, light=True)}</div>"""

def m3(n=3):
    step = lambda num, big, t, c: (f'<div style="display:flex;align-items:center;gap:30px;background:#fff;border-radius:32px;padding:26px 34px">'
                                   f'<div style="flex:none;width:96px;height:96px;border-radius:50%;background:{c};color:#fff;font-family:YS;font-size:56px;display:flex;align-items:center;justify-content:center">{num}</div>'
                                   f'<div><div style="font-family:YS;font-size:50px;line-height:1.05">{big}</div><div style="font-size:31px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">What to do</div>
 <h2 style="font-size:80px;margin:14px 0 24px;max-width:920px">New chest discomfort? <em>Heart first.</em></h2>
 <p style="font-size:34px;line-height:1.35;color:#4A615D;max-width:880px">Treat it as a possible heart problem until a doctor has ruled it out.</p>
 <div style="display:grid;gap:24px;margin-top:50px">
  {step(1, "Get an ECG", "at a clinic or emergency department", "#B0362B")}
  {step(2, "Then gas remedies", "only once the heart is ruled out", "#0D7466")}</div>
 <div style="position:absolute;left:84px;right:84px;top:1000px;display:flex;align-items:center;gap:26px;background:#FAEED8;border-radius:28px;padding:24px 30px">
  <svg viewBox="0 0 600 640" style="width:110px;flex:none"><path d="{HEART}" fill="#D9473A"/></svg>
  <span style="font-size:32px;line-height:1.35">Diabetes? You may feel only mild discomfort. Don't wait it out.</span></div>
 {foot(n, total=N1)}</div>"""

def m4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">Call 112 right away for</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Chest pain <em>with</em></h2>
 {dot_list(["Sweating", "Breathlessness", "Pain spreading to the arm, jaw or back", "Fainting or feeling faint", "Nausea or vomiting"])}
 <div style="margin-top:56px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35"><b>Call 112</b> or go to the nearest emergency department. Every minute counts.</div>
 {foot(n, total=N1)}</div>"""

def mb_screen():
    return ('<div style="font-size:15px;font-weight:600;letter-spacing:.12em;color:#0D7466">MYTH BUSTER · THURSDAY</div>'
            '<div style="font-family:YS;font-size:28px;color:#12302C;line-height:1.15;margin:14px 0 18px">Losing weight without dieting is nothing to worry about.</div>'
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

# ---------------- Instagram 2: Loss of appetite (EN, 5 slides) ----------------
N2 = 5
def a1(n=1):
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Hunger meter</div>
 <h1 style="font-size:104px;margin-top:16px;max-width:900px">Not feeling <em>hungry</em> lately?</h1>
 <p style="font-size:36px;line-height:1.35;color:#4A615D;margin-top:22px;max-width:820px">When it passes, and when to get checked.</p>
 <div style="position:absolute;left:220px;top:500px">{hunger_meter(640)}</div>
 {foot(n, total=N2)}</div>"""

def a2(n=2):
    tile = lambda k, a, b: (f'<div style="background:rgba(255,255,255,.1);border-radius:30px;padding:24px;display:flex;flex-direction:column;align-items:flex-start;gap:12px">{ic(k, 120)}'
                            f'<div style="font-family:YS;font-size:44px;color:#F3B84A;line-height:1.05">{a}</div><div style="font-size:29px;color:#DCEFEA;line-height:1.3">{b}</div></div>')
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">Usually short-lived</div>
 <h2 style="font-size:80px;margin:14px 0 40px">Common <em>causes</em></h2>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px">
  {tile("fever", "Fever", "a viral illness or stomach bug")}{tile("stomach", "Tummy trouble", "acidity, indigestion, constipation")}
  {tile("sleep", "Stress", "worry, exams, poor sleep")}{tile("pill", "New medicines", "ask your doctor to review them")}</div>
 <p style="font-size:31px;line-height:1.35;color:#DCEFEA;margin-top:34px">These usually settle within days to two weeks.</p>
 {foot(n, total=N2, light=True)}</div>"""

def a3(n=3):
    row = lambda art, big, t: (f'<div style="display:flex;align-items:center;gap:34px;background:#fff;border-radius:32px;padding:22px 34px">{art}'
                               f'<div><div style="font-family:YS;font-size:46px;line-height:1.05">{big}</div><div style="font-size:30px;color:#4A615D;margin-top:8px">{t}</div></div></div>')
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">Meanwhile</div>
 <h2 style="font-size:84px;margin:14px 0 40px">Make every bite <em>count</em></h2>
 <div style="display:grid;gap:22px">
  {row(clock_small(120), "Every 2 to 3 hours", "small meals, don't wait to feel hungry")}
  {row(egg_dal(120), "Protein each meal", "dal, curd, paneer, egg, fish, chicken")}
  {row(glass_between(120), "Water between meals", "not a big glass just before eating")}
  {row(no_tonic(120), "No tonics on your own", "they don't treat the cause")}
 </div>
 {foot(n, total=N2)}</div>"""

def a4(n=4):
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:28px;color:#B0362B">See a doctor soon for</div>
 <h2 style="font-size:84px;margin:14px 0 26px">Low appetite <em>with</em></h2>
 {dot_list(["More than 2 to 3 weeks", "Weight loss without trying", "Yellow eyes or dark urine", "Full after a few bites, or vomiting", "Black stools or blood in the stool"])}
 <div style="margin-top:50px;background:#fff;border-radius:28px;padding:26px 30px;font-size:32px;line-height:1.35">Vomiting blood or severe belly pain? <b>Call 112</b> or go to the nearest emergency department.</div>
 {foot(n, total=N2)}</div>"""

def a5(n=5):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on the website</div>
 <h1 style="font-size:84px;margin-top:18px;max-width:900px">Loss of appetite: <em>the full answer</em></h1>
 <p style="font-size:34px;line-height:1.4;color:#DCEFEA;margin-top:30px;max-width:880px">Causes, simple tests, what to eat, and when to worry. In English and हिंदी.</p>
 <div style="position:absolute;right:60px;top:600px;background:#E6F2EF;border-radius:40px;padding:20px">{hunger_meter(340)}</div>
 <div style="position:absolute;left:84px;top:820px">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:62px;padding:16px 44px;border-radius:999px">drlochab.com</div>
  <p style="font-size:28px;color:#CFE5E0;margin-top:22px">Link in bio · Answers</p></div>
 {foot(n, total=N2, light=True)}</div>"""

# ---------------- Instagram 3: Chhath Puja (HI, single post) ----------------
CH = [("नहाय-खाय, खरना", "दिन भर पानी, नारियल पानी, दूध अच्छे से लें"),
      ("खरना का प्रसाद", "आराम से खाएँ, ठूँसकर नहीं"),
      ("व्रत खोलते समय", "पहले पानी या शरबत के घूँट, फिर हल्का खाना"),
      ("डायबिटीज़, किडनी, गर्भावस्था", "निर्जला व्रत से पहले डॉक्टर से पूछें")]
DUSK = "background:radial-gradient(120% 70% at 50% 10%,#7A3E4F 0%,#4E2A45 55%,#2E1A33 100%)"

def ch_rows(size=34, gap=14, lw=330):
    return "".join(f'<div style="display:flex;align-items:center;gap:22px;background:rgba(255,255,255,.09);border-radius:24px;padding:14px 24px;margin-bottom:{gap}px">'
                   f'<span style="flex:none;width:{lw}px;font-family:TD;font-size:{size+2}px;color:#FFC97A;line-height:1.25">{d}</span><span style="font-size:{size}px;line-height:1.3">{t}</span></div>'
                   for d, t in CH)

def ch_post():
    return f"""<div class="s teal hi" style="width:1080px;height:1350px;padding:60px 72px;{DUSK}">
 <div class="kick" style="font-size:30px;color:#FFC97A;text-align:center">छठ पूजा · 13 से 16 नवंबर</div>
 <h1 style="font-size:74px;margin-top:4px;text-align:center">निर्जला व्रत में <em style="color:#FFC97A">सेहत का भी ध्यान</em></h1>
 <div style="position:absolute;left:150px;top:230px">{chhath_scene(780)}</div>
 <div style="position:absolute;left:72px;right:72px;top:740px">{ch_rows(32, 14)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1155px;font-size:30px;line-height:1.35;color:#F7DCC0">चक्कर, बेहोशी, उलझन या बहुत कम पेशाब? 112 पर कॉल करें।</p>
 {foot(light=True, hi=True)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:76px 80px">
 <div class="kick" style="font-size:26px;color:#0D7466">Hunger meter</div>
 <h1 style="font-size:82px;margin-top:14px;max-width:620px">Not feeling <em>hungry</em> lately?</h1>
 <p style="font-size:32px;line-height:1.35;color:#4A615D;margin-top:24px;max-width:560px">Usually it passes. When it lasts weeks, or weight drops, get checked.</p>
 <div style="position:absolute;right:70px;top:120px">{hunger_meter(460)}</div>
 {foot(pad=80)}</div>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_myth():
    return f"""<div class="s saffron" style="width:1080px;height:1920px;padding:150px 84px">
 <div style="display:inline-block;background:#12302C;color:#F3B84A;border-radius:999px;padding:14px 30px" class="kick"><span style="font-size:30px">Myth or fact?</span></div>
 <h1 style="font-size:96px;margin-top:40px">Chest pain after a heavy meal is <em>just gas.</em></h1>
 <div style="position:absolute;left:290px;top:600px">{heart_gas(500, q=False)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1160px">
  <div style="display:inline-block;border:7px solid #B0362B;color:#B0362B;border-radius:20px;padding:4px 30px;transform:rotate(-5deg);font-family:YS;font-size:88px">MYTH</div>
  <p style="font-size:40px;line-height:1.35;margin-top:30px">It can be the heart. New chest discomfort: <b>ECG first</b>, gas remedies later. With sweating or breathlessness, <b>call 112</b>.</p></div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Play more at drlochab.com</span></div>
 {foot(pad=84)}</div>"""

def st_chhath():
    return f"""<div class="s teal hi" style="width:1080px;height:1920px;padding:150px 72px;{DUSK}">
 <div class="kick" style="font-size:34px;color:#FFC97A;text-align:center">छठ पूजा · 13 से 16 नवंबर</div>
 <h1 style="font-size:76px;margin-top:10px;text-align:center">निर्जला व्रत में <em style="color:#FFC97A">सेहत का भी ध्यान</em></h1>
 <div style="position:absolute;left:90px;top:390px">{chhath_scene(900)}</div>
 <div style="position:absolute;left:72px;right:72px;top:990px">{ch_rows(36, 16, 310)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1450px;font-size:36px;line-height:1.35;color:#F7DCC0">चक्कर, बेहोशी या बहुत कम पेशाब? 112 पर कॉल करें।</p>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#FFC97A;color:#2E1A33;font-family:YS;font-size:56px;padding:14px 44px;border-radius:999px">drlochab.com/hi</span></div>
 {foot(light=True, pad=72, hi=True)}</div>"""

def st_appetite():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">Hunger meter</div>
 <h1 style="font-size:108px;margin-top:16px">Not feeling <em>hungry</em> lately?</h1>
 <div style="position:absolute;left:220px;top:600px">{hunger_meter(640)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1290px;display:grid;gap:16px">
  {"".join(f'<div style="background:#fff;border-radius:999px;padding:18px 32px;font-size:36px;display:flex;gap:18px;align-items:center"><span style="width:18px;height:18px;border-radius:50%;background:{c};flex:none"></span>{t}</div>' for c, t in (("#0D7466", "Fever, stress, a tummy bug? Usually passes"), ("#0D7466", "Small meals every 2 to 3 hours"), ("#B0362B", "Weeks, or weight dropping? Get checked")))}</div>
 <div style="position:absolute;left:0;right:0;bottom:200px;text-align:center"><span style="background:#0D7466;color:#fff;font-family:YS;font-size:56px;padding:14px 40px;border-radius:999px">Read more: drlochab.com</span></div>
 {foot(pad=84)}</div>"""

# ---------------- text ----------------
CAP_MYTH = f"""Myth or fact? "Chest pain after a heavy meal is just gas." 🫀

Guess first, then swipe 👉

❌ MYTH. After a big festive meal, chest discomfort is easy to blame on gas. But a heavy meal makes the heart work harder, and a heart attack can feel like burning, pressure or indigestion in the chest or upper belly. People with diabetes may feel only mild discomfort, so many lose precious hours taking gas remedies at home.

What to do:
❤️ Treat new chest discomfort as a possible heart problem until a doctor has ruled it out.
📈 Get an ECG done first; gas or acidity remedies come later.

🚨 Call 112 or go to the nearest emergency department straight away for chest pain with sweating, breathlessness, pain spreading to the arm, jaw or back, or fainting.

🎮 The next Myth or fact? goes up on Thursday. Play them all at drlochab.com (link in bio), in English and Hindi. More on when acidity is serious: {MYTH_LINK}

{SIGN}

#MythOrFact #ChestPain #HeartHealth #Acidity #Gas #Gastroenterologist #Gurugram #DrLochab"""

CAP_APP = f"""Not feeling hungry lately? 🍽️

A few days without much appetite is common after a fever, a tummy bug, a stressful week or a new medicine, and it usually comes back on its own.

When appetite stays low for weeks, it's worth a check-up. It can be an early sign of hepatitis (often before the eyes turn yellow), an ulcer or H. pylori, TB, thyroid or sugar problems, or low mood. Most causes are found with simple blood tests and an ultrasound.

Meanwhile, make every bite count:
⏰ Small meals or snacks every 2 to 3 hours, don't wait to feel hungry
🥚 Protein at each meal: dal, curd, paneer, egg, fish or chicken
💧 Sip water between meals, not a big glass just before eating
🚫 No appetite tonics or syrups on your own: they don't treat the cause

🚩 See a doctor soon if poor appetite lasts more than 2 to 3 weeks, or comes with weight loss, yellow eyes, dark urine, vomiting, feeling full after a few bites, or black stools. Vomiting blood or severe belly pain? Call 112.

📖 New on my website, in English and Hindi: {ANS} (link in bio)

{SIGN}

#LossOfAppetite #GutHealth #LiverHealth #Digestion #Gastroenterologist #Gurugram #DrLochab"""

CAP_CHHATH = f"""छठ पूजा: निर्जला व्रत में सेहत का भी ध्यान 🌅

नहाय-खाय (शुक्रवार 13 नवंबर) से उषा अर्घ्य (सोमवार 16 नवंबर) तक, व्रतियों और परिवार के लिए कुछ छोटी बातें:

🌅 नहाय-खाय और खरना के दिन पानी, नारियल पानी, दूध और दाल अच्छे से लें, ताकि शरीर में पानी की कमी न हो
🌅 खरना का प्रसाद आराम से खाएँ, ठूँसकर नहीं; पेट हल्का रहेगा
🌅 उषा अर्घ्य के बाद व्रत खोलें पहले पानी या शरबत के घूँट से, फिर हल्के खाने से; ठेकुआ और तली चीज़ें थोड़ी मात्रा में
🌅 डायबिटीज़, किडनी या दिल की बीमारी, गर्भावस्था, या बुज़ुर्ग हों तो निर्जला व्रत से पहले अपने डॉक्टर से ज़रूर पूछें; दवाएँ अपने आप न छोड़ें

🚩 चक्कर, बेहोशी, उलझन, बहुत कम पेशाब, या लगातार उल्टी हो तो व्रत से ज़्यादा ज़रूरी इलाज है: 112 पर कॉल करें या नज़दीकी इमरजेंसी में जाएँ।

व्रत में पेट हल्का रखने की पूरी गाइड (हिंदी): {FAST_HI} (लिंक बायो में)

छठी मैया सबको सुख और सेहत दें 🙏

{SIGN_HI}

#छठपूजा #ChhathPuja2026 #व्रत #पेटकीसेहत #GutHealth #Gurugram #DrLochab"""

GBP_TEXT = f"""Not feeling hungry lately? A few days of poor appetite is common after a fever, a stomach upset, a stressful week or a new medicine, and it usually comes back on its own.

When appetite stays low for more than 2 to 3 weeks, or comes with weight loss, it is worth a check-up. It can be an early sign of hepatitis, an ulcer or H. pylori infection, TB, thyroid or sugar problems, or low mood. Most causes are found with simple blood tests and an ultrasound.

Meanwhile, eat small meals every 2 to 3 hours, add protein to each meal, sip water between meals, and avoid appetite tonics bought without a prescription.

See a doctor soon for weight loss without trying, yellow eyes, dark urine, repeated vomiting or black stools. Vomiting blood or severe belly pain is an emergency: call 112.

Read the full answer, with a diet guide and common questions, in English and Hindi.

Button: Learn more → https://{ANS}/"""

WA_EN = f"""🩺 *Not feeling hungry lately?*

Poor appetite for a few days is common and usually passes. But when it lasts for weeks, or the weight starts dropping, it can be an early sign of a liver, stomach or other problem that is easy to find with simple tests. I've written a short, plain answer on the causes, the tests, what to eat meanwhile, and the warning signs:

👉 https://{ANS}/
हिंदी में: https://{ANS_HI}/

– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)"""

WA_HI = f"""🩺 *भूख नहीं लग रही?*

कुछ दिन भूख कम लगना आम है और अक्सर अपने आप ठीक हो जाता है। पर अगर हफ़्तों तक भूख न लगे, या वज़न घटने लगे, तो यह लिवर, पेट या किसी और समस्या का शुरुआती संकेत हो सकता है, जो आसान जाँचों से पता चल जाती है। वजहें, जाँचें, तब तक क्या खाएँ, और ख़तरे के संकेत, यह सब आसान भाषा में यहाँ पढ़ें:

👉 https://{ANS_HI}/

छठ पूजा की शुभकामनाएँ 🌅 व्रत रखने वाले पानी और सेहत का ध्यान रखें।
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
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig1-myth-chest-pain-{i}.png", b)
        for i, f in enumerate([a1, a2, a3, a4, a5], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/ig2-loss-of-appetite-{i}.png", b)
        render(ch_post, 1080, 1350, f"{OUT}/ig3-chhath-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business-loss-of-appetite.png", b)
        render(st_myth, 1080, 1920, f"{OUT}/wa-status-1-myth-chest-pain.png", b)
        render(st_chhath, 1080, 1920, f"{OUT}/wa-status-2-chhath-hi.png", b)
        render(st_appetite, 1080, 1920, f"{OUT}/wa-status-3-loss-of-appetite.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("ig1-caption.txt", CAP_MYTH), ("ig2-caption.txt", CAP_APP), ("ig3-caption-hi.txt", CAP_CHHATH),
                      ("google-business-post.txt", GBP_TEXT), ("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
