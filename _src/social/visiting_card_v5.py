"""Visiting cards v5 (19 Nov 2026): the chosen card-2 layout in colour schemes other than teal and cream.
  A Midnight navy & gold      navy front, gold-foil name; ivory back
  B Graphite & copper         charcoal front, copper-foil name; warm grey-white back
  C Oxblood & gold            deep wine front, gold-foil name; ivory back
  D Monochrome & one accent   pure white front, black type, one fine terracotta line; black back
The logo mark is recoloured to each scheme (teal background replaced; white swirl and gold dot kept).
3.5 x 2 in with 1/16 in bleed; print PDF, previews, mock-ups and one comparison board.
Run: python3 _src/social/visiting_card_v5.py -> _src/out/card-v5/"""
import base64, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import visiting_card_v3 as v3
from visiting_card_v3 import PHONE, SITE, OPD, BLEED, qr_svg, gut_line, css, mockup
from PIL import Image
from playwright.sync_api import sync_playwright

OUT = os.path.join(v3.SRC, "out", "card-v5"); os.makedirs(OUT, exist_ok=True)
hexrgb = lambda h: tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))

def logo(bg, fg="#FFFFFF"):
    """logo-mark.png with its teal square recoloured to bg and the white swirl to fg (gold dot unchanged)."""
    im = Image.open(f"{v3.SRC}/brand/logo-mark.png").convert("RGBA").resize((256, 256), Image.LANCZOS)
    B, F = hexrgb(bg), hexrgb(fg); px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b, a = px[x, y]
            if a == 0 or (r > 150 and b < 110):      # transparent corners, gold dot
                continue
            t = max(0.0, min(1.0, (r - 11) / 244))     # 0 = teal, 1 = white
            px[x, y] = tuple(int(B[i] * (1 - t) + F[i] * t) for i in range(3)) + (a,)
    buf = io.BytesIO(); im.save(buf, "PNG")
    return f'<img src="data:image/png;base64,{base64.b64encode(buf.getvalue()).decode()}" style="width:100%;height:100%;display:block">'

THEMES = {
 "A-navy-gold": dict(front="linear-gradient(160deg,#1B2D52 0%,#111E3A 65%,#0B1428 100%)", ink="#FFFFFF", sub="#B9C4D8", acc="#9FB7E3",
                     metal="linear-gradient(90deg,#B8862E,#F1D28A,#C7952F,#F6DE9C)", metal_solid="#E3BE6C", draw="#D9B061", logo_bg="#1F3561",
                     back="#F7F3EA", b_ink="#111E3A", b_sub="#5E6878", b_day="#A2741C", b_line="#E3DBCB", qr="#111E3A", mock="#CFC8BB"),
 "B-graphite-copper": dict(front="linear-gradient(160deg,#33373B 0%,#222527 65%,#17191B 100%)", ink="#FFFFFF", sub="#B7BCBF", acc="#E7C2A6",
                     metal="linear-gradient(90deg,#9C5B33,#E9B48C,#B06A3D,#F2C7A4)", metal_solid="#D99A6E", draw="#C98559", logo_bg="#3A3E42",
                     back="#F1EFEC", b_ink="#1E2123", b_sub="#6B6F72", b_day="#A35E34", b_line="#DDD8D2", qr="#222527", mock="#C9C4BE"),
 "C-oxblood-gold": dict(front="linear-gradient(160deg,#5E1F2A 0%,#46141D 65%,#330D14 100%)", ink="#FFFFFF", sub="#E0C2C6", acc="#F0D2B0",
                     metal="linear-gradient(90deg,#B8862E,#F1D28A,#C7952F,#F6DE9C)", metal_solid="#E6C273", draw="#D9B061", logo_bg="#6A2531",
                     back="#F8F3EC", b_ink="#3A1018", b_sub="#7A6266", b_day="#9C6B1C", b_line="#E8DCCF", qr="#46141D", mock="#D3C9BD"),
 "D-monochrome": dict(front="#FFFFFF", ink="#111111", sub="#6B6B6B", acc="#B4532F",
                     metal="linear-gradient(90deg,#B4532F,#B4532F)", metal_solid="#111111", draw="#B4532F", logo_bg="#111111",
                     back="#111111", b_ink="#FFFFFF", b_sub="#A6A6A6", b_day="#E08A62", b_line="rgba(255,255,255,.18)", qr="#111111", mock="#D6D3CE"),
}

