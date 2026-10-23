"""Diet charts section (19 Oct 2026): /diet-charts/ (index with the food diary) and one chart page per condition, in English and Hindi.
Rules and food tags: diet_rules.py. Text: diet_text_en.py / diet_text_hi.py. Foods: thali_foods.F (shared with the Thali meter).
The food diary runs entirely in the browser: data stays in localStorage on the visitor's phone, and the pages carry a
Content-Security-Policy with connect-src 'none', the same as the gut tracker, so nothing can be sent anywhere."""
import json
import diet_rules as R, diet_text_en as EN, diet_text_hi as HI, thali_foods

KIND = "diet-charts"
UPD = ("2026-10-19", "19 October 2026", "19 अक्टूबर 2026")
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
       "font-src 'self'; img-src 'self' data:; connect-src 'none'; form-action 'none'; base-uri 'self'")
CATS = {"en": {"g": "Roti, rice & breakfast", "d": "Dal & beans", "m": "Milk, curd & paneer", "n": "Eggs, chicken, fish & meat", "v": "Vegetables",
               "f": "Fruits & nuts", "k": "Tea, coffee & drinks", "o": "Oil, ghee & snacks", "s": "Sweets"},
        "hi": {"g": "रोटी, चावल, पोहा और अनाज", "d": "दाल और चने", "m": "दूध, दही और पनीर", "n": "अंडा, चिकन, मछली और मीट", "v": "सब्ज़ियाँ",
               "f": "फल और मेवे", "k": "चाय, कॉफ़ी और पेय", "o": "तेल, घी और नाश्ता", "s": "मिठाई"}}
# a different plate for each chart card: (main, side, accent) colours
PLATE = ["#E7B54A", "#4E7A2E", "#D8562A", "#9BC46A", "#C98A4A", "#F3B84A", "#2E9C86", "#E9733F", "#7FA6B5", "#B9781E", "#5B8F3A", "#F2C75C"]

def _check():
    R.check([x[1] for x in thali_foods.F])
    for k in EN.UI:
        assert k in HI.UI, k
    assert set(EN.UI) == set(HI.UI) and set(EN.PLAN_NAME) == set(HI.PLAN_NAME) == {p["key"] for p in R.PLANS}
    for slug, plans, _ in R.PAGES:
        a, b = EN.PAGES[slug], HI.PAGES[slug]
        for k in ("goals", "more", "less", "know", "faqs"):
            assert len(a[k]) == len(b[k]), (slug, k)
        assert set(a["care"]) == set(b["care"]) == set(EN.CARE_KEYS), slug
        assert set(a["charts"]) == set(b["charts"]) == set(plans), slug
        for pk in plans:
            assert len(a["charts"][pk]) == len(b["charts"][pk]) == len(R.SLOTS), (slug, pk)
            for x, y in zip(a["charts"][pk], b["charts"][pk]):
                assert len(x) == len(y) and [o.split("|")[0] for o in x] == [o.split("|")[0] for o in y], (slug, pk, x)
        assert ("phase" in a) == ("phase" in b) == (len(plans) > 1), slug
        assert ("stricture" in a) == ("stricture" in b), slug
        if "stricture" in a:
            for k in ("paras", "avoid", "help"):
                assert len(a["stricture"][k]) == len(b["stricture"][k]), (slug, k)
    assert set(EN.PAGES) == set(HI.PAGES) == {s for s, _, _ in R.PAGES}

def data_js(lang, U):
    foods = []
    for c, en, es, hi, hs, f, p, t, _ in thali_foods.F:
        g, fl, fit = R.TAGS[en].split("|")
        foods.append(dict(k=en, n=en if lang == "en" else hi, e=en, s=es if lang == "en" else hs, c=c, f=f, p=p, t=t, g=g, fl=fl, fit=fit))
    plans = [dict(key=p["key"], t=p["t"], good=p["good"], limit=p["limit"], avoid=p["avoid"], extra=p.get("extra", {}), why=p.get("why", "")) for p in R.PLANS]
    names = (EN if lang == "en" else HI).PLAN_NAME
    return json.dumps(dict(T=U, foods=foods, plans=plans, names=names, co=R.CO, slots=R.SLOTS, slotStart=R.SLOT_START, slotFit=R.SLOT_FIT,
                           cats=CATS[lang], order=[p["key"] for p in R.PLANS]), ensure_ascii=False)

def plate(i):
    a, b, c = PLATE[i % 12], PLATE[(i + 5) % 12], PLATE[(i + 9) % 12]
    return (f'<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="var(--accent-soft)"/><circle cx="32" cy="32" r="23" fill="var(--surface)" stroke="var(--line)" stroke-width="2"/>'
            f'<path d="M32 32 L32 12 A20 20 0 0 1 49.3 42 Z" fill="{a}"/><path d="M32 32 L49.3 42 A20 20 0 0 1 14.7 42 Z" fill="{b}"/><path d="M32 32 L14.7 42 A20 20 0 0 1 32 12 Z" fill="{c}"/>'
            f'<circle cx="32" cy="32" r="7" fill="var(--surface)"/></svg>')

def option(o, U, e):
    code, txt = o.split("|", 1)
    kind = {"V": "veg", "E": "egg", "N": "nonveg"}[code[0]]
    lab = U[kind]
    west = f' <span class="dc-west">{U["western"]}</span>' if code.endswith("W") else ""
    return f'<li><span class="dc-mark dc-{kind}" role="img" aria-label="{lab}" title="{lab}"></span><span>{e(txt)}{west}</span></li>'

def targets_html(pk, U, e):
    t = next(p for p in R.PLANS if p["key"] == pk)["t"]
    rows = []
    a, b = t["prot"]
    rows.append((U["m_prot"], U["t_prot_kg"].format(a=f"{a:g}", b=f"{b:g}") + f' ({U["t_prot"].format(a=round(a * 60), b=round(b * 60))}, 60 kg)'))
    rows.append((U["m_fib"], U["t_fib"].format(n=t["fib"]) if t["fib"] else U["t_fib_none"]))
    rows.append((U["m_fat"], U["t_fat"].format(n=t["fat"])))
    rows.append((U["m_veg"], U["t_veg"].format(n=t["veg"])))
    rows.append((U["m_fruit"], U["t_fruit"].format(a=t["fruit"][0], b=t["fruit"][1])))
    rows.append((U["m_water"], U["t_water"].format(a=t["water"][0], b=t["water"][1]) if t["water"] else U["t_water_doc"]))
    for k, lab in (("fried", "t_fried"), ("sugary", "t_sugary"), ("salty", "t_salty")):
        rows.append((U[lab], U["t_lim0"] if t[k] == 0 else U["t_lim"].format(n=t[k])))
    if t.get("meals"):
        rows.append(("", U["t_meals"].format(n=t["meals"])))
    if t.get("bed"):
        rows.append(("", U["t_bed"]))
    return '<dl class="dc-targets">' + "".join(f'<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>' if k else f'<div class="dc-wide"><dd>{e(v)}</dd></div>' for k, v in rows) + "</dl>"

