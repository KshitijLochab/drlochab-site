"""Generates condition, procedure and answer pages (English and Hindi) into site/.
Run after build_site.py has written site/index.html and site/hi/index.html."""
import json, os, html, subprocess
import seo_en, seo_hi, guide_art

SITE = "https://drlochab.com"
UPDATED = ("2026-10-10", "10 October 2026", "10 अक्टूबर 2026")
PHONE, WA = "+91 96671 04882", "https://wa.me/919667104882"
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
   reg="Haryana Medical Council Reg. No. HN-23524", lang_link="हिंदी", lang_aria="यह पेज हिंदी में पढ़ें", city="in Gurugram",
   all_guides="More guides", guides="Guides",
   special="Special guides:", special_p="read the guide for your situation, with diet advice and the warning signs to watch for."),
 "hi": dict(home="होम", conds="बीमारियाँ", procs="जाँच और इलाज", answers="सवाल-जवाब", tips="रोज़ की सलाह", book="अपॉइंटमेंट",
   by="लेखक: डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट", upd="अपडेट", symptoms="आम लक्षण", causes="वजहें और ख़तरे",
   tests="जाँच कैसे होती है", treat="इलाज", proc_help="इलाज में मदद करने वाले प्रोसीजर", diet="डाइट गाइड", more="ज़्यादा खाएँ", less="कम करें",
   know="जानने लायक", when="गैस्ट्रोएंटेरोलॉजिस्ट को कब दिखाएँ", faq="आम सवाल", related="जुड़ी हुई बीमारियाँ", read="यह भी पढ़ें",
   uses="यह किसके लिए किया जाता है", expect="क्या उम्मीद करें", risks="जोखिम", treats="किन बीमारियों में किया जाता है", short="छोटा जवाब",
   cta_h="अपॉइंटमेंट लें", cta_p="अपॉइंटमेंट और वीडियो कंसल्टेशन", cta_call="कॉल या WhatsApp करें", cta_wa="WhatsApp पर मैसेज करें",
   clinic="आर्क्योरा क्लिनिक, M2K कॉर्पोरेट पार्क, 14, मेफ़ील्ड गार्डन, सेक्टर 51, गुरुग्राम", also="अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड में भी",
   disc="यह पेज सामान्य स्वास्थ्य जानकारी के लिए है और डॉक्टर की सलाह की जगह नहीं ले सकता। इमरजेंसी में 112 पर कॉल करें या सबसे पास की इमरजेंसी में जाएँ।",
   reg="हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524", lang_link="English", lang_aria="Read this page in English", city="गुरुग्राम",
   all_guides="और गाइड", guides="गाइड",
   special="ख़ास गाइड:", special_p="अपनी स्थिति के लिए गाइड पढ़ें, जिसमें खाने की सलाह और ख़तरे के संकेत दिए गए हैं।"),
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
  <nav aria-label="Main"><a href="{p}#conditions">{t['conds']}</a><a href="{p}#procedures">{t['procs']}</a><a href="{p}#answers">{t['answers']}</a><a href="{p}#daily">{t['tips']}</a><a class="btn btn-solid btn-sm" href="{p}#visit">{t['book']}</a></nav>
  <a class="lang" href="{other_path}" lang="{'hi' if lang=='en' else 'en'}" aria-label="{t['lang_aria']}">{t['lang_link']}</a>
</div></header>""" + season_bar(lang, other_path)

def season_bar(lang, here=""):
    """Slim banner under the header linking to a timely guide; left out after seo_en.SEASONAL['until'] (at build time and in the browser)."""
    import datetime
    cfg = getattr(seo_en, "SEASONAL", None)
    if not cfg or cfg["slug"] in here:
        return ""
    if datetime.datetime.now(datetime.timezone.utc) >= datetime.datetime.fromisoformat(cfg["until"]):
        return ""
    x = cfg if lang == "en" else seo_hi.SEASONAL
    return (f'<aside class="season" id="season" aria-label="{"Festival guide" if lang == "en" else "त्योहार गाइड"}" data-until="{cfg["until"]}"><div class="wrap"><span class="season-dot" aria-hidden="true"></span>'
            f'<p>{e(x["text"])}</p><a class="season-btn" href="{url(lang, "guides", cfg["slug"])}">{e(x["btn"])} <span aria-hidden="true">→</span></a></div></aside>'
            '<script data-season>(function(){var s=document.getElementById("season");if(s&&new Date()>=new Date(s.dataset.until))s.remove();})();</script>')

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
<p class="small">{t['clinic']}</p><p class="small">{t['also']}</p></aside>"""

