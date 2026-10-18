"""Generates condition, procedure and answer pages (English and Hindi) into site/.
Run after build_site.py has written site/index.html and site/hi/index.html."""
import json, os, html, subprocess
from urllib.parse import quote
import seo_en, seo_hi, guide_art, seo_proc_en, seo_proc_hi, answers_extra_en, answers_extra_hi, cond_diet_en, cond_diet_hi

# diet box + FAQs for answer pages: same slugs and item counts in both languages
for _k, _v in answers_extra_en.EXTRA.items():
    _h = answers_extra_hi.EXTRA[_k]
    assert len(_v["faqs"]) == len(_h["faqs"]) and all(len(_v["diet"][c]) == len(_h["diet"][c]) for c in ("more", "less", "know")), _k
    assert ("labels" in _v["diet"]) == ("labels" in _h["diet"]), _k
for _k, _v in cond_diet_en.DIET.items():
    assert all(len(_v[c]) == len(cond_diet_hi.DIET[_k][c]) for c in ("more", "less", "know")), _k
assert set(cond_diet_en.DIET) == set(cond_diet_hi.DIET) <= {c["slug"] for c in seo_en.CONDS}
assert set(answers_extra_en.EXTRA) == set(answers_extra_hi.EXTRA) <= {a["slug"] for a in seo_en.ANSWERS}

SITE = "https://drlochab.com"
UPDATED = ("2026-10-10", "10 October 2026", "10 अक्टूबर 2026")
PROC_UPDATED = ("2026-10-17", "17 October 2026", "17 अक्टूबर 2026")
PHONE, WA = "+91 96671 04882", "https://wa.me/919667104882"
# WhatsApp Channel for the daily tip. Paste the channel's invite link here (https://whatsapp.com/channel/...); left empty, every channel link stays hidden.
ANSWER_IL = {"capsule-endoscopy": "capsule"}  # answer pages that show a home-page procedure drawing
WA_CHANNEL = ""
FOOT_LINKS = {"en": ("About Dr. Lochab", "Gastroenterologist in Gurgaon", "Gut health tracker"), "hi": ("डॉ. लोचब के बारे में", "गुड़गाँव में गैस्ट्रोएंटेरोलॉजिस्ट", "पेट की सेहत का ट्रैकर")}
CHANNEL_TXT = {"en": ("Get a daily gut-health tip on WhatsApp", "Join the channel"), "hi": ("पेट की सेहत की रोज़ की सलाह WhatsApp पर पाएँ", "चैनल से जुड़ें")}

TRACK_CONDS = {"ibs-irritable-bowel-syndrome", "constipation", "acidity-reflux-gerd", "ulcerative-colitis-crohns-disease", "h-pylori-gastritis-ulcer"}
TRACK_TXT = {"en": ("Keep a symptom diary", "Log your bowel habits, symptoms and possible food triggers for 2 to 4 weeks, privately on your phone, and bring the summary to your visit.", "Open the gut health tracker"),
             "hi": ("लक्षणों की डायरी रखें", "2 से 4 हफ़्ते तक अपनी मल की आदत, लक्षण और संभावित खाने के ट्रिगर अपने फ़ोन पर निजी रूप से लिखें, और सारांश डॉक्टर के पास लाएँ।", "पेट की सेहत का ट्रैकर खोलें")}

def tracker_note(lang):
    h, p_, b = TRACK_TXT[lang]
    return f'<section class="note"><p><b>{h}.</b> {p_}</p><p><a class="btn btn-ghost btn-sm" href="{url(lang, "tools", "gut-tracker")}">{b} →</a></p></section>'

def aka(lang, slug):
    """'Also searched as' Hinglish line on Hindi pages (hinglish.py)."""
    import hinglish
    if lang != "hi" or slug not in hinglish.AKA:
        return ""
    return f'<p class="aka">{hinglish.LABEL} <span lang="hi-Latn">{e(" · ".join(hinglish.AKA[slug]))}</span></p>'

def channel_html(lang, cls="chan"):
    """A small 'join the WhatsApp channel' block, or nothing while WA_CHANNEL is empty."""
    if not WA_CHANNEL:
        return ""
    a, b = CHANNEL_TXT[lang]
    return f'<p class="{cls}"><span>{a}</span> <a class="btn btn-wa btn-sm" href="{WA_CHANNEL}" target="_blank" rel="noopener">{b} <span aria-hidden="true">→</span></a></p>'
