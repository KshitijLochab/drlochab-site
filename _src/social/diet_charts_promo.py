"""Promo set for the features added on 18-19 Oct 2026: diet charts for 12 conditions, the private food diary, comorbidity caveats,
the bigger Thali meter, winter and wedding season guide, easy WhatsApp booking, print and 'add to home screen'.
Instagram carousel (7 slides, 1080x1350), WhatsApp status (3 images, 1080x1920) and a LinkedIn document (PDF), plus captions.
Run: python3 _src/social/diet_charts_promo.py  -> _src/out/diet-charts-promo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS, foot, SRC
from new_tools_promo import phone
from guide_art import winter
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "diet-charts-promo"); os.makedirs(OUT, exist_ok=True)
N = 7
PL = ["#E7B54A", "#4E7A2E", "#D8562A", "#9BC46A", "#C98A4A", "#F3B84A", "#2E9C86", "#E9733F", "#7FA6B5", "#B9781E", "#5B8F3A", "#F2C75C"]

def plate(i, s=96):
    a, b, c = PL[i % 12], PL[(i + 5) % 12], PL[(i + 9) % 12]
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><circle cx="32" cy="32" r="30" fill="#E6F2EF"/><circle cx="32" cy="32" r="23" fill="#fff" stroke="#D3E0DC" stroke-width="2"/>'
            f'<path d="M32 32 L32 12 A20 20 0 0 1 49.3 42 Z" fill="{a}"/><path d="M32 32 L49.3 42 A20 20 0 0 1 14.7 42 Z" fill="{b}"/><path d="M32 32 L14.7 42 A20 20 0 0 1 32 12 Z" fill="{c}"/>'
            f'<circle cx="32" cy="32" r="7" fill="#fff"/></svg>')

def mark(kind, s=24):
    col = {"v": "#167A3E", "e": "#C9851F", "n": "#9C3B1E"}[kind]
    inner = (f'<path d="M{s*.5} {s*.2} L{s*.8} {s*.78} L{s*.2} {s*.78} Z" fill="{col}"/>' if kind == "n" else f'<circle cx="{s/2}" cy="{s/2}" r="{s*.26}" fill="{col}"/>')
    return f'<svg viewBox="0 0 {s} {s}" style="width:{s}px;height:{s}px;flex:none;margin-top:4px"><rect x="1.5" y="1.5" width="{s-3}" height="{s-3}" rx="3" fill="none" stroke="{col}" stroke-width="3"/>{inner}</svg>'

WEST = '<span style="display:inline-block;background:#E6F2EF;color:#0D7466;font-weight:700;font-size:15px;letter-spacing:.06em;padding:2px 10px;border-radius:999px;margin-left:6px;vertical-align:2px">WESTERN</span>'

def chart_screen(f=1.0):
    row = lambda slot, t, opts: (f'<div style="background:#fff;border:2px solid #D3E0DC;border-radius:{int(16*f)}px;padding:{int(12*f)}px {int(14*f)}px;margin-bottom:{int(10*f)}px">'
        f'<div style="font-family:YS;font-size:{int(22*f)}px;color:#12302C">{slot} <span style="font-family:FT;font-size:{int(15*f)}px;color:#4A615D">{t}</span></div>'
        + "".join(f'<div style="display:flex;gap:{int(10*f)}px;font-size:{int(17*f)}px;line-height:1.35;color:#12302C;margin-top:{int(7*f)}px">{mark(k, int(20*f))}<span>{x}</span></div>' for k, x in opts) + "</div>")
    return (f'<div style="font-size:{int(13*f)}px;font-weight:700;letter-spacing:.14em;color:#0D7466">DIET CHART</div>'
            f'<div style="font-family:YS;font-size:{int(30*f)}px;line-height:1.1;color:#12302C;margin:{int(6*f)}px 0 {int(14*f)}px">Fatty liver diet chart</div>'
            + row("Breakfast", "8–9 am", [("v", "2 moong dal chillas with curd"), ("e", "2 boiled eggs, 1 multigrain roti"), ("v", "Overnight oats, no sugar" + WEST.replace("15px", f"{int(12*f)}px"))])
            + row("Lunch", "1–2 pm", [("v", "Bajra roti, dal, sabzi, salad, curd"), ("n", "Fish or chicken curry with salad")])
            + row("Evening", "4–5 pm", [("v", "Roasted chana or sprouts chaat")])
            + row("Dinner", "7–8 pm", [("n", "Grilled fish with vegetables")]))

def diary_screen(f=1.0):
    def m(label, val, unit, pct, sub, col="#C9851F"):
        return (f'<div style="background:#F3F7F6;border-radius:{int(14*f)}px;padding:{int(10*f)}px {int(12*f)}px">'
                f'<div style="font-size:{int(12*f)}px;font-weight:700;letter-spacing:.08em;color:#4A615D">{label}</div>'
                f'<div style="font-family:YS;font-size:{int(28*f)}px;color:#12302C">{val}<span style="font-family:FT;font-size:{int(14*f)}px;color:#4A615D"> {unit}</span></div>'
                f'<div style="height:{int(7*f)}px;border-radius:9px;background:#D3E0DC"><div style="height:100%;width:{pct}%;border-radius:9px;background:{col}"></div></div>'
                f'<div style="font-size:{int(12*f)}px;color:#4A615D;margin-top:{int(4*f)}px">{sub}</div></div>')
    li = lambda t, c: f'<div style="position:relative;background:{c};border-radius:{int(12*f)}px;padding:{int(8*f)}px {int(10*f)}px {int(8*f)}px {int(28*f)}px;font-size:{int(15*f)}px;line-height:1.35;color:#12302C;margin-top:{int(7*f)}px"><span style="position:absolute;left:{int(10*f)}px;top:{int(13*f)}px;width:{int(9*f)}px;height:{int(9*f)}px;border-radius:50%;background:{"#B0362B" if c=="#F8E4E1" else "#C9851F"}"></span>{t}</div>'
    return (f'<div style="font-family:YS;font-size:{int(28*f)}px;color:#12302C;margin-bottom:{int(10*f)}px">Today\'s food</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:{int(8*f)}px">'
            + m("PROTEIN", "39", "g", 60, "aim 60–72 g") + m("FIBRE", "17.5", "g", 58, "at least 30 g")
            + m("FAT", "33", "g", 66, "under 50 g", "#2E9C86") + m("VEGETABLES", "1", "katori", 25, "4 or more") + "</div>"
            + f'<div style="font-size:{int(12*f)}px;font-weight:700;letter-spacing:.1em;color:#4A615D;margin-top:{int(14*f)}px">WHAT TODAY NEEDS</div>'
            + li("Cold drink: sugary. Best avoided.", "#F8E4E1") + li("Protein: about 21 g more today", "#F3F7F6") + li("Vegetables: 3 more katoris", "#F3F7F6")
            + f'<div style="font-size:{int(12*f)}px;font-weight:700;letter-spacing:.1em;color:#4A615D;margin-top:{int(14*f)}px">FOR THE REST OF TODAY</div>'
            + f'<div style="display:flex;justify-content:space-between;align-items:center;background:#F3F7F6;border-radius:{int(12*f)}px;padding:{int(9*f)}px {int(12*f)}px;margin-top:{int(7*f)}px">'
              f'<div><div style="font-size:{int(11*f)}px;font-weight:700;letter-spacing:.08em;color:#4A615D">DINNER</div><div style="font-size:{int(16*f)}px;font-weight:600;color:#12302C">Grilled fish + palak</div></div>'
              f'<span style="background:#0D7466;color:#fff;font-weight:700;font-size:{int(13*f)}px;border-radius:999px;padding:{int(6*f)}px {int(12*f)}px">+ Add</span></div>')

CONDS = ["Everyday gut health", "Fatty liver", "Acidity & gastritis", "IBS & bloating", "Constipation", "Gallstones", "Cirrhosis", "Jaundice",
         "Pancreatitis", "Ulcerative colitis & Crohn's", "Celiac (gluten-free)", "Loose motions"]

def s1():
    chips = "".join(f'<span class="chip" style="background:rgba(255,255,255,.12);font-size:30px;padding:16px 28px"><span style="width:16px;height:16px;border-radius:50%;background:{c}"></span>{t}</span>'
                    for t, c in [("12 conditions", "#F3B84A"), ("Veg · egg · non-veg", "#9BC46A"), ("Free food diary", "#7FD1C1")])
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:28px;color:#F3B84A">New on drlochab.com</div>
 <h1 style="font-size:100px;margin-top:20px">“Doctor,<br>what should<br>I <em>eat?</em>”</h1>
 <div style="font-size:36px;margin-top:24px;color:#CFE5E0;width:500px;line-height:1.3">Indian diet charts for gut and liver problems. Swipe →</div>
 <div style="position:absolute;right:60px;top:430px">{phone(chart_screen(), 400, -5)}</div>
 <div style="position:absolute;left:84px;top:860px;display:flex;flex-direction:column;gap:16px">{chips}</div>
 {foot(1, N, light=True, pad=84)}</div>"""

