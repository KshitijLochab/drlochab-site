"""Introduces the three special guides on drlochab.com (pregnancy, children, after 60).
Instagram carousel (5 slides, 1080x1350) and one WhatsApp Status (1080x1920), using the site's own original illustrations.
Run from anywhere: python3 _src/social/guides_launch.py  -> _src/out/guides-launch/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS as BASE_CSS, foot, SRC
import guide_art
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "guides-launch"); os.makedirs(OUT, exist_ok=True)
CSS = BASE_CSS + """
:root{--accent-soft:#DDEEEA}
.art{background:#FFFFFF;border-radius:44px;box-shadow:0 18px 44px rgba(6,47,42,.16);overflow:hidden}
.art svg{display:block;width:100%;height:100%}
.pill{display:inline-flex;align-items:center;gap:14px;background:#FFFFFF;border-radius:999px;padding:16px 28px;font-size:34px;font-weight:600;color:#12302C}
.pill i{width:16px;height:16px;border-radius:50%;background:#0D7466;flex:none}
.url{display:inline-block;background:#F3B84A;color:#12302C;font-weight:600;border-radius:999px}
"""
art = lambda slug: guide_art.ART[slug]("")

G = [("pregnancy-digestive-health", "Pregnancy and your gut", "mint", ["Nausea and acidity", "Constipation and piles", "What to eat, and warning signs"], None),
     ("children-digestive-health", "Your child's tummy", "saffron", ["Loose motions and ORS", "Constipation and tummy pain", "Warning signs for parents"], "For parents. I see teenagers 12 and above."),
     ("digestive-health-after-60", "Gut health after 60", "cream", ["Constipation and medicines", "Symptoms not to ignore", "A simple diet plan"], None)]

def guide_slide(n, slug, title, bg, points, note):
    pills = "".join(f'<div class="pill"><i></i>{p}</div>' for p in points)
    extra = f'<p style="margin-top:6px;font-size:30px;color:#4A615D">{note}</p>' if note else ""
    return f"""<div class="s {bg}" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#0D7466">Guide {n - 1} of 3</div>
 <h2 style="font-size:80px;margin-top:14px;line-height:1.05">{title}</h2>
 <div class="art" style="position:absolute;left:207px;top:340px;width:666px;height:500px">{art(slug)}</div>
 <div style="position:absolute;left:72px;right:72px;top:880px;display:flex;flex-direction:column;align-items:flex-start;gap:14px">{pills}{extra}</div>
 {foot(n)}</div>"""

COVER = f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:26px;color:#9FD8CC">New on drlochab.com</div>
 <h1 style="font-size:104px;margin-top:22px">3 free guides<br>for <em>special times</em><br>of life</h1>
 <div style="position:absolute;left:72px;right:72px;top:640px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px">
  {''.join(f'<div class="art" style="height:330px">{art(s)}</div>' for s, *_ in G)}
 </div>
 <div style="position:absolute;left:72px;right:72px;top:1010px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;text-align:center;font-size:32px;font-weight:600;line-height:1.25">
  <div>Pregnancy</div><div>Children</div><div>After 60</div>
 </div>
 <p style="position:absolute;left:72px;right:72px;top:1105px;font-size:32px;color:#CFE5E0">In English and Hindi. Swipe to see what's inside.</p>
 {foot(1, light=True)}</div>"""

CTA = f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:24px;color:#9FD8CC">Read them free</div>
 <h2 style="font-size:84px;margin-top:16px">Simple advice,<br>in <em>English and Hindi</em></h2>
 <div style="position:absolute;left:72px;right:72px;top:400px;display:flex;flex-direction:column;gap:18px">
  {''.join(f'<div style="display:flex;align-items:center;gap:26px;background:rgba(255,255,255,.1);border-radius:32px;padding:16px 24px"><div class="art" style="width:176px;height:132px;border-radius:20px;flex:none">{art(s)}</div><div style="font-family:YS;font-size:44px;line-height:1.15">{t}</div></div>' for s, t, *_ in G)}
 </div>
 <div style="position:absolute;left:72px;right:72px;top:1000px">
  <div class="url" style="font-size:36px;padding:20px 36px">drlochab.com → Special guides</div>
  <p style="margin-top:20px;font-size:28px;color:#CFE5E0">Link in bio. Share with someone who is expecting, a parent, or your parents.</p>
 </div>
 {foot(5, light=True)}</div>"""

SLIDES = [COVER] + [guide_slide(i + 2, *g) for i, g in enumerate(G)] + [CTA]

STATUS = f"""<div class="s teal" style="width:1080px;height:1920px;padding:150px 80px">
 <div class="kick" style="font-size:30px;color:#9FD8CC;text-align:center">New on drlochab.com</div>
 <h1 style="font-size:100px;text-align:center;margin-top:22px">3 free <em>guides</em></h1>
 <p style="text-align:center;font-size:38px;color:#CFE5E0;margin-top:18px">for special times of life</p>
 <div style="position:absolute;left:80px;right:80px;top:540px;display:flex;flex-direction:column;gap:28px">
  {''.join(f'<div style="display:flex;align-items:center;gap:30px;background:rgba(255,255,255,.1);border-radius:36px;padding:22px 28px"><div class="art" style="width:280px;height:210px;border-radius:26px;flex:none">{art(s)}</div><div><div style="font-family:YS;font-size:50px;line-height:1.12">{t}</div><div style="font-size:30px;color:#CFE5E0;margin-top:10px">{p[0]}, {p[1].lower()}</div></div></div>' for s, t, _, p, _n in G)}
 </div>
 <div style="position:absolute;left:0;right:0;top:1500px;text-align:center">
  <div class="url" style="font-size:40px;padding:22px 40px">drlochab.com → Special guides</div>
  <p style="margin-top:22px;font-size:32px;color:#CFE5E0">In English and Hindi</p>
 </div>
 {foot(light=True, pad=80, size=1.15)}</div>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html, w, h, path):
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()
        for i, s in enumerate(SLIDES, 1):
            shot(s, 1080, 1350, f"{OUT}/ig-guides-slide-{i}.png")
        shot(STATUS, 1080, 1920, f"{OUT}/wa-status-guides.png")
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
