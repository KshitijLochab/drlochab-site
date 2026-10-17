"""Social content for the week of 19 Oct 2026 (Dussehra Tue 20 Oct; cooler weather setting in).
Instagram: gallstones carousel (EN, 6 slides), Dussehra feast post (HI), winter water post (EN).
Google Business Profile: gallstones (1200x900). WhatsApp Status: 3 images (1080x1920).
Ties in with the new answer page /answers/do-gallstones-need-surgery/ (EN) and /hi/answers/do-gallstones-need-surgery/ (HI).
Run from anywhere: python3 _src/social/week_2026_10_19.py  -> _src/out/week-2026-10-19/"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from playwright.sync_api import sync_playwright
from week_2026_10_12 import CSS, foot, SRC

OUT = os.path.join(SRC, "out", "week-2026-10-19"); os.makedirs(OUT, exist_ok=True)
ANS_EN, ANS_HI = "drlochab.com/answers/do-gallstones-need-surgery", "drlochab.com/hi/answers/do-gallstones-need-surgery"

# ---------- original drawings ----------
SAC = "M292 150 C246 146 214 178 204 236 C190 320 176 418 236 466 C296 512 376 476 384 396 C392 316 350 232 330 184 C322 164 308 152 292 150 Z"

def stones(xy):
    out = ""
    for x, y, r in xy:
        pts = " ".join(f"{x + r * (1 + .12 * math.sin(3 * a)) * math.cos(a):.1f},{y + r * (1 + .12 * math.sin(3 * a)) * math.sin(a):.1f}" for a in [i * math.pi / 5 for i in range(10)])
        out += f'<polygon points="{pts}" fill="#C98A3A" stroke="#7A4E1A" stroke-width="4" stroke-linejoin="round"/><circle cx="{x - r * .3:.0f}" cy="{y - r * .3:.0f}" r="{r * .22:.0f}" fill="#F1C98A"/>'
    return out

def gallbladder(mood="calm", duct_stone=False, w=600, z="#FFFFFF"):
    """The gallbladder as a pear-shaped sac of bile with stones (viewBox 0 0 600 600).
    mood: calm (asleep, a silent stone), plain (awake), pain (lightning, a painful attack). z: colour of the sleeping z's."""
    if mood == "calm":
        face = ('<path d="M258 330 q14 12 28 0 M314 330 q14 12 28 0" fill="none" stroke="#1F4A1A" stroke-width="7" stroke-linecap="round"/>'
                '<path d="M286 368 q14 8 28 0" fill="none" stroke="#1F4A1A" stroke-width="7" stroke-linecap="round"/>'
                f'<text x="150" y="214" font-family="YS" font-size="58" fill="{z}" opacity=".9">z</text><text x="112" y="164" font-family="YS" font-size="42" fill="{z}" opacity=".75">z</text>')
        extra = ""
    elif mood == "plain":
        face = ('<circle cx="272" cy="330" r="9" fill="#1F4A1A"/><circle cx="328" cy="330" r="9" fill="#1F4A1A"/>'
                '<path d="M284 366 q16 10 32 0" fill="none" stroke="#1F4A1A" stroke-width="7" stroke-linecap="round"/>')
        extra = ""
    else:
        face = ('<path d="M254 318 l30 14 M346 318 l-30 14" stroke="#1F4A1A" stroke-width="8" stroke-linecap="round"/>'
                '<ellipse cx="300" cy="372" rx="20" ry="16" fill="#1F4A1A"/>')
        extra = "".join(f'<path d="{d}" fill="#F3B84A" stroke="#B9761A" stroke-width="4" stroke-linejoin="round"/>' for d in
                        ["M140 250 l40 -10 l-14 30 l44 -6 l-62 50 l16 -34 l-40 6 z", "M450 300 l-34 -18 l4 32 l-40 -18 l46 64 l-6 -36 l38 16 z", "M160 420 l36 4 l-20 24 l40 4 l-62 30 l22 -26 l-36 -4 z"])
    ds = stones([(440, 420, 22)]) + '<circle cx="440" cy="420" r="44" fill="none" stroke="#E0503D" stroke-width="7" stroke-dasharray="14 10"/>' if duct_stone else ""
    return f"""<svg viewBox="0 0 600 600" style="width:{w}px;height:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="gb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#B9DC86"/><stop offset=".6" stop-color="#86BC5A"/><stop offset="1" stop-color="#5E9B4B"/></linearGradient>
<filter id="gs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#062F2A" flood-opacity=".3"/></filter></defs>
<path d="M440 30 V580" stroke="#3F7A33" stroke-width="38" stroke-linecap="round"/><path d="M440 30 V580" stroke="#A9D27A" stroke-width="24" stroke-linecap="round"/>
<path d="M298 156 C320 110 380 100 440 120" fill="none" stroke="#3F7A33" stroke-width="30" stroke-linecap="round"/><path d="M298 156 C320 110 380 100 440 120" fill="none" stroke="#A9D27A" stroke-width="17" stroke-linecap="round"/>
<g filter="url(#gs)"><path d="{SAC}" fill="url(#gb)" stroke="#3F7A33" stroke-width="7"/></g>
<ellipse cx="248" cy="240" rx="16" ry="44" fill="#FFFFFF" opacity=".45" transform="rotate(12 248 240)"/>
{stones([(262, 432, 26), (310, 446, 22), (338, 410, 18), (284, 400, 14)])}
{face}{extra}{ds}
</svg>"""

