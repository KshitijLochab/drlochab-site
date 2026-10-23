"""'Breaking news' style announcement: now open at Apollo Clinic, Sector 52 (23 Oct 2026, redesign of apollo_clinic_launch.py).
Instagram post (1080x1350), Instagram story (1080x1920), WhatsApp status EN + HI (1080x1920), Google Business image (1200x900).
Timings and address come from clinics.py. Clinic name in plain text only (no Apollo logo). Captions/post text are reused
from apollo_clinic_launch.py (address added).
Run: python3 _src/social/apollo_clinic_news.py  -> _src/out/apollo-clinic-news/"""
import os, sys, base64
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from week_2026_10_12 import CSS as BASE_CSS, SRC, LOGO
import clinics
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "apollo-clinic-news"); os.makedirs(OUT, exist_ok=True)
PHOTO = "data:image/jpeg;base64," + base64.b64encode(open(f"{SRC}/dr-lochab.jpg", "rb").read()).decode()
RED, YEL, INK, NAVY = "#E3262F", "#FFC72C", "#0A1715", "#071A18"

CSS = BASE_CSS + f"""
@font-face{{font-family:"FV";src:url("file://{SRC}/fonts/Figtree.ttf");font-weight:300 900}}
.news{{position:relative;overflow:hidden;color:#fff;font-family:"FV","FT",sans-serif;
 background:radial-gradient(90% 60% at 80% 18%,#145A50 0%,rgba(20,90,80,0) 60%),linear-gradient(160deg,#0B2E29 0%,{NAVY} 55%,#04100E 100%)}}
.rays{{position:absolute;inset:0;background:repeating-linear-gradient(115deg,rgba(255,255,255,.035) 0 26px,rgba(255,255,255,0) 26px 70px)}}
.tag{{display:inline-flex;align-items:center;gap:14px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}}
.tag .r{{background:{RED};padding:12px 22px;display:inline-flex;align-items:center;gap:12px}}
.tag .w{{background:#fff;color:{INK};padding:12px 22px}}
.dot{{width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 0 0 6px rgba(255,255,255,.3)}}
.mega{{font-weight:900;line-height:.86;letter-spacing:-.03em;text-transform:uppercase}}
.mega b{{color:{YEL};font-weight:900}}
.ticker{{position:absolute;left:0;right:0;display:flex;align-items:stretch;height:96px;font-weight:800;text-transform:uppercase;letter-spacing:.04em}}
.ticker .k{{background:{RED};display:flex;align-items:center;padding:0 30px;font-size:34px;font-weight:900;flex:none}}
.ticker .t{{background:{YEL};color:{INK};flex:1;display:flex;align-items:center;white-space:nowrap;overflow:hidden;font-size:32px;padding-left:26px}}
.photo{{position:absolute;border-radius:50%;overflow:hidden;border:10px solid {YEL};box-shadow:0 30px 60px rgba(0,0,0,.45)}}
.photo img{{width:100%;height:100%;object-fit:cover;object-position:50% 12%}}
.badge{{position:absolute;background:{RED};color:#fff;font-weight:900;text-transform:uppercase;letter-spacing:.06em;padding:12px 22px;border-radius:999px;display:flex;align-items:center;gap:12px;box-shadow:0 12px 24px rgba(0,0,0,.35)}}
.timecard{{background:{YEL};color:{INK};border-radius:28px;display:inline-flex;align-items:center;gap:26px}}
.hi .mega,.hi .tag,.hi .ticker{{font-family:"MK","FV",sans-serif;letter-spacing:0}}
"""

def pin(s=40, col=YEL):
    return f'<svg viewBox="0 0 64 80" style="width:{s}px;height:{s*1.25}px;flex:none"><path d="M32 78 C32 78 6 46 6 28 A26 26 0 0 1 58 28 C58 46 32 78 32 78 Z" fill="{col}"/><circle cx="32" cy="28" r="10" fill="{INK}"/></svg>'

def brand(col="#fff", size=1.0, hi=False):
    name = "डॉ. क्षितिज लोचब" if hi else "Dr. Kshitij Lochab"
    sub = "गैस्ट्रोएंटेरोलॉजिस्ट · drlochab.com/hi" if hi else "Gastroenterologist · drlochab.com"
    return (f'<div style="display:flex;align-items:center;gap:14px"><img src="{LOGO}" style="width:{int(56*size)}px;height:{int(56*size)}px">'
            f'<div><div style="font-family:{"TD" if hi else "YS"};font-size:{int(28*size)}px;color:{col}">{name}</div>'
            f'<div style="font-size:{int(19*size)}px;color:#BFD9D3">{sub}</div></div></div>')

