"""Where and when Dr. Lochab consults: the ONE place to change clinic timings (23 Oct 2026).
Used by the home page (visit section, 'open now' line, booking chips), the 'Book a consultation' box on every page,
the Gurgaon and About pages, and structured data. Change hours here, run publish.sh, and the whole site follows.

APOLLO_CLINIC started 23 Oct 2026, Mon–Sat 4–6 pm. On 30 Oct 2026 Dr. Lochab gave new timings (used on the visiting card):
Arcura Mon–Sat 10 am–5 pm and Sun 9 am–1 pm; Apollo Clinic, Sector 52 and Apollo Hospitals OPD from 6 November; on 5 Nov 2026 he moved the start to 11 November, timings still to be decided (so
so the site says 'call or WhatsApp for timings' and Apollo is left out of the 'open now' line until they are added to SESSIONS).
On 12 Nov 2026 (the start date had passed, timings still not fixed) he chose 'By appointment: call or WhatsApp for timings', with no date.
ARCURA below holds the Arcura hours text used everywhere on the site.
Booking at Apollo Clinic: his WhatsApp/phone or directly at the clinic. Address confirmed by him on 23 Oct 2026; the map link is the one he sent."""

# 17 Nov 2026: Dr. Lochab's new OPD timings (all evenings, no Sunday):
#   Apollo Hospitals, Golf Course Road: Tue, Thu, Sat 4–6 pm. Urgent daytime consultations at Apollo Hospitals only.
#   Apollo Clinic, Sector 52:           Mon, Wed, Fri 6–8 pm.
#   Arcura Clinic, Sector 51:           Tue, Thu, Sat 6:30–8 pm.
# Sessions for the 'open now / next clinic' line. Day numbers: 0 = Sunday ... 6 = Saturday. Hours are 24h, IST (18.5 = 6:30 pm).
SESSIONS = [
 ("apollo_hosp", [2, 4, 6], 16, 18),
 ("arcura", [2, 4, 6], 18.5, 20),
 ("apollo_clinic", [1, 3, 5], 18, 20),
]

# Arcura Clinic hours as shown on the site (keep in step with the arcura SESSIONS above).
ARCURA = dict(
 en=dict(hours=[("Tuesday, Thursday and Saturday", "6:30 pm to 8 pm")], short="Tue, Thu, Sat 6:30–8 pm",
         dl=[("Tue, Thu, Sat", "6:30 – 8 pm")], sentence="Tuesday, Thursday and Saturday, 6:30 pm to 8 pm",
         chips=["Arcura, Tue/Thu/Sat evening"]),
 hi=dict(hours=[("मंगलवार, गुरुवार और शनिवार", "शाम 6:30 से रात 8 बजे")], short="मंगल, गुरु, शनि शाम 6:30–8",
         dl=[("मंगल, गुरु, शनि", "शाम 6:30 – रात 8 बजे")], sentence="मंगलवार, गुरुवार और शनिवार, शाम 6:30 से रात 8 बजे",
         chips=["आर्क्योरा, मंगल/गुरु/शनि शाम"]),
)

APOLLO_CLINIC = dict(
 map="https://maps.app.goo.gl/6K7YkaDWh5TRgQPh8",
 street="Netaji Subhash Marg, Indira Colony 1, Sector 52", postal="122003",
 addr={"en": "Netaji Subhash Marg, Indira Colony 1, Sector 52, Gurugram, Haryana 122003",
       "hi": "नेताजी सुभाष मार्ग, इंदिरा कॉलोनी 1, सेक्टर 52, गुरुग्राम, हरियाणा 122003"},
 en=dict(name="Apollo Clinic, Sector 52", line="Apollo Clinic, Sector 52, Gurugram", place="Apollo Clinic, Sector 52",
         hours=[("Monday, Wednesday and Friday", "6 pm to 8 pm")], short="Mon, Wed, Fri 6–8 pm", dl=[("Mon, Wed, Fri", "6 – 8 pm")],
         book="Book on WhatsApp or call, or directly at the clinic.", dir="Directions to Apollo Clinic", chip="Apollo Clinic, Mon/Wed/Fri evening"),
 hi=dict(name="अपोलो क्लिनिक, सेक्टर 52", line="अपोलो क्लिनिक, सेक्टर 52, गुरुग्राम", place="अपोलो क्लिनिक, सेक्टर 52",
         hours=[("सोमवार, बुधवार और शुक्रवार", "शाम 6 से रात 8 बजे")], short="सोम, बुध, शुक्र शाम 6–8", dl=[("सोम, बुध, शुक्र", "शाम 6 – रात 8 बजे")],
         book="WhatsApp या कॉल करके, या सीधे क्लिनिक पर अपॉइंटमेंट लें।", dir="अपोलो क्लिनिक का रास्ता", chip="अपोलो क्लिनिक, सोम/बुध/शुक्र शाम"),
)

