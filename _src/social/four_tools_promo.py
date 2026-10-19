"""One promo for all four free tools on drlochab.com (19 Oct 2026): Food of the day, Gut Health Tracker, Stool check, Diet charts + food diary.
Instagram post (carousel, 6 slides, 1080x1350), Instagram story / WhatsApp status (6 frames, 1080x1920),
LinkedIn single image (1080x1350) and document PDF, plus captions and WhatsApp messages (EN, HI).
Run: python3 _src/social/four_tools_promo.py  -> _src/out/four-tools-promo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS, foot, SRC
from new_tools_promo import phone, tracker_screen, guava, LOCK, bars_svg
from diet_charts_promo import chart_screen, diary_screen, plate, mark
from stool_check import _shape, _swatch
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "four-tools-promo"); os.makedirs(OUT, exist_ok=True)
N = 6
TOOLS = [  # name, one-liner, accent, page
 ("Food of the day", "A gut-friendly Indian food, every day", "#4E7A1E", "drlochab.com"),
 ("Gut Health Tracker", "Log symptoms in a minute; weekly graphs", "#0D7466", "drlochab.com/tools/gut-tracker"),
 ("Stool check", "Shape and colour: what it means", "#B4531C", "drlochab.com/tools/stool-check"),
 ("Diet charts", "12 conditions, plus a food diary", "#34548A", "drlochab.com/diet-charts"),
]

def icon(i, s=150):
    if i == 0:
        return guava(s)
    if i == 1:
        bars = "".join(f'<rect x="{8+i*10}" y="{56-v}" width="7" height="{v}" rx="2" fill="{"#F3B84A" if i==4 else "#0D7466"}"/>' for i, v in enumerate([18, 30, 22, 38, 44]))
        return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px"><circle cx="32" cy="32" r="31" fill="#E6F2EF"/>{bars}'
                '<path d="M10 40 L22 28 L32 33 L44 18 L54 12" fill="none" stroke="#12302C" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    if i == 2:
        return f'<div style="width:{s}px;padding:{s*.06}px;background:#fff;border-radius:{s*.16}px"><svg viewBox="0 0 120 64" style="width:100%">{_shape(4)}</svg></div>'
    return plate(3, s)

def tile(i, big=False):
    n, d, c, _ = TOOLS[i]
    s = 200 if big else 120
    return (f'<div style="background:#fff;border-radius:30px;padding:26px 24px;display:flex;flex-direction:column;align-items:flex-start;gap:14px;box-shadow:0 14px 30px rgba(0,0,0,.18)">'
            f'<div style="height:{s}px;display:flex;align-items:center">{icon(i, s)}</div>'
            f'<div style="font-family:YS;font-size:{52 if big else 38}px;line-height:1.05;color:#12302C">{n}</div>'
            f'<div style="font-size:{31 if big else 24}px;line-height:1.3;color:#4A615D">{d}</div>'
            f'<span style="width:60px;height:7px;border-radius:9px;background:{c}"></span></div>')

def cover(h=1350, n=1, total=N, story=False):
    top = 150 if story else 96
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:{top}px 84px">
 <div class="kick" style="font-size:{32 if story else 28}px;color:#F3B84A">Free on drlochab.com</div>
 <h1 style="font-size:{112 if story else 96}px;margin-top:18px">4 tools for a<br><em>healthier gut</em></h1>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:{26 if story else 20}px;margin-top:{70 if story else 50}px">{"".join(tile(i, story) for i in range(4))}</div>
 <div style="font-size:{36 if story else 30}px;color:#CFE5E0;margin-top:{60 if story else 34}px">English and हिंदी · No sign-in · {"Tap" if story else "Swipe"} →</div>
 {foot(None if story else n, total, light=True, pad=84, size=1.2 if story else 1)}</div>"""

