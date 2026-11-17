"""Visiting cards, redesigned 17 Nov 2026 with the new OPD timings. Two design directions to choose from:
  A "Midnight & gold": deep ink-teal front with gold line-art of the digestive organs (paths from hub.py), big serif name;
     cream back with the evening timetable as two tickets and a QR code.
  B "Bold portrait": white front with a teal-to-mint wave, round portrait with a gold ring, name and credentials;
     teal back with the timetable and QR code.
Size 3.5 x 2 in (88.9 x 50.8 mm) with 1/16 in bleed on every side, safe zone 1/8 in inside trim.
Outputs a print-ready 2-page PDF per design (front, back; vector text and QR) and PNG previews at 6x.
Run: python3 _src/social/visiting_card_2026.py -> _src/out/card-2026/"""
import base64, io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.dirname(HERE)
sys.path.insert(0, SRC)
import qrcode, qrcode.image.svg
import hub
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "card-2026"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
MARK = '<img src="data:image/png;base64,' + base64.b64encode(open(f"{SRC}/brand/logo-mark.png", "rb").read()).decode() + '" style="width:100%;height:100%;display:block">'
PHOTO = "data:image/jpeg;base64," + base64.b64encode(open(f"{SRC}/brand/portrait-hires.jpg", "rb").read()).decode()

W, H, BLEED, SAFE = 3.5, 2.0, 0.0625, 0.125
PW, PH = W + 2 * BLEED, H + 2 * BLEED
PAD = BLEED + SAFE
INK, TEAL, DEEP, GOLD, GOLD2, CREAM = "#0E2A27", "#0D7466", "#0B6A5E", "#D9A441", "#F3C66B", "#FBF6EC"
SAFF, PLUM = "#E8862A", "#7A4E9E"

def qr_svg(data, col):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=0, image_factory=qrcode.image.svg.SvgPathImage)
    q.add_data(data); q.make(fit=True)
    buf = io.BytesIO(); q.make_image().save(buf)
    s = re.sub(r'<\?xml[^>]*\?>', '', buf.getvalue().decode())
    s = re.sub(r'width="[^"]*" height="[^"]*"', 'width="100%" height="100%"', s, count=1)
    return s.replace('fill="#000000"', f'fill="{col}"')

