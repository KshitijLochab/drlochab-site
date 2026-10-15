"""Promotes the Navratri fasting guide on drlochab.com (live 15 Oct 2026).
Instagram story in English (1080x1920, space left for a link sticker) and WhatsApp Status in Hindi (1080x1920).
Run from anywhere: python3 _src/social/navratri_guide_promo.py  -> _src/out/navratri-guide-promo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, vrat_thali, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "navratri-guide-promo"); os.makedirs(OUT, exist_ok=True)
TICK = '<svg viewBox="0 0 40 40" style="width:44px;height:44px;flex:none"><circle cx="20" cy="20" r="20" fill="#0D7466"/><path d="M11 21 L17 27 L29 14" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def story(kick, title, items, url, foot_html, hi=False):
    rows = "".join(f'<div class="chip" style="background:#FFFFFF;color:#12302C;font-size:{40 if hi else 38}px;padding:18px 28px">{TICK}{t}</div>' for t in items)
    return f"""<div class="s saffron{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:140px 80px">
 <div class="kick" style="font-size:{34 if hi else 28}px;color:#B5542C;text-align:center">{kick}</div>
 <h1 style="font-size:{96 if hi else 92}px;text-align:center;margin-top:16px">{title}</h1>
 <div style="position:absolute;left:250px;top:{560 if hi else 540}px;width:580px;height:580px">{vrat_thali()}</div>
 <div style="position:absolute;left:110px;right:110px;top:1170px;display:flex;flex-direction:column;gap:16px">{rows}</div>
 <div style="position:absolute;left:0;right:0;top:1600px;text-align:center">
  <div style="display:inline-block;background:#0D7466;color:#fff;font-weight:600;font-size:34px;padding:20px 38px;border-radius:999px">{url}</div>
 </div>
 {foot_html}</div>"""

IG = story("New on drlochab.com", "Navratri fasting<br>guide", 
           ["Fast without acidity", "A simple vrat day plan", "Kuttu atta safety", "Who should ask a doctor first"],
           "Free guide on drlochab.com", foot(pad=80, size=1.15))
WA = story("नवरात्रि व्रत गाइड", "बिना एसिडिटी के<br><em>व्रत</em>",
           ["व्रत के दिन का आसान प्लान", "कुट्टू आटे की सुरक्षा", "किन्हें पहले डॉक्टर से पूछना है"],
           "drlochab.com/hi पर पढ़ें", foot(pad=80, size=1.15, hi=True), hi=True)

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for html, name in [(IG, "ig-story-navratri-guide-en.png"), (WA, "wa-status-navratri-guide-hi.png")]:
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/{name}"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
