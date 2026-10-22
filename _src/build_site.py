"""Builds the deployable drlochab.com folder (English at /, Hindi at /hi/) from lochab-gastro.html."""
import json, re, shutil, os
from PIL import Image
import hindi, local_pages

OUT = "site"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(f"{OUT}/hi")

src = open("lochab-gastro.html").read()

schema = {
    "@context": "https://schema.org",
    "@type": "Physician",
    "name": "Dr. Kshitij Lochab",
    "description": "Consultant gastroenterologist and therapeutic endoscopist in Gurugram, trained in EUS and ERCP.",
    "medicalSpecialty": "Gastroenterologic",
    "url": "https://drlochab.com",
    "telephone": "+91-9667104882",
    "image": "https://drlochab.com/dr-lochab.jpg",
    "logo": "https://drlochab.com/logo-mark.png",
    "sameAs": ["https://share.google/9ZndZsg6NHVxeQfYl"],
    "availableLanguage": ["English", "Hindi"],
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Arcura Clinic, M2K Corporate Park & Shopping Plaza, 14, Mayfield Garden, Sector 51",
        "addressLocality": "Gurugram",
        "addressRegion": "Haryana",
        "postalCode": "122003",
        "addressCountry": "IN",
    },
}

PAGES = {
    "en": dict(
        lang="en", url="https://drlochab.com/", up="",
        title="Dr. Kshitij Lochab | Gastroenterologist in Gurgaon (Gurugram)",
        desc=("Gastroenterologist in Gurgaon (Gurugram) at Arcura Clinic, Sector 51. Simple guides to acidity, fatty liver, IBS and jaundice, plus Indian diet charts."),
        og="Clear answers about your stomach, liver and digestion, with a new gut-health tip every day."),
    "hi": dict(
        lang="hi", url="https://drlochab.com/hi/", up="../",
        title="डॉ. क्षितिज लोचब | गुड़गाँव में पेट और लिवर रोग विशेषज्ञ",
        desc=("गुड़गाँव (गुरुग्राम) में गैस्ट्रोएंटेरोलॉजिस्ट, आर्क्योरा क्लिनिक, सेक्टर 51। एसिडिटी, फैटी लिवर, पीलिया और IBS की आसान जानकारी और डाइट चार्ट।"),
        og="पेट, लिवर और पाचन से जुड़े सवालों के सीधे जवाब, और हर दिन सेहत की एक नई सलाह।"),
}

def head(p, extra_links=""):
    up = p["up"]
    return f"""<!doctype html>
<html lang="{p['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{p['title']}</title>
<meta name="description" content="{p['desc']}">
<link rel="canonical" href="{p['url']}">
<link rel="alternate" hreflang="en" href="https://drlochab.com/">
<link rel="alternate" hreflang="hi" href="https://drlochab.com/hi/">
<link rel="alternate" hreflang="x-default" href="https://drlochab.com/">
<meta name="theme-color" content="#0B6A5E">
<link rel="icon" href="{up}logo-mark.svg" type="image/svg+xml">
<link rel="icon" type="image/png" sizes="96x96" href="{up}favicon.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{p['url']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['og']}">
<meta property="og:image" content="https://drlochab.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": [dict(local_pages.physician(full=True), url=p["url"], logo="https://drlochab.com/logo-mark.png")]}, ensure_ascii=False)}</script>
{extra_links}"""

def split(html):
    end = html.index("</style>") + len("</style>")
    top = re.sub(r"<title>.*?</title>\n?", "", html[:end], count=1)
    return top.strip(), html[end:]

def hindi_source(s):
    missing = [en for en, _ in hindi.PAIRS if en not in s]
    if missing:
        raise SystemExit("Hindi build stopped. These English strings changed and need new translations:\n- "
                         + "\n- ".join(m[:90] for m in missing))
    for en, hi in hindi.PAIRS:
        s = s.replace(en, hi)
    a, b = s.index("const ORGANS="), s.index("const esc=")
    s = s[:a] + hindi.DATA_JS + s[b:]
    a = s.index("const GUIDES=[")
    b = s.index("\n];", a) + len("\n];")
    s = s[:a] + hindi.GUIDES_JS + s[b:]
    a, b = s.index("/*PLAY*/"), s.index("/*/PLAY*/")
    s = s[:a] + hindi.PLAY_JS + s[b:]
    s = s.replace('--display:"Young Serif", Georgia,', '--display:"Young Serif","Tiro Devanagari Hindi", Georgia,', 1)
    s = s.replace('--body:"Figtree", system-ui,', '--body:"Figtree","Mukta", system-ui,', 1)
    s = s.replace("</style>", "*{letter-spacing:0!important}\nbody{line-height:1.7}\n</style>", 1)
    left = re.findall(r'"(Loading|Share on|Try this|Showing all|Copy |Book a)[^"]*"', s)
    if left:
        raise SystemExit(f"Hindi build stopped: untranslated interface text {left}")
    return s