def front(t):
    T = THEMES[t]; mono = t.startswith("D")
    name_style = (f"color:{T['ink']}" if mono else f"background:{T['metal']};-webkit-background-clip:text;background-clip:text;color:transparent")
    site_style = (f"color:{T['acc']}" if mono else name_style)
    return f"""<div class="card" style="background:{T['front']};color:{T['ink']}">
 <div style="position:absolute;right:.2in;top:.5in;width:.85in;height:1.15in">{gut_line(T['draw'], 1.4)}</div>
 <div class="in">
  <div style="position:absolute;right:0;top:0;width:.26in;height:.26in">{logo(T['logo_bg'])}</div>
  <div style="position:absolute;left:0;top:0">
   <div style="font-size:6.6pt;color:{T['sub']};letter-spacing:.06em">Dr.</div>
   <div class="serif" style="font-size:19pt;line-height:1.02;{name_style}">Kshitij Lochab</div>
   <div style="width:.5in;height:{1 if mono else 1.2}pt;background:{T['metal']};margin:.06in 0 .05in"></div>
   <div style="font-size:7pt;line-height:1.35;color:{T['ink'] if mono else '#F2F2F2'}">Consultant Gastroenterologist &amp; Therapeutic Endoscopist</div>
   <div style="font-size:7pt;line-height:1.35;color:{T['acc']};font-weight:600">Associate Consultant, Apollo Hospitals, Gurugram</div>
   <div style="margin-top:.07in;padding-left:.07in;border-left:1.2pt solid {T['draw']}">
    <div class="cap" style="font-size:6pt;letter-spacing:.2em;color:{T['metal_solid'] if not mono else T['ink']}">All-India Gold Medal</div>
    <div style="font-size:6pt;color:{T['sub']};margin-top:.015in">DrNB Gastroenterology · Medanta</div></div></div>
  <div style="position:absolute;left:0;bottom:0;display:flex;align-items:flex-end;gap:.12in">
   <div><div class="serif" style="font-size:10pt">{PHONE}</div><div style="font-size:6pt;color:{T['sub']};margin-top:.01in">Call or WhatsApp</div></div>
   <div style="width:.6pt;height:.28in;background:{T['draw']}"></div>
   <div><div class="serif" style="font-size:10pt;{site_style}">{SITE}</div><div style="font-size:6pt;color:{T['sub']};margin-top:.01in">Timings, directions, health guides</div></div></div>
 </div></div>"""

