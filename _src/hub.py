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
 "liver-cancer-screening": ("liver", "Liver cancer (HCC)", "Who needs screening every six months, and why.", "लिवर कैंसर (HCC)", "किसे हर छह महीने जाँच चाहिए, और क्यों।"),
 "tb-medicines-and-liver": ("liver", "Liver injury from TB medicines", "Warning signs, and what to do at once.", "टीबी की दवाओं से लिवर पर असर", "ख़तरे के संकेत, और तुरंत क्या करें।"),
 "oesophageal-cancer": ("stomach", "Food pipe cancer", "Swallowing that gets harder, with weight loss.", "खाने की नली का कैंसर", "बढ़ती निगलने की दिक्कत, वज़न घटने के साथ।"),
 "cholecystitis-gallbladder-infection": ("gb", "Cholecystitis", "Gallbladder inflammation, usually from a stone.", "कोलेसिस्टाइटिस", "पित्ताशय की सूजन, अक्सर पथरी से।"),
 "cholangitis-bile-duct-infection": ("gb", "Cholangitis", "Infection of a blocked bile duct: an emergency.", "कोलैंजाइटिस", "बंद पित्त की नली में इंफ़ेक्शन: इमरजेंसी।"),
 "blocked-bile-duct-obstructive-jaundice": ("gb", "Blocked bile duct", "Jaundice with itching and pale stools.", "पित्त की नली बंद होना", "खुजली और हल्के मल के साथ पीलिया।"),
 "gallbladder-polyps": ("gb", "Gallbladder polyps", "Usually harmless; size decides the plan.", "पित्ताशय के पॉलिप", "अक्सर नुकसान रहित; आकार से योजना तय होती है।"),
 "gallbladder-cancer": ("gb", "Gallbladder cancer", "More common in North India; linked to stones.", "पित्ताशय का कैंसर", "उत्तर भारत में ज़्यादा; पथरी से जुड़ा।"),
 "cholangiocarcinoma-bile-duct-cancer": ("gb", "Bile duct cancer", "Painless jaundice that keeps deepening.", "पित्त की नली का कैंसर", "बिना दर्द का बढ़ता पीलिया।"),
 "choledochal-cyst": ("gb", "Choledochal cyst", "A widened bile duct present from birth.", "कोलेडोकल सिस्ट", "जन्म से फैली हुई पित्त की नली।"),
 "pain-after-gallbladder-removal": ("gb", "Pain after gallbladder removal", "Left-behind stones, bile leaks and other causes.", "पित्ताशय निकालने के बाद दर्द", "बची पथरी, पित्त का रिसाव और दूसरी वजहें।"),
 "chronic-pancreatitis": ("pancreas", "Chronic pancreatitis", "Long-term damage: pain, oily stools, diabetes.", "पुरानी पैंक्रियाटाइटिस", "लंबा नुकसान: दर्द, चिकना मल, डायबिटीज़।"),
 "pancreatic-pseudocyst-walled-off-necrosis": ("pancreas", "Pseudocyst and walled-off necrosis", "Collections after pancreatitis, drained by EUS.", "स्यूडोसिस्ट और वॉल्ड-ऑफ़ नेक्रोसिस", "पैंक्रियाटाइटिस के बाद जमा पानी, EUS से निकाला जाता है।"),
 "pancreatic-cancer": ("pancreas", "Pancreatic cancer", "Painless jaundice, back pain, weight loss.", "पैंक्रियास का कैंसर", "बिना दर्द का पीलिया, पीठ दर्द, वज़न घटना।"),
 "abdominal-tuberculosis": ("intestine", "Abdominal tuberculosis", "Weight loss, fever and belly pain; curable.", "पेट की टीबी", "वज़न घटना, बुखार और पेट दर्द; ठीक हो सकती है।"),
 "hepatitis-a-and-e": ("liver", "Hepatitis A and E", "The commonest cause of jaundice in India.", "हेपेटाइटिस A और E", "भारत में पीलिया की सबसे आम वजह।"),
 "gilberts-syndrome": ("liver", "Gilbert's syndrome", "Slightly high bilirubin that is harmless.", "गिल्बर्ट सिंड्रोम", "थोड़ा बढ़ा बिलीरुबिन जो नुकसान रहित है।"),
 "herbal-supplement-liver-damage": ("liver", "Liver injury from supplements", "Herbal, Ayurvedic and gym products.", "सप्लीमेंट से लिवर को नुकसान", "हर्बल, आयुर्वेदिक और जिम प्रोडक्ट।"),
 "wilsons-disease": ("liver", "Wilson's disease", "Inherited copper build-up in young people.", "विल्सन डिज़ीज़", "युवाओं में ख़ानदानी तांबे का जमाव।"),
 "vomiting-blood-black-stools": ("stomach", "Vomiting blood, black stools", "Upper GI bleeding: an emergency.", "ख़ून की उल्टी, काला मल", "ऊपरी पेट की ब्लीडिंग: इमरजेंसी।"),
 "hiatus-hernia": ("stomach", "Hiatus hernia", "The stomach slides up into the chest.", "हाइटस हर्निया", "पेट का हिस्सा छाती में खिसकना।"),
 "worms-in-stomach": ("intestine", "Worms in the stomach", "Real signs, myths and simple treatment.", "पेट में कीड़े", "असली संकेत, भ्रम और आसान इलाज।"),
 "chronic-diarrhoea-mucus-in-stool": ("intestine", "Long-lasting loose motions", "Diarrhoea for weeks, or mucus in stool.", "लंबे समय के दस्त", "हफ़्तों से दस्त, या मल में आँव।"),
 "appendicitis-or-gas-pain": ("intestine", "Appendicitis or gas?", "Lower right belly pain: how to tell.", "अपेंडिसाइटिस या गैस?", "निचले दाएँ पेट में दर्द: फ़र्क़ कैसे पहचानें।"),
 "typhoid-fever": ("intestine", "Typhoid", "Rising fever; blood culture, not Widal.", "टाइफ़ाइड", "बढ़ता बुखार; विडाल नहीं, ब्लड कल्चर।"),
 "travellers-diarrhoea": ("intestine", "Loose motions while travelling", "Prevention and treatment on trips.", "यात्रा में दस्त", "सफ़र में बचाव और इलाज।"),
}
# Other answer pages, shown as question chips under their organ.
QS = {
 "stomach": ["when-is-acidity-serious", "is-endoscopy-painful", "is-pantoprazole-safe-long-term", "burping-and-hiccups", "weight-loss-injections-and-gut"],
 "liver": ["is-fatty-liver-reversible", "high-sgpt-sgot-liver-function-test", "fatty-liver-grade-on-ultrasound", "fibroscan-test",
           "diet-in-jaundice", "when-is-liver-transplant-needed", "ultrasound-report-terms", "how-much-alcohol-is-safe-for-liver"],
 "gb": [], "pancreas": ["diabetes-and-digestive-system"],
 "intestine": ["gas-and-bloating", "is-ibs-dangerous", "blood-in-stool-always-piles", "stool-tests", "capsule-endoscopy", "do-probiotics-help"],
}
PROCS = {
 "stomach": ["upper-gi-endoscopy", "dilatation-stenting", "gi-bleeding-treatment", "peg-feeding-tube"],
 "liver": ["variceal-banding-evl", "endoscopic-ultrasound-eus"],
 "gb": ["ercp", "endoscopic-ultrasound-eus"],
 "pancreas": ["endoscopic-ultrasound-eus", "ercp"],
 "intestine": ["colonoscopy", "polyp-removal-emr", "gi-bleeding-treatment"],
}

