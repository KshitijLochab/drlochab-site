"""Branded, bilingual 404 page for GitHub Pages (site/404.html). Asset paths are absolute because it is served at any missing URL."""

def render(bp):
    e = bp.e
    def col(lang, h, p, links):
        pre = bp.pre(lang)
        items = "".join(f'<a href="{pre}{u}">{e(t)} <span aria-hidden="true">→</span></a>' for u, t in links)
        return f'<section lang="{lang}"><h2>{h}</h2><p>{p}</p><div class="links">{items}</div></section>'
    en = col("en", "Where to next", "The link may be old or mistyped. These pages may help:",
             [("", "Home"), ("#conditions", "Conditions and symptoms"), ("diet-charts/", "Diet charts"), ("tools/gut-tracker/", "Gut health tracker"), ("#visit", "Book a consultation")])
    hi = col("hi", "आगे कहाँ जाएँ", "यह पेज नहीं मिला। लिंक पुराना या ग़लत हो सकता है। ये पेज मदद कर सकते हैं:",
             [("", "होम"), ("#conditions", "बीमारियाँ और लक्षण"), ("diet-charts/", "डाइट चार्ट"), ("tools/gut-tracker/", "पेट की सेहत का ट्रैकर"), ("#visit", "अपॉइंटमेंट लें")])
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Dr. Kshitij Lochab</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B6A5E">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/assets/fonts/fonts-hi.css">
<link rel="stylesheet" href="/assets/pages.css">
<style>.nf{{max-width:760px;padding-block:48px 64px}}.nf h1{{margin:10px 0 24px}}.nf section{{margin-top:28px}}</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="/"><img src="/logo-mark.svg" alt="" width="40" height="40"><span><span class="brand-name">Dr. Kshitij Lochab</span><span class="brand-sub">Gastroenterology · Liver · Endoscopy</span></span></a>
<nav aria-label="Main"><a class="btn btn-solid btn-sm" href="/#visit">Book a visit</a></nav></div></header>
<main class="wrap nf"><p class="eyebrow">404</p><h1>Page not found</h1><p class="lead" lang="hi">यह पेज नहीं मिला</p>{en}{hi}</main>
<footer><div class="wrap"><p>Dr. Kshitij Lochab · {bp.L["en"]["reg"]} · {bp.PHONE}</p></div></footer>
</body></html>
"""
