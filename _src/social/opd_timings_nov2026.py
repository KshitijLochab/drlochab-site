"""New OPD timings announcement (17 Nov 2026), drawn from clinics.py so the images always match the site.
Apollo Hospitals, Golf Course Road: Tue, Thu, Sat 4–6 pm (urgent daytime consultations here only).
Apollo Clinic, Sector 52: Mon, Wed, Fri 6–8 pm. Arcura Clinic, Sector 51: Tue, Thu, Sat 6:30–8 pm.
Instagram post EN + HI (1080x1350), Instagram story / WhatsApp Status EN + HI (1080x1920), Google Business image (1200x900),
captions, Google post text (no phone number) and WhatsApp messages.
Run from anywhere: python3 _src/social/opd_timings_nov2026.py  -> _src/out/opd-timings-nov-2026/"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.dirname(HERE))
from week_2026_10_12 import CSS, foot, SRC
import week_2026_11_09 as w9
from playwright.sync_api import sync_playwright

OUT = os.path.join(SRC, "out", "opd-timings-nov-2026"); os.makedirs(OUT, exist_ok=True)
w9.OUT = OUT

# Colours per place: Apollo Hospitals teal, Apollo Clinic saffron, Arcura deep green-gold
LOC = {
 "en": [("Apollo Hospitals", "Golf Course Road", "Tue · Thu · Sat", "4 – 6 pm", "#0D7466", [2, 4, 6], 16, 18),
        ("Apollo Clinic", "Sector 52", "Mon · Wed · Fri", "6 – 8 pm", "#E0913A", [1, 3, 5], 18, 20),
        ("Arcura Clinic", "Sector 51, Mayfield Garden", "Tue · Thu · Sat", "6:30 – 8 pm", "#7A4E9E", [2, 4, 6], 18.5, 20)],
 "hi": [("अपोलो हॉस्पिटल्स", "गोल्फ़ कोर्स रोड", "मंगल · गुरु · शनि", "शाम 4 – 6", "#0D7466", [2, 4, 6], 16, 18),
        ("अपोलो क्लिनिक", "सेक्टर 52", "सोम · बुध · शुक्र", "शाम 6 – 8", "#E0913A", [1, 3, 5], 18, 20),
        ("आर्क्योरा क्लिनिक", "सेक्टर 51, मेफ़ील्ड गार्डन", "मंगल · गुरु · शनि", "शाम 6:30 – 8", "#7A4E9E", [2, 4, 6], 18.5, 20)],
}
DAYS = {"en": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], "hi": ["सोम", "मंगल", "बुध", "गुरु", "शुक्र", "शनि", "रवि"]}
TXT = {
 "en": dict(kick="New OPD timings", h='Evening clinics, <em>Monday to Saturday</em>', urgent_h="Urgent during the day?",
            urgent="Daytime urgent consultations at Apollo Hospitals only. Call or WhatsApp first.", sun="Closed", book="Book: call or WhatsApp · drlochab.com"),
 "hi": dict(kick="ओपीडी का नया समय", h='शाम की ओपीडी, <em>सोमवार से शनिवार</em>', urgent_h="दिन में अर्जेंट?",
            urgent="दिन में अर्जेंट परामर्श सिर्फ़ अपोलो हॉस्पिटल्स में। पहले कॉल या WhatsApp करें।", sun="बंद", book="अपॉइंटमेंट: कॉल या WhatsApp · drlochab.com/hi"),
}

def week_chart(lang, w=912, h=520, dark=False):
    """A week timetable: 7 day columns, a 4 pm to 8 pm band, coloured blocks per place (viewBox scaled to w x h)."""
    left, top, right, bot = 92, 56, w - 12, h - 16
    colw = (right - left) / 7
    y = lambda t: top + (t - 16) / 4 * (bot - top)
    ink = "#FFFFFF" if dark else "#12302C"; mut = "#CFE5E0" if dark else "#4A615D"; grid = "rgba(255,255,255,.18)" if dark else "#D3E0DC"
    hours = {"en": {16: "4 pm", 18: "6 pm", 20: "8 pm"}, "hi": {16: "4", 18: "6", 20: "8"}}[lang]
    font = "MK" if lang == "hi" else "FT"
    g = ""
    for t, lbl in hours.items():
        g += f'<line x1="{left}" x2="{right}" y1="{y(t):.0f}" y2="{y(t):.0f}" stroke="{grid}" stroke-width="2" stroke-dasharray="6 8"/>'
        g += f'<text x="{left-14}" y="{y(t)+9:.0f}" text-anchor="end" font-family="{font}" font-size="26" fill="{mut}">{lbl}</text>'
    for i, d in enumerate(DAYS[lang]):
        cx = left + colw * (i + 0.5)
        g += f'<text x="{cx:.0f}" y="36" text-anchor="middle" font-family="{font}" font-weight="600" font-size="28" fill="{ink if i < 6 else mut}">{d}</text>'
        if i == 6:
            g += (f'<rect x="{left+colw*i+8:.0f}" y="{top}" width="{colw-16:.0f}" height="{bot-top}" rx="16" fill="none" stroke="{grid}" stroke-width="3" stroke-dasharray="8 8"/>'
                  f'<text x="{cx:.0f}" y="{(top+bot)/2+10:.0f}" text-anchor="middle" font-family="{font}" font-size="{min(26, int(colw * .3))}" fill="{mut}">{TXT[lang]["sun"]}</text>')
    for name, area, days, time, col, dnums, a, b in LOC[lang]:
        for dn in dnums:
            i = dn - 1
            c = "#8FE3D2" if dark and col == "#0D7466" else col
            g += f'<rect x="{left+colw*i+8:.0f}" y="{y(a)+3:.0f}" width="{colw-16:.0f}" height="{y(b)-y(a)-6:.0f}" rx="16" fill="{c}"/>'
    return f'<svg viewBox="0 0 {w} {h}" style="width:{w}px" xmlns="http://www.w3.org/2000/svg">{g}</svg>'

def cards(lang, size=1.0, dark=False):
    fg = "#FFFFFF" if dark else "#12302C"; bg = "rgba(255,255,255,.08)" if dark else "#FFFFFF"; sub = "#CFE5E0" if dark else "#4A615D"
    hf = "TD" if lang == "hi" else "YS"
    out = ""
    for name, area, days, time, col, *_ in LOC[lang]:
        out += (f'<div style="display:flex;align-items:center;gap:{int(24*size)}px;background:{bg};border-radius:{int(26*size)}px;padding:{int(18*size)}px {int(26*size)}px">'
                f'<span style="flex:none;width:{int(26*size)}px;height:{int(64*size)}px;border-radius:{int(10*size)}px;background:{"#8FE3D2" if dark and col == "#0D7466" else col}"></span>'
                f'<div style="flex:1;min-width:0"><div style="font-family:{hf};font-size:{int(40*size)}px;line-height:1.15;color:{fg}">{name}</div>'
                f'<div style="font-size:{int(26*size)}px;color:{sub}">{area}</div></div>'
                f'<div style="text-align:right;flex:none"><div style="font-weight:600;font-size:{int(30*size)}px;color:{fg}">{days}</div>'
                f'<div style="font-family:{hf};font-size:{int(38*size)}px;color:{col if not dark else "#F3B84A"}">{time}</div></div></div>')
    return out

def urgent_box(lang, size=1.0):
    return (f'<div style="display:flex;gap:{int(22*size)}px;align-items:center;background:#F8E4E1;border-radius:{int(26*size)}px;padding:{int(20*size)}px {int(26*size)}px;color:#12302C">'
            f'<svg viewBox="0 0 48 48" style="width:{int(64*size)}px;height:{int(64*size)}px;flex:none"><circle cx="24" cy="24" r="22" fill="#B0362B"/><path d="M24 12v16" stroke="#fff" stroke-width="5" stroke-linecap="round"/><circle cx="24" cy="35" r="3" fill="#fff"/></svg>'
            f'<div><div style="font-weight:600;font-size:{int(32*size)}px;color:#B0362B">{TXT[lang]["urgent_h"]}</div><div style="font-size:{int(28*size)}px;line-height:1.3">{TXT[lang]["urgent"]}</div></div></div>')

def post(lang):
    hi = " hi" if lang == "hi" else ""
    return f"""<div class="s mint{hi}" style="width:1080px;height:1350px;padding:70px 84px">
 <div class="kick" style="font-size:28px;color:#0D7466">{TXT[lang]["kick"]}</div>
 <h1 style="font-size:{58 if lang == "hi" else 66}px;margin-top:8px">{TXT[lang]["h"]}</h1>
 <div style="margin-top:20px;background:#fff;border-radius:32px;padding:16px 0 2px">{week_chart(lang, h=380)}</div>
 <div style="display:grid;gap:12px;margin-top:18px">{cards(lang, .82)}</div>
 <div style="margin-top:14px">{urgent_box(lang, .8)}</div>
 {foot(hi=lang == "hi")}</div>"""

def story(lang):
    hi = " hi" if lang == "hi" else ""
    return f"""<div class="s teal{hi}" style="width:1080px;height:1920px;padding:150px 84px">
 <div class="kick" style="font-size:32px;color:#F3B84A">{TXT[lang]["kick"]}</div>
 <h1 style="font-size:{72 if lang == "hi" else 84}px;margin-top:12px">{TXT[lang]["h"]}</h1>
 <div style="margin-top:36px;background:rgba(255,255,255,.06);border-radius:36px;padding:22px 0 6px">{week_chart(lang, h=440, dark=True)}</div>
 <div style="display:grid;gap:16px;margin-top:30px">{cards(lang, 1.0, dark=True)}</div>
 <div style="margin-top:24px">{urgent_box(lang, 1.0)}</div>
 <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center"><span style="background:#F3B84A;color:#12302C;font-family:{"TD" if lang == "hi" else "YS"};font-size:44px;padding:14px 40px;border-radius:999px">{TXT[lang]["book"]}</span></div>
 {foot(light=True, pad=84, hi=lang == "hi")}</div>"""

def gbp():
    return f"""<div class="s mint" style="width:1200px;height:900px;padding:60px 70px">
 <div class="kick" style="font-size:24px;color:#0D7466">{TXT["en"]["kick"]}</div>
 <h1 style="font-size:58px;margin-top:8px">{TXT["en"]["h"]}</h1>
 <div style="display:grid;grid-template-columns:560px 1fr;gap:30px;margin-top:26px;align-items:start">
  <div style="background:#fff;border-radius:28px;padding:14px 0 2px">{week_chart("en", w=560, h=400)}</div>
  <div style="display:grid;gap:12px">{cards("en", .7)}</div></div>
 <div style="margin-top:16px;width:1060px">{urgent_box("en", .75)}</div>
 {foot(pad=70)}</div>"""

SIGN = ("Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Fellowship in EUS and ERCP), Gurugram. "
        "HMC Reg. No. HN-23524.")
SIGN_HI = ("डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP फ़ेलोशिप), गुरुग्राम। "
           "HMC रजि. नं. HN-23524।")

CAP_EN = f"""🗓️ New OPD timings

