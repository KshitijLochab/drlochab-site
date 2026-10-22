"""Medical review line and references on article pages (EN + HI), 22 Oct 2026.

HELD FOR DR. LOCHAB'S REVIEW. Nothing here appears on the live site until he approves it:
- REFS_LIVE = False keeps every References section off the site.
- REVIEW_LOG starts empty. Add a page only after Dr. Lochab has actually reviewed it, with the date he did:
      "/conditions/fatty-liver/": "2026-11-02",
  The byline on that page (and its Hindi twin) then reads "Medically reviewed by Dr. Kshitij Lochab on 2 November 2026"
  and the structured data 'lastReviewed' uses that date.
- PREVIEW=1 in the environment shows everything locally for checking (never publish a PREVIEW build).

References are clinical guidelines checked on 22 Oct 2026 against the publisher or journal record (title, journal, year, DOI).
Page numbers are left out on purpose: the DOI link is the reliable pointer."""
import os, re, datetime, html as _html

PREVIEW = os.environ.get("PREVIEW") == "1"
REFS_LIVE = False
DEEP_LIVE = set()        # condition slugs whose deeper sections (cond_more_en/hi.py) are approved and shown
REVIEW_LOG = {}          # "/conditions/slug/": "YYYY-MM-DD", English path; the Hindi twin follows automatically

# key: (authors, title, journal, year, doi)
REFS = {
 "gerd": ("Katz PO, Dunbar KB, Schnoll-Sussman FH, et al.", "ACG Clinical Guideline for the Diagnosis and Management of Gastroesophageal Reflux Disease", "American Journal of Gastroenterology", 2022, "10.14309/ajg.0000000000001538"),
 "hp_acg": ("Chey WD, Howden CW, Moss SF, et al.", "ACG Clinical Guideline: Treatment of Helicobacter pylori Infection", "American Journal of Gastroenterology", 2024, "10.14309/ajg.0000000000002968"),
 "hp_maastricht": ("Malfertheiner P, Megraud F, Rokkas T, et al.", "Management of Helicobacter pylori infection: the Maastricht VI/Florence consensus report", "Gut", 2022, "https://gut.bmj.com/content/71/9/1724"),
 "masld_easl": ("European Association for the Study of the Liver (EASL), European Association for the Study of Diabetes (EASD), European Association for the Study of Obesity (EASO).", "EASL–EASD–EASO Clinical Practice Guidelines on the management of metabolic dysfunction-associated steatotic liver disease (MASLD)", "Journal of Hepatology", 2024, "10.1016/j.jhep.2024.04.031"),
 "nafld_aasld": ("Rinella ME, Neuschwander-Tetri BA, Siddiqui MS, et al.", "AASLD Practice Guidance on the clinical assessment and management of nonalcoholic fatty liver disease", "Hepatology", 2023, "10.1097/HEP.0000000000000323"),
 "lft": ("Kwo PY, Cohen SM, Lim JK.", "ACG Clinical Guideline: Evaluation of Abnormal Liver Chemistries", "American Journal of Gastroenterology", 2017, "10.1038/ajg.2016.517"),
 "ibs_acg": ("Lacy BE, Pimentel M, Brenner DM, et al.", "ACG Clinical Guideline: Management of Irritable Bowel Syndrome", "American Journal of Gastroenterology", 2021, "10.14309/ajg.0000000000001036"),
 "ibs_india": ("Ghoshal UC, Sachdeva S, Pratap N, et al.", "Indian consensus statements on irritable bowel syndrome in adults: a guideline by the Indian Neurogastroenterology and Motility Association and jointly supported by the Indian Society of Gastroenterology", "Indian Journal of Gastroenterology", 2023, "10.1007/s12664-022-01333-5"),
 "uc": ("Rubin DT, Ananthakrishnan AN, Siegel CA, et al.", "ACG Clinical Guideline Update: Ulcerative Colitis in Adults", "American Journal of Gastroenterology", 2025, "10.14309/ajg.0000000000003463"),
 "cd": ("Lichtenstein GR, Loftus EV Jr, Isaacs KL, et al.", "ACG Clinical Guideline: Management of Crohn's Disease in Adults", "American Journal of Gastroenterology", 2025, "10.14309/ajg.0000000000003465"),
 "cic": ("Chang L, Chey WD, Imdad A, et al.", "American Gastroenterological Association–American College of Gastroenterology Clinical Practice Guideline: Pharmacological Management of Chronic Idiopathic Constipation", "Gastroenterology", 2023, "10.1053/j.gastro.2023.03.214"),
 "ap": ("Tenner S, Vege SS, Sheth SG, et al.", "American College of Gastroenterology Guidelines: Management of Acute Pancreatitis", "American Journal of Gastroenterology", 2024, "10.14309/ajg.0000000000002645"),
 "cysts": ("Elta GH, Enestvedt BK, Sauer BG, Lennon AM.", "ACG Clinical Guideline: Diagnosis and Management of Pancreatic Cysts", "American Journal of Gastroenterology", 2018, "10.1038/ajg.2018.14"),
 "prep": ("Jacobson BC, Anderson JC, Burke CA, et al.", "Optimizing Bowel Preparation Quality for Colonoscopy: Consensus Recommendations by the US Multi-Society Task Force on Colorectal Cancer", "American Journal of Gastroenterology", 2025, "10.14309/ajg.0000000000003287"),
 "eus_ae": ("ASGE Standards of Practice Committee; Forbes N, Coelho-Prabhu N, Al-Haddad MA, et al.", "Adverse events associated with EUS and EUS-guided procedures", "Gastrointestinal Endoscopy", 2022, "10.1016/j.gie.2021.09.009"),
 "cbd": ("ASGE Standards of Practice Committee; Buxbaum JL, Abbas Fehmi SM, Sultan S, et al.", "ASGE guideline on the role of endoscopy in the evaluation and management of choledocholithiasis", "Gastrointestinal Endoscopy", 2019, "10.1016/j.gie.2018.10.001"),
 "ercp_ae": ("Dumonceau JM, Kapral C, Aabakken L, et al.", "ERCP-related adverse events: European Society of Gastrointestinal Endoscopy (ESGE) Guideline", "Endoscopy", 2020, "10.1055/a-1075-4080"),
}

