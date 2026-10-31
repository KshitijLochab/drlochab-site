"""Local SEO pages (EN + HI), 18 Oct 2026: 'Gastroenterologist in Gurgaon' landing page and 'About Dr. Kshitij Lochab' profile.
Built by build_pages.build(). Facts here must match the rest of the site (no POEM/ESD; patients aged 12+; Arcura hours)."""
import json

UPD = ("2026-10-18", "18 October 2026", "18 अक्टूबर 2026")
GBP = "https://share.google/9ZndZsg6NHVxeQfYl"
ARCURA = "https://arcuracare.com/dr-kshitij-lochab/"
INSTAGRAM, LINKEDIN = "https://www.instagram.com/drlochab/", "https://www.linkedin.com/in/drlochab/"
SAME_AS = [GBP, INSTAGRAM, LINKEDIN, ARCURA]
HOURS = [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "10:00", "closes": "17:00"},
         {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "09:00", "closes": "13:00"}]
ADDRESS = {"@type": "PostalAddress", "streetAddress": "Arcura Clinic, M2K Corporate Park & Shopping Plaza, 14, Mayfield Garden, Sector 51",
           "addressLocality": "Gurugram", "addressRegion": "Haryana", "postalCode": "122003", "addressCountry": "IN"}

def physician(full=False):
    p = {"@type": "Physician", "@id": "https://drlochab.com/#physician", "name": "Dr. Kshitij Lochab", "url": "https://drlochab.com/",
         "image": "https://drlochab.com/dr-lochab.jpg", "telephone": "+91-9667104882", "medicalSpecialty": "Gastroenterologic",
         "address": ADDRESS, "openingHoursSpecification": HOURS, "areaServed": ["Gurugram", "Gurgaon", "Delhi NCR"],
         "availableLanguage": ["English", "Hindi"], "sameAs": SAME_AS, "hasMap": GBP, "location": [__import__("clinics").location_ld()]}
    if full:
        p.update({"description": "Consultant gastroenterologist and therapeutic endoscopist in Gurgaon (Gurugram), trained in endoscopic ultrasound (EUS) and ERCP.",
                  "award": "All-India Gold Medal, DrNB Gastroenterology",
                  "alumniOf": [{"@type": "CollegeOrUniversity", "name": "Armed Forces Medical College, Pune"},
                               {"@type": "CollegeOrUniversity", "name": "Medical College Baroda"},
                               {"@type": "Hospital", "name": "Medanta – The Medicity, Gurugram"}]})
    return p

