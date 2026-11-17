"""New OPD timings, redesigned (17 Nov 2026): bolder, visual-first version of opd_timings_nov2026.py.
Idea: "Your evening gastro clinic". A dusk sky over a Gurugram skyline with a big clock whose 4 to 8 pm arc glows, and the
doctor's portrait; then the week as two bold tickets (Mon·Wed·Fri and Tue·Thu·Sat); then the urgent-daytime rule.
Instagram carousel EN + HI (3 slides, 1080x1350), story / WhatsApp Status EN + HI (1080x1920), Google Business image (1200x900).
Run from anywhere: python3 _src/social/opd_timings_v2.py  -> _src/out/opd-timings-v2/"""
import base64, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC
import week_2026_11_09 as w9
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "opd-timings-v2"); os.makedirs(OUT, exist_ok=True)
w9.OUT = OUT
PHOTO = "data:image/jpeg;base64," + base64.b64encode(open(f"{SRC}/dr-lochab.jpg", "rb").read()).decode()

TEAL, SAFF, PLUM, GOLD = "#0D7466", "#F08A24", "#7A4E9E", "#F3B84A"
DUSK = "background:linear-gradient(180deg,#141A3C 0%,#2B2350 34%,#6A2E5E 62%,#D9573A 84%,#F5A04A 100%);color:#fff"

T = {
 "en": dict(kick="New OPD timings", h1="Your <em>evening</em> gastro clinic", sub="Every evening · Monday to Saturday · 3 places in Gurugram",
            swipe="Where and when →", mwf="MON · WED · FRI", tts="TUE · THU · SAT",
            ac=("Apollo Clinic", "Sector 52", "6 – 8 pm"), ah=("Apollo Hospitals", "Golf Course Road", "4 – 6 pm"), ar=("Arcura Clinic", "Sector 51", "6:30 – 8 pm"),
            then="then", sun="Sunday: no OPD", wk="Your week", wk_h="Pick your <em>day</em>",
            urg_k="Urgent during the day?", urg_h="Come to <em>Apollo Hospitals</em>", urg_p="Daytime urgent consultations happen only at Apollo Hospitals, Golf Course Road. Call or WhatsApp first so we are ready for you.",
            emerg="Severe pain, vomiting blood or fainting? Call 112.", cta="Call or WhatsApp", num="+91 96671 04882", site="drlochab.com"),
 "hi": dict(kick="ओपीडी का नया समय", h1="अब हर <em>शाम</em> आपके पेट का डॉक्टर", sub="सोमवार से शनिवार · हर शाम · गुरुग्राम में 3 जगह",
            swipe="कहाँ और कब →", mwf="सोम · बुध · शुक्र", tts="मंगल · गुरु · शनि",
            ac=("अपोलो क्लिनिक", "सेक्टर 52", "शाम 6 – 8"), ah=("अपोलो हॉस्पिटल्स", "गोल्फ़ कोर्स रोड", "शाम 4 – 6"), ar=("आर्क्योरा क्लिनिक", "सेक्टर 51", "शाम 6:30 – 8"),
            then="फिर", sun="रविवार: ओपीडी नहीं", wk="आपका हफ़्ता", wk_h="अपना <em>दिन</em> चुनें",
            urg_k="दिन में अर्जेंट?", urg_h="<em>अपोलो हॉस्पिटल्स</em> आइए", urg_p="दिन में अर्जेंट परामर्श सिर्फ़ अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड में होता है। पहले कॉल या WhatsApp करें ताकि हम तैयार रहें।",
            emerg="तेज़ दर्द, ख़ून की उल्टी या बेहोशी? 112 पर कॉल करें।", cta="कॉल या WhatsApp", num="+91 96671 04882", site="drlochab.com/hi"),
}