def remedies(w=640):
    """Lemon water and an oil bottle, each crossed out (viewBox 0 0 640 360)."""
    no = lambda cx, cy: f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#B0362B" stroke-width="18"/><path d="M{cx-106} {cy+106} L{cx+106} {cy-106}" stroke="#B0362B" stroke-width="18" stroke-linecap="round"/>'
    lemon_glass = ('<path d="M110 90 H210 L198 290 H122 Z" fill="#F2F8F6" stroke="#0D7466" stroke-width="6" stroke-linejoin="round"/>'
                   '<path d="M116 140 H204 L196 284 H124 Z" fill="#F7E58A" opacity=".85"/>'
                   '<g transform="translate(206 100)"><circle r="40" fill="#F7D046" stroke="#C9A21F" stroke-width="5"/><circle r="30" fill="#FBEFA6"/>'
                   + "".join(f'<path d="M0 0 L{30*math.cos(a):.1f} {30*math.sin(a):.1f}" stroke="#E9C93A" stroke-width="3"/>' for a in [i * math.pi / 4 for i in range(8)]) + '</g>')
    bottle = ('<path d="M450 70 h44 v40 c30 16 44 40 44 70 v100 c0 14 -10 22 -22 22 h-88 c-12 0 -22 -8 -22 -22 v-100 c0 -30 14 -54 44 -70 z" fill="#F3C24A" stroke="#B9761A" stroke-width="6" stroke-linejoin="round"/>'
              '<rect x="444" y="50" width="56" height="26" rx="6" fill="#0D7466"/><rect x="430" y="180" width="84" height="56" rx="10" fill="#FFFFFF" opacity=".85"/>'
              '<path d="M448 208 q24 -22 48 0" fill="none" stroke="#B9761A" stroke-width="5" stroke-linecap="round"/>')
    return f'<svg viewBox="0 0 640 360" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">{lemon_glass}{no(160, 185)}{bottle}{no(472, 185)}</svg>'