EN = dict(
 local=dict(slug="gastroenterologist-in-gurgaon",
  title="Gastroenterologist in Gurgaon (Gurugram) | Dr. Kshitij Lochab",
  h1="Gastroenterologist in Gurgaon: Dr. Kshitij Lochab",
  eyebrow="Gurgaon (Gurugram) · Sector 51",
  desc="Consult Dr. Kshitij Lochab, gastroenterologist and therapeutic endoscopist in Gurgaon (Gurugram), at Arcura Clinic, Sector 51: timings, address, conditions treated, endoscopy, EUS and ERCP.",
  lead="Dr. Kshitij Lochab is a consultant gastroenterologist and therapeutic endoscopist in Gurgaon (Gurugram). He treats problems of the food pipe, stomach, intestines, liver, gallbladder and pancreas in adults and teenagers aged 12 and above, in English and Hindi. People most often come for acidity and heartburn, gas and bloating, constipation or loose motions, fatty liver, jaundice, and for endoscopy, colonoscopy, EUS or ERCP.",
  clinic_h="Clinic and timings",
  clinic=["Arcura Clinic, M2K Corporate Park & Shopping Plaza, 14, Mayfield Garden, Sector 51, Gurugram (Gurgaon), Haryana 122003. Near Sohna Road and Nirvana Country.",
          "Also consulting at Apollo Hospitals, Golf Course Road, Gurugram."],
  hours_h="Arcura Clinic hours", hours=__import__("clinics").ARCURA["en"]["hours"],
  book="Appointments and video consultations: call or WhatsApp +91 96671 04882.", wa="Book on WhatsApp", dir="Get directions",
  treat_h="Conditions treated", proc_h="Endoscopy and procedures",
  proc_p="Procedures are done in a fully equipped hospital endoscopy unit with monitoring and anaesthesia support.",
  when_h="When to see a gastroenterologist",
  when=["Acidity or indigestion that keeps coming back, or needs tablets every day", "Difficulty swallowing, vomiting or weight loss without trying",
        "Blood in the stool, black stools or a change in bowel habit lasting more than three weeks", "Yellow eyes, raised liver enzymes or fatty liver with diabetes",
        "Long-lasting loose motions, constipation, bloating or belly pain", "Gallstones, pancreatitis or a scan finding that needs explaining"],
  urgent="Vomiting blood, black and tarry stools, severe belly pain or confusion in liver disease are emergencies: call 112 or go to the nearest emergency department.",
  visit_h="Before your visit", visit=["Bring all previous reports, scans, endoscopy and biopsy reports", "Bring a list of every medicine and supplement you take", "No fasting is needed for a consultation"],
  faqs=[["What are the clinic timings?", "Arcura Clinic, Sector 51, Gurugram: Monday to Saturday 10 am to 5 pm, and Sunday 9 am to 1 pm. Call or WhatsApp to book a time."],
        ["Do you offer video consultations?", "Yes, for follow-ups, reviewing reports and diet advice. A first visit for new symptoms is better in person, so that you can be examined."],
        ["Do you see children?", "Teenagers aged 12 and above, and adults. Babies and younger children should first see their paediatrician."],
        ["Do I need a referral?", "No. You can book directly. Bring any notes from doctors you have already seen."]],
 ),
 about=dict(slug="about-dr-kshitij-lochab",
  title="About Dr. Kshitij Lochab | Gastroenterologist in Gurgaon",
  h1="Dr. Kshitij Lochab",
  eyebrow="About",
  role="Consultant Gastroenterologist & Therapeutic Endoscopist, Gurgaon (Gurugram)",
  desc="Dr. Kshitij Lochab: DrNB Gastroenterology (Medanta, All-India Gold Medal), Advanced Fellowship in EUS and ERCP, consultant gastroenterologist in Gurgaon. Qualifications, experience, research and how to book.",
  lead="I treat diseases of the food pipe, stomach, intestines, liver, gallbladder and pancreas. My special training is in advanced endoscopy, including endoscopic ultrasound (EUS) and ERCP, which lets many problems that once needed surgery be treated through a scope. I take time to explain your condition and your options, so that every decision is one we make together.",
  q_h="Training and qualifications",
  q_sum="MBBS · MD Internal Medicine · DrNB Gastroenterology (All-India Gold Medal) · Advanced Fellowship in EUS & ERCP",
  q=[("2018", "MBBS", "Armed Forces Medical College (AFMC), Pune",
      "Founded in 1948, AFMC trains doctors for the Army, Navy and Air Force. Each year about 2,000 candidates are shortlisted from the national NEET merit list for around 150 places, through a written test, interview and medical examination."),
     ("2022", "MD Internal Medicine", "Medical College Baroda",
      "Established in 1949 under the Maharaja Sayajirao University of Baroda and attached to Sir Sayajirao General Hospital, a major public teaching hospital in Gujarat. Training as a physician first means digestive problems are seen alongside diabetes, heart, kidney and other conditions."),
     ("2022", "Senior Residency, Internal Medicine", "Lady Hardinge Medical College, New Delhi", ""),
     ("2026", "DrNB Gastroenterology, All-India Gold Medal", "Medanta – The Medicity, Gurugram",
      "Trained at the Institute of Digestive & Hepatobiliary Sciences, led by Padma Shri awardee Dr Randhir Sud."),
     ("2026", "Advanced Fellowship in EUS and ERCP", "Under Dr Malay Sharma",
      "Dedicated training in endoscopic ultrasound and ERCP, used for bile duct, pancreas and gallbladder problems, and for many conditions that once needed surgery.")],
  x_h="Experience",
  x=[("2026", "Associate Consultant, Gastroenterology, Medanta – The Medicity, Gurugram"),
     ("Now", "Consultant Gastroenterologist, Arcura Clinic, Sector 51, Gurugram"),
     ("Now", "Consultant Gastroenterologist, Apollo Clinic, Sector 52, Gurugram"),
     ("Now", "Associate Consultant, Gastroenterology & Therapeutic Endoscopy, Apollo Hospitals, Golf Course Road, Gurugram")],
  care_h="Areas of care", care=["Fatty liver and hepatitis", "Cirrhosis and GI bleeding", "Bile duct and pancreas", "Acidity and ulcers", "IBS and IBD", "Colon polyps and screening", "Swallowing problems", "Gut and liver care in pregnancy"],
  proc_h="Procedures",
  res_h="Research", res="Work presented at the World Congress of Gastroenterology 2026, on bleeding after variceal banding, EUS-guided procedures, restoring the passage in complete oesophageal strictures, and closing a gastro-colic fistula through the endoscope.",
  reg_h="Registration", reg="Haryana Medical Council, Reg. No. HN-23524",
  lang_h="Languages", langs="English and Hindi. Sees adults and teenagers aged 12 and above.",
  faqs=[["Where does Dr. Kshitij Lochab consult?", "At Arcura Clinic, Mayfield Garden, Sector 51, Gurugram (Monday to Saturday 10 am to 5 pm, Sunday 9 am to 1 pm), and at Apollo Hospitals, Golf Course Road, Gurugram."],
        ["What is Dr. Lochab's specialisation?", "Gastroenterology and therapeutic endoscopy, with advanced training in endoscopic ultrasound (EUS) and ERCP for bile duct and pancreas problems."],
        ["How can I book an appointment?", "Call or WhatsApp +91 96671 04882. Video consultations are available for follow-ups and report reviews."]],
 ),
 links=("About Dr. Lochab", "Gastroenterologist in Gurgaon"),
 more_about="Read the full profile", more_local="Clinic timings and details",
)

