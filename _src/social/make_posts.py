"""Renders Instagram posts (1080x1350) for Dr. Kshitij Lochab from simple slide specs."""
import base64, os, shutil
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(ROOT)
FONTS = os.path.join(SRC, "fonts")
OUT = os.path.join(SRC, "out", "instagram")
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)

b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
LOGO = "data:image/png;base64," + b64(f"{SRC}/brand/logo-mark.png")
PHOTO = "data:image/jpeg;base64," + b64(f"{SRC}/dr-lochab.jpg")
ILLUS_JS = open(f"{SRC}/insta/illus.js").read()
ILLUS_CSS = open(f"{SRC}/insta/illus.css").read()

CSS = f"""
@font-face{{font-family:"YS";src:url("file://{FONTS}/YoungSerif.ttf")}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-400.ttf");font-weight:400}}
@font-face{{font-family:"FT";src:url("file://{FONTS}/Figtree-600.ttf");font-weight:600}}
:root{{--bg:#F3F7F6;--surface:#FFFFFF;--ink:#12302C;--muted:#4A615D;--line:#D3E0DC;--accent:#0D7466;--accent-ink:#FFFFFF;
--accent-soft:#DDEEEA;--warm:#C9851F;--warm-soft:#FAEED8;--urgent:#B0362B;--urgent-soft:#F8E4E1;--organ:#CADDD8;--organ-line:#97B6AF;--mark:#0B6A5E;--body:"FT"}}
*{{box-sizing:border-box;margin:0}}
html,body{{width:1080px;height:1350px}}
body{{font-family:"FT",sans-serif;color:var(--ink);background:var(--bg);overflow:hidden}}
.s{{width:1080px;height:1350px;padding:84px 88px 0;display:flex;flex-direction:column;position:relative}}
.top{{display:flex;justify-content:space-between;align-items:center;font-weight:600;font-size:26px;letter-spacing:.12em;text-transform:uppercase}}
.pill{{padding:12px 24px;border-radius:999px;background:var(--accent-soft);color:var(--accent)}}
.count{{color:var(--muted);letter-spacing:.06em}}
.main{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px}}
h1{{font-family:"YS",serif;font-weight:400;font-size:96px;line-height:1.08;letter-spacing:-.01em}}
h2{{font-family:"YS",serif;font-weight:400;font-size:70px;line-height:1.12}}
p{{font-size:42px;line-height:1.45;color:var(--muted);max-width:880px}}
ul{{list-style:none;padding:0;display:flex;flex-direction:column;gap:30px}}
li{{font-size:44px;line-height:1.3;display:flex;gap:28px;align-items:flex-start}}
li::before{{content:"";flex:none;width:22px;height:22px;border-radius:50%;background:var(--dot,var(--accent));margin-top:14px}}
.foot{{height:150px;border-top:2px solid var(--line);display:flex;align-items:center;gap:22px}}
.foot img{{width:72px;height:72px}}
.foot b{{font-family:"YS",serif;font-weight:400;font-size:32px;display:block}}
.foot span{{font-size:24px;color:var(--muted);letter-spacing:.04em}}
.swipe{{margin-left:auto;font-weight:600;font-size:26px;color:var(--accent)}}
/* cover */
.cover{{background:var(--mark);color:#fff}}
.cover .pill{{background:rgba(255,255,255,.14);color:#fff}}
.cover .count,.cover p,.cover .foot span{{color:#CFE5E0}}
.cover h1 em{{font-style:normal;color:#F1B84E}}
.cover .foot{{border-color:rgba(255,255,255,.2)}}
.cover .swipe{{color:#F1B84E}}
/* urgent */
.urgent .pill{{background:var(--urgent-soft);color:var(--urgent)}}
.urgent li{{--dot:var(--urgent)}}
.urgent h2 em{{font-style:normal;color:var(--urgent)}}
/* warm */
.warm{{background:var(--warm-soft)}}
.box{{background:var(--surface);border-radius:32px;padding:40px 44px;display:flex;flex-direction:column;gap:14px}}
.box small{{font-size:24px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}}
.box strong{{font-family:"YS",serif;font-weight:400;font-size:56px;font-variant-numeric:tabular-nums}}
.myth{{font-family:"YS",serif;font-size:66px;line-height:1.15;color:var(--muted);text-decoration:line-through;text-decoration-color:var(--urgent);text-decoration-thickness:5px}}
.lbl{{font-size:26px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}}
.fig{{background:var(--surface);border-radius:32px;height:470px;display:grid;place-items:center;overflow:hidden}}
.fig > svg{{width:100%;height:100%}}
{ILLUS_CSS}
.il-lbl{{font-size:9px}}
"""

