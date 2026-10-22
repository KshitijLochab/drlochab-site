"""Research and presentations list for the About page (EN + HI), drafted 22 Oct 2026.

HELD FOR CONFIRMATION: RESEARCH_LIVE = False. Titles below are working descriptions taken from earlier conversations;
Dr. Lochab must confirm the exact titles, author order, journal and meeting names before this goes live.
Until then the About page keeps its one-line research summary. PREVIEW=1 shows the list locally.
Research titles stay in English on the Hindi page (that is how they were published)."""
import os

RESEARCH_LIVE = False
PREVIEW = os.environ.get("PREVIEW") == "1"

# (kind, title, where, year, role)
ITEMS = [
 ("article", "EUS-guided tractogastrostomy for external pancreatic fistula in disconnected pancreatic duct syndrome: a case series",
  "Journal of Digestive Endoscopy; also presented as a poster at WCOG 2026", "2026", "co-author (Sud S, et al.)"),
 ("poster", "Haematological safety of tofacitinib combined with azathioprine in ulcerative colitis: a prospective cohort study",
  "World Congress of Gastroenterology (WCOG) 2026", "2026", "presenting author"),
 ("poster", "Bleeding from ulcers after variceal band ligation: a 10-year experience with glue therapy, oesophageal stenting and early TIPS",
  "WCOG 2026; earlier presented at ENDOCON 2025", "2026", "presenting author"),
 ("poster", "Restoring the lumen in a total oesophageal stricture with a double-scope technique: a case report",
  "WCOG 2026", "2026", "co-author"),
 ("poster", "Closure of a malignant gastro-colonic fistula with a 36-mm cardiac septal occluder: a case report",
  "WCOG 2026; also ENDOCON 2026", "2026", "co-author"),
]
INTERESTS = {"en": ["Variceal bleeding and portal hypertension", "EUS-guided procedures", "Complex oesophageal strictures", "Safety of IBD treatments", "Pancreatic duct strictures in chronic pancreatitis"],
             "hi": ["वैरिसियल ब्लीडिंग और पोर्टल हाइपरटेंशन", "EUS से होने वाले प्रोसीजर", "खाने की नली की जटिल सिकुड़न", "IBD के इलाज की सुरक्षा", "क्रोनिक पैंक्रियाटाइटिस में पैंक्रियास नली की सिकुड़न"]}
T = {"en": dict(kind={"article": "Journal article", "poster": "Poster"}, interests="Research interests", list_h="Publications and presentations"),
     "hi": dict(kind={"article": "जर्नल लेख", "poster": "पोस्टर"}, interests="शोध के विषय", list_h="प्रकाशन और प्रस्तुतियाँ")}

def html(lang, e):
    """Returns the research block, or '' while held."""
    if not (RESEARCH_LIVE or PREVIEW):
        return ""
    X = T[lang]
    items = "".join(f'<li><span class="rs-k">{X["kind"][k]} · {e(y)}</span><b lang="en">{e(t)}</b><span lang="en">{e(w)} · {e(r)}</span></li>' for k, t, w, y, r in ITEMS)
    return (f'<h3>{X["interests"]}</h3><div class="lp-tags">' + "".join(f"<span>{e(i)}</span>" for i in INTERESTS[lang]) + "</div>"
            f'<h3>{X["list_h"]}</h3><ul class="rs-list">{items}</ul>')

CSS = ".rs-list{list-style:none;padding:0;margin:0;display:grid;gap:12px}.rs-list li{display:grid;gap:3px;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px}.rs-list .rs-k{font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--accent)}.rs-list li>span:last-child{font-size:.88rem;color:var(--muted)}"
