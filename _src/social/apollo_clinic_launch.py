"""Announcement: now also consulting at Apollo Clinic, Sector 52, Gurugram (23 Oct 2026).
Instagram post (1080x1350), Instagram story (1080x1920), WhatsApp status EN + HI (1080x1920), Google Business image (1200x900),
captions and post text. Timings come from clinics.py; a small line says timings may change (check drlochab.com).
No Apollo logo or brand artwork; clinic names in plain text only. No phone number in the Google post text.
Run: python3 _src/social/apollo_clinic_launch.py  -> _src/out/apollo-clinic-launch/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS, foot, SRC
import clinics
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "apollo-clinic-launch"); os.makedirs(OUT, exist_ok=True)

def pin(s=90, col="#F3B84A", ink="#12302C"):
    return (f'<svg viewBox="0 0 64 80" style="width:{s}px;height:{s*1.25}px;flex:none"><path d="M32 78 C32 78 6 46 6 28 A26 26 0 0 1 58 28 C58 46 32 78 32 78 Z" fill="{col}" stroke="{ink}" stroke-width="3"/>'
            f'<circle cx="32" cy="28" r="10" fill="{ink}"/></svg>')

def mapart(w=900):
    """Two pins on a simple road map: Sector 52 (new) and Sector 51."""
    return f"""<svg viewBox="0 0 900 420" style="width:{w}px;display:block">
 <rect x="0" y="0" width="900" height="420" rx="36" fill="#0E5F55"/>
 <path d="M-20 300 C200 260 420 330 920 250" stroke="#2C7F73" stroke-width="44" fill="none"/>
 <path d="M-20 300 C200 260 420 330 920 250" stroke="#F3F7F6" stroke-width="3" stroke-dasharray="18 16" fill="none" opacity=".6"/>
 <path d="M300 -20 C320 120 280 260 330 440" stroke="#2C7F73" stroke-width="34" fill="none"/>
 <path d="M640 -20 C610 140 660 280 620 440" stroke="#2C7F73" stroke-width="26" fill="none"/>
 {''.join(f'<rect x="{x}" y="{y}" width="{w_}" height="{h_}" rx="10" fill="#13695E"/>' for x, y, w_, h_ in [(40,40,200,150),(370,30,220,120),(700,40,160,140),(40,350,220,60),(380,360,200,50),(690,330,170,80),(380,170,200,80)])}
 <g transform="translate(470 150)"><circle r="70" fill="#F3B84A" opacity=".25"/><path d="M0 60 C0 60 -40 12 -40 -16 A40 40 0 0 1 40 -16 C40 12 0 60 0 60 Z" fill="#F3B84A" stroke="#12302C" stroke-width="4"/><circle cy="-16" r="15" fill="#12302C"/></g>
 <g transform="translate(205 228) scale(.72)"><path d="M0 60 C0 60 -40 12 -40 -16 A40 40 0 0 1 40 -16 C40 12 0 60 0 60 Z" fill="#FFFFFF" stroke="#12302C" stroke-width="5"/><circle cy="-16" r="15" fill="#12302C"/></g>
 <text x="470" y="250" text-anchor="middle" font-family="FT" font-weight="600" font-size="30" fill="#FFFFFF">Sector 52</text>
 <text x="205" y="300" text-anchor="middle" font-family="FT" font-weight="600" font-size="26" fill="#CFE5E0">Sector 51</text>
