"""'Explore your digestive system' hub on the home page (17 Oct 2026).
Replaces the old conditions list and the separate answers section: one organ at a time, chosen from a body map or tabs.
Each organ panel lists its common problems (condition pages + answer pages that describe a condition),
questions and tests (other answer pages) and procedures. Rendered as static HTML by build_site.py so every link is crawlable."""
import html, json, subprocess
import seo_en, seo_hi

e = lambda s: html.escape(s, quote=True)
ORDER = ["stomach", "liver", "gb", "pancreas", "intestine"]
COLOR = {"stomach": ("#F4B6AE", "#D9776B"), "liver": ("#D98C72", "#A9523D"), "gb": ("#AFD27E", "#6E9A3A"),
         "pancreas": ("#F3CF7A", "#C49A35"), "intestine": ("#F6CDB5", "#CF8B62")}

WHAT = {
 "en": {"stomach": "The food pipe carries food down; the stomach churns it with acid.",
        "liver": "Cleans the blood, stores energy and makes bile to digest fat.",
        "gb": "The gallbladder stores bile and squeezes it into the gut after meals.",
        "pancreas": "Makes digestive juices, and the insulin that controls blood sugar.",
        "intestine": "Absorb food and water, then form and pass stool."},
 "hi": {"stomach": "खाने की नली खाना नीचे ले जाती है; पेट उसे एसिड के साथ मथता है।",
        "liver": "खून साफ़ करता है, ऊर्जा जमा करता है और फ़ैट पचाने के लिए पित्त बनाता है।",
        "gb": "पित्ताशय पित्त जमा करता है और खाने के बाद उसे आँत में छोड़ता है।",
        "pancreas": "पाचन रस और खून की शुगर काबू में रखने वाला इंसुलिन बनाता है।",
        "intestine": "खाना और पानी सोखती हैं, फिर मल बनाकर बाहर निकालती हैं।"},
}

LBL = {
 "en": dict(problems="Common problems", qs="Questions and tests", procs="Tests and procedures", hint="Tap a part of the body",
            topics="topics", topic="topic", az="Browse all topics, A to Z", az_c="Conditions and problems", az_q="Questions and tests", az_p="Procedures",
            map="Digestive system: choose an organ", pick="Choose a part of the digestive system"),
 "hi": dict(problems="आम समस्याएँ", qs="सवाल और जाँचें", procs="जाँच और प्रोसीजर", hint="शरीर के किसी हिस्से पर टैप करें",
            topics="विषय", topic="विषय", az="सभी विषय देखें", az_c="बीमारियाँ और समस्याएँ", az_q="सवाल और जाँचें", az_p="प्रोसीजर",
            map="पाचन तंत्र: कोई अंग चुनें", pick="पाचन तंत्र का कोई हिस्सा चुनें"),
}