def foot(swipe=False):
    return (f'<div class="foot"><img src="{LOGO}"><div><b>Dr. Kshitij Lochab</b>'
            f'<span>Gastroenterologist · drlochab.com</span></div>'
            + ('<span class="swipe">Swipe →</span>' if swipe else "") + "</div>")

def slide(cls, tag, count, inner, swipe=False):
    top = f'<div class="top"><span class="pill">{tag}</span><span class="count">{count}</span></div>'
    return f'<div class="s {cls}">{top}<div class="main">{inner}</div>{foot(swipe)}</div>'

def cta(tag, count):
    return slide("warm", tag, count, """
      <h2>Have questions about your gut or liver?</h2>
      <div class="box"><small>Consultations &amp; video consultations</small><strong>+91 96671 04882</strong>
      <span style="font-size:34px;color:var(--muted)">Call or WhatsApp</span></div>
      <p>Arcura Clinic, M2K Corporate Park, Sector 51, Gurugram<br>Daily tips at drlochab.com</p>
      <p style="font-weight:600;color:var(--accent)">Save this post and share it with your family.</p>""")

POSTS = {
 "01-meet-your-gastroenterologist": [f"""
  <div class="s" style="padding:0">
    <div style="height:760px;background:url('{PHOTO}') center 18%/cover"></div>
    <div style="flex:1;padding:56px 88px 0;display:flex;flex-direction:column;gap:22px">
      <span class="lbl" style="color:var(--accent)">Gastroenterologist · Gurugram</span>
      <h2 style="font-size:66px">Hello, Gurugram. I'm Dr.&nbsp;Kshitij&nbsp;Lochab.</h2>
      <ul style="gap:12px">
        <li style="font-size:32px">DrNB Gastroenterology, Medanta · All-India Gold Medal</li>
        <li style="font-size:32px">Advanced Fellowship in EUS &amp; ERCP</li>
        <li style="font-size:32px">Arcura Clinic, Sector 51 · Video consultations</li>
      </ul>
    </div>
    <div style="padding:0 88px">{foot()}</div>
  </div>"""],
 "02-acidity-warning-signs": [
  slide("cover","Acidity","1/5","<h1>Acidity: when is it <em>more than</em> just acidity?</h1><p>Know when home care is enough, and when to see a doctor.</p>",True),
  slide("","Acidity","2/5","<h2>Occasional heartburn is common</h2><p>Burning after a heavy or late meal, now and then, is usually reflux. Simple habits help most people:</p><ul><li>Finish dinner 3 hours before bed</li><li>Eat smaller meals</li><li>Raise the head end of your bed</li></ul>",True),
  slide("","Acidity","3/5","<h2>See a gastroenterologist if</h2><ul><li>It happens twice a week or more</li><li>It doesn't settle in 2 to 4 weeks</li><li>Food sticks when you swallow</li><li>You are losing weight without trying</li></ul>",True),
  slide("urgent","Warning signs","4/5","<h2>Go to hospital <em>today</em> if you</h2><ul><li>Vomit blood or coffee-ground material</li><li>Pass black, sticky, tar-like stools</li><li>Feel faint or dizzy with stomach pain</li></ul><p>In an emergency, call 112.</p>",True),
  cta("Acidity","5/5")],
 "03-fatty-liver": [
  slide("cover","Liver","1/5","<h1>Fatty liver: silent, common and <em>reversible</em></h1><p>What an ultrasound report saying \"fatty liver\" really means.</p>",True),
  slide("","Liver","2/5","<h2>Why it matters</h2><p>Fat builds up in the liver, usually without any symptoms. In some people it slowly causes scarring, which can lead to cirrhosis over years.</p>",True),
  slide("","Liver","3/5","<h2>Who should get checked</h2><ul><li>People who are overweight</li><li>Type 2 diabetes or high cholesterol</li><li>Regular alcohol use</li><li>Fatty liver seen on an ultrasound</li></ul>",True),
  slide("","Liver","4/5","<h2>What reverses it</h2><ul><li>Lose 7 to 10% of body weight, slowly</li><li>Walk briskly 150 minutes a week</li><li>Cut sugary drinks, sweets and maida</li><li>Avoid alcohol completely</li></ul>",True),
  cta("Liver","5/5")],
 "04-living-with-ibs": [
  slide("cover","IBS","1/5","<h1>IBS: real symptoms, <em>a healthy bowel</em></h1><p>Pain, bloating and bathroom trouble, explained simply.</p>",True),
  slide("","IBS","2/5","<h2>What IBS is</h2><p>The link between your gut and brain becomes over-sensitive, so normal gas and movement feel like pain or urgency. It does not damage the bowel or turn into cancer.</p>",True),
  slide("","IBS","3/5","<h2>What helps most people</h2><ul><li>Meals at the same times every day</li><li>Gentle fibre: oats and isabgol</li><li>Finding your triggers: onion, garlic, rajma, milk</li><li>Better sleep and less stress</li></ul>",True),
  slide("urgent","Get tested","4/5","<h2>It's <em>not</em> IBS if you have</h2><ul><li>Blood in the stool</li><li>Weight loss without trying</li><li>Symptoms that wake you at night</li><li>Fever or anaemia</li></ul><p>These need proper tests.</p>",True),
  cta("IBS","5/5")],
 "05-myth-spicy-food": [
  slide("","Myth or fact","", """<div class="lbl" style="color:var(--urgent)">Myth</div><div class="myth">Spicy food causes stomach ulcers.</div>
   <div class="lbl" style="color:var(--accent);margin-top:20px">Fact</div><h2>Most ulcers are caused by an infection called H.&nbsp;pylori, or by painkillers.</h2>
   <p>Spice can make existing gastritis burn more, but it doesn't create an ulcer. Recurring upper stomach pain? Ask about an H.&nbsp;pylori test.</p>""")],
 "06-endoscopy-what-to-expect": [
  slide("cover","Endoscopy","1/5","<h1>Nervous about an endoscopy? <em>Here's what happens.</em></h1><p>Step by step, from the night before to going home.</p>",True),
  slide("","Before","2/5","<h2>Before the test</h2><ul><li>Nothing to eat for 6 to 8 hours</li><li>Bring old reports and your medicine list</li><li>Tell us about blood thinners or diabetes medicines</li></ul>",True),
  slide("","During","3/5",'<div class="fig" id="fig"></div><h2>During: 10 to 15 minutes</h2><p>A thin, flexible camera goes through the mouth into the stomach. Throat spray or light sedation keeps you comfortable.</p>',True),
  slide("","After","4/5","<h2>After the test</h2><ul><li>Home the same day</li><li>If sedated, don't drive that day</li><li>Biopsy results in about a week</li></ul>",True),
  cta("Endoscopy","5/5")],
}

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for name, slides in POSTS.items():
        os.makedirs(f"{OUT}/{name}")
        for i, s in enumerate(slides, 1):
            html = f"<!doctype html><html><head><meta charset=utf-8><style>{CSS}</style></head><body>{s}<script>{ILLUS_JS};var f=document.getElementById('fig');if(f)f.innerHTML=IL.gastro;</script></body></html>"
            open(f"{OUT}/tmp.html", "w").write(html)
            pg.goto(f"file://{OUT}/tmp.html")
            pg.wait_for_timeout(250)
            pg.screenshot(path=f"{OUT}/{name}/slide-{i}.png")
    b.close()
print("done")