</svg>"""

def sched(hi=False, big=1.0):
    A = clinics.APOLLO_CLINIC["hi" if hi else "en"]
    rows = [(A["name"], "; ".join(f"{d}, {h}" for d, h in A["hours"]), True),
            (("आर्क्योरा क्लिनिक, सेक्टर 51" if hi else "Arcura Clinic, Sector 51"), ("सोम–शुक्र शाम 6–8 बजे · रविवार सुबह 9–दोपहर 1 बजे" if hi else "Mon–Fri 6–8 pm · Sunday 9 am–1 pm"), False)]
    new = "नया" if hi else "New"
    return "".join(f'<div style="display:flex;gap:{int(22*big)}px;align-items:center;background:{"#FFFFFF" if n_ else "rgba(255,255,255,.1)"};color:{"#12302C" if n_ else "#FFFFFF"};'
                   f'border-radius:{int(28*big)}px;padding:{int(22*big)}px {int(26*big)}px;margin-top:{int(16*big)}px">{pin(int(56*big), "#F3B84A" if n_ else "#FFFFFF")}'
                   f'<div><div style="font-family:{"TD" if hi else "YS"};font-size:{int(38*big)}px;line-height:1.15">{nm}'
                   + (f' <span style="font-family:FT;font-size:{int(20*big)}px;font-weight:600;background:#F3B84A;color:#12302C;border-radius:8px;padding:3px 10px;vertical-align:middle">{new}</span>' if n_ else "")
                   + f'</div><div style="font-size:{int(28*big)}px;line-height:1.3;margin-top:6px;{"color:#0D7466;font-weight:600" if n_ else "color:#DCEFEA"}">{hrs}</div></div></div>'
                   for nm, hrs, n_ in rows)

def story():
    return f"""<div class="s teal" style="width:1080px;height:1920px;padding:170px 84px">
 <div class="kick" style="font-size:30px;color:#F3B84A">New clinic timing</div>
 <h1 style="font-size:104px;margin-top:20px">Now also at <em>Apollo Clinic, Sector 52</em></h1>
 <div style="margin-top:56px">{mapart(912)}</div>
 {sched(big=1.25)}
 <p style="font-size:38px;line-height:1.35;color:#DCEFEA;margin-top:40px">Book on WhatsApp or call, or directly at the clinic.</p>
 <div style="position:absolute;left:84px;right:84px;bottom:165px;text-align:center">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:76px;padding:18px 52px;border-radius:999px">drlochab.com</div>
  <div style="font-size:26px;color:#9FCFC5;margin-top:22px">Timings may change; the latest are always on drlochab.com.</div></div>
 {foot(None, light=True, pad=84)}</div>"""

def post(h=1350, story=False):
    top = 170 if story else 90
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:{top}px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">New clinic timing</div>
 <h1 style="font-size:{92 if story else 84}px;margin-top:18px">Now also at <em>Apollo Clinic, Sector 52</em></h1>
 <div style="margin-top:{40 if story else 26}px">{mapart(912 if story else 860)}</div>
 {sched(big=1.08 if story else 1.0)}
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:{40 if story else 26}px">
  <div style="font-size:26px;color:#CFE5E0;line-height:1.35">Book on WhatsApp or call,<br>or directly at the clinic.</div>
  <div style="background:#F3B84A;color:#12302C;font-family:YS;font-size:40px;padding:12px 30px;border-radius:999px">drlochab.com</div></div>
 <div style="font-size:21px;color:#9FCFC5;margin-top:16px">Timings may change; the latest are always on drlochab.com.</div>
 {foot(None, light=True, pad=84)}</div>"""

def status(hi=False):
    if hi:
        k, h1, bk, note, url = ("नया क्लिनिक समय", "अब <em>अपोलो क्लिनिक, सेक्टर 52</em> में भी", "WhatsApp या कॉल करके, या सीधे क्लिनिक पर अपॉइंटमेंट लें।",
                                "समय बदल सकता है; ताज़ा समय हमेशा drlochab.com पर।", "drlochab.com/hi")
    else:
        k, h1, bk, note, url = ("New clinic timing", "Now also at <em>Apollo Clinic, Sector 52</em>", "Book on WhatsApp or call, or directly at the clinic.",
                                "Timings may change; the latest are always on drlochab.com.", "drlochab.com")
    return f"""<div class="s teal{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:160px 84px">
 <div class="kick" style="font-size:30px;color:#F3B84A">{k}</div>
 <h1 style="font-size:{88 if hi else 96}px;margin-top:20px">{h1}</h1>
 <div style="margin-top:50px">{mapart(912)}</div>
 {sched(hi, big=1.12)}
 <p style="font-size:36px;line-height:1.35;color:#DCEFEA;margin-top:44px">{bk}</p>
 <div style="position:absolute;left:84px;right:84px;bottom:220px;text-align:center">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:76px;padding:18px 52px;border-radius:999px">{url}</div>
  <div style="font-size:26px;color:#9FCFC5;margin-top:22px">{note}</div></div>
 {foot(None, light=True, pad=84, hi=hi)}</div>"""