import html as _html
import seo_en, seo_hi, hub

def food_js(lang):
    """Food of the day data and labels for one language (see food_day.py)."""
    import food_day
    items = food_day.EN if lang == "en" else [dict(h, ic=e["ic"], col=e["col"]) for h, e in zip(food_day.HI, food_day.EN)]
    return "const FOD=" + json.dumps(items, ensure_ascii=False) + ";\nconst FO=" + json.dumps(food_day.LABELS[lang], ensure_ascii=False) + ";"

def trk_card(lang):
    """The gut tracker card at the top of the home page, rendered in HTML so the hero does not jump when the script runs."""
    import food_day
    FO = food_day.LABELS[lang]
    esc = lambda x: _html.escape(x, quote=True)
    bars = "".join(f'<rect class="trk-bar" style="animation-delay:{i*.08:g}s" x="{x-3}" y="{39-h}" width="6" height="{h}" rx="3" fill="{"#F3C66B" if i == 4 else "#fff"}"/>'
                   for i, (x, h) in enumerate([[8,22],[16,12],[24,26],[32,16],[40,30]]))
    art = ('<svg viewBox="0 0 48 48" aria-hidden="true"><rect x="5" y="40" width="38" height="2.5" rx="1.2" fill="rgba(255,255,255,.6)"/>' + bars
           + '<path d="M6 30 L16 22 L24 27 L32 15 L42 10" fill="none" stroke="#F3C66B" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" opacity=".9"/></svg>')
    return (f'<a class="trk" id="trkCard" href="tools/gut-tracker/"><span class="trk-art">{art}</span><span class="trk-k"><span class="trk-new">{esc(FO["trNew"])}</span>{esc(FO["trK"])}</span>'
            f'<span class="trk-q">{esc(FO["trQ"])}<small>{esc(FO["trSub"])}</small></span><span class="trk-go">{esc(FO["trGo"])}</span></a>')

def diet_tab(lang):
    """The 'Diet charts' tab in Gut Health Daily: one card per chart page, plus the food diary. Relative links work from / and /hi/."""
    import diet_rules, diet_text_en, diet_text_hi
    T = diet_text_en if lang == "en" else diet_text_hi
    esc = lambda x: _html.escape(x, quote=True)
    intro = ("Indian diet charts for 12 gut and liver conditions, with veg and non-veg options. The food diary shows what your day is missing."
             if lang == "en" else "पेट और लिवर की 12 बीमारियों के लिए भारतीय डाइट चार्ट, शाकाहारी और नॉन-वेज विकल्पों के साथ। फ़ूड डायरी बताती है कि आज के खाने में क्या कम है।")
    allc = "All diet charts" if lang == "en" else "सभी डाइट चार्ट"
    note = ("These are general charts. Your own diet may need changes based on your reports, other conditions and medicines."
            if lang == "en" else "ये सामान्य चार्ट हैं। आपकी रिपोर्ट, दूसरी बीमारियों और दवाइयों के हिसाब से आपकी डाइट में बदलाव की ज़रूरत हो सकती है।")
    cards = "".join(f'<a href="diet-charts/{slug}/"><b>{esc(T.PAGES[slug]["name"])}</b><span>{esc(T.PAGES[slug]["blurb"])}</span></a>'
                    for slug, _, _ in diet_rules.PAGES)
    return (f'<div class="dtab-top"><p>{esc(intro)}</p><div class="btns"><a class="btn btn-solid btn-sm" href="diet-charts/#diary">{T.UI["diary_btn"]}</a>'
            f'<a class="btn btn-ghost btn-sm" href="diet-charts/">{allc}</a></div></div><div class="dtab">{cards}</div>'
            f'<p class="small" style="margin-top:16px">{esc(note)}</p>')

