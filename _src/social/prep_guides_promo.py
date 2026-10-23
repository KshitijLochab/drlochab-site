"""Promo for the colonoscopy and endoscopy preparation guides with planner (23 Oct 2026).
Instagram carousel (4 slides, 1080x1350), Instagram story (1080x1920), WhatsApp status EN + HI (1080x1920),
Google Business Profile image (1200x900), plus captions and post text.
Facts follow prep_guides.py exactly. No brand names, no doses, no phone number in the Google post text.
Run: python3 _src/social/prep_guides_promo.py  -> _src/out/prep-guides-promo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS, foot, SRC
from new_tools_promo import phone
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "prep-guides-promo"); os.makedirs(OUT, exist_ok=True)
N = 4
URL_C, URL_E = "drlochab.com/guides/colonoscopy-preparation", "drlochab.com/guides/endoscopy-preparation"

# ---------- original drawings ----------
def clock(s=64, col="#0D7466"):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><circle cx="32" cy="32" r="28" fill="#fff" stroke="{col}" stroke-width="5"/>'
            f'<path d="M32 16 V32 L43 39" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def glass(s=64):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><path d="M14 8 H50 L45 56 Q44 60 40 60 H24 Q20 60 19 56 Z" fill="#fff" stroke="#0D7466" stroke-width="4" stroke-linejoin="round"/>'
            '<path d="M17 26 H47 L44 55 Q43.5 57 41 57 H23 Q20.5 57 20 55 Z" fill="#CDEBF4"/><circle cx="30" cy="40" r="2.5" fill="#fff"/><circle cx="36" cy="47" r="2" fill="#fff"/></svg>')

def bowl(s=64):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><path d="M6 30 H58 C58 46 46 56 32 56 C18 56 6 46 6 30 Z" fill="#fff" stroke="#0D7466" stroke-width="4"/>'
            '<path d="M10 30 C12 18 52 18 54 30 Z" fill="#F6EBD2"/>' + "".join(f'<ellipse cx="{x}" cy="{y}" rx="3.4" ry="1.8" fill="#E3D2AE"/>' for x, y in [(20, 25), (28, 22), (36, 23), (44, 26), (32, 27), (24, 28)]) + "</svg>")

def bottle(s=64):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><rect x="24" y="4" width="16" height="9" rx="3" fill="#0D7466"/>'
            '<path d="M22 13 H42 V20 Q50 24 50 32 V56 Q50 60 46 60 H18 Q14 60 14 56 V32 Q14 24 22 20 Z" fill="#fff" stroke="#0D7466" stroke-width="4" stroke-linejoin="round"/>'
            '<path d="M17 36 H47 V55 Q47 57 45 57 H19 Q17 57 17 55 Z" fill="#F3D27A"/><path d="M32 22 V31" stroke="#0D7466" stroke-width="3" stroke-linecap="round"/></svg>')

def nodrink(s=64):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><circle cx="32" cy="32" r="28" fill="#fff" stroke="#B0362B" stroke-width="5"/>'
            '<path d="M22 16 H42 L39 48 H25 Z" fill="#CDEBF4" stroke="#12302C" stroke-width="3" stroke-linejoin="round"/><path d="M14 50 L50 14" stroke="#B0362B" stroke-width="5" stroke-linecap="round"/></svg>')

def pill(s=64):
    return (f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><g transform="rotate(-35 32 32)"><rect x="10" y="22" width="44" height="20" rx="10" fill="#fff" stroke="#0D7466" stroke-width="4"/>'
            '<path d="M32 22 V42" stroke="#0D7466" stroke-width="4"/><path d="M32 24 H44 A8 8 0 0 1 44 40 H32 Z" fill="#F3B84A"/></g></svg>')

def calendar(s=200):
    return (f'<svg viewBox="0 0 200 200" style="width:{s}px;height:{s}px"><rect x="18" y="34" width="150" height="140" rx="22" fill="#fff"/>'
            '<path d="M18 56 Q18 34 40 34 H146 Q168 34 168 56 V74 H18 Z" fill="#F3B84A"/><rect x="50" y="20" width="12" height="32" rx="6" fill="#12302C"/><rect x="124" y="20" width="12" height="32" rx="6" fill="#12302C"/>'
            + "".join(f'<rect x="{38 + c*36}" y="{90 + r*28}" width="22" height="16" rx="5" fill="{"#0D7466" if (r, c) == (1, 2) else "#D7E7E3"}"/>' for r in range(3) for c in range(4))
            + '<g transform="translate(132 120)"><circle r="40" fill="#12302C"/><path d="M-14 12 H14 L10 6 V-4 A10 10 0 0 0 -10 -4 V6 Z" fill="#F3B84A"/><circle cy="18" r="5" fill="#F3B84A"/>'
            '<path d="M-24 -18 Q-30 -6 -26 6 M24 -18 Q30 -6 26 6" fill="none" stroke="#F3B84A" stroke-width="4" stroke-linecap="round"/></g></svg>')

def swatch(c, lbl, sub):
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1"><div style="width:96px;height:52px;border-radius:26px;background:{c};border:3px solid rgba(0,0,0,.12)"></div>'
            f'<b style="font-size:24px">{lbl}</b><span style="font-size:20px;color:#4A615D">{sub}</span></div>')

# the planner, as the patient sees it on the phone (sample test time 10:00 am)
PLAN = [("2 days before", "Start low-fibre food"), ("Day before · 12 noon", "Clear liquids only"), ("Day before · 7 pm", "Bowel prep, first half"),
        ("Test day · 5 am", "Bowel prep, second half"), ("Test day · 8 am", "Stop all drinks"), ("Test day · 10 am", "Colonoscopy")]

def plan_screen(fs=1.0):
    rows = "".join(f'<div style="display:flex;gap:{int(12*fs)}px;align-items:flex-start;padding:{int(9*fs)}px 0;border-left:3px solid #CFE0DC;margin-left:{int(9*fs)}px;padding-left:{int(16*fs)}px;position:relative">'
                   f'<span style="position:absolute;left:-{int(11*fs)}px;top:{int(12*fs)}px;width:{int(18*fs)}px;height:{int(18*fs)}px;border-radius:50%;background:{"#0D7466" if i == len(PLAN)-1 else "#fff"};border:3px solid #0D7466"></span>'
                   f'<div><div style="font-size:{int(15*fs)}px;font-weight:600;color:#0D7466">{t}</div><div style="font-size:{int(19*fs)}px;color:#12302C;line-height:1.25">{w}</div></div></div>'
                   for i, (t, w) in enumerate(PLAN))
    return (f'<div style="font-size:{int(14*fs)}px;font-weight:600;letter-spacing:.12em;color:#4A615D">YOUR PLAN</div>'
            f'<div style="font-family:YS;font-size:{int(26*fs)}px;color:#12302C;margin:{int(4*fs)}px 0 {int(10*fs)}px;white-space:nowrap">Colonoscopy · 10 am</div>{rows}'
            f'<div style="margin-top:{int(14*fs)}px;background:#0D7466;color:#fff;border-radius:999px;padding:{int(10*fs)}px;text-align:center;font-size:{int(16*fs)}px;font-weight:600">Save reminders to my calendar</div>')

# ---------- Instagram carousel ----------
def cover(h=1350, n=1, story=False):
    top = 170 if story else 96
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:{top}px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">New · free · English & हिंदी</div>
 <h1 style="font-size:{98 if story else 88}px;margin-top:22px">Colonoscopy or endoscopy <em>coming up?</em></h1>
 <p style="font-size:{38 if story else 34}px;line-height:1.35;color:#DCEFEA;margin-top:24px;max-width:{900 if story else 560}px">Enter your test date and time. Get your own plan, step by step, with the exact day and hour for each step.</p>
 <div style="position:absolute;right:{70 if not story else 120}px;top:{430 if not story else 760}px">{phone(plan_screen(1.0 if not story else 1.18), w=380 if not story else 450, tilt=5)}</div>
 <div style="position:absolute;left:84px;top:{700 if not story else 1250}px;display:grid;gap:16px">{"".join(f'<div style="display:flex;align-items:center;gap:14px;font-size:{30 if story else 28}px"><span style="width:14px;height:14px;border-radius:50%;background:#F3B84A"></span>{t}</div>' for t in ("A dated, timed plan", "Calendar reminders", "Send it on WhatsApp", "Print or save as PDF"))}</div>
 <div style="position:absolute;left:{470 if not story else 470}px;top:{980 if not story else 1560}px">{calendar(200 if not story else 220)}</div>
 {foot(None if story else n, total=N, light=True, pad=84)}</div>"""