def chart_html(rows, U, e):
    out = ""
    for s, opts in zip(R.SLOTS, rows):
        out += (f'<div class="dc-slot"><div class="dc-when"><b>{U["s_" + s]}</b><span>{U["st_" + s]}</span></div>'
                f'<ul class="dc-opts">' + "".join(option(o, U, e) for o in opts) + "</ul></div>")
    legend = (f'<p class="dc-legend"><span><span class="dc-mark dc-veg"></span>{U["veg"]}</span><span><span class="dc-mark dc-egg"></span>{U["egg"]}</span>'
              f'<span><span class="dc-mark dc-nonveg"></span>{U["nonveg"]}</span><span><span class="dc-west">{U["western"]}</span></span></p>')
    return legend + f'<div class="dc-chart">{out}</div>'

def diary_html(U, e, plan, plans):
    return (f'<section class="dd-wrap" id="diary" aria-labelledby="dd-h"><h2 id="dd-h">{e(U["diary_h"])}</h2><p>{e(U["diary_p"])}</p>'
            f'<p class="dd-priv">{e(U["privacy"])}</p><p class="dd-warn" id="ddNoStore" hidden>{e(U["nostore"])}</p>'
            f'<div class="dd" id="dd" data-plan="{plan}" data-plans="{",".join(plans)}"><noscript>{e(U["n_start"])}</noscript></div></section>')

def crumbs(lang, bp, name=None):
    p = bp.pre(lang); t = bp.L[lang]; U = (EN if lang == "en" else HI).UI
    mid = (f'<a href="{bp.url(lang, KIND, "")[:-1]}">{U["idx_eyebrow"]}</a><span>›</span><span aria-current="page">{bp.e(name)}</span>' if name
           else f'<span aria-current="page">{U["idx_eyebrow"]}</span>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{p}">{t["home"]}</a><span>›</span>{mid}</nav>'

def ld(lang, bp, path, name, desc, faqs, idx=False):
    p = bp.pre(lang); U = (EN if lang == "en" else HI).UI
    items = [{"@type": "ListItem", "position": 1, "name": bp.L[lang]["home"], "item": bp.SITE + p},
             {"@type": "ListItem", "position": 2, "name": U["idx_eyebrow"], "item": bp.SITE + p + KIND + "/"}]
    if not idx:
        items.append({"@type": "ListItem", "position": 3, "name": name, "item": bp.SITE + path})
    g = [{"@type": "MedicalWebPage", "name": name, "description": desc, "url": bp.SITE + path, "inLanguage": lang, "lastReviewed": UPD[0], "dateModified": UPD[0] + "T09:00:00+05:30",
          "author": bp.physician(lang), "reviewedBy": bp.physician(lang), "about": {"@type": "Diet", "name": name}},
         {"@type": "BreadcrumbList", "itemListElement": items}]
    if faqs:
        g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]})
    return {"@context": "https://schema.org", "@graph": g}

def page(lang, bp, head_args, body, plan_js=True):
    path, path_en, path_hi, title, desc, ldj = head_args
    U = (EN if lang == "en" else HI).UI
    h = bp.head(lang, title, desc, path_en, path_hi, ldj)
    h = h.replace("<head>", f'<head>\n<meta http-equiv="Content-Security-Policy" content="{CSP}">\n<meta name="referrer" content="no-referrer">', 1)
    h = h.replace("</head>", f"<style>{CSS}</style></head>", 1)
    return (h + bp.header(lang, path_hi if lang == "en" else path_en) + f'<main class="wrap grid"><article>{body}</article>{bp.aside(lang)}</main>'
            + f"<script>{JS.replace('__DATA__', data_js(lang, U))}</script>" + bp.footer(lang, diet=False))

