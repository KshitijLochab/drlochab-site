"""Builds the deployable drlochab.com folder (English at /, Hindi at /hi/) from lochab-gastro.html."""
import json, re, shutil, os
from PIL import Image
import hindi

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
        "postalCode": "122018",
        "addressCountry": "IN",
    },
}

PAGES = {
    "en": dict(
        lang="en", url="https://drlochab.com/", up="",
        title="Dr. Kshitij Lochab | Gastroenterologist in Gurugram",
        desc=("Dr. Kshitij Lochab, gastroenterologist in Gurugram. Plain-language guides to acidity, fatty liver, "
              "jaundice, IBS and more, daily diet tips, and appointments at Arcura Clinic, Sector 51."),
        og="Clear answers about your stomach, liver and digestion, with a new gut-health tip every day."),
    "hi": dict(
        lang="hi", url="https://drlochab.com/hi/", up="../",
        title="डॉ. क्षितिज लोचब | गुरुग्राम में पेट और लिवर रोग विशेषज्ञ",
        desc=("डॉ. क्षितिज लोचब, गुरुग्राम में गैस्ट्रोएंटेरोलॉजिस्ट। एसिडिटी, फैटी लिवर, पीलिया, IBS जैसी बीमारियों की "
              "आसान भाषा में जानकारी, रोज़ की डाइट सलाह, और आर्क्योरा क्लिनिक, सेक्टर 51 में अपॉइंटमेंट।"),
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
<link rel="icon" type="image/png" sizes="512x512" href="{up}favicon.png">
<link rel="apple-touch-icon" href="{up}apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{p['url']}">
<meta property="og:title" content="{p['title']}">
<meta property="og:description" content="{p['og']}">
<meta property="og:image" content="https://drlochab.com/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(dict(schema, url=p['url']), ensure_ascii=False)}</script>
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
    s = s.replace('--display:"Young Serif", Georgia,', '--display:"Young Serif","Tiro Devanagari Hindi", Georgia,', 1)
    s = s.replace('--body:"Figtree", system-ui,', '--body:"Figtree","Mukta", system-ui,', 1)
    s = s.replace("</style>", "*{letter-spacing:0!important}\nbody{line-height:1.7}\n</style>", 1)
    left = re.findall(r'"(Loading|Share on|Try this|Showing all|Copy |Book a)[^"]*"', s)
    if left:
        raise SystemExit(f"Hindi build stopped: untranslated interface text {left}")
    return s

import html as _html
import seo_en, seo_hi

def link_lists(lang):
    """Static, crawlable links from the home page to every condition, procedure and answer page."""
    pre = "/" if lang == "en" else "/hi/"
    S = seo_en if lang == "en" else seo_hi
    esc = lambda x: _html.escape(x, quote=True)
    cond = "".join(f'<a href="{pre}conditions/{b["slug"]}/">{esc(x["seo"])}</a>' for b, x in zip(seo_en.CONDS, S.CONDS))
    proc = "".join(f'<a href="{pre}procedures/{b["slug"]}/">{esc(x["seo"])}</a>' for b, x in zip(seo_en.PROCS, S.PROCS))
    ans = "".join(f'<a href="{pre}answers/{b["slug"]}/">{esc(x["q"])}<span aria-hidden="true">→</span></a>' for b, x in zip(seo_en.ANSWERS, S.ANSWERS))
    h_c = "Detailed guides to each condition" if lang == "en" else "हर बीमारी की पूरी जानकारी"
    h_p = "Detailed guides to each procedure" if lang == "en" else "हर प्रोसीजर की पूरी जानकारी"
    return {"<!--COND_LINKS-->": f'<div class="guides"><h3>{h_c}</h3><div>{cond}</div></div>',
            "<!--PROC_LINKS-->": f'<div class="guides"><h3>{h_p}</h3><div>{proc}</div></div>',
            "<!--ANSWER_LINKS-->": f'<div class="answers">{ans}</div>'}

for key, p in PAGES.items():
    s = src if key == "en" else hindi_source(src)
    for ph, block in link_lists(key).items():
        assert ph in s, ph
        s = s.replace(ph, block)
    top, body = split(s)
    fonts = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi&family=Mukta:wght@400;500;600;700&display=swap">\n'
             if key == "hi" else "")
    path = f"{OUT}/index.html" if key == "en" else f"{OUT}/hi/index.html"
    open(path, "w").write(head(p, fonts) + top + "\n</head>\n<body>" + body + "\n</body>\n</html>\n")

for f in ["tips.json", "ibs.json", "dr-lochab.jpg"]:
    shutil.copy(f, OUT)
shutil.copy("tips-hi.json", f"{OUT}/hi/tips.json")
shutil.copy("ibs-hi.json", f"{OUT}/hi/ibs.json")
shutil.copy("brand/logo-mark.png", f"{OUT}/logo-mark.png")
shutil.copy("brand/logo-mark.svg", f"{OUT}/logo-mark.svg")
mark = Image.open("brand/logo-mark.png").convert("RGBA")
mark.resize((512, 512), Image.LANCZOS).save(f"{OUT}/favicon.png")
apple = Image.new("RGBA", (180, 180), "#F3F7F6")
apple.paste(mark.resize((180, 180), Image.LANCZOS), (0, 0), mark.resize((180, 180), Image.LANCZOS))
apple.convert("RGB").save(f"{OUT}/apple-touch-icon.png")

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
urls = "".join(
    f'  <url><loc>https://drlochab.com{u}</loc><changefreq>{"daily" if en == "/" else "monthly"}</changefreq>'
    f'<xhtml:link rel="alternate" hreflang="en" href="https://drlochab.com{en}"/>'
    f'<xhtml:link rel="alternate" hreflang="hi" href="https://drlochab.com{hi}"/></url>\n'
    for en, hi in pairs for u in (en, hi))
open(f"{OUT}/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + urls + "</urlset>\n")
print("pages:", len(pairs) * 2)
print("built:", sorted(os.listdir(OUT)), sorted(os.listdir(f"{OUT}/hi")))