# Apollo Hospitals, Golf Course Road: OPD, and the only place for urgent daytime consultations.
APOLLO_HOSP = dict(
 en=dict(name="Apollo Hospitals, Golf Course Road", line="Apollo Hospitals, Golf Course Road, Gurugram", place="Apollo Hospitals, Golf Course Road",
         hours=[("Tuesday, Thursday and Saturday", "4 pm to 6 pm")], short="Tue, Thu, Sat 4–6 pm", dl=[("Tue, Thu, Sat", "4 – 6 pm")],
         urgent="Urgent daytime consultations: at Apollo Hospitals only. Call or WhatsApp first.", chip="Apollo Hospitals, Tue/Thu/Sat 4–6 pm"),
 hi=dict(name="अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड", line="अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम", place="अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड",
         hours=[("मंगलवार, गुरुवार और शनिवार", "शाम 4 से 6 बजे")], short="मंगल, गुरु, शनि शाम 4–6", dl=[("मंगल, गुरु, शनि", "शाम 4 – 6 बजे")],
         urgent="दिन में अर्जेंट परामर्श: सिर्फ़ अपोलो हॉस्पिटल्स में। पहले कॉल या WhatsApp करें।", chip="अपोलो हॉस्पिटल्स, मंगल/गुरु/शनि शाम 4–6"),
)

def schedule(lang):
    """All three OPDs as (place line, days and hours) in the page language, in weekly order of first session."""
    return [(APOLLO_HOSP[lang]["line"], APOLLO_HOSP[lang]["short"]),
            (APOLLO_CLINIC[lang]["line"], APOLLO_CLINIC[lang]["short"]),
            ("Arcura Clinic, Sector 51, Gurugram" if lang == "en" else "आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम", ARCURA[lang]["short"])]

def schedule_sentence(lang):
    """One sentence with every OPD, for FAQs and llms.txt."""
    if lang == "en":
        return ("Arcura Clinic, Sector 51: Tuesday, Thursday and Saturday, 6:30 pm to 8 pm. Apollo Clinic, Sector 52: Monday, Wednesday and Friday, 6 pm to 8 pm. "
                "Apollo Hospitals, Golf Course Road: Tuesday, Thursday and Saturday, 4 pm to 6 pm. Urgent daytime consultations are at Apollo Hospitals only.")
    return ("आर्क्योरा क्लिनिक, सेक्टर 51: मंगलवार, गुरुवार और शनिवार, शाम 6:30 से रात 8 बजे। अपोलो क्लिनिक, सेक्टर 52: सोमवार, बुधवार और शुक्रवार, शाम 6 से रात 8 बजे। "
            "अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड: मंगलवार, गुरुवार और शनिवार, शाम 4 से 6 बजे। दिन में अर्जेंट परामर्श सिर्फ़ अपोलो हॉस्पिटल्स में।")

ARCURA_PLACE = {"en": "Arcura, Sector 51", "hi": "आर्क्योरा, सेक्टर 51"}
HOUR_TXT = {"en": {16: "4 pm", 18: "6 pm", 18.5: "6:30 pm", 20: "8 pm"},
            "hi": {16: "शाम 4 बजे", 18: "शाम 6 बजे", 18.5: "शाम 6:30 बजे", 20: "रात 8 बजे"}}