def s2():
    tiles = "".join(f'<div style="display:flex;align-items:center;gap:16px;background:#fff;border-radius:24px;padding:16px 18px;box-shadow:0 8px 20px rgba(0,0,0,.06)">{plate(i, 64)}'
                    f'<span style="font-family:YS;font-size:30px;line-height:1.1">{t}</span></div>' for i, t in enumerate(CONDS))
    return f"""<div class="s cream" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#0D7466">Diet charts</div>
 <h1 style="font-size:90px;margin-top:14px">One chart for<br><em>your condition</em></h1>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:48px">{tiles}</div>
 {foot(2, N, pad=84)}</div>"""

def s3():
    return f"""<div class="s mint" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#0D7466">A full sample day</div>
 <h1 style="font-size:88px;margin-top:14px">Real Indian food,<br>morning to <em>bedtime</em></h1>
 <div style="position:absolute;left:84px;top:520px;width:470px;display:flex;flex-direction:column;gap:30px">
  <div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:600">{mark("v", 44)}Vegetarian</div>
  <div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:600">{mark("e", 44)}With eggs</div>
  <div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:600">{mark("n", 44)}Non-veg</div>
  <div style="display:flex;gap:18px;align-items:center;font-size:36px;font-weight:600"><span style="background:#fff;color:#0D7466;font-weight:700;font-size:24px;letter-spacing:.06em;padding:6px 14px;border-radius:999px">WESTERN</span>quick options</div>
  <div style="font-size:30px;line-height:1.35;color:#4A615D;margin-top:14px">Plus daily targets, what to eat more of, what to cut down, and when to see a doctor.</div>
 </div>
 <div style="position:absolute;right:66px;top:360px">{phone(chart_screen(), 400, 4)}</div>
 {foot(3, N, pad=84)}</div>"""