def colo(h=1350, n=2):
    steps = [(clock, "7 days before", "Stop iron tablets. Ask your doctor about blood thinners, diabetes medicines and insulin."),
             (bowl, "2 days before", "Low-fibre food: rice, khichdi, idli, curd. No seeds, salads or whole grains."),
             (glass, "Day before, from 12 noon", "Clear liquids only: water, ORS, clear soup, tea without milk."),
             (bottle, "Evening before + morning of the test", "Bowel prep in two halves. The second starts about 5 hours before."),
             (nodrink, "2 hours before", "Stop all drinks, including water. Come with an adult.")]
    rows = "".join(f'<div style="display:flex;gap:22px;align-items:center;background:#fff;border-radius:24px;padding:18px 22px">{f(70)}'
                   f'<div><div style="font-size:24px;font-weight:600;color:#0D7466">{t}</div><div style="font-size:27px;line-height:1.3">{d}</div></div></div>' for f, t, d in steps)
    return f"""<div class="s cream" style="width:1080px;height:{h}px;padding:80px 84px">
 <div class="kick" style="font-size:24px;color:#0D7466">Colonoscopy</div>
 <h2 style="font-size:64px;margin:10px 0 28px">A clean bowel means <em>nothing is missed</em></h2>
 <div style="display:grid;gap:14px">{rows}</div>
 <div style="font-size:24px;font-weight:600;color:#4A615D;margin-top:22px">By the end of the prep, stool should be:</div>
 <div style="display:flex;gap:10px;margin-top:12px;align-items:flex-start">{swatch("#7B4A24", "Not ready", "brown")}{swatch("#C9922E", "Almost", "dark yellow")}{swatch("#F2DD7A", "Ready", "clear yellow")}</div>
 {foot(n, total=N, pad=84)}</div>"""

