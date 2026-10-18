"""Practo profile cover images (18 Oct 2026). No phone numbers or web addresses inside the image (directories reject them).
Wide banner 1920x480 (4:1, text kept in the centre safe area) and 16:9 1920x1080 with portrait.
python3 _src/social/practo_cover.py -> _src/out/practo/"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gbp_brand import FONTS, PHOTO, TUBE, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "practo"); os.makedirs(OUT, exist_ok=True)
PIN = '<svg width="24" height="30" viewBox="0 0 24 30"><path d="M12 1C6 1 1.5 5.5 1.5 11.3 1.5 19 12 29 12 29s10.5-10 10.5-17.7C22.5 5.5 18 1 12 1z" fill="#F3B84A"/><circle cx="12" cy="11" r="4" fill="#0B6A5E"/></svg>'

WIDE = f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}
*{{box-sizing:border-box;margin:0}}
body{{width:1920px;height:480px;overflow:hidden;font-family:"FT",sans-serif;color:#fff;
 background:radial-gradient(120% 160% at 30% 40%,#0F7D6E 0%,#0B6A5E 45%,#084A42 100%)}}
.motif{{position:absolute;right:120px;top:-220px;width:760px;height:760px;opacity:.12}}
.motif2{{position:absolute;left:-160px;top:120px;width:520px;height:520px;opacity:.06}}
.txt{{position:absolute;left:330px;right:330px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.kick{{font-weight:600;letter-spacing:.2em;text-transform:uppercase;font-size:22px;color:#F3B84A}}
h1{{font-family:"YS",serif;font-weight:400;font-size:62px;line-height:1.1;margin-top:14px}}
.chips{{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-top:24px}}
.chips span{{font-size:22px;font-weight:600;padding:10px 20px;border-radius:999px;background:rgba(255,255,255,.12);border:1.5px solid rgba(255,255,255,.25)}}
.chips span.gold{{background:#F3B84A;color:#12302C;border-color:#F3B84A}}
.place{{margin-top:22px;font-size:22px;color:#CFE5E0;display:flex;align-items:center;gap:10px}}
</style></head><body>
<svg class="motif" viewBox="0 -6 64 64"><path d="{TUBE}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>
<svg class="motif2" viewBox="0 -6 64 64"><path d="{TUBE}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/></svg>
<div class="txt">
 <div class="kick">Gastroenterology · Liver · Pancreas · Endoscopy</div>
 <h1>Consultant Gastroenterologist &amp; Therapeutic Endoscopist</h1>
 <div class="chips"><span class="gold">All-India Gold Medal, DrNB Gastroenterology</span><span>Advanced Fellowship in EUS &amp; ERCP</span><span>Medanta trained</span></div>
 <p class="place">{PIN}Arcura Clinic, Mayfield Garden, Sector 51, Gurugram</p>
</div>
</body></html>"""

FULL = f"""<!doctype html><html><head><meta charset=utf-8><style>{FONTS}
*{{box-sizing:border-box;margin:0}}
body{{width:1920px;height:1080px;overflow:hidden;font-family:"FT",sans-serif;color:#12302C;
 background:linear-gradient(90deg,#F2EEEA 0%,#EAE5E1 45%,#E6E1DD 62%,#E3DED9 100%)}}
.photo{{position:absolute;right:0;bottom:0;width:900px;height:1080px;background:url({PHOTO}) center top/cover;
 -webkit-mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.35) 18%,#000 40%,#000 100%);mask-image:linear-gradient(90deg,transparent 0%,rgba(0,0,0,.35) 18%,#000 40%,#000 100%)}}
.motif{{position:absolute;left:-120px;top:-180px;width:1100px;height:1100px;opacity:.08}}
.txt{{position:absolute;left:150px;top:220px;width:920px}}
.kick{{font-weight:600;letter-spacing:.18em;text-transform:uppercase;font-size:24px;color:#0D7466}}
h1{{font-family:"YS",serif;font-weight:400;font-size:104px;line-height:1.02;margin-top:22px}}
.role{{font-size:38px;margin-top:22px;line-height:1.35}}
.chips{{display:flex;flex-wrap:wrap;gap:14px;margin-top:40px;max-width:860px}}
.chips span{{font-size:25px;font-weight:600;padding:12px 24px;border-radius:999px;background:#FFFFFF;border:2px solid #D3E0DC}}
.chips span.gold{{background:#0B6A5E;color:#fff;border-color:#0B6A5E}}
.care{{margin-top:34px;font-size:27px;color:#4A615D;line-height:1.5;max-width:820px}}
.place{{margin-top:30px;font-size:28px;color:#4A615D;display:flex;align-items:center;gap:14px}}
</style></head><body>
<svg class="motif" viewBox="0 -6 64 64"><path d="{TUBE}" fill="none" stroke="#0B6A5E" stroke-width="7" stroke-linecap="round"/></svg>
<div class="photo"></div>
<div class="txt">
 <div class="kick">Gastroenterology · Liver · Endoscopy</div>
 <h1>Dr. Kshitij Lochab</h1>
 <p class="role">Consultant Gastroenterologist &amp;<br>Therapeutic Endoscopist</p>
 <div class="chips"><span class="gold">All-India Gold Medal, DrNB</span><span>EUS &amp; ERCP Fellowship</span><span>Medanta trained</span></div>
 <p class="care">Acidity and ulcers · Fatty liver and hepatitis · Gallbladder, bile duct and pancreas · IBS and IBD · Endoscopy and colonoscopy</p>
 <p class="place">{PIN.replace('#F3B84A','#0D7466').replace('#0B6A5E','#fff')}Arcura Clinic, Sector 51, Gurugram</p>
</div>
</body></html>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, html, w, h in [("practo-cover-wide", WIDE, 1920, 480), ("practo-cover-16x9", FULL, 1920, 1080)]:
            pg = b.new_page(viewport={"width": w, "height": h})
            open(f"{OUT}/tmp.html", "w").write(html); pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400)
            pg.screenshot(path=f"{OUT}/{name}.png"); pg.close()
        b.close()
    os.remove(f"{OUT}/tmp.html")
    from PIL import Image
    for n in ("practo-cover-wide", "practo-cover-16x9"):
        Image.open(f"{OUT}/{n}.png").convert("RGB").save(f"{OUT}/{n}.jpg", quality=92)
    print("done")