def open_js(lang):
    """OPENTXT + SESS for the home page 'open now' line, in the page language."""
    import json
    T = dict(en=dict(open="Open now · until ${t}", today="Opens today at ${t}", next="Next clinic: ${d}, ${t}", tom="tomorrow",
                     days=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]),
             hi=dict(open="अभी खुला है · ${t} तक", today="आज ${t} से", next="अगला क्लिनिक: ${d}, ${t}", tom="कल",
                     days=["रविवार", "सोमवार", "मंगलवार", "बुधवार", "गुरुवार", "शुक्रवार", "शनिवार"]))[lang]
    places = {"arcura": ARCURA_PLACE[lang], "apollo_clinic": APOLLO_CLINIC[lang]["place"], "apollo_hosp": APOLLO_HOSP[lang]["place"]}
    sess = [dict(p=places[k], d=days, a=a, b=b) for k, days, a, b in SESSIONS]
    return ("const OPENTXT={open:t=>`" + T["open"] + "`,today:t=>`" + T["today"] + "`,next:(d,t)=>`" + T["next"] + "`,t:"
            + json.dumps({str(k): v for k, v in HOUR_TXT[lang].items()}, ensure_ascii=False) + ",days:" + json.dumps(T["days"], ensure_ascii=False)
            + ",tom:" + json.dumps(T["tom"], ensure_ascii=False) + "};\nconst SESS=" + json.dumps(sess, ensure_ascii=False) + ";")

def opening_spec(key="apollo_clinic"):
    """schema.org openingHoursSpecification for one location (arcura, apollo_clinic or apollo_hosp)."""
    names = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    hm = lambda x: f"{int(x):02d}:{int(round((x % 1) * 60)):02d}"
    return [{"@type": "OpeningHoursSpecification", "dayOfWeek": [names[d] for d in days], "opens": hm(a), "closes": hm(b)}
            for k, days, a, b in SESSIONS if k == key]

def location_ld():
    """Other practice locations (Apollo Clinic, Apollo Hospitals) for the Physician structured data."""
    return [_apollo_clinic_ld(), {"@type": "Hospital", "name": "Apollo Hospitals, Golf Course Road, Gurugram",
            "address": {"@type": "PostalAddress", "streetAddress": "Golf Course Road", "addressLocality": "Gurugram", "addressRegion": "Haryana", "addressCountry": "IN"},
            "telephone": "+91-9667104882", "openingHoursSpecification": opening_spec("apollo_hosp")}]

def _apollo_clinic_ld():
    d = {"@type": "MedicalClinic", "name": "Apollo Clinic, Sector 52, Gurugram",
            "address": {"@type": "PostalAddress", "streetAddress": APOLLO_CLINIC["street"], "addressLocality": "Gurugram", "addressRegion": "Haryana", "postalCode": APOLLO_CLINIC["postal"], "addressCountry": "IN"},
            "hasMap": APOLLO_CLINIC["map"], "telephone": "+91-9667104882"}
    d["openingHoursSpecification"] = opening_spec("apollo_clinic")
    return d

def home_block(lang):
    """Second clinic card in the home page visit section."""
    import html
    X = APOLLO_CLINIC[lang]; e = lambda s: html.escape(s, quote=True)
    hours = '<dl class="hours">' + "".join(f"<dt>{e(d)}</dt><dd>{e(h)}</dd>" for d, h in X["dl"]) + "</dl>"
    return (f'<div class="clinic2"><address><strong>{e(X["name"])}</strong><br>{e(APOLLO_CLINIC["addr"][lang])}</address>{hours}<p>{e(X["book"])}</p>'
            f'<div class="hero-cta"><a class="btn btn-ghost" href="{APOLLO_CLINIC["map"]}" target="_blank" rel="noopener">{e(X["dir"])}</a></div></div>')

def home_block3(lang):
    """Third card in the home page visit section: Apollo Hospitals OPD and the urgent daytime note."""
    import html
    X = APOLLO_HOSP[lang]; e = lambda s: html.escape(s, quote=True)
    hours = '<dl class="hours">' + "".join(f"<dt>{e(d)}</dt><dd>{e(h)}</dd>" for d, h in X["dl"]) + "</dl>"
    return f'<div class="clinic2"><address><strong>{e(X["line"])}</strong></address>{hours}<p><b>{e(X["urgent"])}</b></p></div>'

def aside_html(lang, e):
    """Every OPD for the 'Book a consultation' box on inner pages."""
    rows = "".join(f'<p class="small">{e(p)} · <b>{e(h)}</b></p>' for p, h in schedule(lang))
    return rows + f'<p class="small">{e(APOLLO_HOSP[lang]["urgent"])}</p>'