I now see patients every evening from Monday to Saturday, at three places in Gurugram:

🏥 Apollo Hospitals, Golf Course Road: Tue, Thu, Sat · 4 to 6 pm
🩺 Apollo Clinic, Sector 52: Mon, Wed, Fri · 6 to 8 pm
🩺 Arcura Clinic, Sector 51 (Mayfield Garden): Tue, Thu, Sat · 6:30 to 8 pm

⚠️ Need to be seen urgently during the day? Urgent daytime consultations are at Apollo Hospitals only. Please call or WhatsApp first.
🚨 In an emergency, call 112 or go to the nearest emergency department.

📞 Appointments: call or WhatsApp +91 96671 04882
📍 Timings, addresses and directions: drlochab.com (link in bio)

{SIGN}

#Gastroenterologist #Gurugram #Gurgaon #ApolloHospitals #Sector51 #Sector52 #DrLochab"""

CAP_HI = f"""🗓️ ओपीडी का नया समय

अब मैं गुरुग्राम में सोमवार से शनिवार हर शाम, तीन जगह मरीज़ों को देखता हूँ:

🏥 अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड: मंगल, गुरु, शनि · शाम 4 से 6 बजे
🩺 अपोलो क्लिनिक, सेक्टर 52: सोम, बुध, शुक्र · शाम 6 से रात 8 बजे
🩺 आर्क्योरा क्लिनिक, सेक्टर 51 (मेफ़ील्ड गार्डन): मंगल, गुरु, शनि · शाम 6:30 से रात 8 बजे

⚠️ दिन में अर्जेंट दिखाना हो? दिन में अर्जेंट परामर्श सिर्फ़ अपोलो हॉस्पिटल्स में होता है। पहले कॉल या WhatsApp करें।
🚨 इमरजेंसी में 112 पर कॉल करें या नज़दीकी इमरजेंसी विभाग जाएँ।

📞 अपॉइंटमेंट: +91 96671 04882 पर कॉल या WhatsApp
📍 समय, पता और रास्ता: drlochab.com/hi (लिंक बायो में)

{SIGN_HI}

#गैस्ट्रोएंटेरोलॉजिस्ट #गुरुग्राम #Gurgaon #ApolloHospitals #Sector51 #Sector52 #DrLochab"""