# ---------------- original drawings ----------------
def skyline(w=1080, h=380, glow=True):
    """Gurugram-style glass towers in silhouette with lit windows, against the sunset (viewBox 0 0 1080 380)."""
    import random
    rnd = random.Random(7)
    towers = [(0, 170, 90), (80, 120, 70), (140, 210, 110), (240, 90, 80), (310, 240, 120), (420, 150, 70), (480, 280, 130),
              (600, 190, 90), (680, 250, 110), (780, 130, 80), (850, 220, 120), (960, 160, 120)]
    g = ""
    for x, th, tw in towers:
        y0 = h - th
        g += f'<rect x="{x}" y="{y0}" width="{tw}" height="{th}" fill="#1A1433"/>'
        g += f'<rect x="{x}" y="{y0}" width="{tw*.35:.0f}" height="{th}" fill="#231C42"/>'
        for wy in range(y0 + 16, h - 10, 22):
            for wx in range(x + 10, x + tw - 12, 18):
                if rnd.random() < .34:
                    g += f'<rect x="{wx}" y="{wy}" width="9" height="11" rx="1.5" fill="#FFD27A" opacity="{rnd.choice([.55, .8, 1])}"/>'
    sun = (f'<circle cx="540" cy="{h-20}" r="230" fill="url(#sun)"/><circle cx="540" cy="{h-20}" r="330" fill="#FFB25A" opacity=".18"/>' if glow else "")
    return (f'<svg viewBox="0 0 1080 {h}" style="width:{w}px;display:block" xmlns="http://www.w3.org/2000/svg">'
            f'<defs><radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFE7A8"/><stop offset=".6" stop-color="#FFB453"/><stop offset="1" stop-color="#F07A3A"/></radialGradient></defs>'
            f'{sun}{g}<rect y="{h-6}" width="1080" height="6" fill="#120E26"/></svg>')

def clock(w=420, lang="en"):
    """A big wall clock; the 4 to 8 pm arc glows gold; hands at 6:30 (viewBox 0 0 400 400)."""
    import math
    cx = cy = 200; R = 170
    pt = lambda hr, r: (cx + r * math.sin(math.radians(hr * 30)), cy - r * math.cos(math.radians(hr * 30)))
    x1, y1 = pt(4, 150); x2, y2 = pt(8, 150)
    ticks = "".join(f'<line x1="{pt(i/5,158)[0]:.1f}" y1="{pt(i/5,158)[1]:.1f}" x2="{pt(i/5,166 if i%5 else 140)[0]:.1f}" y2="{pt(i/5,166 if i%5 else 140)[1]:.1f}" '
                    f'stroke="#12302C" stroke-width="{6 if i%5==0 else 2}" stroke-linecap="round"/>' for i in range(60))
    nums = "".join(f'<text x="{pt(n,112)[0]:.0f}" y="{pt(n,112)[1]+14:.0f}" text-anchor="middle" font-family="YS" font-size="40" fill="{"#C2551F" if n in (4,5,6,7,8) else "#12302C"}">{n}</text>' for n in range(1, 13))
    hx, hy = pt(6.5, 82); mx, my = pt(6, 130)
    return f"""<svg viewBox="0 0 400 400" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><filter id="cl" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="18" stdDeviation="18" flood-color="#0B0820" flood-opacity=".55"/></filter>
<radialGradient id="face" cx=".45" cy=".4" r=".7"><stop offset="0" stop-color="#FFFDF6"/><stop offset="1" stop-color="#F3E7CF"/></radialGradient></defs>
<g filter="url(#cl)"><circle cx="{cx}" cy="{cy}" r="{R+18}" fill="#F3B84A"/><circle cx="{cx}" cy="{cy}" r="{R+6}" fill="#C98A1E"/><circle cx="{cx}" cy="{cy}" r="{R}" fill="url(#face)"/></g>
<path d="M{x1:.1f} {y1:.1f} A150 150 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="#F5A04A" stroke-width="26" stroke-linecap="round" opacity=".85"/>
{ticks}{nums}
<line x1="{cx}" y1="{cy}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#12302C" stroke-width="12" stroke-linecap="round"/>
<line x1="{cx}" y1="{cy}" x2="{mx:.1f}" y2="{my:.1f}" stroke="#12302C" stroke-width="7" stroke-linecap="round"/>
<circle cx="{cx}" cy="{cy}" r="14" fill="#C2551F"/><circle cx="{cx}" cy="{cy}" r="5" fill="#FFF"/></svg>"""

def stars(n=26, w=1080, h=500, seed=3):
    import random
    r = random.Random(seed)
    return (f'<svg viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0;width:{w}px" xmlns="http://www.w3.org/2000/svg">'
            + "".join(f'<circle cx="{r.randint(10,w-10)}" cy="{r.randint(10,h-10)}" r="{r.choice([1.5,2,2.5,3])}" fill="#fff" opacity="{r.choice([.35,.6,.9])}"/>' for _ in range(n)) + "</svg>")

