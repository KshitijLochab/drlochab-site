"""Visiting cards v3 (17 Nov 2026), after researching 2026 card trends (Vistaprint, Paperlust, Overnight Prints, design-principle guides):
tactile minimalism with generous white space, one typeface pair, name as the largest element and contact details no smaller
than about 7 pt; 'blueprint' cards (deep blue with white schematic line drawings on a grid); vertical layouts; dark stock with
metallic foil; a QR code labelled with what it gives you.
Three directions, each front + back, print PDF (with bleed) and a photographed-style mock-up:
  1 Anatomy blueprint  (horizontal): drafting-sheet drawing of the digestive tract in white on deep blue; clean white back.
  2 Vertical minimal   (portrait):   off-white, oversized stacked name, one gold-foil line drawing; deep teal back.
  3 Midnight foil      (horizontal): near-black with tone-on-tone ripple motif and gold-foil name; matching back.
Run: python3 _src/social/visiting_card_v3.py -> _src/out/card-v3/"""
import base64, io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.dirname(HERE)
sys.path.insert(0, SRC)
import qrcode, qrcode.image.svg
import hub
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "card-v3"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
MARK = f'<img src="data:image/png;base64,{b64(f"{SRC}/brand/logo-mark.png")}" style="width:100%;height:100%;display:block">'
BLEED, SAFE = 0.0625, 0.125
FOIL = "linear-gradient(115deg,#B8862E 0%,#F6D78B 28%,#C7952F 48%,#FBE3A0 66%,#A9771F 100%)"
PHONE, SITE = "+91 96671 04882", "drlochab.com"

def qr_svg(data, col):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=0, image_factory=qrcode.image.svg.SvgPathImage)
    q.add_data(data); q.make(fit=True)
    buf = io.BytesIO(); q.make_image().save(buf)
    s = re.sub(r'<\?xml[^>]*\?>', '', buf.getvalue().decode())
    s = re.sub(r'width="[^"]*" height="[^"]*"', 'width="100%" height="100%"', s, count=1)
    return s.replace('fill="#000000"', f'fill="{col}"')