# Answer pages that describe a condition, shown as problem cards: slug -> (organ, EN name, EN line, HI name, HI line)
PROBLEMS = {
 "stomach-cancer-warning-signs": ("stomach", "Stomach cancer", "Warning signs that need an endoscopy.", "पेट का कैंसर", "ख़तरे के संकेत जिनमें एंडोस्कोपी ज़रूरी है।"),
 "achalasia": ("stomach", "Achalasia", "The food pipe muscle does not relax.", "अकेलेशिया", "खाने की नली की मांसपेशी ढीली नहीं होती।"),
 "alcoholic-hepatitis": ("liver", "Alcoholic hepatitis", "Sudden liver inflammation from heavy drinking.", "अल्कोहलिक हेपेटाइटिस", "ज़्यादा शराब से लिवर में अचानक सूजन।"),
 "aclf-acute-on-chronic-liver-failure": ("liver", "ACLF (acute-on-chronic liver failure)", "Sudden worsening of long-standing liver disease.", "ACLF (एक्यूट-ऑन-क्रॉनिक लिवर फ़ेल्योर)", "पुरानी लिवर बीमारी का अचानक बिगड़ना।"),
 "ascites-fluid-in-abdomen": ("liver", "Ascites (fluid in the belly)", "Fluid build-up, most often from cirrhosis.", "जलोदर (पेट में पानी)", "पेट में पानी भरना, अक्सर सिरोसिस से।"),
 "hepatic-encephalopathy": ("liver", "Hepatic encephalopathy", "Confusion and sleepiness in liver disease.", "हेपेटिक एन्सेफ़ेलोपैथी", "लिवर की बीमारी में भ्रम और ज़्यादा नींद।"),
 "liver-abscess": ("liver", "Liver abscess", "Pus in the liver, with fever and right-sided pain.", "लिवर एब्सेस", "लिवर में मवाद, बुखार और दाईं ओर दर्द के साथ।"),
 "piles-fissure-fistula": ("intestine", "Piles, fissure and fistula", "Bleeding, pain or discharge at the back passage.", "बवासीर, फ़िशर और फ़िस्टुला", "मल द्वार पर खून, दर्द या रिसाव।"),
 "celiac-disease": ("intestine", "Celiac disease", "Gluten damages the small intestine.", "सीलिएक बीमारी", "ग्लूटेन से छोटी आँत को नुकसान।"),
 "lactose-intolerance": ("intestine", "Lactose intolerance", "Gas and loose motions after milk.", "लैक्टोज़ इनटॉलरेंस", "दूध के बाद गैस और दस्त।"),
 "stomach-infection-gastroenteritis": ("intestine", "Stomach infection", "Loose motions and vomiting, usually from a virus.", "पेट का इंफ़ेक्शन", "दस्त और उल्टी, अक्सर वायरस से।"),
}
# Other answer pages, shown as question chips under their organ.
QS = {
 "stomach": ["when-is-acidity-serious", "is-endoscopy-painful"],
 "liver": ["is-fatty-liver-reversible", "high-sgpt-sgot-liver-function-test", "fatty-liver-grade-on-ultrasound", "fibroscan-test",
           "diet-in-jaundice", "liver-cancer-screening", "when-is-liver-transplant-needed"],
 "gb": [], "pancreas": [],
 "intestine": ["gas-and-bloating", "is-ibs-dangerous", "blood-in-stool-always-piles", "stool-tests", "capsule-endoscopy"],
}
PROCS = {
 "stomach": ["upper-gi-endoscopy", "dilatation-stenting", "gi-bleeding-treatment", "peg-feeding-tube"],
 "liver": ["variceal-banding-evl", "endoscopic-ultrasound-eus"],
 "gb": ["ercp", "endoscopic-ultrasound-eus"],
 "pancreas": ["endoscopic-ultrasound-eus", "ercp"],
 "intestine": ["colonoscopy", "polyp-removal-emr", "gi-bleeding-treatment"],
}

SHORT = {"en": {"stomach": "Food pipe & stomach", "liver": "Liver", "gb": "Gallbladder", "pancreas": "Pancreas", "intestine": "Intestines"},
         "hi": {"stomach": "खाने की नली और पेट", "liver": "लिवर", "gb": "पित्ताशय", "pancreas": "पैंक्रियास", "intestine": "आँतें"}}
# Body map geometry (viewBox 0 0 300 430). Patient's right is the viewer's left, as in an anatomy chart.
TORSO = ("M136 76 C122 86 96 92 74 96 C50 100 36 114 33 140 C29 180 25 228 24 262 C24 274 36 278 39 266 "
         "C42 236 45 196 50 158 C54 196 58 236 58 280 C58 330 66 384 92 414 L208 414 C234 384 242 330 242 280 "
         "C242 236 246 196 250 158 C255 196 258 236 261 266 C264 278 276 274 276 262 C275 228 271 180 267 140 "
         "C264 114 250 100 226 96 C204 92 178 86 164 76 Z")
ESOPH = "M150 84 C150 120 156 150 170 182"
LIVER = ("M70 182 C76 162 112 150 152 154 C174 156 194 160 206 168 C204 180 190 188 172 192 C164 216 142 236 112 240 "
         "C88 242 68 228 66 208 C65 198 67 190 70 182 Z")
STOM = ("M168 180 C176 166 206 162 224 172 C242 182 246 210 238 232 C230 254 208 268 184 266 C172 265 162 260 156 252 "
        "L160 244 C168 248 178 250 188 246 C204 240 214 226 214 210 C214 196 204 186 190 186 C182 186 176 190 170 194 Z")
DUO = "M156 250 C142 252 132 262 132 276 C132 292 144 302 162 302"
PANC = "M146 272 C162 266 198 264 228 254 C240 251 244 260 236 266 C208 278 178 286 158 292 C144 294 136 284 146 272 Z"
BILE = "M134 228 C138 244 142 256 146 268"
COLON = "M90 380 V322 Q90 310 102 310 H204 Q216 310 216 322 V362 Q216 380 194 384 Q174 388 164 394 L160 400"
SMALL = "M116 328 H188 Q197 328 197 336 Q197 344 188 344 H120 Q111 344 111 352 Q111 360 120 360 H188 Q197 360 197 368 Q197 375 188 375 H128"
PINS = {"stomach": (214, 214), "liver": (106, 200), "gb": (124, 236), "pancreas": (204, 272), "intestine": (155, 352)}
LABEL_AT = {"stomach": (214, 150), "liver": (106, 172), "gb": (104, 262), "pancreas": (214, 296), "intestine": (155, 302)}

