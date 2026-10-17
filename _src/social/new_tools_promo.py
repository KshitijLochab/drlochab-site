"""Instagram carousel (EN, 6 slides, 1080x1350) promoting the new tools on drlochab.com (live 17 Oct 2026):
Gut Health Tracker (private), stool check, Food of the day, plus the Diwali guide on the last slide.
Run: python3 _src/social/new_tools_promo.py  -> _src/out/new-tools-promo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS, foot, SRC
from stool_check import _shape, _swatch
from guide_art import diwali
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "new-tools-promo"); os.makedirs(OUT, exist_ok=True)
N = 6

LOCK = ('<svg viewBox="0 0 64 64" style="width:100%;height:100%"><rect x="12" y="28" width="40" height="30" rx="7" fill="#F3B84A"/>'
        '<path d="M20 28 V20 a12 12 0 0 1 24 0 V28" fill="none" stroke="#F3B84A" stroke-width="6" stroke-linecap="round"/>'
        '<circle cx="32" cy="41" r="4.5" fill="#12302C"/><rect x="30" y="43" width="4" height="8" rx="2" fill="#12302C"/></svg>')

def phone(inner, w=420, tilt=-4):
    h = int(w * 1.9)
    return (f'<div style="width:{w}px;height:{h}px;border-radius:{int(w*.13)}px;background:#12302C;padding:{int(w*.045)}px;transform:rotate({tilt}deg);'
            f'box-shadow:0 40px 80px rgba(0,0,0,.35)"><div style="width:100%;height:100%;border-radius:{int(w*.1)}px;background:#F3F7F6;overflow:hidden;position:relative;padding:{int(w*.07)}px {int(w*.06)}px">{inner}</div></div>')

def bars_svg(vals, goal=None, col="#0D7466", hi=None):
    n = len(vals); bw = 300 / n
    b = "".join(f'<rect x="{i*bw+bw*.18:.1f}" y="{110-v*10:.1f}" width="{bw*.64:.1f}" height="{v*10:.1f}" rx="5" fill="{hi if (hi and i==n-1) else col}"/>' for i, v in enumerate(vals))
    g = f'<line x1="0" x2="300" y1="{110-goal*10}" y2="{110-goal*10}" stroke="#12302C" stroke-dasharray="6 6" stroke-width="2" opacity=".5"/>' if goal else ""
    return f'<svg viewBox="0 0 300 116" style="width:100%;display:block"><line x1="0" x2="300" y1="111" y2="111" stroke="#D3E0DC" stroke-width="2"/>{g}{b}</svg>'

def tracker_screen(big=False):
    chip = lambda t, on=False: f'<span style="display:inline-block;border:2px solid {"#0D7466" if on else "#D3E0DC"};background:{"#E6F2EF" if on else "#fff"};border-radius:999px;padding:6px 14px;font-size:17px;font-weight:600;color:#12302C;margin:0 6px 8px 0">{t}</span>'
    types = "".join(f'<div style="flex:1;border:2px solid {"#0D7466" if i==3 else "#D3E0DC"};background:{"#E6F2EF" if i==3 else "#fff"};border-radius:10px;padding:4px 2px"><svg viewBox="0 0 120 64" style="width:100%">{_shape(i+1)}</svg></div>' for i in range(7))
    return f"""
 <div style="font-family:YS;font-size:30px;color:#12302C">My gut tracker</div>
 <div style="font-size:16px;color:#4A615D;margin:2px 0 14px">Today · saved on this phone</div>
 <div style="font-weight:600;font-size:18px;color:#12302C;margin-bottom:6px">Stool type</div>
 <div style="display:flex;gap:5px;margin-bottom:14px">{types}</div>
 <div style="font-weight:600;font-size:18px;color:#12302C;margin-bottom:6px">Symptoms</div>
 <div>{chip("Bloating: mild", True)}{chip("Pain: none")}{chip("Acidity: none")}</div>
 <div style="font-weight:600;font-size:18px;color:#12302C;margin:8px 0 6px">Triggers</div>
 <div>{chip("Milk", True)}{chip("Fried food")}{chip("Stress", True)}</div>
 <div style="background:#fff;border:2px solid #D3E0DC;border-radius:16px;padding:12px 14px;margin-top:10px">
  <div style="font-weight:600;font-size:17px;color:#12302C;margin-bottom:6px">Bowel movements, 14 days</div>{bars_svg([1,2,1,1,3,2,1,1,2,1,1,2,1,1], hi="#F3B84A")}</div>"""

def slide1():
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on drlochab.com</div>
 <h1 style="font-size:104px;margin-top:20px">Your gut,<br><em>tracked</em> and<br><em>decoded</em></h1>
 <div style="font-size:36px;margin-top:26px;color:#CFE5E0;width:520px;line-height:1.3">Three free tools for a healthier gut. Swipe →</div>
 <div style="position:absolute;right:64px;top:480px">{phone(tracker_screen(), 372, -6)}</div>
 <div style="position:absolute;left:84px;top:820px;display:flex;flex-direction:column;gap:16px">
  {''.join(f'<span class="chip" style="background:rgba(255,255,255,.12);font-size:30px;padding:16px 28px"><span style="width:16px;height:16px;border-radius:50%;background:{c}"></span>{t}</span>' for t, c in [("Gut Health Tracker", "#F3B84A"), ("Stool check", "#C98A55"), ("Food of the day", "#9CC069")])}
 </div>
 {foot(1, N, light=True, pad=84)}</div>"""