def feast_plate(w=560):
    """A small festive plate: one jalebi, one laddoo, a puri and sabzi, with marigolds (viewBox 0 0 600 600)."""
    jalebi = "M0 0 " + " ".join(f"L{(6 + 5.2 * t) * math.cos(t):.1f} {(6 + 5.2 * t) * math.sin(t):.1f}" for t in [i * .25 for i in range(1, 66)])
    marigold = lambda x, y, s: f'<g transform="translate({x} {y}) scale({s})">' + "".join(f'<circle cx="{14*math.cos(a/6*math.pi):.1f}" cy="{14*math.sin(a/6*math.pi):.1f}" r="12" fill="#F28C1E"/>' for a in range(12)) + '<circle r="14" fill="#F9B233"/><circle r="6" fill="#E46F10"/></g>'
    laddoo = '<circle cx="404" cy="236" r="58" fill="#F0A030" stroke="#C47A16" stroke-width="5"/>' + "".join(f'<circle cx="{404 + 34*math.cos(a):.0f}" cy="{236 + 34*math.sin(a):.0f}" r="5" fill="#C47A16" opacity=".7"/>' for a in [i * .9 for i in range(7)]) + '<circle cx="388" cy="218" r="14" fill="#FFD28A" opacity=".7"/>'
    puri = '<ellipse cx="226" cy="388" rx="104" ry="92" fill="#E9B866" stroke="#B9852E" stroke-width="5"/><ellipse cx="206" cy="366" rx="54" ry="40" fill="#F6D592" opacity=".8"/>'
    sabzi = '<circle cx="402" cy="404" r="78" fill="#C8D0D2"/><circle cx="402" cy="404" r="66" fill="#E6A94A"/>' + "".join(f'<rect x="{x}" y="{y}" width="22" height="22" rx="6" fill="#F4D58A" stroke="#C9963A" stroke-width="2" transform="rotate({r} {x+11} {y+11})"/>' for x, y, r in [(370,380,10),(402,372,-20),(424,402,30),(380,416,-10),(410,430,20)]) + '<circle cx="392" cy="398" r="6" fill="#3F8A3A"/><circle cx="430" cy="384" r="5" fill="#3F8A3A"/>'
    return f"""<svg viewBox="0 0 600 600" style="width:{w}px;height:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><radialGradient id="fs" cx="42%" cy="38%" r="70%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="#E4E9EA"/><stop offset="1" stop-color="#B9C3C6"/></radialGradient>
<filter id="fsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#0B2A26" flood-opacity=".3"/></filter></defs>
<g filter="url(#fsh)"><circle cx="300" cy="300" r="250" fill="#C8D0D2"/></g><circle cx="300" cy="300" r="230" fill="url(#fs)"/>
<g transform="translate(206 218)"><path d="{jalebi}" fill="none" stroke="#C9661A" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/><path d="{jalebi}" fill="none" stroke="#F59A2E" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/></g>
{laddoo}{puri}{sabzi}
{marigold(70, 80, 1.2)}{marigold(530, 76, 1)}{marigold(64, 524, 1)}{marigold(536, 528, 1.1)}
</svg>"""

def warm_glass(w=520):
    """A steel glass of warm water wrapped in a striped winter scarf, with steam (viewBox 0 0 600 640)."""
    steam = "".join(f'<path d="M{x} 150 c-24 -30 24 -50 0 -80 c-20 -26 14 -44 4 -66" fill="none" stroke="#7FB8AC" stroke-width="12" stroke-linecap="round" opacity=".85"/>' for x in (240, 300, 360))
    stripes = "".join(f'<path d="M{x} 352 l-14 96" stroke="#FFFFFF" stroke-width="12" opacity=".8"/>' for x in range(178, 440, 44))
    return f"""<svg viewBox="0 0 600 640" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">
<defs><linearGradient id="st" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#AEB9BC"/><stop offset=".35" stop-color="#F4F7F7"/><stop offset=".7" stop-color="#D3DADC"/><stop offset="1" stop-color="#9AA6A9"/></linearGradient>
<filter id="wsh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#062F2A" flood-opacity=".35"/></filter></defs>
{steam}
<g filter="url(#wsh)"><path d="M150 170 H450 L420 600 H180 Z" fill="url(#st)" stroke="#8A979A" stroke-width="5" stroke-linejoin="round"/></g>
<ellipse cx="300" cy="172" rx="150" ry="22" fill="#CFE8F2" stroke="#8A979A" stroke-width="5"/>
<path d="M150 350 C230 380 370 380 452 350 L444 446 C370 476 232 476 158 446 Z" fill="#E0503D"/>{stripes}
<path d="M392 410 C410 470 400 540 430 600 L470 590 C450 530 452 470 432 404 Z" fill="#E0503D"/><path d="M420 560 l46 -12 M412 520 l40 -10" stroke="#FFFFFF" stroke-width="10" opacity=".8"/>
<path d="M430 600 l-6 24 M444 597 l0 24 M458 594 l6 22" stroke="#C0392B" stroke-width="7" stroke-linecap="round"/>
</svg>"""