REVIEW = "https://g.page/r/CYmK8BpICDd6EBM/review"

L = {
 "en": dict(home="Home", conds="Conditions", procs="Procedures", answers="Answers", tips="Daily tips", book="Book a visit",
   by="By Dr. Kshitij Lochab, Consultant Gastroenterologist", upd="Updated", symptoms="Common symptoms", causes="Causes and risk factors",
   tests="How it is diagnosed", treat="Treatment", proc_help="Procedures that may help", diet="Diet guide", more="Eat more", less="Cut down",
   know="Good to know", when="When to see a gastroenterologist", faq="Common questions", related="Related conditions", read="Read next",
   uses="What it is used for", expect="What to expect", risks="Risks", treats="Conditions it is used for", short="Short answer",
   cta_h="Book a consultation", cta_p="Appointments and video consultations", cta_call="Call or WhatsApp", cta_wa="Message on WhatsApp",
   clinic="Arcura Clinic, M2K Corporate Park, 14, Mayfield Garden, Sector 51, Gurugram", also="Also at Apollo Hospitals, Golf Course Road",
   disc="This page is for general health education and does not replace a consultation. In an emergency, call 112 or go to the nearest emergency department.",
   reg="Haryana Medical Council Reg. No. HN-23524", lang_link="हिंदी", lang_aria="यह पेज हिंदी में पढ़ें", city="in Gurgaon (Gurugram)", hours="Mon–Fri 6–8 pm · Sun 9 am–1 pm",
   all_guides="More guides", guides="Guides",
   special="Special guides:", special_p="read the guide for your situation, with diet advice and the warning signs to watch for.",
   about="How it works", prep="Before the procedure", day="On the day", glance="At a glance", after="After the procedure",
   alarm="Get medical help straight away if you have", alts="Other tests and options", where="{n} in Gurgaon (Gurugram)",
   where_p="Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist (DrNB Gastroenterology, Medanta; Advanced Fellowship in EUS and ERCP), sees patients in Gurugram (Gurgaon) at Arcura Clinic, M2K Corporate Park, Sector 51, and at Apollo Hospitals, Golf Course Road. Book a consultation by call or WhatsApp on +91 96671 04882. Video consultations are available to go through your reports before a visit."),
 "hi": dict(home="होम", conds="बीमारियाँ", procs="जाँच और इलाज", answers="सवाल-जवाब", tips="रोज़ की सलाह", book="अपॉइंटमेंट",
   by="लेखक: डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट", upd="अपडेट", symptoms="आम लक्षण", causes="वजहें और ख़तरे",
   tests="जाँच कैसे होती है", treat="इलाज", proc_help="इलाज में मदद करने वाले प्रोसीजर", diet="डाइट गाइड", more="ज़्यादा खाएँ", less="कम करें",
   know="जानने लायक", when="गैस्ट्रोएंटेरोलॉजिस्ट को कब दिखाएँ", faq="आम सवाल", related="जुड़ी हुई बीमारियाँ", read="यह भी पढ़ें",
   uses="यह किसके लिए किया जाता है", expect="क्या उम्मीद करें", risks="जोखिम", treats="किन बीमारियों में किया जाता है", short="छोटा जवाब",
   cta_h="अपॉइंटमेंट लें", cta_p="अपॉइंटमेंट और वीडियो कंसल्टेशन", cta_call="कॉल या WhatsApp करें", cta_wa="WhatsApp पर मैसेज करें",
   clinic="आर्क्योरा क्लिनिक, M2K कॉर्पोरेट पार्क, 14, मेफ़ील्ड गार्डन, सेक्टर 51, गुरुग्राम", also="अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड में भी",
   disc="यह पेज सामान्य स्वास्थ्य जानकारी के लिए है और डॉक्टर की सलाह की जगह नहीं ले सकता। इमरजेंसी में 112 पर कॉल करें या सबसे पास की इमरजेंसी में जाएँ।",
   reg="हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524", lang_link="English", lang_aria="Read this page in English", city="गुरुग्राम (गुड़गाँव)", hours="सोम–शुक्र शाम 6–8 · रवि सुबह 9–1",
   all_guides="और गाइड", guides="गाइड",
   special="ख़ास गाइड:", special_p="अपनी स्थिति के लिए गाइड पढ़ें, जिसमें खाने की सलाह और ख़तरे के संकेत दिए गए हैं।",
   about="यह कैसे होता है", prep="प्रोसीजर से पहले", day="प्रोसीजर वाले दिन", glance="एक नज़र में", after="प्रोसीजर के बाद",
   alarm="इनमें से कुछ भी हो तो तुरंत डॉक्टर को दिखाएँ", alts="दूसरी जाँचें और विकल्प", where="गुरुग्राम (गुड़गाँव) में {n}",
   where_p="डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट (DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता; EUS और ERCP में एडवांस्ड फ़ेलोशिप), गुरुग्राम (गुड़गाँव) में आर्क्योरा क्लिनिक, M2K कॉर्पोरेट पार्क, सेक्टर 51, और अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड में मरीज़ देखते हैं। अपॉइंटमेंट के लिए +91 96671 04882 पर कॉल या WhatsApp करें। मिलने से पहले रिपोर्ट दिखाने के लिए वीडियो कंसल्टेशन भी उपलब्ध है।"),
}