def link_lists(lang):
    """Static, crawlable links from the home page to every condition, procedure and answer page."""
    pre = "/" if lang == "en" else "/hi/"
    S = seo_en if lang == "en" else seo_hi
    esc = lambda x: _html.escape(x, quote=True)
    cond = "".join(f'<a href="{pre}conditions/{b["slug"]}/">{esc(x["seo"])}</a>' for b, x in zip(seo_en.CONDS, S.CONDS))
    proc = "".join(f'<a href="{pre}procedures/{b["slug"]}/">{esc(x["seo"])}</a>' for b, x in zip(seo_en.PROCS, S.PROCS))
    LIVER = {"is-fatty-liver-reversible","diet-in-jaundice","alcoholic-hepatitis","aclf-acute-on-chronic-liver-failure","high-sgpt-sgot-liver-function-test",
             "ascites-fluid-in-abdomen","hepatic-encephalopathy","liver-abscess","liver-cancer-screening","when-is-liver-transplant-needed","fatty-liver-grade-on-ultrasound"}
    TESTS = {"is-endoscopy-painful","fibroscan-test","capsule-endoscopy","stool-tests"}
    grp = lambda slug: "l" if slug in LIVER else "t" if slug in TESTS else "g"
    heads = {"l": "Liver", "g": "Stomach and bowel", "t": "Tests and procedures"} if lang == "en" else {"l": "लिवर", "g": "पेट और आँतें", "t": "जाँच और प्रोसीजर"}
    ans = ""
    for k in ("l", "g", "t"):
        items = "".join(f'<a href="{pre}answers/{b["slug"]}/">{esc(x["q"])}<span aria-hidden="true">→</span></a>' for b, x in zip(seo_en.ANSWERS, S.ANSWERS) if grp(b["slug"]) == k)
        if items: ans += f'<h3 class="ans-h">{heads[k]}</h3><div class="answers">{items}</div>'
    h_c = "Detailed guides to each condition" if lang == "en" else "हर बीमारी की पूरी जानकारी"
    h_p = "Detailed guides to each procedure" if lang == "en" else "हर प्रोसीजर की पूरी जानकारी"
    import guide_art
    feats = ""
    for g, x in zip(seo_en.SPECIAL, S.SPECIAL):
        art = guide_art.ART[g["slug"]]("").replace('role="img" aria-label=""', 'aria-hidden="true" focusable="false"')
        feats += (f'<a class="feature" href="{pre}guides/{g["slug"]}/"><div class="feature-art">{art}</div><div>'
                  f'<h3>{esc(x["name"])}</h3><p>{esc(x["blurb"])}</p><span class="btn btn-solid">{esc(x["feature_btn"])} <span aria-hidden="true">→</span></span></div></a>')
    x0 = S.SPECIAL[0]
    guides = (f'<section id="guides" class="alt">\n    <div class="wrap">\n      <div class="sec-head">\n        <p class="eyebrow">{esc(x0["feature_kick"])}</p>\n'
              f'        <h2>{esc(x0["section_h"])}</h2>\n      </div>\n      <div class="features">{feats}</div>\n    </div>\n  </section>')
    import build_pages
    season = build_pages.season_bar(lang)
    return {"<!--SEASONAL-->": season, "<!--GUIDES_SECTION-->": guides, "<!--COND_LINKS-->": f'<div class="guides"><h3>{h_c}</h3><div>{cond}</div></div>',
            "<!--PROC_LINKS-->": f'<div class="guides"><h3>{h_p}</h3><div>{proc}</div></div>',
            "<!--ANSWER_LINKS-->": ans,
            "/*FOOD*/": food_js(lang),
            "<!--WA_CHANNEL-->": build_pages.channel_html(lang),
            "<!--HOURS-->": ('<dl class="hours"><dt>Mon–Fri</dt><dd>6 pm – 8 pm</dd><dt>Sunday</dt><dd>9 am – 1 pm</dd><dt>Saturday</dt><dd>Closed</dd></dl>' if lang == "en"
                             else '<dl class="hours"><dt>सोम–शुक्र</dt><dd>शाम 6 – 8 बजे</dd><dt>रविवार</dt><dd>सुबह 9 – दोपहर 1 बजे</dd><dt>शनिवार</dt><dd>बंद</dd></dl>')
                            + f'<p><a style="color:var(--warm-on-ink)" href="{pre}gastroenterologist-in-gurgaon/">{local_pages.EN["more_local"] if lang == "en" else local_pages.HI["more_local"]} →</a></p>',
            "<!--ABOUT_LINK-->": f'<a class="about-more" href="{pre}about-dr-kshitij-lochab/">{local_pages.EN["more_about"] if lang == "en" else local_pages.HI["more_about"]} →</a>',
            "<!--FOOT_LINKS-->": f'<p class="foot-links"><a href="{pre}about-dr-kshitij-lochab/">{build_pages.FOOT_LINKS[lang][0]}</a> · <a href="{pre}gastroenterologist-in-gurgaon/">{build_pages.FOOT_LINKS[lang][1]}</a> · <a href="{pre}tools/gut-tracker/">{build_pages.FOOT_LINKS[lang][2]}</a> · <a href="{pre}diet-charts/">{build_pages.L[lang]['dietnav']}</a></p>' + build_pages.social_html(lang),
            "<!--TRACKER-->": ('<a class="ibs-track" href="tools/gut-tracker/">' + ("Track your symptoms privately →" if lang == "en" else "अपने लक्षण निजी रूप से ट्रैक करें →") + '</a>'),
            "<!--TRK_CARD-->": trk_card(lang),
            "<!--PREP_LINKS-->": __import__("prep_guides").home_links(lang),
            "<!--DIET_TAB-->": diet_tab(lang),
            "<!--DIET_FAB-->": build_pages.diet_fab(lang, "diet-charts/"),
            "<!--HUB-->": hub.hub_html(lang, hub.page_data(src[src.index("const ORGANS="):src.index("const esc=")] if lang == "en" else hindi.DATA_JS))}