# ---------- Instagram 1: gallstones carousel (6 slides, English) ----------
def slide(n, bg, kick, title, art, line, kick_col="#0D7466", art_top=360):
    return f"""<div class="s {bg}" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:26px;color:{kick_col}">{kick}</div>
 <h2 style="font-size:90px;margin-top:16px">{title}</h2>
 <div style="position:absolute;left:0;right:0;top:{art_top}px;display:flex;justify-content:center">{art}</div>
 <p style="position:absolute;left:72px;right:72px;top:960px;font-size:46px;line-height:1.3">{line}</p>
 {foot(n, 6)}</div>"""

GALL = [
 f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:26px;color:#9FD8CC">Gallstones</div>
  <h1 style="font-size:112px;margin-top:22px">Do they always<br>need an <em>operation?</em></h1>
  <div style="position:absolute;right:40px;top:470px">{gallbladder("calm", w=560)}</div>
  <p style="position:absolute;left:72px;top:620px;font-size:46px;color:#FFFFFF;max-width:440px;line-height:1.25"><b style="font-weight:600;color:#F3B84A">Usually not.</b><br>Here is how doctors decide.</p>
  {foot(1, 6, light=True)}</div>""",
 slide(2, "mint", "Silent stones", "Found by chance?<br>Usually <em>just watched</em>", gallbladder("calm", w=540, z="#0D7466"),
       "Never caused pain? The chance of trouble is low. <b style='font-weight:600'>Most need no operation.</b>"),
 slide(3, "cream", "Painful stones", "Pain attacks?<br><em>Keyhole removal</em>", gallbladder("pain", w=540),
       "Strong upper belly pain after heavy meals tends to come back. <b style='font-weight:600'>Removing the gallbladder</b> is the usual fix."),
 slide(4, "saffron", "Stone in the bile duct", "Slipped out?<br>Removed by <em>ERCP</em>", gallbladder("plain", duct_stone=True, w=540),
       "A scope through the mouth takes the stone out, <b style='font-weight:600'>without a cut.</b> Then the gallbladder is usually removed."),
 slide(5, "rose", "Myth", "Home remedies<br><em>do not</em> dissolve stones", remedies(760),
       "Lemon water, juices and oil flushes cannot remove stones, and <b style='font-weight:600'>some can bring on an attack.</b>", "#B0362B", 430),
 f"""<div class="s teal" style="width:1080px;height:1350px;padding:84px 72px">
  <div class="kick" style="font-size:26px;color:#F3B84A">Go to emergency, or call 112, if</div>
  <h2 style="font-size:84px;margin-top:16px">Pain lasts <em>hours</em>, or comes with</h2>
  <div style="margin-top:60px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
   {''.join(f'<div class="chip" style="background:#FFFFFF;color:#12302C;font-size:44px;padding:40px 34px;border-radius:36px"><span style="width:22px;height:22px;border-radius:50%;background:#B0362B;flex:none"></span>{t}</div>' for t in ["Fever, shivering", "Yellow eyes or skin"])}
   <div class="chip" style="grid-column:span 2;background:#FFFFFF;color:#12302C;font-size:44px;padding:40px 34px;border-radius:36px"><span style="width:22px;height:22px;border-radius:50%;background:#B0362B;flex:none"></span>Repeated vomiting</div>
  </div>
  <p style="margin-top:64px;font-size:40px;line-height:1.35;color:#CFE5E0">Read the full answer:</p>
  <div style="margin-top:18px;display:inline-block;background:#F3B84A;color:#12302C;font-weight:600;font-size:31px;padding:22px 34px;border-radius:999px">{ANS_EN}</div>
  {foot(6, 6, light=True)}</div>""",
]

# ---------- Instagram 2: Dussehra feast (Hindi, single post) ----------
FEAST_HI = [("1", "छोटी प्लेट, एक बार"), ("2", "मिठाई एक-दो टुकड़े"), ("3", "खाने के बाद 15 मिनट सैर"), ("4", "रात का खाना जल्दी")]
def feast_chips(size, gap, cols=2):
    return (f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:{gap}px">' + "".join(
        f'<div class="chip" style="background:#FFFFFF;color:#12302C;font-size:{size}px;padding:16px 26px;gap:16px"><span style="font-family:YS;color:#0D7466;font-size:{size+6}px">{n}</span>{t}</div>'
        for n, t in FEAST_HI) + "</div>")

FEAST_POST = f"""<div class="s saffron hi" style="width:1080px;height:1350px;padding:70px 72px">
 <div class="kick" style="font-size:30px;color:#B5542C;text-align:center">दशहरा, 20 अक्टूबर</div>
 <h1 style="font-size:84px;margin-top:4px;text-align:center">दावत भी, पेट भी <em>ख़ुश</em></h1>
 <div style="position:absolute;left:270px;top:262px">{feast_plate(540)}</div>
 <div style="position:absolute;left:72px;right:72px;top:836px">{feast_chips(36, 16)}</div>
 <p style="position:absolute;left:72px;right:72px;top:1052px;font-size:31px;line-height:1.4;color:#4A615D;text-align:center">त्योहार के बाद भी 2 हफ़्ते से ज़्यादा एसिडिटी या दर्द रहे, <b style="font-weight:600;color:#12302C">तो जाँच करवाएँ।</b></p>
 {foot(hi=True)}</div>"""

# ---------- Instagram 3: cooler weather, keep drinking water (English, single post) ----------
WINTER = [("1", "Warm water or soup through the day"), ("2", "Winter greens: methi, palak, sarson"), ("3", "Guava, carrots and amla")]
WINTER_POST = f"""<div class="s mint" style="width:1080px;height:1350px;padding:84px 72px">
 <div class="kick" style="font-size:26px;color:#0D7466">Cooler days ahead</div>
 <h1 style="font-size:96px;margin-top:16px">Less thirst,<br><em>harder stools</em></h1>
 <div style="position:absolute;right:56px;top:300px">{warm_glass(430)}</div>
 <div style="position:absolute;left:72px;right:72px;top:812px;display:flex;flex-direction:column;gap:16px">
  {''.join(f'<div class="chip" style="background:#FFFFFF;font-size:38px;padding:20px 30px"><span style="font-family:YS;color:#0D7466;font-size:44px;min-width:34px">{n}</span>{t}</div>' for n, t in WINTER)}
 </div>
 <p style="position:absolute;left:72px;top:440px;max-width:520px;font-size:42px;line-height:1.3">We drink less when it is cool. <b style="font-weight:600">Keep sipping, even when not thirsty.</b></p>
 {foot()}</div>"""

# ---------- Google Business Profile (1200x900) ----------
GBP = f"""<div class="s teal" style="width:1200px;height:900px;padding:80px 72px">
 <div class="kick" style="font-size:24px;color:#9FD8CC">Gallstones</div>
 <h1 style="font-size:80px;margin-top:18px;max-width:640px">An operation is <em>not always</em> needed</h1>
 <p style="font-size:30px;margin-top:26px;color:#CFE5E0;max-width:560px">When stones can be watched, when they need treatment, and the warning signs.</p>
 <div style="position:absolute;right:30px;top:150px">{gallbladder("calm", w=560)}</div>
 {foot(light=True, pad=72, size=1.05)}</div>"""

# ---------- WhatsApp Status (1080x1920) ----------
def status_chips(items, size=44, dark=False):
    bg = "rgba(255,255,255,.12)" if dark else "#FFFFFF"; num = "#F3B84A" if dark else "#0D7466"
    return "".join(f'<div class="chip" style="background:{bg};font-size:{size}px;border-radius:40px;padding:24px 32px"><span style="font-family:YS;color:{num};font-size:{size+6}px;min-width:44px">{n}</span>{t}</div>' for n, t in items)

WA = [
 ("status-1-gallstones-hi", f"""<div class="s teal hi" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:36px;color:#9FD8CC;text-align:center">पित्त की पथरी</div>
  <h1 style="font-size:100px;text-align:center;margin-top:10px">हर बार <em>ऑपरेशन</em><br>ज़रूरी नहीं</h1>
  <div style="position:absolute;left:210px;top:520px">{gallbladder("calm", w=640)}</div>
  <div style="position:absolute;left:80px;right:80px;top:1190px;display:flex;flex-direction:column;gap:20px">
   {status_chips([("1", "बिना दर्द की पथरी: अक्सर बस नज़र"), ("2", "दर्द के दौरे: दूरबीन से ऑपरेशन"), ("3", "घरेलू नुस्खे पथरी नहीं गलाते")], 42, dark=True)}
  </div>
  <div style="position:absolute;left:0;right:0;top:1690px;text-align:center;font-size:30px;color:#CFE5E0">{ANS_HI}</div>
  {foot(light=True, pad=80, size=1.15, hi=True)}</div>"""),
 ("status-2-dussehra-hi", f"""<div class="s saffron hi" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:36px;color:#B5542C;text-align:center">दशहरे की शुभकामनाएँ</div>
  <h1 style="font-size:100px;text-align:center;margin-top:10px">दावत भी, पेट भी <em>ख़ुश</em></h1>
  <div style="position:absolute;left:220px;top:480px">{feast_plate(640)}</div>
  <div style="position:absolute;left:80px;right:80px;top:1180px">{feast_chips(40, 20, 1)}</div>
  {foot(pad=80, size=1.15, hi=True)}</div>"""),
 ("status-3-winter-water", f"""<div class="s mint" style="width:1080px;height:1920px;padding:150px 80px">
  <div class="kick" style="font-size:30px;color:#0D7466;text-align:center">Cooler days ahead</div>
  <h1 style="font-size:100px;text-align:center;margin-top:20px">Keep <em>sipping</em>,<br>even when not thirsty</h1>
  <div style="position:absolute;left:290px;top:600px">{warm_glass(500)}</div>
  <div style="position:absolute;left:80px;right:80px;top:1220px;display:flex;flex-direction:column;gap:20px">{status_chips(WINTER, 40)}</div>
  <div style="position:absolute;left:0;right:0;top:1690px;text-align:center;font-size:32px;color:#4A615D">drlochab.com/conditions/constipation</div>
  {foot(pad=80, size=1.15)}</div>"""),
]

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        def shot(html, w, h, path):
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{html}</body></html>")
            pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=path); pg.close()
        for i, s in enumerate(GALL, 1):
            shot(s, 1080, 1350, f"{OUT}/ig1-gallstones-slide-{i}.png")
        shot(FEAST_POST, 1080, 1350, f"{OUT}/ig2-dussehra-feast-hi.png")
        shot(WINTER_POST, 1080, 1350, f"{OUT}/ig3-winter-water.png")
        shot(GBP, 1200, 900, f"{OUT}/gbp-gallstones.png")
        for name, s in WA:
            shot(s, 1080, 1920, f"{OUT}/wa-{name}.png")
        b.close()
    os.remove(f"{OUT}/tmp.html")
    print("done", OUT)
