"""Hindi version of drlochab.com. build_site.py applies these to the English source to make /hi/index.html.
Every English string listed here must exist in the source; the build stops if one is missing,
so text changed on the English page is never silently left untranslated."""

# Exact text replacements for page markup, interface strings and illustration labels.
PAIRS = [
 # header
 ('<span class="brand-sub">Gastroenterology · Liver · Endoscopy</span>', '<span class="brand-sub">पेट · लिवर · एंडोस्कोपी</span>'),
 ('<a href="#daily">Daily tips</a>', '<a href="#daily">रोज़ की सलाह</a>'),
 ('<a href="#symptoms">Symptoms</a>', '<a href="#symptoms">लक्षण</a>'),
 ('<a href="#conditions">Conditions</a>', '<a href="#conditions">बीमारियाँ</a>'),
 ('<a href="#procedures">Procedures</a>', '<a href="#procedures">जाँच और इलाज</a>'),
 ('<a href="#about">About</a>', '<a href="#about">डॉक्टर के बारे में</a>'),
 ('href="#visit">Book a visit</a>', 'href="#visit">अपॉइंटमेंट</a>'),
 ('<a class="lang" href="/hi/" lang="hi" hreflang="hi" aria-label="यह पेज हिंदी में पढ़ें">हिंदी</a>',
  '<a class="lang" href="/" lang="en" hreflang="en" aria-label="Read this page in English">English</a>'),

 # hero
 ('<p class="eyebrow">Gastroenterologist · Gurgaon (Gurugram)</p>', '<p class="eyebrow">गैस्ट्रोएंटेरोलॉजिस्ट · गुरुग्राम (गुड़गाँव)</p>'),
 ('<h1>Clear answers about your <em>stomach, liver and digestion.</em></h1>', '<h1>आपके <em>पेट, लिवर और पाचन</em> से जुड़े सवालों के सीधे जवाब।</h1>'),
 ('<p class="lede">Many gut and liver problems are easy to treat when they are caught early, and many others are harmless once properly checked. This page explains the common ones in plain language, so you know what to watch for and when to see a specialist.</p>',
  '<p class="lede">पेट और लिवर की कई बीमारियाँ समय पर पकड़ में आ जाएँ तो आसानी से ठीक हो जाती हैं, और कई तकलीफ़ें ठीक से जाँच के बाद मामूली निकलती हैं। यहाँ आम बीमारियों को आसान भाषा में समझाया गया है, ताकि आप जान सकें कि किन बातों पर ध्यान दें और विशेषज्ञ को कब दिखाएँ।</p>'),
 ('rel="noopener">WhatsApp to book</a>', 'rel="noopener">WhatsApp पर अपॉइंटमेंट</a>'),
 ('<a class="btn btn-ghost" href="#symptoms">Check a symptom</a>', '<a class="btn btn-ghost" href="#symptoms">लक्षण देखें</a>'),
 ('<span>DrNB Gastroenterology, Medanta</span>', '<span>DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता</span>'),
 ('<span>All-India Gold Medal</span>', '<span>ऑल-इंडिया गोल्ड मेडल</span>'),
 ('<span>Advanced Fellowship in EUS &amp; ERCP</span>', '<span>EUS और ERCP में एडवांस्ड फ़ेलोशिप</span>'),
 ('src="dr-lochab.jpg" alt="Dr. Kshitij Lochab in a white doctor\'s coat"', 'src="../dr-lochab.jpg" alt="सफ़ेद कोट में डॉ. क्षितिज लोचब"'),
 ('<figcaption><b>Dr. Kshitij Lochab</b><span>Haryana Medical Council Reg. No. HN-23524</span></figcaption>',
  '<figcaption><b>डॉ. क्षितिज लोचब</b><span>हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524</span></figcaption>'),

 # red flags
 ('<span class="pill pill-urgent">Do not wait</span>', '<span class="pill pill-urgent">देर न करें</span>'),
 ('<h2 id="rf-h">Get medical care today if you have</h2>', '<h2 id="rf-h">इनमें से कुछ भी हो तो आज ही डॉक्टर को दिखाएँ</h2>'),
 ('<p class="note">In an emergency, call <strong>112</strong> or go to the nearest hospital emergency department.</p>',
  '<p class="note">इमरजेंसी में <strong>112</strong> पर कॉल करें या सबसे पास के अस्पताल की इमरजेंसी में जाएँ।</p>'),
 ('<li>Vomiting of blood or coffee-ground material</li>', '<li>उल्टी में खून या कॉफ़ी जैसा काला पदार्थ</li>'),
 ('<li>Black, sticky, tar-like stools</li>', '<li>काला, चिपचिपा, तारकोल जैसा मल</li>'),
 ('<li>Yellow eyes with fever, confusion or drowsiness</li>', '<li>पीली आँखों के साथ बुखार, बेहोशी जैसा लगना या ज़्यादा नींद</li>'),
 ('<li>Sudden, severe belly pain with vomiting</li>', '<li>अचानक तेज़ पेट दर्द के साथ उल्टी</li>'),
 ('<li>Food stuck in the chest, unable to swallow saliva</li>', '<li>खाना छाती में अटक जाए, थूक भी न निगल पाएँ</li>'),
 ('<li>Heavy bleeding from the back passage</li>', '<li>मल द्वार से ज़्यादा खून आना</li>'),

 # daily
 ('<p class="eyebrow">Gut Health Daily</p>', '<p class="eyebrow">रोज़ की सेहत सलाह</p>'),
 ('<h2>One small habit for a healthier gut, every day</h2>', '<h2>हर दिन एक छोटी आदत, स्वस्थ पेट के लिए</h2>'),
 ('<p class="lede">A new tip each morning on diet, digestion and liver health, written for everyday Indian kitchens and routines, plus a daily tip for people living with IBS. Share the ones you find useful with your family.</p>',
  '<p class="lede">हर सुबह खान-पान, पाचन और लिवर की सेहत पर एक नई सलाह, हमारी रोज़ की रसोई और दिनचर्या को ध्यान में रखकर। साथ में IBS वाले लोगों के लिए अलग से रोज़ की सलाह। जो काम की लगे, उसे परिवार के साथ ज़रूर शेयर करें।</p>'),
 ('aria-label="Gut Health Daily">', 'aria-label="रोज़ की सेहत सलाह">'),
 ('aria-selected="true">Today\'s tip</button>', 'aria-selected="true">आज की सलाह</button>'),
 ('tabindex="-1">Diet guides</button>', 'tabindex="-1">डाइट गाइड</button>'),
 ('tabindex="-1">Past tips</button>', 'tabindex="-1">पुरानी सलाह</button>'),
 ('<p class="small">Loading today\'s tip…</p>', '<p class="small">आज की सलाह लोड हो रही है…</p>'),
 ('<span class="ibs-badge">IBS Corner</span><span class="small" id="ibs-h">A daily tip for people living with IBS</span>',
  '<span class="ibs-badge">IBS कॉर्नर</span><span class="small" id="ibs-h">IBS वाले लोगों के लिए रोज़ की सलाह</span>'),
 ('<p class="small">Loading…</p>', '<p class="small">लोड हो रहा है…</p>'),
 ('aria-label="Choose a diet guide"', 'aria-label="डाइट गाइड चुनें"'),
 ('These are general guides. Your own diet may need changes based on your reports, other conditions and medicines.',
  'ये सामान्य गाइड हैं। आपकी रिपोर्ट, दूसरी बीमारियों और दवाइयों के हिसाब से आपकी डाइट में बदलाव की ज़रूरत हो सकती है।'),
 ('aria-label="Choose which tips to show"', 'aria-label="कौन-सी सलाह देखनी है चुनें"'),
 ('aria-pressed="true">Gut health tips</button>', 'aria-pressed="true">पेट की सेहत की सलाह</button>'),
 ('aria-pressed="false">IBS tips</button>', 'aria-pressed="false">IBS की सलाह</button>'),

 # symptoms
 ('<p class="eyebrow">Symptom guide</p>', '<p class="eyebrow">लक्षण गाइड</p>'),
 ('<h2>What is my body telling me?</h2>', '<h2>मेरा शरीर मुझे क्या बता रहा है?</h2>'),
 ('<p class="lede">Tap a symptom to see what commonly causes it and how soon you should see a doctor. This is a guide to help you decide, not a diagnosis.</p>',
  '<p class="lede">किसी लक्षण पर टैप करें और देखें कि आम तौर पर इसकी वजह क्या होती है और डॉक्टर को कितनी जल्दी दिखाना चाहिए। यह फ़ैसला लेने में मदद के लिए है, यह बीमारी की जाँच (डायग्नोसिस) नहीं है।</p>'),
 ('aria-label="Symptoms"', 'aria-label="लक्षण"'),
 ('</i>Routine visit</span>', '</i>आम दिनों में दिखाएँ</span>'),
 ('</i>Within a few days</span>', '</i>कुछ दिनों के अंदर</span>'),
 ('</i>Today</span>', '</i>आज ही</span>'),

 # conditions
 ('<p class="eyebrow">Conditions explained</p>', '<p class="eyebrow">बीमारियों की जानकारी</p>'),
 ('<h2>Explore your digestive system</h2>', '<h2>अपने पाचन तंत्र को जानें</h2>'),
 ('<p class="lede">Choose a part of the body to see its common problems, the questions patients ask, and the tests that help.</p>',
  '<p class="lede">शरीर का कोई हिस्सा चुनें और देखें उसकी आम समस्याएँ, मरीज़ों के सवाल, और कौन-सी जाँचें मदद करती हैं।</p>'),

 # procedures
 ('<p class="eyebrow">Tests &amp; procedures</p>', '<p class="eyebrow">जाँच और इलाज</p>'),
 ('<h2>What to expect from an endoscopy</h2>', '<h2>एंडोस्कोपी में क्या होता है</h2>'),
 ('<p class="lede">Most procedures use a thin, flexible tube with a camera. There are no cuts, and most people go home the same day. Tap any one to see how it works.</p>',
  '<p class="lede">ज़्यादातर प्रोसीजर में कैमरे वाली एक पतली, मुड़ने वाली नली इस्तेमाल होती है। कोई चीरा नहीं लगता, और ज़्यादातर लोग उसी दिन घर चले जाते हैं। कैसे होता है, यह देखने के लिए किसी पर भी टैप करें।</p>'),

 # myths

 # about
 ('<h2>Dr. Kshitij Lochab<span>Consultant Gastroenterologist &amp; Therapeutic Endoscopist</span></h2>',
  '<h2>डॉ. क्षितिज लोचब<span>कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट</span></h2>'),
 ('<p class="lede">I treat diseases of the food pipe, stomach, intestines, liver, gallbladder and pancreas. My special training is in advanced endoscopy, which lets many problems that once needed surgery be treated through a scope instead. I take time to explain your condition and your options, so that every decision is one we make together.</p>',
  '<p class="lede">मैं खाने की नली, पेट, आँतों, लिवर, पित्ताशय और पैंक्रियास की बीमारियों का इलाज करता हूँ। मेरी विशेष ट्रेनिंग एडवांस्ड एंडोस्कोपी में है, जिससे कई ऐसी बीमारियाँ, जिनके लिए पहले ऑपरेशन करना पड़ता था, अब स्कोप से ठीक हो जाती हैं। मैं आपकी बीमारी और इलाज के विकल्प आराम से समझाता हूँ, ताकि हर फ़ैसला हम मिलकर लें।</p>'),
 ('>Areas of care</p>', '>इलाज के क्षेत्र</p>'),
 ('<span>Fatty liver &amp; hepatitis</span><span>Cirrhosis &amp; GI bleeding</span><span>Bile duct &amp; pancreas</span><span>Acidity &amp; ulcers</span><span>IBS &amp; IBD</span><span>Colon polyps &amp; screening</span><span>Swallowing problems</span><span>Gut &amp; liver care in pregnancy</span>',
  '<span>फैटी लिवर और हेपेटाइटिस</span><span>सिरोसिस और पेट से खून आना</span><span>पित्त नली और पैंक्रियास</span><span>एसिडिटी और अल्सर</span><span>IBS और IBD</span><span>आँत के पॉलिप और जाँच</span><span>निगलने में तकलीफ़</span><span>प्रेगनेंसी में पेट और लिवर की देखभाल</span>'),
 ('<span class="k">Current role</span><span>Associate Consultant, Gastroenterology &amp; Therapeutic Endoscopy, Apollo Hospitals, Golf Course Road, Gurugram</span>',
  '<span class="k">वर्तमान पद</span><span>एसोसिएट कंसल्टेंट, गैस्ट्रोएंटेरोलॉजी और थेराप्यूटिक एंडोस्कोपी, अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम</span>'),
 ('<span class="k">Training</span><span>DrNB Gastroenterology, Medanta – The Medicity, Gurugram (Institute of Digestive &amp; Hepatobiliary Sciences)</span>',
  '<span class="k">ट्रेनिंग</span><span>DrNB गैस्ट्रोएंटेरोलॉजी, मेदांता – द मेडिसिटी, गुरुग्राम (इंस्टिट्यूट ऑफ़ डाइजेस्टिव एंड हेपेटोबिलियरी साइंसेज़)</span>'),
 ('<span class="k gold">Award</span><span>All-India Gold Medal, DrNB Gastroenterology</span>',
  '<span class="k gold">सम्मान</span><span>ऑल-इंडिया गोल्ड मेडल, DrNB गैस्ट्रोएंटेरोलॉजी</span>'),
 ('<span class="k">Fellowship</span><span>Advanced Fellowship in Endoscopic Ultrasound (EUS) &amp; ERCP</span>',
  '<span class="k">फ़ेलोशिप</span><span>एंडोस्कोपिक अल्ट्रासाउंड (EUS) और ERCP में एडवांस्ड फ़ेलोशिप</span>'),
 ('<span class="k">Experience</span><span>Formerly Associate Consultant, Medanta – The Medicity</span>',
  '<span class="k">अनुभव</span><span>पूर्व एसोसिएट कंसल्टेंट, मेदांता – द मेडिसिटी</span>'),
 ('<span class="k">Registration</span><span>Haryana Medical Council, Reg. No. HN-23524</span>',
  '<span class="k">रजिस्ट्रेशन</span><span>हरियाणा मेडिकल काउंसिल, रजि. नं. HN-23524</span>'),
 ('<span class="k">Research</span><span>Work on variceal bleeding, EUS-guided procedures and complex oesophageal strictures, presented at the World Congress of Gastroenterology 2026</span>',
  '<span class="k">रिसर्च</span><span>वैरिसियल ब्लीडिंग, EUS से होने वाले प्रोसीजर और खाने की नली की जटिल सिकुड़न पर काम, वर्ल्ड कांग्रेस ऑफ़ गैस्ट्रोएंटेरोलॉजी 2026 में प्रस्तुत</span>'),

 # faq
 ('<p class="eyebrow">Before you visit</p>', '<p class="eyebrow">आने से पहले</p>'),
 ('<h2>Common questions</h2>', '<h2>आम सवाल</h2>'),
 ('<summary>Do I need a referral to see a gastroenterologist?</summary><p>No. You can book directly. If another doctor has seen you, bring their notes and prescriptions.</p>',
  '<summary>क्या गैस्ट्रोएंटेरोलॉजिस्ट को दिखाने के लिए किसी डॉक्टर का रेफ़रल चाहिए?</summary><p>नहीं। आप सीधे अपॉइंटमेंट ले सकते हैं। अगर किसी और डॉक्टर को दिखाया है, तो उनके पर्चे और नोट्स साथ लाएँ।</p>'),
 ('<summary>What should I bring to my first consultation?</summary><p>All previous reports, scans, endoscopy and biopsy reports, and a list of every medicine and supplement you take. Photos of reports on your phone are fine.</p>',
  '<summary>पहली बार आते समय क्या लाना चाहिए?</summary><p>पुरानी सभी रिपोर्ट, स्कैन, एंडोस्कोपी और बायोप्सी की रिपोर्ट, और जो भी दवा या सप्लीमेंट आप लेते हैं उनकी लिस्ट। फ़ोन में रिपोर्ट की फ़ोटो भी चलेगी।</p>'),
 ('<summary>Do I need to come fasting?</summary><p>Not for a consultation. Fasting is needed only for procedures such as endoscopy, and for some blood tests. You will be told in advance.</p>',
  '<summary>क्या खाली पेट आना है?</summary><p>सिर्फ़ डॉक्टर को दिखाने के लिए नहीं। खाली पेट केवल एंडोस्कोपी जैसे प्रोसीजर और कुछ ब्लड टेस्ट के लिए आना होता है। यह आपको पहले से बता दिया जाएगा।</p>'),
 ('<summary>Are video consultations available?</summary><p>Yes. They work well for follow-ups, reviewing reports and diet advice. A first visit for new symptoms is better in person, so that you can be examined.</p>',
  '<summary>क्या वीडियो कंसल्टेशन होता है?</summary><p>हाँ। फ़ॉलो-अप, रिपोर्ट दिखाने और डाइट की सलाह के लिए यह अच्छा रहता है। नए लक्षणों के लिए पहली बार आमने-सामने दिखाना बेहतर है, ताकि ठीक से जाँच हो सके।</p>'),
 ('<summary>Is endoscopy safe?</summary><p>Endoscopy is a routine and very safe procedure. Serious complications are uncommon. The benefits and risks for your situation are explained before any procedure, and you can ask any question you have.</p>',
  '<summary>क्या एंडोस्कोपी सुरक्षित है?</summary><p>एंडोस्कोपी एक आम और बहुत सुरक्षित प्रोसीजर है। गंभीर दिक्कतें बहुत कम होती हैं। हर प्रोसीजर से पहले आपकी स्थिति के हिसाब से फ़ायदे और जोखिम समझाए जाते हैं, और आप कोई भी सवाल पूछ सकते हैं।</p>'),
 ('<summary>Where are endoscopy and other procedures done?</summary><p>Procedures are done in a fully equipped hospital endoscopy unit with monitoring and anaesthesia support. The details are shared at your consultation.</p>',
  '<summary>एंडोस्कोपी और दूसरे प्रोसीजर कहाँ होते हैं?</summary><p>प्रोसीजर अस्पताल की पूरी सुविधाओं वाली एंडोस्कोपी यूनिट में होते हैं, जहाँ मॉनिटरिंग और बेहोशी (एनेस्थीसिया) की सुविधा रहती है। पूरी जानकारी कंसल्टेशन के समय दी जाती है।</p>'),

 # visit
 ('<p class="eyebrow">Visit the clinic</p>', '<p class="eyebrow">क्लिनिक आएँ</p>'),
 ('<h2>Book a consultation</h2>', '<h2>अपॉइंटमेंट लें</h2>'),
 ('<p>Bring any previous reports, scans and a list of the medicines you take. If you have had an endoscopy before, bring that report too.</p>',
  '<p>पुरानी रिपोर्ट, स्कैन और अपनी दवाइयों की लिस्ट साथ लाएँ। अगर पहले एंडोस्कोपी हुई है, तो उसकी रिपोर्ट भी लाएँ।</p>'),
 ('<span class="phone-lbl">Appointments &amp; video consultations</span>', '<span class="phone-lbl">अपॉइंटमेंट और वीडियो कंसल्टेशन</span>'),
 ('<span class="phone-lbl">Call or WhatsApp</span>', '<span class="phone-lbl">कॉल या WhatsApp करें</span>'),
 ('rel="noopener">Message on WhatsApp</a>', 'rel="noopener">WhatsApp पर मैसेज करें</a>'),
 ('id="copyPhone" type="button">Copy number</button>', 'id="copyPhone" type="button">नंबर कॉपी करें</button>'),
 ("<p>Can't travel? Video consultations are available for follow-ups and for reviewing reports.</p>",
  '<p>आ नहीं सकते? फ़ॉलो-अप और रिपोर्ट दिखाने के लिए वीडियो कंसल्टेशन उपलब्ध है।</p>'),
 ('<address id="addr"><strong>Arcura Clinic</strong><br>M2K Corporate Park &amp; Shopping Plaza<br>14, Mayfield Garden, Sector 51<br>Gurugram, Haryana 122003</address>',
  '<address id="addr"><strong>आर्क्योरा क्लिनिक (Arcura Clinic)</strong><br>M2K कॉर्पोरेट पार्क एंड शॉपिंग प्लाज़ा<br>14, मेफ़ील्ड गार्डन, सेक्टर 51<br>गुरुग्राम, हरियाणा 122003</address>'),
 ('rel="noopener">Get directions</a>', 'rel="noopener">रास्ता देखें</a>'),
 ('id="copyAddr" type="button">Copy address</button>', 'id="copyAddr" type="button">पता कॉपी करें</button>'),
 ('<p>Visited recently? You can share your experience on <a href="https://g.page/r/CYmK8BpICDd6EBM/review" target="_blank" rel="noopener" style="color:var(--warm-on-ink)">Google</a>. It helps others find the right care.</p>',
  '<p>हाल ही में आए थे? अपना अनुभव <a href="https://g.page/r/CYmK8BpICDd6EBM/review" target="_blank" rel="noopener" style="color:var(--warm-on-ink)">Google</a> पर शेयर करें। इससे दूसरों को सही इलाज ढूँढने में मदद मिलती है।</p>'),
 ('<p>Also consulting at Apollo Hospitals, Golf Course Road, Gurugram.</p>', '<p>अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम में भी देखते हैं।</p>'),
 ('<a class="fab" href="#visit" aria-label="Book a visit">', '<a class="fab" href="#visit" aria-label="अपॉइंटमेंट लें">'),
 ('</svg>\n  Book\n</a>', '</svg>\n  अपॉइंटमेंट\n</a>'),

 # footer
 ('<p>This website is for general health education. It does not replace a consultation with a doctor, and nothing here is a diagnosis or treatment plan for any individual.</p>',
  '<p>यह वेबसाइट सामान्य स्वास्थ्य जानकारी के लिए है। यह डॉक्टर की सलाह की जगह नहीं ले सकती, और यहाँ लिखी कोई भी बात किसी व्यक्ति के लिए डायग्नोसिस या इलाज की योजना नहीं है।</p>'),
 ('<p>In a medical emergency, call 112 or go to the nearest emergency department.</p>', '<p>मेडिकल इमरजेंसी में 112 पर कॉल करें या सबसे पास की इमरजेंसी में जाएँ।</p>'),
 ('<p>Dr. Kshitij Lochab · Haryana Medical Council Reg. No. HN-23524 · +91 96671 04882</p>', '<p>डॉ. क्षितिज लोचब · हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524 · +91 96671 04882</p>'),
 ('<p>© 2026 Dr. Kshitij Lochab</p>', '<p>© 2026 डॉ. क्षितिज लोचब</p>'),

 # myth buster and fibre counter
 ('<p class="eyebrow">Myth Buster</p>', '<p class="eyebrow">भ्रम और सच</p>'),
 ('<h2>Myth or fact? Take a guess</h2>', '<h2>भ्रम या सच? अंदाज़ा लगाइए</h2>'),
 ('<p class="lede">Swipe through common beliefs about the stomach and liver and guess which are true. New ones every Monday and Thursday.</p>',
  '<p class="lede">पेट और लिवर से जुड़ी आम धारणाओं को स्वाइप करें और अंदाज़ा लगाइए कि कौन-सी सच है। हर सोमवार और गुरुवार नई जुड़ती हैं।</p>'),
 ('aria-selected="false" tabindex="-1">Thali meter</button>', 'aria-selected="false" tabindex="-1">थाली मीटर</button>'),
 ('<h3>How balanced is your thali today?</h3>', '<h3>आज आपकी थाली कितनी संतुलित है?</h3>'),
 ('<p class="lede">Tap what you have eaten today. Three meters show your fibre, protein and fat against what most adults need.</p>',
  '<p class="lede">आज आपने जो खाया है उस पर टैप करें। तीन मीटर दिखाते हैं कि आपका फ़ाइबर, प्रोटीन और फ़ैट ज़्यादातर बड़ों की ज़रूरत के मुकाबले कितना है।</p>'),

 # script: interface strings
 ('`<span class="pill ${cls}">${lbl}</span><h3>${esc(x.l)}</h3><dl><div><dt>Common causes</dt><dd>${esc(x.c)}</dd></div><div><dt>What to do</dt>',
  '`<span class="pill ${cls}">${lbl}</span><h3>${esc(x.l)}</h3><dl><div><dt>आम वजहें</dt><dd>${esc(x.c)}</dd></div><div><dt>क्या करें</dt>'),
 ('const SITE="https://drlochab.com";', 'const SITE="https://drlochab.com/hi/";'),
 ('new Intl.DateTimeFormat("en-IN",', 'new Intl.DateTimeFormat("hi-IN",'),
 ('<b>Try this today</b>${esc(t.try)}</div><div class="tip-actions">', '<b>आज यह करके देखें</b>${esc(t.try)}</div><div class="tip-actions">'),
 ('rel="noopener">Share on WhatsApp</a><span class="small">A new tip appears every morning.</span>',
  'rel="noopener">WhatsApp पर शेयर करें</a><span class="small">हर सुबह एक नई सलाह आती है।</span>'),
 ('Past tips will appear here as new ones are added each day.', 'रोज़ नई सलाह जुड़ने के साथ पुरानी सलाह यहाँ दिखेंगी।'),
 ('<b>Try this</b>${esc(t.try)}', '<b>यह करके देखें</b>${esc(t.try)}'),
 ('\\n\\nTry this: ${t.try}\\n\\nDaily gut-health tips from Dr. Kshitij Lochab: ${SITE}', '\\n\\nयह करके देखें: ${t.try}\\n\\nडॉ. क्षितिज लोचब की रोज़ की सेहत सलाह: ${SITE}'),
 ('<b>Try this today</b>${esc(t.try)}</div><a class="btn btn-ghost btn-sm"', '<b>आज यह करके देखें</b>${esc(t.try)}</div><a class="btn btn-ghost btn-sm"'),
 ('href="${shareLink(t,"IBS tip: ")}" target="_blank" rel="noopener">Share on WhatsApp</a>', 'href="${shareLink(t,"IBS सलाह: ")}" target="_blank" rel="noopener">WhatsApp पर शेयर करें</a>'),
 ("Today's tip could not load. Please refresh the page.", 'आज की सलाह लोड नहीं हो पाई। कृपया पेज रीफ़्रेश करें।'),
 ("Today's IBS tip could not load. Please refresh the page.", 'आज की IBS सलाह लोड नहीं हो पाई। कृपया पेज रीफ़्रेश करें।'),
 ('col("more","Eat more",g.more)+col("less","Cut down",g.less)+col("know","Good to know",g.know)',
  'col("more","ज़्यादा खाएँ",g.more)+col("less","कम करें",g.less)+col("know","जानने लायक",g.know)'),
 ('msg.textContent=label+" selected. Copy it from your menu.";', 'msg.textContent=label+" चुना गया है। मेन्यू से कॉपी करें।";'),
 ('msg.textContent=label+" copied.";', 'msg.textContent=label+" कॉपी हो गया।";'),
 ('"addr","Address");', '"addr","पता");'),
 ('"phoneNum","Number");', '"phoneNum","नंबर");'),

 # trust strip, open status, booking chips (18 Oct 2026)
 ('<b>Dr. Kshitij Lochab</b><span>Gold Medal DrNB · EUS &amp; ERCP fellowship</span><span class="id-open" id="openNow">Arcura Clinic, Sector 51, Gurugram</span></div><a class="btn btn-solid btn-sm" href="#visit">Book</a>',
  '<b>डॉ. क्षितिज लोचब</b><span>DrNB में ऑल-इंडिया गोल्ड मेडल · EUS और ERCP फ़ेलोशिप</span><span class="id-open" id="openNow">आर्क्योरा क्लिनिक, सेक्टर 51, गुरुग्राम</span></div><a class="btn btn-solid btn-sm" href="#visit">अपॉइंटमेंट</a>'),
 ('<p class="reason-lbl">What is the visit about? <span>Optional</span></p>', '<p class="reason-lbl">किस बारे में दिखाना है? <span>चाहें तो चुनें</span></p>'),
 ('<p class="reason-lbl">When suits you? <span>Optional</span></p>', '<p class="reason-lbl">कब आना ठीक रहेगा? <span>चाहें तो चुनें</span></p>'),
 ('const OPENTXT={open:t=>`Open now · until ${t}`,today:t=>`Opens today at ${t}`,next:(d,t)=>`Next clinic: ${d}, ${t}`,place:"Arcura, Sector 51",t:{9:"9 am",13:"1 pm",18:"6 pm",20:"8 pm"},days:["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],tom:"tomorrow"};',
  'const OPENTXT={open:t=>`अभी खुला है · ${t} तक`,today:t=>`आज ${t} से`,next:(d,t)=>`अगला क्लिनिक: ${d}, ${t}`,place:"आर्क्योरा, सेक्टर 51",t:{9:"सुबह 9 बजे",13:"दोपहर 1 बजे",18:"शाम 6 बजे",20:"रात 8 बजे"},days:["रविवार","सोमवार","मंगलवार","बुधवार","गुरुवार","शुक्रवार","शनिवार"],tom:"कल"};'),
 ('const BOOK={hello:"Hello Dr. Lochab, I would like to book a consultation",about:" about: ",when:"Preferred time: ",src:"(Found you on drlochab.com)",',
  'const BOOK={hello:"नमस्ते डॉ. लोचब, मुझे अपॉइंटमेंट लेना है",about:", इस बारे में: ",when:"मेरे लिए सही समय: ",src:"(drlochab.com से)",'),
 (' reasons:["Acidity or gastritis","Fatty liver or liver report","Jaundice or hepatitis","Gas, bloating or IBS","Constipation or loose motions","Endoscopy or colonoscopy","EUS or ERCP","Gallbladder or pancreas","Review of reports"],',
  ' reasons:["एसिडिटी या गैस्ट्राइटिस","फैटी लिवर या लिवर रिपोर्ट","पीलिया या हेपेटाइटिस","गैस, पेट फूलना या IBS","कब्ज़ या दस्त","एंडोस्कोपी या कोलोनोस्कोपी","EUS या ERCP","पित्ताशय या पैंक्रियास","रिपोर्ट दिखानी है"],'),
 (' times:["Weekday evening","Sunday morning","Video consultation"]};', ' times:["सोम–शुक्र शाम","रविवार सुबह","वीडियो कंसल्टेशन"]};'),
 ('<span class="hook-k">Diet charts</span><span class="hook-q">What should I eat with fatty liver, acidity or IBS?</span><span class="hook-go">See diet charts →</span>',
  '<span class="hook-k">डाइट चार्ट</span><span class="hook-q">फैटी लिवर, एसिडिटी या IBS में क्या खाएँ?</span><span class="hook-go">डाइट चार्ट देखें →</span>'),
 ('<a href="diet-charts/">Diet charts</a>', '<a href="diet-charts/">डाइट चार्ट</a>'),
 ('<p class="fb-plan"><a href="diet-charts/">Need a full diet plan for a condition, with a daily food diary? Open the diet charts →</a></p>',
  '<p class="fb-plan"><a href="diet-charts/">किसी बीमारी के लिए पूरा डाइट प्लान और रोज़ की फ़ूड डायरी चाहिए? डाइट चार्ट खोलें →</a></p>'),
 ('aria-label="Call +91 96671 04882"', 'aria-label="+91 96671 04882 पर कॉल करें"'),
 ('>My profile on the Arcura Clinic website →</a>', '>आर्क्योरा क्लिनिक की वेबसाइट पर मेरी प्रोफ़ाइल →</a>'),
 # illustration labels
 ('label(196,104,"Stomach")+label(134,40,"Food pipe")+label(56,128,"Liver","middle")', 'label(196,104,"पेट")+label(134,40,"खाने की नली")+label(56,128,"लिवर","middle")'),
 ('label(120,195,"Polyp","middle")+label(228,318,"Large bowel","end")', 'label(120,195,"पॉलिप","middle")+label(228,318,"बड़ी आँत","end")'),
 ('label(200,186,"Pancreas")+label(194,104,"Stomach")+label(151,212,"Ultrasound view","middle")', 'label(200,186,"पैंक्रियास")+label(194,104,"पेट")+label(151,212,"अल्ट्रासाउंड से दिखता हिस्सा","middle")'),
 ('label(176,18,"Liver","middle")+label(124,84,"Bile duct")+label(120,58,"Stone")+label(150,142,"Pancreas","middle")+label(14,146,"Intestine")',
  'label(176,18,"लिवर","middle")+label(124,84,"पित्त नली")+label(120,58,"पथरी")+label(150,142,"पैंक्रियास","middle")+label(14,146,"आँत")'),
 ('["Swollen vein","in the food pipe"]', '["खाने की नली में","फूली हुई नस"]'),
 ('["Vein sucked in,","band put on"]', '["नस खींचकर","बैंड लगाया"]'),
 ('["Vein shrinks and","falls off in days"]', '["नस सिकुड़कर कुछ","दिनों में गिर जाती है"]'),
 ('["Growth (polyp)","on bowel lining"]', '["आँत की परत पर","गाँठ (पॉलिप)"]'),
 ('["Lifted, then","caught in a loop"]', '["उठाकर तार के","फंदे में पकड़ा"]'),
 ('["Removed and","sent for testing"]', '["निकालकर जाँच","के लिए भेजा"]'),
 ('["Ulcer with a","bleeding vessel"]', '["अल्सर में","खून वाली नस"]'),
 ('["Tiny clip","seals the vessel"]', '["छोटी क्लिप से","नस बंद की"]'),
 ('["Bleeding stops,","clip falls off later"]', '["खून रुका, क्लिप","बाद में गिर जाती है"]'),
 ('${label(130,37,"Belly wall")}${label(130,90,"Stomach")}${label(92,58,"Feeding tube","end")}', '${label(130,37,"पेट की दीवार")}${label(130,90,"पेट")}${label(92,58,"फ़ीडिंग ट्यूब","end")}'),
 ('${label(108,29,"Recorder")}${label(80,140,"Pill camera","middle")}${label(196,104,"Small intestine","end")}', '${label(108,29,"रिकॉर्डर")}${label(80,140,"पिल कैमरा","middle")}${label(196,104,"छोटी आँत","end")}'),
 ("Upper GI endoscopy: the scope passes through the food pipe into the stomach", "अपर GI एंडोस्कोपी: स्कोप खाने की नली से होकर पेट में जाता है"),
 ("Colonoscopy: the scope travels around the large bowel, where polyps can be removed", "कोलोनोस्कोपी: स्कोप बड़ी आँत में घूमता है, जहाँ पॉलिप निकाले जा सकते हैं"),
 ("Endoscopic ultrasound: an ultrasound probe on the scope looks through the stomach wall at the pancreas", "एंडोस्कोपिक अल्ट्रासाउंड: स्कोप पर लगा अल्ट्रासाउंड पेट की दीवार के पार पैंक्रियास को देखता है"),
 ("ERCP: from the intestine, a thin tube enters the bile duct to remove a stone", "ERCP: आँत से एक पतली नली पित्त नली में जाकर पथरी निकालती है"),
 ("Variceal banding in three steps: a swollen vein, a band placed on it, and the vein shrinking away", "वैरिसियल बैंडिंग तीन चरणों में: फूली हुई नस, उस पर बैंड, और नस का सिकुड़ जाना"),
 ("Polyp removal in three steps: a growth on the bowel lining, lifted and caught in a wire loop, then removed", "पॉलिप निकालना तीन चरणों में: आँत की परत पर गाँठ, उसे उठाकर तार के फंदे में पकड़ना, फिर निकालना"),
 ("Bleeding control in three steps: a bleeding ulcer, a clip placed on the vessel, and the bleeding stopped", "खून रोकना तीन चरणों में: खून बहता अल्सर, नस पर क्लिप, और खून रुकना"),
 ("Feeding tube: a soft tube passes through the belly wall into the stomach, held by a small disc on each side", "फ़ीडिंग ट्यूब: एक नरम नली पेट की दीवार से होकर पेट में जाती है, दोनों तरफ़ छोटी डिस्क से टिकी रहती है"),
 ("Dilatation: a balloon passed through the scope widens a narrowed section", "डाइलेटेशन: स्कोप से डाला गया बैलून सिकुड़े हिस्से को चौड़ा करता है"),
 ("Capsule endoscopy: a swallowed pill camera travels through the small intestine and sends pictures to a recorder worn on a belt", "कैप्सूल एंडोस्कोपी: निगला गया पिल कैमरा छोटी आँत से गुज़रता है और बेल्ट पर बँधे रिकॉर्डर को तस्वीरें भेजता है"),
 ('${label(100,148,"Balloon gently widens the narrowing","middle")}', '${label(100,148,"बैलून धीरे से सिकुड़न को चौड़ा करता है","middle")}'),
]

