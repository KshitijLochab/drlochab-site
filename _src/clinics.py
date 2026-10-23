"""Where and when Dr. Lochab consults: the ONE place to change clinic timings (23 Oct 2026).
Used by the home page (visit section, 'open now' line, booking chips), the 'Book a consultation' box on every page,
the Gurgaon and About pages, and structured data. Change hours here, run publish.sh, and the whole site follows.

APOLLO_CLINIC started 23 Oct 2026, Mon–Sat 4–6 pm; Dr. Lochab expects the timing to change in about 3 weeks.
Booking at Apollo Clinic: his WhatsApp/phone or directly at the clinic. Street address still to come from him
(only 'Sector 52, Gurugram' confirmed); the map link is the one he sent."""

# Sessions for the 'open now / next clinic' line. Day numbers: 0 = Sunday ... 6 = Saturday. Hours are 24h, IST.
SESSIONS = [
 ("arcura", [1, 2, 3, 4, 5], 18, 20),
 ("arcura", [0], 9, 13),
 ("apollo", [1, 2, 3, 4, 5, 6], 16, 18),
]

APOLLO_CLINIC = dict(
 map="https://maps.app.goo.gl/6K7YkaDWh5TRgQPh8",
 street="Sector 52",            # replace with the full street address once confirmed
 en=dict(name="Apollo Clinic, Sector 52", line="Apollo Clinic, Sector 52, Gurugram", place="Apollo Clinic, Sector 52",
         hours=[("Monday to Saturday", "4 pm to 6 pm")], short="Mon–Sat 4–6 pm",
         book="Book on WhatsApp or call, or directly at the clinic.", dir="Directions to Apollo Clinic", chip="Apollo Clinic, Sector 52 (4–6 pm)"),
 hi=dict(name="अपोलो क्लिनिक, सेक्टर 52", line="अपोलो क्लिनिक, सेक्टर 52, गुरुग्राम", place="अपोलो क्लिनिक, सेक्टर 52",
         hours=[("सोमवार से शनिवार", "शाम 4 से 6 बजे")], short="सोम–शनि शाम 4–6 बजे",
         book="WhatsApp या कॉल करके, या सीधे क्लिनिक पर अपॉइंटमेंट लें।", dir="अपोलो क्लिनिक का रास्ता", chip="अपोलो क्लिनिक, सेक्टर 52 (शाम 4–6)"),
)
ARCURA_PLACE = {"en": "Arcura, Sector 51", "hi": "आर्क्योरा, सेक्टर 51"}
HOUR_TXT = {"en": {9: "9 am", 13: "1 pm", 16: "4 pm", 18: "6 pm", 20: "8 pm"},
            "hi": {9: "सुबह 9 बजे", 13: "दोपहर 1 बजे", 16: "शाम 4 बजे", 18: "शाम 6 बजे", 20: "रात 8 बजे"}}

def open_js(lang):
    """OPENTXT + SESS for the home page 'open now' line, in the page language."""
    import json
    T = dict(en=dict(open="Open now · until ${t}", today="Opens today at ${t}", next="Next clinic: ${d}, ${t}", tom="tomorrow",
                     days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]),
             hi=dict(open="अभी खुला है · ${t} तक", today="आज ${t} से", next="अगला क्लिनिक: ${d}, ${t}", tom="कल",
                     days=["रविवार", "सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार"]))[lang]
    places = {"arcura": ARCURA_PLACE[lang], "apollo": APOLLO_CLINIC[lang]["place"]}
    sess = [dict(p=places[k], d=days, a=a, b=b) for k, days, a, b in SESSIONS]
    return ("const OPENTXT={open:t=>`" + T["open"] + "`,today:t=>`" + T["today"] + "`,next:(d,t)=>`" + T["next"] + "`,t:"
            + json.dumps({str(k): v for k, v in HOUR_TXT[lang].items()}, ensure_ascii=False) + ",days:" + json.dumps(T["days"], ensure_ascii=False)
            + ",tom:" + json.dumps(T["tom"], ensure_ascii=False) + "};\nconst SESS=" + json.dumps(sess, ensure_ascii=False) + ";")

def opening_spec():
    """schema.org openingHoursSpecification for Apollo Clinic."""
    names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    out = []
    for k, days, a, b in SESSIONS:
        if k == "apollo":
            out.append({"@type": "OpeningHoursSpecification", "dayOfWeek": [names[d] for d in days], "opens": f"{a:02d}:00", "closes": f"{b:02d}:00"})
    return out

def location_ld():
    """Second practice location for the Physician structured data."""
    return {"@type": "MedicalClinic", "name": "Apollo Clinic, Sector 52, Gurugram",
            "address": {"@type": "PostalAddress", "streetAddress": APOLLO_CLINIC["street"], "addressLocality": "Gurugram", "addressRegion": "Haryana", "addressCountry": "IN"},
            "hasMap": APOLLO_CLINIC["map"], "telephone": "+91-9667104882", "openingHoursSpecification": opening_spec()}

def home_block(lang):
    """Second clinic card in the home page visit section."""
    import html
    X = APOLLO_CLINIC[lang]; e = lambda s: html.escape(s, quote=True)
    hours = '<dl class="hours">' + "".join(f"<dt>{e(d)}</dt><dd>{e(h)}</dd>" for d, h in X["hours"]) + "</dl>"
    return (f'<div class="clinic2"><address><strong>{e(X["name"])}</strong><br>Gurugram, Haryana</address>{hours}<p>{e(X["book"])}</p>'
            f'<div class="hero-cta"><a class="btn btn-ghost" href="{APOLLO_CLINIC["map"]}" target="_blank" rel="noopener">{e(X["dir"])}</a></div></div>')