def render_all(bp):
    """Yields (path, path_en, path_hi, html) for every diet chart page in both languages."""
    _check()
    for lang in ("en", "hi"):
        X = EN if lang == "en" else HI
        U = X.UI; e = bp.e
        # index
        path, pe, ph = bp.url(lang, KIND, "")[:-1], bp.url("en", KIND, "")[:-1], bp.url("hi", KIND, "")[:-1]
        cards = "".join(
            f'<a class="dc-card" href="{bp.url(lang, KIND, slug)}">{plate(i)}<span><b>{e(X.PAGES[slug]["name"])}</b><span>{e(X.PAGES[slug]["blurb"])}</span>'
            f'<span class="dc-go">{U["card_btn"]}</span></span></a>' for i, (slug, _, _) in enumerate(R.PAGES))
        body = (crumbs(lang, bp) + f'<p class="eyebrow">{U["idx_eyebrow"]}</p><h1>{e(U["idx_h1"])}</h1>{bp.byline(lang, UPD)}'
                + f'<p class="lead">{e(U["idx_lead"])}</p><p><a class="btn btn-solid btn-sm" href="#diary">{U["diary_btn"]}</a></p>'
                + f'<section><h2>{U["pick_h"]}</h2><div class="dc-cards">{cards}</div></section>'
                + diary_html(U, e, "gut", []) + f'<p class="dc-note">{e(U["note"])}</p>')
        yield path, pe, ph, page(lang, bp, (path, pe, ph, U["idx_title"], U["idx_desc"], ld(lang, bp, path, U["idx_h1"], U["idx_desc"], [], True)), body)
        # chart pages
        for i, (slug, plans, cond) in enumerate(R.PAGES):
            P = X.PAGES[slug]
            path, pe, ph = bp.url(lang, KIND, slug), bp.url("en", KIND, slug), bp.url("hi", KIND, slug)
            sec = []
            sec.append(f'<p class="lead">{e(P["lead"])}</p>')
            sec.append(f'<p class="dc-jump"><a class="btn btn-solid btn-sm" href="#diary">{U["track_cta"]} →</a><button type="button" class="btn btn-ghost btn-sm dc-print" onclick="print()">{U["print_btn"]}</button></p>')
            sec.append(f'<section><h2>{U["goals_h"]}</h2><ul class="dc-goals">' + "".join(f"<li>{e(g)}</li>" for g in P["goals"]) + "</ul></section>")
            if "stricture" in P:
                st = P["stricture"]
                sec.append(f'<section class="dc-str" id="stricture"><h2>{e(st["h"])}</h2>' + "".join(f"<p>{e(x)}</p>" for x in st["paras"])
                           + f'<div class="dc-two"><div class="gcol less"><h3>{e(st["avoid_h"])}</h3>{bp.ul(st["avoid"])}</div><div class="gcol more"><h3>{e(st["help_h"])}</h3>{bp.ul(st["help"])}</div></div>'
                           + f'<p class="dc-urgent">{e(st["urgent"])}</p></section>')
            for pk in plans:
                sub = f' <span class="dc-phase">{e(X.PLAN_NAME[pk].split(": ", 1)[-1])}</span>' if len(plans) > 1 else ""
                intro = f'<p class="small">{e(P["phase"][pk])}</p>' if len(plans) > 1 else ""
                sec.append(f'<section><h2>{U["chart_h"]}{sub}</h2>{intro}<p class="small">{e(U["chart_note"])}</p>' + chart_html(P["charts"][pk], U, e) + "</section>")
                sec.append(f'<section><h2>{U["targets_h"]}{sub}</h2>' + targets_html(pk, U, e) + "</section>")
            sec.append(f'<section><div class="guide"><div class="gcol more"><h3>{U["more"]}</h3>{bp.ul(P["more"])}</div>'
                       f'<div class="gcol less"><h3>{U["less"]}</h3>{bp.ul(P["less"])}</div><div class="gcol know"><h3>{U["know"]}</h3>{bp.ul(P["know"])}</div></div></section>')
            sec.append(f'<section><h2>{U["care_h"]}</h2><div class="dc-care">' + "".join(
                f'<div><h3>{U["co_" + k]}</h3><p>{e(P["care"][k])}</p></div>' for k in EN.CARE_KEYS) + "</div></section>")
            sec.append(diary_html(U, e, plans[0], plans))
            sec.append(bp.faq_html(lang, P["faqs"]))
            sec.append(f'<section class="see"><h2>{U["doc_h"]}</h2><p>{e(P["doc"])}</p></section>')
            rel = []
            if cond:
                k = [c["slug"] for c in bp.seo_en.CONDS].index(cond)
                rel.append((bp.url(lang, "conditions", cond), (bp.seo_en if lang == "en" else bp.seo_hi).CONDS[k]["seo"]))
            for a_slug, d_slug in bp.ANSWER_DIET.items():
                if d_slug == slug:
                    k = [a["slug"] for a in bp.seo_en.ANSWERS].index(a_slug)
                    rel.append((bp.url(lang, "answers", a_slug), (bp.seo_en if lang == "en" else bp.seo_hi).ANSWERS[k]["q"]))
            rel += [(bp.url(lang, KIND, s2), X.PAGES[s2]["name"]) for s2, _, _ in R.PAGES if s2 != slug]
            sec.append(f'<section><h2>{U["others_h"]}</h2>{bp.links(rel)}</section>')
            sec.append(f'<p class="dc-note">{e(U["note"])}</p>')
            body = (crumbs(lang, bp, P["name"]) + f'<p class="eyebrow">{U["eyebrow"]}</p><h1>{e(P["h1"])}</h1>{bp.byline(lang, UPD)}' + "".join(sec))
            yield path, pe, ph, page(lang, bp, (path, pe, ph, P["title"], P["desc"], ld(lang, bp, path, P["h1"], P["desc"], P["faqs"])), body)