def s4():
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">Free food diary</div>
 <h1 style="font-size:92px;margin-top:14px">See what your<br>day is <em>missing</em></h1>
 <div style="position:absolute;left:84px;top:560px;width:450px;display:flex;flex-direction:column;gap:26px;font-size:34px;line-height:1.3;color:#E6F2EF">
  <div><b style="color:#fff">Tap</b> what you ate, meal by meal</div>
  <div><b style="color:#fff">See</b> protein, fibre, fat, vegetables, fruit and water</div>
  <div><b style="color:#fff">Get</b> a warning for foods to avoid</div>
  <div><b style="color:#fff">Know</b> what to eat for the rest of the day</div>
  <div style="display:flex;gap:12px;align-items:center;font-size:28px;color:#F3B84A;font-weight:600;margin-top:6px">🔒 Stays on your phone</div>
 </div>
 <div style="position:absolute;right:56px;top:400px">{phone(diary_screen(), 410, 5)}</div>
 {foot(4, N, light=True, pad=84)}</div>"""

def s5():
    chips = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;background:#fff;border-radius:22px;padding:22px 28px;font-size:34px;font-weight:600;box-shadow:0 8px 20px rgba(0,0,0,.06)">{t}'
                    f'<span style="font-size:26px;font-weight:600;color:{c};background:{bg};padding:6px 16px;border-radius:999px">{s}</span></div>'
                    for t, s, c, bg in [("Diabetes", "sweets: avoid", "#B0362B", "#F8E4E1"), ("High BP or heart", "salt: avoid", "#B0362B", "#F8E4E1"),
                                         ("Kidney disease", "protein: ask doctor", "#8A5A12", "#FAEED8"), ("Pregnancy", "tea: 2 cups", "#8A5A12", "#FAEED8"), ("Age over 65", "more protein", "#0D7466", "#E6F2EF")])
    return f"""<div class="s rose" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#B0362B">One size does not fit all</div>
 <h1 style="font-size:88px;margin-top:14px">Have <em>diabetes</em> or<br>BP too? The advice<br>adjusts.</h1>
 <div style="display:flex;flex-direction:column;gap:16px;margin-top:50px">{chips}</div>
 <div style="font-size:30px;margin-top:34px;line-height:1.35">Special guidance for Crohn's disease with a narrowing (stricture), pancreatitis and cirrhosis.</div>
 {foot(5, N, pad=84)}</div>"""

def s6():
    art = winter("").replace('role="img" aria-label=""', 'aria-hidden="true"').replace('var(--accent-soft)', '#FAEED8')
    item = lambda ic, h, p: (f'<div style="display:flex;gap:22px;align-items:center;background:#fff;border-radius:26px;padding:22px 26px;box-shadow:0 8px 20px rgba(0,0,0,.06)">'
                             f'<div style="flex:none;width:76px;height:76px;border-radius:50%;background:#E6F2EF;display:grid;place-items:center;font-size:40px">{ic}</div>'
                             f'<div><div style="font-family:YS;font-size:36px;line-height:1.1">{h}</div><div style="font-size:26px;color:#4A615D;margin-top:4px;line-height:1.3">{p}</div></div></div>')
    return f"""<div class="s saffron" style="width:1080px;height:1350px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#B4531C">Also new</div>
 <h1 style="font-size:84px;margin-top:14px">More reasons<br>to <em style="color:#B4531C">visit</em></h1>
 <div style="position:absolute;right:40px;top:70px;width:330px">{art}</div>
 <div style="display:flex;flex-direction:column;gap:16px;margin-top:46px">
  {item("🍛", "Thali meter: 120+ foods", "Chai, lassi, puri, chicken, fish, momos and more")}
  {item("❄️", "Winter and wedding season guide", "Feasts without acidity, constipation or a liver scare")}
  {item("💬", "Book on WhatsApp in one tap", "Pick the reason and time; the message is ready")}
  {item("🖨️", "Print your diet chart", "Clean pages to stick on the fridge")}
  {item("📱", "Add to your home screen", "Opens like an app, in English or Hindi")}
 </div>
 {foot(6, N, pad=84)}</div>"""

def s7(li=False):
    return f"""<div class="s teal" style="width:1080px;height:1350px;padding:96px 84px;text-align:center">
 <div class="kick" style="font-size:26px;color:#F3B84A">Free · English and Hindi · No sign-in</div>
 <h1 style="font-size:100px;margin-top:20px">Find your<br>diet chart at</h1>
 <div style="display:inline-block;margin-top:44px;background:#F3B84A;color:#12302C;font-family:YS;font-size:58px;padding:24px 48px;border-radius:999px;white-space:nowrap">drlochab.com/diet-charts</div>
 <div style="font-size:34px;color:#CFE5E0;margin-top:30px">{"हिंदी में: drlochab.com/hi/diet-charts" if li else "Link in bio · हिंदी में भी उपलब्ध"}</div>
 <div style="display:flex;justify-content:center;gap:22px;margin-top:70px">{"".join(plate(i, 120) for i in (1, 3, 6, 9))}</div>
 <div style="font-size:30px;color:#CFE5E0;margin-top:56px;line-height:1.4">General guidance, not a personal prescription.<br>Your doctor's advice comes first.</div>
 {foot(7, N, light=True, pad=84)}</div>"""

# ---------- WhatsApp status, 1080x1920 ----------
def w1():
    return f"""<div class="s teal" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:32px;color:#F3B84A">New · Free</div>
 <h1 style="font-size:118px;margin-top:24px">“Doctor, what<br>should I <em>eat?</em>”</h1>
 <div style="font-size:44px;margin-top:30px;color:#CFE5E0;line-height:1.3">Indian diet charts for fatty liver, acidity, IBS, constipation, gallstones and 7 more.</div>
 <div style="position:absolute;left:50%;top:690px;transform:translateX(-50%)">{phone(chart_screen(1.28), 550, -3)}</div>
 {foot(None, light=True, pad=84, size=1.2)}</div>"""

def w2():
    return f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:32px;color:#0D7466">Free food diary</div>
 <h1 style="font-size:112px;margin-top:24px">See what your<br>day is <em>missing</em></h1>
 <div style="font-size:44px;margin-top:30px;color:#4A615D;line-height:1.3">Protein, fibre, vegetables, water, and what to eat next. Stays on your phone.</div>
 <div style="position:absolute;left:50%;top:690px;transform:translateX(-50%)">{phone(diary_screen(1.28), 550, 3)}</div>
 {foot(None, pad=84, size=1.2)}</div>"""

