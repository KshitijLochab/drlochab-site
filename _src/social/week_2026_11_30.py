"""WhatsApp content for the week of 30 Nov to 6 Dec 2026 (no major festival; winter smog season).
Instagram and Google posts are made by their own tasks (Buffer), so this script makes only WhatsApp:
3 Status images (1080x1920), each in a different visual style, and the broadcast text (EN + HI).
 1 Mon 30 Nov  Low iron? Check the gut (new answer page)      clean medical diagram with labels, rose + gold accent
 2 Thu 3 Dec   H. pylori: treat, wait, re-test                 comic-strip panels (3 frames), sky-blue accent
 3 Sat 5 Dec   स्मॉग वाले दिन: खाने के बाद 10 मिनट घर में (HI)    hand-drawn whiteboard sketch, marker colours
Original drawings only. No doses, no brand names. Every image: logo, name and drlochab.com.
Run: python3 _src/social/week_2026_11_30.py  -> _src/out/week-2026-11-30/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC, STOM
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "week-2026-11-30"); os.makedirs(OUT, exist_ok=True)
ANS = "drlochab.com/answers/low-haemoglobin-iron-deficiency-gut"
ANS_HI = "drlochab.com/hi/answers/low-haemoglobin-iron-deficiency-gut"
HP = "drlochab.com/conditions/h-pylori-gastritis-ulcer"

EXTRA_CSS = """
.ink{background:#FFFFFF;color:#12302C}
.board{background:#FBFBF8;color:#1F2B2A;background-image:radial-gradient(#E4E8E6 1.6px,transparent 1.6px);background-size:36px 36px}
.panel{background:#fff;border:6px solid #12302C;border-radius:26px;position:relative;overflow:hidden}
.pn{position:absolute;left:18px;top:14px;width:58px;height:58px;border-radius:50%;background:#12302C;color:#fff;font-family:YS;font-size:34px;display:flex;align-items:center;justify-content:center}
.cap{font-family:YS;font-size:50px;line-height:1.05}
.mk{font-family:"MK",sans-serif;font-weight:600}
"""

# ---------------- original drawings ----------------
def gut_leaks(w=860):
    """Clean labelled diagram: the digestive tract with three slow-bleed spots and an iron 'fuel gauge' (viewBox 0 0 860 900)."""
    drop = lambda x, y, s=1: (f'<g transform="translate({x} {y}) scale({s})"><path d="M0 -34 C14 -14 22 0 22 12 A22 22 0 0 1 -22 12 C-22 0 -14 -14 0 -34 Z" fill="#C2453A"/>'
                              f'<ellipse cx="-7" cy="8" rx="5" ry="8" fill="#fff" opacity=".55"/></g>')
    def label(x1, y1, x2, y2, t, anchor="start"):
        tx = x2 + (14 if anchor == "start" else -14)
        return (f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#12302C" stroke-width="4" fill="none"/><circle cx="{x1}" cy="{y1}" r="8" fill="#12302C"/>'
                f'<text x="{tx}" y="{y2+12}" text-anchor="{anchor}" font-family="FT" font-weight="600" font-size="36" fill="#12302C">{t}</text>')
    colon = ("M250 470 C210 470 200 500 200 540 L200 760 C200 800 230 812 262 812 L300 812 M250 470 L600 470 C640 470 652 500 652 540 L652 760"
             " C652 800 620 812 590 812 L480 812 C440 812 420 830 420 860")
    small = "M330 560 c60 -30 130 -30 190 0 c-60 30 -130 30 -190 0 m0 60 c60 -30 130 -30 190 0 c-60 30 -130 30 -190 0 m0 60 c60 -30 130 -30 190 0 c-60 30 -130 30 -190 0"
    return f"""<svg viewBox="0 0 860 900" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<path d="M430 20 L430 150" stroke="#E7A79F" stroke-width="34" stroke-linecap="round"/>
<g transform="translate(150 70) scale(.95)"><path d="{STOM}" fill="#F6C9C2" stroke="#9C4A42" stroke-width="7"/></g>
<path d="{colon}" fill="none" stroke="#F0B8A6" stroke-width="58" stroke-linecap="round" stroke-linejoin="round"/>
<path d="{colon}" fill="none" stroke="#B4644F" stroke-width="5" stroke-dasharray="2 18" stroke-linecap="round"/>
<path d="{small}" fill="none" stroke="#F6D2C0" stroke-width="30" stroke-linecap="round"/>
{drop(380, 330)}{drop(640, 640, .9)}{drop(420, 872, .8)}
{label(380, 330, 160, 250, "Ulcer", "end")}{label(652, 640, 720, 640, "Polyp")}{label(430, 870, 160, 870, "Piles", "end")}
{label(520, 560, 640, 380, "Celiac,")}<text x="654" y="434" font-family="FT" font-weight="600" font-size="36" fill="#12302C">worms</text>
</svg>"""

def iron_gauge(w=300, level=.12):
    """A fuel gauge marked Fe, needle near empty (viewBox 0 0 300 190)."""
    import math
    a = math.pi * (1 - level); x = 150 + 110 * math.cos(a); y = 160 - 110 * math.sin(a)
    return f"""<svg viewBox="0 0 300 190" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<path d="M30 160 A120 120 0 0 1 270 160" fill="none" stroke="#E4ECEA" stroke-width="30"/>
<path d="M30 160 A120 120 0 0 1 66 75" fill="none" stroke="#C2453A" stroke-width="30"/>
<text x="26" y="188" font-family="YS" font-size="30" fill="#C2453A">E</text><text x="256" y="188" font-family="YS" font-size="30" fill="#0D7466">F</text>
<text x="150" y="120" text-anchor="middle" font-family="YS" font-size="44" fill="#12302C">Fe</text>
<path d="M150 160 L{x:.0f} {y:.0f}" stroke="#12302C" stroke-width="9" stroke-linecap="round"/><circle cx="150" cy="160" r="14" fill="#12302C"/></svg>"""

def germ(w=200, sad=False, ghost=False):
    """A cartoon H. pylori: a curly rod with tails (viewBox 0 0 200 140)."""
    op = ".25" if ghost else "1"
    face = ('<circle cx="80" cy="64" r="7" fill="#12302C"/><circle cx="112" cy="64" r="7" fill="#12302C"/>' +
            ('<path d="M82 92 q14 -12 28 0" stroke="#12302C" stroke-width="6" fill="none" stroke-linecap="round"/>' if sad else
             '<path d="M82 86 q14 12 28 0" stroke="#12302C" stroke-width="6" fill="none" stroke-linecap="round"/>'))
    return f"""<svg viewBox="0 0 200 140" style="width:{w}px;opacity:{op}" xmlns="http://www.w3.org/2000/svg">
<path d="M40 70 C40 30 70 30 96 50 C122 70 150 30 160 70 C170 110 130 120 100 96 C76 78 40 110 40 70 Z" fill="#8FCB6B" stroke="#3F7D2B" stroke-width="6"/>
<path d="M160 70 c18 -8 22 -26 36 -20 M160 76 c20 6 18 26 34 26" stroke="#3F7D2B" stroke-width="5" fill="none" stroke-linecap="round"/>{face}</svg>"""

def pill_pack(w=220):
    """A generic blister strip (no brand) (viewBox 0 0 220 140)."""
    holes = "".join(f'<ellipse cx="{50+i*60}" cy="{50+j*44}" rx="20" ry="14" fill="#fff" stroke="#9FB5B0" stroke-width="4"/>' for i in range(3) for j in range(2))
    return f'<svg viewBox="0 0 220 140" style="width:{w}px" xmlns="http://www.w3.org/2000/svg"><rect x="10" y="16" width="200" height="112" rx="18" fill="#D7E6F3" stroke="#5B86A8" stroke-width="6"/>{holes}</svg>'

def calendar(w=230, text="4 weeks"):
    return f"""<svg viewBox="0 0 230 210" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<rect x="10" y="30" width="210" height="170" rx="20" fill="#fff" stroke="#12302C" stroke-width="6"/><rect x="10" y="30" width="210" height="52" rx="20" fill="#5B86A8"/>
<rect x="10" y="60" width="210" height="22" fill="#5B86A8"/><rect x="56" y="12" width="14" height="40" rx="7" fill="#12302C"/><rect x="160" y="12" width="14" height="40" rx="7" fill="#12302C"/>
<text x="115" y="160" text-anchor="middle" font-family="YS" font-size="46" fill="#12302C">{text}</text></svg>"""

def breath_test(w=300):
    """A person-free breath bag and a stool pot, the two non-invasive tests (viewBox 0 0 300 220)."""
    return f"""<svg viewBox="0 0 300 220" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<path d="M40 200 C20 140 30 70 90 60 C150 50 160 140 130 200 Z" fill="#EAF3FB" stroke="#5B86A8" stroke-width="6"/>
<rect x="76" y="28" width="28" height="38" rx="6" fill="#5B86A8"/><path d="M60 120 q30 -20 60 0 M58 150 q32 -20 64 0" stroke="#9FB5B0" stroke-width="5" fill="none"/>
<rect x="190" y="110" width="80" height="90" rx="12" fill="#fff" stroke="#12302C" stroke-width="6"/><rect x="184" y="92" width="92" height="26" rx="8" fill="#F3B84A" stroke="#12302C" stroke-width="5"/>
<circle cx="250" cy="40" r="34" fill="#0D7466"/><path d="M234 40 l11 12 l22 -24" stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>"""

def sketch_walk(w=920):
    """Whiteboard-style marker sketch: a smoggy window on one side, a stick figure walking a loop around the dining table (viewBox 0 0 920 760)."""
    mk = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'
    smog = "".join(f'<path d="M{x} {y} q30 -24 60 0 q30 -24 60 0" stroke="#9AA3A8" stroke-width="9" {mk}/>' for x, y in ((44, 120), (70, 190), (40, 260)))
    return f"""<svg viewBox="0 0 920 760" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<!-- window with smog -->
<rect x="24" y="40" width="250" height="300" rx="8" fill="#EEF0F0" stroke="#1F2B2A" stroke-width="8"/>
<path d="M149 40 V340 M24 190 H274" stroke="#1F2B2A" stroke-width="6"/>{smog}
<text x="150" y="395" text-anchor="middle" font-family="FT" font-weight="600" font-size="36" fill="#7A8287">AQI 300+</text>
<path d="M60 430 L240 430" stroke="#C2453A" stroke-width="10" {mk}/>
<!-- dining table, top view, with plate -->
<rect x="440" y="300" width="300" height="190" rx="24" fill="#FFF4DC" stroke="#1F2B2A" stroke-width="8"/>
<circle cx="590" cy="395" r="58" fill="#fff" stroke="#1F2B2A" stroke-width="6"/><circle cx="590" cy="395" r="30" fill="none" stroke="#E0A33A" stroke-width="6"/>
<!-- dashed loop path -->
<ellipse cx="590" cy="395" rx="280" ry="210" stroke="#2F7FD0" stroke-width="7" stroke-dasharray="4 22" {mk}/>
<path d="M850 300 l26 16 l-6 -30" stroke="#2F7FD0" stroke-width="8" {mk}/>
<!-- stick figure walking -->
<g transform="translate(330 560)"><circle cx="0" cy="-130" r="34" fill="#fff" stroke="#1F2B2A" stroke-width="8"/>
<path d="M0 -96 L0 0 M0 -70 L-44 -30 M0 -70 L40 -36 M0 0 L-36 74 M0 0 L42 70" stroke="#1F2B2A" stroke-width="9" {mk}/>
<path d="M-10 -136 q10 8 20 0" stroke="#1F2B2A" stroke-width="5" {mk}/></g>
<!-- timer -->
<g transform="translate(800 110)"><circle r="78" fill="#fff" stroke="#1F2B2A" stroke-width="8"/><path d="M0 0 L0 -54 M0 0 L36 20" stroke="#1F2B2A" stroke-width="8" {mk}/>
<path d="M0 -78 A78 78 0 0 1 67 -39" stroke="#1FA35A" stroke-width="16" {mk}/><rect x="-14" y="-104" width="28" height="18" rx="4" fill="#1F2B2A"/>
</g>
</svg>"""

# ---------------- WhatsApp Status (1080x1920) ----------------
def st_iron():
    return f"""<div class="s ink" style="width:1080px;height:1920px;padding:130px 84px">
 <div class="kick" style="font-size:30px;color:#B0362B">Low haemoglobin · khoon ki kami</div>
 <h1 style="font-size:100px;margin-top:20px">Low iron?<br><em style="color:#B0362B">Check the gut.</em></h1>
 <div style="position:absolute;right:70px;top:150px">{iron_gauge(250)}</div>
 <div style="position:absolute;left:110px;top:500px">{gut_leaks(800)}</div>
 <div style="position:absolute;left:84px;right:84px;top:1380px;background:#FAEED8;border-radius:28px;padding:30px 36px">
  <p style="font-size:42px;line-height:1.3"><b>Men, and women after menopause:</b> low iron usually means slow bleeding or poor absorption in the gut. Find the cause, don't just take iron.</p></div>
 <p style="position:absolute;left:84px;right:84px;bottom:150px;font-size:32px;color:#4A615D">Send this to someone taking iron tablets for months · {ANS.split('/')[0]}</p>
 {foot(pad=84)}</div>"""

def st_hpylori():
    panels = [
        (pill_pack(200) + germ(140, sad=True), "Treat", "Finish the full course."),
        (calendar(220), "Wait", "At least 4 weeks after. Acidity tablets off for 2, if your doctor agrees."),
        ('<div style="position:absolute;left:0;top:40px">' + germ(110, ghost=True) + "</div>" + breath_test(300), "Re-test", "Breath or stool test, to be sure it's gone."),
    ]
    html = ""
    for i, (art, h, t) in enumerate(panels, 1):
        html += (f'<div class="panel" style="height:400px;display:grid;grid-template-columns:420px 1fr;align-items:center;padding:0 36px 0 70px">'
                 f'<div class="pn">{i}</div><div style="display:flex;align-items:center;justify-content:center;gap:6px;position:relative;height:100%">{art}</div>'
                 f'<div><div class="cap">{h}</div><p style="font-size:36px;line-height:1.3;margin-top:12px;color:#33504B">{t}</p></div></div>')
    return f"""<div class="s" style="width:1080px;height:1920px;padding:120px 72px;background:#EAF3FB;color:#12302C">
 <div class="kick" style="font-size:30px;color:#3C6A8E">H. pylori</div>
 <h1 style="font-size:96px;margin-top:14px">Treat. Wait.<br><em style="color:#2F6E9E">Re-test.</em></h1>
 <div style="display:grid;gap:30px;margin-top:50px">{html}</div>
 <p style="position:absolute;left:72px;right:72px;bottom:150px;font-size:32px;color:#3C5A57">Feeling better is not proof. Send this to anyone on an H. pylori course · drlochab.com</p>
 {foot(pad=72)}</div>"""

def st_smog_hi():
    return f"""<div class="s board hi" style="width:1080px;height:1920px;padding:130px 72px">
 <div class="mk" style="font-size:40px;color:#7A8287">बाहर स्मॉग है?</div>
 <h1 style="font-size:92px;margin-top:10px;color:#1F2B2A">खाने के बाद <span style="color:#1FA35A">10 मिनट</span><br>घर में ही टहलें</h1>
 <div style="position:absolute;left:80px;top:560px">{sketch_walk(920)}</div>
 <div style="position:absolute;left:72px;right:72px;top:1360px;display:grid;gap:22px">
  {"".join(f'<div class="mk" style="font-size:42px;display:flex;gap:20px;align-items:center"><span style="color:{c};font-size:52px">{m}</span>{t}</div>' for c, m, t in (("#1FA35A", "✓", "खाने के बाद शुगर कम चढ़ती है"), ("#1FA35A", "✓", "पेट हल्का, गैस और भारीपन कम"), ("#C2453A", "✗", "खाकर 2 से 3 घंटे लेटें नहीं")))}</div>
 <p style="position:absolute;left:72px;right:72px;bottom:150px;font-size:32px;color:#4A615D">घर के बुज़ुर्गों को भेजें · सीने में दर्द या साँस फूले तो 112</p>
 {foot(pad=72, hi=True)}</div>"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}{EXTRA_CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500); pg.screenshot(path=path); pg.close()

# ---------------- text ----------------
WA_EN = f"""Low haemoglobin or iron deficiency? 🩸

In men of any age, and in women after menopause, low iron is rarely "just weakness". The usual cause is in the stomach or bowel: slow bleeding (an ulcer, piles, a polyp) or poor absorption (celiac disease, H. pylori, worms). The cause should be found, often with an endoscopy and colonoscopy, not just treated with iron tablets for months.

What to check, which tests help, iron and food, and the warning signs:
👉 https://{ANS}/

Hindi: https://{ANS_HI}/

Black stools with dizziness, vomiting blood or fainting is an emergency: call 112.
– Dr. Kshitij Lochab, Gastroenterologist, Gurugram (drlochab.com)
(You are receiving this because you agreed to get health tips. Reply STOP to opt out.)"""

WA_HI = f"""हीमोग्लोबिन कम या आयरन की कमी? 🩸

किसी भी उम्र के पुरुषों में, और पीरियड बंद होने के बाद महिलाओं में, आयरन की कमी "बस कमज़ोरी" नहीं होती। आमतौर पर वजह पेट या आँत में होती है: धीमी ब्लीडिंग (अल्सर, बवासीर, पॉलिप) या आयरन ठीक से न सोख पाना (सीलिएक, H. pylori, पेट के कीड़े)। महीनों तक सिर्फ़ आयरन की गोलियाँ लेने की जगह वजह ढूँढनी चाहिए, अक्सर एंडोस्कोपी और कोलोनोस्कोपी से।

क्या जाँच करवाएँ, आयरन और खान-पान, और ख़तरे के संकेत:
👉 https://{ANS_HI}/

चक्कर के साथ काला मल, ख़ून की उल्टी या बेहोशी इमरजेंसी है: 112 पर कॉल करें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, गुरुग्राम (drlochab.com/hi)
(आपने हेल्थ टिप्स पाने की सहमति दी है, इसलिए यह संदेश मिला। बंद करने के लिए STOP लिखें।)"""

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        render(st_iron, 1080, 1920, f"{OUT}/wa-status-1-low-iron-gut.png", b)
        render(st_hpylori, 1080, 1920, f"{OUT}/wa-status-2-h-pylori-retest.png", b)
        render(st_smog_hi, 1080, 1920, f"{OUT}/wa-status-3-smog-walk-hi.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
            os.remove(f"{OUT}/{f}")
    for name, txt in [("whatsapp-broadcast-en.txt", WA_EN), ("whatsapp-broadcast-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