def gbp():
    return f"""<div class="s teal" style="width:1200px;height:900px;padding:70px 80px">
 <div class="kick" style="font-size:24px;color:#F3B84A">New clinic timing</div>
 <h1 style="font-size:72px;margin-top:14px">Now also at <em>Apollo Clinic, Sector 52</em></h1>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:28px;align-items:center">
  <div>{mapart(500)}</div><div>{sched(big=.82)}</div></div>
 {foot(None, light=True, pad=80)}</div>"""

A = clinics.APOLLO_CLINIC["en"]
WHEN = "; ".join(f"{d}, {h}" for d, h in A["hours"])
CAPTION = f"""📍 Now also consulting at Apollo Clinic, Sector 52, Gurugram

🕓 {WHEN}
📍 Arcura Clinic, Sector 51 continues: Monday to Friday 6 to 8 pm, Sunday 9 am to 1 pm

If evenings don't suit you, the afternoon sitting at Sector 52 is an easier option. I see adults and teenagers aged 12 and above for acidity, gas and bloating, constipation, fatty liver, jaundice, IBS, and for endoscopy, colonoscopy, EUS and ERCP.

📲 Book on WhatsApp or call (number in bio), or directly at the clinic.
Timings may change in the coming weeks; the latest are always on drlochab.com.

#Gurugram #Gurgaon #Gastroenterologist #Sector52 #GutHealth #LiverHealth #DrLochab"""

STORY_NOTE = """Instagram story tips:
• Add a Location sticker: Apollo Clinic, Sector 52, Gurugram.
• Add a Link sticker to https://drlochab.com/gastroenterologist-in-gurgaon/ near the bottom.
• Optional: a second Link sticker with the Book link https://wa.me/919667104882"""

GBP_TEXT = f"""Now also consulting at Apollo Clinic, Sector 52, Gurugram.

{WHEN}. Arcura Clinic, Sector 51 continues on Monday to Friday 6 to 8 pm and Sunday 9 am to 1 pm.

Consultations for acidity, gas and bloating, constipation, fatty liver, jaundice, IBS and other stomach and liver problems, and for endoscopy, colonoscopy, EUS and ERCP. Adults and teenagers aged 12 and above, in English and Hindi.

Appointments can be booked on WhatsApp or directly at the clinic. Timings may change in the coming weeks; the latest are on drlochab.com.

Button: Learn more → https://drlochab.com/gastroenterologist-in-gurgaon/"""

WHATSAPP_EN = f"""📍 *Now also at Apollo Clinic, Sector 52, Gurugram*

🕓 {WHEN}
Arcura Clinic, Sector 51 continues: Mon–Fri 6–8 pm, Sunday 9 am–1 pm

Book by replying here or calling, or directly at the clinic.
Directions: {clinics.APOLLO_CLINIC["map"]}
Latest timings: https://drlochab.com

– Dr. Kshitij Lochab, Gastroenterologist"""

AH = clinics.APOLLO_CLINIC["hi"]
WHATSAPP_HI = f"""📍 *अब अपोलो क्लिनिक, सेक्टर 52, गुरुग्राम में भी*

🕓 {"; ".join(f"{d}, {h}" for d, h in AH["hours"])}
आर्क्योरा क्लिनिक, सेक्टर 51 में भी जारी: सोम–शुक्र शाम 6–8 बजे, रविवार सुबह 9–दोपहर 1 बजे

इसी नंबर पर जवाब देकर या कॉल करके, या सीधे क्लिनिक पर अपॉइंटमेंट लें।
रास्ता: {clinics.APOLLO_CLINIC["map"]}
ताज़ा समय: https://drlochab.com/hi

– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        render(post, 1080, 1350, f"{OUT}/insta-post.png", b)
        render(story, 1080, 1920, f"{OUT}/insta-story.png", b)
        render(lambda: status(False), 1080, 1920, f"{OUT}/whatsapp-status-en.png", b)
        render(lambda: status(True), 1080, 1920, f"{OUT}/whatsapp-status-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
    for name, txt in [("instagram-caption.txt", CAPTION + "\n\n" + STORY_NOTE), ("google-business-post.txt", GBP_TEXT),
                      ("whatsapp-message-en.txt", WHATSAPP_EN), ("whatsapp-message-hi.txt", WHATSAPP_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done")
