"""Google Business Profile logo (720x720) and cover photo (1920x1080).
python3 _src/social/gbp_brand.py -> _src/out/gbp/"""
import base64, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SRC, "out", "gbp"); os.makedirs(OUT, exist_ok=True)
F = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
MARK = open(f"{SRC}/brand/logo-mark.svg").read()
PHOTO = "data:image/jpeg;base64," + b64(f"{SRC}/brand/portrait-hires.jpg")
FONTS = f"""@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}"""

# Google shows the logo inside a circle: keep the mark well inside it.
LOGO = f"""<!doctype html><html><head><meta charset=utf-8><style>*{{margin:0}}
body{{width:720px;height:720px;background:radial-gradient(circle at 50% 42%,#FFFFFF 0%,#F3F7F6 70%,#E4EEEB 100%);display:grid;place-items:center}}
.m{{width:430px;height:430px;filter:drop-shadow(0 18px 30px rgba(11,74,66,.25))}} .m svg{{width:100%;height:100%}}
</style></head><body><div class="m">{MARK}</div></body></html>"""

# The tube line from the logo, drawn large as a background motif.
TUBE = "M25.5 -4 V17 C25.5 24 15.5 27.5 15.5 37 C15.5 46.5 22.5 52.5 32 52.5 C41.5 52.5 48.5 46 48.5 37.5 C48.5 31 45 26.5 39.5 25.5"
COVER = f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}
*{{box-sizing:border-box;margin:0}}
body{{width:1920px;height:1080px;overflow:hidden;font-family:"FT",sans-serif;color:#12302C;
 background:linear-gradient(90deg,#F2EEEA 0%,#EAE5E1 45%,#E6E1DD 62%,#E3DED9 100%)}}
.photo{{position:absolute;right:0;bottom:0;width:900px;height:1080px;background:url({PHOTO}) center top/cover;
 -webkit-mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.35) 18%,#000 40%,#000 100%);mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.35) 18%,#000 40%,#000 100%)}}
.motif{{position:absolute;left:-120px;top:-180px;width:1100px;height:1100px;opacity:.08}}
.txt{{position:absolute;left:150px;top:230px;width:900px}}
.kick{{font-weight:600;letter-spacing:.18em;text-transform:uppercase;font-size:24px;color:#0D7466}}
h1{{font-family:"YS",serif;font-weight:400;font-size:104px;line-height:1.02;margin-top:22px}}
.role{{font-size:38px;margin-top:22px;line-height:1.35}}
.chips{{display:flex;flex-wrap:wrap;gap:14px;margin-top:40px;max-width:820px}}
.chips span{{font-size:25px;font-weight:600;padding:12px 24px;border-radius:999px;background:#FFFFFF;border:2px solid #D3E0DC}}
.chips span.gold{{background:#0B6A5E;color:#fff;border-color:#0B6A5E}}
.place{{margin-top:44px;font-size:28px;color:#4A615D;display:flex;align-items:center;gap:14px}}
.place b{{color:#0D7466;font-weight:600}}
</style></head><body>
<svg class="motif" viewBox="0 -6 64 64"><path d="{TUBE}" fill="none" stroke="#0B6A5E" stroke-width="7" stroke-linecap="round"/></svg>
<div class="photo"></div>
<div class="txt">
 <div class="kick">Gastroenterology · Liver · Endoscopy</div>
 <h1>Dr. Kshitij Lochab</h1>
 <p class="role">Consultant Gastroenterologist &amp;<br>Therapeutic Endoscopist</p>
 <div class="chips"><span class="gold">All-India Gold Medal, DrNB</span><span>EUS &amp; ERCP Fellowship</span><span>Medanta trained</span></div>
 <p class="place"><svg width="26" height="32" viewBox="0 0 24 30"><path d="M12 1C6 1 1.5 5.5 1.5 11.3 1.5 19 12 29 12 29s10.5-10 10.5-17.7C22.5 5.5 18 1 12 1z" fill="#0D7466"/><circle cx="12" cy="11" r="4" fill="#fff"/></svg>Arcura Clinic, Sector 51, Gurugram &nbsp;·&nbsp; <b>drlochab.com</b></p>
</div>
</body></html>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, html, w, h in [("google-logo", LOGO, 720, 720), ("google-cover", COVER, 1920, 1080)]:
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(html); pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/{name}.png"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html")
    from PIL import Image, ImageDraw
    # preview of the circular crop Google applies to the logo
    lg = Image.open(f"{OUT}/google-logo.png").convert("RGBA"); m = Image.new("L", lg.size, 0)
    ImageDraw.Draw(m).ellipse([0, 0, lg.size[0], lg.size[1]], fill=255); lg.putalpha(m); lg.save(f"{OUT}/logo-circle-preview.png")
    Image.open(f"{OUT}/google-cover.png").convert("RGB").save(f"{OUT}/google-cover.jpg", quality=90)
    print("done")