# Replaces everything from "const ORGANS=" up to "const esc=" in the English source.
DATA_JS = r'''const ORGANS={stomach:"खाने की नली और पेट",liver:"लिवर",gb:"पित्ताशय और पित्त नली",pancreas:"पैंक्रियास",intestine:"आँतें"};
const TIERS={routine:["pill-routine","आम दिनों में दिखाएँ"],soon:["pill-soon","कुछ दिनों के अंदर दिखाएँ"],urgent:["pill-urgent","आज ही दिखाएँ"]};

const SYMPTOMS=[
 {l:"सीने में जलन या एसिडिटी",t:"routine",c:"एसिड रिफ़्लक्स (GERD), गैस्ट्राइटिस, या H. pylori इन्फ़ेक्शन।",a:"थोड़ा-थोड़ा खाएँ और रात का खाना जल्दी खाएँ। अगर हफ़्ते में दो बार या उससे ज़्यादा हो, या 2 से 4 हफ़्ते से ज़्यादा चले, तो दिखाएँ।"},
 {l:"पेट फूलना और गैस",t:"routine",c:"IBS, कब्ज़, कुछ चीज़ें न पचना (जैसे दूध), या H. pylori।",a:"अगर बार-बार हो या रोज़ के काम पर असर डाले तो दिखाएँ। साथ में वज़न घट रहा हो तो जल्दी दिखाएँ।"},
 {l:"कब्ज़",t:"routine",c:"कम फ़ाइबर या कम पानी, कम चलना-फिरना, कुछ दवाइयाँ, थायरॉइड या IBS। कभी-कभी आँत में गाँठ।",a:"आम दिनों में दिखाएँ। अगर 45 की उम्र के बाद नई शुरू हुई हो या मल में खून आए तो जल्दी दिखाएँ।"},
 {l:"रिपोर्ट में फैटी लिवर",t:"routine",c:"ज़्यादा वज़न, डायबिटीज़, हाई कोलेस्ट्रॉल या शराब।",a:"लिवर में स्कारिंग की जाँच और इलाज के लिए दिखाएँ। शुरुआती फैटी लिवर ठीक हो सकता है।"},
 {l:"2 हफ़्ते से ज़्यादा दस्त",t:"soon",c:"जियार्डिया जैसे इन्फ़ेक्शन, सीलिएक बीमारी, IBS, IBD, थायरॉइड या दवाइयाँ।",a:"कुछ दिनों में दिखाएँ, खासकर अगर खून आए, वज़न घटे या रात में उठकर शौच जाना पड़े।"},
 {l:"पीली आँखें या गहरा पेशाब",t:"soon",c:"हेपेटाइटिस A, B, C या E, शराब, कुछ दवाइयाँ या जड़ी-बूटी वाले प्रोडक्ट, या पित्त नली में रुकावट।",a:"एक-दो दिन में दिखाएँ। साथ में कँपकँपी वाला बुखार, बेहोशी जैसा लगना या ज़्यादा नींद हो तो आज ही दिखाएँ।"},
 {l:"निगलते समय खाना अटकना",t:"soon",c:"खाने की नली का सिकुड़ना, नली की माँसपेशियों की दिक्कत, ज़्यादा रिफ़्लक्स, या गाँठ।",a:"जल्दी विशेषज्ञ को दिखाएँ। आम तौर पर एंडोस्कोपी से वजह पता चल जाती है।"},
 {l:"बिना कोशिश वज़न घटना",t:"soon",c:"कई वजहें हो सकती हैं, जैसे पेट, पैंक्रियास, आँत, लिवर या थायरॉइड की बीमारी।",a:"पूरी जाँच के लिए कुछ दिनों में दिखाएँ।"},
 {l:"मल में लाल खून",t:"soon",c:"बवासीर, फ़िशर, पॉलिप, IBD, और कभी-कभी आँत का कैंसर।",a:"जल्दी दिखाएँ। खून ज़्यादा हो या चक्कर आएँ तो आज ही दिखाएँ।"},
 {l:"काला, तारकोल जैसा मल",t:"urgent",c:"पेट या ऊपरी आँत से खून आना, जैसे अल्सर या लिवर की बीमारी में फूली हुई नसें। आयरन की गोलियों से भी मल काला हो सकता है।",a:"आज ही दिखाएँ। कमज़ोरी, बेहोशी जैसा लगे या साँस फूले तो इमरजेंसी में जाएँ।"},
 {l:"उल्टी में खून",t:"urgent",c:"अल्सर, खाने की नली में चोट, या लिवर की बीमारी में फूली नसों (वैरिसीज़) से खून।",a:"यह इमरजेंसी है। सबसे पास की इमरजेंसी में जाएँ या 112 पर कॉल करें।"},
 {l:"पेट में तेज़ दर्द",t:"urgent",c:"पैंक्रियाटाइटिस, पित्त की पथरी का दर्द, अल्सर फटना, अपेंडिसाइटिस या आँत में रुकावट।",a:"अगर दर्द अचानक या बहुत तेज़ हो, या साथ में उल्टी या बुखार हो, तो तुरंत इमरजेंसी में जाएँ।"}
];

const CONDITIONS=[
 {o:"stomach",n:"एसिडिटी और रिफ़्लक्स (GERD)",s:"पेट का एसिड वापस खाने की नली में आना।",w:"पेट का एसिड ऊपर खाने की नली में आ जाता है। कभी-कभी जलन होना आम है। बार-बार रिफ़्लक्स से नली में सूजन आ सकती है और सालों में उसकी परत ख़राब हो सकती है।",g:["खाने के बाद छाती के पीछे जलन","मुँह में खट्टा पानी या खाना वापस आना","लेटने या झुकने पर ज़्यादा","लंबे समय से खाँसी या आवाज़ भारी होना"],h:"थोड़ा-थोड़ा खाना, सोने से कम से कम 3 घंटे पहले खाना, पलंग का सिर वाला हिस्सा ऊँचा करना, अतिरिक्त वज़न घटाना, और तंबाकू व शराब कम करना। ज़रूरत हो तो दवाइयाँ अच्छा काम करती हैं।",e:"हफ़्ते में दो बार या ज़्यादा लक्षण, 2 से 4 हफ़्ते में आराम न हो, या निगलने में दिक्कत या वज़न घटने जैसा कोई ख़तरे का संकेत।"},
 {o:"stomach",n:"H. pylori, गैस्ट्राइटिस और अल्सर",s:"आम तौर पर एक आम इन्फ़ेक्शन या दर्द की गोलियाँ इसकी वजह होती हैं।",w:"H. pylori पेट का एक आम इन्फ़ेक्शन है जिससे सूजन और अल्सर हो सकते हैं। आइबुप्रोफ़ेन, डाइक्लोफ़ेनाक और एस्पिरिन जैसी दर्द की गोलियाँ भी अक्सर वजह होती हैं।",g:["ऊपरी पेट में जलन या कुतरने जैसा दर्द","खाने से दर्द का बदलना","जी मिचलाना या जल्दी पेट भर जाना","काला मल, जिसका मतलब खून आना है"],h:"साँस, मल या बायोप्सी टेस्ट से H. pylori का पता चलता है। लगभग दो हफ़्ते की दवाइयों से आम तौर पर यह ठीक हो जाता है। दर्द की गोली बंद करने से पेट ठीक होने लगता है।",e:"ऊपरी पेट का दर्द जो कुछ हफ़्तों से ज़्यादा रहे। काला मल या उल्टी में खून हो तो उसी दिन दिखाएँ।"},
 {o:"stomach",n:"निगलने में तकलीफ़",s:"खाना नीचे जाते समय अटकना कभी सामान्य नहीं है।",w:"छाती में खाना अटकने की वजह खाने की नली का सिकुड़ना (स्ट्रिक्चर), नली की माँसपेशियों की दिक्कत, ज़्यादा रिफ़्लक्स या कोई गाँठ हो सकती है।",g:["छाती की हड्डी के पीछे खाना अटकना","खाना नीचे उतारने के लिए पानी पीना पड़ना","बिना पचा खाना वापस आना","वज़न घटना"],h:"एंडोस्कोपी से वजह पता चलती है। सिकुड़न को अक्सर उसी प्रोसीजर में बैलून या डाइलेटर से चौड़ा किया जा सकता है।",e:"निगलने में तकलीफ़ जो बार-बार हो। थूक भी न निगल पाएँ तो इमरजेंसी में जाएँ।"},
 {o:"liver",n:"फैटी लिवर (MASLD)",s:"बहुत आम, अक्सर बिना लक्षण के, और कई बार ठीक हो सकता है।",w:"लिवर में चर्बी जमा हो जाती है, ज़्यादातर वज़न बढ़ने, डायबिटीज़, हाई कोलेस्ट्रॉल या शराब से। आम तौर पर लक्षण नहीं होते, लेकिन कुछ लोगों में धीरे-धीरे लिवर में स्कारिंग (फ़ाइब्रोसिस) और सिरोसिस हो सकता है।",g:["आम तौर पर कोई लक्षण नहीं","अल्ट्रासाउंड या लिवर के ब्लड टेस्ट में पता चलता है","थकान या दाईं तरफ़ भारीपन"],h:"शरीर का 7 से 10% वज़न घटाना, नियमित व्यायाम, शुगर कंट्रोल और शराब से दूरी शुरुआती फैटी लिवर को ठीक कर सकते हैं। लिवर स्टिफ़नेस टेस्ट से स्कारिंग की जाँच होती है।",e:"रिपोर्ट में फैटी लिवर, लिवर एंज़ाइम बढ़े हुए, या डायबिटीज़ के साथ वज़न बढ़ना।"},
 {o:"liver",n:"हेपेटाइटिस B और C",s:"चुपचाप रहने वाले इन्फ़ेक्शन जिनका इलाज है, और C पूरी तरह ठीक हो सकता है।",w:"ये वायरल इन्फ़ेक्शन खून, असुरक्षित इंजेक्शन, बिना जाँच का खून चढ़ने, यौन संपर्क (ज़्यादातर हेपेटाइटिस B) और माँ से बच्चे में फैलते हैं। कई लोगों में सालों तक कोई लक्षण नहीं होते।",g:["अक्सर कोई लक्षण नहीं","रक्तदान, प्रेगनेंसी या ऑपरेशन से पहले के टेस्ट में पता चलना","बाद में: पीलिया, पैरों या पेट में सूजन"],h:"हेपेटाइटिस C लगभग 3 महीने की गोलियों से पूरी तरह ठीक हो जाता है। हेपेटाइटिस B दवाइयों और नियमित जाँच से कंट्रोल रहता है, और टीके से इससे बचा जा सकता है।",e:"HBsAg या anti-HCV टेस्ट पॉज़िटिव हो, चाहे आप बिल्कुल ठीक महसूस करें।"},
 {o:"liver",n:"पीलिया (जॉन्डिस)",s:"यह किसी दिक्कत का संकेत है, अपने आप में बीमारी नहीं।",w:"पीलिया में आँखें और त्वचा पीली हो जाती हैं। आम वजहें हैं दूषित खाने या पानी से हेपेटाइटिस A और E, शराब, कुछ दवाइयाँ और जड़ी-बूटी वाले प्रोडक्ट, और पित्त नली में रुकावट।",g:["पीली आँखें और गहरा पेशाब","हल्के रंग का मल और खुजली","भूख न लगना और जी मिचलाना"],h:"ब्लड टेस्ट और अल्ट्रासाउंड से वजह पता चलती है, और इलाज उसी के हिसाब से होता है। पित्त नली की रुकावट अक्सर बिना ऑपरेशन ERCP से खुल जाती है।",e:"एक-दो दिन में दिखाएँ। कँपकँपी वाला बुखार, बेहोशी जैसा लगना, ज़्यादा नींद या खून आए तो तुरंत जाएँ।"},
 {o:"liver",n:"सिरोसिस",s:"लिवर में लंबे समय की स्कारिंग।",w:"सालों तक लिवर को नुकसान होने से स्वस्थ हिस्से की जगह स्कार बन जाता है। आम वजहें शराब, फैटी लिवर और हेपेटाइटिस B या C हैं।",g:["पेट या पैरों में सूजन","उल्टी में खून या काला मल","भ्रम या बहुत ज़्यादा नींद","आसानी से नील पड़ना"],h:"वजह का इलाज, हर 6 महीने में लिवर कैंसर की जाँच, और एंडोस्कोपी से फूली नसों (वैरिसीज़) को खून आने से पहले ढूँढकर बैंड लगाना।",e:"सिरोसिस में विशेषज्ञ से नियमित फ़ॉलो-अप ज़रूरी है। उल्टी में खून या भ्रम होना इमरजेंसी है।"},
 {o:"gb",n:"पित्त की पथरी और पित्त नली की पथरी",s:"पथरी जो पित्त के बहाव को रोक सकती है।",w:"पित्ताशय में पथरी बन जाती है। कई बार इससे कोई दिक्कत नहीं होती। कुछ पथरी पित्त नली में खिसककर उसे रोक देती हैं, जिससे पीलिया, इन्फ़ेक्शन या पैंक्रियाटाइटिस हो सकता है।",g:["ऊपरी दाएँ या बीच के पेट में दर्द, अक्सर भारी खाने के बाद","दर्द का पीठ या दाएँ कंधे तक जाना","पीलिया, या कँपकँपी वाला बुखार"],h:"पित्ताशय सर्जन निकालते हैं। पित्त नली में फँसी पथरी ERCP से निकाली जाती है, जो बिना चीरे वाला एंडोस्कोपिक प्रोसीजर है।",e:"बार-बार दर्द के दौरे, या दर्द के साथ पीलिया या बुखार।"},
 {o:"pancreas",n:"पैंक्रियाटाइटिस",s:"पैंक्रियास में सूजन, अचानक या लंबे समय की।",w:"अचानक (एक्यूट) होने वाले दौरे की वजह ज़्यादातर पित्त की पथरी या शराब होती है। बार-बार दौरे पड़ने से क्रॉनिक पैंक्रियाटाइटिस हो सकता है।",g:["ऊपरी पेट में तेज़ दर्द जो पीठ तक जाए","उल्टी","लंबी बीमारी में: तैलीय मल, वज़न घटना, डायबिटीज़"],h:"एक्यूट दौरे में अस्पताल में इलाज ज़रूरी है। पानी की थैलियाँ, नली की पथरी और सिकुड़न अक्सर ओपन सर्जरी की जगह EUS या ERCP से ठीक हो जाती हैं।",e:"उल्टी के साथ पेट में तेज़ दर्द में इमरजेंसी इलाज चाहिए।"},
 {o:"pancreas",n:"पैंक्रियास की सिस्ट और गाँठ",s:"अक्सर किसी स्कैन में संयोग से पता चलती है।",w:"पैंक्रियास की सिस्ट अक्सर किसी और वजह से हुए स्कैन में दिख जाती है। ज़्यादातर नुकसानदेह नहीं होतीं। कुछ में निगरानी या इलाज की ज़रूरत होती है।",g:["अक्सर कोई लक्षण नहीं","लक्षण हों तो: ऊपरी पेट दर्द, पीलिया या वज़न घटना"],h:"एंडोस्कोपिक अल्ट्रासाउंड (EUS) से पास से साफ़ तस्वीर मिलती है और बारीक सुई से सैंपल लिया जा सकता है, ताकि सही इलाज तय हो सके।",e:"स्कैन में पैंक्रियास में कोई भी सिस्ट या गाँठ।"},
 {o:"intestine",n:"इरिटेबल बाउल सिंड्रोम (IBS)",s:"लक्षण असली हैं, लेकिन आँत को कोई नुकसान नहीं।",w:"एक आम बीमारी जिसमें आँत ज़्यादा संवेदनशील हो जाती है। इससे असली तकलीफ़ होती है, लेकिन आँत को नुकसान नहीं होता और कैंसर नहीं होता।",g:["पेट दर्द जो शौच के बाद कम हो जाए","पेट फूलना","कब्ज़, दस्त, या बारी-बारी दोनों","तनाव में बढ़ना"],h:"खान-पान में बदलाव, फ़ाइबर ठीक करना, तनाव कम करना, और ज़रूरत के हिसाब से दवाइयाँ। ज़रूरत हो तो दूसरी बीमारियों को हटाने के लिए जाँच होती है।",e:"लक्षण रोज़ की ज़िंदगी पर असर डालें, या 45 की उम्र के बाद आँत के नए लक्षण।"},
 {o:"intestine",n:"अल्सरेटिव कोलाइटिस और क्रोहन बीमारी",s:"आँत में लंबे समय की सूजन।",w:"इन्फ़्लेमेटरी बाउल डिज़ीज़ (IBD) में शरीर की रोग-प्रतिरोधक प्रणाली आँत में सूजन कर देती है। भारत में यह बढ़ रही है और अक्सर पहले इसे इन्फ़ेक्शन या TB समझ लिया जाता है।",g:["हफ़्तों तक खून या आँव के साथ दस्त","पेट दर्द और वज़न घटना","तुरंत शौच जाने की जल्दी, या रात में उठकर जाना"],h:"बायोप्सी के साथ कोलोनोस्कोपी से पुष्टि होती है। आधुनिक दवाइयाँ सूजन को कंट्रोल करती हैं और ज़्यादातर लोग लंबे समय तक ठीक रहते हैं।",e:"दो हफ़्ते से ज़्यादा खून वाले दस्त।"},
 {o:"intestine",n:"कब्ज़",s:"अक्सर आसानी से ठीक, कभी-कभी ख़तरे का संकेत।",w:"सख़्त, कम या मुश्किल से होने वाला मल, ज़्यादातर कम फ़ाइबर, कम पानी, कम चलने-फिरने या दवाइयों से।",g:["हफ़्ते में 3 से कम बार शौच","ज़ोर लगाना पड़ना","पेट पूरा साफ़ न होने का एहसास"],h:"ज़्यादा फ़ाइबर, पानी और चलना-फिरना, शौच का तय समय, और ज़रूरत हो तो सुरक्षित जुलाब।",e:"45 की उम्र के बाद नई कब्ज़, मल में खून, वज़न घटना, या आसान उपायों से आराम न मिलना।"},
 {o:"intestine",n:"आँत के पॉलिप और आँत का कैंसर",s:"पॉलिप जल्दी पकड़ने से कई कैंसर रुक जाते हैं।",w:"पॉलिप बड़ी आँत में छोटी गाँठें होती हैं। कुछ कई सालों में कैंसर बन सकती हैं। आँत का कैंसर अब 50 से कम उम्र के लोगों में भी बढ़ रहा है।",g:["मल में खून","3 हफ़्ते से ज़्यादा शौच की आदत में बदलाव","खून की कमी, थकान या वज़न घटना","शुरुआत में अक्सर कोई लक्षण नहीं"],h:"कोलोनोस्कोपी से पॉलिप मिलते हैं और उसी जाँच में निकाल दिए जाते हैं। बड़ी चपटी गाँठें अक्सर बिना ऑपरेशन एंडोस्कोपी (EMR) से निकल जाती हैं।",e:"इनमें से कोई भी लक्षण, या माता-पिता या भाई-बहन को आँत का कैंसर।"}
];

const PROCS=[
 {il:"gastro",n:"अपर GI एंडोस्कोपी",a:"गैस्ट्रोस्कोपी",w:"मुँह से एक पतला कैमरा डालकर खाने की नली, पेट और आँत का पहला हिस्सा देखा जाता है। ज़रूरत हो तो बिना दर्द के छोटी बायोप्सी ली जाती है।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 10 से 15 मिनट"],["आराम","गले में स्प्रे, या चाहें तो हल्की बेहोशी की दवा"],["बाद में","उसी दिन घर"]]},
 {il:"colono",n:"कोलोनोस्कोपी",a:"बड़ी आँत",w:"मल द्वार से कैमरा डालकर बड़ी आँत की जाँच होती है। जाँच में मिले पॉलिप उसी समय निकाल दिए जाते हैं।",d:[["तैयारी","एक दिन पहले हल्का खाना और पेट साफ़ करने की दवा"],["समय","लगभग 20 से 45 मिनट"],["आराम","आम तौर पर हल्की बेहोशी में"],["बाद में","उसी दिन घर; उस दिन गाड़ी न चलाएँ"]]},
 {il:"eus",n:"एंडोस्कोपिक अल्ट्रासाउंड",a:"EUS",w:"स्कोप के सिरे पर लगे अल्ट्रासाउंड से शरीर के अंदर से पैंक्रियास, पित्त नली और आसपास की ग्रंथियों की साफ़ तस्वीर मिलती है। इससे सुई से सैंपल और पानी की थैलियाँ भी निकाली जा सकती हैं।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 20 से 60 मिनट"],["आराम","हल्की बेहोशी में"],["किसके लिए","पैंक्रियास की सिस्ट और गाँठ, पित्त नली की दिक्कत, गाँठ की स्टेज जानना"]]},
 {il:"ercp",n:"ERCP",a:"पित्त और पैंक्रियास की नली",w:"एक्स-रे की मदद से स्कोप पित्त और पैंक्रियास की नली के मुँह तक पहुँचता है, और बिना चीरे के पथरी निकालता है और रुकावट में स्टेंट डालता है।",d:[["तैयारी","खाली पेट और पहले ब्लड टेस्ट"],["समय","लगभग 30 से 60 मिनट"],["आराम","गहरी बेहोशी या एनेस्थीसिया में"],["बाद में","अक्सर अस्पताल में थोड़ा रुकना"]]},
 {il:"evl",n:"वैरिसियल बैंडिंग",a:"EVL",w:"लिवर की बीमारी में खाने की नली की नसें फूलकर फट सकती हैं। स्कोप से छोटे रबर बैंड लगाकर इन्हें सिकोड़ा जाता है और खून आने से रोका जाता है।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 15 से 20 मिनट"],["आराम","हल्की बेहोशी में"],["बाद में","एक-दो दिन नरम खाना; दोबारा सेशन लग सकते हैं"]]},
 {il:"emr",n:"पॉलिप निकालना और EMR",a:"एंडोस्कोपिक रिसेक्शन",w:"पॉलिप और कुछ शुरुआती चपटी गाँठें स्कोप से उठाकर निकाल दी जाती हैं, अक्सर ऑपरेशन की ज़रूरत ही नहीं पड़ती।",d:[["तैयारी","एंडोस्कोपी या कोलोनोस्कोपी जैसी"],["समय","आकार और संख्या पर निर्भर"],["आराम","हल्की बेहोशी में"],["बाद में","निकाले गए हिस्से की रिपोर्ट लगभग एक हफ़्ते में"]]},
 {il:"stop",n:"खून रोकना",a:"हीमोस्टेसिस",w:"अल्सर या फटी नस से आता खून स्कोप से छोटी क्लिप, इंजेक्शन या गर्मी से रोका जाता है, आम तौर पर बिना ऑपरेशन।",d:[["तैयारी","ज़रूरत पर तुरंत, ड्रिप या खून चढ़ाकर हालत संभालने के बाद"],["समय","लगभग 20 से 45 मिनट"],["आराम","हल्की बेहोशी में"],["बाद में","निगरानी के लिए अस्पताल में थोड़ा रुकना"]]},
 {il:"peg",n:"फ़ीडिंग ट्यूब (PEG)",a:"पोषण सहायता",w:"जो लोग सुरक्षित रूप से निगल नहीं पाते, उनके लिए स्कोप की मदद से त्वचा से होकर पेट में एक नरम फ़ीडिंग ट्यूब लगाई जाती है।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 20 से 30 मिनट"],["आराम","हल्की बेहोशी में"],["बाद में","आम तौर पर एक दिन के अंदर खाना शुरू"]]},
 {il:"dil",n:"डाइलेटेशन और स्टेंटिंग",a:"सिकुड़न खोलना",w:"खाने की नली, पित्त नली या आँत के सिकुड़े हिस्से को बैलून से चौड़ा किया जाता है, या स्कोप से स्टेंट डालकर खुला रखा जाता है।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 20 से 45 मिनट"],["आराम","हल्की बेहोशी में"],["बाद में","खाना धीरे-धीरे बढ़ाया जाता है"]]},
 {il:"capsule",n:"कैप्सूल एंडोस्कोपी",a:"पिल कैमरा",w:"आप एक बड़ी गोली जितना कैमरा निगलते हैं। यह छोटी आँत की हज़ारों तस्वीरें लेता है, जहाँ तक सामान्य एंडोस्कोप पूरी तरह नहीं पहुँच पाता, और फिर अपने-आप मल के साथ निकल जाता है।",d:[["तैयारी","एक दिन पहले सिर्फ़ साफ़ तरल और रात भर खाली पेट"],["समय","लगभग 8 से 12 घंटे रिकॉर्डिंग, इस बीच आप अपना काम कर सकते हैं"],["आराम","न बेहोशी, न नली"],["किसके लिए","छिपी हुई ब्लीडिंग, बिना कारण खून की कमी, क्रोन्स बीमारी का शक"]]}
];


'''