e = lambda s: html.escape(s, quote=True)

def load():
    subprocess.run(["node", "extract.js", "en"], check=True, capture_output=True)
    subprocess.run(["node", "extract.js", "hi"], check=True, capture_output=True)
    return {k: json.load(open(f"data-{k}.json")) for k in ("en", "hi")}

def pre(lang): return "/" if lang == "en" else "/hi/"
def url(lang, kind, slug): return f"{pre(lang)}{kind}/{slug}/"

def head(lang, title, desc, path_en, path_hi, ld):
    canon = SITE + (path_en if lang == "en" else path_hi)
    fonts = "family=Young+Serif&family=Figtree:wght@400;500;600;700" + ("&family=Tiro+Devanagari+Hindi&family=Mukta:wght@400;500;600;700" if lang == "hi" else "")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en" href="{SITE}{path_en}">
<link rel="alternate" hreflang="hi" href="{SITE}{path_hi}">
<link rel="alternate" hreflang="x-default" href="{SITE}{path_en}">
<meta name="theme-color" content="#0B6A5E">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="article">
<meta property="og:url" content="{canon}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<link rel="stylesheet" href="/assets/pages.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body class="lang-{lang}">"""

def header(lang, other_path):
    t = L[lang]; p = pre(lang)
    return f"""
<header class="top"><div class="wrap">
  <a class="brand" href="{p}"><img src="/logo-mark.svg" alt="" width="40" height="40"><span><span class="brand-name">Dr. Kshitij Lochab</span><span class="brand-sub">{'Gastroenterology · Liver · Endoscopy' if lang=='en' else 'पेट · लिवर · एंडोस्कोपी'}</span></span></a>
  <nav aria-label="Main"><a href="{p}#conditions">{t['conds']}</a><a href="{p}#procedures">{t['procs']}</a><a href="{p}#conditions">{t['answers']}</a><a href="{p}#daily">{t['tips']}</a><a class="btn btn-solid btn-sm" href="{p}#visit">{t['book']}</a></nav>
  <a class="lang" href="{other_path}" lang="{'hi' if lang=='en' else 'en'}" aria-label="{t['lang_aria']}">{t['lang_link']}</a>
