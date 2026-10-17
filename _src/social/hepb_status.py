"""WhatsApp Status (1080x1920), Sat 17 Oct 2026: Know your hepatitis B status. Hindi and English, matching the redesigned post (hepb_post.py).
Run from anywhere: python3 _src/social/hepb_status.py  -> _src/out/hepb/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, shield
from hepb_post import OUT, TUBE, SYRINGE
from playwright.sync_api import sync_playwright

T = {
 "hi": dict(kick="लिवर को सुरक्षित रखें", h="क्या आप अपना<br><em>हेपेटाइटिस B</em><br>स्टेटस जानते हैं?",
            facts=["सालों तक बिना लक्षण के रह सकता है", "सिरोसिस और लिवर कैंसर तक पहुँच सकता है"],
            s1k="जाँच करवाएँ", s1="एक ब्लड टेस्ट: HBsAg", s2k="सुरक्षित रहें", s2="नेगेटिव? टीका लगवाएँ",
            note="पॉज़िटिव? इलाज और नियमित जाँच से लिवर ठीक रहता है। परिवार की भी जाँच करवाएँ।",
            url="drlochab.com/hi पर पढ़ें"),
 "en": dict(kick="Protect your liver", h="Do you know<br>your <em>hepatitis B</em><br>status?",
            facts=["Often silent for years", "Can lead to cirrhosis and liver cancer"],
            s1k="Get tested", s1="One blood test: HBsAg", s2k="Get protected", s2="Negative? Get the vaccine",
            note="Positive? Treatment and regular follow-up keep the liver healthy. Test your family too.",
            url="Read more on drlochab.com"),
}

def status(lang):
    x = T[lang]; hi = lang == "hi"
    card = lambda icon, num, kick, col, txt, bg: (f'<div style="background:#FFFFFF;color:#12302C;border-radius:36px;padding:26px 32px;display:flex;align-items:center;gap:26px">{icon}'
        f'<div style="flex:1"><div class="kick" style="font-size:{24 if hi else 20}px;color:{col}">{kick}</div><div style="font-family:{"TD" if hi else "YS"},serif;font-size:{46 if hi else 44}px;line-height:1.2;margin-top:6px">{txt}</div></div>'
        f'<span style="font-family:YS;font-size:96px;color:{bg};line-height:1">{num}</span></div>')
    facts = "".join(f'<div style="display:flex;gap:16px;align-items:flex-start;font-size:{36 if hi else 34}px;line-height:1.35;color:#E6F2EF"><span style="flex:none;width:18px;height:18px;border-radius:50%;background:#F3B84A;margin-top:{16 if hi else 14}px"></span>{t}</div>' for t in x["facts"])
    return f"""<div class="s teal{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:130px 80px">
 <div style="position:absolute;right:-200px;top:-160px;width:700px;height:700px;border-radius:50%;background:rgba(255,255,255,.06)"></div>
 <div class="kick" style="font-size:{32 if hi else 28}px;color:#F3B84A;position:relative">{x["kick"]}</div>
 <h1 style="font-size:{98 if hi else 100}px;margin-top:16px;position:relative">{x["h"]}</h1>
 <div style="position:absolute;right:50px;top:{510 if hi else 490}px;width:440px;height:440px;border-radius:50%;background:#E6F2EF"></div>
 <div style="position:absolute;right:90px;top:{550 if hi else 530}px;width:360px;height:360px">{shield()}</div>
 <div style="position:absolute;left:80px;top:{990 if hi else 970}px;right:80px;display:flex;flex-direction:column;gap:14px">{facts}</div>
 <div style="position:absolute;left:80px;right:80px;top:1150px;display:flex;flex-direction:column;gap:20px">
  {card(TUBE, "1", x["s1k"], "#0D7466", x["s1"], "#DDEEEA")}
  {card(SYRINGE, "2", x["s2k"], "#B5542C", x["s2"], "#FCEBD0")}
 </div>
 <p style="position:absolute;left:80px;right:80px;top:{1550 if hi else 1520}px;font-size:{32 if hi else 30}px;line-height:1.4;color:#CFE5E0">{x["note"]}</p>
 <div style="position:absolute;left:80px;top:1640px"><div style="display:inline-block;background:#F3B84A;color:#12302C;font-weight:600;font-size:32px;padding:16px 32px;border-radius:999px">{x["url"]}</div></div>
 {foot(light=True, pad=80, size=1.1, hi=hi)}</div>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("hi", "en"):
            pg = b.new_page(viewport={"width": 1080, "height": 1920})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{status(lang)}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/wa-status-hepatitis-b-{lang}.png"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html"); print("done")