GBP_TEXT = """New OPD timings. Dr. Kshitij Lochab now sees patients every evening from Monday to Saturday in Gurugram:

Apollo Hospitals, Golf Course Road: Tuesday, Thursday and Saturday, 4 pm to 6 pm.
Apollo Clinic, Sector 52: Monday, Wednesday and Friday, 6 pm to 8 pm.
Arcura Clinic, Sector 51 (Mayfield Garden): Tuesday, Thursday and Saturday, 6:30 pm to 8 pm.

Urgent daytime consultations are at Apollo Hospitals only; please get in touch before coming. In an emergency, call 112 or go to the nearest emergency department.

Use the Call button to book, or see timings, addresses and directions on the website.

Button: Learn more → https://drlochab.com/#visit"""

WA_EN = """🗓️ *New OPD timings: Dr. Kshitij Lochab*

I now see patients every evening, Monday to Saturday:
• *Apollo Hospitals, Golf Course Road*: Tue, Thu, Sat, 4–6 pm
• *Apollo Clinic, Sector 52*: Mon, Wed, Fri, 6–8 pm
• *Arcura Clinic, Sector 51*: Tue, Thu, Sat, 6:30–8 pm

Urgent daytime consultations: Apollo Hospitals only, please call or WhatsApp first.
Appointments: call or WhatsApp this number.
Addresses and directions: https://drlochab.com/#visit"""

