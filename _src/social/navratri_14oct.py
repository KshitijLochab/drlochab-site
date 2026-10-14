"""Wed 14 Oct 2026 (Navratri day 4): fasting without acidity.
Instagram post in English (1080x1350), Google Business Profile image in Hindi (1200x900) and WhatsApp Status in Hindi (1080x1920).
Reuses the vrat thali drawing from week_2026_10_12.py.
Run from anywhere: python3 _src/social/navratri_14oct.py  -> _src/out/navratri-14oct/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, vrat_thali, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "navratri-14oct"); os.makedirs(OUT, exist_ok=True)

EN = ["Roast, don't fry", "Eat a little every 3–4 hours", "Water, chaach, coconut water"]
HI = ["तला कम, भुना ज़्यादा", "हर 3–4 घंटे में थोड़ा खाएँ", "पानी, छाछ, नारियल पानी"]

def chips(items, size, gap, pad="14px 32px"):
    return "".join(f'<div class="chip" style="background:#FFFFFF;color:#12302C;font-size:{size}px;margin-bottom:{gap}px;padding:{pad}">'
                   f'<span style="font-family:YS;color:#0D7466;font-size:{size+6}px;min-width:36px">{n}</span>{t}</div>' for n, t in enumerate(items, 1))

IG_EN = f"""<div class="s saffron" style="width:1080px;height:1350px;padding:76px 72px">
 <div class="kick" style="font-size:26px;color:#B5542C;text-align:center">Navratri fasting</div>
 <h1 style="font-size:84px;margin-top:12px;text-align:center">Fast, but keep your<br>stomach <em>light</em></h1>
 <div style="position:absolute;left:310px;top:290px;width:460px;height:460px">{vrat_thali()}</div>
 <div style="position:absolute;left:150px;right:150px;top:790px">{chips(EN, 38, 14)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1100px;font-size:30px;line-height:1.35;color:#4A615D;text-align:center">Diabetes, pregnancy or a stomach problem? <b style="font-weight:600;color:#12302C">Ask your doctor before fasting.</b></p>
 {foot()}</div>"""

GBP_HI = f"""<div class="s saffron hi" style="width:1200px;height:900px;padding:70px 72px">
 <div class="kick" style="font-size:28px;color:#B5542C">नवरात्रि व्रत</div>
 <h1 style="font-size:76px;margin-top:8px;max-width:600px">व्रत में भी पेट रहे <em>हल्का</em></h1>
 <div style="position:absolute;left:72px;top:340px;width:560px">{chips(HI, 34, 14, "12px 28px")}</div>
 <p style="position:absolute;left:72px;top:640px;width:600px;font-size:25px;line-height:1.4;color:#4A615D">डायबिटीज़, प्रेगनेंसी या पेट की बीमारी है? <b style="font-weight:600;color:#12302C">व्रत से पहले डॉक्टर से पूछें।</b></p>
 <div style="position:absolute;right:50px;top:150px;width:500px;height:500px">{vrat_thali()}</div>
 {foot(hi=True, size=1.05)}</div>"""

WA_HI = f"""<div class="s saffron hi" style="width:1080px;height:1920px;padding:150px 80px">
 <div class="kick" style="font-size:36px;color:#B5542C;text-align:center">नवरात्रि व्रत</div>
 <h1 style="font-size:104px;text-align:center;margin-top:16px">पेट रहे <em>हल्का</em></h1>
 <div style="position:absolute;left:170px;top:470px;width:740px;height:740px">{vrat_thali()}</div>
 <div style="position:absolute;left:150px;right:150px;top:1260px">{chips(HI, 44, 20)}</div>
 <p style="position:absolute;left:80px;right:80px;top:1610px;font-size:34px;line-height:1.4;color:#4A615D;text-align:center">डायबिटीज़, प्रेगनेंसी या पेट की बीमारी है?<br><b style="font-weight:600;color:#12302C">व्रत से पहले डॉक्टर से पूछें।</b></p>
 {foot(pad=80, size=1.15, hi=True)}</div>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html, w, h, path):
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()
        shot(IG_EN, 1080, 1350, f"{OUT}/ig-navratri-fasting-en.png")
        shot(GBP_HI, 1200, 900, f"{OUT}/gbp-navratri-vrat-hi.png")
        shot(WA_HI, 1080, 1920, f"{OUT}/wa-status-navratri-vrat-hi.png")
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