# Replaces the GUIDES array in the English source.
GUIDES_JS = r'''const GUIDES=[
 {n:"फैटी लिवर",more:["हर खाने में सब्ज़ियाँ और सलाद","साबुत अनाज: चोकर वाला आटा, बाजरा-रागी, ओट्स, ब्राउन राइस","प्रोटीन के लिए दाल, चना, राजमा और अंकुरित अनाज","जूस की जगह साबुत फल","कम चीनी वाली सादी चाय या कॉफ़ी"],less:["कोल्ड ड्रिंक, पैकेट वाले जूस और मिठाइयाँ","तले स्नैक्स, नमकीन और बेकरी की चीज़ें","मैदा: सफ़ेद ब्रेड, बिस्किट, नूडल्स","प्रोसेस्ड और रेड मीट","शराब, जिसे पूरी तरह छोड़ना सबसे अच्छा है"],know:["शरीर का 7 से 10% वज़न घटाने से शुरुआती फैटी लिवर ठीक हो सकता है; दुबले लोगों में 3 से 5% भी मदद करता है","हफ़्ते में लगभग 150 मिनट तेज़ चलना वज़न घटने से पहले ही फ़ायदा देता है","स्कारिंग की जाँच के लिए लिवर स्टिफ़नेस टेस्ट करवाएँ"]},
 {n:"एसिडिटी और रिफ़्लक्स",more:["थोड़ा-थोड़ा, बार-बार खाना","सोने से कम से कम 3 घंटे पहले रात का खाना","ओट्स, पकी सब्ज़ियाँ, केला और पपीता जैसे कम खट्टे फल","खाने के बीच में पानी","खाने के बाद थोड़ी देर टहलना"],less:["देर रात भारी खाना","तला और बहुत चिकना खाना","ज़्यादा चाय, कॉफ़ी और सोडा","चॉकलेट और पुदीना, जो अक्सर जलन बढ़ाते हैं","शराब और तंबाकू"],know:["ज़्यादा वज़न हो तो वज़न घटाना सबसे असरदार क़दमों में से एक है","हर व्यक्ति में जलन बढ़ाने वाली चीज़ें अलग होती हैं; दो हफ़्ते की खाने की डायरी से अपनी चीज़ें पहचानें","रात की तकलीफ़ में पलंग का सिर वाला हिस्सा 6 से 8 इंच ऊँचा करें","निगलने में दिक्कत या वज़न घटे तो विशेषज्ञ को दिखाएँ"]},
 {n:"IBS और पेट फूलना",more:["खाने का तय समय","घुलने वाला फ़ाइबर: ओट्स, इसबगोल, पकी सब्ज़ियाँ","दही और छाछ, अगर सूट करें","दिन भर में पर्याप्त पानी","धीरे-धीरे, चबाकर खाना"],less:["राजमा, चना, प्याज़ और लहसुन ज़्यादा मात्रा में, अगर इनसे तकलीफ़ बढ़े","सोडा और कोल्ड ड्रिंक","सॉर्बिटॉल वाली शुगर-फ़्री च्युइंग गम और मिठाइयाँ","ज़्यादा मात्रा में गेहूँ का चोकर, जिससे पेट और फूल सकता है","ज़्यादा चाय और कॉफ़ी","बहुत तीखा या तैलीय खाना"],know:["सही मार्गदर्शन में लो-FODMAP डाइट कई लोगों की मदद करती है","तनाव और कम नींद से लक्षण बढ़ते हैं","45 के बाद नए लक्षण, खून आना या वज़न घटे तो पहले जाँच ज़रूरी है"]},
 {n:"कब्ज़",more:["रोज़ 25 से 30 ग्राम फ़ाइबर, धीरे-धीरे बढ़ाएँ","कीवी और सूखे आलूबुखारे (प्रून), जो अच्छा असर करते हैं, साथ में अमरूद, नाशपाती और पपीता","साबुत अनाज, दाल और सब्ज़ियाँ","इतना पानी कि पेशाब हल्का पीला रहे","रोज़ टहलना या व्यायाम"],less:["मैदा और पैकेट वाले स्नैक्स","नाश्ता छोड़ना","शौच की इच्छा को रोकना","बिना सलाह लंबे समय तक तेज़ जुलाब"],know:["नाश्ते के बाद छोटे स्टूल पर पैर रखकर शौच के लिए बैठें","इसबगोल पर्याप्त पानी के साथ ही काम करता है","45 के बाद नई कब्ज़ या मल में खून हो तो जाँच करवाएँ"]},
 {n:"पीलिया के बाद",more:["पर्याप्त कैलोरी वाला सामान्य, संतुलित घर का खाना","दाल, दही, फल और सब्ज़ियाँ","भरपूर साफ़, उबला या फ़िल्टर किया पानी","भूख कम हो तो थोड़ा-थोड़ा बार-बार खाना","थकान रहने तक आराम"],less:["शराब, पूरी तरह","डॉक्टर के लिखे बिना जड़ी-बूटी और दवाइयाँ","सड़क का खाना और असुरक्षित पानी"],know:["आम खाने में डलने वाली हल्दी, तेल या नमक छोड़ने की ज़रूरत नहीं","सिर्फ़ उबला खाना खाने से कमज़ोरी आती है और ठीक होने में देर लगती है","बुखार, भ्रम, ज़्यादा नींद या खून आए तो तुरंत दिखाएँ"]},
 {n:"सिरोसिस",more:["पर्याप्त प्रोटीन: दाल, पनीर, दही, अंडे, मछली या चिकन","हर 3 से 4 घंटे में थोड़ा खाना","सोने से पहले हल्का नाश्ता, जैसे रोटी के साथ दूध या पोहा","ताज़ा घर का खाना"],less:["ऊपर से नमक, पापड़, अचार, नमकीन और पैकेट वाला खाना, अगर सूजन है","शराब, पूरी तरह","कच्चा या अधपका मीट और सी-फ़ूड"],know:["डॉक्टर न कहें तो प्रोटीन कम न करें","सोने से पहले का नाश्ता माँसपेशियों को बचाता है","सूजन हो तो: दिन भर में 2 ग्राम से ज़्यादा सोडियम नहीं (कुल लगभग एक समतल छोटा चम्मच, यानी 5 ग्राम नमक), बिना सलाह के लो-सोडियम नमक नहीं, और पानी डॉक्टर के बताए अनुसार"]},
 {n:"पैंक्रियाटाइटिस के बाद",more:["पहले कुछ हफ़्ते: थोड़ा-थोड़ा, बार-बार, हल्का खाना","उबला, भाप में पका या हल्का पका खाना","प्रोटीन: दाल, दही, पनीर, अंडे, मछली, चिकन","भरपूर पानी और तरल"],less:["शराब, पूरी तरह और हमेशा के लिए","धूम्रपान","तला खाना और एक बार में बहुत ज़्यादा खाना","ट्राइग्लिसराइड या शुगर ज़्यादा हो तो चीनी, मिठाई और मीठे पेय"],know:["एक बार के दौरे के बाद, ठीक होने पर ज़्यादातर लोग सामान्य, संतुलित खाना खा सकते हैं","क्रॉनिक पैंक्रियाटाइटिस में फ़ैट बहुत कम न करें; खाने के साथ एंज़ाइम कैप्सूल इसे पचाने में मदद करते हैं","अगर दौरा पित्त की पथरी से हुआ था, तो पित्ताशय निकालने से दोबारा दौरा नहीं होता","उल्टी के साथ अचानक तेज़ दर्द में इमरजेंसी इलाज चाहिए"]},
 {n:"दस्त (लूज़ मोशन)",more:["ORS, घूँट-घूँट बार-बार","खिचड़ी, दही-चावल, केला, दाल का पानी","नारियल पानी और पतला सूप","आराम"],less:["तला और तीखा खाना","दूध, अगर इससे दस्त बढ़ें","फलों के जूस और कोल्ड ड्रिंक","खून या बुखार हो तो बिना सलाह दस्त रोकने की गोली"],know:["पैकेट वाला WHO ORS सबसे अच्छा है। घर पर: 1 लीटर साफ़ पानी में 6 समतल चम्मच चीनी और आधा समतल चम्मच नमक","मल में खून, तेज़ बुखार या बहुत कम पेशाब हो तो डॉक्टर को दिखाएँ","दो हफ़्ते से ज़्यादा दस्त में जाँच ज़रूरी है"]}
];'''

