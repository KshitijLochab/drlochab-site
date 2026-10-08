"""Fatty liver diet guide: a 1200x900 Google post image and a printable A4 handout (PDF + PNG)."""
import base64, os
from playwright.sync_api import sync_playwright

SRC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(SRC, "out", "handouts"); os.makedirs(D, exist_ok=True)
FONTS = os.path.join(SRC, "fonts")
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = "data:image/png;base64," + b64(f"{SRC}/brand/logo-mark.png")
QR = "data:image/png;base64," + b64(f"{SRC}/brand/qr-site.png")

BASE = f"""
@font-face{{font-family:"YS";src:url("file://{FONTS}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-600.ttf");font-weight:600}}
:root{{--bg:#F3F7F6;--ink:#12302C;--muted:#4A615D;--line:#D3E0DC;--teal:#0B6A5E;--soft:#DDEEEA;--warm:#C9851F;--warmsoft:#FAEED8;--red:#B0362B;--redsoft:#F8E4E1}}
*{{box-sizing:border-box;margin:0}}
body{{font-family:"FT",sans-serif;color:var(--ink);background:var(--bg)}}
h1,h2,h3{{font-family:"YS",serif;font-weight:400}}
.lbl{{font-weight:600;letter-spacing:.12em;text-transform:uppercase}}
ul{{padding-left:1.1em;display:flex;flex-direction:column}}
.col{{background:#fff;border-radius:22px}}
.col.more .lbl{{color:var(--teal)}} .col.less .lbl{{color:var(--red)}} .col.know .lbl{{color:var(--warm)}}
.col.more li::marker{{color:var(--teal)}} .col.less li::marker{{color:var(--red)}} .col.know li::marker{{color:var(--warm)}}
.brand{{display:flex;align-items:center;gap:16px}}
.brand b{{font-family:"YS",serif;font-weight:400;display:block}}
.brand span{{color:var(--muted)}}
"""

POST = f"""<!doctype html><html><head><meta charset=utf-8><style>{BASE}
html,body{{width:1200px;height:900px;overflow:hidden}}
.s{{padding:56px 64px 0;height:900px;display:flex;flex-direction:column;justify-content:space-between}}
.head{{display:flex;justify-content:space-between;align-items:flex-end;gap:30px}}
.head .lbl{{color:var(--teal);font-size:20px;margin-bottom:10px}}
h1{{font-size:64px;line-height:1.05}}
.goal{{background:var(--teal);color:#fff;border-radius:22px;padding:20px 26px;max-width:330px;flex:none}}
.goal strong{{font-family:"YS",serif;font-weight:400;font-size:44px;display:block;color:#F1B84E}}
.goal span{{font-size:20px;line-height:1.35;display:block;color:#DDEFEA}}
.cols{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.col{{padding:28px 28px 30px}}
.col .lbl{{font-size:18px;margin-bottom:12px;display:block}}
.col ul{{gap:14px;font-size:26px;line-height:1.3}}
.foot{{height:110px;border-top:2px solid var(--line);display:flex;align-items:center;justify-content:space-between}}
.brand img{{width:62px;height:62px}} .brand b{{font-size:28px}} .brand span{{font-size:19px}}
.site{{font-weight:600;font-size:24px;color:var(--teal)}}
</style></head><body><div class="s">
<div class="head"><div><div class="lbl">Diet guide</div><h1>Eating for a<br>healthier liver</h1></div>
<div class="goal"><strong>7 to 10%</strong><span>weight loss can reverse early fatty liver</span></div></div>
<div class="cols">
<div class="col more"><span class="lbl">Eat more</span><ul><li>Vegetables and salad at every meal</li><li>Whole grains, millets, oats</li><li>Dal, chana and sprouts</li><li>Whole fruit instead of juice</li></ul></div>
<div class="col less"><span class="lbl">Cut down</span><ul><li>Soft drinks, juices, sweets</li><li>Fried snacks and namkeen</li><li>Maida: white bread, biscuits</li><li>Alcohol, best avoided fully</li></ul></div>
<div class="col know"><span class="lbl">Good to know</span><ul><li>Brisk walking, 150 minutes a week</li><li>Lose weight slowly: half to one kilo a week</li><li>Fatty liver on an ultrasound? Get checked for scarring</li></ul></div>
</div>
<div class="foot"><div class="brand"><img src="{LOGO}"><div><b>Dr. Kshitij Lochab</b><span>Gastroenterologist · Sector 51, Gurugram</span></div></div><span class="site">drlochab.com</span></div>
</div></body></html>"""

