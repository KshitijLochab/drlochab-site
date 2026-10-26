"""'The smart mithai box': Diwali 2026 food guide promo (26 Oct 2026).
New visual format (asked for after the teal cards and the breaking-news set felt monotonous): a top-down illustrated
mithai box in maroon and gold foil, six compartments, each a drawn sweet or snack with one tip from diwali_guide.py.
No photo of the doctor (NMC 2026, clause 9.2); name, qualifications and registration go in the captions; AI line kept subtle.
Instagram post (1080x1350), Instagram story (1080x1920, space for a link sticker), WhatsApp status EN + HI (1080x1920),
Google Business image (1200x900).
Run: python3 _src/social/diwali_mithai_box.py  -> _src/out/diwali-mithai-box/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS as BASE_CSS, SRC, LOGO
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "diwali-mithai-box"); os.makedirs(OUT, exist_ok=True)
GOLD, GOLD2, MAROON, CREAM, INK = "#F3C969", "#C9963B", "#4A0A27", "#FFF5E3", "#4A0A27"
AI = {"en": "Prepared with AI assistance and reviewed by Dr. Kshitij Lochab.", "hi": "AI की सहायता से तैयार और डॉ. क्षितिज लोचब द्वारा समीक्षित।"}

CSS = BASE_CSS + f"""
@font-face{{font-family:"FV";src:url("file://{SRC}/fonts/Figtree.ttf");font-weight:300 900}}
*{{box-sizing:border-box;margin:0}}
.bg{{position:relative;overflow:hidden;color:{CREAM};font-family:"FV","FT",sans-serif;
 background:radial-gradient(70% 45% at 50% 0%,#8A1745 0%,rgba(138,23,69,0) 70%),radial-gradient(60% 40% at 50% 100%,#6B1035 0%,rgba(107,16,53,0) 70%),linear-gradient(180deg,#3E0820,#2A0515)}}
.hi{{font-family:"MK","FV",sans-serif}}
.pat{{position:absolute;inset:0;opacity:.13}}
.kick{{display:inline-flex;align-items:center;gap:14px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:{GOLD}}}
.hi .kick{{letter-spacing:.02em}}
.kick i{{display:block;width:60px;height:2px;background:{GOLD}}}
.h1{{font-family:"YS";color:{GOLD};line-height:.98;letter-spacing:-.01em;text-shadow:0 4px 0 rgba(0,0,0,.25)}}
.hi .h1{{font-family:"TD";line-height:1.15;letter-spacing:0}}
.sub{{color:#F7DCC0;font-weight:600}}
.box{{position:relative;border-radius:34px;padding:22px;
 background:linear-gradient(145deg,#D0245F,#A5164B 55%,#86103C);
 box-shadow:0 40px 80px rgba(0,0,0,.5),inset 0 0 0 4px {GOLD2},inset 0 0 0 10px #B81B53,inset 0 0 0 12px {GOLD}}}
.tray{{display:grid;gap:16px;padding:18px;border-radius:22px;background:#6E0D35;box-shadow:inset 0 6px 18px rgba(0,0,0,.45)}}
.cell{{position:relative;border-radius:18px;background:{CREAM};color:{INK};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
 box-shadow:inset 0 0 0 7px #F8E6C6,inset 0 0 0 9px rgba(201,150,59,.45),0 3px 0 rgba(0,0,0,.25);
 background-image:repeating-conic-gradient(from 0deg at 50% 38%,rgba(201,150,59,.07) 0 4deg,rgba(255,255,255,0) 4deg 8deg)}}
.cell .n{{position:absolute;top:14px;left:14px;border-radius:50%;background:{MAROON};color:{GOLD};font-weight:900;display:flex;align-items:center;justify-content:center}}
.cell b{{display:block;font-weight:900;line-height:1.08}}
.cell span{{display:block;font-weight:500;line-height:1.25;color:#6B2A45}}
.hi .cell b{{font-weight:600}}
.tag{{position:absolute;left:50%;transform:translateX(-50%) rotate(-2deg);background:linear-gradient(180deg,#F8D987,{GOLD2});color:{MAROON};
 font-family:"YS";padding:10px 30px;border-radius:10px;box-shadow:0 8px 16px rgba(0,0,0,.35);white-space:nowrap}}
.hi .tag{{font-family:"TD"}}
.tag:before{{content:"";position:absolute;left:-14px;top:50%;width:12px;height:12px;margin-top:-6px;border-radius:50%;background:{MAROON};box-shadow:0 0 0 3px {GOLD2}}}
.pill{{display:inline-flex;align-items:center;gap:16px;border-radius:999px;background:{GOLD};color:{MAROON};font-weight:800}}
.warn{{border-radius:22px;border:2px solid rgba(243,201,105,.55);background:rgba(0,0,0,.22);display:flex;gap:20px;align-items:flex-start;color:#FBE7D0}}
.ai{{color:rgba(247,220,192,.55)}}
"""

DEFS = f"""<svg width="0" height="0" style="position:absolute"><defs>
<linearGradient id="silver" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFDF8"/><stop offset=".55" stop-color="#EDE6D8"/><stop offset="1" stop-color="#CFC6B4"/></linearGradient>
<radialGradient id="ladoo" cx=".38" cy=".35" r=".7"><stop offset="0" stop-color="#FFD27A"/><stop offset=".6" stop-color="#F0A132"/><stop offset="1" stop-color="#C9711A"/></radialGradient>
<radialGradient id="katori" cx=".5" cy=".5" r=".55"><stop offset=".78" stop-color="#E9C27A"/><stop offset=".9" stop-color="#B98A3E"/><stop offset="1" stop-color="#8E6528"/></radialGradient>
<radialGradient id="glass" cx=".45" cy=".42" r=".6"><stop offset="0" stop-color="#FAFBD8"/><stop offset=".85" stop-color="#E6EFB0"/><stop offset="1" stop-color="#C9D98A"/></radialGradient>
<radialGradient id="flame" cx=".5" cy=".7" r=".6"><stop offset="0" stop-color="#FFF6C8"/><stop offset=".5" stop-color="#FFC53D"/><stop offset="1" stop-color="#F06B1A"/></radialGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFC94D" stop-opacity=".55"/><stop offset="1" stop-color="#FFC94D" stop-opacity="0"/></radialGradient>
<linearGradient id="clay" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E0793A"/><stop offset="1" stop-color="#9C3F14"/></linearGradient>
<linearGradient id="pbox" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8417A"/><stop offset="1" stop-color="#A3164A"/></linearGradient>
<pattern id="jaali" width="90" height="90" patternUnits="userSpaceOnUse">
 <path d="M45 8 L50 40 L82 45 L50 50 L45 82 L40 50 L8 45 L40 40 Z" fill="{GOLD}"/><circle cx="0" cy="0" r="4" fill="{GOLD}"/><circle cx="90" cy="0" r="4" fill="{GOLD}"/><circle cx="0" cy="90" r="4" fill="{GOLD}"/><circle cx="90" cy="90" r="4" fill="{GOLD}"/>
</pattern></defs></svg>"""

def pattern():
    return '<svg class="pat" width="100%" height="100%"><rect width="100%" height="100%" fill="url(#jaali)"/></svg>'

def diya(s=120, style=""):
    return (f'<svg viewBox="0 0 120 120" style="width:{s}px;height:{s}px;position:absolute;{style}">'
            '<circle cx="60" cy="52" r="52" fill="url(#glow)"/>'
            '<path d="M60 18 C70 34 72 46 60 58 C48 46 50 34 60 18 Z" fill="url(#flame)"/>'
            '<path d="M14 66 Q60 58 106 66 Q100 98 60 102 Q20 98 14 66 Z" fill="url(#clay)"/>'
            f'<path d="M14 66 Q60 74 106 66" fill="none" stroke="{GOLD}" stroke-width="3"/>'
            f'<g fill="{GOLD}"><circle cx="40" cy="84" r="3"/><circle cx="60" cy="88" r="3"/><circle cx="80" cy="84" r="3"/></g></svg>')

def spark(x, y, s=26, op=.9):
    return (f'<svg viewBox="0 0 20 20" style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;opacity:{op}">'
            f'<path d="M10 0 L12 8 L20 10 L12 12 L10 20 L8 12 L0 10 L8 8 Z" fill="{GOLD}"/></svg>')

# ---- the six sweets / snacks (viewBox 200x140) ----
def ic_katli():
    d = lambda cx, cy, r: f'{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}'
    return (f'<polygon points="{d(80,72,52)}" fill="url(#silver)" stroke="#BDB29C" stroke-width="3"/>'
            f'<polygon points="{d(80,72,40)}" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>'
            f'<polygon points="{d(128,76,46)}" fill="url(#silver)" stroke="#BDB29C" stroke-width="3"/>'
            f'<polygon points="{d(128,76,35)}" fill="none" stroke="#fff" stroke-width="2" opacity=".8"/>'
            '<path d="M112 58 l6 -3 M140 92 l7 -4 M70 54 l5 -3" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
            f'<path d="M170 22 L173 31 L182 34 L173 37 L170 46 L167 37 L158 34 L167 31 Z" fill="{GOLD2}"/>')

def ic_ladoo():
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="3.2" fill="#B8641A" opacity=".55"/>' for x, y in
                   [(70,50),(92,40),(110,58),(80,78),(104,92),(126,74),(66,96),(94,110),(118,44),(130,98),(84,60),(100,74)])
    lite = "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#FFE6A8"/>' for x, y in [(78,44),(100,52),(88,90),(116,84),(74,70)])
    return (f'<ellipse cx="98" cy="128" rx="52" ry="8" fill="rgba(74,10,39,.12)"/><circle cx="98" cy="74" r="54" fill="url(#ladoo)"/>{dots}{lite}'
            '<g transform="translate(150 18)"><path d="M18 0 C28 16 34 24 34 33 A16 16 0 0 1 2 33 C2 24 8 16 18 0 Z" fill="#D7263D"/>'
            '<path d="M11 32 h14 M18 25 v14" stroke="#fff" stroke-width="4" stroke-linecap="round"/></g>')

def ic_katori():
    mk = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r}" ry="{r*.86:.1f}" fill="#FFFBF2" stroke="#D9C39C" stroke-width="2"/><ellipse cx="{x-3}" cy="{y-3}" rx="{r*.35:.1f}" ry="{r*.25:.1f}" fill="#EFE2C8"/>'
                 for x, y, r in [(84,52,15),(110,48,14),(70,76,14),(98,74,15),(124,70,14),(86,100,13)])
    ch = "".join(f'<circle cx="{x}" cy="{y}" r="7.5" fill="#A8622C" stroke="#7C4419" stroke-width="2"/>' for x, y in [(116,96),(132,92),(106,106),(60,58),(130,48)])
    return f'<circle cx="100" cy="74" r="66" fill="url(#katori)"/><circle cx="100" cy="74" r="54" fill="#F3DDB0"/>{mk}{ch}'

def ic_glass():
    seg = "".join(f'<line x1="78" y1="70" x2="{78+28*__import__("math").cos(a*0.785):.1f}" y2="{70+28*__import__("math").sin(a*0.785):.1f}" stroke="#FFF7C2" stroke-width="3"/>' for a in range(8))
    return ('<circle cx="100" cy="72" r="64" fill="#E7F3F5" stroke="#B9D5DA" stroke-width="4"/><circle cx="100" cy="72" r="54" fill="url(#glass)"/>'
            f'<circle cx="78" cy="70" r="31" fill="#F7D530" stroke="#E2B714" stroke-width="3"/><circle cx="78" cy="70" r="25" fill="#FBE36A"/>{seg}'
            '<rect x="112" y="40" width="26" height="26" rx="6" fill="#fff" opacity=".75" transform="rotate(14 125 53)"/>'
            '<rect x="118" y="78" width="22" height="22" rx="6" fill="#fff" opacity=".7" transform="rotate(-10 129 89)"/>'
            '<ellipse cx="106" cy="104" rx="15" ry="7" fill="#3E9B4F" transform="rotate(-30 106 104)"/><ellipse cx="122" cy="110" rx="13" ry="6" fill="#56B867" transform="rotate(20 122 110)"/>'
            '<line x1="146" y1="20" x2="112" y2="66" stroke="#E64A7B" stroke-width="7" stroke-linecap="round"/>')

def ic_clock():
    ticks = "".join(f'<line x1="{100+48*__import__("math").cos(a*0.5236):.1f}" y1="{72+48*__import__("math").sin(a*0.5236):.1f}" x2="{100+42*__import__("math").cos(a*0.5236):.1f}" y2="{72+42*__import__("math").sin(a*0.5236):.1f}" stroke="{MAROON}" stroke-width="{5 if a % 3 == 0 else 2.5}" stroke-linecap="round"/>' for a in range(12))
    return (f'<circle cx="100" cy="72" r="62" fill="{GOLD}" stroke="{GOLD2}" stroke-width="4"/><circle cx="100" cy="72" r="54" fill="#FFFBF0"/>{ticks}'
            f'<line x1="100" y1="72" x2="66" y2="72" stroke="{MAROON}" stroke-width="8" stroke-linecap="round"/>'
            f'<line x1="100" y1="72" x2="100" y2="32" stroke="{MAROON}" stroke-width="5" stroke-linecap="round"/><circle cx="100" cy="72" r="6" fill="#D7263D"/>'
            '<path d="M168 20 A18 18 0 1 0 184 48 A14 14 0 1 1 168 20 Z" fill="#F0B43C"/>'
            '<g fill="#B98A3E" opacity=".8"><ellipse cx="30" cy="112" rx="7" ry="11" transform="rotate(-15 30 112)"/><ellipse cx="44" cy="96" rx="7" ry="11" transform="rotate(-15 44 96)"/></g>')

def ic_fresh():
    return ('<rect x="40" y="58" width="104" height="66" rx="8" fill="url(#pbox)"/><rect x="34" y="44" width="116" height="22" rx="6" fill="#F05C8E"/>'
            f'<rect x="85" y="44" width="14" height="80" fill="{GOLD}"/><path d="M92 44 C72 22 60 34 78 44 Z M92 44 C112 22 124 34 106 44 Z" fill="{GOLD}" stroke="{GOLD2}" stroke-width="2"/>'
            '<rect x="50" y="84" width="28" height="22" rx="4" fill="#FFF5E3"/><path d="M55 95 l6 6 l12 -13" fill="none" stroke="#2E8B57" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
            '<g transform="translate(160 40)"><circle r="30" fill="#DDF1FB" stroke="#5AB0DA" stroke-width="3"/>'
            '<g stroke="#2E86C1" stroke-width="4" stroke-linecap="round"><line x1="0" y1="-18" x2="0" y2="18"/><line x1="-15.6" y1="-9" x2="15.6" y2="9"/><line x1="-15.6" y1="9" x2="15.6" y2="-9"/>'
            '<path d="M-5 -14 L0 -9 L5 -14 M-5 14 L0 9 L5 14" fill="none" stroke-width="3"/></g></g>')

ICONS = [ic_katli, ic_ladoo, ic_katori, ic_glass, ic_clock, ic_fresh]

TIPS = {
 "en": [("1–2 pieces", "after a meal, never on an empty stomach"), ("Diabetes?", "a small piece after food, check sugar more often"),
        ("Roasted, not fried", "makhana and chana over namkeen"), ("Nimbu paani", "over colas and binge drinking"),
        ("Dinner by 9 pm", "then a 15-minute walk"), ("Buy fresh, keep cold", "licensed shop, fridge within 2\u00a0hours")],
 "hi": [("1–2 पीस", "खाने के बाद, खाली पेट कभी नहीं"), ("डायबिटीज़ है?", "खाने के बाद छोटा पीस, शुगर बार-बार जाँचें"),
        ("भुना, तला नहीं", "नमकीन की जगह मखाना और चना"), ("नींबू पानी", "कोल्ड ड्रिंक और ज़्यादा शराब की जगह"),
        ("रात 9 बजे तक खाना", "फिर 15 मिनट टहलें"), ("ताज़ा ख़रीदें, ठंडा रखें", "लाइसेंस वाली दुकान, 2 घंटे में फ्रिज")],
}
TXT = {
 "en": dict(kick="Diwali · 8 Nov 2026", h1="The smart<br>mithai box", sub="6 ways to enjoy Diwali without acidity", tag="Happy Diwali",
            pill="Free Diwali food guide", url="drlochab.com", warn_b="Not just acidity:",
            warn="severe upper belly pain going to the back, with vomiting, after a party needs the emergency department."),
 "hi": dict(kick="दिवाली · 8 नवंबर 2026", h1="सेहत वाला<br>मिठाई का डिब्बा", sub="बिना एसिडिटी के दिवाली मनाने के 6 तरीके", tag="शुभ दीपावली",
            pill="दिवाली की मुफ़्त फ़ूड गाइड", url="drlochab.com/hi", warn_b="यह सिर्फ़ एसिडिटी नहीं:",
            warn="पार्टी के बाद पेट के ऊपरी हिस्से में तेज़ दर्द जो पीठ तक जाए, साथ में उल्टी, तो तुरंत इमरजेंसी जाएँ।"),
}

def brand(lang, size=1.0):
    hi = lang == "hi"
    name = "डॉ. क्षितिज लोचब" if hi else "Dr. Kshitij Lochab"
    sub = "गैस्ट्रोएंटेरोलॉजिस्ट, गुरुग्राम" if hi else "Gastroenterologist, Gurugram"
    return (f'<div style="display:flex;align-items:center;gap:{int(14*size)}px"><img src="{LOGO}" style="width:{int(58*size)}px;height:{int(58*size)}px;border-radius:50%;background:{CREAM}">'
            f'<div><div style="font-family:{"TD" if hi else "YS"};font-size:{int(29*size)}px;color:{CREAM};line-height:1.1">{name}</div>'
            f'<div style="font-size:{int(20*size)}px;color:#E9C7A6">{sub}</div></div></div>')

def cell(i, lang, w, h, icon_h, fb, fs, show_sub=True):
    t, s = TIPS[lang][i]
    sub = f'<span style="font-size:{fs}px;margin-top:6px">{s}</span>' if show_sub else ""
    nsz = int(fb * 1.15)
    return (f'<div class="cell" style="width:{w}px;height:{h}px;padding:{int(h*.05)}px {int(w*.07)}px">'
            f'<div class="n" style="width:{nsz}px;height:{nsz}px;font-size:{int(nsz*.55)}px">{i+1}</div>'
            f'<svg viewBox="0 0 200 140" style="width:{int(icon_h*200/140)}px;height:{icon_h}px;flex:none">{ICONS[i]()}</svg>'
            f'<b style="font-size:{fb}px;margin-top:{int(h*.035)}px">{t}</b>{sub}</div>')

def box(lang, cols, w, h, icon_h, fb, fs, tag_fs, show_sub=True):
    cells = "".join(cell(i, lang, w, h, icon_h, fb, fs, show_sub) for i in range(6))
    return (f'<div class="box"><div class="tag" style="top:-{int(tag_fs*1.1)}px;font-size:{tag_fs}px">{TXT[lang]["tag"]}</div>'
            f'<div class="tray" style="grid-template-columns:repeat({cols},{w}px)">{cells}</div></div>')

def pill(lang, fs):
    x = TXT[lang]
    arrow = f'<svg viewBox="0 0 24 24" style="width:{fs}px;height:{fs}px"><path d="M4 12h14M12 5l7 7-7 7" fill="none" stroke="{MAROON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    return f'<div class="pill" style="padding:{int(fs*.55)}px {int(fs*1.1)}px;font-size:{fs}px">{x["pill"]} {arrow} {x["url"]}</div>'

def post(lang="en"):
    x = TXT[lang]
    return f"""<div class="bg {lang}" style="width:1080px;height:1350px;padding:58px 64px 0">{DEFS}{pattern()}
 {diya(150, "right:40px;top:30px")}{spark(880, 210, 30)}{spark(820, 60, 18, .7)}{spark(60, 1180, 22, .6)}
 <div class="kick" style="font-size:24px"><i></i>{x["kick"]}</div>
 <div class="h1" style="font-size:{104 if lang == "en" else 84}px;margin-top:18px">{x["h1"]}</div>
 <div class="sub" style="font-size:32px;margin-top:16px">{x["sub"]}</div>
 <div style="position:absolute;left:64px;top:414px">{box(lang, 3, 284, 330, 118, 30, 21, 30)}</div>
 <div style="position:absolute;left:64px;right:64px;bottom:46px;display:flex;justify-content:space-between;align-items:center">
  {brand(lang, .95)}{pill(lang, 25)}</div>
 <div class="ai" style="position:absolute;left:0;right:0;bottom:14px;text-align:center;font-size:15px">{AI[lang]}</div></div>"""

def tall(lang="en", sticker=False):
    x = TXT[lang]
    warn_ic = '<svg viewBox="0 0 24 24" style="width:44px;height:44px;flex:none"><path d="M12 2 L23 21 H1 Z" fill="#FF6B5A"/><rect x="11" y="9" width="2.4" height="6.5" rx="1.2" fill="#fff"/><circle cx="12.2" cy="18" r="1.4" fill="#fff"/></svg>'
    gap = '<div style="height:150px"></div>' if sticker else f'<div style="margin-top:44px;display:flex;justify-content:center">{pill(lang, 34)}</div>'
    return f"""<div class="bg {lang}" style="width:1080px;height:1920px;padding:110px 70px 0">{DEFS}{pattern()}
 {diya(180, "right:50px;top:80px")}{spark(860, 330, 34)}{spark(780, 130, 20, .7)}{spark(980, 1700, 24, .6)}
 <div class="kick" style="font-size:28px"><i></i>{x["kick"]}</div>
 <div class="h1" style="font-size:{124 if lang == "en" else 100}px;margin-top:22px">{x["h1"]}</div>
 <div class="sub" style="font-size:38px;margin-top:20px">{x["sub"]}</div>
 <div style="margin-top:64px">{box(lang, 2, 434, 268, 108, 35, 24, 34)}</div>
 {gap}
 <div class="warn" style="position:absolute;left:70px;right:70px;bottom:166px;padding:20px 26px;font-size:26px;line-height:1.35">{warn_ic}<div><b style="color:{GOLD}">{x["warn_b"]}</b> {x["warn"]}</div></div>
 <div style="position:absolute;left:70px;right:70px;bottom:68px">{brand(lang, 1.0)}</div>
 <div class="ai" style="position:absolute;left:70px;right:70px;bottom:34px;font-size:17px">{AI[lang]}</div></div>"""

def gbp():
    x = TXT["en"]
    return f"""<div class="bg en" style="width:1200px;height:900px;padding:60px 0 0 60px">{DEFS}{pattern()}
 {diya(110, "left:50px;top:430px")}{spark(330, 300, 22)}
 <div class="kick" style="font-size:20px"><i style="width:40px"></i>{x["kick"]}</div>
 <div class="h1" style="font-size:70px;margin-top:20px">The smart<br>mithai<br>box</div>
 <div class="sub" style="font-size:25px;margin-top:18px;width:350px;line-height:1.3">{x["sub"]}</div>
 <div style="position:absolute;left:60px;bottom:130px;width:350px;font-size:21px;line-height:1.4;color:#F7DCC0">Sweets, snacks, alcohol and food safety: the free festival guide, in English and Hindi.</div>
 <div style="position:absolute;left:60px;bottom:56px">{brand("en", .9)}</div>
 <div style="position:absolute;right:40px;top:96px">{box("en", 3, 196, 320, 100, 24, 17, 26)}</div></div>"""

def render(html, w, h, path, b):
    pg = b.new_page(viewport={"width": w, "height": h})
    tmp = f"{OUT}/tmp.html"
    open(tmp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
    pg.goto(f"file://{tmp}"); pg.wait_for_timeout(700); pg.screenshot(path=path); pg.close()

CRED_EN = "Dr. Kshitij Lochab, MBBS, MD (Internal Medicine), DrNB (Gastroenterology), Advanced Fellowship in EUS & ERCP · Haryana Medical Council Reg. No. HN-23524"
CRED_HI = "डॉ. क्षितिज लोचब, MBBS, MD (इंटरनल मेडिसिन), DrNB (गैस्ट्रोएंटेरोलॉजी), EUS और ERCP में एडवांस्ड फ़ेलोशिप · हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524"
GUIDE_EN, GUIDE_HI = "https://drlochab.com/guides/diwali-food-guide/", "https://drlochab.com/hi/guides/diwali-food-guide/"

CAPTION = f"""The smart mithai box 🪔 6 ways to enjoy Diwali without acidity

Every Diwali week, gastroenterologists see more acidity, bloating, loose motions from stale sweets, gallstone attacks and pancreatitis. A few habits keep the festival fun:

1️⃣ One or two pieces of mithai, after a meal. Never sweets on an empty stomach.
2️⃣ Diabetes? A small piece after food, check your sugar more often, and don't skip your medicines. "Sugar-free" sweets still have fat and calories.
3️⃣ Roasted makhana and chana instead of fried namkeen again and again.
4️⃣ Nimbu paani, chaas or water instead of colas. Avoid binge drinking (4 or more drinks at a sitting), and no alcohol at all with fatty liver, other liver disease or past pancreatitis.
5️⃣ Festive dinner by about 9 pm, a 15-minute walk after, and no lying down for 2 to 3 hours.
6️⃣ Khoya, paneer and milk sweets from licensed shops (check the FSSAI number and best-before date), in the fridge within 2 hours, eaten within 2 to 3 days.

⚠️ Severe upper belly pain going to the back, with vomiting, after a party is not "just acidity". Go to the emergency department.

The full Diwali food guide (food safety, a simple Diwali day plan, and who should plan ahead) is free on the website, in English and Hindi.
Link in bio 👉 drlochab.com

Save this for Diwali week and share it with the family 🪔

#Diwali2026 #HappyDiwali #DiwaliFood #Acidity #GutHealth #LiverHealth #Gastroenterologist #Gurugram #DrLochab

{CRED_EN}
Prepared with AI assistance and reviewed by Dr. Kshitij Lochab."""

STORY_NOTE = f"""Instagram story tips:
• Add a Link sticker to {GUIDE_EN} in the empty space between the box and the red warning note.
• Optional quiz sticker: "Kaju katli or besan ladoo, which one is your Diwali weakness?" (two options)."""

GBP_TEXT = f"""Diwali without acidity: the smart mithai box

Diwali week brings sweets, namkeen, parties and late dinners, and with them more acidity, bloating, food poisoning and gallstone and pancreatitis attacks. Six simple habits help:

1. One or two pieces of mithai, after a meal, never on an empty stomach.
2. With diabetes, a small piece after food, check sugar more often and keep up your medicines.
3. Roasted makhana and chana instead of fried namkeen.
4. Nimbu paani, chaas or water instead of colas; avoid binge drinking, and no alcohol with liver disease or past pancreatitis.
5. Festive dinner by about 9 pm, then a short walk.
6. Milk sweets from licensed shops, refrigerated within 2 hours.

Severe upper belly pain going to the back, with vomiting, after a party needs the emergency department.

The free Diwali food guide covers food safety, a simple Diwali day plan and who should take extra care, in English and Hindi.

{CRED_EN}
Prepared with AI assistance and reviewed by Dr. Kshitij Lochab.

Button: Learn more → {GUIDE_EN}"""

WHATSAPP_EN = f"""🪔 *The smart mithai box: 6 ways to enjoy Diwali without acidity*

1. 1–2 pieces of mithai, after a meal, never on an empty stomach
2. Diabetes? A small piece after food, check sugar more often
3. Roasted makhana and chana, not fried namkeen
4. Nimbu paani over colas; no binge drinking
5. Dinner by 9 pm, then a 15-minute walk
6. Milk sweets from licensed shops, in the fridge within 2 hours

⚠️ Severe upper belly pain going to the back, with vomiting, after a party: go to the emergency department.

Free Diwali food guide 👉 {GUIDE_EN}

Happy Diwali to you and your family!
– {CRED_EN}
_Prepared with AI assistance and reviewed by Dr. Kshitij Lochab._"""

WHATSAPP_HI = f"""🪔 *सेहत वाला मिठाई का डिब्बा: बिना एसिडिटी के दिवाली मनाने के 6 तरीके*

1. 1–2 पीस मिठाई, खाने के बाद; खाली पेट कभी नहीं
2. डायबिटीज़ है? खाने के बाद छोटा पीस, शुगर बार-बार जाँचें
3. तले नमकीन की जगह भुना मखाना और चना
4. कोल्ड ड्रिंक की जगह नींबू पानी; एक साथ ज़्यादा शराब नहीं
5. रात 9 बजे तक खाना, फिर 15 मिनट टहलें
6. खोया, पनीर की मिठाई लाइसेंस वाली दुकान से, 2 घंटे में फ्रिज में

⚠️ पार्टी के बाद पेट के ऊपरी हिस्से में तेज़ दर्द जो पीठ तक जाए, साथ में उल्टी, तो तुरंत इमरजेंसी जाएँ।

दिवाली की मुफ़्त फ़ूड गाइड 👉 {GUIDE_HI}

आपको और आपके परिवार को दीपावली की शुभकामनाएँ!
– {CRED_HI}
_{AI["hi"]}_"""

if __name__ == "__main__":
    from PIL import Image
    import zipfile
    with sync_playwright() as p:
        b = p.chromium.launch()
        render(post("en"), 1080, 1350, f"{OUT}/insta-post.png", b)
        render(tall("en", sticker=True), 1080, 1920, f"{OUT}/insta-story.png", b)
        render(tall("en"), 1080, 1920, f"{OUT}/whatsapp-status-en.png", b)
        render(tall("hi"), 1080, 1920, f"{OUT}/whatsapp-status-hi.png", b)
        render(gbp(), 1200, 900, f"{OUT}/google-business.png", b)
        b.close()
    os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92)
    for name, txt in [("instagram-caption.txt", CAPTION + "\n\n" + STORY_NOTE), ("google-business-post.txt", GBP_TEXT),
                      ("whatsapp-message-en.txt", WHATSAPP_EN), ("whatsapp-message-hi.txt", WHATSAPP_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    with zipfile.ZipFile(f"{OUT}/diwali-mithai-box.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(os.listdir(OUT)):
            if f.endswith((".jpg", ".txt")): z.write(f"{OUT}/{f}", f)
    print("done")