for key, p in PAGES.items():
    s = src if key == "en" else hindi_source(src)
    for ph, block in link_lists(key).items():
        s = s.replace(ph, block)
    assert "<!--HUB-->" not in s
    top, body = split(s)
    fonts = ('<link rel="stylesheet" href="/assets/fonts/fonts-hi.css">\n'
             if key == "hi" else "")
    path = f"{OUT}/index.html" if key == "en" else f"{OUT}/hi/index.html"
    open(path, "w").write(head(p, fonts) + top + "\n</head>\n<body>" + body + "\n</body>\n</html>\n")

for f in ["tips.json", "ibs.json", "myths.json", "dr-lochab.jpg"]:
    shutil.copy(f, OUT)
shutil.copy("tips-hi.json", f"{OUT}/hi/tips.json")
shutil.copy("ibs-hi.json", f"{OUT}/hi/ibs.json")
shutil.copy("myths-hi.json", f"{OUT}/hi/myths.json")
shutil.copy("brand/logo-mark.png", f"{OUT}/logo-mark.png")
shutil.copy("brand/logo-mark.svg", f"{OUT}/logo-mark.svg")
mark = Image.open("brand/logo-mark.png").convert("RGBA")
mark.resize((96, 96), Image.LANCZOS).save(f"{OUT}/favicon.png", optimize=True)
apple = Image.new("RGBA", (180, 180), "#F3F7F6")
apple.paste(mark.resize((180, 180), Image.LANCZOS), (0, 0), mark.resize((180, 180), Image.LANCZOS))
apple.convert("RGB").save(f"{OUT}/apple-touch-icon.png")

# small round-crop source for the phone trust strip (shown at 56 px)
ph = Image.open("dr-lochab.jpg").convert("RGB")
side = ph.width
ph.crop((0, int(ph.height * 0.04), side, int(ph.height * 0.04) + side)).resize((112, 112), Image.LANCZOS).save(f"{OUT}/dr-lochab-thumb.jpg", quality=82)
# tighter face crop for the phone portrait card (shown at 96px, so 2x = 192px)
fw = int(ph.width * 0.62); fx = (ph.width - fw) // 2 + int(ph.width * 0.04)
ph.crop((fx, int(ph.height * 0.06), fx + fw, int(ph.height * 0.06) + fw)).resize((192, 192), Image.LANCZOS).save(f"{OUT}/dr-lochab-face.jpg", quality=82)

