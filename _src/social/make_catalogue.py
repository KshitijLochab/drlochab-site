"""Square (1080x1080) WhatsApp catalogue images for Dr. Kshitij Lochab's services."""
import base64, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import condition_art as CA
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.dirname(HERE)
D = os.path.join(SRC, "out", "catalogue"); os.makedirs(D, exist_ok=True)
FONTS = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = "data:image/png;base64," + b64(f"{SRC}/brand/logo-mark.png")
PHOTO = "data:image/jpeg;base64," + b64(f"{SRC}/dr-lochab.jpg")
IL = json.load(open(f"{SRC}/data-en.json"))["IL"]
MAP = open(f"{HERE}/map.svg").read()
ILCSS = open(f"{SRC}/insta/illus.css").read()
MAPCSS = open(f"{HERE}/map.css").read()

def organ_map(organ):
    k = f'class="organ" data-organ="{organ}"'
    assert k in MAP, organ
    return MAP.replace(k, f'class="organ on" data-organ="{organ}"', 1)

def portrait(badge=None):
    b = f'<span class="badge">{badge}</span>' if badge else ""
    return f'<div class="photo" style="background-image:url({PHOTO})">{b}</div>'

ITEMS = [
 ("01-clinic-consultation", "Clinic consultation", "Assessment and treatment of stomach, liver, intestine, gallbladder and pancreas problems.", portrait()),
 ("02-video-consultation", "Video consultation", "Follow-ups, report reviews and diet advice by WhatsApp video call.", portrait("Video call")),
 ("03-upper-gi-endoscopy", "Upper GI endoscopy", "Camera test of the food pipe, stomach and duodenum. About 10 to 15 minutes.", IL["gastro"]),
 ("04-colonoscopy", "Colonoscopy", "Examination of the large bowel, with polyp removal in the same test.", IL["colono"]),
 ("05-eus", "Endoscopic ultrasound (EUS)", "Close imaging of the pancreas and bile duct, with needle sampling.", IL["eus"]),
 ("06-ercp", "ERCP", "Removal of bile duct stones and stenting of blockages, without surgery.", IL["ercp"]),
 ("07-fatty-liver-care", "Fatty liver care", "Checks for liver fat and scarring, with a diet and weight-loss plan to reverse it.", CA.fatty_liver()),
 ("08-ibs-care", "IBS care", "Diet, routine and medical treatment for bloating, pain and bowel trouble.", CA.ibs()),
 ("09-ibd-care", "IBD care", "Long-term treatment of ulcerative colitis and Crohn's disease to keep the bowel calm.", CA.ibd()),
 ("10-pancreatitis-care", "Pancreatitis care", "Treatment of acute and chronic pancreatitis, with EUS and ERCP for complications.", CA.pancreatitis()),
]

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{FONTS}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-600.ttf");font-weight:600}}
:root{{--bg:#F3F7F6;--surface:#FFFFFF;--ink:#12302C;--muted:#4A615D;--line:#D3E0DC;--accent:#0D7466;--accent-ink:#FFFFFF;--accent-soft:#DDEEEA;
--warm:#C9851F;--warm-soft:#FAEED8;--urgent:#B0362B;--organ:#CADDD8;--organ-line:#97B6AF;--mark:#0B6A5E;--body:"FT"}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;height:1080px;overflow:hidden;background:var(--bg);font-family:"FT",sans-serif;color:var(--ink)}}
.s{{width:1080px;height:1080px;padding:56px;display:flex;flex-direction:column;gap:36px}}
.art{{flex:1;min-height:0;background:var(--surface);border-radius:36px;overflow:hidden;display:grid;place-items:center;padding:24px}}
.art > svg{{width:100%;height:100%}}
.photo{{width:100%;height:100%;border-radius:24px;background-size:cover;background-position:center 15%;position:relative}}
.badge{{position:absolute;left:24px;bottom:24px;background:var(--mark);color:#fff;font-weight:600;font-size:30px;padding:12px 24px;border-radius:999px}}
.txt{{display:flex;flex-direction:column;gap:12px}}
h1{{font-family:"YS",serif;font-weight:400;font-size:66px;line-height:1.05}}
p{{font-size:32px;line-height:1.35;color:var(--muted)}}
.foot{{display:flex;align-items:center;justify-content:space-between;border-top:2px solid var(--line);padding-top:24px}}
.brand{{display:flex;align-items:center;gap:16px}}
.brand img{{width:60px;height:60px}}
.brand b{{font-family:"YS",serif;font-weight:400;font-size:28px;display:block}}
.brand span{{font-size:20px;color:var(--muted)}}
.site{{font-weight:600;font-size:26px;color:var(--accent)}}
{ILCSS}
{MAPCSS}
.organ.on .fill{{fill:var(--accent);stroke:var(--accent)}} .organ.on .tube{{stroke:var(--accent)}} .organ.on .coil{{stroke:#fff}}
"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1080})
    for name, title, desc, art in ITEMS:
        html = (f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class='s'>"
                f"<div class='art'>{art}</div><div class='txt'><h1>{title}</h1><p>{desc}</p></div>"
                f"<div class='foot'><div class='brand'><img src='{LOGO}'><div><b>Dr. Kshitij Lochab</b><span>Gastroenterologist · Sector 51, Gurugram</span></div></div><span class='site'>drlochab.com</span></div>"
                "</div></body></html>")
        open(f"{D}/tmp.html", "w").write(html)
        pg.goto(f"file://{D}/tmp.html"); pg.wait_for_timeout(250)
        pg.screenshot(path=f"{D}/{name}.png")
    b.close()
print("done")
