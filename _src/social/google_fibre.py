"""Google Business Profile post (1200x900): fibre fuel gauge. python3 _src/social/google_fibre.py -> _src/out/google/fibre.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from story_fibre import gauge, icon, ICONS, LOGO, F, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "google"); os.makedirs(OUT, exist_ok=True)
HTML = f"""<!doctype html><html><head><meta charset=utf-8><style>
@font-face{{font-family:"YS";src:url("file://{F}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{F}/Figtree-600.ttf");font-weight:600}}
*{{box-sizing:border-box;margin:0}}
body{{width:1200px;height:900px;overflow:hidden;font-family:"FT",sans-serif;color:#12302C;
 background:radial-gradient(90% 90% at 70% 40%,#FFF6E4 0%,#FCEBD0 60%,#F6DDB4 100%)}}
.kick{{font-weight:600;letter-spacing:.16em;text-transform:uppercase}}
h1{{font-family:"YS",serif;font-weight:400;line-height:1.02}}
em{{font-style:normal;color:#B0362B}}
</style></head><body>
 <div style="position:absolute;left:64px;top:60px;width:540px">
  <div class="kick" style="font-size:20px;color:#0D7466">Gut health tip</div>
  <h1 style="font-size:76px;margin-top:14px">Is your gut running on <em>empty?</em></h1>
  <p style="font-size:28px;line-height:1.4;margin-top:22px">Most of us eat too little fibre.<br>Aim for <b style="font-family:YS;font-weight:400;font-size:38px;color:#0D7466;white-space:nowrap">25–30 g</b> a day.</p>
 </div>
 <div style="position:absolute;right:50px;top:70px;width:560px">{gauge()}</div>
 <div style="position:absolute;left:64px;right:64px;top:530px">
  <div class="kick" style="font-size:18px;color:#4A615D;margin-bottom:14px">Fill up with</div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">
   {''.join(f'<div style="background:#fff;border-radius:28px;padding:14px 10px 18px;text-align:center"><div style="width:120px;height:120px;margin:0 auto">{icon(k)}</div><div style="font-size:24px;font-weight:600;margin-top:4px">{k}</div></div>' for k in ICONS)}
  </div>
 </div>
 <div style="position:absolute;left:64px;right:64px;bottom:42px;display:flex;align-items:center;justify-content:space-between">
  <div style="display:flex;align-items:center;gap:14px"><img src="{LOGO}" style="width:60px;height:60px">
   <div><b style="font-family:YS;font-weight:400;font-size:26px;display:block">Dr. Kshitij Lochab</b><span style="font-size:19px;color:#4A615D">Gastroenterologist · Sector 51, Gurugram</span></div></div>
  <span style="font-weight:600;font-size:24px;color:#0D7466">drlochab.com</span>
 </div>
</body></html>"""
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1200, "height": 900})
    open(f"{OUT}/tmp.html", "w").write(HTML); pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(300)
    pg.screenshot(path=f"{OUT}/fibre.png"); b.close()
os.remove(f"{OUT}/tmp.html"); print("done")