HI = dict(
 local=dict(
  title="गुड़गाँव (गुरुग्राम) में गैस्ट्रोएंटेरोलॉजिस्ट | डॉ. क्षितिज लोचब",
  h1="गुड़गाँव में पेट और लिवर रोग विशेषज्ञ: डॉ. क्षितिज लोचब",
  eyebrow="गुड़गाँव (गुरुग्राम) · सेक्टर 51",
  desc="गुड़गाँव (गुरुग्राम) में गैस्ट्रोएंटेरोलॉजिस्ट डॉ. क्षितिज लोचब से आर्क्योरा क्लिनिक, सेक्टर 51 में मिलें: समय, पता, किन बीमारियों का इलाज, एंडोस्कोपी, EUS और ERCP।",
  lead="डॉ. क्षितिज लोचब गुड़गाँव (गुरुग्राम) में कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट हैं। वे खाने की नली, पेट, आँतों, लिवर, पित्ताशय और पैंक्रियास की बीमारियों का इलाज करते हैं, बड़ों और 12 साल से बड़े किशोरों का, हिंदी और अंग्रेज़ी में। लोग सबसे ज़्यादा एसिडिटी और सीने में जलन, गैस और पेट फूलना, कब्ज़ या दस्त, फैटी लिवर, पीलिया, और एंडोस्कोपी, कोलोनोस्कोपी, EUS या ERCP के लिए आते हैं।",
  clinic_h="क्लिनिक और समय",
  clinic=["आर्क्योरा क्लिनिक, M2K कॉर्पोरेट पार्क एंड शॉपिंग प्लाज़ा, 14, मेफ़ील्ड गार्डन, सेक्टर 51, गुरुग्राम (गुड़गाँव), हरियाणा 122003। सोहना रोड और निर्वाणा कंट्री के पास।",
          "अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम में भी परामर्श।"],
  hours_h="आर्क्योरा क्लिनिक का समय", hours=__import__("clinics").ARCURA["hi"]["hours"],
  book="अपॉइंटमेंट और वीडियो परामर्श: +91 96671 04882 पर कॉल या WhatsApp करें।", wa="WhatsApp पर अपॉइंटमेंट", dir="रास्ता देखें",
  treat_h="किन बीमारियों का इलाज", proc_h="एंडोस्कोपी और प्रोसीजर",
  proc_p="प्रोसीजर मॉनिटरिंग और एनेस्थीसिया सुविधा वाली पूरी तरह सुसज्जित अस्पताल की एंडोस्कोपी यूनिट में होते हैं।",
  when_h="गैस्ट्रोएंटेरोलॉजिस्ट को कब दिखाएँ",
  when=["बार-बार लौटने वाली एसिडिटी या अपच, या रोज़ गोली की ज़रूरत", "निगलने में दिक़्क़त, उल्टी या बिना कोशिश वज़न घटना",
        "मल में ख़ून, काला मल या तीन हफ़्ते से ज़्यादा मल की आदत में बदलाव", "आँखें पीली, बढ़े लिवर एंज़ाइम या डायबिटीज़ के साथ फ़ैटी लिवर",
        "लंबे दस्त, क़ब्ज़, पेट फूलना या पेट दर्द", "पित्त की पथरी, पैंक्रियाटाइटिस या स्कैन की कोई बात जिसे समझना हो"],
  urgent="ख़ून की उल्टी, काला तारकोल जैसा मल, पेट में तेज़ दर्द या लिवर की बीमारी में बेहोशी जैसा लगना इमरजेंसी है: 112 पर कॉल करें या नज़दीकी इमरजेंसी में जाएँ।",
  visit_h="आने से पहले", visit=["पुरानी सभी रिपोर्ट, स्कैन, एंडोस्कोपी और बायोप्सी रिपोर्ट लाएँ", "हर दवा और सप्लीमेंट की सूची लाएँ", "परामर्श के लिए भूखे रहने की ज़रूरत नहीं"],
  faqs=[["क्लिनिक का समय क्या है?", "आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम: सोमवार से शनिवार सुबह 10 से शाम 5 बजे, और रविवार सुबह 9 से दोपहर 1 बजे। समय तय करने के लिए कॉल या WhatsApp करें।"],
        ["क्या वीडियो परामर्श होता है?", "हाँ, फ़ॉलो-अप, रिपोर्ट देखने और डाइट सलाह के लिए। नए लक्षणों में पहली बार आमने-सामने दिखाना बेहतर है, ताकि जाँच हो सके।"],
        ["क्या आप बच्चों को देखते हैं?", "12 साल और उससे बड़े किशोरों और बड़ों को। शिशु और छोटे बच्चे पहले अपने बाल रोग विशेषज्ञ को दिखाएँ।"],
        ["क्या रेफ़रल चाहिए?", "नहीं। आप सीधे अपॉइंटमेंट ले सकते हैं। जिन डॉक्टरों को पहले दिखाया है उनके नोट्स साथ लाएँ।"]],
 ),
 about=dict(
  title="डॉ. क्षितिज लोचब के बारे में | गुड़गाँव में गैस्ट्रोएंटेरोलॉजिस्ट",
  h1="डॉ. क्षितिज लोचब",
  eyebrow="परिचय",
  role="कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट, गुड़गाँव (गुरुग्राम)",
  desc="डॉ. क्षितिज लोचब: DrNB गैस्ट्रोएंटेरोलॉजी (मेदांता, ऑल-इंडिया गोल्ड मेडल), EUS और ERCP में एडवांस्ड फ़ेलोशिप, गुड़गाँव में कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट। योग्यता, अनुभव, शोध और अपॉइंटमेंट।",
  lead="मैं खाने की नली, पेट, आँतों, लिवर, पित्ताशय और पैंक्रियास की बीमारियों का इलाज करता हूँ। मेरी ख़ास ट्रेनिंग एडवांस्ड एंडोस्कोपी में है, जिसमें एंडोस्कोपिक अल्ट्रासाउंड (EUS) और ERCP शामिल हैं, जिनसे कई समस्याएँ जिनमें पहले ऑपरेशन लगता था, अब दूरबीन से ठीक हो जाती हैं। मैं आपकी बीमारी और विकल्प समझाने में समय लेता हूँ, ताकि हर फ़ैसला हम साथ मिलकर लें।",
  q_h="ट्रेनिंग और योग्यता",
  q_sum="MBBS · MD इंटरनल मेडिसिन · DrNB गैस्ट्रोएंटेरोलॉजी (ऑल-इंडिया गोल्ड मेडल) · EUS और ERCP में एडवांस्ड फ़ेलोशिप",
  q=[("2018", "MBBS", "आर्म्ड फ़ोर्सेज़ मेडिकल कॉलेज (AFMC), पुणे",
      "1948 में स्थापित AFMC थल सेना, नौसेना और वायु सेना के लिए डॉक्टर तैयार करता है। हर साल राष्ट्रीय NEET मेरिट सूची से करीब 2,000 उम्मीदवार चुने जाते हैं, और लिखित परीक्षा, इंटरव्यू और मेडिकल जाँच के बाद लगभग 150 सीटें भरी जाती हैं।"),
     ("2022", "MD इंटरनल मेडिसिन", "मेडिकल कॉलेज बड़ौदा",
      "1949 में महाराजा सयाजीराव यूनिवर्सिटी ऑफ़ बड़ौदा के तहत स्थापित, और गुजरात के बड़े सरकारी टीचिंग अस्पताल, सर सयाजीराव जनरल अस्पताल से जुड़ा। पहले फ़िज़िशियन की ट्रेनिंग का मतलब है कि पेट की बीमारी को डायबिटीज़, दिल, किडनी और दूसरी बीमारियों के साथ जोड़कर देखा जाता है।"),
     ("2022", "सीनियर रेज़िडेंसी, इंटरनल मेडिसिन", "लेडी हार्डिंग मेडिकल कॉलेज, नई दिल्ली", ""),
     ("2026", "DrNB गैस्ट्रोएंटेरोलॉजी, ऑल-इंडिया गोल्ड मेडल", "मेदांता – द मेडिसिटी, गुरुग्राम",
      "इंस्टिट्यूट ऑफ़ डाइजेस्टिव एंड हेपेटोबिलियरी साइंसेज़ में ट्रेनिंग, जिसका नेतृत्व पद्म श्री से सम्मानित डॉ. रणधीर सूद करते हैं।"),
     ("2026", "EUS और ERCP में एडवांस्ड फ़ेलोशिप", "डॉ. मलय शर्मा के मार्गदर्शन में",
      "एंडोस्कोपिक अल्ट्रासाउंड और ERCP की विशेष ट्रेनिंग, जो पित्त की नली, पैंक्रियास और पित्ताशय की समस्याओं में, और कई ऐसी बीमारियों में काम आती है जिनमें पहले ऑपरेशन करना पड़ता था।")],
  x_h="अनुभव",
  x=[("2026", "एसोसिएट कंसल्टेंट, गैस्ट्रोएंटेरोलॉजी, मेदांता – द मेडिसिटी, गुरुग्राम"),
     ("अभी", "कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट, आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम"),
     ("अभी", "कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट, अपोलो क्लिनिक, सेक्टर 52, गुरुग्राम"),
     ("अभी", "एसोसिएट कंसल्टेंट, गैस्ट्रोएंटेरोलॉजी और थेराप्यूटिक एंडोस्कोपी, अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम")],
  care_h="इलाज के क्षेत्र", care=["फ़ैटी लिवर और हेपेटाइटिस", "सिरोसिस और GI ब्लीडिंग", "पित्त की नली और पैंक्रियास", "एसिडिटी और अल्सर", "IBS और IBD", "आँत के पॉलिप और स्क्रीनिंग", "निगलने की समस्याएँ", "गर्भावस्था में पेट और लिवर की देखभाल"],
  proc_h="प्रोसीजर",
  res_h="शोध", res="वर्ल्ड कांग्रेस ऑफ़ गैस्ट्रोएंटेरोलॉजी 2026 में प्रस्तुत काम: वैरिसियल बैंडिंग के बाद ब्लीडिंग, EUS-गाइडेड प्रोसीजर, खाने की नली के पूरी तरह बंद होने पर रास्ता खोलना, और एंडोस्कोप से गैस्ट्रो-कोलिक फ़िस्टुला बंद करना।",
  reg_h="रजिस्ट्रेशन", reg="हरियाणा मेडिकल काउंसिल, रजि. नं. HN-23524",
  lang_h="भाषाएँ", langs="हिंदी और अंग्रेज़ी। बड़ों और 12 साल से बड़े किशोरों को देखते हैं।",
  faqs=[["डॉ. क्षितिज लोचब कहाँ परामर्श देते हैं?", "आर्क्योरा क्लिनिक, मेफ़ील्ड गार्डन, सेक्टर 51, गुरुग्राम में (सोमवार से शनिवार सुबह 10 से शाम 5, रविवार सुबह 9 से दोपहर 1), और अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम में।"],
        ["डॉ. लोचब की विशेषज्ञता क्या है?", "गैस्ट्रोएंटेरोलॉजी और थेराप्यूटिक एंडोस्कोपी, पित्त की नली और पैंक्रियास की समस्याओं के लिए एंडोस्कोपिक अल्ट्रासाउंड (EUS) और ERCP में एडवांस्ड ट्रेनिंग के साथ।"],
        ["अपॉइंटमेंट कैसे लें?", "+91 96671 04882 पर कॉल या WhatsApp करें। फ़ॉलो-अप और रिपोर्ट देखने के लिए वीडियो परामर्श उपलब्ध है।"]],
 ),
 links=("डॉ. लोचब के बारे में", "गुड़गाँव में गैस्ट्रोएंटेरोलॉजिस्ट"),
 more_about="पूरा परिचय पढ़ें", more_local="क्लिनिक का समय और जानकारी",
)
for k in ("local", "about"):
    HI[k]["slug"] = EN[k]["slug"]

