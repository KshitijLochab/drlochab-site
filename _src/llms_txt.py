"""/llms.txt for drlochab.com (12 Nov 2026): a plain Markdown map of the site for AI assistants and answer engines.

Written by build_site.py from the built pages (each page's <h1> and meta description), so it lists every page and
never goes stale. The key facts at the top come from clinics.py and the same wording as the About page.
Keep it factual: no rankings, no superlatives, no prices (NMC rules on advertising)."""
import html, os, re
import clinics

SITE = "https://drlochab.com"
GROUPS = [("about-dr-kshitij-lochab", "About"), ("gastroenterologist-in-gurgaon", "About"), ("conditions", "Conditions"),
          ("procedures", "Procedures and tests"), ("answers", "Answers to common questions"), ("guides", "Guides"),
          ("diet-charts", "Indian diet charts"), ("tools", "Free tools (data stays on the user's device)")]

def _meta(out, u):
    h = open(f"{out}{u}index.html", encoding="utf-8").read()
    t = re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', h)
    clean = lambda s: html.unescape(re.sub(r"<[^>]+>", "", s)).strip()
    return clean(t.group(1)) if t else u, clean(d.group(1)) if d else ""

def render(out, pairs):
    A = clinics.ARCURA["en"]
    lines = [
        "# Dr. Kshitij Lochab, Gastroenterologist in Gurgaon (Gurugram)",
        "",
        "> Patient education on the stomach, liver, gallbladder, pancreas and intestines, written for people in India in plain English "
        "and simple Hindi, prepared with AI assistance and medically reviewed by Dr. Kshitij Lochab. Education only: it does not replace "
        "a consultation. In an emergency in India, call 112 or go to the nearest emergency department.",
        "",
        "## Key facts",
        "- Name: Dr. Kshitij Lochab (Dr. Lochab)",
        "- Role: Consultant Gastroenterologist and Therapeutic Endoscopist, Gurugram (Gurgaon), Haryana, India",
        "- Training: MBBS; MD Internal Medicine; DrNB Gastroenterology at Medanta – The Medicity, Gurugram (All-India Gold Medal); Advanced Fellowship in EUS and ERCP",
        "- Current role: Associate Consultant, Apollo Hospitals, Golf Course Road, Gurugram",
        "- Registration: Haryana Medical Council Reg. No. HN-23524",
        f"- Clinic: Arcura Clinic, M2K Corporate Park & Shopping Plaza, 14, Mayfield Garden, Sector 51, Gurugram, Haryana 122003. Hours: {A['sentence']}.",
        f"- Also: {clinics.APOLLO_CLINIC['en']['name']}, {clinics.APOLLO_CLINIC['addr']['en']}; and Apollo Hospitals, Golf Course Road",
        "- Appointments and video consultations: call or WhatsApp +91 96671 04882",
        "- Sees adults and teenagers aged 12 and above; consults in English and Hindi",
        "- Treats: acidity and GERD, H. pylori, gastritis and ulcers, swallowing problems, fatty liver, hepatitis B and C, jaundice, cirrhosis, "
        "gallstones and bile duct stones, pancreatitis, pancreatic cysts, IBS, ulcerative colitis and Crohn's disease, constipation, colon polyps",
        "- Procedures: upper GI endoscopy, colonoscopy, endoscopic ultrasound (EUS), ERCP, variceal banding, polyp removal and EMR, "
        "endoscopic control of bleeding, PEG feeding tubes, dilatation and stenting, capsule endoscopy",
        "- Online: https://drlochab.com (English), https://drlochab.com/hi/ (Hindi), Instagram @drlochab, https://www.linkedin.com/in/drlochab/, "
        "https://arcuracare.com/dr-kshitij-lochab/",
        "",
        "Every page below also exists in Hindi at the same path under /hi/ (for example /hi/conditions/fatty-liver/).",
    ]
    for prefix in dict.fromkeys(g for _, g in GROUPS):
        rows = []
        for en, _hi in pairs:
            first = en.strip("/").split("/")[0]
            if dict(GROUPS).get(first) != prefix:
                continue
            title, desc = _meta(out, en)
            rows.append(f"- [{title}]({SITE}{en}): {desc}")
        if rows:
            lines += ["", f"## {prefix}"] + rows
    lines += ["", "## Optional", f"- [Home page]({SITE}/): daily gut-health tip, Myth Buster, symptom checker and Thali meter",
              f"- [Sitemap]({SITE}/sitemap.xml)"]
    return "\n".join(lines) + "\n"