def food(h=1350, n=2, story=False):
    y = 420 if story else 0
    return f"""<div class="s cream" style="width:1080px;height:{h}px;padding:{150 if story else 96}px 84px">
 <div class="kick" style="font-size:28px;color:#4E7A1E">1 · Food of the day</div>
 <h1 style="font-size:{104 if story else 92}px;margin-top:16px">{"A new<br>gut-friendly food,<br>" if story else "A new gut-friendly<br>food, "}<em style="color:#4E7A1E">every day</em></h1>
 <div style="position:absolute;left:50px;top:{470+y}px">{guava(470)}</div>
 <div style="position:absolute;right:80px;top:{560+y}px;width:440px;background:#fff;border:4px solid #8DB33A;border-radius:34px;padding:34px;transform:rotate(2deg);box-shadow:0 20px 40px rgba(0,0,0,.12)">
  <span style="display:inline-block;background:#4E7A1E;color:#fff;font-weight:600;letter-spacing:.12em;font-size:22px;padding:6px 14px;border-radius:10px">TODAY</span>
  <div style="font-family:YS;font-size:62px;margin-top:14px">Guava</div>
  <div style="font-size:30px;font-weight:600;margin-top:6px;color:#4E7A1E">About 5 g fibre</div>
  <div style="font-size:28px;margin-top:14px;line-height:1.35">Keeps stools soft and regular. Eat it whole, with the peel.</div>
 </div>
 <div style="position:absolute;left:84px;right:84px;top:{1060+y}px;font-size:{38 if story else 34}px;line-height:1.3">Why it helps, how to eat it, and who should be careful. A new one every morning.</div>
 {foot(None if story else n, N, pad=84, size=1.2 if story else 1)}</div>"""

def tracker(h=1350, n=3, story=False):
    tick = lambda t: (f'<div style="display:flex;gap:16px;align-items:center;font-size:{36 if story else 33}px;font-weight:600"><span style="flex:none;width:44px;height:44px;border-radius:50%;'
                      f'background:#0D7466;color:#fff;display:grid;place-items:center;font-size:26px">✓</span>{t}</div>')
    if story:
        return f"""<div class="s mint" style="width:1080px;height:{h}px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#0D7466">2 · Gut Health Tracker</div>
 <h1 style="font-size:104px;margin-top:16px">One minute a day.<br><em>Clear patterns.</em></h1>
 <div style="position:absolute;left:50%;top:640px;transform:translateX(-50%)">{phone(tracker_screen(), 470, -3)}</div>
 <div style="position:absolute;left:84px;right:84px;bottom:190px;display:flex;justify-content:center;align-items:center;gap:18px;background:#0B6A5E;color:#fff;border-radius:999px;padding:22px 30px;font-size:34px;font-weight:600">
  <span style="width:44px;height:44px">{LOCK}</span>Stays on your phone · no sign-in</div>
 {foot(None, N, pad=84, size=1.2)}</div>"""
    return f"""<div class="s mint" style="width:1080px;height:{h}px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#0D7466">2 · Gut Health Tracker</div>
 <h1 style="font-size:88px;margin-top:16px">One minute a day.<br><em>Clear patterns.</em></h1>
 <div style="position:absolute;left:84px;top:560px;display:flex;flex-direction:column;gap:24px;width:500px">
  {tick("Bowel habits, stool type")}{tick("Bloating, pain, acidity")}{tick("Food triggers, water")}{tick("Weekly graphs")}{tick("Report for your doctor")}
  <div style="display:flex;gap:14px;align-items:center;font-size:28px;font-weight:600;color:#0D7466;margin-top:8px"><span style="width:38px;height:38px;background:#0B6A5E;border-radius:50%;padding:6px">{LOCK}</span>Private: stays on your phone</div>
 </div>
 <div style="position:absolute;right:64px;top:350px">{phone(tracker_screen(), 400, 5)}</div>
 {foot(n, N, pad=84)}</div>"""

