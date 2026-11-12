"""Question headings for condition and procedure pages (12 Nov 2026).

Search engines and AI answer engines match pages to the questions people ask, so each section heading on a
condition or procedure page is phrased as the question it answers ("What causes fatty liver?"), and the first line
under it answers that question. The names below are the short, everyday forms used inside those questions.
Hindi questions are written so they read correctly whatever the grammatical gender of the name.
Used by build_pages.build(); the build stops if a condition or procedure has no entry.
"""

COND = {  # slug -> (English name inside a question, Hindi name inside a question)
 "acidity-reflux-gerd": ("acidity and reflux (GERD)", "एसिडिटी और रिफ़्लक्स (GERD)"),
 "h-pylori-gastritis-ulcer": ("H. pylori, gastritis and ulcers", "H. pylori, गैस्ट्राइटिस और अल्सर"),
 "swallowing-difficulty": ("difficulty swallowing", "निगलने में तकलीफ़"),
 "fatty-liver": ("fatty liver", "फैटी लिवर"),
 "hepatitis-b-c": ("hepatitis B and C", "हेपेटाइटिस B और C"),
 "jaundice": ("jaundice", "पीलिया"),
 "cirrhosis": ("cirrhosis", "सिरोसिस"),
 "gallstones": ("gallstones and bile duct stones", "पित्त की पथरी"),
 "pancreatitis": ("pancreatitis", "पैंक्रियाटाइटिस"),
 "pancreatic-cysts": ("pancreatic cysts and lumps", "पैंक्रियास की सिस्ट और गाँठ"),
 "ibs-irritable-bowel-syndrome": ("IBS", "IBS"),
 "ulcerative-colitis-crohns-disease": ("ulcerative colitis and Crohn's disease", "अल्सरेटिव कोलाइटिस और क्रोहन बीमारी"),
 "constipation": ("constipation", "कब्ज़"),
 "colon-polyps-colon-cancer": ("colon polyps and colon cancer", "आँत के पॉलिप और आँत का कैंसर"),
}

PROC = {
 "upper-gi-endoscopy": ("an upper GI endoscopy", "अपर GI एंडोस्कोपी"),
 "colonoscopy": ("a colonoscopy", "कोलोनोस्कोपी"),
 "endoscopic-ultrasound-eus": ("an endoscopic ultrasound (EUS)", "एंडोस्कोपिक अल्ट्रासाउंड (EUS)"),
 "ercp": ("an ERCP", "ERCP"),
 "variceal-banding-evl": ("variceal banding", "वैरिसियल बैंडिंग"),
 "polyp-removal-emr": ("polyp removal (EMR)", "पॉलिप निकालने (EMR)"),
 "gi-bleeding-treatment": ("endoscopic bleeding control", "एंडोस्कोपी से खून रोकने"),
 "peg-feeding-tube": ("a feeding tube (PEG)", "फ़ीडिंग ट्यूब (PEG)"),
 "dilatation-stenting": ("dilatation and stenting", "डाइलेटेशन और स्टेंटिंग"),
}

Q = {
 "en": dict(
  symptoms="What are the symptoms of {n}?", causes="What causes {n}?", tests="How is {n} diagnosed?", treat="How is {n} treated?",
  proc_help="Which procedures can help with {n}?", diet="What should you eat with {n}?", when="When should you see a gastroenterologist for {n}?",
  about="How does {n} work?", uses="When is {n} needed?", prep="How do you prepare for {n}?", day="What happens on the day of {n}?",
  expect="What should you expect during {n}?", after="What happens after {n}?", risks="What are the risks of {n}?",
  alarm="When should you get medical help straight away after {n}?", alts="What are the alternatives to {n}?",
  treats="Which conditions is {n} used for?", where="Where can you have {n} in Gurgaon (Gurugram)?"),
 "hi": dict(
  symptoms="{n} के लक्षण क्या हैं?", causes="{n} की वजहें क्या हैं?", tests="{n} की जाँच कैसे होती है?", treat="{n} का इलाज कैसे होता है?",
  proc_help="{n} में कौन-से प्रोसीजर मदद करते हैं?", diet="{n} में क्या खाएँ?", when="{n} में गैस्ट्रोएंटेरोलॉजिस्ट को कब दिखाएँ?",
  about="{n} की प्रक्रिया क्या है?", uses="{n} की ज़रूरत कब पड़ती है?", prep="{n} की तैयारी कैसे करें?", day="{n} वाले दिन क्या होता है?",
  expect="{n} में क्या उम्मीद करें?", after="{n} के बाद क्या होता है?", risks="{n} के जोखिम क्या हैं?",
  alarm="{n} के बाद कब तुरंत डॉक्टर को दिखाएँ?", alts="{n} के अलावा और क्या विकल्प हैं?",
  treats="किन बीमारियों में {n} की ज़रूरत पड़ती है?", where="गुरुग्राम (गुड़गाँव) में {n} कहाँ करवाएँ?"),
}

def q(lang, key, kind, slug):
    names = COND if kind == "cond" else PROC
    n = names[slug][0 if lang == "en" else 1]
    s = Q[lang][key].format(n=n)
    return s[0].upper() + s[1:] if lang == "en" else s

def check(cond_slugs, proc_slugs):
    missing = [s for s in cond_slugs if s not in COND] + [s for s in proc_slugs if s not in PROC]
    assert not missing, f"qheads.py: add question names for {missing}"