CSS = """
.lp-qsum{font-weight:600;color:var(--accent);margin:0 0 14px}
.lp-q{display:grid;gap:12px}
.lp-qc{display:grid;gap:3px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 16px}
.lp-qc b{font-size:1.02rem}.lp-qy{font-size:.75rem;font-weight:700;letter-spacing:.1em;color:var(--muted)}
.lp-qp{color:var(--accent);font-weight:600;font-size:.95rem}.lp-qc p{margin:4px 0 0;font-size:.92rem;color:var(--muted);line-height:1.5}
.lp-hours{display:grid;grid-template-columns:auto 1fr;gap:8px 20px;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px 20px;margin:8px 0 14px;max-width:460px}
.lp-hours dt{font-weight:700}.lp-hours dd{margin:0}
.lp-act{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}
.lp-tl{list-style:none;padding:0;margin:0}
.lp-tl li{display:grid;grid-template-columns:64px 1fr;gap:12px;padding:10px 0;border-bottom:1px solid var(--line)}
.lp-tl b{color:var(--accent)}
.lp-head{display:grid;grid-template-columns:160px 1fr;gap:22px;align-items:center;margin:8px 0 18px}
.lp-head img{width:160px;height:200px;object-fit:cover;border-radius:18px}
.lp-role{font-size:1.05rem;color:var(--muted);margin:0}
.lp-tags{display:flex;flex-wrap:wrap;gap:8px}.lp-tags span{background:var(--accent-soft);border-radius:999px;padding:6px 12px;font-size:.9rem}
@media (max-width:560px){.lp-head{grid-template-columns:110px 1fr}.lp-head img{width:110px;height:138px}}
"""