def organs(stroke, sw=1.6, op=1):
    """Gold line art of oesophagus, liver, gallbladder, stomach, duodenum, pancreas and bowel (hub.py body-map paths)."""
    vb = " ".join(map(str, hub.VB))
    paths = [hub.ESOPH, hub.LIVER, hub.GB, hub.STOM, hub.DUO, hub.PANC, hub.BILE, hub.COLON, hub.SMALL]
    return (f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:100%;opacity:{op}">'
            + "".join(f'<path d="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>' for d in paths) + "</svg>")

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
@page{{size:{PW}in {PH}in;margin:0}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:{PW}in}}
body{{font-family:"FT",sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.card{{width:{PW}in;height:{PH}in;position:relative;overflow:hidden;page-break-after:always}}
.in{{position:absolute;left:{PAD}in;right:{PAD}in;top:{PAD}in;bottom:{PAD}in}}
.serif{{font-family:"YS",serif;font-weight:400}}
.k{{font-size:5pt;font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
/* tickets on the back */
.tk{{border-radius:.07in;overflow:hidden}}
.tk .d{{font-size:5.4pt;font-weight:600;letter-spacing:.14em;padding:.03in .07in;color:#fff}}
.tk .r{{display:flex;align-items:center;gap:.05in;padding:.035in .07in}}
.tk .r + .r{{padding-top:0}}
.tk .dot{{flex:none;width:.05in;height:.16in;border-radius:.02in}}
.tk .n{{font-family:"YS",serif;font-size:7.4pt;line-height:1.05}}
.tk .a{{font-size:5pt;opacity:.75}}
.tk .t{{margin-left:auto;font-family:"YS",serif;font-size:8.4pt;white-space:nowrap}}
"""

def tickets(light=True):
    """The week as two tickets. light=True: white tickets on cream; False: translucent on teal."""
    bg = "#FFFFFF" if light else "rgba(255,255,255,.1)"; fg = INK if light else "#FFFFFF"
    def row(name, area, t, col):
        return (f'<div class="r"><span class="dot" style="background:{col}"></span><div><div class="n" style="color:{fg}">{name}</div>'
                f'<div class="a" style="color:{fg}">{area}</div></div><div class="t" style="color:{col if light else GOLD2}">{t}</div></div>')
    sh = "box-shadow:0 .02in .05in rgba(14,42,39,.12);" if light else ""
    return (f'<div class="tk" style="background:{bg};{sh}"><div class="d" style="background:{SAFF}">MON · WED · FRI</div>'
            + row("Apollo Clinic", "Sector 52, Gurugram", "6 – 8 pm", SAFF) + "</div>"
            + f'<div class="tk" style="background:{bg};{sh}margin-top:.055in"><div class="d" style="background:{TEAL if light else "#0A5149"}">TUE · THU · SAT</div>'
            + row("Apollo Hospitals", "Golf Course Road", "4 – 6 pm", TEAL if light else "#8FE3D2")
            + row("Arcura Clinic", "Sector 51, Mayfield Garden", "6:30 – 8 pm", PLUM if light else GOLD2) + "</div>")

# ---------------- Design A: Midnight & gold ----------------
def a_front():
    return f"""<div class="card" style="background:radial-gradient(130% 120% at 85% 20%,#14423C 0%,{INK} 55%,#081C1A 100%);color:#fff">
 <div style="position:absolute;right:-.12in;top:.02in;width:2.05in;height:2.05in">{organs(GOLD, 1.5, .9)}</div>
 <div style="position:absolute;right:-.12in;top:.02in;width:2.05in;height:2.05in;filter:blur(3px)">{organs(GOLD2, 2.5, .35)}</div>
 <div class="in">
  <div style="display:flex;flex-direction:column;justify-content:space-between;height:100%">
  <div style="display:flex;align-items:center;gap:.06in"><div style="width:.28in;height:.28in;background:#fff;border-radius:.06in;padding:.015in">{MARK}</div>
   <span class="k" style="color:{GOLD2}">Gastroenterology · Liver · Endoscopy</span></div>
  <div>
   <div class="serif" style="font-size:17pt;line-height:1.02">Dr. Kshitij<br>Lochab</div>
   <div style="font-size:6.2pt;margin-top:.05in;color:#DCEDE9">Consultant Gastroenterologist &amp;<br>Therapeutic Endoscopist</div>
   <div style="font-size:5.4pt;margin-top:.025in;color:#A9C9C2">MBBS · MD · DrNB (Gastroenterology)<br>Advanced Fellowship in EUS &amp; ERCP</div>
   <div style="display:inline-block;margin-top:.05in;font-size:5.4pt;font-weight:600;color:{INK};background:linear-gradient(90deg,{GOLD},{GOLD2});border-radius:.05in;padding:.012in .06in">All-India Gold Medal · DrNB</div></div>
  <div><div class="serif" style="font-size:10.5pt;color:{GOLD2};letter-spacing:.01em">+91 96671 04882</div>
    <div style="font-size:5.4pt;color:#A9C9C2">Call or WhatsApp · drlochab.com · @drlochab</div></div>
 </div></div></div>"""

def a_back():
    return f"""<div class="card" style="background:{CREAM};color:{INK}">
 <div style="position:absolute;left:0;top:0;bottom:0;width:{BLEED + .09}in;background:linear-gradient(180deg,{GOLD},{GOLD2})"></div>
 <div class="in" style="left:{PAD + .06}in">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="k" style="color:#B5701A">Evening OPD · Gurugram</span><span style="font-size:5pt;color:#4A615D">Mon to Sat</span></div>
  <div style="display:flex;gap:.1in;margin-top:.05in">
   <div style="flex:1">{tickets(True)}</div>
   <div style="width:.62in;display:flex;flex-direction:column;align-items:center">
    <div style="width:.6in;height:.6in;background:#fff;border-radius:.06in;padding:.04in">{qr_svg("https://drlochab.com", INK)}</div>
    <div style="font-size:4.6pt;text-align:center;color:#4A615D;line-height:1.25;margin-top:.03in">Scan for timings,<br>directions &amp; health guides</div></div></div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:center;border-top:.6px solid #E3D7C2;padding-top:.035in">
   <span style="font-size:5.4pt"><b style="color:#B0362B">Urgent during the day?</b> Apollo Hospitals only · call first</span>
   <span style="font-size:4.8pt;color:#4A615D">HMC Reg. HN-23524</span></div>
 </div></div>"""

# ---------------- Design B: Bold portrait ----------------
def b_front():
    wave = (f'<svg viewBox="0 0 350 200" preserveAspectRatio="none" style="position:absolute;left:0;top:0;width:100%;height:100%">'
            f'<defs><linearGradient id="wv" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{DEEP}"/><stop offset="1" stop-color="#15A08C"/></linearGradient></defs>'
            f'<path d="M210 0 H350 V200 H170 C230 160 160 90 220 50 C240 36 220 14 210 0 Z" fill="url(#wv)"/>'
            f'<path d="M196 0 C206 16 226 38 206 52 C146 92 216 162 156 200" fill="none" stroke="{GOLD}" stroke-width="2.2"/></svg>')
    return f"""<div class="card" style="background:#FFFFFF;color:{INK}">{wave}
 <div style="position:absolute;right:{PAD + .08}in;top:{.38 + BLEED}in;width:1.1in;height:1.1in;border-radius:50%;padding:.04in;background:linear-gradient(135deg,{GOLD2},{GOLD});box-shadow:0 .03in .08in rgba(0,0,0,.25)">
  <img src="{PHOTO}" style="width:100%;height:100%;border-radius:50%;object-fit:cover;object-position:50% 16%"></div>
 <div class="in">
  <div style="display:flex;align-items:center;gap:.05in"><div style="width:.26in;height:.26in">{MARK}</div><span class="k" style="color:{TEAL}">drlochab.com</span></div>
  <div style="position:absolute;left:0;top:.42in;width:1.9in">
   <div class="serif" style="font-size:16pt;line-height:1.02">Dr. Kshitij<br>Lochab</div>
   <div style="width:.35in;height:2px;background:{GOLD};margin:.05in 0 .04in"></div>
   <div style="font-size:6.2pt;font-weight:600;color:{TEAL}">Consultant Gastroenterologist<br>&amp; Therapeutic Endoscopist</div>
   <div style="font-size:5.4pt;color:#4A615D;margin-top:.03in;line-height:1.35">MBBS · MD · DrNB (Gastroenterology)<br>All-India Gold Medal · Fellowship in EUS &amp; ERCP</div></div>
  <div style="position:absolute;left:0;bottom:0">
   <div class="serif" style="font-size:10.5pt;color:{INK}">+91 96671 04882</div>
   <div style="font-size:5.2pt;color:#4A615D">Appointments · Call or WhatsApp</div></div>
 </div></div>"""

def b_back():
    return f"""<div class="card" style="background:radial-gradient(120% 120% at 10% 0%,#13897A 0%,{DEEP} 50%,#084A42 100%);color:#fff">
 <div style="position:absolute;right:-.3in;bottom:-.35in;width:1.6in;height:1.6in;opacity:.18">{organs("#FFFFFF", 1.4)}</div>
 <div class="in">
  <div style="display:flex;justify-content:space-between;align-items:baseline"><span class="k" style="color:{GOLD2}">Evening OPD · Gurugram</span><span style="font-size:5pt;color:#CFE5E0">Monday to Saturday</span></div>
  <div style="display:flex;gap:.1in;margin-top:.05in">
   <div style="flex:1">{tickets(False)}</div>
   <div style="width:.62in;display:flex;flex-direction:column;align-items:center">
    <div style="width:.6in;height:.6in;background:#fff;border-radius:.06in;padding:.04in">{qr_svg("https://drlochab.com", INK)}</div>
    <div style="font-size:4.6pt;text-align:center;color:#CFE5E0;line-height:1.25;margin-top:.03in">Scan for timings<br>&amp; directions</div></div></div>
  <div style="position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;align-items:center;border-top:.6px solid rgba(255,255,255,.25);padding-top:.035in">
   <span style="font-size:5.4pt"><b style="color:{GOLD2}">Urgent during the day?</b> Apollo Hospitals only · call first</span>
   <span style="font-size:4.8pt;color:#CFE5E0">HMC Reg. HN-23524</span></div>
 </div></div>"""

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        for tag, fr, bk in (("A-midnight-gold", a_front, a_back), ("B-bold-portrait", b_front, b_back)):
            html = f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{fr()}{bk()}</body></html>"
            path = f"{OUT}/card.html"; open(path, "w").write(html)
            pg = b.new_page(); pg.goto(f"file://{path}"); pg.wait_for_timeout(500)
            pg.pdf(path=f"{OUT}/visiting-card-{tag}-print.pdf", width=f"{PW}in", height=f"{PH}in", print_background=True); pg.close()
            pv = b.new_page(viewport={"width": int(PW * 96), "height": int(PH * 96 * 2)}, device_scale_factor=6)
            pv.goto(f"file://{path}"); pv.wait_for_timeout(500)
            cards = pv.locator(".card")
            for i, nm in enumerate(["front", "back"]):
                box = cards.nth(i).bounding_box()
                pv.screenshot(path=f"{OUT}/card-{tag}-{nm}.png", clip={"x": box["x"] + BLEED * 96, "y": box["y"] + BLEED * 96, "width": W * 96, "height": H * 96})
            pv.close(); os.remove(path)
        b.close()
    print("done", sorted(os.listdir(OUT)))