# web app manifest and icons ("Add to home screen")
for size in (192, 512):
    icon = Image.new("RGBA", (size, size), "#F3F7F6")
    m = mark.resize((size, size), Image.LANCZOS); icon.paste(m, (0, 0), m); icon.convert("RGB").save(f"{OUT}/icon-{size}.png")
    mk = Image.new("RGBA", (size, size), "#0B6A5E")          # maskable: mark inside the 80% safe zone
    inner = int(size * 0.62); mm = mark.resize((inner, inner), Image.LANCZOS)
    pad = Image.new("RGBA", (inner, inner), "#F3F7F6"); pad.paste(mm, (0, 0), mm)
    mk.paste(pad, ((size - inner) // 2, (size - inner) // 2)); mk.convert("RGB").save(f"{OUT}/icon-maskable-{size}.png")
json.dump({"name": "Dr. Kshitij Lochab, Gastroenterologist", "short_name": "Dr. Lochab", "start_url": "/", "scope": "/", "display": "standalone",
           "background_color": "#F3F7F6", "theme_color": "#0B6A5E", "lang": "en",
           "description": "Gut and liver health guides, diet charts, a private gut tracker and appointments with Dr. Kshitij Lochab in Gurugram.",
           "icons": [{"src": "/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/icon-512.png", "sizes": "512x512", "type": "image/png"},
                     {"src": "/icon-maskable-192.png", "sizes": "192x192", "type": "image/png", "purpose": "maskable"},
                     {"src": "/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
           "shortcuts": [{"name": "Diet charts", "url": "/diet-charts/"}, {"name": "Gut health tracker", "url": "/tools/gut-tracker/"}, {"name": "हिंदी", "url": "/hi/"}]},
          open(f"{OUT}/site.webmanifest", "w"), ensure_ascii=False, indent=1)

# self-hosted fonts
shutil.copytree("webfonts", f"{OUT}/assets/fonts", dirs_exist_ok=True)

og = Image.new("RGB", (1200, 630), "#F3F7F6")
lock = Image.open("brand/logo-horizontal.png").convert("RGBA")
lw = 640
lock = lock.resize((lw, int(lock.height * lw / lock.width)), Image.LANCZOS)
og.paste(lock, (60, (630 - lock.height) // 2 - 20), lock)
photo = Image.open("dr-lochab.jpg").convert("RGB")
og.paste(photo.resize((504, 630), Image.LANCZOS), (1200 - 504, 0))
og.save(f"{OUT}/og-image.jpg", quality=85)

open(f"{OUT}/CNAME", "w").write("drlochab.com\n")
open(f"{OUT}/robots.txt", "w").write("User-agent: *\nAllow: /\nSitemap: https://drlochab.com/sitemap.xml\n")
import build_pages
pairs = [("/", "/hi/")] + build_pages.build()
import not_found
open(f"{OUT}/404.html", "w").write(not_found.render(build_pages))
urls = "".join(
    f'  <url><loc>https://drlochab.com{u}</loc><changefreq>{"daily" if en == "/" else "monthly"}</changefreq>'
    f'<xhtml:link rel="alternate" hreflang="en" href="https://drlochab.com{en}"/>'
    f'<xhtml:link rel="alternate" hreflang="hi" href="https://drlochab.com{hi}"/></url>\n'
    for en, hi in pairs for u in (en, hi))
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
# Keep "→" on the same line as the word before it, everywhere.
for d, _, fs in os.walk(OUT):
    for f in fs:
        if f.endswith(".html"):
            fp = os.path.join(d, f); h = open(fp, encoding="utf-8").read()
            h2 = h.replace(" →", "\u00a0→").replace("← ", "←\u00a0")
            # Devanagari fonts load after the page has rendered (font-display: optional keeps the page from jumping)
            h2 = h2.replace('<link rel="stylesheet" href="/assets/fonts/fonts-hi.css">',
                            '<link rel="stylesheet" href="/assets/fonts/fonts-hi.css" media="print" onload="this.media=\'all\'"><noscript><link rel="stylesheet" href="/assets/fonts/fonts-hi.css"></noscript>')
            # the diet-guide data is only needed by extract.js (already run), not by visitors
            if f == "index.html" and os.path.relpath(d, OUT) in (".", "hi") and "const GUIDES=[" in h2:
                i = h2.index("const GUIDES=["); j = h2.index("];", i) + 3
                h2 = h2[:i] + h2[j:]
            if h2 != h: open(fp, "w", encoding="utf-8").write(h2)
print("pages:", len(pairs) * 2)
print("built:", sorted(os.listdir(OUT)), sorted(os.listdir(f"{OUT}/hi")))