def stool(h=1350, n=4, story=False):
    shapes = "".join(f'<div style="background:#fff;border-radius:22px;padding:14px 10px 8px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,.08)"><svg viewBox="0 0 120 64" style="width:100%">{_shape(i+1)}</svg>'
                     f'<div style="font-weight:600;font-size:22px;color:#4A615D">Type {i+1}</div></div>' for i in range(7))
    cols = "".join(f'<svg viewBox="20 12 80 44" style="width:{120 if story else 110}px">{_swatch(k)}</svg>' for k in ["brown", "green", "yellow", "pale", "black", "red"])
    return f"""<div class="s saffron" style="width:1080px;height:{h}px;padding:{150 if story else 96}px 84px">
 <div class="kick" style="font-size:28px;color:#B4531C">3 · Stool check</div>
 <h1 style="font-size:{108 if story else 92}px;margin-top:16px">What does<br>your stool <em style="color:#B4531C">say?</em></h1>
 <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:{90 if story else 50}px">{shapes}
  <div style="display:grid;place-items:center;font-family:YS;font-size:40px;color:#B4531C">Shape</div></div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:{50 if story else 34}px;background:#fff;border-radius:26px;padding:20px 26px">{cols}</div>
 <div style="font-size:{40 if story else 34}px;margin-top:{60 if story else 36}px;line-height:1.3">Pick the shape and the colour. See what each one means, and <b>when to see a doctor.</b></div>
 {foot(None if story else n, N, pad=84, size=1.2 if story else 1)}</div>"""

def diet(h=1350, n=5, story=False):
    if story:
        return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#F3B84A">4 · Diet charts + food diary</div>
 <h1 style="font-size:100px;margin-top:16px">“Doctor, what<br>should I <em>eat?</em>”</h1>
 <div style="font-size:38px;color:#CFE5E0;margin-top:20px;line-height:1.3">12 conditions · veg, egg and non-veg · a diary that shows what your day is missing</div>
 <div style="position:absolute;left:70px;top:820px">{phone(chart_screen(), 420, -5)}</div>
 <div style="position:absolute;right:70px;top:900px">{phone(diary_screen(), 420, 5)}</div>
 {foot(None, N, light=True, pad=84, size=1.2)}</div>"""
    chips = "".join(f'<span style="display:inline-block;background:rgba(255,255,255,.12);border-radius:999px;padding:12px 22px;font-size:26px;font-weight:600;margin:0 10px 12px 0">{t}</span>'
                    for t in ["Fatty liver", "Acidity", "IBS", "Constipation", "Gallstones", "Cirrhosis", "Jaundice", "Pancreatitis", "Ulcerative colitis & Crohn's", "Celiac", "Loose motions", "Everyday gut health"])
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">4 · Diet charts + food diary</div>
 <h1 style="font-size:86px;margin-top:16px">“Doctor, what<br>should I <em>eat?</em>”</h1>
 <div style="width:520px;margin-top:36px">{chips}</div>
 <div style="width:520px;font-size:30px;color:#CFE5E0;line-height:1.35;margin-top:14px">Veg, egg and non-veg days. A food diary that shows what you are missing. Advice for diabetes, BP, kidney disease and pregnancy.</div>
 <div style="position:absolute;right:56px;top:360px">{phone(diary_screen(), 400, 5)}</div>
 {foot(n, N, light=True, pad=84)}</div>"""