def w3():
    return f"""<div class="s teal" style="width:1080px;height:1920px;padding:220px 84px;text-align:center">
 <h1 style="font-size:120px">Find your<br><em>diet chart</em></h1>
 <div style="display:flex;justify-content:center;gap:24px;margin-top:90px">{"".join(plate(i, 150) for i in (1, 3, 6))}</div>
 <div style="display:inline-block;margin-top:100px;background:#F3B84A;color:#12302C;font-family:YS;font-size:60px;padding:26px 46px;border-radius:999px;white-space:nowrap">drlochab.com/diet-charts</div>
 <div style="font-size:46px;color:#CFE5E0;margin-top:44px">हिंदी में भी · Free · No sign-in</div>
 <div style="font-size:40px;color:#fff;margin-top:110px;line-height:1.4">Appointments: Arcura Clinic, Sector 51<br><span style="color:#CFE5E0">Mon–Fri 6–8 pm · Sun 9 am–1 pm</span></div>
 {foot(None, light=True, pad=84, size=1.2)}</div>"""

CAPTION = """"Doctor, what should I eat?" 🍽️

It's the question I hear most in clinic, so I've built the answer into my website: free Indian diet charts for 12 gut and liver conditions.

✅ Fatty liver, acidity & gastritis, IBS & bloating, constipation, gallstones, cirrhosis, jaundice, pancreatitis, ulcerative colitis & Crohn's disease, celiac (gluten-free), loose motions, and everyday gut health
🥗 A full sample day, morning to bedtime, with veg, egg and non-veg options and a few quick Western choices
⚖️ Advice that adjusts if you also have diabetes, high BP, kidney disease, pregnancy, or are over 65
📝 A free food diary: tap what you ate and see what your day is missing, foods to avoid, and what to eat for the rest of the day. It stays on your phone; nothing is uploaded.

Also new: the Thali meter now has 120+ everyday foods (chai, lassi, puri, chicken, fish…), a winter and wedding season guide, one-tap WhatsApp booking, printable charts, and you can add the site to your home screen.

Free, in English and Hindi. Link in bio 👉 drlochab.com/diet-charts

These charts are general guidance. If your doctor has given you a specific diet, follow that.

#DietChart #IndianDiet #FattyLiver #GutHealth #IBS #Acidity #Gastroenterologist #Gurugram #HealthyEating #DrLochab"""