SHORT = {"en": {"stomach": "Stomach", "liver": "Liver", "gb": "Gallbladder", "pancreas": "Pancreas", "intestine": "Intestines"},
         "hi": {"stomach": "पेट", "liver": "लिवर", "gb": "पित्ताशय", "pancreas": "पैंक्रियास", "intestine": "आँतें"}}
# Body map geometry. viewBox x -70..370, y 70..415. Patient's right is the viewer's left, as in an anatomy chart.
VB = (-75, 70, 460, 345)
ESOPH = "M150 84 C150 120 156 150 170 182"
LIVER = ("M70 182 C76 162 112 150 152 154 C174 156 194 160 206 168 C204 180 190 188 172 192 C164 216 142 236 112 240 "
         "C88 242 68 228 66 208 C65 198 67 190 70 182 Z")
STOM = ("M170 186 C172 170 190 158 212 158 C236 158 254 176 254 202 C254 230 242 252 220 261 "
        "C204 268 184 268 168 262 C162 260 158 257 155 253 L157 239 C168 240 180 236 187 228 "
        "C193 220 194 206 188 198 C184 193 177 191 173 190 C171 189 170 188 170 186 Z")
DUO = "M156 250 C142 252 132 262 132 276 C132 292 144 302 162 302"
PANC = "M146 272 C162 266 198 264 228 254 C240 251 244 260 236 266 C208 278 178 286 158 292 C144 294 136 284 146 272 Z"
BILE = "M134 228 C138 244 142 256 146 268"
GB = "M124 222 C134 222 140 232 138 244 C136 254 128 258 122 254 C114 248 114 230 124 222 Z"
COLON = "M90 380 V322 Q90 310 102 310 H204 Q216 310 216 322 V362 Q216 380 194 384 Q174 388 164 394 L160 400"
SMALL = "M116 328 H188 Q197 328 197 336 Q197 344 188 344 H120 Q111 344 111 352 Q111 360 120 360 H188 Q197 360 197 368 Q197 375 188 375 H128"
# organ anchor point, label anchor point, side
CALLOUT = {"stomach": ((238, 196), (264, 134)), "pancreas": ((232, 262), (300, 300)),
           "liver": ((96, 190), (30, 132)), "gb": ((124, 240), (10, 270)), "intestine": ((212, 368), (302, 390))}

