"""Navratri 2026: a practical, gut-friendly fasting plan. Instagram carousel, 6 slides, 1080x1350, English.
Reuses the vrat thali drawing and brand CSS from week_2026_10_12.py.
Run from anywhere: python3 _src/social/navratri_carousel.py  -> _src/out/navratri-carousel/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS as BASE, foot, vrat_thali, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "navratri-carousel"); os.makedirs(OUT, exist_ok=True)
N = 6
CSS = BASE + """
.card{background:#FFFFFF;border-radius:32px;box-shadow:0 14px 36px rgba(11,42,38,.08)}
.row{display:grid;grid-template-columns:1fr 70px 1fr;align-items:center;gap:10px;padding:26px 30px}
.old{font-size:36px;color:#4A615D;text-decoration:line-through;text-decoration-color:#B0362B;text-decoration-thickness:3px}
.new{font-size:36px;font-weight:600;color:#12302C}
.t{display:grid;grid-template-columns:200px 1fr;gap:24px;align-items:center;padding:22px 30px;border-bottom:2px solid #F1E6D2}
.t:last-child{border-bottom:0}
.t b{font-weight:600;font-size:28px;color:#B5542C;letter-spacing:.06em;text-transform:uppercase}
.t span{font-size:34px;line-height:1.3}
.trap{display:flex;gap:28px;align-items:flex-start;padding:30px 34px}
.trap .x{flex:none;width:64px;height:64px;border-radius:50%;background:#B0362B;color:#fff;font-size:40px;font-weight:600;display:grid;place-items:center}
.trap h3{font-family:YS;font-weight:400;font-size:44px;line-height:1.15}
.trap p{font-size:31px;line-height:1.35;color:#4A615D;margin-top:8px}
.who{display:flex;gap:22px;align-items:flex-start;padding:24px 30px}
.who i{flex:none;width:20px;height:20px;border-radius:50%;background:#0D7466;margin-top:16px}
.who b{font-weight:600;font-size:36px}
.who p{font-size:30px;line-height:1.35;color:#4A615D;margin-top:4px}
"""
ARROW = '<svg viewBox="0 0 90 40" style="width:64px"><path d="M6 20 H74 M58 6 L78 20 L58 34" fill="none" stroke="#0D7466" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>'

S1 = f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:26px;color:#9FD8CC">Navratri 2026 · Save this</div>
 <h1 style="font-size:104px;margin-top:22px">Fasting<br>without the<br><em>acidity</em></h1>
 <p style="font-size:36px;margin-top:26px;color:#CFE5E0;max-width:400px">A practical, gut-friendly plan for your vrat days.</p>
 <div style="position:absolute;right:-70px;top:500px;width:680px;height:680px">{vrat_thali()}</div>
 {foot(1, N, light=True)}</div>"""

SWAPS = [("Sabudana vada", "Sabudana khichdi with peanuts"), ("Kuttu puri, pakoras", "Kuttu or singhara roti"),
         ("Fried aloo chips", "Roasted makhana"), ("Sweet lassi, fruit juice", "Chaach or whole fruit")]
S2 = f"""<div class="s cream" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#0D7466">Step 1</div>
 <h2 style="font-size:84px;margin-top:12px">Swap fried<br>for <em>roasted</em></h2>
 <div style="margin-top:56px;display:flex;flex-direction:column;gap:20px">
  {''.join(f'<div class="card row"><div class="old">{a}</div>{ARROW}<div class="new">{b}</div></div>' for a, b in SWAPS)}
 </div>
 <p style="margin-top:34px;font-size:32px;line-height:1.35;color:#4A615D">Same vrat foods, far less oil. Fried food sits longer in the stomach and triggers acidity.</p>
 {foot(2, N)}</div>"""

DAY = [("Morning", "Water first, then a few soaked almonds"), ("Breakfast", "A fruit with a bowl of curd"),
       ("Lunch", "Sabudana khichdi or samak rice with vegetables, and curd"), ("Evening", "Roasted makhana with chaach"),
       ("Dinner", "Kuttu roti with lauki or aloo-tamatar sabzi, by 8 pm")]
S3 = f"""<div class="s saffron" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#B5542C">Step 2</div>
 <h2 style="font-size:84px;margin-top:12px">Eat a little,<br>every <em>3–4 hours</em></h2>
 <div class="card" style="margin-top:50px">
  {''.join(f'<div class="t"><b>{k}</b><span>{v}</span></div>' for k, v in DAY)}
 </div>
 <p style="margin-top:30px;font-size:30px;color:#4A615D">Sip water, nimbu paani or coconut water between meals.</p>
 {foot(3, N)}</div>"""

TRAPS = [("Chai on an empty stomach", "Start with water and a few almonds or a fruit, then have your tea."),
         ("Long gaps of 6 hours or more", "An empty stomach still makes acid. Small meals keep it calm."),
         ("A heavy, late, fried dinner", "Eat light, by 8 pm, and wait 2 to 3 hours before lying down.")]
S4 = f"""<div class="s rose" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#B0362B">Step 3</div>
 <h2 style="font-size:84px;margin-top:12px">Avoid 3<br><em>acidity traps</em></h2>
 <div style="margin-top:50px;display:flex;flex-direction:column;gap:20px">
  {''.join(f'<div class="card trap"><div class="x">✕</div><div><h3>{h}</h3><p>{p}</p></div></div>' for h, p in TRAPS)}
 </div>
 {foot(4, N)}</div>"""

WHO = [("Diabetes", "Sugar can drop or rise. Check it more often, and ask your doctor about your medicines before fasting."),
       ("Pregnancy or breastfeeding", "Avoid long fasts. Eat every few hours and drink plenty of fluids."),
       ("Ulcer or severe acidity", "Long gaps can bring back pain. Choose a fruit-and-curd vrat over nirjala."),
       ("Older adults on many medicines", "Some tablets must be taken with food. Check timings with your doctor.")]
S5 = f"""<div class="s mint" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#0D7466">Before you fast</div>
 <h2 style="font-size:80px;margin-top:12px">Talk to your<br>doctor <em>first</em> if you have</h2>
 <div class="card" style="margin-top:44px;padding:10px 0">
  {''.join(f'<div class="who"><i></i><div><b>{h}</b><p>{p}</p></div></div>' for h, p in WHO)}
 </div>
 {foot(5, N)}</div>"""

STOP = ["Dizziness or fainting", "Shaking and sweating (low sugar)", "Vomiting that will not stop", "Black stools or vomiting blood", "Chest or upper belly pain"]
S6 = f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#9FD8CC">Know when to stop</div>
 <h2 style="font-size:84px;margin-top:12px">Break the fast and<br><em>see a doctor</em> if</h2>
 <div style="margin-top:48px;display:flex;flex-direction:column;gap:16px">
  {''.join(f'<div class="chip" style="background:rgba(255,255,255,.12);font-size:38px;padding:22px 32px"><span style="width:18px;height:18px;border-radius:50%;background:#F3B84A;flex:none"></span>{t}</div>' for t in STOP)}
 </div>
 <p style="margin-top:36px;font-size:32px;line-height:1.35;color:#CFE5E0">In an emergency, call 112 or go to the nearest emergency department.</p>
 <p style="margin-top:14px;font-size:30px;color:#FFFFFF"><b style="font-weight:600;color:#F3B84A">Tip:</b> buy kuttu atta fresh, from a trusted shop.</p>
 {foot(6, N, light=True)}</div>"""

SLIDES = [S1, S2, S3, S4, S5, S6]

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for i, s in enumerate(SLIDES, 1):
            pg = b.new_page(viewport={"width": 1080, "height": 1350})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{s}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/ig-navratri-plan-slide-{i}.png"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