def blueprint_art(col="#FFFFFF"):
    """Drafting-sheet drawing: organ outlines (hub.py paths), leader lines with labels, a scale bar and centre marks."""
    x0, y0, w, h = hub.VB
    paths = [hub.ESOPH, hub.LIVER, hub.GB, hub.STOM, hub.DUO, hub.PANC, hub.BILE, hub.COLON, hub.SMALL]
    lab = {"stomach": "STOMACH", "pancreas": "PANCREAS", "liver": "LIVER", "intestine": "COLON"}
    spots = {"stomach": ((238, 196), (292, 128)), "pancreas": ((232, 262), (290, 300)), "liver": ((96, 190), (40, 120)), "intestine": ((90, 352), (36, 396))}
    g = "".join(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/>' for d in paths)
    for k, ((ax, ay), (lx, ly)) in spots.items():
        anchor = "end" if lx < ax else "start"
        g += (f'<circle cx="{ax}" cy="{ay}" r="2.6" fill="{col}"/><path d="M{ax} {ay} L{lx} {ly}" stroke="{col}" stroke-width=".8" opacity=".8"/>'
              f'<text x="{lx + (-4 if anchor == "end" else 4)}" y="{ly + 4}" text-anchor="{anchor}" font-family="FT" font-weight="600" font-size="11" letter-spacing="1.5" fill="{col}" opacity=".9">{lab[k]}</text>')
    g += (f'<path d="M150 74 V86 M144 80 H156" stroke="{col}" stroke-width=".8" opacity=".7"/>'
          f'<path d="M240 405 H320 M240 400 V410 M280 402 V408 M320 400 V410" stroke="{col}" stroke-width=".8" opacity=".7"/>'
          f'<text x="280" y="398" text-anchor="middle" font-family="FT" font-size="9" fill="{col}" opacity=".7" letter-spacing="1">FIG. 1</text>')
    return f'<svg viewBox="{x0} {y0} {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">{g}</svg>'

def gut_line(col, sw=1.4):
    """A single fine line: oesophagus, stomach and the frame of the bowel, for the minimal card."""
    return (f'<svg viewBox="40 70 240 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%">'
            + "".join(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>' for d in (hub.ESOPH, hub.STOM, hub.DUO, hub.COLON, hub.SMALL)) + "</svg>")

def ripple(col, w=3.75, h=2.25):
    """Tone-on-tone motif: concentric arcs echoing the logo's loop, repeated across the card."""
    g = ""
    for cx in range(-40, 420, 90):
        for cy in range(-40, 280, 90):
            for r in (14, 26, 38):
                g += f'<circle cx="{cx + (45 if (cy // 90) % 2 else 0)}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="1"/>'
    return f'<svg viewBox="0 0 375 225" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%">{g}</svg>'

def css(pw, ph):
    return f"""
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
@page{{size:{pw}in {ph}in;margin:0}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:"FT",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.card{{width:{pw}in;height:{ph}in;position:relative;overflow:hidden;page-break-after:always}}
.in{{position:absolute;left:{BLEED + SAFE}in;right:{BLEED + SAFE}in;top:{BLEED + SAFE}in;bottom:{BLEED + SAFE}in}}
.serif{{font-family:"YS",serif;font-weight:400}}
.cap{{font-weight:600;letter-spacing:.18em;text-transform:uppercase}}
.foil{{background:{FOIL};-webkit-background-clip:text;background-clip:text;color:transparent}}
"""

# OPD rows: (days, place, area, time)
OPD = [("Mon · Wed · Fri", "Apollo Clinic", "Sector 52", "6 – 8 pm"),
       ("Tue · Thu · Sat", "Apollo Hospitals", "Golf Course Road", "4 – 6 pm"),
       ("Tue · Thu · Sat", "Arcura Clinic", "Sector 51", "6:30 – 8 pm")]

def opd_rows(fg, sub, acc, line, size=1.0):
    s = size
    return "".join(
        f'<div style="display:grid;grid-template-columns:{.86*s}in 1fr auto;align-items:center;gap:.06in;padding:{.032*s}in 0;border-top:.5pt solid {line}">'
        f'<span class="cap" style="font-size:{5.6*s}pt;color:{acc};letter-spacing:.1em">{d}</span>'
        f'<span><span class="serif" style="font-size:{8.6*s}pt;color:{fg}">{p}</span> <span style="font-size:{6.4*s}pt;color:{sub}">{a}</span></span>'
        f'<span style="font-size:{7.6*s}pt;font-weight:600;color:{fg};white-space:nowrap">{t}</span></div>' for d, p, a, t in OPD)

# ---------------- 1 Anatomy blueprint (3.5 x 2 in) ----------------
def bp_front():
    grid = ("background-color:#0F3B6E;background-image:linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),"
            "linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),"
            "linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:.25in .25in,.25in .25in,.05in .05in,.05in .05in")
    return f"""<div class="card" style="{grid};color:#fff">
 <div style="position:absolute;right:.08in;top:.14in;width:2.2in;height:1.85in">{blueprint_art()}</div>
 <div class="in">
  <div style="position:absolute;left:0;top:0;width:.3in;height:.3in">{MARK}</div>
  <div style="position:absolute;left:0;bottom:0;width:1.7in">
   <div class="cap" style="font-size:5.6pt;color:#9CC3EA">Gastroenterology</div>
   <div class="serif" style="font-size:16pt;line-height:1.02;margin-top:.04in">Dr. Kshitij<br>Lochab</div>
   <div style="width:.3in;height:1pt;background:#fff;opacity:.6;margin:.06in 0"></div>
   <div style="font-size:6.8pt;line-height:1.35;color:#D6E6F7">Consultant Gastroenterologist<br>&amp; Therapeutic Endoscopist</div></div>
 </div></div>"""

def bp_back():
    return f"""<div class="card" style="background:#FFFFFF;color:#0F2340">
 <div style="position:absolute;left:0;top:0;bottom:0;width:{BLEED + .06}in;background:#0F3B6E"></div>
 <div class="in" style="left:{BLEED + SAFE + .05}in">
  <div style="display:flex;justify-content:space-between;align-items:flex-start">
   <div><div class="serif" style="font-size:11pt">Dr. Kshitij Lochab</div>
    <div style="font-size:6pt;color:#4B5D74;margin-top:.01in">DrNB Gastroenterology · All-India Gold Medal · EUS &amp; ERCP</div></div></div>
  <div style="margin-top:.05in">{opd_rows("#0F2340", "#5B6B80", "#1E5FA8", "#DCE4EE")}</div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:flex-end">
   <div><div class="serif" style="font-size:11pt;color:#0F3B6E">{PHONE}</div>
    <div style="font-size:6.4pt;color:#4B5D74">Call or WhatsApp · {SITE}</div>
    <div style="font-size:5.8pt;color:#A23A2E;margin-top:.02in">Urgent during the day: Apollo Hospitals only</div></div>
   <div style="display:flex;align-items:center;gap:.05in"><span style="font-size:5.4pt;color:#5B6B80;text-align:right;line-height:1.3">Scan for<br>directions</span>
    <div style="width:.44in;height:.44in">{qr_svg("https://drlochab.com", "#0F2340")}</div></div></div>
 </div></div>"""

# ---------------- 2 Vertical minimal (2 x 3.5 in) ----------------
def vm_front():
    return f"""<div class="card" style="background:#F6F2EA;color:#13241F">
 <div class="in">
  <div style="width:.26in;height:.26in">{MARK}</div>
  <div style="position:absolute;left:0;right:0;top:.5in">
   <div style="font-size:7pt;color:#6D7A73;letter-spacing:.06em">Dr.</div>
   <div class="serif" style="font-size:23pt;line-height:.98;margin-top:.01in">Kshitij<br>Lochab</div>
   <div style="width:.5in;height:1.2pt;background:{FOIL};margin:.09in 0 .07in"></div>
   <div style="font-size:7pt;line-height:1.4;color:#2E4740">Consultant Gastroenterologist<br>&amp; Therapeutic Endoscopist</div></div>
  <div style="position:absolute;right:-.06in;bottom:.5in;width:.85in;height:1.1in;opacity:.95">{gut_line("#C69A3E", 1.5)}</div>
  <div style="position:absolute;left:0;right:0;bottom:0">
   <div class="serif" style="font-size:10pt">{PHONE}</div>
   <div style="font-size:6.6pt;color:#6D7A73;margin-top:.02in">Call or WhatsApp · {SITE}</div></div>
 </div></div>"""

def vm_back():
    rows = "".join(f'<div style="padding:.07in 0;border-top:.5pt solid rgba(255,255,255,.22)"><div class="cap" style="font-size:5.6pt;color:#F1CD7E;letter-spacing:.12em">{d}</div>'
                   f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:.02in"><span class="serif" style="font-size:9pt">{p}</span>'
                   f'<span style="font-size:7.6pt;font-weight:600">{t}</span></div><div style="font-size:6.2pt;color:#BFDCD5">{a}, Gurugram</div></div>' for d, p, a, t in OPD)
    return f"""<div class="card" style="background:linear-gradient(170deg,#0F6B5F 0%,#0A4D45 100%);color:#fff">
 <div class="in">
  <div class="cap" style="font-size:6pt;color:#F1CD7E">Evening OPD</div>
  <div class="serif" style="font-size:12pt;margin:.03in 0 .08in">Monday to Saturday</div>
  {rows}
  <div style="border-top:.5pt solid rgba(255,255,255,.22);padding-top:.06in;font-size:6.2pt;line-height:1.35;color:#E6F2EF">Urgent during the day?<br>Apollo Hospitals only. Call first.</div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:flex-end">
   <div style="font-size:5.6pt;line-height:1.4;color:#BFDCD5">MBBS · MD · DrNB<br>All-India Gold Medal<br>HMC Reg. HN-23524</div>
   <div style="text-align:center"><div style="width:.52in;height:.52in;background:#fff;padding:.035in;border-radius:.04in">{qr_svg("https://drlochab.com", "#0A4D45")}</div>
    <div style="font-size:5.2pt;color:#BFDCD5;margin-top:.025in">Scan: directions</div></div></div>
 </div></div>"""

# ---------------- 3 Midnight foil (3.5 x 2 in) ----------------
def mf_front():
    return f"""<div class="card" style="background:radial-gradient(120% 140% at 80% 10%,#1D2A27 0%,#0E1312 60%,#090C0B 100%);color:#fff">
 {ripple("rgba(255,255,255,.045)")}
 <div class="in" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">
  <div style="width:.34in;height:.34in;margin-bottom:.1in">{MARK}</div>
  <div class="serif foil" style="font-size:19pt;line-height:1.05">Dr. Kshitij Lochab</div>
  <div style="width:.4in;height:1pt;background:{FOIL};margin:.08in 0"></div>
  <div class="cap" style="font-size:6pt;color:#D8D2C4;letter-spacing:.22em">Gastroenterologist · Therapeutic Endoscopist</div>
  <div style="font-size:6.4pt;color:#9AA5A1;margin-top:.05in">DrNB Gastroenterology · All-India Gold Medal · EUS &amp; ERCP</div>
 </div></div>"""

def mf_back():
    return f"""<div class="card" style="background:#0E1312;color:#fff">
 {ripple("rgba(255,255,255,.03)")}
 <div class="in">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="cap foil" style="font-size:6pt">Evening OPD · Gurugram</span>
   <span style="font-size:6pt;color:#9AA5A1">Monday to Saturday</span></div>
  <div style="margin-top:.06in">{opd_rows("#FFFFFF", "#9AA5A1", "#E2B95B", "rgba(255,255,255,.14)")}</div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:flex-end">
   <div><div class="serif foil" style="font-size:11pt">{PHONE}</div>
    <div style="font-size:6.4pt;color:#C9C3B6">Call or WhatsApp · {SITE}</div>
    <div style="font-size:5.8pt;color:#E59A8E;margin-top:.02in">Urgent during the day: Apollo Hospitals only</div></div>
   <div style="width:.46in;height:.46in;background:#fff;padding:.03in;border-radius:.04in">{qr_svg("https://drlochab.com", "#0E1312")}</div></div>
 </div></div>"""

DESIGNS = [("1-anatomy-blueprint", 3.5, 2.0, bp_front, bp_back, "#D9D3C7"),
           ("2-vertical-minimal", 2.0, 3.5, vm_front, vm_back, "#C9C1B2"),
           ("3-midnight-foil", 3.5, 2.0, mf_front, mf_back, "#B9B3A6")]

def mockup(fr, bk, w, h, bg, k=3.2):
    """A photographed-style scene: both sides on a soft paper backdrop with real shadows (2400 x 1600 px)."""
    pw, ph = w + 2 * BLEED, h + 2 * BLEED
    cw, ch = w * 96 * k, h * 96 * k; off = BLEED * 96 * k
    card = lambda html, x, y, rot: (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{cw}px;height:{ch}px;transform:rotate({rot}deg);'
                                    f'box-shadow:0 30px 60px rgba(30,25,15,.35),0 6px 14px rgba(30,25,15,.25);border-radius:6px;overflow:hidden">'
                                    f'<div style="position:absolute;left:-{off}px;top:-{off}px;transform:scale({k});transform-origin:0 0">{html}</div></div>')
    if w > h:
        pos = [(170, 150, -6), (1140, 800, 4)]
    else:
        pos = [(560, 170, -5), (1300, 230, 4)]
    return (f'<div style="width:2400px;height:1600px;position:relative;overflow:hidden;'
            f'background:radial-gradient(90% 90% at 40% 30%,#F4EFE6 0%,{bg} 100%)">'
            f'<div style="position:absolute;inset:0;opacity:.18;background-image:radial-gradient(rgba(0,0,0,.25) 1px,transparent 1px);background-size:6px 6px"></div>'
            + card(fr(), *pos[0]) + card(bk(), *pos[1]) + "</div>")

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for tag, w, h, fr, bk, bg in DESIGNS:
            pw, ph = w + 2 * BLEED, h + 2 * BLEED
            html = f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)}</style></head><body>{fr()}{bk()}</body></html>"
            path = f"{OUT}/card.html"; open(path, "w").write(html)
            pg = b.new_page(); pg.goto(f"file://{path}"); pg.wait_for_timeout(500)
            pg.pdf(path=f"{OUT}/card-{tag}-print.pdf", width=f"{pw}in", height=f"{ph}in", print_background=True); pg.close()
            pv = b.new_page(viewport={"width": int(pw * 96) + 2, "height": int(ph * 96 * 2) + 2}, device_scale_factor=6)
            pv.goto(f"file://{path}"); pv.wait_for_timeout(500)
            cards = pv.locator(".card")
            for i, nm in enumerate(["front", "back"]):
                box = cards.nth(i).bounding_box()
                pv.screenshot(path=f"{OUT}/card-{tag}-{nm}.png", clip={"x": box["x"] + BLEED * 96, "y": box["y"] + BLEED * 96, "width": w * 96, "height": h * 96})
            pv.close()
            mk = f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)} .card{{page-break-after:auto}}</style></head><body style='margin:0'>{mockup(fr, bk, w, h, bg)}</body></html>"
            open(path, "w").write(mk)
            pm = b.new_page(viewport={"width": 2400, "height": 1600}); pm.goto(f"file://{path}"); pm.wait_for_timeout(600)
            pm.screenshot(path=f"{OUT}/mockup-{tag}.png"); pm.close()
            os.remove(path)
        b.close()
    print("done", sorted(os.listdir(OUT)))