def icon(kind, s=64, col="#fff"):
    """hospital (building with a cross) or clinic (shop front with awning), on a coloured disc."""
    if kind == "hosp":
        body = ('<rect x="16" y="20" width="32" height="32" rx="3" fill="#fff"/><rect x="27" y="26" width="10" height="20" fill="{c}"/><rect x="22" y="31" width="20" height="10" fill="{c}"/>'
                '<rect x="20" y="14" width="24" height="8" rx="2" fill="#fff"/>')
    else:
        body = ('<rect x="14" y="30" width="36" height="22" rx="2" fill="#fff"/><path d="M12 22 H52 L48 32 H16 Z" fill="#fff"/>'
                '<path d="M16 32 q4 5 8 0 q4 5 8 0 q4 5 8 0 q4 5 8 0" fill="none" stroke="{c}" stroke-width="2.5"/><rect x="28" y="38" width="9" height="14" fill="{c}"/>')
    return f'<svg viewBox="0 0 64 64" style="width:{s}px;height:{s}px;flex:none"><circle cx="32" cy="32" r="32" fill="{col}"/>{body.replace("{c}", col)}</svg>'

def portrait(s=200, ring=GOLD):
    return (f'<div style="width:{s}px;height:{s}px;border-radius:50%;padding:8px;background:{ring};box-shadow:0 18px 40px rgba(0,0,0,.35);flex:none">'
            f'<img src="{PHOTO}" style="width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 18%"></div>')

# ---------------- building blocks ----------------
def hf(lang): return "TD" if lang == "hi" else "YS"

def ticket(lang, days, rows, col, size=1.0):
    """A bold ticket: the days in big letters, then one or two place rows with times."""
    X = T[lang]; s = size
    rr = ""
    for i, (kind, (name, area, time)) in enumerate(rows):
        if i:
            rr += (f'<div style="display:flex;align-items:center;gap:{int(14*s)}px;margin:{int(4*s)}px 0 {int(4*s)}px {int(30*s)}px;color:{col};font-weight:600;font-size:{int(24*s)}px">'
                   f'<span style="width:4px;height:{int(26*s)}px;background:{col};border-radius:2px"></span>{X["then"]}</div>')
        c = TEAL if kind == "hosp" else (PLUM if "6:30" in time else SAFF)
        rr += (f'<div style="display:flex;align-items:center;gap:{int(22*s)}px">{icon(kind, int(76*s), c)}'
               f'<div style="flex:1;min-width:0"><div style="font-family:{hf(lang)};font-size:{int(46*s)}px;line-height:1.1;color:#12302C">{name}</div>'
               f'<div style="font-size:{int(26*s)}px;color:#4A615D">{area}</div></div>'
               f'<div style="font-family:{hf(lang)};font-size:{int(52*s)}px;color:{c};white-space:nowrap">{time}</div></div>')
    return (f'<div style="background:#fff;border-radius:{int(40*s)}px;overflow:hidden;box-shadow:0 20px 50px rgba(18,48,44,.18)">'
            f'<div style="background:{col};color:#fff;padding:{int(18*s)}px {int(34*s)}px;font-weight:600;letter-spacing:.08em;font-size:{int(44*s)}px">{days}</div>'
            f'<div style="padding:{int(26*s)}px {int(34*s)}px">{rr}</div></div>')

def week_tickets(lang, s=1.0, gap=28):
    X = T[lang]
    return (ticket(lang, X["mwf"], [("clinic", X["ac"])], SAFF, s) + f'<div style="height:{gap}px"></div>'
            + ticket(lang, X["tts"], [("hosp", X["ah"]), ("clinic", X["ar"])], TEAL, s))

