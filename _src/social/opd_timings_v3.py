"""New OPD timings, third design (17 Nov 2026): modern and sophisticated, in the same visual language as the visiting card
Dr. Lochab chose (card 2): warm off-white and deep teal, one serif for headings, tracked gold capitals, a thin gold rule,
the fine gold line drawing of the digestive tract, lots of white space and no cartoon illustration.
Instagram carousel EN + HI (cover + timetable; the timetable also works as a single post), story / WhatsApp Status EN + HI,
Google Business image.
Run: python3 _src/social/opd_timings_v3.py -> _src/out/opd-timings-v3/"""
import base64, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, SRC)
import hub
import week_2026_11_09 as w9
from week_2026_10_12 import CSS
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "opd-timings-v3"); os.makedirs(OUT, exist_ok=True)
w9.OUT = OUT
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = f"data:image/png;base64,{b64(f'{SRC}/brand/logo-mark.png')}"
CREAM, INK, TEAL, DEEP, GOLD, GOLDT, MUTE = "#F6F2EA", "#13241F", "#0D7466", "#0A4D45", "#C69A3E", "#A2741C", "#6D7A73"
FOIL = "linear-gradient(90deg,#B8862E,#F1D28A,#C7952F)"

T = {
 "en": dict(kick="New OPD timings", cover="Now seeing patients <i>every evening.</i>", cover_sub="Monday to Saturday · three places in Gurugram",
            head="Evening OPD", head2="Monday to Saturday",
            rows=[("Mon · Wed · Fri", "Apollo Clinic", "Sector 52, Gurugram", "6 – 8 pm"),
                  ("Tue · Thu · Sat", "Apollo Hospitals", "Golf Course Road, Gurugram", "4 – 6 pm"),
                  ("Tue · Thu · Sat", "Arcura Clinic", "Sector 51, Mayfield Garden", "6:30 – 8 pm")],
            urg_k="Urgent during the day", urg="Apollo Hospitals only. Please call or WhatsApp first.",
            sun="No OPD on Sunday", swipe="Timings →", name="Dr. Kshitij Lochab",
            role="Consultant Gastroenterologist & Therapeutic Endoscopist", book="Appointments", call="Call or WhatsApp"),
 "hi": dict(kick="ओपीडी का नया समय", cover="अब हर <i>शाम</i> मरीज़ों के लिए।", cover_sub="सोमवार से शनिवार · गुरुग्राम में तीन जगह",
            head="शाम की ओपीडी", head2="सोमवार से शनिवार",
            rows=[("सोम · बुध · शुक्र", "अपोलो क्लिनिक", "सेक्टर 52, गुरुग्राम", "शाम 6 – 8"),
                  ("मंगल · गुरु · शनि", "अपोलो हॉस्पिटल्स", "गोल्फ़ कोर्स रोड, गुरुग्राम", "शाम 4 – 6"),
                  ("मंगल · गुरु · शनि", "आर्क्योरा क्लिनिक", "सेक्टर 51, मेफ़ील्ड गार्डन", "शाम 6:30 – 8")],
            urg_k="दिन में अर्जेंट", urg="सिर्फ़ अपोलो हॉस्पिटल्स में। पहले कॉल या WhatsApp करें।",
            sun="रविवार को ओपीडी नहीं", swipe="समय देखें →", name="डॉ. क्षितिज लोचब",
            role="कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट", book="अपॉइंटमेंट", call="कॉल या WhatsApp"),
}
PHONE, SITE = "+91 96671 04882", {"en": "drlochab.com", "hi": "drlochab.com/hi"}

X_CSS = f"""
.serif{{font-family:"YS",serif;font-weight:400}}
.hi .serif{{font-family:"TD","YS",serif}}
.caps{{font-weight:600;letter-spacing:.24em;text-transform:uppercase}}
.hi .caps{{letter-spacing:.04em}}
h1 i,h2 i{{font-style:normal;color:{TEAL}}}
.dark h1 i,.dark h2 i{{color:#E9C77B}}
"""

def gut_line(col, sw=2.2, w=300):
    return (f'<svg viewBox="40 70 240 340" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">'
            + "".join(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
                      for d in (hub.ESOPH, hub.STOM, hub.DUO, hub.COLON, hub.SMALL)) + "</svg>")

def rule(w=120, h=3):
    return f'<div style="width:{w}px;height:{h}px;background:{FOIL};border-radius:2px"></div>'

