"""Promotes the new Myth Buster and Thali meter on drlochab.com (live 17 Oct 2026).
Instagram story (EN, 1080x1920), WhatsApp Status (HI and EN, 1080x1920), Google Business Profile post image (EN, 1200x900).
Run: python3 _src/social/site_games_promo.py  -> _src/out/site-games-promo/"""
import math, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "site-games-promo"); os.makedirs(OUT, exist_ok=True)

# Reuse the steel thali drawing from thali.py without running that script.
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "thali.py")).read()
exec(_src[_src.index("def thali("):_src.index("ICON = {")])

def gauge(angle, zones=("#E9A090", "#F3C66B", "#2E9C86")):
    cx, cy, r = 60, 60, 44
    P = lambda a: (cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a)))
    segs = [(180, 120), (120, 60), (60, 0)]
    arcs = "".join(f'<path d="M{P(a)[0]:.1f} {P(a)[1]:.1f} A{r} {r} 0 0 1 {P(b)[0]:.1f} {P(b)[1]:.1f}" fill="none" stroke="{c}" stroke-width="14"{' stroke-linecap="round"' if i != 1 else ""}/>'
                   for i, ((a, b), c) in enumerate(zip(segs, zones)))
    return (f'<svg viewBox="0 0 120 72" style="width:100%;display:block">{arcs}<g transform="rotate({angle} 60 60)"><line x1="60" y1="60" x2="60" y2="24" stroke="#12302C" stroke-width="6" stroke-linecap="round"/></g>'
            f'<circle cx="60" cy="60" r="9" fill="#12302C"/><circle cx="60" cy="60" r="3.5" fill="#F3C66B"/></svg>')

X = '<svg viewBox="0 0 24 24" style="width:1em;height:1em"><path d="M6 6 L18 18 M18 6 L6 18" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/></svg>'
OK = '<svg viewBox="0 0 24 24" style="width:1em;height:1em"><path d="M4 12.5 L10 18 L20 6" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

T = {
 "en": dict(kick="New on drlochab.com", h1="Play, learn<br>and <em>eat better</em>", myth="Myth or fact?", claim="“Cold milk cures acidity.”",
            m="Myth", f="Fact", guess="Guess, then see the answer", thali="Thali meter", g=("Fibre", "Protein", "Fat"), tq="Tap what you ate. See your balance.",
            cta="Try both free on drlochab.com", hi=False),
 "hi": dict(kick="drlochab.com पर नया", h1="खेलें, सीखें<br>और <em>सही खाएँ</em>", myth="भ्रम या सच?", claim="“ठंडा दूध एसिडिटी ठीक करता है।”",
            m="भ्रम", f="सच", guess="अंदाज़ा लगाइए, फिर जवाब देखिए", thali="थाली मीटर", g=("फ़ाइबर", "प्रोटीन", "फ़ैट"), tq="जो खाया उस पर टैप करें, संतुलन देखें",
            cta="drlochab.com/hi पर मुफ़्त आज़माएँ", hi=True),
}

def myth_card(t, scale=1.0):
    s = lambda v: int(v * scale)
    return f"""<div style="background:#12302C;color:#fff;border-radius:{s(44)}px;padding:{s(44)}px {s(48)}px {s(40)}px;transform:rotate(-2deg);box-shadow:0 {s(24)}px {s(50)}px rgba(0,0,0,.28);position:relative">
  <span style="display:inline-block;background:#B0362B;color:#fff;font-weight:600;letter-spacing:{'.02em' if t['hi'] else '.14em'};text-transform:uppercase;font-size:{s(30 if t['hi'] else 26)}px;padding:{s(8)}px {s(18)}px;border-radius:{s(12)}px;transform:rotate(-3deg)">{t['myth']}</span>
  <div class="q" style="font-size:{s(64 if t['hi'] else 70)}px;line-height:1.15;margin:{s(22)}px 0 {s(28)}px">{t['claim']}</div>
  <div style="display:flex;gap:{s(18)}px">
   <span style="flex:1;display:flex;align-items:center;justify-content:center;gap:{s(12)}px;border:{s(4)}px solid #fff;border-radius:999px;font-weight:600;font-size:{s(40)}px;padding:{s(16)}px 0">{X}{t['m']}</span>
   <span style="flex:1;display:flex;align-items:center;justify-content:center;gap:{s(12)}px;border:{s(4)}px solid #fff;border-radius:999px;font-weight:600;font-size:{s(40)}px;padding:{s(16)}px 0">{OK}{t['f']}</span>
  </div>
  <div style="position:absolute;right:{s(-26)}px;top:{s(-34)}px;width:{s(104)}px;height:{s(104)}px;border-radius:50%;background:#F3B84A;color:#12302C;display:grid;place-items:center;font-family:YS;font-size:{s(72)}px;transform:rotate(10deg)">?</div>
 </div>"""