CSS = r"""
.dc-jump{margin:4px 0 8px;display:flex;flex-wrap:wrap;gap:10px}
.dc-goals{list-style:none;padding:0;display:grid;gap:8px}
.dc-goals li{position:relative;padding:12px 14px 12px 44px;background:var(--surface);border:1px solid var(--line);border-radius:14px}
.dc-goals li::before{content:"";position:absolute;left:14px;top:14px;width:18px;height:18px;border-radius:50%;background:var(--accent);
 -webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='12' r='12'/%3E%3Cpath d='M6.5 12.5l3.5 3.5 7.5-8' stroke='white' stroke-width='2.6' fill='none' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/contain no-repeat}
.dc-goals li::after{content:"";position:absolute;left:18px;top:19px;width:10px;height:6px;border-left:2.6px solid var(--accent-ink);border-bottom:2.6px solid var(--accent-ink);transform:rotate(-45deg)}
.dc-legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.85rem;color:var(--muted);margin:4px 0 12px}
.dc-legend>span{display:inline-flex;align-items:center;gap:6px}
.dc-mark{flex:none;display:inline-block;width:14px;height:14px;border:2px solid currentColor;border-radius:3px;position:relative;margin-top:.3em}
.dc-mark::after{content:"";position:absolute;inset:2px;border-radius:50%;background:currentColor}
.dc-veg{color:#167A3E}.dc-nonveg{color:#9C3B1E}.dc-egg{color:#C9851F}
.dc-nonveg::after{border-radius:0;clip-path:polygon(50% 5%,95% 95%,5% 95%)}
.dc-west{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--accent);background:var(--accent-soft);border-radius:999px;padding:1px 8px;margin-left:4px;vertical-align:1px}
.dc-chart{display:grid;gap:10px}
.dc-slot{display:grid;grid-template-columns:150px 1fr;gap:14px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.dc-when b{display:block;font-family:var(--display);font-weight:400;font-size:1.05rem}
.dc-when span{font-size:.85rem;color:var(--muted)}
.dc-opts{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.dc-opts li{display:flex;gap:10px;align-items:flex-start;font-size:.97rem;line-height:1.45}
.dc-phase{font-family:var(--body);font-size:.8rem;font-weight:700;letter-spacing:.04em;color:var(--warm-text);background:var(--warm-soft);border-radius:999px;padding:3px 10px;vertical-align:middle;margin-left:6px}
.dc-targets{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin:0}
.dc-targets>div{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px}
.dc-targets dt{font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.dc-targets dd{margin:2px 0 0;font-weight:600}
.dc-targets .dc-wide{grid-column:1/-1;background:var(--accent-soft);border-color:transparent}
.dc-care{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px}
.dc-care>div{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px}
.dc-care h3{font-family:var(--body);font-size:.95rem;font-weight:700;margin-bottom:6px}
.dc-care p{font-size:.93rem;margin:0}
.dc-str{background:var(--surface);border:1px solid var(--line);border-left:5px solid var(--warm);border-radius:18px;padding:20px}
.dc-two{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px}.dc-two .gcol{background:var(--bg)}
.dc-urgent{margin:14px 0 0;padding:12px 14px;border-radius:12px;background:var(--urgent-soft);color:var(--ink);font-weight:600}
@media (max-width:640px){.dc-two{grid-template-columns:1fr}}
.dc-note{font-size:.85rem;color:var(--muted);margin-top:28px}
.dc-cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:12px}
.dc-card{display:grid;grid-template-columns:56px 1fr;gap:14px;align-items:start;padding:16px;background:var(--surface);border:1px solid var(--line);border-radius:18px;text-decoration:none;color:var(--ink)}
.dc-card:hover{border-color:var(--accent);box-shadow:0 4px 14px rgba(13,116,102,.08)}
.dc-card svg{width:56px;height:56px}
.dc-card b{display:block;font-family:var(--display);font-weight:400;font-size:1.12rem;line-height:1.25}
.dc-card span span{display:block;font-size:.88rem;color:var(--muted);line-height:1.45;margin-top:3px}
.dc-card .dc-go{color:var(--accent);font-weight:600;margin-top:6px}
@media (max-width:560px){.dc-slot{grid-template-columns:1fr;gap:8px}}

/* food diary */
.dd-wrap{margin-top:40px;padding:22px;border-radius:24px;background:var(--accent-soft);scroll-margin-top:90px}
.dd-wrap>h2{margin-bottom:6px}
.dd-priv{font-size:.88rem;color:var(--muted);display:flex;gap:8px;align-items:flex-start}
.dd-priv::before{content:"";flex:none;width:16px;height:16px;margin-top:.25em;background:var(--accent);-webkit-mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='4' y='10' width='16' height='11' rx='2'/%3E%3Cpath d='M8 10V7a4 4 0 0 1 8 0v3' fill='none' stroke='black' stroke-width='2.4'/%3E%3C/svg%3E") center/contain no-repeat;mask:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect x='4' y='10' width='16' height='11' rx='2'/%3E%3Cpath d='M8 10V7a4 4 0 0 1 8 0v3' fill='none' stroke='black' stroke-width='2.4'/%3E%3C/svg%3E") center/contain no-repeat}
.dd-warn{background:var(--warm-soft);color:var(--warm-text);border-radius:12px;padding:10px 14px;font-size:.9rem}
.dd{display:grid;gap:14px}
.dd-card{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:16px}
.dd-card>h3{font-family:var(--body);font-size:.78rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.dd-set summary{cursor:pointer;font-weight:700;list-style:none;display:flex;justify-content:space-between;gap:10px;align-items:center}
.dd-set summary::-webkit-details-marker{display:none}
.dd-set summary span{font-weight:500;color:var(--muted);font-size:.9rem;text-align:right}
.dd-set summary::after{content:"";flex:none;width:9px;height:9px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(45deg);margin-top:-4px}
.dd-set[open] summary::after{transform:rotate(-135deg);margin-top:4px}
.dd-f{display:grid;gap:6px;margin-top:14px}
.dd-f>label,.dd-f>p{font-size:.78rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);margin:0}
.dd select,.dd input[type=number],.dd-sheet input[type=search]{font:inherit;font-size:1rem;color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;width:100%}
.dd-seg,.dd-chips{display:flex;flex-wrap:wrap;gap:8px}
.dd .chip,.dd-sheet .chip{font-family:var(--body);font-size:.88rem;font-weight:600;padding:8px 13px;border-radius:999px;border:1.5px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.dd .chip[aria-pressed="true"],.dd-sheet .chip[aria-pressed="true"]{background:var(--accent);border-color:var(--accent);color:var(--accent-ink)}
.dd-m{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.dd-mt{background:var(--bg);border-radius:14px;padding:10px 12px;min-width:0}
.dd-mt b{display:block;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.dd-mt strong{display:block;font-size:1.35rem;font-family:var(--display);font-weight:400;margin:2px 0}
.dd-mt strong small{font-family:var(--body);font-size:.8rem;color:var(--muted)}
.dd-bar{height:7px;border-radius:99px;background:var(--line);overflow:hidden}
.dd-bar i{display:block;height:100%;border-radius:99px;background:var(--warm);transition:width .5s}
.dd-mt.ok .dd-bar i{background:#2E9C86}.dd-mt.over .dd-bar i{background:var(--urgent)}
.dd-mt span{display:block;font-size:.75rem;color:var(--muted);margin-top:5px;line-height:1.3}
.dd-w{display:flex;align-items:center;gap:8px;margin-top:2px}.dd-w strong{display:flex;align-items:baseline;gap:4px;white-space:nowrap}
.dd-w button{width:30px;height:30px;border-radius:50%;border:1.5px solid var(--line);background:var(--surface);color:var(--ink);font-size:1.1rem;font-weight:700;cursor:pointer;line-height:1}
.dd-cnt{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
.dd-cnt span{font-size:.8rem;font-weight:600;padding:4px 10px;border-radius:999px;background:var(--bg)}
.dd-cnt span.over{background:var(--urgent-soft);color:var(--urgent)}
.dd-msgs{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.dd-msgs li{padding:9px 12px 9px 34px;border-radius:12px;background:var(--bg);font-size:.94rem;position:relative;line-height:1.45}
.dd-msgs li::before{content:"";position:absolute;left:12px;top:15px;width:10px;height:10px;border-radius:50%;background:var(--warm)}
.dd-msgs li.bad{background:var(--urgent-soft)}.dd-msgs li.bad::before{background:var(--urgent)}
.dd-msgs li.ok{background:var(--accent-soft)}.dd-msgs li.ok::before{background:#2E9C86}
.dd-msgs li.i::before{background:var(--muted)}
.dd-sg{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.dd-sg li{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;padding:10px 12px;border-radius:12px;background:var(--bg)}
.dd-sg small{display:block;color:var(--muted);font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.dd-sg em{display:block;font-style:normal;font-size:.85rem;color:var(--muted)}
.dd-add1{border:none;background:var(--accent);color:var(--accent-ink);font-weight:700;border-radius:999px;padding:8px 14px;cursor:pointer;font-size:.9rem}
.dd-slots{display:grid;gap:10px}
.dd-slot{border:1px solid var(--line);border-radius:14px;padding:12px}
.dd-slot.now{border-color:var(--accent);box-shadow:0 0 0 2px var(--accent-soft)}
.dd-sh{display:flex;justify-content:space-between;align-items:center;gap:10px}
.dd-sh b{font-family:var(--display);font-weight:400;font-size:1.05rem}
.dd-sh span{font-size:.8rem;color:var(--muted);margin-left:6px}
.dd-sh button{border:1.5px solid var(--accent);background:transparent;color:var(--accent);font-weight:700;border-radius:999px;padding:6px 12px;cursor:pointer;font-size:.85rem;white-space:nowrap}
.dd-items{display:flex;flex-wrap:wrap;gap:6px;margin-top:8px}
.dd-it{display:inline-flex;align-items:center;gap:6px;font-size:.88rem;padding:5px 6px 5px 11px;border-radius:999px;background:var(--bg);border:1.5px solid transparent}
.dd-it.st-good{border-color:rgba(46,156,134,.45)}.dd-it.st-limit{border-color:var(--warm)}.dd-it.st-avoid{border-color:var(--urgent)}
.dd-it button{width:24px;height:24px;border-radius:50%;border:none;background:var(--line);color:var(--ink);font-weight:700;cursor:pointer;line-height:1}
.dd-foot{display:flex;flex-wrap:wrap;gap:10px;align-items:center;justify-content:space-between}
.dd-foot .chip.warn{border-color:var(--urgent);color:var(--urgent)}
.dd-sheet{position:fixed;inset:0;z-index:60;display:flex;align-items:flex-end;justify-content:center;background:rgba(6,20,18,.45)}
.dd-sheet[hidden]{display:none}
.dd-panel{background:var(--surface);color:var(--ink);width:100%;max-width:720px;max-height:88vh;border-radius:22px 22px 0 0;display:flex;flex-direction:column;box-shadow:0 -10px 30px rgba(0,0,0,.2)}
.dd-ph{padding:14px 16px 10px;border-bottom:1px solid var(--line);display:grid;gap:10px}
.dd-ph-top{display:flex;justify-content:space-between;align-items:center;gap:10px}
.dd-ph-top b{font-size:1rem}
.dd-ph .btn{padding:8px 16px}
.dd-slotpick,.dd-catpick{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
.dd-slotpick::-webkit-scrollbar,.dd-catpick::-webkit-scrollbar{display:none}
.dd-slotpick .chip,.dd-catpick .chip{flex:none;font-size:.8rem;padding:6px 11px}
.dd-list{overflow-y:auto;padding:8px 12px 18px;display:grid;gap:6px;align-content:start}
.dd-row{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;width:100%;text-align:left;font:inherit;color:inherit;background:var(--bg);border:1.5px solid transparent;border-radius:12px;padding:10px 12px;cursor:pointer}
.dd-row:hover{border-color:var(--accent)}
.dd-row b{display:block;font-size:.95rem;font-weight:600}
.dd-row small{display:block;font-size:.8rem;color:var(--muted)}
.dd-row i{font-style:normal;font-size:.78rem;color:var(--muted)}
.dd-bdg{font-size:.72rem;font-weight:700;padding:3px 9px;border-radius:999px;white-space:nowrap}
.dd-bdg.good{background:var(--accent-soft);color:var(--accent)}.dd-bdg.limit{background:var(--warm-soft);color:var(--warm-text)}.dd-bdg.avoid{background:var(--urgent-soft);color:var(--urgent)}
.dd-row .dd-n{display:inline-block;min-width:22px;text-align:center;font-size:.78rem;font-weight:700;background:var(--accent);color:var(--accent-ink);border-radius:99px;padding:1px 6px;margin-left:6px}
.dd-toast{position:fixed;left:50%;bottom:calc(84px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:70;background:var(--ink);color:var(--bg);padding:9px 16px;border-radius:999px;font-size:.9rem;font-weight:600;opacity:0;transition:opacity .2s;pointer-events:none}
.dd-toast.on{opacity:1}
@media (max-width:560px){.dd-wrap{margin-inline:-6px;padding:16px 12px}.dd-m{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (prefers-reduced-motion:reduce){.dd-bar i{transition:none}}
"""