WHATSAPP_EN = """🍽️ *"Doctor, what should I eat?"*

Free Indian diet charts for 12 gut and liver conditions are now on my website: fatty liver, acidity, IBS, constipation, gallstones, cirrhosis, jaundice, pancreatitis, ulcerative colitis & Crohn's disease, celiac, loose motions and everyday gut health.

• A full day's plan with veg, egg and non-veg options
• Advice for diabetes, BP, kidney disease, pregnancy and age over 65
• A free food diary that shows what your day is missing (stays on your phone)

👉 https://drlochab.com/diet-charts/
हिंदी में: https://drlochab.com/hi/diet-charts/

Please share with family and friends who ask what to eat.
– Dr. Kshitij Lochab, Gastroenterologist, Arcura Clinic, Sector 51, Gurugram"""

WHATSAPP_HI = """🍽️ *"डॉक्टर साहब, क्या खाएँ?"*

पेट और लिवर की 12 बीमारियों के लिए मुफ़्त भारतीय डाइट चार्ट अब मेरी वेबसाइट पर हैं: फैटी लिवर, एसिडिटी, IBS, कब्ज़, पथरी, सिरोसिस, पीलिया, पैंक्रियाटाइटिस, अल्सरेटिव कोलाइटिस और क्रोहन बीमारी, सीलिएक, दस्त, और रोज़ की पेट की सेहत।

• शाकाहारी, अंडा और मांसाहारी विकल्पों के साथ पूरे दिन का प्लान
• डायबिटीज़, BP, किडनी की बीमारी, प्रेगनेंसी और 65+ उम्र के लिए सलाह
• मुफ़्त फ़ूड डायरी, जो बताती है कि आज क्या कमी है (सिर्फ़ आपके फ़ोन पर रहती है)

👉 https://drlochab.com/hi/diet-charts/

जो भी पूछते हैं कि क्या खाएँ, उनके साथ ज़रूर शेयर करें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम"""