</div></header>""" + season_bar(lang, other_path)

def season_bar(lang, here=""):
    """Slim banner(s) under the header linking to a timely guide. seo_en.SEASONAL is a list of dicts with slug, until and an optional start;
    seo_hi.SEASONAL holds the Hindi text in the same order. Each banner shows only between start and until, checked at build time and in the browser."""
    import datetime
    cfgs = getattr(seo_en, "SEASONAL", None) or []
    if isinstance(cfgs, dict):
        cfgs = [cfgs]
    his = seo_hi.SEASONAL if isinstance(seo_hi.SEASONAL, list) else [seo_hi.SEASONAL]
    now = datetime.datetime.now(datetime.timezone.utc)
    out = ""
    for cfg, hx in zip(cfgs, his):
        if cfg["slug"] in here or now >= datetime.datetime.fromisoformat(cfg["until"]):
            continue
        start = cfg.get("start")
        hidden = " hidden" if start and now < datetime.datetime.fromisoformat(start) else ""
        x = cfg if lang == "en" else hx
        out += (f'<aside class="season"{hidden} aria-label="{"Festival guide" if lang == "en" else "त्योहार गाइड"}" data-from="{start or ""}" data-until="{cfg["until"]}"><div class="wrap"><span class="season-dot" aria-hidden="true"></span>'
                f'<p>{e(x["text"])}</p><a class="season-btn" href="{url(lang, "guides", cfg["slug"])}">{e(x["btn"])} <span aria-hidden="true">→</span></a></div></aside>')
    if not out:
        return ""
    return out + ('<script data-season>(function(){var n=new Date();document.querySelectorAll("aside.season").forEach(function(s){'
                  'var f=s.dataset.from,u=s.dataset.until;if(n>=new Date(u)||(f&&n<new Date(f)))s.remove();else s.hidden=false;});})();</script>')

def crumbs(lang, mid_label, mid_anchor, name):
    p = pre(lang); t = L[lang]
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{p}">{t["home"]}</a><span>›</span><a href="{p}#{mid_anchor}">{mid_label}</a><span>›</span><span aria-current="page">{e(name)}</span></nav>'

def byline(lang, upd=None):
    t = L[lang]; u = upd or UPDATED
    return f'<p class="byline">{t["by"]} · {t["upd"]} {u[1] if lang=="en" else u[2]}</p>'

def ul(items): return "<ul>" + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"

def faq_html(lang, faqs):
    return f'<section><h2>{L[lang]["faq"]}</h2><div class="faqs">' + "".join(
        f'<div class="faq"><h3>{e(q)}</h3><p>{e(a)}</p></div>' for q, a in faqs) + "</div></section>"

def links(items):
    return '<div class="links">' + "".join(f'<a href="{h}">{e(n)} <span aria-hidden="true">→</span></a>' for h, n in items) + "</div>"

def aside(lang):
    t = L[lang]
    return f"""<aside class="cta"><h2>{t['cta_h']}</h2><p class="lbl">{t['cta_p']}</p><p class="num">{PHONE}</p><p class="small">{t['cta_call']}</p>
<a class="btn btn-solid" href="{WA}" target="_blank" rel="noopener">{t['cta_wa']}</a>
<p class="small">{t['clinic']}</p><p class="small"><b>{t['hours']}</b></p><p class="small">{t['also']}</p>
<p class="small"><a href="{pre(lang)}about-dr-kshitij-lochab/">{FOOT_LINKS[lang][0]} →</a></p></aside>"""

def footer(lang):
    t = L[lang]
    fl = f'<p class="foot-links"><a href="{pre(lang)}about-dr-kshitij-lochab/">{FOOT_LINKS[lang][0]}</a> · <a href="{pre(lang)}gastroenterologist-in-gurgaon/">{FOOT_LINKS[lang][1]}</a> · <a href="{pre(lang)}tools/gut-tracker/">{FOOT_LINKS[lang][2]}</a></p>'
    return f"""<footer><div class="wrap">{channel_html(lang, "chan chan-foot")}{fl}<p>{t['disc']}</p><p>Dr. Kshitij Lochab · {t['reg']} · {PHONE}</p><p>© 2026 Dr. Kshitij Lochab</p></div></footer>