def cta(h=1350, n=6, story=False, li=False):
    rows = "".join(f'<div style="display:flex;align-items:center;gap:20px;background:rgba(255,255,255,.1);border-radius:24px;padding:16px 22px;text-align:left">'
                   f'<div style="flex:none;width:{84 if story else 72}px;height:{84 if story else 72}px;display:flex;align-items:center;justify-content:center;overflow:hidden">{icon(i, 84 if story else 72)}</div>'
                   f'<div><div style="font-family:YS;font-size:{38 if story else 34}px">{n_}</div><div style="font-size:{26 if story else 23}px;color:#CFE5E0">{u}</div></div></div>'
                   for i, (n_, _, _, u) in enumerate(TOOLS))
    sub = "हिंदी में: drlochab.com/hi" if li else ("Link in bio · हिंदी में भी" if not story else "हिंदी में: drlochab.com/hi")
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:{170 if story else 90}px 84px;text-align:center">
 <div class="kick" style="font-size:{30 if story else 26}px;color:#F3B84A">Free · Private · No sign-in</div>
 <h1 style="font-size:{108 if story else 92}px;margin-top:18px">Try them today</h1>
 <div style="display:inline-block;margin-top:{40 if story else 30}px;background:#F3B84A;color:#12302C;font-family:YS;font-size:{80 if story else 72}px;padding:20px 54px;border-radius:999px">drlochab.com</div>
 <div style="font-size:{34 if story else 30}px;color:#CFE5E0;margin-top:20px">{sub}</div>
 <div style="display:flex;flex-direction:column;gap:14px;margin-top:{60 if story else 40}px">{rows}</div>
 {f'<div style="font-size:36px;color:#fff;margin-top:60px;line-height:1.4">Appointments: Arcura Clinic, Sector 51, Gurugram<br><span style="color:#CFE5E0">Mon–Fri 6–8 pm · Sun 9 am–1 pm</span></div>' if story else ""}
 {foot(None if story else n, N, light=True, pad=84, size=1.2 if story else 1)}</div>"""

def linkedin_single():
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:90px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">Free · privacy-first · English and Hindi</div>
 <h1 style="font-size:84px;margin-top:16px">Four patient tools<br>for <em>gut health</em></h1>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:46px">{"".join(tile(i) for i in range(4))}</div>
 <div style="display:flex;justify-content:space-between;align-items:center;margin-top:34px">
  <div style="font-size:30px;color:#CFE5E0;line-height:1.35">Data stays on the patient's phone.<br>No sign-in, nothing uploaded.</div>
  <div style="background:#F3B84A;color:#12302C;font-family:YS;font-size:44px;padding:14px 32px;border-radius:999px">drlochab.com</div></div>
 {foot(None, light=True, pad=84)}</div>"""

CAPTION = """4 free tools for a healthier gut 🌿

All on drlochab.com, in English and Hindi, with no sign-in:

🍐 Food of the day: one gut-friendly Indian food every morning, with why it helps, how to eat it, and who should be careful.

📊 Gut Health Tracker: log bowel habits, stool type, bloating, pain, acidity, food triggers and water in about a minute a day. See weekly graphs and print a report for your doctor. 🔒 Your entries stay on your own phone.

💩 Stool check: pick the shape and colour to see what it usually means and when to see a doctor.

🍽️ Diet charts: Indian diet charts for 12 conditions, including fatty liver, acidity, IBS, constipation, gallstones, cirrhosis, pancreatitis, and ulcerative colitis & Crohn's disease, with veg, egg and non-veg options, plus a food diary that shows what your day is missing.

Save this post and share it with someone who keeps asking about their tummy 👇
Link in bio 👉 drlochab.com

Black or tarry stools, vomiting blood or severe belly pain are an emergency: call 112 or go to the nearest emergency department.

#GutHealth #DigestiveHealth #DietChart #IBS #FattyLiver #Constipation #Gastroenterologist #Gurugram #HealthyGut #DrLochab"""

STORY_NOTE = """Instagram story tips:
• Frame 1: add a poll sticker, e.g. "Do you check your stool?" Yes / Never
• Frame 6: add a Link sticker to https://drlochab.com over the empty space near the bottom
• Optional: add the "Book" link (https://wa.me/919667104882) as a second link sticker on frame 6"""