def page_data(js_block):
    """ORGANS and CONDITIONS as defined in the page source for one language."""
    out = subprocess.run(["node", "-e", js_block + ";console.log(JSON.stringify({ORGANS,CONDITIONS}))"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def body_map(lang, organs):
    c = COLOR
    def grp(k, inner):
        return f'<g class="org" data-organ="{k}" tabindex="-1" role="button" aria-label="{e(organs[k])}">{inner}</g>'
    def grad(k):
        f, l = c[k]
        return (f'<radialGradient id="bm-{k}" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".55"/>'
                f'<stop offset=".45" stop-color="{f}"/><stop offset="1" stop-color="{l}" stop-opacity=".9"/></radialGradient>')
    defs = ("<defs>" + "".join(grad(k) for k in ORDER)
            + '<filter id="bm-sh" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="1.5" stdDeviation="1.6" flood-color="#12302C" flood-opacity=".22"/></filter>'
            + '<linearGradient id="bm-body" x1="0" y1="0" x2="0" y2="1"><stop offset="0" class="bm-b1"/><stop offset="1" class="bm-b2"/></linearGradient></defs>')
    body = (f'<g class="bm-body"><circle cx="150" cy="38" r="30"/><path d="M137 62 H163 V84 H137 Z"/><path d="{TORSO}"/></g>'
            '<g class="bm-ribs" fill="none">' + "".join(f'<path d="M{150-w} {y} Q150 {y+18} {150+w} {y}"/>' for w, y in [(70, 118), (80, 136), (86, 154)]) + '</g>')
    gut = grp("intestine",
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][1]}" stroke-width="24" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][0]}" stroke-width="19" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][1]}" stroke-width="19" stroke-dasharray="1.6 9" stroke-linejoin="round" opacity=".45"/>'
              f'<path d="{SMALL}" fill="none" stroke="{c["intestine"][1]}" stroke-width="13" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{SMALL}" fill="none" stroke="#F9D9C6" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="M122 334 H150" stroke="#fff" stroke-width="2.5" stroke-linecap="round" opacity=".7"/>')
    panc = grp("pancreas", f'<path d="{DUO}" fill="none" stroke="#E7B7A2" stroke-width="11" stroke-linecap="round"/>'
                           f'<path d="{PANC}" fill="url(#bm-pancreas)" stroke="{c["pancreas"][1]}" stroke-width="1.8" filter="url(#bm-sh)"/>'
                           + "".join(f'<circle cx="{x}" cy="{y}" r="1.7" fill="{c["pancreas"][1]}" opacity=".55"/>' for x, y in [(150,280),(166,276),(184,272),(202,267),(220,262)]))
    stomach = grp("stomach", f'<path d="{ESOPH}" fill="none" stroke="{c["stomach"][1]}" stroke-width="13" stroke-linecap="round"/>'
                             f'<path d="{ESOPH}" fill="none" stroke="{c["stomach"][0]}" stroke-width="8.5" stroke-linecap="round"/>'
                             f'<path d="{STOM}" fill="url(#bm-stomach)" stroke="{c["stomach"][1]}" stroke-width="1.8" filter="url(#bm-sh)"/>'
                             '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".55">'
                             '<path d="M196 196 C210 204 216 222 210 238"/><path d="M220 192 C232 208 232 228 222 246"/><path d="M182 256 C196 258 210 252 220 242"/></g>')
    liver = grp("liver", f'<path d="{LIVER}" fill="url(#bm-liver)" stroke="{c["liver"][1]}" stroke-width="1.8" filter="url(#bm-sh)"/>'
                         f'<path d="M150 158 C146 176 150 186 160 192" fill="none" stroke="{c["liver"][1]}" stroke-width="1.4" opacity=".6"/>')
    gb = grp("gb", f'<path d="{BILE}" fill="none" stroke="{c["gb"][1]}" stroke-width="3" stroke-linecap="round"/>'
                   f'<path d="M124 222 C134 222 140 232 138 244 C136 254 128 258 122 254 C114 248 114 230 124 222 Z" fill="url(#bm-gb)" stroke="{c["gb"][1]}" stroke-width="1.8" filter="url(#bm-sh)"/>')
    pins = "".join(f'<g class="pin" data-organ="{k}" transform="translate({x} {y})" aria-hidden="true"><circle class="pulse" r="8" stroke="{c[k][1]}"/>'
                   f'<circle r="7" fill="#fff" stroke="{c[k][1]}" stroke-width="3"/><circle r="2.6" fill="{c[k][1]}"/></g>' for k, (x, y) in PINS.items())
    labels = ""
    for k, (x, y) in LABEL_AT.items():
        t = SHORT[lang][k]; w = len(t) * (7.4 if lang == "hi" else 6.6) + 18
        labels += (f'<g class="olabel" data-organ="{k}" aria-hidden="true"><rect x="{x - w/2:.0f}" y="{y - 12}" width="{w:.0f}" height="22" rx="11"/>'
                   f'<text x="{x}" y="{y + 3}" text-anchor="middle">{e(t)}</text></g>')
    return (f'<svg class="body-map" viewBox="20 0 260 430" role="group" aria-label="{e(LBL[lang]["map"])}">{defs}{body}'
            f'{gut}{panc}{stomach}{liver}{gb}{pins}{labels}</svg>')


