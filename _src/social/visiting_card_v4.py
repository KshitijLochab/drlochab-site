"""Visiting cards v4 (19 Nov 2026): two more directions built on the chosen card 2 (visiting_card_v3.mh_front / mh_back).
  4 Teal reverse: the chosen layout on deep teal with gold-foil name and line drawing; warm off-white back with the timetable.
  5 Monogram:     deep teal front with a large gold 'KL' monogram in a fine gold ring, name and roles beside a gold rule;
                  off-white back with the timetable.
3.5 x 2 in, 1/16 in bleed, print PDF + previews + mock-up, same as v3.
Run: python3 _src/social/visiting_card_v4.py -> _src/out/card-v4/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import visiting_card_v3 as v3
from visiting_card_v3 import MARK, FOIL, PHONE, SITE, OPD, BLEED, qr_svg, gut_line, css, mockup
from playwright.sync_api import sync_playwright

OUT = os.path.join(v3.SRC, "out", "card-v4"); os.makedirs(OUT, exist_ok=True)
TEALBG = "background:linear-gradient(160deg,#0F6B5F 0%,#0A4D45 70%,#083F39 100%);color:#fff"
CREAM, INK, MUTE, GOLDT, GOLD = "#F6F2EA", "#13241F", "#6D7A73", "#A2741C", "#C69A3E"

def cream_back():
    rows = "".join(f'<div style="display:grid;grid-template-columns:.8in 1fr auto;align-items:center;gap:.06in;padding:.04in 0;border-top:.5pt solid #E2D9C8">'
                   f'<span class="cap" style="font-size:5.6pt;color:{GOLDT};letter-spacing:.1em">{d}</span>'
                   f'<div style="line-height:1.15"><div class="serif" style="font-size:8.6pt">{p}</div><div style="font-size:6pt;color:{MUTE}">{a}, Gurugram</div></div>'
                   f'<span style="font-size:7.6pt;font-weight:600;white-space:nowrap">{t}</span></div>' for d, p, a, t in OPD)
    return f"""<div class="card" style="background:{CREAM};color:{INK}">
 <div class="in"><div style="display:flex;gap:.14in;height:100%">
  <div style="flex:1;display:flex;flex-direction:column">
   <div style="display:flex;align-items:baseline;gap:.06in"><span class="cap" style="font-size:5.8pt;color:{GOLDT}">Evening OPD</span><span class="serif" style="font-size:9pt">Monday to Saturday</span></div>
   <div style="margin-top:.04in">{rows}<div style="border-top:.5pt solid #E2D9C8"></div></div>
   <div style="margin-top:auto;padding-left:.06in;border-left:1pt solid #B0362B;font-size:6pt"><b style="color:#B0362B">Urgent during the day?</b> Apollo Hospitals only. Call first.</div></div>
  <div style="width:.62in;display:flex;flex-direction:column;align-items:center;justify-content:space-between">
   <div style="text-align:center"><div style="width:.6in;height:.6in">{qr_svg("https://drlochab.com", "#0A4D45")}</div>
    <div style="font-size:5.2pt;color:{MUTE};margin-top:.03in">Scan: directions</div></div>
   <div style="display:flex;flex-direction:column;align-items:center;gap:.03in"><div style="width:.22in;height:.22in">{MARK}</div>
    <div style="font-size:5.2pt;line-height:1.4;color:{MUTE};text-align:center">HMC Reg.<br>HN-23524</div></div></div>
 </div></div></div>"""

def reverse_front():
    return f"""<div class="card" style="{TEALBG}">
 <div style="position:absolute;right:.2in;top:.5in;width:.85in;height:1.15in">{gut_line("#D9B061", 1.5)}</div>
 <div class="in">
  <div style="position:absolute;right:0;top:0;width:.26in;height:.26in">{MARK}</div>
  <div style="position:absolute;left:0;top:0">
   <div style="font-size:6.6pt;color:#BFDCD5;letter-spacing:.06em">Dr.</div>
   <div class="serif foil" style="font-size:19pt;line-height:1.02">Kshitij Lochab</div>
   <div style="width:.5in;height:1.2pt;background:{FOIL};margin:.06in 0 .05in"></div>
   <div style="font-size:7pt;line-height:1.35;color:#E6F2EF">Consultant Gastroenterologist &amp; Therapeutic Endoscopist</div>
   <div style="font-size:7pt;line-height:1.35;color:#9FE0D2;font-weight:600">Associate Consultant, Apollo Hospitals, Gurugram</div>
   <div style="margin-top:.07in;padding-left:.07in;border-left:1.2pt solid #D9B061">
    <div class="cap" style="font-size:6pt;letter-spacing:.2em;color:#EBC874">All-India Gold Medal</div>
    <div style="font-size:6pt;color:#BFDCD5;margin-top:.015in">DrNB Gastroenterology · Medanta</div></div></div>
  <div style="position:absolute;left:0;bottom:0;display:flex;align-items:flex-end;gap:.12in">
   <div><div class="serif" style="font-size:10pt">{PHONE}</div><div style="font-size:6pt;color:#BFDCD5;margin-top:.01in">Call or WhatsApp</div></div>
   <div style="width:.6pt;height:.28in;background:#D9B061"></div>
   <div><div class="serif foil" style="font-size:10pt">{SITE}</div><div style="font-size:6pt;color:#BFDCD5;margin-top:.01in">Timings, directions, health guides</div></div></div>
 </div></div>"""

def monogram_front():
    return f"""<div class="card" style="{TEALBG}">
 <div class="in" style="display:flex;align-items:center;gap:.16in">
  <div style="flex:none;width:1.02in;height:1.02in;border-radius:50%;border:1pt solid #D9B061;display:flex;align-items:center;justify-content:center;position:relative">
   <div style="position:absolute;inset:.05in;border-radius:50%;border:.4pt solid rgba(217,176,97,.6)"></div>
   <span class="serif foil" style="font-size:34pt;letter-spacing:-.02em;line-height:1">KL</span></div>
  <div style="width:.6pt;align-self:stretch;margin:.12in 0;background:linear-gradient(180deg,transparent,#D9B061,transparent)"></div>
  <div style="flex:1;min-width:0">
   <div class="serif" style="font-size:14.5pt;line-height:1.05">Dr. Kshitij Lochab</div>
   <div style="font-size:6.6pt;line-height:1.4;color:#E6F2EF;margin-top:.05in">Consultant Gastroenterologist<br>&amp; Therapeutic Endoscopist</div>
   <div style="font-size:6.6pt;color:#9FE0D2;font-weight:600;margin-top:.02in">Associate Consultant, Apollo Hospitals</div>
   <div class="cap" style="font-size:5.6pt;letter-spacing:.2em;color:#EBC874;margin-top:.07in">All-India Gold Medal · DrNB</div>
   <div style="margin-top:.1in;display:flex;gap:.1in;align-items:baseline"><span class="serif" style="font-size:9pt;white-space:nowrap">{PHONE}</span>
    <span class="serif foil" style="font-size:9pt">{SITE}</span></div>
  </div>
 </div></div>"""

DESIGNS = [("4-teal-reverse", reverse_front, cream_back, "#CFC7B8"), ("5-monogram", monogram_front, cream_back, "#C9C1B2")]

if __name__ == "__main__":
    w, h = 3.5, 2.0; pw, ph = w + 2 * BLEED, h + 2 * BLEED
    with sync_playwright() as p:
        b = p.chromium.launch()
        for tag, fr, bk, bg in DESIGNS:
            path = f"{OUT}/card.html"
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)}</style></head><body>{fr()}{bk()}</body></html>")
            pg = b.new_page(); pg.goto(f"file://{path}"); pg.wait_for_timeout(500)
            pg.pdf(path=f"{OUT}/card-{tag}-print.pdf", width=f"{pw}in", height=f"{ph}in", print_background=True); pg.close()
            pv = b.new_page(viewport={"width": int(pw * 96) + 2, "height": int(ph * 96 * 2) + 2}, device_scale_factor=6)
            pv.goto(f"file://{path}"); pv.wait_for_timeout(500)
            for i, nm in enumerate(["front", "back"]):
                box = pv.locator(".card").nth(i).bounding_box()
                pv.screenshot(path=f"{OUT}/card-{tag}-{nm}.png", clip={"x": box["x"] + BLEED * 96, "y": box["y"] + BLEED * 96, "width": w * 96, "height": h * 96})
            pv.close()
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)} .card{{page-break-after:auto}}</style></head><body style='margin:0'>{mockup(fr, bk, w, h, bg)}</body></html>")
            pm = b.new_page(viewport={"width": 2400, "height": 1600}); pm.goto(f"file://{path}"); pm.wait_for_timeout(600)
            pm.screenshot(path=f"{OUT}/mockup-{tag}.png"); pm.close(); os.remove(path)
        b.close()
    print("done", sorted(os.listdir(OUT)))