# English path -> reference keys (the Hindi twin gets the same list)
PAGE_REFS = {
 "/conditions/acidity-reflux-gerd/": ["gerd"],
 "/conditions/h-pylori-gastritis-ulcer/": ["hp_acg", "hp_maastricht"],
 "/conditions/fatty-liver/": ["masld_easl", "nafld_aasld"],
 "/answers/is-fatty-liver-reversible/": ["masld_easl", "nafld_aasld"],
 "/answers/high-sgpt-sgot-liver-function-test/": ["lft"],
 "/conditions/ibs-irritable-bowel-syndrome/": ["ibs_acg", "ibs_india"],
 "/conditions/ulcerative-colitis-crohns-disease/": ["uc", "cd"],
 "/conditions/constipation/": ["cic"],
 "/conditions/pancreatitis/": ["ap"],
 "/conditions/pancreatic-cysts/": ["cysts"],
 "/procedures/colonoscopy/": ["prep"],
 "/guides/colonoscopy-preparation/": ["prep"],
 "/procedures/endoscopic-ultrasound-eus/": ["eus_ae"],
 "/procedures/ercp/": ["cbd", "ercp_ae"],
}

T = {"en": dict(h="References", note="Clinical guidelines this page follows. They are written for doctors.",
                rev="Medically reviewed by Dr. Kshitij Lochab on {d}", by="By Dr. Kshitij Lochab, Consultant Gastroenterologist"),
     "hi": dict(h="संदर्भ", note="वे चिकित्सा दिशानिर्देश जिनके आधार पर यह पेज लिखा गया है। ये डॉक्टरों के लिए अंग्रेज़ी में लिखे गए हैं।",
                rev="डॉ. क्षितिज लोचब द्वारा {d} को मेडिकल समीक्षा", by="लेखक: डॉ. क्षितिज लोचब, कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट")}