def T(hi):
    A = clinics.APOLLO_CLINIC["hi" if hi else "en"]
    if hi:
        return dict(br="ब्रेकिंग", new="नया क्लिनिक", now="अभी", open="खुला", lead="डॉ. क्षितिज लोचब अब परामर्श दे रहे हैं", clinic="अपोलो क्लिनिक", sector="सेक्टर 52, गुरुग्राम",
                    days="सोम–शनि", time="शाम 4–6", addr=clinics.APOLLO_CLINIC["addr"]["hi"], badge="अब यहाँ भी", book="WhatsApp या कॉल करके, या सीधे क्लिनिक पर अपॉइंटमेंट",
                    tick=f"अब खुला · अपोलो क्लिनिक, सेक्टर 52 · सोम–शनि शाम 4–6 बजे · आर्क्योरा क्लिनिक, सेक्टर 51 भी जारी · ", note="समय बदल सकता है; ताज़ा समय drlochab.com/hi पर")
    return dict(br="Breaking", new="New clinic", now="Now", open="Open", lead="Dr. Kshitij Lochab is now consulting at", clinic="Apollo Clinic", sector="Sector 52, Gurugram",
                days="Mon–Sat", time="4–6 pm", addr=clinics.APOLLO_CLINIC["addr"]["en"], badge="Now consulting", book="Book on WhatsApp or call, or directly at the clinic",
                tick="Now open · Apollo Clinic, Sector 52 · Mon–Sat 4–6 pm · Arcura Clinic, Sector 51 continues · Book on WhatsApp · ", note="Timings may change; latest on drlochab.com")

def tag(x, s=30):
    return f'<div class="tag" style="font-size:{s}px"><span class="r"><span class="dot"></span>{x["br"]}</span><span class="w">{x["new"]}</span></div>'

def ticker(x, bottom=0, k="LIVE"):
    return f'<div class="ticker" style="bottom:{bottom}px"><div class="k">{k}</div><div class="t">{(x["tick"] * 3)}</div></div>'

def timecard(x, s=1.0):
    return (f'<div class="timecard" style="padding:{int(20*s)}px {int(34*s)}px"><div style="font-weight:900;font-size:{int(40*s)}px;text-transform:uppercase;line-height:1">{x["days"]}</div>'
            f'<div style="width:4px;align-self:stretch;background:{INK};opacity:.25"></div><div style="font-weight:900;font-size:{int(96*s)}px;line-height:1;letter-spacing:-.02em">{x["time"]}</div></div>')

def post(hi=False):
    x = T(hi)
    return f"""<div class="news{' hi' if hi else ''}" style="width:1080px;height:1350px;padding:70px 72px"><div class="rays"></div>
 {tag(x)}
 <div class="mega" style="font-size:205px;margin-top:44px">{x["now"]}<br><b>{x["open"]}</b></div>
 <div class="photo" style="width:330px;height:330px;right:62px;top:190px"><img src="{PHOTO}"></div>
 <div class="badge" style="right:84px;top:492px;font-size:24px"><span class="dot" style="width:14px;height:14px"></span>{x["badge"]}</div>
 <div style="font-size:34px;font-weight:600;margin-top:34px;color:#DCEFEA">{x["lead"]}</div>
 <div style="font-family:YS;font-size:96px;line-height:1;margin-top:8px">{x["clinic"]}</div>
 <div style="font-size:46px;font-weight:800;color:{YEL};margin-top:6px">{x["sector"]}</div>
 <div style="display:flex;align-items:center;gap:30px;margin-top:34px">{timecard(x, .92)}</div>
 <div style="display:flex;gap:14px;align-items:flex-start;margin-top:26px;font-size:24px;line-height:1.35;color:#CFE5E0;max-width:900px">{pin(30)}<span>{x["addr"]}</span></div>
 <div style="position:absolute;left:72px;right:72px;bottom:120px;display:flex;justify-content:space-between;align-items:flex-end">{brand()}<div style="font-size:19px;color:#9FCFC5;text-align:right">{x["note"]}</div></div>
 {ticker(x)}</div>"""

