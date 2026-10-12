"""Visiting card, 3.5 x 2 in (88.9 x 50.8 mm) with 1/16 in bleed on every side.
Outputs a print-ready 2-page PDF (front, back) and PNG previews. python3 _src/social/visiting_card.py -> _src/out/card/"""
import io, os, re
import qrcode, qrcode.image.svg
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "card"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
MARK = open(f"{SRC}/brand/logo-mark.svg").read()

def qr_svg(data):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=0, image_factory=qrcode.image.svg.SvgPathImage)
    q.add_data(data); q.make(fit=True)
    buf = io.BytesIO(); q.make_image().save(buf)
    s = buf.getvalue().decode()
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    return s.replace('fill="#000000"', 'fill="#12302C"')

# Card geometry (CSS inches). Trim 3.5 x 2; bleed 0.0625 each side; safe zone 0.125 inside trim.
W, H, BLEED, SAFE = 3.5, 2.0, 0.0625, 0.125
PW, PH = W + 2 * BLEED, H + 2 * BLEED
PAD = BLEED + SAFE

PLACES = [
    ("Apollo Hospitals", "Golf Course Road, Gurugram", None, "Associate Consultant, Gastroenterology &amp; Therapeutic Endoscopy"),
    ("Apollo Clinic", "Sector 52, Gurugram", "2 – 5 pm", None),
    ("Arcura Clinic", "M2K Corporate Park, 14 Mayfield Garden, Sector 51", "Mon–Fri 6 – 8 pm<br>Sun 9 am – 1 pm", None),
]

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
@page{{size:{PW}in {PH}in;margin:0}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:{PW}in}}
body{{font-family:"FT",sans-serif;color:#12302C;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.card{{width:{PW}in;height:{PH}in;position:relative;overflow:hidden;page-break-after:always}}
.front{{background:#FBFAF7}}
.back{{background:#0B6A5E;color:#fff}}
.trim{{position:absolute;left:{BLEED}in;top:{BLEED}in;width:{W}in;height:{H}in;outline:.5px dashed #E0503D;display:none}}
.show-trim .trim{{display:block}}
/* front */
.band{{position:absolute;left:0;top:0;bottom:0;width:{BLEED + 0.16}in;background:#0B6A5E}}
.band::after{{content:"";position:absolute;right:0;top:0;bottom:0;width:.03in;background:#C9851F}}
.f{{position:absolute;left:{PAD + 0.12}in;right:{PAD}in;top:{PAD}in;bottom:{PAD}in;display:flex;flex-direction:column;justify-content:space-between}}
.mark{{position:absolute;right:0;top:0;width:.42in;height:.42in}} .mark svg{{width:100%;height:100%}}
.name{{font-family:"YS",serif;font-size:15.5pt;line-height:1.05;margin-top:.01in}}
.deg{{font-size:6.6pt;font-weight:600;color:#0D7466;margin-top:.045in;letter-spacing:.01em}}
.role{{font-size:6.8pt;margin-top:.035in;line-height:1.3}}
.gold{{display:inline-block;margin-top:.05in;font-size:6pt;font-weight:600;color:#7A4E0E;background:#FAEED8;border-radius:.06in;padding:.012in .06in}}
.int{{display:flex;align-items:center;gap:.06in;font-size:6pt;color:#4A615D}}
.int i{{flex:0 0 .22in;height:.6px;background:#C9851F}}
.int span{{font-weight:600;color:#0D7466}}
.bot{{display:flex;justify-content:space-between;align-items:flex-end}}
.contact{{font-size:6.8pt;line-height:1.45}}
.contact b{{font-family:"YS",serif;font-weight:400;font-size:11pt;letter-spacing:.01em}}
.contact .small{{font-size:6pt;color:#4A615D}}
.qr{{width:.5in;text-align:center}}
.qr svg{{width:.5in;height:.5in;display:block}}
.qr span{{display:block;font-size:4.8pt;color:#4A615D;margin-top:.02in}}
/* back */
.b{{position:absolute;left:{PAD}in;right:{PAD}in;top:{PAD}in;bottom:{PAD}in;display:flex;flex-direction:column}}
.bh{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:.6px solid rgba(255,255,255,.3);padding-bottom:.035in}}
.bh .k{{font-size:5.6pt;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#F3C66B}}
.bh .k2{{font-size:5.6pt;color:#CFE5E0}}
.pl{{display:grid;grid-template-columns:1fr auto;gap:.02in .08in;padding:.042in 0;border-bottom:.6px solid rgba(255,255,255,.18)}}
.pl:last-of-type{{border-bottom:0}}
.pl .n{{font-family:"YS",serif;font-size:8.6pt;line-height:1.1}}
.pl .a{{font-size:5.9pt;color:#CFE5E0;line-height:1.3;grid-column:1}}
.pl .r{{font-size:5.6pt;color:#CFE5E0;font-style:italic;grid-column:1}}
.pl .t{{grid-column:2;grid-row:1/4;align-self:center;text-align:right;font-size:6.6pt;font-weight:600;color:#fff;white-space:nowrap;line-height:1.35;
 background:rgba(255,255,255,.12);border-radius:.06in;padding:.03in .065in}}
.bf{{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:6.6pt}}
.bf b{{font-family:"YS",serif;font-weight:400;font-size:8.4pt;color:#F3C66B}}
.bf .reg{{font-size:5.2pt;color:#CFE5E0}}
"""

def front():
    return f"""<div class="card front"><div class="band"></div><div class="trim"></div><div class="f">
 <div class="mark">{MARK}</div>
 <div>
  <div class="name">Dr. Kshitij Lochab</div>
  <div class="deg">MBBS · MD (Medicine) · DrNB (Gastroenterology)</div>
  <div class="role">Consultant Gastroenterologist &amp;<br>Therapeutic Endoscopist · Fellowship in EUS &amp; ERCP</div>
  <div class="gold">All-India Gold Medal, DrNB</div>
 </div>
 <div class="int"><i></i>Liver <span>·</span> Pancreas &amp; bile ducts <span>·</span> Stomach &amp; bowel <span>·</span> Endoscopy</div>
 <div class="bot">
  <div class="contact"><b>+91 96671 04882</b><br>Appointments &amp; video consultations<br>Call or WhatsApp · <span class="small">drlochab.com · @drlochab</span></div>
  <div class="qr">{qr_svg("https://drlochab.com")}<span>Scan for website</span></div>
 </div>
</div></div>"""

def back():
    rows = "".join(
        f'<div class="pl"><div class="n">{n}</div><div class="a">{a}</div>{f"<div class=r>{r}</div>" if r else ""}{f'<div class="t">{t}</div>' if t else ""}</div>'
        for n, a, t, r in PLACES)
    return f"""<div class="card back"><div class="trim"></div><div class="b">
 <div class="bh"><span class="k">Consultations</span><span class="k2">Gastroenterology · Liver · Endoscopy</span></div>
 {rows}
 <div class="bf"><span>Appointments: <b>+91 96671 04882</b></span><span class="reg">HMC Reg. No. HN-23524</span></div>
</div></div>"""

if __name__ == "__main__":
    html = f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{front()}{back()}</body></html>"
    path = f"{OUT}/card.html"; open(path, "w").write(html)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(); pg.goto(f"file://{path}"); pg.wait_for_timeout(400)
        pg.pdf(path=f"{OUT}/visiting-card-print.pdf", width=f"{PW}in", height=f"{PH}in", print_background=True)
        # previews: trimmed size, 6x scale
        pv = b.new_page(viewport={"width": int(PW * 96), "height": int(PH * 96 * 2)}, device_scale_factor=6)
        pv.goto(f"file://{path}"); pv.wait_for_timeout(400)
        cards = pv.locator(".card")
        for i, nm in enumerate(["front", "back"]):
            box = cards.nth(i).bounding_box()
            pv.screenshot(path=f"{OUT}/card-{nm}.png", clip={"x": box["x"] + BLEED * 96, "y": box["y"] + BLEED * 96, "width": W * 96, "height": H * 96})
        b.close()
    os.remove(path); print("done")