PAIRS += [
 ('const PFX="/";', 'const PFX="/hi/";'),
 ('const MORE="Read the full guide →";', 'const MORE="पूरी जानकारी पढ़ें →";'),
 ('const MOREP="Read more about this procedure →";', 'const MOREP="इस प्रोसीजर के बारे में और पढ़ें →";'),
]

# Replaces the block between /*PLAY*/ and /*/PLAY*/ (Myth Buster and fibre counter text and foods).
PLAY_JS = r'''/*PLAY*/
const MB={eyebrow:"भ्रम या सच?",ask:"आपको क्या लगता है?",myth:"भ्रम",fact:"सच",isMyth:"यह भ्रम है",isFact:"यह सच है",right:"आपने सही पहचाना!",wrong:"सही नहीं। बहुत लोग ऐसा ही मानते हैं।",doLbl:"इसकी जगह क्या करें",doLblF:"क्या करें",docLbl:"डॉक्टर को कब दिखाएँ",more:"और पढ़ें →",share:"परिवार को WhatsApp पर चुनौती दें",shareTail:"अंदाज़ा लगाइए, फिर डॉ. क्षितिज लोचब से जवाब जानिए:",next:d=>d===1?"अगला भ्रम: कल":`अगला भ्रम ${d} दिन में`,nextDefault:"हर सोमवार और गुरुवार एक नया भ्रम",score:(r,n)=>`आपका स्कोर: <b>${n} में से ${r}</b> सही`,past:"पिछले भ्रम",hint:"जवाब देखने के लिए टैप करें",go:"ख़ुद को परखें →",err:"भ्रम लोड नहीं हो पाया। कृपया पेज रीफ़्रेश करें।",latest:"नया",of:(i,n)=>`${n} में से ${i}`,nextBtn:"अगला भ्रम →",prevA:"पिछला भ्रम",nextA:"अगला भ्रम"};
const FT={reset:"फिर से शुरू करें",u:"ग्राम",legend:"हर सर्विंग में",add:f=>`${f.n} जोड़ें, ${f.s}: फ़ाइबर ${f.f} ग्राम, प्रोटीन ${f.p} ग्राम, फ़ैट ${f.t} ग्राम`,sub:f=>`एक ${f.n} हटाएँ`,
 meters:{f:{n:"फ़ाइबर",t:"कम से कम 25–30 ग्राम",st:["कम","सही दिशा में","अच्छा"]},p:{n:"प्रोटीन",t:"लक्ष्य लगभग 45–55 ग्राम",st:["कम","सही दिशा में","अच्छा"]},t:{n:"फ़ैट",t:"कुल मिलाकर लगभग 60 ग्राम से कम",st:["ठीक","ध्यान दें","बहुत ज़्यादा"]}},
 msg:{start:"आज आपने जो खाया है, उस पर टैप करें।",fat:"आज फ़ैट ज़्यादा है। तेल, घी और तली चीज़ें कम करें।",prot:"थोड़ा प्रोटीन जोड़ें: दाल, दही, पनीर, अंडा, चिकन या मछली।",fib:"फ़ाइबर जोड़ें: एक फल, एक कटोरी सब्ज़ी या दाल।",good:"आज की थाली अच्छी संतुलित है। आपका पेट शुक्रिया कहेगा!"},
 cats:{g:"रोटी, चावल, पोहा और अनाज",d:"दाल और चने",m:"दूध, दही और पनीर",n:"अंडा, चिकन, मछली और मीट",v:"सब्ज़ियाँ",f:"फल और मेवे",k:"चाय, कॉफ़ी और पेय",o:"तेल, घी और नाश्ता",s:"मिठाई"},jump:"सीधे जाएँ",
 note:"ये मात्राएँ घर की एक आम सर्विंग के हिसाब से मोटा अनुमान हैं, जो भारतीय फ़ूड कंपोज़िशन टेबल (ICMR-NIN) और USDA के आँकड़ों से निकाली गई हैं। दाल, सब्ज़ी और करी में हर कटोरी में लगभग 1 छोटा चम्मच तेल गिना गया है; ऊपर से डाला घी, मक्खन या तेल अलग से जोड़ें। चीनी यहाँ नहीं गिनी गई है, इसलिए मीठी चाय, जूस, कोल्ड ड्रिंक और मिठाई कम ही रखें। ज़्यादातर बड़ों के लिए ICMR-NIN लगभग 0.8 से 1 ग्राम प्रोटीन प्रति किलो वज़न (रोज़ लगभग 45 से 55 ग्राम) और दिन भर में 4 से 5 छोटे चम्मच से ज़्यादा तेल या घी न लेने की सलाह देता है। किडनी या लिवर की बीमारी हो तो डॉक्टर से पूछें कि आपके लिए कितना प्रोटीन ठीक है; फैटी लिवर में फ़ैट और तेल कम रखें। फ़ाइबर धीरे-धीरे बढ़ाएँ और साथ में पानी ज़्यादा पिएँ। आपकी सूची सिर्फ़ आज के लिए इसी फ़ोन पर रहती है, कल फिर आइए और नई थाली गिनिए।",
 hookK:"थाली मीटर",hookQ:"फ़ाइबर, प्रोटीन, फ़ैट: आज आपकी थाली कैसी है?",hookGo:"अपनी थाली गिनें →",hookHave:(f,p,t)=>`आज: फ़ाइबर ${f} · प्रोटीन ${p} · फ़ैट ${t} ग्राम`,hookTop:"और जोड़ें →"};
const FOODS=[
 {c:"g",n:"आटे की रोटी",s:"1 मीडियम रोटी",f:3,p:3,t:0.5},{c:"g",n:"बाजरा या ज्वार की रोटी",s:"1 रोटी",f:3.5,p:3.5,t:1.5},{c:"g",n:"सादा पराठा, घी या तेल वाला",s:"1 पराठा",f:3.5,p:4,t:8},
 {c:"g",n:"ओट्स, पानी में बने",s:"1 बाउल",f:4,p:5,t:2.5},{c:"g",n:"ब्राउन राइस",s:"1 कटोरी",f:2.5,p:4,t:1.5},{c:"g",n:"सफ़ेद चावल",s:"1 कटोरी",f:0.5,p:4,t:0.5},
 {c:"g",n:"इडली",s:"2 इडली",f:1.5,p:4,t:0.5},{c:"g",n:"सादा डोसा",s:"1 डोसा",f:1,p:3,t:4},{c:"g",n:"सफ़ेद ब्रेड",s:"2 स्लाइस",f:1.5,p:4.5,t:1.5},
 {c:"g",n:"ब्राउन या होल व्हीट ब्रेड",s:"2 स्लाइस",f:3,p:6,t:2},{c:"d",n:"दाल, तड़के वाली",s:"1 कटोरी",f:3,p:7,t:3},{c:"d",n:"राजमा या छोले",s:"1 कटोरी",f:7,p:9,t:6},
 {c:"d",n:"भुने चने, छिलके वाले",s:"1 मुट्ठी",f:4,p:6,t:1.5},{c:"d",n:"सोया चंक्स की सब्ज़ी",s:"1 कटोरी",f:3,p:13,t:5},{c:"m",n:"दूध (टोंड)",s:"1 गिलास",f:0,p:6.5,t:6},
 {c:"m",n:"दही",s:"1 कटोरी",f:0,p:4.5,t:4.5},{c:"m",n:"छाछ",s:"1 गिलास",f:0,p:2,t:1},{c:"m",n:"पनीर",s:"50 ग्राम, लगभग 5 टुकड़े",f:0,p:9,t:10},
 {c:"n",n:"अंडा, उबला",s:"1 अंडा",f:0,p:6,t:5},{c:"n",n:"चिकन करी",s:"1 कटोरी, लगभग 100 ग्राम मीट",f:0,p:25,t:12},{c:"n",n:"मछली करी",s:"1 कटोरी, लगभग 100 ग्राम मछली",f:0,p:20,t:7},
 {c:"v",n:"मिक्स सब्ज़ी",s:"1 कटोरी",f:3,p:2,t:5},{c:"v",n:"आलू की सब्ज़ी",s:"1 कटोरी",f:2.5,p:2.5,t:5},{c:"v",n:"मटर",s:"1 कटोरी",f:5,p:5,t:5},
 {c:"v",n:"भिंडी",s:"1 कटोरी",f:2.5,p:2,t:6},{c:"v",n:"पालक या साग",s:"1 कटोरी",f:3.5,p:4,t:5},{c:"v",n:"गोभी",s:"1 कटोरी",f:2.5,p:2,t:5},
 {c:"v",n:"बीन्स",s:"1 कटोरी",f:3,p:2,t:5},{c:"v",n:"बैंगन",s:"1 कटोरी",f:2.5,p:1,t:6},{c:"v",n:"पत्ता गोभी",s:"1 कटोरी",f:2,p:1.5,t:5},
 {c:"v",n:"लौकी या तोरी",s:"1 कटोरी",f:1,p:1,t:4},{c:"v",n:"गाजर, कच्ची",s:"1 मीडियम",f:2,p:0.5,t:0},{c:"v",n:"शकरकंदी, भुनी",s:"1 मीडियम",f:4,p:2.5,t:0},
 {c:"v",n:"भुट्टा, भुना",s:"1 भुट्टा",f:2.5,p:3,t:1.5},{c:"v",n:"सलाद",s:"1 प्लेट",f:2,p:1,t:0},{c:"f",n:"अमरूद",s:"1 फल",f:5,p:2.5,t:1},
 {c:"f",n:"नाशपाती",s:"1 फल",f:5.5,p:0.5,t:0},{c:"f",n:"सेब, छिलके समेत",s:"1 फल",f:4,p:0.5,t:0},{c:"f",n:"अनार",s:"1 कटोरी दाने",f:3.5,p:1.5,t:1},
 {c:"f",n:"केला",s:"1 फल",f:3,p:1.5,t:0.5},{c:"f",n:"संतरा",s:"1 फल",f:3,p:1,t:0},{c:"f",n:"पपीता",s:"1 बाउल",f:2.5,p:0.5,t:0.5},
 {c:"f",n:"बादाम",s:"1 मुट्ठी, लगभग 20",f:3,p:5,t:12},{c:"f",n:"मूँगफली, भुनी",s:"1 मुट्ठी",f:2.5,p:7,t:15},{c:"o",n:"ऊपर से घी, मक्खन या तेल",s:"1 छोटा चम्मच",f:0,p:0,t:5},
 {c:"o",n:"समोसा",s:"1 समोसा",f:2,p:4,t:15},{c:"o",n:"पकौड़े",s:"1 प्लेट, लगभग 6",f:3,p:5,t:15},{c:"o",n:"नमकीन या भुजिया",s:"1 छोटी कटोरी",f:1.5,p:4,t:10},
 {c:"o",n:"चिप्स",s:"1 छोटा पैकेट",f:1,p:1.5,t:9},{c:"o",n:"क्रीम बिस्कुट",s:"4 बिस्कुट",f:0.5,p:2,t:8},{c:"k",n:"चाय, दूध वाली",s:"1 कप",f:0,p:2,t:2},
 {c:"k",n:"कॉफ़ी, दूध वाली",s:"1 कप",f:0,p:3,t:3},{c:"k",n:"बिना दूध की चाय, ग्रीन टी या ब्लैक कॉफ़ी",s:"1 कप",f:0,p:0,t:0},{c:"k",n:"लस्सी, मीठी या नमकीन",s:"1 गिलास",f:0,p:5,t:5},
 {c:"k",n:"मिल्कशेक (केला या आम)",s:"1 गिलास",f:1,p:7,t:6},{c:"k",n:"नींबू पानी या शिकंजी",s:"1 गिलास",f:0,p:0,t:0},{c:"k",n:"नारियल पानी",s:"1 गिलास",f:1,p:1.5,t:0.5},
 {c:"k",n:"फलों का जूस",s:"1 गिलास",f:0.5,p:1,t:0},{c:"k",n:"कोल्ड ड्रिंक",s:"1 कैन या गिलास",f:0,p:0,t:0},{c:"g",n:"पूरी",s:"2 पूरी",f:3,p:3,t:9},
 {c:"g",n:"भटूरा",s:"1 भटूरा",f:1.5,p:5,t:12},{c:"g",n:"आलू पराठा",s:"1 पराठा",f:5,p:5,t:10},{c:"g",n:"पोहा",s:"1 प्लेट",f:2,p:4,t:7},
 {c:"g",n:"उपमा",s:"1 प्लेट",f:2.5,p:5,t:8},{c:"g",n:"बेसन का चीला",s:"1 चीला",f:4,p:8,t:7},{c:"g",n:"वेज पुलाव या जीरा राइस",s:"1 कटोरी",f:1.5,p:4,t:5},
 {c:"g",n:"मसाला डोसा",s:"1 डोसा",f:2.5,p:5,t:10},{c:"g",n:"खिचड़ी",s:"1 बाउल",f:2,p:7,t:5},{c:"d",n:"सांभर",s:"1 कटोरी",f:3,p:4,t:3},
 {c:"d",n:"कढ़ी",s:"1 कटोरी",f:1,p:5,t:7},{c:"d",n:"अंकुरित मूँग (स्प्राउट्स), चाट या सलाद",s:"1 कटोरी",f:4,p:7,t:1},{c:"m",n:"पनीर की सब्ज़ी (भुर्जी या मटर पनीर)",s:"1 कटोरी",f:1.5,p:11,t:17},
 {c:"m",n:"रायता",s:"1 कटोरी",f:0.5,p:4,t:4},{c:"n",n:"ऑमलेट या अंडा भुर्जी",s:"2 अंडे",f:0.5,p:12,t:15},{c:"n",n:"अंडा करी",s:"2 अंडे, ग्रेवी में",f:1,p:13,t:15},
 {c:"n",n:"तंदूरी या ग्रिल्ड चिकन",s:"लगभग 100 ग्राम मीट",f:0,p:26,t:7},{c:"n",n:"बटर चिकन",s:"1 कटोरी, लगभग 100 ग्राम मीट",f:1,p:25,t:22},{c:"n",n:"चिकन बिरयानी",s:"1 प्लेट",f:1.5,p:22,t:16},
 {c:"n",n:"फ़िश फ़्राई",s:"1 टुकड़ा, लगभग 100 ग्राम",f:0.5,p:20,t:12},{c:"n",n:"मटन करी",s:"1 कटोरी, लगभग 100 ग्राम मीट",f:0.5,p:22,t:18},{c:"n",n:"चिकन मोमोज़, स्टीम्ड",s:"1 प्लेट, 6 मोमोज़",f:1.5,p:14,t:7},
 {c:"f",n:"आम",s:"1 फल",f:2.5,p:1,t:0.5},{c:"f",n:"तरबूज़ या ख़रबूज़ा",s:"1 बाउल",f:0.5,p:1,t:0},{c:"f",n:"अंगूर",s:"1 कटोरी",f:1,p:0.5,t:0},
 {c:"f",n:"खजूर",s:"3 खजूर",f:2,p:0.5,t:0},{c:"o",n:"कचौड़ी",s:"1 कचौड़ी",f:2,p:4,t:13},{c:"o",n:"मेदु वड़ा",s:"2 वड़े",f:3,p:7,t:10},
 {c:"o",n:"वेज मोमोज़, स्टीम्ड",s:"1 प्लेट, 6 मोमोज़",f:2,p:6,t:5},{c:"o",n:"पाव भाजी",s:"1 प्लेट, 2 पाव",f:6,p:9,t:18},{c:"o",n:"पिज़्ज़ा",s:"2 स्लाइस",f:2.5,p:13,t:14},
 {c:"o",n:"इंस्टेंट नूडल्स",s:"1 पैकेट",f:1.5,p:6,t:12},{c:"o",n:"रस्क या सादे बिस्कुट",s:"2 रस्क या 4 बिस्कुट",f:0.5,p:2,t:3},{c:"s",n:"जलेबी",s:"2 जलेबी",f:0,p:1,t:7},
 {c:"s",n:"गुलाब जामुन",s:"1 पीस",f:0,p:1.5,t:6},{c:"s",n:"लड्डू या बर्फ़ी",s:"1 पीस",f:0.5,p:2,t:7},{c:"s",n:"खीर या सेवइयाँ",s:"1 कटोरी",f:0.5,p:5,t:6},
 {c:"s",n:"आइसक्रीम",s:"1 स्कूप",f:0,p:2.5,t:7},{c:"g",n:"म्यूज़्ली या कॉर्नफ़्लेक्स, दूध के साथ",s:"1 बाउल",f:1.5,p:8,t:6.5},{c:"g",n:"दलिया, सब्ज़ियों के साथ",s:"1 बाउल",f:5,p:5,t:3},
 {c:"g",n:"रागी (नाचनी) की रोटी या दलिया",s:"1 रोटी या 1 बाउल",f:3.5,p:2,t:0.5},{c:"g",n:"किनोआ, पका हुआ",s:"1 कटोरी",f:4,p:6.5,t:3},{c:"g",n:"रेड सॉस पास्ता",s:"1 प्लेट",f:4,p:10,t:9},
 {c:"g",n:"व्हाइट सॉस पास्ता",s:"1 प्लेट",f:2.5,p:14,t:20},{c:"g",n:"वेज सैंडविच, होल व्हीट ब्रेड",s:"1 सैंडविच",f:4,p:7,t:6},{c:"g",n:"दही चावल",s:"1 कटोरी",f:0.5,p:7,t:5},
 {c:"d",n:"मूँग दाल का चीला",s:"1 चीला",f:3,p:8,t:6},{c:"m",n:"हंग कर्ड या ग्रीक योगर्ट",s:"1 कटोरी",f:0,p:12,t:6},{c:"n",n:"ग्रिल्ड या स्टीम्ड मछली",s:"1 टुकड़ा, लगभग 100 ग्राम",f:0,p:22,t:4},
 {c:"n",n:"ग्रिल्ड चिकन या फ़िश सलाद",s:"1 बाउल",f:3,p:26,t:8},{c:"n",n:"चिकन सूप, साफ़",s:"1 बाउल",f:0.5,p:8,t:3},{c:"v",n:"सब्ज़ियों का साफ़ सूप",s:"1 बाउल",f:2,p:1.5,t:1.5},
 {c:"f",n:"कीवी",s:"1 फल",f:2.5,p:1,t:0.5},{c:"f",n:"प्रून्स (सूखे आलूबुख़ारे)",s:"4 से 5 प्रून्स",f:3,p:1,t:0},{c:"f",n:"अखरोट",s:"4 साबुत अखरोट, लगभग 15 ग्राम",f:1,p:2.5,t:10},
 {c:"f",n:"मखाना, भुना",s:"1 बाउल",f:2,p:2.5,t:3},{c:"f",n:"इसबगोल, पानी में",s:"1 बड़ा चम्मच",f:4,p:0,t:0},{c:"k",n:"ORS",s:"1 गिलास",f:0,p:0,t:0},
 {c:"o",n:"बर्गर (आलू टिक्की या चिकन)",s:"1 बर्गर",f:2.5,p:12,t:15},{c:"o",n:"अचार",s:"1 छोटा चम्मच",f:0,p:0,t:2.5},{c:"o",n:"पापड़",s:"1 पापड़, भुना",f:1,p:2.5,t:0.5},
 {c:"s",n:"चॉकलेट",s:"2 छोटे टुकड़े, लगभग 20 ग्राम",f:0.5,p:1.5,t:6}
];
'''