def signature(lang, dark=False, size=1.0):
    fg = "#FFFFFF" if dark else INK; sub = "#BFDCD5" if dark else MUTE; s = size
    return (f'<div style="display:flex;align-items:center;gap:{int(22*s)}px"><img src="{LOGO}" style="width:{int(64*s)}px;height:{int(64*s)}px;border-radius:{int(14*s)}px">'
            f'<div><div class="serif" style="font-size:{int(30*s)}px;color:{fg}">{T[lang]["name"]}</div>'
            f'<div style="font-size:{int(20*s)}px;color:{sub}">{T[lang]["role"]}</div></div></div>')

def contact(lang, dark=False, size=1.0):
    fg = "#FFFFFF" if dark else INK; sub = "#BFDCD5" if dark else MUTE; acc = "#E9C77B" if dark else TEAL; s = size
    return (f'<div style="display:flex;align-items:flex-end;gap:{int(28*s)}px">'
            f'<div><div style="font-size:{int(20*s)}px;color:{sub}">{T[lang]["call"]}</div><div class="serif" style="font-family:YS;font-size:{int(40*s)}px;color:{fg}">{PHONE}</div></div>'
            f'<div style="width:1.5px;height:{int(56*s)}px;background:{GOLD}"></div>'
            f'<div class="serif" style="font-family:YS;font-size:{int(40*s)}px;color:{acc}">{SITE[lang]}</div></div>')

def timetable(lang, size=1.0, dark=False):
    s = size; X = T[lang]
    fg = "#FFFFFF" if dark else INK; sub = "#BFDCD5" if dark else MUTE; line = "rgba(255,255,255,.2)" if dark else "#E2D9C8"; day = "#E9C77B" if dark else GOLDT
    out = ""
    for d, p, a, t in X["rows"]:
        out += (f'<div style="display:flex;align-items:center;gap:{int(24*s)}px;padding:{int(30*s)}px 0;border-top:1.5px solid {line}">'
                f'<div style="flex:1;min-width:0"><div class="caps" style="font-size:{int((27 if lang == "hi" else 21)*s)}px;color:{day}">{d}</div>'
                f'<div class="serif" style="font-size:{int(54*s)}px;line-height:1.1;color:{fg};margin-top:{int(8*s)}px">{p}</div>'
                f'<div style="font-size:{int(24*s)}px;color:{sub};margin-top:{int(4*s)}px">{a}</div></div>'
                f'<div class="serif" style="font-family:{"TD" if lang == "hi" else "YS"};font-size:{int(52*s)}px;color:{fg};white-space:nowrap">{t}</div></div>')
    return out + f'<div style="border-top:1.5px solid {line}"></div>'

def urgent(lang, size=1.0, dark=False):
    s = size; X = T[lang]; fg = "#FFFFFF" if dark else INK
    return (f'<div style="display:flex;gap:{int(22*s)}px;align-items:flex-start">'
            f'<div style="width:{int(4*s)}px;align-self:stretch;background:#B0362B;border-radius:2px"></div>'
            f'<div><div class="caps" style="font-size:{int((26 if lang == "hi" else 20)*s)}px;color:#B0362B">{X["urg_k"]}</div>'
            f'<div style="font-size:{int(28*s)}px;color:{fg};margin-top:{int(6*s)}px">{X["urg"]}</div></div></div>')