def thali_card(t, scale=1.0, plate=360):
    s = lambda v: int(v * scale)
    gs = "".join(f'<div style="text-align:center"><div style="width:{s(200)}px">{gauge(a)}</div><div style="font-weight:600;font-size:{s(32)}px;margin-top:{s(4)}px">{n}</div></div>'
                 for n, a in zip(t["g"], (-30, 18, -55)))
    return f"""<div style="background:#FBF5EA;color:#12302C;border-radius:{s(44)}px;padding:{s(36)}px {s(36)}px {s(34)}px;transform:rotate(1.5deg);box-shadow:0 {s(24)}px {s(50)}px rgba(0,0,0,.25);display:flex;flex-direction:column;align-items:center">
  <span style="align-self:flex-start;display:inline-block;background:#0B6A5E;color:#fff;font-weight:600;letter-spacing:{'.02em' if t['hi'] else '.14em'};text-transform:uppercase;font-size:{s(30 if t['hi'] else 26)}px;padding:{s(8)}px {s(18)}px;border-radius:{s(12)}px;transform:rotate(-3deg)">{t['thali']}</span>
  <div style="width:{s(plate)}px;height:{s(plate)}px;margin-top:{s(-10)}px">{thali()}</div>
  <div style="display:flex;gap:{s(30)}px;margin-top:{s(-6)}px">{gs}</div>
 </div>"""

def story(lang):
    t = T[lang]
    return f"""<div class="s teal{' hi' if t['hi'] else ''}" style="width:1080px;height:1920px;padding:130px 90px">
 <div class="kick" style="font-size:{34 if t['hi'] else 30}px;color:#F3B84A;text-align:center">{t['kick']}</div>
 <h1 style="font-size:{104 if t['hi'] else 110}px;text-align:center;margin-top:18px">{t['h1']}</h1>
 <div style="position:absolute;left:110px;right:110px;top:{540 if t['hi'] else 520}px">{myth_card(t)}</div>
 <div style="position:absolute;left:150px;right:150px;top:{1068 if t['hi'] else 1010}px">{thali_card(t, 0.85 if t['hi'] else 0.98)}</div>
 <div style="position:absolute;left:0;right:0;top:{1660 if t['hi'] else 1640}px;text-align:center">
  <span style="display:inline-block;background:#F3B84A;color:#12302C;font-weight:600;font-size:{40 if t['hi'] else 38}px;padding:22px 44px;border-radius:999px">{t['cta']}</span>
 </div>
 {foot(light=True, pad=90, size=1.15, hi=t['hi'])}</div>"""

def gbp():
    t = T["en"]
    return f"""<div class="s teal" style="width:1200px;height:900px;padding:70px 70px">
 <div class="kick" style="font-size:24px;color:#F3B84A">New on drlochab.com</div>
 <h1 style="font-size:74px;margin-top:14px;width:520px">Play, learn<br>and <em>eat better</em></h1>
 <div style="position:absolute;left:70px;top:350px;width:500px;display:flex;flex-direction:column;gap:18px">
  <div style="background:rgba(255,255,255,.12);border-radius:24px;padding:18px 24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><span style="background:#B0362B;border-radius:10px;padding:5px 12px;font-size:20px;font-weight:600;letter-spacing:.12em">MYTH OR FACT?</span><span style="font-size:30px;font-weight:600">Guess, then see the answer</span></div>
  <div style="background:rgba(255,255,255,.12);border-radius:24px;padding:18px 24px;display:flex;flex-direction:column;gap:8px;align-items:flex-start"><span style="background:#F3B84A;color:#12302C;border-radius:10px;padding:5px 12px;font-size:20px;font-weight:600;letter-spacing:.12em">THALI METER</span><span style="font-size:30px;font-weight:600">Fibre, protein and fat in your day</span></div>
 </div>
 <div style="position:absolute;left:70px;top:672px;font-size:30px;font-weight:600;color:#F3B84A">Free on drlochab.com</div>
 <div style="position:absolute;right:60px;top:70px;width:520px">{thali_card(t, 0.8, 380)}</div>
 {foot(light=True, pad=70, size=1.0)}</div>"""

if __name__ == "__main__":
    css = CSS + '.q{font-family:"YS",serif} .hi .q{font-family:"TD","YS",serif;line-height:1.3!important}'
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html, w, h, name):
            pg = b.new_page(viewport={"width": w, "height": h})
            path = f"{OUT}/tmp.html"
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{css}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{path}"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/{name}"); pg.close()
        shot(story("en"), 1080, 1920, "instagram-story.png")
        shot(story("hi"), 1080, 1920, "whatsapp-status-hi.png")
        shot(story("en"), 1080, 1920, "whatsapp-status-en.png")
        shot(gbp(), 1200, 900, "google-post.png")
        b.close()
    os.remove(f"{OUT}/tmp.html"); print("done")