def slide2():
    tick = lambda t: f'<div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:600"><span style="flex:none;width:46px;height:46px;border-radius:50%;background:#0D7466;color:#fff;display:grid;place-items:center;font-size:28px">✓</span>{t}</div>'
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#0D7466">Gut Health Tracker</div>
 <h1 style="font-size:92px;margin-top:16px">One minute<br>a day. <em>Clear</em><br><em>patterns.</em></h1>
 <div style="position:absolute;left:84px;top:640px;display:flex;flex-direction:column;gap:26px;width:500px">
  {tick("Bowel habits and stool type")}{tick("Bloating, pain, acidity")}{tick("Food triggers, water, activity")}{tick("Weekly graphs")}
 </div>
 <div style="position:absolute;right:70px;top:330px">{phone(tracker_screen(), 400, 5)}</div>
 {foot(2, N, pad=84)}</div>"""

def slide3():
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px;text-align:center">
 <div class="kick" style="font-size:26px;color:#F3B84A">Private by design</div>
 <h1 style="font-size:96px;margin-top:18px">Your data<br>stays on <em>your phone</em></h1>
 <div style="width:300px;height:300px;margin:60px auto 0;border-radius:50%;background:rgba(255,255,255,.1);padding:56px">{LOCK}</div>
 <div style="display:flex;justify-content:center;gap:18px;margin-top:60px;flex-wrap:wrap">
  {''.join(f'<span class="chip" style="background:rgba(255,255,255,.12);font-size:32px;padding:18px 30px">{t}</span>' for t in ["No sign-in", "Nothing uploaded", "Optional PIN lock"])}
 </div>
 <div style="font-size:32px;color:#CFE5E0;margin-top:44px">Print a report for your doctor when you choose.</div>
 {foot(3, N, light=True, pad=84)}</div>"""