def hero(lang, H=1350, clock_w=430, h1=96, story=False):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s{hi}" style="width:1080px;height:{H}px;{DUSK};padding:{150 if story else 80}px 80px 0">
 {stars()}
 <div style="position:relative">
  <div class="kick" style="display:inline-block;background:{GOLD};color:#12302C;border-radius:999px;padding:12px 28px;font-size:28px">{X["kick"]}</div>
  <h1 style="font-size:{h1}px;margin-top:26px;max-width:920px;color:#fff">{X["h1"]}</h1>
  <p style="font-size:34px;color:#F6DCC8;margin-top:18px;max-width:900px">{X["sub"]}</p></div>
 <div style="position:absolute;left:{560 if not story else 540}px;top:{H*0.33 if not story else 560}px">{clock(clock_w, lang)}</div>
 <div style="position:absolute;left:90px;top:{H*0.40 if not story else 640}px;display:flex;flex-direction:column;align-items:flex-start;gap:14px">
  {portrait(230)}<div style="font-family:YS;font-size:34px;color:#fff;margin-top:6px">{"Dr. Kshitij Lochab" if lang == "en" else "डॉ. क्षितिज लोचब"}</div>
  <div style="font-size:24px;color:#F6DCC8">{"Gastroenterologist · Gurugram" if lang == "en" else "गैस्ट्रोएंटेरोलॉजिस्ट · गुरुग्राम"}</div></div>
 <div style="position:absolute;left:0;right:0;bottom:130px">{skyline()}</div>
 <div style="position:absolute;left:0;right:0;bottom:0;height:130px;background:#120E26"></div>"""

# ---------------- Instagram carousel (3 slides) ----------------
def s1(lang):
    X = T[lang]
    return hero(lang, h1=96 if lang == "en" else 80) + f"""
 <div style="position:absolute;right:80px;bottom:360px;font-weight:600;font-size:32px;color:#fff;background:rgba(18,14,38,.55);padding:12px 26px;border-radius:999px">{X["swipe"]}</div>
 {foot(1, total=3, light=True, hi=lang == "hi")}</div>"""

def s2(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s cream{hi}" style="width:1080px;height:1350px;padding:80px 80px">
 <div class="kick" style="font-size:28px;color:#C2551F">{X["wk"]}</div>
 <h1 style="font-size:{92 if lang == "en" else 80}px;margin:8px 0 40px">{X["wk_h"]}</h1>
 {week_tickets(lang, 1.14, 34)}
 <div style="margin-top:40px;display:inline-flex;align-items:center;gap:16px;font-size:30px;color:#4A615D;background:#EFE6D6;border-radius:999px;padding:12px 28px">
  <svg viewBox="0 0 24 24" style="width:30px;height:30px"><path d="M15 3a9 9 0 1 0 6 15.7A8 8 0 0 1 15 3z" fill="#4A615D"/></svg>{X["sun"]}</div>
 {foot(2, total=3, hi=lang == "hi")}</div>"""

def noon_hospital(w=520):
    """The midday sun high over a hospital with a red cross and an ambulance-free calm street (viewBox 0 0 520 420)."""
    rays = "".join(f'<line x1="{400+70*__import__("math").cos(a):.0f}" y1="{90+70*__import__("math").sin(a):.0f}" x2="{400+100*__import__("math").cos(a):.0f}" y2="{90+100*__import__("math").sin(a):.0f}" stroke="#F3B84A" stroke-width="8" stroke-linecap="round"/>'
                   for a in [i * 0.785 for i in range(8)])
    win = "".join(f'<rect x="{x}" y="{y}" width="26" height="30" rx="3" fill="#BFE3F0"/>' for x in (120, 170, 300, 350) for y in (200, 260, 320))
    return f"""<svg viewBox="0 0 520 420" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<circle cx="400" cy="90" r="54" fill="#F3B84A"/>{rays}
<rect x="90" y="160" width="340" height="250" rx="12" fill="#FFFFFF" stroke="#12302C" stroke-width="6"/>
<rect x="200" y="110" width="120" height="300" rx="10" fill="#FFFFFF" stroke="#12302C" stroke-width="6"/>
<rect x="245" y="128" width="30" height="80" rx="4" fill="#B0362B"/><rect x="220" y="153" width="80" height="30" rx="4" fill="#B0362B"/>
{win}<rect x="236" y="330" width="48" height="80" rx="6" fill="#0D7466"/>
<rect x="40" y="406" width="440" height="10" rx="5" fill="#12302C"/></svg>"""