def page_data(js_block):
    """ORGANS and CONDITIONS as defined in the page source for one language."""
    out = subprocess.run(["node", "-e", js_block + ";console.log(JSON.stringify({ORGANS,CONDITIONS}))"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def body_map(lang, organs, counts):
    c = COLOR
    x0, y0, w, h = VB
    def grp(k, inner):
        return f'<g class="org" data-organ="{k}">{inner}</g>'
    def grad(k):
        f, l = c[k]
        return (f'<radialGradient id="bm-{k}" cx="35%" cy="28%" r="85%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".6"/>'
                f'<stop offset=".42" stop-color="{f}"/><stop offset="1" stop-color="{l}"/></radialGradient>')
    defs = ("<defs>" + "".join(grad(k) for k in ORDER)
            + '<filter id="bm-sh" x="-25%" y="-25%" width="150%" height="150%"><feDropShadow dx="0" dy="2" stdDeviation="2.2" flood-color="#12302C" flood-opacity=".25"/></filter>'
            + '<radialGradient id="bm-glow" cx="50%" cy="50%" r="50%"><stop offset="0" class="bm-g1"/><stop offset="1" class="bm-g2"/></radialGradient></defs>')
    W = 'stroke="#fff" stroke-width="2.4"'
    glow = '<ellipse class="bm-glowshape" cx="155" cy="246" rx="132" ry="172" fill="url(#bm-glow)"/>'
    gut = grp("intestine",
              f'<path d="{COLON}" fill="none" stroke="#fff" stroke-width="27" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][1]}" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][0]}" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{COLON}" fill="none" stroke="{c["intestine"][1]}" stroke-width="17" stroke-dasharray="1.6 9" stroke-linejoin="round" opacity=".5"/>'
              f'<path d="{SMALL}" fill="none" stroke="#fff" stroke-width="15" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{SMALL}" fill="none" stroke="{c["intestine"][1]}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="{SMALL}" fill="none" stroke="#FBE0CF" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
    panc = grp("pancreas", f'<path d="{DUO}" fill="none" stroke="#fff" stroke-width="13" stroke-linecap="round"/>'
                           f'<path d="{DUO}" fill="none" stroke="#EDB9A3" stroke-width="9" stroke-linecap="round"/>'
                           f'<path d="{PANC}" fill="url(#bm-pancreas)" {W} filter="url(#bm-sh)"/>'
                           + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="{c["pancreas"][1]}" opacity=".55"/>' for x, y in [(150,280),(166,276),(184,272),(202,267),(220,262)]))
    stomach = grp("stomach", f'<path d="{ESOPH}" fill="none" stroke="#fff" stroke-width="13" stroke-linecap="round"/>'
                             f'<path d="{ESOPH}" fill="none" stroke="{c["stomach"][1]}" stroke-width="9" stroke-linecap="round"/>'
                             f'<path d="{ESOPH}" fill="none" stroke="{c["stomach"][0]}" stroke-width="5" stroke-linecap="round"/>'
                             f'<path d="{STOM}" fill="url(#bm-stomach)" {W} filter="url(#bm-sh)"/>'
                             '<g fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" opacity=".6">'
                             '<path d="M214 180 C228 194 232 218 224 242"/><path d="M234 178 C246 196 246 222 236 246"/>'
                             '<path d="M176 254 C192 257 206 252 216 244"/><path d="M196 200 C208 212 210 230 202 246"/></g>')
    liver = grp("liver", f'<path d="{LIVER}" fill="url(#bm-liver)" {W} filter="url(#bm-sh)"/>'
                         f'<path d="M150 158 C146 176 150 186 160 192" fill="none" stroke="#fff" stroke-width="1.6" opacity=".6"/>')
    gb = grp("gb", f'<path d="{BILE}" fill="none" stroke="#fff" stroke-width="6" stroke-linecap="round"/>'
                   f'<path d="{BILE}" fill="none" stroke="{c["gb"][1]}" stroke-width="3" stroke-linecap="round"/>'
                   f'<path d="{GB}" fill="url(#bm-gb)" {W} filter="url(#bm-sh)"/>')
    lines = "".join(f'<g class="lead" data-organ="{k}"><path d="M{lx} {ly} L{ax} {ay}"/><circle cx="{ax}" cy="{ay}" r="3.6"/></g>'
                    for k, ((ax, ay), (lx, ly)) in CALLOUT.items())
    svg = (f'<svg class="body-map" viewBox="{x0} {y0} {w} {h}" aria-hidden="true" focusable="false">{defs}{glow}'
           f'{gut}{panc}{stomach}{liver}{gb}{lines}</svg>')
    L = LBL[lang]
    btns = ""
    for k in ORDER:
        (ax, ay), (lx, ly) = CALLOUT[k]
        left = (lx - x0) / w * 100; top = (ly - y0) / h * 100
        n = counts[k]
        btns += (f'<button type="button" class="hub-tab" role="tab" id="hubtab-{k}" data-k="{k}" aria-controls="hub-{k}" aria-selected="false" tabindex="-1" '
                 f'style="left:{left:.2f}%;top:{top:.2f}%"><i style="background:{c[k][0]};border-color:{c[k][1]}"></i>'
                 f'<span>{e(SHORT[lang][k])}</span><em>{n}</em></button>')
    return (f'<div class="hub-mapwrap">{svg}<div class="hub-tabs" role="tablist" aria-label="{e(L["pick"])}">{btns}</div></div>'
            f'<p class="hub-hint"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 11V5a2 2 0 0 1 4 0v5m0-1a2 2 0 0 1 4 0v2m0-1a2 2 0 0 1 4 0v4c0 4-3 7-7 7h-1c-3 0-5-2-6.5-4L4 15a1.8 1.8 0 0 1 2.8-2.2L9 15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>{L["hint"]}</p>')


def hub_html(lang, data):
    L = LBL[lang]; pre = "/" if lang == "en" else "/hi/"
    S = seo_en if lang == "en" else seo_hi
    organs = data["ORGANS"]; conds = data["CONDITIONS"]
    ans_q = {b["slug"]: x["q"] for b, x in zip(seo_en.ANSWERS, S.ANSWERS)}
    proc_n = {b["slug"]: x["seo"] for b, x in zip(seo_en.PROCS, S.PROCS)}
    counts, panels, az_c, az_q, az_p = {}, [], [], [], []
    for k in ORDER:
        probs = [(f'{pre}conditions/{seo_en.CONDS[i]["slug"]}/', c["n"], c["s"]) for i, c in enumerate(conds) if c["o"] == k]
        probs += [(f'{pre}answers/{slug}/', v[1] if lang == "en" else v[3], v[2] if lang == "en" else v[4]) for slug, v in PROBLEMS.items() if v[0] == k]
        qs = [(f'{pre}answers/{s}/', ans_q[s]) for s in QS[k]]
        ps = [(f'{pre}procedures/{s}/', proc_n[s]) for s in PROCS[k]]
        az_c += [(h, n) for h, n, _ in probs]; az_q += qs; az_p += ps
        n = len(probs) + len(qs)
        fill, line = COLOR[k]
        counts[k] = n
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
            f'<div class="hub-pick">{body_map(lang, organs, counts)}</div>'
            f'<div class="hub-main">{"".join(panels)}</div></div>'
            f'<details class="az"><summary>{L["az"]}</summary><div class="az-cols">{az}</div></details>')