def slide4():
    shapes = "".join(f'<div style="background:#fff;border-radius:22px;padding:14px 10px 8px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.08)"><svg viewBox="0 0 120 64" style="width:100%">{_shape(i+1)}</svg><div style="font-weight:600;font-size:24px;color:#12302C">{i+1}</div></div>' for i in range(7))
    cols = "".join(f'<svg viewBox="20 12 80 44" style="width:110px">{_swatch(k)}</svg>' for k in ["brown", "green", "yellow", "pale", "black", "red"])
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#B4531C">Stool check</div>
 <h1 style="font-size:96px;margin-top:16px">What does<br>your stool <em style="color:#B4531C">say?</em></h1>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:56px">{shapes}
  <div style="display:grid;place-items:center;font-family:YS;font-size:40px;color:#B4531C">Shape</div></div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:40px;background:#fff;border-radius:26px;padding:20px 26px">{cols}</div>
 <div style="font-size:36px;margin-top:40px;line-height:1.3">Pick the shape and colour. See what it means and <b>when to see a doctor.</b></div>
 {foot(4, N, pad=84)}</div>"""

def guava(size=420):
    return (f'<svg viewBox="0 0 200 200" style="width:{size}px;height:{size}px"><ellipse cx="100" cy="188" rx="64" ry="8" fill="#12302C" opacity=".12"/>'
            '<path d="M100 40 C150 40 176 86 170 126 C164 166 132 182 100 182 C68 182 36 166 30 126 C24 86 50 40 100 40Z" fill="#8DC04A"/>'
            '<path d="M100 40 C150 40 176 86 170 126 C164 166 132 182 100 182" fill="none" stroke="#6E9A3A" stroke-width="5"/>'
            '<ellipse cx="72" cy="88" rx="14" ry="24" fill="#fff" opacity=".3"/>'
            '<path d="M100 42 C100 28 108 20 118 16" stroke="#5A3A1A" stroke-width="6" fill="none" stroke-linecap="round"/>'
            '<path d="M106 32 C120 12 146 14 152 24 C138 36 120 38 106 32Z" fill="#3F8A3A"/>'
            '<g transform="translate(118 96)"><circle r="34" fill="#F7B5A8"/><circle r="22" fill="#F29C8C"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF3D9"/>' for x, y in [(-10,-6),(8,-10),(12,6),(-4,10),(0,-2),(-14,6)]) + '</g></svg>')

def slide5():
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#4E7A1E">Food of the day</div>
 <h1 style="font-size:96px;margin-top:16px">A new gut-friendly<br>food, <em style="color:#4E7A1E">every day</em></h1>
 <div style="position:absolute;left:60px;top:470px">{guava(470)}</div>
 <div style="position:absolute;right:84px;top:560px;width:430px;background:#fff;border:4px solid #8DB33A;border-radius:34px;padding:34px 34px 30px;transform:rotate(2deg);box-shadow:0 20px 40px rgba(0,0,0,.12)">
  <span style="display:inline-block;background:#4E7A1E;color:#fff;font-weight:600;letter-spacing:.12em;font-size:22px;padding:6px 14px;border-radius:10px">TODAY</span>
  <div style="font-family:YS;font-size:62px;margin-top:14px">Guava</div>
  <div style="font-size:30px;font-weight:600;margin-top:6px;color:#4E7A1E">About 5 g fibre</div>
  <div style="font-size:28px;margin-top:14px;line-height:1.35">Keeps stools soft and regular. Eat it whole, with the peel.</div>
  <div style="font-size:24px;color:#4A615D;margin-top:18px">Tomorrow: <b style="color:#12302C">Ragi</b></div>
 </div>
 <div style="position:absolute;left:84px;right:84px;top:1050px;font-size:34px;line-height:1.3">Why it helps, how to eat it, and who should be careful.</div>
 {foot(5, N, pad=84)}</div>"""

