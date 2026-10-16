"""Hepatitis B is preventable: redesigned Instagram post (1080x1350), bolder and fuller than the week_2026_10_12 version.
Run from anywhere: python3 _src/social/hepb_post.py  -> _src/out/hepb/ig-hepatitis-b-v2.png"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from week_2026_10_12 import CSS, foot, shield, SRC
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "hepb"); os.makedirs(OUT, exist_ok=True)

TUBE = """<svg viewBox="0 0 120 120" style="width:118px;height:118px"><circle cx="60" cy="60" r="58" fill="#E6F2EF"/>
<g transform="rotate(20 60 60)"><rect x="46" y="20" width="28" height="78" rx="14" fill="#FFFFFF" stroke="#0D7466" stroke-width="5"/>
<path d="M49 62 H71 V84 a11 11 0 0 1 -22 0 Z" fill="#B0362B"/><rect x="42" y="16" width="36" height="10" rx="4" fill="#0D7466"/></g></svg>"""
SYRINGE = """<svg viewBox="0 0 120 120" style="width:118px;height:118px"><circle cx="60" cy="60" r="58" fill="#FCEBD0"/>
<g transform="rotate(-45 60 60)"><rect x="40" y="48" width="44" height="24" rx="5" fill="#FFFFFF" stroke="#0D7466" stroke-width="5"/>
<rect x="44" y="52" width="22" height="16" rx="3" fill="#9BD3EA"/><path d="M84 60 H100" stroke="#0D7466" stroke-width="4" stroke-linecap="round"/>
<path d="M40 60 H28 M28 50 V70" stroke="#0D7466" stroke-width="6" stroke-linecap="round"/><path d="M58 48 V42 M70 48 V42" stroke="#0D7466" stroke-width="4" stroke-linecap="round"/></g></svg>"""

FACTS = ["Often silent for years", "Can lead to cirrhosis and liver cancer", "Spreads through blood, unsafe needles, and mother to baby"]

POST = f"""<div class="s teal" style="width:1080px;height:1350px;padding:80px 72px">
 <div style="position:absolute;right:-180px;top:-180px;width:620px;height:620px;border-radius:50%;background:rgba(255,255,255,.06)"></div>
 <div style="position:absolute;left:-160px;bottom:120px;width:420px;height:420px;border-radius:50%;background:rgba(255,255,255,.05)"></div>
 <div class="kick" style="font-size:26px;color:#F3B84A;position:relative">Protect your liver</div>
 <h1 style="font-size:104px;margin-top:18px;position:relative">Hepatitis B is<br><em>preventable</em></h1>
 <div style="position:absolute;right:30px;top:290px;width:470px;height:470px;border-radius:50%;background:#E6F2EF"></div>
 <div style="position:absolute;right:65px;top:320px;width:400px;height:400px">{shield()}</div>
 <div style="position:absolute;left:72px;top:400px;width:520px;display:flex;flex-direction:column;gap:16px">
  {''.join(f'<div style="display:flex;gap:16px;align-items:flex-start;font-size:32px;line-height:1.3;color:#E6F2EF"><span style="flex:none;width:16px;height:16px;border-radius:50%;background:#F3B84A;margin-top:14px"></span>{t}</div>' for t in FACTS)}
 </div>
 <div style="position:absolute;left:72px;right:72px;top:780px;display:grid;grid-template-columns:1fr 1fr;gap:24px">
  <div style="background:#FFFFFF;color:#12302C;border-radius:36px;padding:30px 30px 34px;display:flex;flex-direction:column;gap:14px">
   <div style="display:flex;align-items:center;justify-content:space-between">{TUBE}<span style="font-family:YS;font-size:90px;color:#DDEEEA;line-height:1">1</span></div>
   <div class="kick" style="font-size:20px;color:#0D7466">Get tested</div>
   <div style="font-family:YS;font-size:42px;line-height:1.15">One blood test: HBsAg</div>
  </div>
  <div style="background:#FFFFFF;color:#12302C;border-radius:36px;padding:30px 30px 34px;display:flex;flex-direction:column;gap:14px">
   <div style="display:flex;align-items:center;justify-content:space-between">{SYRINGE}<span style="font-family:YS;font-size:90px;color:#FCEBD0;line-height:1">2</span></div>
   <div class="kick" style="font-size:20px;color:#B5542C">Get protected</div>
   <div style="font-family:YS;font-size:42px;line-height:1.15">Negative? Get the vaccine</div>
  </div>
 </div>
 <p style="position:absolute;left:72px;right:72px;top:1138px;font-size:28px;color:#CFE5E0">Positive? It can be treated and followed up. Family members should be tested too.</p>
 {foot(light=True)}</div>"""

if __name__ == "__main__":
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1080, "height": 1350})
        open(f"{OUT}/tmp.html", "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{POST}</body></html>")
        pg.goto(f"file://{OUT}/tmp.html"); pg.wait_for_timeout(400); pg.screenshot(path=f"{OUT}/ig-hepatitis-b-v2.png"); b.close()
    os.remove(f"{OUT}/tmp.html"); print("done")