def back(t):
    T = THEMES[t]
    rows = "".join(f'<div style="display:grid;grid-template-columns:.8in 1fr auto;align-items:center;gap:.06in;padding:.04in 0;border-top:.5pt solid {T["b_line"]}">'
                   f'<span class="cap" style="font-size:5.6pt;color:{T["b_day"]};letter-spacing:.1em">{d}</span>'
                   f'<div style="line-height:1.15"><div class="serif" style="font-size:8.6pt">{p}</div><div style="font-size:6pt;color:{T["b_sub"]}">{a}, Gurugram</div></div>'
                   f'<span style="font-size:7.6pt;font-weight:600;white-space:nowrap">{tm}</span></div>' for d, p, a, tm in OPD)
    qr_bg = "#FFFFFF" if t.startswith("D") else "transparent"
    return f"""<div class="card" style="background:{T['back']};color:{T['b_ink']}">
 <div class="in"><div style="display:flex;gap:.14in;height:100%">
  <div style="flex:1;display:flex;flex-direction:column">
   <div style="display:flex;align-items:baseline;gap:.06in"><span class="cap" style="font-size:5.8pt;color:{T['b_day']}">Evening OPD</span><span class="serif" style="font-size:9pt">Monday to Saturday</span></div>
   <div style="margin-top:.04in">{rows}<div style="border-top:.5pt solid {T['b_line']}"></div></div>
   <div style="margin-top:auto;padding-left:.06in;border-left:1pt solid #C0392B;font-size:6pt"><b style="color:{'#E07A6A' if t.startswith('D') else '#B0362B'}">Urgent during the day?</b> Apollo Hospitals only. Call first.</div></div>
  <div style="width:.62in;display:flex;flex-direction:column;align-items:center;justify-content:space-between">
   <div style="text-align:center"><div style="width:.6in;height:.6in;background:{qr_bg};padding:{'.04in' if t.startswith('D') else '0'};border-radius:.04in">{qr_svg("https://drlochab.com", T['qr'])}</div>
    <div style="font-size:5.2pt;color:{T['b_sub']};margin-top:.03in">Scan: directions</div></div>
   <div style="font-size:5.2pt;line-height:1.4;color:{T['b_sub']};text-align:center">MBBS · MD · DrNB<br>HMC Reg.<br>HN-23524</div></div>
 </div></div></div>"""

if __name__ == "__main__":
    w, h = 3.5, 2.0; pw, ph = w + 2 * BLEED, h + 2 * BLEED
    with sync_playwright() as p:
        b = p.chromium.launch()
        for t in THEMES:
            fr, bk = (lambda t=t: front(t)), (lambda t=t: back(t))
            path = f"{OUT}/card.html"
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)}</style></head><body>{fr()}{bk()}</body></html>")
            pg = b.new_page(); pg.goto(f"file://{path}"); pg.wait_for_timeout(500)
            pg.pdf(path=f"{OUT}/card-{t}-print.pdf", width=f"{pw}in", height=f"{ph}in", print_background=True); pg.close()
            pv = b.new_page(viewport={"width": int(pw * 96) + 2, "height": int(ph * 96 * 2) + 2}, device_scale_factor=6)
            pv.goto(f"file://{path}"); pv.wait_for_timeout(500)
            for i, nm in enumerate(["front", "back"]):
                box = pv.locator(".card").nth(i).bounding_box()
                pv.screenshot(path=f"{OUT}/card-{t}-{nm}.png", clip={"x": box["x"] + BLEED * 96, "y": box["y"] + BLEED * 96, "width": w * 96, "height": h * 96})
            pv.close()
            open(path, "w").write(f"<!doctype html><html><head><meta charset=utf-8><style>{css(pw, ph)} .card{{page-break-after:auto}}</style></head><body style='margin:0'>{mockup(fr, bk, w, h, THEMES[t]['mock'])}</body></html>")
            pm = b.new_page(viewport={"width": 2400, "height": 1600}); pm.goto(f"file://{path}"); pm.wait_for_timeout(600)
            pm.screenshot(path=f"{OUT}/mockup-{t}.png"); pm.close(); os.remove(path)
        b.close()
    # comparison board: fronts on the left, backs on the right
    ims = [(Image.open(f"{OUT}/card-{t}-front.png").convert("RGB"), Image.open(f"{OUT}/card-{t}-back.png").convert("RGB")) for t in THEMES]
    cw, ch = ims[0][0].size; g = 60
    board = Image.new("RGB", (cw * 2 + g * 3, ch * len(ims) + g * (len(ims) + 1)), "#E9E5DE")
    for i, (f, k) in enumerate(ims):
        board.paste(f, (g, g + i * (ch + g))); board.paste(k, (cw + 2 * g, g + i * (ch + g)))
    board.resize((board.width // 3, board.height // 3), Image.LANCZOS).save(f"{OUT}/colour-options-board.png")
    print("done", sorted(os.listdir(OUT)))