ONLINE = {"en": ("Find me online", "Instagram @drlochab: gut-health tips", "LinkedIn", "Profile on Arcura Clinic", "Google Business Profile and reviews"),
          "hi": ("ऑनलाइन यहाँ मिलें", "Instagram @drlochab: पेट की सेहत की सलाह", "LinkedIn", "आर्क्योरा क्लिनिक पर प्रोफ़ाइल", "Google बिज़नेस प्रोफ़ाइल और रिव्यू")}

def render(lang, bp, kind, conds, procs):
    """kind: 'local' or 'about'. conds/procs: lists of (url, name) in the page language."""
    import clinics, copy
    X = copy.deepcopy((EN if lang == "en" else HI)[kind]); e = bp.e; t = bp.L[lang]
    A = clinics.APOLLO_CLINIC[lang]
    when2 = "; ".join(f"{d}, {h}" for d, h in A["hours"])
    X["faqs"][0][1] += (f" Also at {A['line']}: {when2}." if lang == "en" else f" {A['line']} में भी: {when2}।")
    path, path_en, path_hi = f"{bp.pre(lang)}{X['slug']}/", f"/{X['slug']}/", f"/hi/{X['slug']}/"
    sec = lambda h, inner: f"<section><h2>{e(h)}</h2>{inner}</section>"
    if kind == "local":
        hours = '<dl class="lp-hours">' + "".join(f"<dt>{e(d)}</dt><dd>{e(h)}</dd>" for d, h in X["hours"]) + "</dl>"
        body = (f'<p class="lead">{e(X["lead"])}</p>'
                + sec(X["clinic_h"], "".join(f"<p>{e(p)}</p>" for p in X["clinic"]) + f'<h3>{e(X["hours_h"])}</h3>{hours}<p>{e(X["book"])}</p>'
                      + f'<h3>{e(A["name"])}</h3><p>{e(clinics.APOLLO_CLINIC["addr"][lang])}</p><dl class="lp-hours">' + "".join(f"<dt>{e(d)}</dt><dd>{e(h)}</dd>" for d, h in A["hours"]) + f'</dl><p>{e(A["book"])}</p>'
                      f'<div class="lp-act"><a class="btn btn-solid btn-sm" href="{bp.WA}" target="_blank" rel="noopener">{e(X["wa"])}</a>'
                      f'<a class="btn btn-ghost btn-sm" href="{GBP}" target="_blank" rel="noopener">{"Directions to Arcura Clinic" if lang == "en" else "आर्क्योरा क्लिनिक का रास्ता"}</a>'
                      f'<a class="btn btn-ghost btn-sm" href="{clinics.APOLLO_CLINIC["map"]}" target="_blank" rel="noopener">{e(A["dir"])}</a>'
                      f'<a class="btn btn-ghost btn-sm" href="{ARCURA}" target="_blank" rel="noopener">{e(ONLINE[lang][3])}</a></div>')
                + sec(X["treat_h"], bp.links(conds))
                + sec(X["proc_h"], f'<p>{e(X["proc_p"])}</p>' + bp.links(procs))
                + f'<section class="see"><h2>{e(X["when_h"])}</h2>{bp.ul(X["when"])}<p>{e(X["urgent"])}</p></section>'
                + sec(X["visit_h"], bp.ul(X["visit"]))
                + bp.faq_html(lang, X["faqs"]))
        graph = [dict(physician(), **{"@type": ["Physician", "MedicalClinic"]})]
    else:
        tl = lambda items: '<ul class="lp-tl">' + "".join(f"<li><b>{e(y)}</b><span>{e(v)}</span></li>" for y, v in items) + "</ul>"
        body = (f'<div class="lp-head"><img src="/dr-lochab.jpg" alt="{e(X["h1"])}" width="160" height="200"><div><p class="lp-role">{e(X["role"])}</p></div></div>'
                f'<p class="lead">{e(X["lead"])}</p>'
                + sec(X["q_h"], f'<p class="lp-qsum">{e(X["q_sum"])}</p><div class="lp-q">' + "".join(
                      f'<div class="lp-qc"><span class="lp-qy">{e(y)}</span><b>{e(d)}</b><span class="lp-qp">{e(pl)}</span>' + (f'<p>{e(c)}</p>' if c else "") + "</div>"
                      for y, d, pl, c in X["q"]) + "</div>") + sec(X["x_h"], tl(X["x"]))
                + sec(X["care_h"], '<div class="lp-tags">' + "".join(f"<span>{e(c)}</span>" for c in X["care"]) + "</div>")
                + sec(X["proc_h"], bp.links(procs))
                + sec(X["res_h"], f"<p>{e(X['res'])}</p>")
                + sec(X["reg_h"], f"<p>{e(X['reg'])}</p>") + sec(X["lang_h"], f"<p>{e(X['langs'])}</p>")
                + sec(ONLINE[lang][0], '<div class="links">' + "".join(f'<a href="{u}" target="_blank" rel="noopener">{e(n)} <span aria-hidden="true">→</span></a>' for u, n in zip((INSTAGRAM, LINKEDIN, ARCURA, GBP), ONLINE[lang][1:])) + "</div>")
                + bp.faq_html(lang, X["faqs"]))
        graph = [{"@type": "ProfilePage", "url": bp.SITE + path, "name": X["title"], "inLanguage": lang, "dateCreated": UPD[0] + "T09:00:00+05:30", "dateModified": UPD[0] + "T09:00:00+05:30", "mainEntity": {"@id": "https://drlochab.com/#physician"}},
                 physician(full=True)]
    ld = {"@context": "https://schema.org", "@graph": graph + [
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": t["home"], "item": bp.SITE + bp.pre(lang)},
                                                       {"@type": "ListItem", "position": 2, "name": X["h1"], "item": bp.SITE + path}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in X["faqs"]]}]}
    head = bp.head(lang, X["title"], X["desc"], path_en, path_hi, ld).replace("</head>", f"<style>{CSS}</style></head>", 1)
    crumbs = f'<nav class="crumbs" aria-label="Breadcrumb"><a href="{bp.pre(lang)}">{e(t["home"])}</a><span>›</span><span aria-current="page">{e(X["h1"])}</span></nav>'
    html = (head + bp.header(lang, path_hi if lang == "en" else path_en)
            + f'<main class="wrap grid"><article>{crumbs}<p class="eyebrow">{e(X["eyebrow"])}</p><h1>{e(X["h1"])}</h1>{bp.byline(lang, UPD)}' + body
            + f"</article>{bp.aside(lang)}</main>" + bp.footer(lang))
    return path, path_en, path_hi, html