def slide6(li=False):
    art = diwali("").replace('role="img" aria-label=""', 'aria-hidden="true"').replace('var(--accent-soft)', '#0F7D6E')
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px;text-align:center">
 <div class="kick" style="font-size:26px;color:#F3B84A">Free · English and Hindi</div>
 <h1 style="font-size:100px;margin-top:18px">Try them<br>today on</h1>
 <div style="display:inline-block;margin-top:40px;background:#F3B84A;color:#12302C;font-family:YS;font-size:84px;padding:24px 56px;border-radius:999px">drlochab.com</div>
 <div style="font-size:34px;color:#CFE5E0;margin-top:26px">{"No sign-in · hindi: drlochab.com/hi".replace("hindi","हिंदी में") if li else "Link in bio · हिंदी में भी: drlochab.com/hi"}</div>
 <div style="margin:56px auto 0;width:760px;background:rgba(255,255,255,.1);border-radius:34px;padding:22px 30px;display:flex;align-items:center;gap:22px;text-align:left">
  <div style="flex:none;width:220px">{art}</div>
  <div><div class="kick" style="font-size:22px;color:#F3B84A">Also new</div><div style="font-family:YS;font-size:44px;line-height:1.15;margin-top:6px">Diwali food guide: enjoy the sweets without acidity</div></div>
 </div>
 {foot(6, N, light=True, pad=84)}</div>"""

CAPTION = """Your gut, tracked and decoded 📊

Three new free tools on drlochab.com:

1️⃣ Gut Health Tracker: log bowel habits, stool type, bloating, pain, acidity, food triggers, water and activity in about a minute a day. See weekly graphs and print a clear summary to show your doctor.
🔒 Private by design: your entries stay on your own phone. No sign-in, nothing uploaded, optional PIN lock.

2️⃣ What does your stool say? Pick the shape and colour to see what it usually means and when to see a doctor.

3️⃣ Food of the day: a new gut-friendly Indian food every day, with why it helps and who should be careful.

Plus a Diwali food guide to enjoy the sweets without acidity.

All free, in English and Hindi. Link in bio 👉 drlochab.com

Black or tarry stools, vomiting blood or severe belly pain are an emergency: call 112 or go to the nearest emergency department.

#GutHealth #Gastroenterologist #IBS #DigestiveHealth #GutHealthTracker #Gurugram #HealthyGut #DrLochab"""

LINKEDIN = """New on my website: three free, privacy-first gut-health tools for patients

Many patients with IBS, constipation, bloating or reflux come to a consultation unsure how often symptoms happen or what sets them off. To help, I have added three simple tools to drlochab.com, in English and Hindi:

1. Gut Health Tracker: patients log bowel habits, stool type, bloating, pain, acidity, possible food triggers, water and activity in about a minute a day. It shows weekly graphs and creates a one-page summary to bring to the doctor. Warning signs such as blood in the stool or black stools prompt the patient to seek care.

2. Stool check: shape (based on the Bristol stool form scale) and colour, explained separately, with clear advice on when to see a doctor.

3. Food of the day: one gut-friendly Indian food every day, with why it helps and who should be careful.

Privacy was the first design rule. Entries stay only on the patient's own phone: no account, no upload, no tracking, and an optional PIN that encrypts the data. The page is technically blocked from sending data anywhere; patients share a report only when they choose to.

Colleagues: if you see patients with functional bowel symptoms, two to four weeks of tracking before a referral can make the first visit far more productive. The tools are free for anyone to use.

drlochab.com

#Gastroenterology #DigitalHealth #PatientEducation #IBS #Gurugram"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([slide1, slide2, slide3, slide4, slide5, slide6], 1):
            pg = b.new_page(viewport={"width": 1080, "height": 1350})
            path = f"{OUT}/tmp.html"
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{f()}</body></html>")
            pg.goto(f"file://{path}"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/slide-{i}.png"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html")
    open(f"{OUT}/caption.txt", "w").write(CAPTION + "\n")
    # LinkedIn document post: same slides, LinkedIn wording on the last slide, as one PDF
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{slide6(True)}</body></html>")
        pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/slide-6-linkedin.png"); b.close()
    os.remove(f"{OUT}/tmp.html")
    pages = [Image.open(f"{OUT}/slide-{i}.png").convert("RGB") for i in range(1, 6)] + [Image.open(f"{OUT}/slide-6-linkedin.png").convert("RGB")]
    pages[0].save(f"{OUT}/linkedin-gut-tools.pdf", save_all=True, append_images=pages[1:], resolution=144, quality=95)
    open(f"{OUT}/linkedin-caption.txt", "w").write(LINKEDIN + "\n")
    print("done")