# ---------------- Instagram slide 1: cover ----------------
def cover(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s dark{hi}" style="width:1080px;height:1350px;background:linear-gradient(165deg,#0F6B5F 0%,{DEEP} 60%,#073B35 100%);color:#fff;padding:110px 96px">
 <div style="position:absolute;right:70px;top:300px;opacity:.9">{gut_line("#D9B061", 2.4, 400)}</div>
 <div class="caps" style="font-size:24px;color:#E9C77B">{X["kick"]}</div>
 <div style="margin:34px 0 40px">{rule(140)}</div>
 <h1 class="serif" style="font-size:{108 if lang == "en" else 92}px;line-height:1.06;max-width:640px;font-weight:400">{X["cover"]}</h1>
 <p style="font-size:32px;color:#CFE5E0;margin-top:40px;max-width:560px;line-height:1.4">{X["cover_sub"]}</p>
 <div style="position:absolute;left:96px;right:96px;bottom:96px;display:flex;justify-content:space-between;align-items:flex-end">
  {signature(lang, dark=True)}<span style="font-size:26px;color:#E9C77B;font-weight:600">{X["swipe"]}</span></div>
</div>"""

# ---------------- Instagram slide 2: timetable (also a stand-alone post) ----------------
def table_post(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s{hi}" style="width:1080px;height:1350px;background:{CREAM};color:{INK};padding:96px 96px">
 <img src="{LOGO}" style="position:absolute;right:96px;top:90px;width:70px;height:70px;border-radius:16px">
 <div style="position:absolute;right:80px;bottom:60px;opacity:.5">{gut_line(GOLD, 2, 120)}</div>
 <div class="caps" style="font-size:{28 if lang == "hi" else 22}px;color:{GOLDT}">{X["name"]} · {X["kick"]}</div>
 <h1 class="serif" style="font-size:{86 if lang == "en" else 76}px;line-height:1.05;margin-top:22px;font-weight:400">{X["head"]}<br><i>{X["head2"]}</i></h1>
 <div style="margin-top:44px">{timetable(lang, .95)}</div>
 <div style="margin-top:34px;display:flex;justify-content:space-between;align-items:flex-start;gap:30px">{urgent(lang, .95)}
  <span style="font-size:24px;color:{MUTE};white-space:nowrap;margin-top:4px">{X["sun"]}</span></div>
 <div style="position:absolute;left:96px;right:96px;bottom:84px">{contact(lang, size=.95)}</div>
</div>"""

# ---------------- Story / WhatsApp Status ----------------
def story(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s{hi}" style="width:1080px;height:1920px;background:{CREAM};color:{INK}">
 <div class="dark" style="position:absolute;left:0;right:0;top:0;height:780px;background:linear-gradient(165deg,#0F6B5F 0%,{DEEP} 70%);color:#fff;padding:170px 90px 0">
  <div style="position:absolute;right:70px;top:300px;opacity:.9">{gut_line("#D9B061", 2.4, 230)}</div>
  <img src="{LOGO}" style="position:absolute;right:90px;top:160px;width:72px;height:72px;border-radius:16px">
  <div class="caps" style="font-size:{30 if lang == "hi" else 26}px;color:#E9C77B">{X["kick"]}</div>
  <div style="margin:28px 0 30px">{rule(130)}</div>
  <h1 class="serif" style="font-size:{86 if lang == "en" else 76}px;line-height:1.06;max-width:640px;font-weight:400">{X["cover"]}</h1>
  <div class="serif" style="position:absolute;left:90px;bottom:44px;font-size:30px;color:#CFE5E0">{X["name"]}</div></div>
 <div style="position:absolute;left:90px;right:90px;top:830px">{timetable(lang, 1.04 if lang == "en" else .9)}
  <div style="margin-top:44px">{urgent(lang, 1.1)}</div>
  <div style="margin-top:24px;font-size:28px;color:{MUTE}">{X["sun"]}</div></div>
 <div style="position:absolute;left:90px;right:90px;bottom:{150 if lang == "en" else 110}px">{contact(lang, size=.95)}</div>
</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    X = T["en"]
    return f"""<div class="s" style="width:1200px;height:900px;background:{CREAM};color:{INK}">
 <div class="dark" style="position:absolute;left:0;top:0;bottom:0;width:430px;background:linear-gradient(165deg,#0F6B5F 0%,{DEEP} 70%);color:#fff;padding:70px 56px">
  <div class="caps" style="font-size:18px;color:#E9C77B">{X["kick"]}</div>
  <div style="margin:22px 0 26px">{rule(100, 2)}</div>
  <h1 class="serif" style="font-size:58px;line-height:1.08;font-weight:400">Now seeing patients <i>every evening.</i></h1>
  <div style="position:absolute;left:56px;bottom:150px;opacity:.85">{gut_line("#D9B061", 2.2, 150)}</div>
  <div style="position:absolute;left:56px;right:40px;bottom:56px;display:flex;align-items:center;gap:14px"><img src="{LOGO}" style="width:48px;height:48px;border-radius:11px">
   <div class="serif" style="font-size:22px">Dr. Kshitij Lochab</div></div></div>
 <div style="position:absolute;left:490px;right:60px;top:56px">
  <div class="caps" style="font-size:17px;color:{GOLDT}">Monday to Saturday</div>
  <div style="margin-top:10px">{timetable("en", .68)}</div>
  <div style="margin-top:22px">{urgent("en", .74)}</div>
  <div style="margin-top:12px;font-size:18px;color:{MUTE}">No OPD on Sunday</div></div>
 <div style="position:absolute;left:490px;right:60px;bottom:52px">{contact("en", size=.72)}</div>
</div>"""

if __name__ == "__main__":
    from PIL import Image
    w9.CSS = CSS + X_CSS
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("en", "hi"):
            w9.render(lambda: cover(lang), 1080, 1350, f"{OUT}/ig-timings-{lang}-1-cover.png", b)
            w9.render(lambda: table_post(lang), 1080, 1350, f"{OUT}/ig-timings-{lang}-2-timetable.png", b)
            w9.render(lambda: story(lang), 1080, 1920, f"{OUT}/story-status-timings-{lang}.png", b)
        w9.render(gbp, 1200, 900, f"{OUT}/google-business-timings.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=94); os.remove(f"{OUT}/{f}")
    print("done", sorted(os.listdir(OUT)))