def endo(h=1350, n=3):
    box = lambda f, big, t, d, bg: (f'<div style="background:{bg};border-radius:28px;padding:26px 28px;display:flex;gap:24px;align-items:center">{f(96)}'
                                    f'<div><div style="font-family:YS;font-size:{big[1]}px;line-height:1">{big[0]}</div><div style="font-size:26px;font-weight:600;color:#0D7466;margin-top:6px">{t}</div>'
                                    f'<div style="font-size:26px;line-height:1.3;margin-top:4px">{d}</div></div></div>')
    return f"""<div class="s mint" style="width:1080px;height:{h}px;padding:80px 84px">
 <div class="kick" style="font-size:24px;color:#0D7466">Upper GI endoscopy</div>
 <h2 style="font-size:66px;margin:10px 0 32px">Mostly, just an <em>empty stomach</em></h2>
 <div style="display:grid;gap:18px">
  {box(bowl, ("6 hours", 72), "before the test", "Nothing to eat. Have a light dinner by about 10 pm for a morning test.", "#fff")}
  {box(glass, ("2 hours", 72), "before the test", "Last small sips of plain water. Then nothing at all.", "#fff")}
  {box(pill, ("Tablets", 60), "BP and thyroid", "Usually taken as normal, with a small sip of water. Ask about diabetes medicines and blood thinners.", "#fff")}
 </div>
 <p style="font-size:26px;line-height:1.35;margin-top:24px;color:#4A615D">Having sedation? Bring an adult to take you home. Do not stop any medicine on your own.</p>
 {foot(n, total=N, pad=84)}</div>"""

def cta(h=1350, n=4):
    step = lambda i, t: (f'<div style="display:flex;gap:22px;align-items:center"><span style="flex:none;width:64px;height:64px;border-radius:50%;background:#F3B84A;color:#12302C;'
                         f'font-family:YS;font-size:34px;display:grid;place-items:center">{i}</span><span style="font-size:34px;line-height:1.3">{t}</span></div>')
    return f"""<div class="s teal" style="width:1080px;height:{h}px;padding:96px 84px">
 <div class="kick" style="font-size:26px;color:#F3B84A">Your plan in 3 steps</div>
 <h2 style="font-size:72px;margin:16px 0 40px">Free on <em>drlochab.com</em></h2>
 <div style="display:grid;gap:26px">{step(1, "Open the colonoscopy or endoscopy guide")}{step(2, "Enter the date and time of your test")}{step(3, "Save reminders to your calendar or send the plan on WhatsApp")}</div>
 <div style="display:grid;gap:14px;margin-top:46px;justify-items:start">
  <span style="background:rgba(255,255,255,.12);border-radius:999px;padding:12px 22px;font-size:26px">English & हिंदी</span>
  <span style="background:rgba(255,255,255,.12);border-radius:999px;padding:12px 22px;font-size:26px">Nothing is stored or sent</span>
  <span style="background:rgba(255,255,255,.12);border-radius:999px;padding:12px 22px;font-size:26px">Printable</span></div>
 <div style="display:inline-block;margin-top:40px;background:#F3B84A;color:#12302C;font-family:YS;font-size:60px;padding:16px 42px;border-radius:999px">drlochab.com</div>
 <p style="font-size:24px;color:#CFE5E0;margin-top:22px;max-width:520px">If your hospital gives you a different instruction sheet, follow theirs.</p>
 <div style="position:absolute;right:76px;top:560px">{phone(plan_screen(0.88), w=320, tilt=5)}</div>
 {foot(n, total=N, light=True, pad=84)}</div>"""