def footer(lang):
    t = L[lang]
    return f"""<footer><div class="wrap"><p>{t['disc']}</p><p>Dr. Kshitij Lochab · {t['reg']} · {PHONE}</p><p>© 2026 Dr. Kshitij Lochab</p></div></footer>
<aside aria-label="{t['book']}"><a class="fab" href="{WA}" target="_blank" rel="noopener">{t['book']}</a></aside>
</body></html>"""

def physician(lang):
    return {"@type": "Physician", "name": "Dr. Kshitij Lochab", "url": SITE + pre(lang), "medicalSpecialty": "Gastroenterologic",
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

def page_title(lang, seo):
    """Condition and procedure titles; uses the short name when the full title would be cut off in search results (about 65 characters)."""
    t = L[lang]
    full = f"{seo} {t['city']} | Dr. Kshitij Lochab" if lang == "en" else f"{seo}, {t['city']} | डॉ. क्षितिज लोचब"
    if len(full) <= 65: return full
    return f"{seo} {t['city']} | Dr. Lochab" if lang == "en" else f"{seo}, {t['city']} | डॉ. लोचब"

def meta_desc(lang, kind, name, lead):
    """A complete meta description (no cut-off text): for conditions the name and its one-line summary, for procedures the
    procedure name, then what the page covers and who wrote it. Kept to about 160 characters."""
    if kind == "cond":
        tail = " Symptoms, tests and treatment by Dr. Kshitij Lochab, Gurugram." if lang == "en" else " लक्षण, जाँच और इलाज, गुरुग्राम के डॉ. क्षितिज लोचब से जानें।"
        return f"{name}: {lead}{tail}"
    if lang == "en":
        return f"{name} in Gurugram: what it is used for, what to expect, risks and recovery, explained by Dr. Kshitij Lochab."
    return f"{name}, गुरुग्राम: यह कब किया जाता है, क्या उम्मीद करें, जोखिम और रिकवरी, डॉ. क्षितिज लोचब से जानें।"

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
            title = page_title(lang, x["seo"])
            desc = meta_desc(lang, "cond", c["n"], c["s"])
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
            body.append(f'<section class="see"><h2>{t["when"]}</h2><p>{e(c["e"])}</p></section>')
            body.append(guide_notes(lang, "conds", i))
            body.append(faq_html(lang, x["faqs"]))
            reads = answer_links(lang, S, base["answer"])
            rel = [(url(lang, "conditions", seo_en.CONDS[j]["slug"]), d["CONDITIONS"][j]["n"]) for j, cc in enumerate(d["CONDITIONS"]) if cc["o"] == c["o"] and j != i]
            if reads: body.append(f'<section><h2>{t["read"]}</h2>{links(reads)}</section>')
            if rel: body.append(f'<section><h2>{t["related"]}</h2>{links(rel)}</section>')
            ld = ld_page(lang, path, c["n"], desc, "MedicalCondition", c["n"], x["faqs"], t["conds"], "conditions")
            page = (head(lang, title, desc, path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["conds"], "conditions", c["n"])}'
                    + f'<p class="eyebrow">{e(d["ORGANS"][c["o"]])}</p><h1>{e(c["n"])}</h1>{byline(lang)}' + "".join(body)
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
        # ---- procedures
        for i, pr in enumerate(d["PROCS"]):
            base = seo_en.PROCS[i]; x = S.PROCS[i]
            path, path_en, path_hi = url(lang, "procedures", base["slug"]), url("en", "procedures", base["slug"]), url("hi", "procedures", base["slug"])
            title = page_title(lang, x["seo"])
            desc = meta_desc(lang, "proc", x["seo"], None)
            table = '<dl class="expect">' + "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in pr["d"]) + "</dl>"
            body = [f'<figure class="fig">{d["IL"][pr["il"]]}</figure>', f'<p class="lead">{e(pr["w"])}</p>',
                    f'<section><h2>{t["uses"]}</h2>{ul(x["uses"])}</section>',
                    f'<section><h2>{t["expect"]}</h2>{table}</section>',
                    f'<section><h2>{t["risks"]}</h2><p>{e(x["risks"])}</p></section>',
                    f'<section><h2>{t["treats"]}</h2>' + links([(url(lang, "conditions", seo_en.CONDS[j]["slug"]), d["CONDITIONS"][j]["n"]) for j in base["conds"]]) + "</section>",
                    guide_notes(lang, "procs", i), faq_html(lang, x["faqs"])]
            if base["answer"]:
                body.append(f'<section><h2>{t["read"]}</h2>' + links(answer_links(lang, S, base["answer"])) + "</section>")
            ld = ld_page(lang, path, pr["n"], desc, "MedicalProcedure", pr["n"], x["faqs"], t["procs"], "procedures")
            page = (head(lang, title, desc, path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["procs"], "procedures", pr["n"])}'
                    + f'<p class="eyebrow">{e(pr["a"])}</p><h1>{e(pr["n"])}</h1>{byline(lang)}' + "".join(body)
                    + f"</article>{aside(lang)}</main>" + footer(lang))
            write(path, page); pages.append((path_en, path_hi))
        # ---- answers
        for i, a in enumerate(S.ANSWERS):
            base = seo_en.ANSWERS[i]
            path, path_en, path_hi = url(lang, "answers", base["slug"]), url("en", "answers", base["slug"]), url("hi", "answers", base["slug"])
            title = f"{a['q']} | Dr. Kshitij Lochab, Gurugram" if lang == "en" else f"{a['q']} | डॉ. क्षितिज लोचब, गुरुग्राम"
            secs = []
            for h, parts in a["sections"]:
                items = [p_[2:] for p_ in parts if p_.startswith("- ")]
                paras = [p_ for p_ in parts if not p_.startswith("- ")]
                secs.append(f"<section><h2>{e(h)}</h2>" + "".join(f"<p>{e(p_)}</p>" for p_ in paras) + (ul(items) if items else "") + "</section>")
            rel = []
            if base.get("cond") is not None:
                rel.append((url(lang, "conditions", seo_en.CONDS[base["cond"]]["slug"]), d["CONDITIONS"][base["cond"]]["n"]))
            if base.get("proc") is not None:
                rel.append((url(lang, "procedures", seo_en.PROCS[base["proc"]]["slug"]), d["PROCS"][base["proc"]]["n"]))
            # the next three answers in turn, so every answer page is linked from three others
            n = len(S.ANSWERS)
            others = [(url(lang, "answers", seo_en.ANSWERS[(i + k) % n]["slug"]), S.ANSWERS[(i + k) % n]["q"]) for k in range(1, min(4, n))]
            body = (f'<div class="short"><p class="lbl">{t["short"]}</p><p>{e(a["short"])}</p></div>' + "".join(secs)
                    + f'<section><h2>{t["read"]}</h2>{links(rel + others)}</section>')
            ld = ld_page(lang, path, a["q"], a["desc"], "MedicalCondition" if base.get("cond") is not None else "MedicalProcedure",
                         rel[0][1] if rel else a["q"], [[a["q"], a["short"]]], t["answers"], "answers", base.get("updated"))
            page = (head(lang, title, a["desc"], path_en, path_hi, ld) + header(lang, path_hi if lang == "en" else path_en)
                    + f'<main class="wrap grid"><article>{crumbs(lang, t["answers"], "answers", a["q"])}'
                    + f'<p class="eyebrow">{t["answers"]}</p><h1>{e(a["q"])}</h1>{byline(lang, base.get("updated"))}' + body
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
    os.makedirs("site/assets", exist_ok=True)
    il_css = open("insta/illus.css").read()
    open("site/assets/pages.css", "w").write(open("pages.css").read() + il_css)
    return sorted(set(pages))

if __name__ == "__main__":
    print(len(build()), "page pairs")
