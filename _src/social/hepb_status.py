"""WhatsApp Status (1080x1920), Sat 17 Oct 2026: Know your hepatitis B status. Hindi and English, matching the redesigned post (hepb_post.py).
Run from anywhere: python3 _src/social/hepb_status.py  -> _src/out/hepb/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, shield
from hepb_post import OUT, TUBE, SYRINGE
from playwright.sync_api import sync_playwright

T = {
 "hi": dict(kick="लिवर को सुरक्षित रखें", h="अपना<br><em>हेपेटाइटिस B</em><br>स्टेटस जानें",
            facts=["सालों तक बिना लक्षण", "सिरोसिस और लिवर कैंसर का ख़तरा"],
            who_h="किन्हें जाँच ज़रूर करवानी चाहिए?",
            who=["परिवार में किसी को हेपेटाइटिस B हो", "प्रेगनेंसी में, हर महिला को", "कभी खून चढ़ा हो या ऑपरेशन हुआ हो", "टैटू, पियर्सिंग या असुरक्षित इंजेक्शन", "लिवर टेस्ट (SGPT) बढ़ा हुआ हो"],
            s1k="जाँच करवाएँ", s1="एक ब्लड टेस्ट: HBsAg", s2k="सुरक्षित रहें", s2="नेगेटिव? टीका लगवाएँ",
            note="पॉज़िटिव? इलाज और नियमित जाँच से लिवर ठीक रहता है।", url="drlochab.com/hi पर पढ़ें"),
 "en": dict(kick="Protect your liver", h="Know your<br><em>hepatitis B</em><br>status",
            facts=["Silent for years", "Can lead to cirrhosis and liver cancer"],
            who_h="Who should get tested?",
            who=["A family member has hepatitis B", "Every pregnant woman", "Had a blood transfusion or surgery", "Tattoos, piercing or unsafe injections", "Raised liver tests (SGPT)"],
            s1k="Get tested", s1="One blood test: HBsAg", s2k="Get protected", s2="Negative? Get the vaccine",
            note="Positive? Treatment and regular follow-up keep the liver healthy.", url="Read more on drlochab.com"),
}
TICK = '<svg viewBox="0 0 40 40" style="width:42px;height:42px;flex:none"><circle cx="20" cy="20" r="20" fill="#0D7466"/><path d="M11 21 L17 27 L29 14" fill="none" stroke="#fff" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def status(lang):
    x = T[lang]; hi = lang == "hi"; disp = "TD" if hi else "YS"
    facts = "".join(f'<div style="display:inline-flex;align-items:center;gap:14px;background:rgba(255,255,255,.12);border-radius:999px;padding:14px 26px;font-size:{32 if hi else 30}px;font-weight:600"><span style="width:14px;height:14px;border-radius:50%;background:#F3B84A"></span>{t}</div>' for t in x["facts"])
    who = "".join(f'<div style="display:flex;align-items:center;gap:20px;padding:{12 if hi else 15}px 0;border-top:2px solid #EEF3F1;font-size:34px">{TICK}{t}</div>' for t in x["who"])
    step = lambda icon, num, kick, col, txt, bg: (f'<div style="background:#FFFFFF;color:#12302C;border-radius:32px;padding:24px 26px;display:flex;flex-direction:column;gap:10px">'
        f'<div style="display:flex;align-items:center;justify-content:space-between">{icon}<span style="font-family:YS;font-size:80px;color:{bg};line-height:1">{num}</span></div>'
        f'<div class="kick" style="font-size:{24 if hi else 20}px;color:{col}">{kick}</div><div style="font-family:{disp},serif;font-size:{40 if hi else 38}px;line-height:1.2">{txt}</div></div>')
    return f"""<div class="s teal{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:120px 80px">
 <div style="position:absolute;right:-220px;top:-200px;width:760px;height:760px;border-radius:50%;background:rgba(255,255,255,.06)"></div>
 <div style="position:absolute;left:-180px;top:1180px;width:520px;height:520px;border-radius:50%;background:rgba(255,255,255,.05)"></div>
 <div class="kick" style="font-size:{32 if hi else 28}px;color:#F3B84A;position:relative">{x["kick"]}</div>
 <h1 style="font-size:{94 if hi else 88}px;margin-top:14px;position:relative;max-width:540px">{x["h"]}</h1>
 <div style="position:absolute;right:50px;top:160px;width:380px;height:380px;border-radius:50%;background:#E6F2EF;box-shadow:0 0 0 18px rgba(230,242,239,.18)"></div>
 <div style="position:absolute;right:80px;top:190px;width:320px;height:320px">{shield()}</div>
 <div style="position:absolute;left:80px;right:80px;top:620px;display:flex;flex-wrap:wrap;gap:14px">{facts}</div>
 <div style="position:absolute;left:80px;right:80px;top:{780 if hi else 770}px;background:#FFFFFF;color:#12302C;border-radius:36px;padding:30px 36px 18px">
  <div style="font-family:{disp},serif;font-size:{50 if hi else 48}px;margin-bottom:12px">{x["who_h"]}</div>{who}
 </div>
 <div style="position:absolute;left:80px;right:80px;top:{1380 if hi else 1320}px;display:grid;grid-template-columns:1fr 1fr;gap:20px">
  {step(TUBE, "1", x["s1k"], "#0D7466", x["s1"], "#DDEEEA")}
  {step(SYRINGE, "2", x["s2k"], "#B5542C", x["s2"], "#FCEBD0")}
 </div>
 <p style="position:absolute;left:80px;right:80px;top:{1700 if hi else 1640}px;font-size:{30 if hi else 28}px;color:#CFE5E0">{x["note"]}</p>
 <div style="position:absolute;right:80px;bottom:62px"><div style="display:inline-block;background:#F3B84A;color:#12302C;font-weight:600;font-size:{30 if hi else 28}px;padding:16px 30px;border-radius:999px">{x["url"]}</div></div>
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