MONTHS_HI = ["जनवरी", "फ़रवरी", "मार्च", "अप्रैल", "मई", "जून", "जुलाई", "अगस्त", "सितंबर", "अक्टूबर", "नवंबर", "दिसंबर"]

def _en_path(path):
    return path[3:] if path.startswith("/hi/") else path

def refs_html(lang, path):
    keys = PAGE_REFS.get(_en_path(path))
    if not keys or not (REFS_LIVE or PREVIEW):
        return ""
    e = lambda x: _html.escape(x, quote=True)
    link = lambda d: (f'<a href="{d}" target="_blank" rel="noopener">{d.split("//")[1].split("/")[0]}</a>' if d.startswith("http")
                      else f'<a href="https://doi.org/{d}" target="_blank" rel="noopener">doi:{d}</a>')
    items = "".join(f'<li>{e(a)} {e(t)}. <i>{e(j)}</i> {y}. {link(d)}</li>' for a, t, j, y, d in (REFS[k] for k in keys))
    return f'<section class="refs" lang="en"><h2 lang="{lang}">{T[lang]["h"]}</h2><p class="small" lang="{lang}">{T[lang]["note"]}</p><ol>{items}</ol></section>'

def review_date(path):
    d = REVIEW_LOG.get(_en_path(path))
    return datetime.date.fromisoformat(d) if d else None

def apply(path, text):
    """Called by build_pages.write(): adds References before the share box and the reviewed-by line to the byline."""
    lang = "hi" if path.startswith("/hi/") else "en"
    r = refs_html(lang, path)
    if r and "</article>" in text:
        anchor = '<section class="share-end">' if '<section class="share-end">' in text else "</article>"
        text = text.replace(anchor, r + anchor, 1)
    d = review_date(path)
    if d and 'class="byline"' in text:
        ds = d.strftime("%-d %B %Y") if lang == "en" else f"{d.day} {MONTHS_HI[d.month - 1]} {d.year}"
        text = re.sub(r'<p class="byline">.*?</p>', f'<p class="byline">{T[lang]["by"]} · {T[lang]["rev"].format(d=ds)}</p>', text, count=1, flags=re.S)
        text = re.sub(r'"lastReviewed": "[^"]*"', f'"lastReviewed": "{d.isoformat()}"', text)
    return text

def deep_sections(lang, slug, e):
    """Extra sections for a condition page, if approved (or PREVIEW). Returns HTML."""
    if slug not in DEEP_LIVE and not PREVIEW:
        return ""
    import cond_more_en, cond_more_hi
    M = (cond_more_en if lang == "en" else cond_more_hi).MORE.get(slug)
    if not M:
        return ""
    out = ""
    for h, items in M:
        body, ul = "", []
        for it in items + [""]:
            if it.startswith("- "):
                ul.append(f"<li>{e(it[2:])}</li>"); continue
            if ul: body += "<ul>" + "".join(ul) + "</ul>"; ul = []
            if it: body += f"<p>{e(it)}</p>"
        out += f"<section><h2>{e(h)}</h2>{body}</section>"
    return out

def check():
    for p, ks in PAGE_REFS.items():
        assert all(k in REFS for k in ks), p
    for p, d in REVIEW_LOG.items():
        datetime.date.fromisoformat(d); assert not p.startswith("/hi/"), p
check()
import cond_more_en as _ce, cond_more_hi as _ch
assert set(_ce.MORE) == set(_ch.MORE)
for _k in _ce.MORE:
    assert [len(i) for _, i in _ce.MORE[_k]] == [len(i) for _, i in _ch.MORE[_k]], _k