# ---------- WhatsApp status ----------
def status(hi=False):
    if hi:
        k, h1, c_h, c, e_h, e, u, note = ("नया · मुफ़्त", "कोलोनोस्कोपी या एंडोस्कोपी होने वाली है?", "कोलोनोस्कोपी",
            ["2 दिन पहले: कम फ़ाइबर वाला खाना", "एक दिन पहले दोपहर 12 बजे से: सिर्फ़ साफ़ तरल", "आँत की दवा दो हिस्सों में: रात को और जाँच से 5 घंटे पहले", "2 घंटे पहले: सब कुछ पीना बंद"],
            "एंडोस्कोपी", ["6 घंटे पहले से कुछ न खाएँ", "2 घंटे पहले तक पानी के छोटे घूँट"],
            "drlochab.com/hi", "अपनी तारीख़ और समय डालें, पूरा प्लान पाएँ")
    else:
        k, h1, c_h, c, e_h, e, u, note = ("New · free", "Colonoscopy or endoscopy coming up?", "Colonoscopy",
            ["2 days before: low-fibre food", "Day before, from 12 noon: clear liquids only", "Bowel prep in two halves: evening and 5 hours before", "2 hours before: stop all drinks"],
            "Endoscopy", ["Nothing to eat for 6 hours before", "Small sips of water until 2 hours before"],
            "drlochab.com", "Enter your test date and time for your own plan")
    li = lambda items: "".join(f'<div style="display:flex;gap:16px;align-items:flex-start;font-size:36px;line-height:1.3;margin-top:14px"><span style="flex:none;width:16px;height:16px;border-radius:50%;background:#F3B84A;margin-top:16px"></span>{x}</div>' for x in items)
    return f"""<div class="s teal{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:30px;color:#F3B84A">{k}</div>
 <h1 style="font-size:{86 if hi else 96}px;margin-top:20px">{h1}</h1>
 <div style="display:flex;gap:26px;align-items:center;margin-top:50px"><span style="background:#fff;border-radius:50%;padding:14px;display:grid">{bottle(80)}</span><h2 style="font-size:58px">{c_h}</h2></div>{li(c)}
 <div style="display:flex;gap:26px;align-items:center;margin-top:54px"><span style="background:#fff;border-radius:50%;padding:14px;display:grid">{glass(80)}</span><h2 style="font-size:58px">{e_h}</h2></div>{li(e)}
 <div style="display:flex;align-items:center;gap:30px;margin-top:70px">{calendar(210)}<div style="font-size:38px;line-height:1.35;color:#DCEFEA">{note}</div></div>
 <div style="position:absolute;left:84px;right:84px;bottom:230px;text-align:center">
  <div style="display:inline-block;background:#F3B84A;color:#12302C;font-family:YS;font-size:76px;padding:18px 52px;border-radius:999px">{u}</div></div>
 {foot(None, light=True, pad=84, hi=hi)}</div>"""

# ---------- Google Business Profile image ----------
def gbp():
    return f"""<div class="s teal" style="width:1200px;height:900px;padding:80px 80px">
 <div class="kick" style="font-size:26px;color:#F3B84A">Free on drlochab.com</div>
 <h1 style="font-size:78px;margin-top:20px;max-width:640px">Getting ready for a <em>colonoscopy or endoscopy?</em></h1>
 <p style="font-size:32px;line-height:1.35;color:#DCEFEA;margin-top:24px;max-width:600px">A step-by-step plan with your own dates and times, in English and Hindi.</p>
 <div style="position:absolute;right:90px;top:70px">{phone(plan_screen(1.0), w=380, tilt=4)}</div>
 {foot(None, light=True, pad=80)}</div>"""