JS = r"""(function(){
const D=__DATA__, T=D.T, F=D.foods, P={}; D.plans.forEach(p=>P[p.key]=p);
const BY={}; F.forEach(f=>BY[f.k]=f);
const root=document.getElementById("dd"); if(!root)return;
const esc=s=>String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/"/g,"&quot;");
const fmt=(s,o)=>{if("n" in o){o.s=o.n==1?"":"s";o.es=o.n==1?"":"es";}return s.replace(/\{(\w+)\}/g,(m,k)=>k in o?o[k]:m);};
const r1=n=>String(Math.round(n*10)/10);
let canStore=true; try{localStorage.setItem("dd-t","1");localStorage.removeItem("dd-t");}catch(e){canStore=false;}
if(!canStore)document.getElementById("ddNoStore").hidden=false;
const ls={get(k,d){if(!canStore)return d;try{const v=localStorage.getItem(k);return v?JSON.parse(v):d;}catch(e){return d;}},set(k,v){if(!canStore)return;try{localStorage.setItem(k,JSON.stringify(v));}catch(e){}}};
const now=new Date(), pad=n=>String(n).padStart(2,"0"), TODAY=`${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())}`;
if(canStore){try{for(let i=localStorage.length-1;i>=0;i--){const k=localStorage.key(i);if(k&&k.indexOf("dd-day-")===0&&(now-new Date(k.slice(7)))/864e5>30)localStorage.removeItem(k);}}catch(e){}}
let S=Object.assign({plan:"gut",diet:"n",co:[],kg:""},ls.get("dd-set",{}));
const pagePlans=(root.dataset.plans||"").split(",").filter(Boolean);
if(pagePlans.length&&pagePlans.indexOf(S.plan)<0)S.plan=root.dataset.plan;
if(!P[S.plan])S.plan="gut";
let DAY=ls.get("dd-day-"+TODAY,{s:{},w:0});
const save=()=>{ls.set("dd-set",S);ls.set("dd-day-"+TODAY,DAY);};
const hourNow=()=>{const d=new Date();return d.getHours()+d.getMinutes()/60;};
const curSlot=()=>{const h=hourNow();let c=D.slots[0];D.slots.forEach(s=>{if(h>=D.slotStart[s])c=s;});return h<4?"bed":c;};
const dietOK=f=>S.diet==="n"||(S.diet==="e"?f.g!=="M":(f.g!=="M"&&f.g!=="E"));
const match=(r,f)=>r[0]==="@"?f.fl.indexOf(r[1])>=0:r[0]==="#"?f.g===r[1]:r===f.k;
const why=(r,f)=>{if(r[0]==="@")return T["r_"+r[1]];if(r[0]==="#")return T["r_"+r[1]]||T.r_name;for(const c of f.fl)if(T["r_"+c])return T["r_"+c];return T["r_"+f.g]||T.r_name;};
function status(f){const p=P[S.plan],av=p.avoid.slice(),li=p.limit.slice();
  S.co.forEach(c=>{const r=D.co[c];if(r){(r.avoid||[]).forEach(x=>av.push(x));(r.limit||[]).forEach(x=>li.push(x));}});
  for(const r of av)if(match(r,f))return["avoid",(p.why&&p.avoid.indexOf(r)>=0)?T["r_"+p.why]:why(r,f)];
  for(const r of li)if(match(r,f))return["limit",why(r,f)];
  return p.good.indexOf(f.k)>=0?["good",""]:["",""];}
function targets(){const p=P[S.plan],t=p.t,co=S.co,kg=+S.kg>20&&+S.kg<250?+S.kg:60;let pr=t.prot.slice();
  if(co.indexOf("old")>=0)pr=[Math.max(pr[0],1.0),Math.max(pr[1],1.2)];
  let lo=Math.round(pr[0]*kg),hi=Math.round(pr[1]*kg);if(co.indexOf("preg")>=0){lo+=10;hi+=10;}
  const kid=co.indexOf("kidney")>=0,fr=t.fruit.slice();if(co.indexOf("diabetes")>=0)fr[1]=Math.min(fr[1],3);
  const ex=Object.assign({},p.extra||{});if(co.indexOf("lactose")>=0)ex.l=Math.min(ex.l===undefined?1:ex.l,1);if(co.indexOf("preg")>=0)ex.c=Math.min(ex.c===undefined?2:ex.c,2);
  return{lo:kid?null:lo,hi:kid?null:hi,cap:kid?Math.round(.8*kg):null,kg:kg,kgSet:+S.kg>20,fib:t.fib,fat:t.fat,veg:t.veg,fruit:fr,water:(kid||!t.water)?null:t.water,
    lim:{f:t.fried,u:(co.indexOf("diabetes")>=0?0:t.sugary),s:((co.indexOf("bp")>=0||kid)?0:t.salty)},ex:ex,meals:t.meals||0,bed:!!t.bed};}
function totals(){const o={p:0,f:0,t:0,veg:0,fruit:0,cnt:{},items:[],filled:0};
  D.slots.forEach(s=>{const m=DAY.s[s]||{};let any=false;Object.keys(m).forEach(k=>{const n=m[k],f=BY[k];if(!f||!n)return;any=true;
    o.p+=f.p*n;o.f+=f.f*n;o.t+=f.t*n;if(f.g==="V")o.veg+=n;if(f.g==="F")o.fruit+=n;for(const c of f.fl)o.cnt[c]=(o.cnt[c]||0)+n;o.items.push([s,f,n]);});if(any)o.filled++;});
  return o;}
function add(slot,k,d){DAY.s[slot]=DAY.s[slot]||{};const n=(DAY.s[slot][k]||0)+d;if(n<=0)delete DAY.s[slot][k];else DAY.s[slot][k]=n;save();}
/* settings */
function settingsHtml(){const t=T,o=D.order.map(k=>`<option value="${k}"${k===S.plan?" selected":""}>${esc(D.names[k])}</option>`).join("");
  const seg=["v","e","n"].map(d=>`<button type="button" class="chip" data-diet="${d}" aria-pressed="${S.diet===d}">${t["d_"+d]}</button>`).join("");
  const co=["diabetes","bp","kidney","preg","lactose","old"].map(c=>`<button type="button" class="chip" data-co="${c}" aria-pressed="${S.co.indexOf(c)>=0}">${t["co_"+c]}</button>`).join("");
  const sum=esc(D.names[S.plan])+" · "+t["d_"+S.diet]+(S.co.length?" · +"+S.co.length:"");
  return `<details class="dd-card dd-set"${ls.get("dd-set",null)?"":" open"}><summary>${t.set_h}<span>${sum}</span></summary>
   <div class="dd-f"><label for="ddPlan">${t.set_plan}</label><select id="ddPlan">${o}</select></div>
   <div class="dd-f"><p>${t.set_diet}</p><div class="dd-seg">${seg}</div></div>
   <div class="dd-f"><p>${t.set_co}</p><div class="dd-chips">${co}</div></div>
   <div class="dd-f"><label for="ddKg">${t.set_kg}</label><input id="ddKg" type="number" inputmode="decimal" min="25" max="200" value="${esc(S.kg)}" placeholder="60"></div></details>`;}
function meter(cls,label,val,unit,pct,sub){return `<div class="dd-mt ${cls}"><b>${label}</b><strong>${val}<small> ${unit}</small></strong><div class="dd-bar"><i style="width:${Math.max(0,Math.min(100,pct))}%"></i></div><span>${sub}</span></div>`;}
function summaryHtml(tg,o){const t=T;let h="";
  if(tg.lo)h+=meter(o.p>=tg.lo?"ok":"",t.m_prot,r1(o.p),t.u_g,o.p/tg.hi*100,fmt(t.t_prot,{a:tg.lo,b:tg.hi}));
  else h+=meter("",t.m_prot,r1(o.p),t.u_g,tg.cap?o.p/tg.cap*100:0,t.t_prot_doc);
  h+=tg.fib?meter(o.f>=tg.fib?"ok":"",t.m_fib,r1(o.f),t.u_g,o.f/tg.fib*100,fmt(t.t_fib,{n:tg.fib})):meter("",t.m_fib,r1(o.f),t.u_g,0,t.t_fib_none);
  h+=meter(o.t>tg.fat?"over":"ok",t.m_fat,r1(o.t),t.u_g,o.t/tg.fat*100,fmt(t.t_fat,{n:tg.fat}));
  h+=meter(o.veg>=tg.veg?"ok":"",t.m_veg,o.veg,o.veg==1?t.u_kat1:t.u_kat,o.veg/tg.veg*100,fmt(t.t_veg,{n:tg.veg}));
  h+=meter(o.fruit>tg.fruit[1]?"over":o.fruit>=tg.fruit[0]?"ok":"",t.m_fruit,o.fruit,o.fruit==1?t.u_serv1:t.u_serv,o.fruit/tg.fruit[1]*100,fmt(t.t_fruit,{a:tg.fruit[0],b:tg.fruit[1]}));
  const w=DAY.w||0;
  h+=`<div class="dd-mt${tg.water&&w>=tg.water[0]?" ok":""}"><b>${t.m_water}</b><div class="dd-w"><button type="button" data-w="-1" aria-label="${t.w_sub}">−</button><strong>${w}<small> ${w==1?t.u_glass1:t.u_glass}</small></strong><button type="button" data-w="1" aria-label="${t.w_add}">+</button></div>`
   +(tg.water?`<div class="dd-bar"><i style="width:${Math.min(100,w/tg.water[1]*100)}%"></i></div><span>${fmt(t.t_water,{a:tg.water[0],b:tg.water[1]})}</span>`:`<span>${t.t_water_doc}</span>`)+`</div>`;
  const cn=[["f",tg.lim.f,t.c_f],["u",tg.lim.u,t.c_u],["s",tg.lim.s,t.c_s]];Object.keys(tg.ex).forEach(k=>cn.push([k,tg.ex[k],t["c_"+k]]));
  const chips=cn.map(([k,l,lab])=>{const n=o.cnt[k]||0;return `<span class="${n>l?"over":""}">${lab}: ${n}/${l}</span>`;}).join("");
  const note=tg.lo&&!tg.kgSet?`<p class="small" style="margin:10px 0 0">${fmt(t.based,{kg:tg.kg})}</p>`:"";
  return `<div class="dd-card"><div class="dd-m">${h}</div><div class="dd-cnt">${chips}</div>${note}</div>`;}
function needs(tg,o){const t=T,out=[],h=hourNow();
  if(!o.items.length){out.push(["i",t.n_start]);return out;}
  const seen={};o.items.forEach(([s,f])=>{const st=status(f);if(st[0]==="avoid"&&!seen[f.k]){seen[f.k]=1;out.push(["bad",fmt(t.n_avoid,{food:f.n,reason:st[1]})]);}});
  if(o.t>tg.fat)out.push(["bad",fmt(t.n_fat,{n:tg.fat})]);
  const cn=[["f",tg.lim.f,t.c_f],["u",tg.lim.u,t.c_u],["s",tg.lim.s,t.c_s]];Object.keys(tg.ex).forEach(k=>cn.push([k,tg.ex[k],t["c_"+k]]));
  cn.forEach(([k,l,lab])=>{const n=o.cnt[k]||0;if(l===0&&n&&o.items.every(([s,f])=>f.fl.indexOf(k)<0||seen[f.k]))return;if(n>l)out.push(["bad",l===0?fmt(t.n_cnt0,{label:lab}):fmt(t.n_cnt,{label:lab,n:n,m:l})]);});
  if(tg.cap&&o.p>tg.cap)out.push(["warn",t.n_kidney]);
  if(tg.lo&&o.p<tg.lo)out.push(["warn",fmt(t.n_prot,{n:Math.round(tg.lo-o.p),list:t["n_prot_"+S.diet]})]);
  if(tg.fib&&o.f<tg.fib)out.push(["warn",fmt(t.n_fib,{n:Math.round(tg.fib-o.f)})]);
  if(o.veg<tg.veg)out.push(["warn",fmt(t.n_veg,{n:tg.veg-o.veg})]);
  if(o.fruit<tg.fruit[0])out.push(["warn",fmt(t.n_fruit,{n:tg.fruit[0]-o.fruit})]);
  if(o.fruit>tg.fruit[1])out.push(["bad",fmt(t.n_fruit_hi,{n:o.fruit,m:tg.fruit[1]})]);
  if(tg.water&&(DAY.w||0)<tg.water[0])out.push(["warn",fmt(t.n_water,{n:tg.water[0]-(DAY.w||0)})]);
  const empty=s=>!DAY.s[s]||!Object.keys(DAY.s[s]).length;
  if(tg.meals&&h>=11&&empty("early")&&empty("bf"))out.push(["warn",t.n_skip]);
  if(tg.meals&&h>=18&&o.filled<tg.meals-1)out.push(["warn",fmt(t.n_meals,{n:tg.meals})]);
  if(tg.bed&&h>=17&&empty("bed"))out.push(["warn",t.n_bed]);
  if(!out.some(x=>x[0]!=="i"))out.push(["ok",t.n_ok]);
  return out;}
function suggest(tg,o){const order=D.slots,cur=curSlot(),i0=order.indexOf(cur);
  const empty=s=>!DAY.s[s]||!Object.keys(DAY.s[s]).length;
  let rest=order.slice(i0).filter(s=>empty(s));if(cur==="bed")rest=["bed"].filter(empty);
  if(!tg.bed)rest=rest.filter(s=>s!=="bed"||hourNow()>=21);
  const nP=tg.lo?Math.max(0,tg.lo-o.p):0,nF=tg.fib?Math.max(0,tg.fib-o.f):0,nV=Math.max(0,tg.veg-o.veg),nFr=Math.max(0,tg.fruit[0]-o.fruit),fatLeft=tg.fat-o.t;
  if(!nP&&!nF&&!nV&&!nFr&&!(tg.bed&&rest.indexOf("bed")>=0))return null;
  const used={},out=[];
  const score=f=>(nP?Math.min(f.p,nP)/Math.max(nP,12)*3:0)+(nF?Math.min(f.f,nF)/Math.max(nF,6)*3:0)+(nV&&f.g==="V"?2:0)+(nFr&&f.g==="F"?2:0)-(f.t>fatLeft?3:f.t/25);
  for(const s of rest){if(out.length>=5)break;const fit=D.slotFit[s];
    const c=F.filter(f=>dietOK(f)&&f.fit.indexOf(fit)>=0&&status(f)[0]==="good"&&!used[f.k]).sort((a,b)=>score(b)-score(a));
    const pk=[],prim=c.filter(f=>f.g!=="V"&&f.g!=="F");
    if((nP||nF)&&prim[0])pk.push(prim[0]);
    if(fit==="m"&&nV){const v=c.find(f=>f.g==="V");if(v)pk.push(v);}
    if(fit!=="m"&&nFr){const v=c.find(f=>f.g==="F");if(v)pk.push(v);}
    if(!pk.length&&c[0])pk.push(c[0]);
    pk.forEach(f=>{used[f.k]=1;out.push([s,f]);});}
  return out;}
function adviceHtml(tg,o){const t=T;const ms=needs(tg,o).map(([c,m])=>`<li class="${c}">${esc(m)}</li>`).join("");
  const sg=suggest(tg,o);let sh="";
  if(o.items.length){
    if(sg===null)sh=`<p style="margin:0">${t.sg_none}</p>`;
    else if(sg.length)sh=`<ul class="dd-sg">`+sg.map(([s,f])=>{const r=f.g==="V"?t.sg_veg:f.g==="F"?t.sg_fruit:fmt(t.sg_adds,{p:r1(f.p),f:r1(f.f)});
      return `<li><span><small>${t["s_"+s]}</small>${esc(f.n)} <em>${esc(f.s)} · ${esc(r)}</em></span><button type="button" class="dd-add1" data-s="${s}" data-k="${esc(f.k)}" aria-label="${esc(fmt(t.added,{food:f.n}))}">+ ${t.add}</button></li>`;}).join("")+`</ul>`;}
  return `<div class="dd-card"><h3>${t.need_h}</h3><ul class="dd-msgs">${ms}</ul></div>`+(sh?`<div class="dd-card"><h3>${t.rest_h}</h3>${sh}</div>`:"");}
function slotsHtml(){const t=T,cur=curSlot();
  return `<div class="dd-card"><div class="dd-slots">`+D.slots.map(s=>{const m=DAY.s[s]||{};
    const it=Object.keys(m).filter(k=>BY[k]&&m[k]).map(k=>{const f=BY[k],st=status(f)[0];return `<span class="dd-it st-${st||"none"}">${esc(f.n)}${m[k]>1?" ×"+m[k]:""}<button type="button" data-rm="${s}" data-k="${esc(k)}" aria-label="${esc(t.remove)}: ${esc(f.n)}">−</button></span>`;}).join("");
    return `<div class="dd-slot${s===cur?" now":""}"><div class="dd-sh"><div><b>${t["s_"+s]}</b><span>${t["st_"+s]}</span></div><button type="button" data-open="${s}">+ ${t.add}</button></div>${it?`<div class="dd-items">${it}</div>`:""}</div>`;}).join("")+`</div></div>`;}
function footHtml(){return `<div class="dd-foot"><button type="button" class="chip" id="ddClear">${T.clear}</button></div>`;}
function render(keepOpen){const tg=targets(),o=totals();
  root.innerHTML=settingsHtml()+summaryHtml(tg,o)+adviceHtml(tg,o)+slotsHtml()+footHtml();
  if(keepOpen){const d=root.querySelector(".dd-set");if(d)d.open=true;}}
/* picker sheet */
const sheet=document.createElement("div");sheet.className="dd-sheet";sheet.hidden=true;
sheet.innerHTML=`<div class="dd-panel" role="dialog" aria-modal="true" aria-labelledby="ddSheetH"><div class="dd-ph"><div class="dd-ph-top"><b id="ddSheetH"></b><button type="button" class="btn btn-solid" id="ddDone">${T.done}</button></div>
 <div class="dd-slotpick" id="ddSlotPick"></div><input type="search" id="ddSearch" placeholder="${esc(T.search)}" aria-label="${esc(T.search)}" autocomplete="off"><div class="dd-catpick" id="ddCatPick"></div></div><div class="dd-list" id="ddList"></div></div>`;
document.body.appendChild(sheet);
const toast=document.createElement("div");toast.className="dd-toast";toast.setAttribute("role","status");toast.setAttribute("aria-live","polite");document.body.appendChild(toast);
let tt=null;const say=m=>{toast.textContent=m;toast.classList.add("on");clearTimeout(tt);tt=setTimeout(()=>toast.classList.remove("on"),1400);};
let PK={slot:"bf",cat:"",q:"",opener:null};
function listHtml(){const q=PK.q.trim().toLowerCase(),m=DAY.s[PK.slot]||{};
  const rows=F.filter(f=>dietOK(f)&&(!PK.cat||f.c===PK.cat)&&(!q||f.n.toLowerCase().indexOf(q)>=0||f.e.toLowerCase().indexOf(q)>=0));
  const rank={good:0,"":1,limit:2,avoid:3};
  rows.sort((a,b)=>q?0:(rank[status(a)[0]]-rank[status(b)[0]]));
  return rows.map(f=>{const st=status(f),b=st[0]?`<span class="dd-bdg ${st[0]}">${T[st[0]]}</span>`:"";const n=m[f.k]?`<span class="dd-n">${m[f.k]}</span>`:"";
    return `<button type="button" class="dd-row" data-k="${esc(f.k)}"><span><b>${esc(f.n)}${n}</b><small>${esc(f.s)}${st[1]?" · "+esc(st[1]):""}</small><i>${T.m_fib} ${r1(f.f)} · ${T.m_prot} ${r1(f.p)} · ${T.m_fat} ${r1(f.t)} ${T.u_g}</i></span>${b}</button>`;}).join("");}
function drawSheet(){document.getElementById("ddSheetH").textContent=fmt(T.add_to,{slot:T["s_"+PK.slot]});
  document.getElementById("ddSlotPick").innerHTML=D.slots.map(s=>`<button type="button" class="chip" data-ps="${s}" aria-pressed="${s===PK.slot}">${T["s_"+s]}</button>`).join("");
  document.getElementById("ddCatPick").innerHTML=`<button type="button" class="chip" data-pc="" aria-pressed="${!PK.cat}">${T.all}</button>`+Object.keys(D.cats).map(c=>`<button type="button" class="chip" data-pc="${c}" aria-pressed="${PK.cat===c}">${esc(D.cats[c])}</button>`).join("");
  document.getElementById("ddList").innerHTML=listHtml();}
function openSheet(slot,opener){PK.slot=slot;PK.opener=opener;PK.q="";PK.cat="";document.getElementById("ddSearch").value="";drawSheet();sheet.hidden=false;document.body.style.overflow="hidden";
  setTimeout(()=>document.getElementById(matchMedia("(pointer:coarse)").matches?"ddDone":"ddSearch").focus(),30);}
function closeSheet(){sheet.hidden=true;document.body.style.overflow="";render();const o=PK.opener&&root.querySelector(`[data-open="${PK.slot}"]`);if(o)o.focus();}
sheet.addEventListener("click",e=>{if(e.target===sheet){closeSheet();return;}const b=e.target.closest("button");if(!b)return;
  if(b.id==="ddDone")closeSheet();
  else if(b.dataset.ps!==undefined){PK.slot=b.dataset.ps;drawSheet();}
  else if(b.dataset.pc!==undefined){PK.cat=b.dataset.pc;drawSheet();}
  else if(b.dataset.k){add(PK.slot,b.dataset.k,1);say(fmt(T.added,{food:BY[b.dataset.k].n}));const y=document.getElementById("ddList").scrollTop;document.getElementById("ddList").innerHTML=listHtml();document.getElementById("ddList").scrollTop=y;}});
document.getElementById("ddSearch").addEventListener("input",e=>{PK.q=e.target.value;document.getElementById("ddList").innerHTML=listHtml();});
document.addEventListener("keydown",e=>{if(sheet.hidden)return;if(e.key==="Escape"){closeSheet();return;}
  if(e.key==="Tab"){const f=[...sheet.querySelectorAll("button,input")].filter(x=>x.offsetParent);if(!f.length)return;const a=f[0],z=f[f.length-1];
    if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus();}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus();}}});
/* main events */
let clearArmed=false;
root.addEventListener("click",e=>{const b=e.target.closest("button");if(!b)return;
  if(b.dataset.open){openSheet(b.dataset.open,b);return;}
  if(b.dataset.rm){add(b.dataset.rm,b.dataset.k,-1);render();return;}
  if(b.dataset.w){DAY.w=Math.max(0,(DAY.w||0)+(+b.dataset.w));save();render();return;}
  if(b.dataset.s&&b.dataset.k){add(b.dataset.s,b.dataset.k,1);say(fmt(T.added,{food:BY[b.dataset.k].n}));render();return;}
  if(b.dataset.diet){S.diet=b.dataset.diet;save();render(true);return;}
  if(b.dataset.co){const c=b.dataset.co,i=S.co.indexOf(c);if(i>=0)S.co.splice(i,1);else S.co.push(c);save();render(true);return;}
  if(b.id==="ddClear"){if(!clearArmed){clearArmed=true;b.textContent=T.clear2;b.classList.add("warn");setTimeout(()=>{clearArmed=false;if(b.isConnected){b.textContent=T.clear;b.classList.remove("warn");}},3000);return;}
    DAY={s:{},w:0};save();clearArmed=false;render();}});
root.addEventListener("change",e=>{if(e.target.id==="ddPlan"){S.plan=e.target.value;save();render(true);}
  else if(e.target.id==="ddKg"){S.kg=e.target.value;save();render(true);}});
render();
})();"""