def tall(hi=False):
    x = T(hi)
    return f"""<div class="news{' hi' if hi else ''}" style="width:1080px;height:1920px;padding:150px 72px"><div class="rays"></div>
 {tag(x, 34)}
 <div class="mega" style="font-size:{200 if not hi else 250}px;margin-top:70px">{x["now"]}<br><b>{x["open"]}</b></div>
 <div class="photo" style="width:360px;height:360px;right:60px;top:320px"><img src="{PHOTO}"></div>
 <div class="badge" style="right:80px;top:650px;font-size:28px"><span class="dot" style="width:16px;height:16px"></span>{x["badge"]}</div>
 <div style="font-size:40px;font-weight:600;margin-top:110px;color:#DCEFEA">{x["lead"]}</div>
 <div style="font-family:{"TD" if hi else "YS"};font-size:{120 if not hi else 110}px;line-height:1.05;margin-top:12px">{x["clinic"]}</div>
 <div style="font-size:58px;font-weight:800;color:{YEL};margin-top:8px">{x["sector"]}</div>
 <div style="margin-top:70px">{timecard(x, 1.2)}</div>
 <div style="display:flex;gap:16px;align-items:flex-start;margin-top:40px;font-size:31px;line-height:1.35;color:#CFE5E0">{pin(38)}<span>{x["addr"]}</span></div>
 <div style="font-size:31px;line-height:1.35;margin-top:22px;color:#fff;font-weight:600">{x["book"]}</div>
 <div style="margin-top:34px;padding:20px 26px;border-radius:22px;background:rgba(255,255,255,.08);font-size:29px;line-height:1.35;color:#DCEFEA">{"आर्क्योरा क्लिनिक, सेक्टर 51 भी जारी: सोम–शुक्र शाम 6–8 बजे · रविवार सुबह 9–दोपहर 1 बजे" if hi else "Arcura Clinic, Sector 51 continues: Mon–Fri 6–8 pm · Sunday 9 am–1 pm"}</div>
 <div style="position:absolute;left:72px;right:72px;bottom:150px;display:flex;justify-content:space-between;align-items:flex-end">{brand(size=1.1, hi=hi)}<div style="font-size:21px;color:#9FCFC5;text-align:right;max-width:380px">{x["note"]}</div></div>
 {ticker(x, 0, "नया" if hi else "LIVE")}</div>"""

def gbp():
    x = T(False)
    return f"""<div class="news" style="width:1200px;height:900px;padding:56px 64px"><div class="rays"></div>
 {tag(x, 26)}
 <div class="mega" style="font-size:150px;margin-top:30px">{x["now"]} <b>{x["open"]}</b></div>
 <div style="font-size:28px;font-weight:600;margin-top:22px;color:#DCEFEA">{x["lead"]}</div>
 <div style="font-family:YS;font-size:74px;line-height:1;margin-top:6px">{x["clinic"]}</div><div style="font-size:38px;font-weight:800;color:{YEL};margin-top:6px">{x["sector"]}</div>
 <div style="margin-top:22px">{timecard(x, .74)}</div>
 <div class="photo" style="width:300px;height:300px;right:64px;top:250px"><img src="{PHOTO}"></div>
 <div class="badge" style="right:92px;top:520px;font-size:21px"><span class="dot" style="width:12px;height:12px"></span>{x["badge"]}</div>
 {ticker(x)}</div>"""

def render(fn, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fn()}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(600); pg.screenshot(path=path); pg.close()

if __name__ == "__main__":
    from PIL import Image
    import apollo_clinic_launch as L
    addr_en, addr_hi = clinics.APOLLO_CLINIC["addr"]["en"], clinics.APOLLO_CLINIC["addr"]["hi"]
    with sync_playwright() as p:
        b = p.chromium.launch()
        render(post, 1080, 1350, f"{OUT}/insta-post.png", b)
        render(tall, 1080, 1920, f"{OUT}/insta-story.png", b)
        render(lambda: tall(False), 1080, 1920, f"{OUT}/whatsapp-status-en.png", b)
        render(lambda: tall(True), 1080, 1920, f"{OUT}/whatsapp-status-hi.png", b)
        render(gbp, 1200, 900, f"{OUT}/google-business.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
    cap = L.CAPTION.replace("📍 Now also consulting at Apollo Clinic, Sector 52, Gurugram\n", f"🚨 NOW OPEN: Apollo Clinic, Sector 52, Gurugram\n📍 {addr_en}\n")
    gtxt = L.GBP_TEXT.replace("Now also consulting at Apollo Clinic, Sector 52, Gurugram.", f"Now open: consultations at Apollo Clinic, Sector 52, Gurugram ({addr_en}).")
    wen = L.WHATSAPP_EN.replace("🕓", f"📍 {addr_en}\n🕓", 1)
    whi = L.WHATSAPP_HI.replace("🕓", f"📍 {addr_hi}\n🕓", 1)
    for name, txt in [("instagram-caption.txt", cap + "\n\n" + L.STORY_NOTE), ("google-business-post.txt", gtxt),
                      ("whatsapp-message-en.txt", wen), ("whatsapp-message-hi.txt", whi)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done")