A4 = f"""<!doctype html><html><head><meta charset=utf-8><style>{BASE}
@page{{size:A4;margin:0}}
html,body{{width:210mm;height:297mm;background:var(--bg)}}
.p{{width:210mm;height:297mm;padding:12mm 13mm 9mm;display:flex;flex-direction:column;gap:4mm}}
.top{{display:flex;justify-content:space-between;align-items:center}}
.brand img{{width:15mm;height:15mm}} .brand b{{font-size:16pt}} .brand span{{font-size:9pt;display:block}}
.reg{{text-align:right;font-size:8.5pt;color:var(--muted);line-height:1.5}}
.title .lbl{{color:var(--teal);font-size:9pt}}
h1{{font-size:24pt;line-height:1.1;margin-top:1mm}}
.intro{{font-size:10pt;line-height:1.45;color:var(--muted);max-width:165mm}}
.cols{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}}
.col{{padding:4mm 4.5mm}}
.col .lbl{{font-size:8.5pt;display:block;margin-bottom:2.5mm}}
.col ul{{gap:1.8mm;font-size:9.5pt;line-height:1.35}}
.day{{background:#fff;border-radius:22px;padding:5mm 6mm}}
.day h2{{font-size:14pt;margin-bottom:3mm}}
table{{width:100%;border-collapse:collapse;font-size:9.5pt;line-height:1.35}}
td{{padding:1.3mm 0;border-top:1px solid var(--line);vertical-align:top}}
td:first-child{{width:34mm;font-weight:600;color:var(--teal)}}
.row{{display:grid;grid-template-columns:1fr 1fr;gap:4mm}}
.box{{border-radius:22px;padding:5mm 6mm}}
.box h3{{font-size:12pt;margin-bottom:2mm}}
.goalbox{{background:var(--soft)}}
.fill{{font-size:10pt;line-height:1.9}}
.fill span{{display:inline-block;border-bottom:1.5px solid var(--ink);width:24mm}}
.warn{{background:var(--warmsoft)}}
.warn ul{{gap:1.2mm;font-size:9.5pt;line-height:1.35}}
.foot{{margin-top:auto;border-top:1.5px solid var(--line);padding-top:4mm;display:flex;justify-content:space-between;align-items:center;gap:6mm}}
.contact{{font-size:9pt;line-height:1.55;color:var(--muted)}}
.contact strong{{color:var(--ink);font-size:10.5pt}}
.qr{{display:flex;align-items:center;gap:3mm;font-size:8.5pt;color:var(--muted);text-align:right}}
.qr img{{width:20mm;height:20mm}}
.disc{{font-size:7.5pt;color:var(--muted)}}
</style></head><body><div class="p">
<div class="top"><div class="brand"><img src="{LOGO}"><div><b>Dr. Kshitij Lochab</b><span>Consultant Gastroenterologist &amp; Therapeutic Endoscopist</span></div></div>
<div class="reg">DrNB Gastroenterology (Medanta) · All-India Gold Medal<br>Haryana Medical Council Reg. No. HN-23524</div></div>
<div class="title"><div class="lbl">Patient diet guide</div><h1>Fatty liver: eating for a healthier liver</h1></div>
<p class="intro">Fatty liver means extra fat has built up in the liver. It usually causes no symptoms, but over years it can scar the liver. The good news: in its early stage it can be reversed. Steady weight loss, daily activity and the food changes below make the biggest difference.</p>
<div class="cols">
<div class="col more"><span class="lbl">Eat more</span><ul><li>Vegetables and salad at every meal</li><li>Whole grains: atta with chokar, bajra, ragi, oats, brown rice</li><li>Dal, chana, rajma and sprouts for protein</li><li>Whole fruit instead of juice</li><li>Plain tea or coffee with little or no sugar</li></ul></div>
<div class="col less"><span class="lbl">Cut down</span><ul><li>Soft drinks, packaged juices and sweets</li><li>Fried snacks, namkeen, bakery items</li><li>Maida: white bread, biscuits, noodles</li><li>Processed and red meat</li><li>Alcohol: best avoided completely</li></ul></div>
<div class="col know"><span class="lbl">Good to know</span><ul><li>Losing 7 to 10% of body weight can reverse early fatty liver</li><li>Aim for half to one kilo a week; crash diets are not needed</li><li>About 150 minutes of brisk walking a week helps even before weight falls</li><li>Control blood sugar and cholesterol if they are high</li></ul></div>
</div>
<div class="day"><h2>A sample day</h2><table>
<tr><td>Morning</td><td>Tea without sugar, with a few soaked almonds or walnuts</td></tr>
<tr><td>Breakfast</td><td>Vegetable poha, oats, or besan chilla with curd</td></tr>
<tr><td>Mid-morning</td><td>One whole fruit: guava, apple, orange or papaya</td></tr>
<tr><td>Lunch</td><td>2 multigrain rotis, dal, a vegetable sabzi, salad and curd</td></tr>
<tr><td>Evening</td><td>Roasted chana or sprouts chaat, plain tea or buttermilk</td></tr>
<tr><td>Dinner (by 8 pm)</td><td>1 to 2 rotis or a small bowl of rice, dal or paneer, chicken or fish, and vegetables</td></tr>
</table></div>
<div class="row">
<div class="box goalbox"><h3>My goals</h3><div class="fill">Weight today: <span></span> kg<br>Target (7 to 10% less): <span></span> kg<br>Walk every day: <span></span> minutes</div></div>
<div class="box warn"><h3>See your doctor soon if you notice</h3><ul><li>Yellow eyes or dark urine</li><li>Swelling of the belly or legs</li><li>Vomiting blood or black stools</li><li>Unusual confusion or sleepiness</li></ul></div>
</div>
<div class="foot"><div class="contact"><strong>Appointments and video consultations: +91 96671 04882</strong> (call or WhatsApp)<br>Arcura Clinic, M2K Corporate Park, 14, Mayfield Garden, Sector 51, Gurugram<br><span class="disc">General guidance only. Your diet may need changes based on your reports, other conditions and medicines.</span></div>
<div class="qr"><span>Daily diet tips<br>drlochab.com</span><img src="{QR}"></div></div>
</div></body></html>"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1200, "height": 900})
    open(f"{D}/post.html", "w").write(POST)
    pg.goto(f"file://{D}/post.html"); pg.wait_for_timeout(300)
    pg.screenshot(path=f"{D}/fatty-liver-google-post.png")
    pg2 = b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=2)
    open(f"{D}/a4.html", "w").write(A4)
    pg2.goto(f"file://{D}/a4.html"); pg2.wait_for_timeout(300)
    over = pg2.evaluate("document.querySelector('.p').scrollHeight - document.querySelector('.p').clientHeight")
    print("A4 overflow px:", over)
    pg2.screenshot(path=f"{D}/fatty-liver-diet-guide.png")
    pg2.pdf(path=f"{D}/fatty-liver-diet-guide.pdf", format="A4", print_background=True)
    b.close()
print("done")