WHATSAPP_EN = """🌿 *4 free tools for a healthier gut*

On my website, in English and Hindi, with no sign-in:

🍐 *Food of the day*: one gut-friendly Indian food every day
📊 *Gut Health Tracker*: log symptoms in a minute, see weekly graphs, print a report for your doctor (stays on your phone)
💩 *Stool check*: what the shape and colour mean, and when to see a doctor
🍽️ *Diet charts*: 12 conditions, veg, egg and non-veg, with a food diary

👉 https://drlochab.com
हिंदी में: https://drlochab.com/hi

Please share with family and friends.
– Dr. Kshitij Lochab, Gastroenterologist, Arcura Clinic, Sector 51, Gurugram"""

WHATSAPP_HI = """🌿 *पेट की सेहत के लिए 4 मुफ़्त टूल*

मेरी वेबसाइट पर, हिंदी और अंग्रेज़ी में, बिना साइन-इन के:

🍐 *आज का खाना*: हर दिन पेट के लिए फ़ायदेमंद एक भारतीय खाना
📊 *पेट की सेहत का ट्रैकर*: एक मिनट में लक्षण लिखें, हफ़्ते के ग्राफ़ देखें, डॉक्टर के लिए रिपोर्ट निकालें (सिर्फ़ आपके फ़ोन पर)
💩 *मल की जाँच*: आकार और रंग का क्या मतलब है, और कब डॉक्टर को दिखाएँ
🍽️ *डाइट चार्ट*: 12 बीमारियों के लिए, शाकाहारी, अंडा और मांसाहारी विकल्पों और फ़ूड डायरी के साथ

👉 https://drlochab.com/hi

परिवार और दोस्तों के साथ ज़रूर शेयर करें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम"""

LINKEDIN = """Four free, privacy-first gut-health tools for patients, now on drlochab.com

Good gastroenterology care depends on what happens between visits: what patients eat, how their symptoms behave, and whether they recognise warning signs early. I have built four simple tools to help with that, in English and Hindi:

1. Food of the day: one gut-friendly Indian food each day, with practical advice on how to eat it and who should be careful.

2. Gut Health Tracker: bowel habits, stool type, bloating, pain, acidity, likely food triggers and water intake, logged in about a minute a day, with weekly graphs and a one-page report for the consultation.

3. Stool check: Bristol stool form and colour explained separately, with clear guidance on when to see a doctor.

4. Diet charts: Indian diet charts for 12 conditions (including fatty liver, cirrhosis, pancreatitis, IBS, and ulcerative colitis and Crohn's disease, with a separate plan for stricturing Crohn's), veg, egg and non-veg options, caveats for diabetes, CKD, hypertension and pregnancy, and a food diary that shows what the day is missing.

Privacy was the first design rule: entries stay on the patient's own phone, with no account and nothing uploaded.

Colleagues are welcome to share these with patients; feedback on the clinical content is always welcome.

drlochab.com

#Gastroenterology #PatientEducation #DigitalHealth #GutHealth #ClinicalNutrition #Gurugram"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    post = [cover, food, tracker, stool, diet, cta]
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate(post, 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/post-{i}.png", b)
            render(lambda: f(h=1920, story=True), 1080, 1920, f"{OUT}/story-{i}.png", b)
        render(lambda: cta(n=6, li=True), 1080, 1350, f"{OUT}/post-6-linkedin.png", b)
        render(linkedin_single, 1080, 1350, f"{OUT}/linkedin-single.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
    pages = [Image.open(f"{OUT}/post-{i}.png").convert("RGB") for i in range(1, 6)] + [Image.open(f"{OUT}/post-6-linkedin.png").convert("RGB")]
    pages[0].save(f"{OUT}/linkedin-four-tools.pdf", save_all=True, append_images=pages[1:], resolution=144, quality=95)
    for name, text in [("instagram-caption", CAPTION), ("instagram-story-tips", STORY_NOTE), ("whatsapp-message-en", WHATSAPP_EN),
                       ("whatsapp-message-hi", WHATSAPP_HI), ("linkedin-caption", LINKEDIN)]:
        open(f"{OUT}/{name}.txt", "w").write(text + "\n")
    print("done")
