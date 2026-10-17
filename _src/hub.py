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

LIVER = "M28 114 C32 90 96 80 130 96 C126 104 120 108 114 112 C112 134 92 152 62 154 C40 156 24 138 28 114 Z"
STOMACH = "M124 98 C150 84 192 98 190 128 C188 154 160 168 138 160 C120 154 122 134 138 130 C152 126 152 112 128 112 Z"
PANC = "M96 182 C118 172 160 172 196 166 C203 172 197 181 182 184 C158 188 124 191 104 192 C94 192 90 186 96 182 Z"
COLON = "M62 286 V216 Q62 204 74 204 H176 Q190 204 190 218 V262 Q190 282 164 286 Q140 290 132 302"
PINS = {"stomach": (163, 126), "liver": (64, 118), "gb": (98, 158), "pancreas": (150, 181), "intestine": (127, 246)}


def page_data(js_block):
    """ORGANS and CONDITIONS as defined in the page source for one language."""
    out = subprocess.run(["node", "-e", js_block + ";console.log(JSON.stringify({ORGANS,CONDITIONS}))"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def body_map(lang, organs):
    c = COLOR
    def grp(k, inner):
        return (f'<g class="org" data-organ="{k}" tabindex="-1" role="button" aria-label="{e(organs[k])}">{inner}</g>')
    stomach = grp("stomach", f'<path d="M126 -6 V100" stroke="{c["stomach"][1]}" stroke-width="15" stroke-linecap="round"/>'
                             f'<path d="M126 -6 V100" stroke="{c["stomach"][0]}" stroke-width="10" stroke-linecap="round"/>'
                             f'<path d="{STOMACH}" fill="{c["stomach"][0]}" stroke="{c["stomach"][1]}" stroke-width="2"/>'
                             f'<path d="M140 104 C160 100 178 110 180 128" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".55"/>')
    liver = grp("liver", f'<path d="{LIVER}" fill="{c["liver"][0]}" stroke="{c["liver"][1]}" stroke-width="2"/>'
                         f'<path d="M40 112 C52 98 82 94 104 100" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" opacity=".45"/>')
    gb = grp("gb", f'<path d="M112 120 C110 140 100 150 98 160" fill="none" stroke="{c["gb"][1]}" stroke-width="3"/>'
                   f'<ellipse cx="98" cy="156" rx="9" ry="14" transform="rotate(-20 98 156)" fill="{c["gb"][0]}" stroke="{c["gb"][1]}" stroke-width="2"/>')
    panc = grp("pancreas", f'<path d="{PANC}" fill="{c["pancreas"][0]}" stroke="{c["pancreas"][1]}" stroke-width="2"/>'
                           + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="{c["pancreas"][1]}" opacity=".6"/>' for x, y in [(112,184),(128,182),(146,180),(164,177),(182,174)]))
    gut = grp("intestine", f'<path d="{COLON}" fill="none" stroke="{c["intestine"][1]}" stroke-width="21" stroke-linecap="round" stroke-linejoin="round"/>'
                           f'<path d="{COLON}" fill="none" stroke="{c["intestine"][0]}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
                           f'<rect x="84" y="222" width="88" height="56" rx="22" fill="#F9DCCB" stroke="{c["intestine"][1]}" stroke-width="2"/>'
                           f'<path d="M100 234 H156 Q164 234 164 242 Q164 249 156 249 H102 Q94 249 94 256 Q94 264 102 264 H154" fill="none" stroke="{c["intestine"][1]}" stroke-width="3" stroke-linecap="round"/>')
    pins = "".join(f'<g class="pin" data-organ="{k}" transform="translate({x} {y})" aria-hidden="true"><circle class="pulse" r="8" stroke="{c[k][1]}"/>'
                   f'<circle r="7" fill="#fff" stroke="{c[k][1]}" stroke-width="3"/><circle r="2.6" fill="{c[k][1]}"/></g>' for k, (x, y) in PINS.items())
    torso = ('<path class="torso" d="M104 -24 H148 L150 -2 C196 6 234 30 240 82 C244 120 238 200 238 300 C238 322 224 334 204 334 H36 '
             'C16 334 2 322 2 300 C2 200 -4 120 0 82 C6 30 44 6 102 -2 Z"/>')
    return (f'<svg class="body-map" viewBox="-12 -28 264 368" role="group" aria-label="{e(LBL[lang]["map"])}">{torso}'
            f'{gut}{panc}{liver}{gb}{stomach}{pins}</svg>')


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