WA_HI = """🗓️ *ओपीडी का नया समय: डॉ. क्षितिज लोचब*

अब मैं सोमवार से शनिवार हर शाम मरीज़ों को देखता हूँ:
• *अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड*: मंगल, गुरु, शनि, शाम 4–6
• *अपोलो क्लिनिक, सेक्टर 52*: सोम, बुध, शुक्र, शाम 6–8
• *आर्क्योरा क्लिनिक, सेक्टर 51*: मंगल, गुरु, शनि, शाम 6:30–8

दिन में अर्जेंट परामर्श: सिर्फ़ अपोलो हॉस्पिटल्स में, पहले कॉल या WhatsApp करें।
अपॉइंटमेंट: इसी नंबर पर कॉल या WhatsApp करें।
पता और रास्ता: https://drlochab.com/hi/#visit"""

if __name__ == "__main__":
    from PIL import Image
    with sync_playwright() as p:
        b = p.chromium.launch()
        w9.render(lambda: post("en"), 1080, 1350, f"{OUT}/ig-opd-timings-en.png", b)
        w9.render(lambda: post("hi"), 1080, 1350, f"{OUT}/ig-opd-timings-hi.png", b)
        w9.render(lambda: story("en"), 1080, 1920, f"{OUT}/story-status-opd-timings-en.png", b)
        w9.render(lambda: story("hi"), 1080, 1920, f"{OUT}/story-status-opd-timings-hi.png", b)
        w9.render(gbp, 1200, 900, f"{OUT}/google-business-opd-timings.png", b)
        b.close()
    if os.path.exists(f"{OUT}/tmp.html"): os.remove(f"{OUT}/tmp.html")
    for f in os.listdir(OUT):
        if f.endswith(".png"):
            Image.open(f"{OUT}/{f}").convert("RGB").save(f"{OUT}/{f[:-4]}.jpg", quality=92); os.remove(f"{OUT}/{f}")
    for name, txt in [("instagram-caption-en.txt", CAP_EN), ("instagram-caption-hi.txt", CAP_HI), ("google-business-post.txt", GBP_TEXT),
                      ("whatsapp-message-en.txt", WA_EN), ("whatsapp-message-hi.txt", WA_HI)]:
        open(f"{OUT}/{name}", "w").write(txt)
    print("done", sorted(os.listdir(OUT)))