# ---------- text ----------
CAPTION = """Colonoscopy or endoscopy coming up? Here's your plan 🗓️

A colonoscopy is only as good as the bowel preparation. When the bowel is clean, even small polyps can be seen and removed. When it isn't, the test may have to be repeated.

Colonoscopy, in short:
🥣 2 days before: low-fibre food (rice, khichdi, idli, curd; no seeds, salads or whole grains)
💧 Day before, from 12 noon: clear liquids only (water, ORS, clear soup, tea without milk)
🧴 Bowel prep in two halves: the evening before, and again starting about 5 hours before the test
🚫 2 hours before: stop all drinks, and come with an adult

Upper GI endoscopy, in short:
🍽️ Nothing to eat for at least 6 hours before
💧 Small sips of plain water until 2 hours before
💊 BP and thyroid tablets usually as normal with a sip of water; ask your doctor about diabetes medicines and blood thinners

✨ New on my website: enter the date and time of your test and get your own plan with the exact day and hour for each step. Save reminders to your phone calendar, or send the plan on WhatsApp. In English and Hindi, and nothing you type is stored.

Do not stop any medicine on your own. If your hospital gives you a different instruction sheet, follow theirs.

Save this post for later, and share it with someone who has a test coming up 👇
Link in bio 👉 drlochab.com

#Colonoscopy #Endoscopy #BowelPrep #GutHealth #DigestiveHealth #Gastroenterologist #Gurugram #DrLochab"""

STORY_NOTE = """Instagram story tips:
• Add a Link sticker to https://drlochab.com/guides/colonoscopy-preparation/ in the empty space under the headline (left of the phone).
• Optional question sticker: "Got a test coming up? Ask me anything about the preparation."
• Optional: add the Book link (https://wa.me/919667104882) as a second link sticker."""

GBP_TEXT = """Getting ready for a colonoscopy or endoscopy?

A clean bowel lets even small polyps be seen during a colonoscopy, and an empty stomach keeps an endoscopy clear and safe. Our free preparation guides turn the instructions into a simple plan:

Colonoscopy: low-fibre food for 2 days, clear liquids from noon the day before, the bowel preparation in two halves, and no drinks in the last 2 hours.
Endoscopy: nothing to eat for 6 hours, small sips of water until 2 hours before.

Enter the date and time of your test to see the exact day and hour for each step, and save reminders to your calendar. Available in English and Hindi. Please do not stop any medicine on your own; ask your doctor about blood thinners and diabetes medicines.

Button: Learn more → https://drlochab.com/guides/colonoscopy-preparation/"""

WHATSAPP_EN = """🗓️ *Colonoscopy or endoscopy coming up?*

My website now has free preparation guides. Enter the date and time of your test and get your own plan, with the exact day and hour for each step, and calendar reminders.

🥣 Colonoscopy: https://drlochab.com/guides/colonoscopy-preparation/
🍽️ Endoscopy: https://drlochab.com/guides/endoscopy-preparation/
हिंदी में: https://drlochab.com/hi/guides/colonoscopy-preparation/

Please share with anyone who has a test coming up.
– Dr. Kshitij Lochab, Gastroenterologist, Arcura Clinic, Sector 51, Gurugram"""

WHATSAPP_HI = """🗓️ *कोलोनोस्कोपी या एंडोस्कोपी होने वाली है?*

मेरी वेबसाइट पर अब तैयारी की मुफ़्त गाइड हैं। अपनी जाँच की तारीख़ और समय डालें, और हर क़दम के दिन और समय के साथ अपना प्लान पाएँ, कैलेंडर रिमाइंडर के साथ।

🥣 कोलोनोस्कोपी: https://drlochab.com/hi/guides/colonoscopy-preparation/
🍽️ एंडोस्कोपी: https://drlochab.com/hi/guides/endoscopy-preparation/

जिनकी जाँच होने वाली है, उनके साथ ज़रूर शेयर करें।
– डॉ. क्षितिज लोचब, गैस्ट्रोएंटेरोलॉजिस्ट, आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(500); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, f in enumerate([cover, colo, endo, cta], 1):
            render(lambda: f(n=i), 1080, 1350, f"{OUT}/insta-post-{i}.png", b)
        render(lambda: cover(h=1920, story=True), 1080, 1920, f"{OUT}/insta-story.png", b)
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
    print("done", sorted(os.listdir(OUT)))