def hub_html(lang, data):
    L = LBL[lang]; pre = "/" if lang == "en" else "/hi/"
    S = seo_en if lang == "en" else seo_hi
    organs = data["ORGANS"]; conds = data["CONDITIONS"]
    ans_q = {b["slug"]: x["q"] for b, x in zip(seo_en.ANSWERS, S.ANSWERS)}
    proc_n = {b["slug"]: x["seo"] for b, x in zip(seo_en.PROCS, S.PROCS)}
    tabs, panels, az_c, az_q, az_p = [], [], [], [], []
    for k in ORDER:
        probs = [(f'{pre}conditions/{seo_en.CONDS[i]["slug"]}/', c["n"], c["s"]) for i, c in enumerate(conds) if c["o"] == k]
        probs += [(f'{pre}answers/{slug}/', v[1] if lang == "en" else v[3], v[2] if lang == "en" else v[4]) for slug, v in PROBLEMS.items() if v[0] == k]
        qs = [(f'{pre}answers/{s}/', ans_q[s]) for s in QS[k]]
        ps = [(f'{pre}procedures/{s}/', proc_n[s]) for s in PROCS[k]]
        az_c += [(h, n) for h, n, _ in probs]; az_q += qs; az_p += ps
        n = len(probs) + len(qs)
        fill, line = COLOR[k]
        tabs.append(f'<button type="button" class="hub-tab" role="tab" id="hubtab-{k}" data-k="{k}" aria-controls="hub-{k}" aria-selected="false" tabindex="-1">'
                    f'<i style="background:{fill};border-color:{line}"></i><span>{e(organs[k])}</span><em>{n} {L["topic"] if n == 1 else L["topics"]}</em></button>')
        cards = "".join(f'<a class="hc" href="{h}"><b>{e(nm)}</b><span>{e(ln)}</span><i aria-hidden="true">→</i></a>' for h, nm, ln in probs)
        chips = "".join(f'<a class="hq" href="{h}">{e(q)}</a>' for h, q in qs)
        pchips = "".join(f'<a class="hp" href="{h}">{e(nm)}</a>' for h, nm in ps)
        panels.append(f'<div class="hub-panel" role="tabpanel" id="hub-{k}" data-k="{k}" aria-labelledby="hubtab-{k}" hidden>'
                      f'<div class="hub-head"><i style="background:{fill};border-color:{line}"></i><div><h3>{e(organs[k])}</h3><p>{e(WHAT[lang][k])}</p></div></div>'
                      f'<h4>{L["problems"]}</h4><div class="hcs">{cards}</div>'
                      + (f'<h4>{L["qs"]}</h4><div class="hqs">{chips}</div>' if qs else "")
                      + f'<h4>{L["procs"]}</h4><div class="hqs">{pchips}</div></div>')
    uniq = lambda xs: sorted({h: n for h, n in xs}.items(), key=lambda t: t[1].lower())
    az = "".join(f'<div><h4>{t}</h4><ul>' + "".join(f'<li><a href="{h}">{e(n)}</a></li>' for h, n in uniq(xs)) + "</ul></div>"
                 for t, xs in [(L["az_c"], az_c), (L["az_q"], az_q), (L["az_p"], az_p)])
    return (f'<div class="hub" id="hub" data-sel="stomach">'
            f'<div class="hub-pick"><div class="hub-mapwrap">{body_map(lang, organs)}<p class="hub-hint"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 11V5a2 2 0 0 1 4 0v5m0-1a2 2 0 0 1 4 0v2m0-1a2 2 0 0 1 4 0v4c0 4-3 7-7 7h-1c-3 0-5-2-6.5-4L4 15a1.8 1.8 0 0 1 2.8-2.2L9 15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>{L["hint"]}</p></div>'
            f'<div class="hub-tabs" role="tablist" aria-label="{e(L["pick"])}">{"".join(tabs)}</div></div>'
            f'<div class="hub-main">{"".join(panels)}</div></div>'
            f'<details class="az"><summary>{L["az"]}</summary><div class="az-cols">{az}</div></details>')