<a class="fab" href="{WA}" target="_blank" rel="noopener">{t['book']}</a>
</body></html>"""

def physician(lang):
    return {"@type": "Physician", "@id": "https://drlochab.com/#physician", "name": "Dr. Kshitij Lochab", "url": SITE + pre(lang), "medicalSpecialty": "Gastroenterologic",
            "sameAs": ["https://share.google/9ZndZsg6NHVxeQfYl", "https://www.instagram.com/drlochab/", "https://www.linkedin.com/in/drlochab/"],
            "telephone": "+91-9667104882", "address": {"@type": "PostalAddress", "streetAddress": "Arcura Clinic, M2K Corporate Park, 14, Mayfield Garden, Sector 51",
            "addressLocality": "Gurugram", "addressRegion": "Haryana", "postalCode": "122018", "addressCountry": "IN"}}

def ld_page(lang, path, name, desc, about_type, about_name, faqs, mid_label, mid_anchor, upd=None):
    p = pre(lang); u = upd or UPDATED
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "MedicalWebPage", "name": name, "description": desc, "url": SITE + path, "inLanguage": lang,
         "lastReviewed": u[0], "dateModified": u[0], "author": physician(lang), "reviewedBy": physician(lang),
         "about": {"@type": about_type, "name": about_name}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": L[lang]["home"], "item": SITE + p},
            {"@type": "ListItem", "position": 2, "name": mid_label, "item": f"{SITE}{p}#{mid_anchor}"},
            {"@type": "ListItem", "position": 3, "name": name, "item": SITE + path}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}]}

def write(path, text):
    full = "site" + path + "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(text)

def answer_links(lang, S, ans):
    """Links to one answer slug or a list of them, in the page language."""
    slugs = [a["slug"] for a in seo_en.ANSWERS]
    out = []
    for slug in ([ans] if isinstance(ans, str) else (ans or [])):
        k = slugs.index(slug)
        out.append((url(lang, "answers", slug), S.ANSWERS[k]["q"]))
    return out

def guide_notes(lang, kind, idx):
    """One callout box linking a condition or procedure page to the special guides that list it."""
    S = seo_en if lang == "en" else seo_hi
    hits = [(g, x) for g, x in zip(seo_en.SPECIAL, S.SPECIAL) if idx in g[kind]]
    if not hits:
        return ""
    if len(hits) == 1:
        g, x = hits[0]
        text = f'<p><b>{e(x["note_q"])}</b> {e(x["note_p"])}</p>'
    else:
        text = f'<p><b>{L[lang]["special"]}</b> {L[lang]["special_p"]}</p>'
    return f'<section class="note">{text}' + links([(url(lang, "guides", g["slug"]), x["name"]) for g, x in hits]) + "</section>"

def build():
    D = load()
    pages = []
    for lang, S in (("en", seo_en), ("hi", seo_hi)):
        d, t = D[lang], L[lang]
        # ---- conditions
        for i, c in enumerate(d["CONDITIONS"]):
            base = seo_en.CONDS[i]; x = S.CONDS[i]
            path, path_en, path_hi = url(lang, "conditions", base["slug"]), url("en", "conditions", base["slug"]), url("hi", "conditions", base["slug"])
            title = f"{x['seo']} {t['city']} | Dr. Kshitij Lochab" if lang == "en" else f"{x['seo']}, {t['city']} | डॉ. क्षितिज लोचब"
            desc = (c["s"] + " " + c["w"])[:155].rsplit(" ", 1)[0] + "…"
            body = [f'<p class="lead">{e(c["w"])}</p>',
                    f'<section><h2>{t["symptoms"]}</h2>{ul(c["g"])}</section>',
                    f'<section><h2>{t["causes"]}</h2>{ul(x["causes"])}</section>',
                    f'<section><h2>{t["tests"]}</h2><p>{e(x["tests"])}</p></section>',
                    f'<section><h2>{t["treat"]}</h2><p>{e(c["h"])}</p></section>']
            if base["procs"]:
                body.append(f'<section><h2>{t["proc_help"]}</h2>' + links([(url(lang, "procedures", seo_en.PROCS[j]["slug"]), d["PROCS"][j]["n"]) for j in base["procs"]]) + "</section>")
            if base["guide"] is not None:
                g = d["GUIDES"][base["guide"]]
                body.append(f'<section><h2>{t["diet"]}: {e(g["n"])}</h2><div class="guide">'
                            f'<div class="gcol more"><h3>{t["more"]}</h3>{ul(g["more"])}</div>'
                            f'<div class="gcol less"><h3>{t["less"]}</h3>{ul(g["less"])}</div>'
                            f'<div class="gcol know"><h3>{t["know"]}</h3>{ul(g["know"])}</div></div></section>')
            elif base["slug"] in cond_diet_en.DIET:
                g = (cond_diet_en if lang == "en" else cond_diet_hi).DIET[base["slug"]]
                body.append(f'<section><h2>{e(g["h"])}</h2><div class="guide">'
                            f'<div class="gcol more"><h3>{t["more"]}</h3>{ul(g["more"])}</div>'
                            f'<div class="gcol less"><h3>{t["less"]}</h3>{ul(g["less"])}</div>'
                            f'<div class="gcol know"><h3>{t["know"]}</h3>{ul(g["know"])}</div></div></section>')
            body.append(f'<section class="see"><h2>{t["when"]}</h2><p>{e(c["e"])}</p></section>')
            if base["slug"] in TRACK_CONDS:
                body.append(tracker_note(lang))
            body.append(guide_notes(lang, "conds", i))
            body.append(faq_html(lang, x["faqs"]))
            reads = answer_links(lang, S, base["answer"])
            rel = [(url(lang, "conditions", seo_en.CONDS[j]["slug"]), d["CONDITIONS"][j]["n"]) for j, cc in enumerate(d["CONDITIONS"]) if cc["o"] == c["o"] and j != i]
            if reads: body.append(f'<section><h2>{t["read"]}</h2>{links(reads)}</section>')
            if rel: body.append(f'<section><h2>{t["related"]}</h2>{links(rel)}</section>')
            ld = ld_page(lang, path, c["n"], desc, "MedicalCondition", c["n"], x["faqs"], t["conds"], "conditions")
            page = (head(lang, title, desc, path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["conds"], "conditions", c["n"])}'
                    + f'<p class="eyebrow">{e(d["ORGANS"][c["o"]])}</p><h1>{e(c["n"])}</h1>{aka(lang, base["slug"])}{byline(lang)}' + "".join(body)
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
        # ---- procedures
        for i, pr in enumerate(d["PROCS"][:len(seo_en.PROCS)]):  # extra home tiles (capsule) link to answer pages
            base = seo_en.PROCS[i]; x = S.PROCS[i]
            path, path_en, path_hi = url(lang, "procedures", base["slug"]), url("en", "procedures", base["slug"]), url("hi", "procedures", base["slug"])
            title = f"{x['seo']} {t['city']} | Dr. Kshitij Lochab" if lang == "en" else f"{x['seo']}, {t['city']} | डॉ. क्षितिज लोचब"
            M = (seo_proc_en if lang == "en" else seo_proc_hi).MORE.get(base["slug"], {})
            desc = M.get("desc") or (pr["w"][:155].rsplit(" ", 1)[0] + "…")
            faqs = x["faqs"] + M.get("faqs", [])
            table = '<dl class="expect">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in pr["d"]) + "</dl>"
            sec = lambda h, inner: f"<section><h2>{h}</h2>{inner}</section>"
            body = [f'<figure class="fig">{d["IL"][pr["il"]]}</figure>', f'<p class="lead">{e(pr["w"])}</p>']
            if M.get("intro"): body.append(sec(t["about"], "".join(f"<p>{e(p_)}</p>" for p_ in M["intro"])))
            body.append(sec(t["uses"], ul(x["uses"])))
            if M.get("prep"): body.append(sec(t["prep"], ul(M["prep"])))
            if M.get("day"): body.append(sec(t["day"], f"<p>{e(M['day'])}</p><h3>{t['glance']}</h3>{table}"))
            else: body.append(sec(t["expect"], table))
            if M.get("after"): body.append(sec(t["after"], ul(M["after"])))
            body.append(sec(t["risks"], f"<p>{e(M.get('risks') or x['risks'])}</p>"))
            if M.get("alarm"): body.append(f'<section class="alarm"><h2>{t["alarm"]}</h2>{ul(M["alarm"])}<p class="small">{e(t["disc"])}</p></section>')
            if M.get("alts"): body.append(sec(t["alts"], f"<p>{e(M['alts'])}</p>"))
            body.append(sec(t["treats"], links([(url(lang, "conditions", seo_en.CONDS[j]["slug"]), d["CONDITIONS"][j]["n"]) for j in base["conds"]])))
            body.append(guide_notes(lang, "procs", i))
            if M: body.append(sec(e(t["where"].format(n=x["seo"])), f"<p>{e(t['where_p'])}</p>"))
            body.append(faq_html(lang, faqs))
            if base["answer"]:
                body.append(f'<section><h2>{t["read"]}</h2>' + links(answer_links(lang, S, base["answer"])) + "</section>")
            upd = PROC_UPDATED if M else None
            ld = ld_page(lang, path, pr["n"], desc, "MedicalProcedure", pr["n"], faqs, t["procs"], "procedures", upd)
            page = (head(lang, title, desc, path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["procs"], "procedures", pr["n"])}'
                    + f'<p class="eyebrow">{e(pr["a"])}</p><h1>{e(pr["n"])}</h1>{byline(lang, upd)}' + "".join(body)
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
        # ---- answers
        for i, a in enumerate(S.ANSWERS):
            base = seo_en.ANSWERS[i]
            path, path_en, path_hi = url(lang, "answers", base["slug"]), url("en", "answers", base["slug"]), url("hi", "answers", base["slug"])
            title = f"{a['q']} | Dr. Kshitij Lochab, Gurgaon" if lang == "en" else f"{a['q']} | डॉ. क्षितिज लोचब, गुड़गाँव"
            secs = []
            for h, parts in a["sections"]:
                items = [p_[2:] for p_ in parts if p_.startswith("- ")]
                paras = [p_ for p_ in parts if not p_.startswith("- ")]
                secs.append(f"<section><h2>{e(h)}</h2>" + "".join(f"<p>{e(p_)}</p>" for p_ in paras) + (ul(items) if items else "") + "</section>")
            X = (answers_extra_en if lang == "en" else answers_extra_hi).EXTRA.get(base["slug"])
            xfaqs = []
            if X:
                dt = X["diet"]; lb = dt.get("labels") or (t["more"], t["less"], t["know"])
                secs.append(f'<section><h2>{e(dt["h"])}</h2><div class="guide">'
                            f'<div class="gcol more"><h3>{e(lb[0])}</h3>{ul(dt["more"])}</div>'
                            f'<div class="gcol less"><h3>{e(lb[1])}</h3>{ul(dt["less"])}</div>'
                            f'<div class="gcol know"><h3>{e(lb[2])}</h3>{ul(dt["know"])}</div></div></section>')
                xfaqs = X["faqs"]
                secs.append(faq_html(lang, xfaqs))
            rel = []
            if base.get("cond") is not None:
                rel.append((url(lang, "conditions", seo_en.CONDS[base["cond"]]["slug"]), d["CONDITIONS"][base["cond"]]["n"]))
            if base.get("proc") is not None:
                rel.append((url(lang, "procedures", seo_en.PROCS[base["proc"]]["slug"]), d["PROCS"][base["proc"]]["n"]))
            # the next three answers in turn, so every answer page is linked from three others
            n = len(S.ANSWERS)
            others = [(url(lang, "answers", seo_en.ANSWERS[(i + k) % n]["slug"]), S.ANSWERS[(i + k) % n]["q"]) for k in range(1, min(4, n))]
            fig = f'<figure class="fig">{d["IL"][ANSWER_IL[base["slug"]]]}</figure>' if base["slug"] in ANSWER_IL else ""
            body = (fig + f'<div class="short"><p class="lbl">{t["short"]}</p><p>{e(a["short"])}</p></div>' + "".join(secs)
                    + f'<section><h2>{t["read"]}</h2>{links(rel + others)}</section>')
            ld = ld_page(lang, path, a["q"], a["desc"], "MedicalProcedure" if base.get("cond") is None and base.get("proc") is not None else "MedicalCondition",
                         rel[0][1] if rel else a["q"], [[a["q"], a["short"]]] + xfaqs, t["answers"], "conditions")
            page = (head(lang, title, a["desc"], path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["answers"], "conditions", a["q"])}'
                    + f'<p class="eyebrow">{t["answers"]}</p><h1>{e(a["q"])}</h1>{aka(lang, base["slug"])}{byline(lang)}' + body
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
        # ---- special guides
        for i, x in enumerate(S.SPECIAL):
            base = seo_en.SPECIAL[i]
            path, path_en, path_hi = url(lang, "guides", base["slug"]), url("en", "guides", base["slug"]), url("hi", "guides", base["slug"])
            hp = lambda items: "".join(f'<div class="faq"><h3>{e(h)}</h3><p>{e(p_)}</p></div>' for h, p_ in items)
            def block(bid, kind):
                if kind == "cards":
                    return (f'<section id="{bid}"><h2>{e(x["tri_h"])}</h2><div class="tri">'
                            + "".join(f'<div class="tri-card"><p class="lbl">{e(w)}</p><h3>{e(h)}</h3>{ul(items)}</div>' for w, h, items in x["tri"]) + "</div></section>")
                if kind == "probs":
                    return (f'<section id="{bid}"><h2>{e(x["prob_h"])}</h2><div class="probs">'
                            + "".join(f'<div class="prob"><h3>{e(h)}</h3><p>{e(p_)}</p><p class="lbl">{e(x["help_lbl"])}</p>{ul(items)}<p class="prob-see">{e(see)}</p></div>'
                                      for h, p_, items, see in x["probs"]) + "</div></section>")
                if kind == "attn":
                    return f'<section id="{bid}"><h2>{e(x["liver_h"])}</h2><p>{e(x["liver_p"])}</p><div class="faqs">{hp(x["liver"])}</div></section>'
                if kind == "urgent":
                    return f'<section id="{bid}" class="urgent"><h2>{e(x["urgent_h"])}</h2>{ul(x["urgent"])}<p>{e(x["urgent_p"])}</p></section>'
                if kind == "pre":
                    return f'<section id="{bid}"><h2>{e(x["pre_h"])}</h2><p>{e(x["pre_p"])}</p><div class="faqs">{hp(x["pre"])}</div></section>'
                if kind == "diet":
                    day = '<dl class="expect day">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in x["day"]) + "</dl>"
                    return (f'<section id="{bid}"><h2>{e(x["diet_h"])}</h2><p>{e(x["diet_p"])}</p><div class="guide">'
                            f'<div class="gcol more"><h3>{t["more"]}</h3>{ul(x["more"])}</div>'
                            f'<div class="gcol less"><h3>{t["less"]}</h3>{ul(x["less"])}</div>'
                            f'<div class="gcol know"><h3>{t["know"]}</h3>{ul(x["know"])}</div></div>'
                            f'<h3 class="day-h">{e(x["day_h"])}</h3>{day}</section>')
                if kind == "test":
                    return f'<section id="{bid}"><h2>{e(x["test_h"])}</h2>' + "".join(f"<p>{e(p_)}</p>" for p_ in x["test"]) + "</section>"
                if kind == "care":
                    return f'<section id="{bid}"><h2>{e(x["care_h"])}</h2><p>{e(x["care"])}</p></section>'
                if kind == "who":
                    return f'<section id="{bid}" class="note"><h2>{e(x["care_h"])}</h2><p>{e(x["care"])}</p></section>'
                raise SystemExit(f"unknown guide block {kind}")
            listed = [(bid, kind) for bid, kind in base["blocks"] if kind not in ("care", "who")]
            assert len(listed) == len(x["toc"]), (base["slug"], lang, "toc labels must match the listed blocks")
            toc = (f'<nav class="toc" aria-label="{e(x["toc_lbl"])}"><p class="lbl">{e(x["toc_lbl"])}</p>'
                   + "".join(f'<a href="#{bid}">{e(l_)}</a>' for (bid, _), l_ in zip(listed, x["toc"])) + "</nav>")
            body = [f'<figure class="fig">{guide_art.ART[base["slug"]](e(x["alt"]))}</figure>', f'<p class="lead">{e(x["lead"])}</p>',
                    f'<div class="short"><p class="lbl">{e(x["short_lbl"])}</p><p>{e(x["short"])}</p></div>', toc]
            body += [block(bid, kind) for bid, kind in base["blocks"]]
            body.append(faq_html(lang, x["faqs"]))
            reads = (answer_links(lang, S, base["answers"])
                     + [(url(lang, "conditions", seo_en.CONDS[j]["slug"]), d["CONDITIONS"][j]["n"]) for j in base["conds"]]
                     + [(url(lang, "procedures", seo_en.PROCS[j]["slug"]), d["PROCS"][j]["n"]) for j in base["procs"]])
            body.append(f'<section><h2>{t["read"]}</h2>{links(reads)}</section>')
            ld = ld_page(lang, path, x["h1"], x["desc"], "MedicalCondition", x["name"], x["faqs"], t["guides"], "guides", base.get("updated"))
            page = (head(lang, x["title"], x["desc"], path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["guides"], "guides", x["name"])}'
                    + f'<p class="eyebrow">{e(x["eyebrow"])}</p><h1>{e(x["h1"])}</h1>{byline(lang, base.get("updated"))}' + "".join(body)
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
    # ---- tools
    import stool_check, sys
    for lang in ("en", "hi"):
        path, path_en, path_hi, page = stool_check.render(lang, sys.modules[__name__])
        write(path, page); pages.append((path_en, path_hi))
        import gut_tracker
        path, path_en, path_hi, page = gut_tracker.render(lang, sys.modules[__name__])
        write(path, page); pages.append((path_en, path_hi))
        import local_pages
        cl = [(url(lang, "conditions", seo_en.CONDS[j]["slug"]), D[lang]["CONDITIONS"][j]["n"]) for j in range(len(seo_en.CONDS))]
        pl = [(url(lang, "procedures", seo_en.PROCS[j]["slug"]), D[lang]["PROCS"][j]["n"]) for j in range(len(seo_en.PROCS))]
        for kind in ("local", "about"):
            path, path_en, path_hi, page = local_pages.render(lang, sys.modules[__name__], kind, cl, pl)
            write(path, page); pages.append((path_en, path_hi))
    os.makedirs("site/assets", exist_ok=True)
    il_css = open("insta/illus.css").read()
    open("site/assets/pages.css", "w").write(open("pages.css").read() + il_css)
    return sorted(set(pages))

if __name__ == "__main__":
    print(len(build()), "page pairs")