LINKEDIN = """"Doctor, what should I eat?" Turning the most common clinic question into a free resource

Almost every gastroenterology consultation ends with this question, and a few verbal points or a generic printout rarely answer it well for Indian patients. So I have added Indian diet charts for 12 conditions to drlochab.com, in English and Hindi:

Fatty liver, acidity and gastritis, IBS, constipation, gallstones, cirrhosis, acute hepatitis and jaundice, pancreatitis (after an attack and chronic), ulcerative colitis and Crohn's disease (flare, remission, and stricturing Crohn's), celiac disease, acute diarrhoea, and everyday gut health.

Each chart has:
• A full sample day using everyday Indian food, with veg, egg and non-veg options and a few Western choices
• Daily targets (for example, protein of 1.2 to 1.5 g/kg and a bedtime snack in cirrhosis, or a 2 g sodium limit with ascites)
• Caveats for common comorbidities: diabetes, hypertension and heart disease, CKD, pregnancy and older age
• Clear "when to see a doctor" advice

Patients can also use a food diary that compares their day with the chart, flags foods to avoid, and suggests what to eat at the next meal. Like the gut tracker, it is privacy-first: data stays only on the patient's phone and the page cannot send it anywhere.

Also added: a bigger Thali meter (120+ foods), a seasonal winter and wedding guide, one-tap WhatsApp booking, and printable charts.

Colleagues are welcome to share the charts with patients; they are free and need no sign-in. Feedback on the clinical content is very welcome.

drlochab.com/diet-charts

#Gastroenterology #Hepatology #ClinicalNutrition #PatientEducation #DigitalHealth #Gurugram"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([s1, s2, s3, s4, s5, s6, s7], 1):
            render(f, 1080, 1350, f"{OUT}/insta-{i}.png", b)
        render(lambda: s7(True), 1080, 1350, f"{OUT}/insta-7-linkedin.png", b)
        for i, f in enumerate([w1, w2, w3], 1):
            render(f, 1080, 1920, f"{OUT}/whatsapp-status-{i}.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
    pages = [Image.open(f"{OUT}/insta-{i}.png").convert("RGB") for i in range(1, 7)] + [Image.open(f"{OUT}/insta-7-linkedin.png").convert("RGB")]
    pages[0].save(f"{OUT}/linkedin-diet-charts.pdf", save_all=True, append_images=pages[1:], resolution=144, quality=95)
    open(f"{OUT}/instagram-caption.txt", "w").write(CAPTION + "\n")
    open(f"{OUT}/whatsapp-message-en.txt", "w").write(WHATSAPP_EN + "\n")
    open(f"{OUT}/whatsapp-message-hi.txt", "w").write(WHATSAPP_HI + "\n")
    open(f"{OUT}/linkedin-caption.txt", "w").write(LINKEDIN + "\n")
    print("done")