def s3(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s rose{hi}" style="width:1080px;height:1350px;padding:80px 80px">
 <div class="kick" style="font-size:30px;color:#B0362B">{X["urg_k"]}</div>
 <h1 style="font-size:{90 if lang == "en" else 78}px;margin-top:10px">{X["urg_h"]}</h1>
 <div style="position:absolute;left:280px;top:330px">{noon_hospital(520)}</div>
 <p style="position:absolute;left:80px;right:80px;top:790px;font-size:36px;line-height:1.4">{X["urg_p"]}</p>
 <div style="position:absolute;left:80px;right:80px;top:990px;display:flex;gap:22px;align-items:center;background:#12302C;border-radius:999px;padding:18px 18px 18px 40px">
  <div style="flex:1"><div style="font-size:26px;color:#CFE5E0">{X["cta"]}</div><div style="font-family:YS;font-size:54px;color:#fff;letter-spacing:.01em">{X["num"]}</div></div>
  <div style="background:{GOLD};color:#12302C;font-family:YS;font-size:36px;padding:18px 30px;border-radius:999px">{X["site"]}</div></div>
 <p style="position:absolute;left:80px;right:80px;top:1150px;font-size:28px;color:#B0362B;font-weight:600">{X["emerg"]}</p>
 {foot(3, total=3, hi=lang == "hi")}</div>"""

# ---------------- Story / WhatsApp Status (1080x1920) ----------------
def story(lang):
    X = T[lang]; hi = " hi" if lang == "hi" else ""
    return f"""<div class="s{hi}" style="width:1080px;height:1920px;{DUSK}">
 {stars(30, 1080, 700)}
 <div style="position:absolute;left:80px;right:80px;top:130px">
  <div class="kick" style="display:inline-block;background:{GOLD};color:#12302C;border-radius:999px;padding:12px 28px;font-size:30px">{X["kick"]}</div>
  <h1 style="font-size:{92 if lang == "en" else 78}px;margin-top:22px;color:#fff">{X["h1"]}</h1></div>
 <div style="position:absolute;left:0;right:0;top:690px">{skyline(1080, 230, glow=True)}</div>
 <div style="position:absolute;left:90px;top:{390 if lang == "en" else 400}px;display:flex;align-items:center;gap:60px;z-index:2">{portrait(210)}{clock(320, lang)}</div>
 <div style="position:absolute;left:0;right:0;top:914px;bottom:0;background:#FBF5EA"></div>
 <div style="position:absolute;left:60px;right:60px;top:960px">{week_tickets(lang, .9, 22)}</div>
 <div style="position:absolute;left:60px;right:60px;top:1580px;display:flex;gap:18px;align-items:center;background:#F8E4E1;border-radius:28px;padding:18px 26px">
  <svg viewBox="0 0 48 48" style="width:56px;height:56px;flex:none"><circle cx="24" cy="24" r="22" fill="#B0362B"/><path d="M24 12v16" stroke="#fff" stroke-width="5" stroke-linecap="round"/><circle cx="24" cy="35" r="3" fill="#fff"/></svg>
  <div style="font-size:29px;line-height:1.3;color:#12302C"><b style="color:#B0362B">{X["urg_k"]}</b> {"Apollo Hospitals only. Call or WhatsApp first." if lang == "en" else "सिर्फ़ अपोलो हॉस्पिटल्स। पहले कॉल या WhatsApp करें।"}</div></div>
 <div style="position:absolute;left:0;right:0;top:1720px;text-align:center"><span style="background:#12302C;color:#fff;font-family:YS;font-size:46px;padding:14px 36px;border-radius:999px">{X["num"]} · {X["site"]}</span></div>
 {foot(pad=60, hi=lang == "hi", size=.8)}</div>"""

# ---------------- Google Business Profile (1200x900) ----------------
def gbp():
    X = T["en"]
    return f"""<div class="s" style="width:1200px;height:900px;{DUSK}">
 {stars(20, 1200, 400)}
 <div style="position:absolute;left:60px;top:56px;width:520px">
  <div class="kick" style="display:inline-block;background:{GOLD};color:#12302C;border-radius:999px;padding:10px 24px;font-size:22px">{X["kick"]}</div>
  <h1 style="font-size:64px;margin-top:18px;color:#fff">{X["h1"]}</h1>
  <p style="font-size:24px;color:#F6DCC8;margin-top:12px">Every evening · Monday to Saturday</p></div>
 <div style="position:absolute;left:70px;top:360px;display:flex;align-items:center;gap:20px">{portrait(150)}{clock(230)}</div>
 <div style="position:absolute;left:0;width:620px;bottom:0">{skyline(620, 220)}</div>
 <div style="position:absolute;right:50px;top:50px;width:540px">{week_tickets("en", .62, 16)}
  <div style="margin-top:16px;background:#F8E4E1;border-radius:22px;padding:14px 20px;font-size:21px;line-height:1.3;color:#12302C"><b style="color:#B0362B">Urgent during the day?</b> Apollo Hospitals only. Call or WhatsApp first.</div>
  <div style="margin-top:14px;font-size:20px;color:#fff;opacity:.9">Sunday: no OPD</div>
  <div style="margin-top:26px;display:flex;align-items:center;gap:14px"><img src="{__import__('week_2026_10_12').LOGO}" style="width:56px;height:56px">
   <div><div style="font-family:YS;font-size:26px;color:#fff">Dr. Kshitij Lochab</div><div style="font-size:18px;color:#F6DCC8">Gastroenterologist · drlochab.com</div></div></div></div>
 </div>"""

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for lang in ("en", "hi"):
            for i, f in enumerate([s1, s2, s3], 1):
                w9.render(lambda: f(lang), 1080, 1350, f"{OUT}/ig-timings-{lang}-{i}.png", b)
            w9.render(lambda: story(lang), 1080, 1920, f"{OUT}/story-status-timings-{lang}.png", b)
        w9.render(gbp, 1200, 900, f"{OUT}/google-business-timings.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=93); os.remove(f"{OUT}/{f}")
    print("done", sorted(os.listdir(OUT)))
