"""Hindi version of drlochab.com. build_site.py applies these to the English source to make /hi/index.html.
Every English string listed here must exist in the source; the build stops if one is missing,
so text changed on the English page is never silently left untranslated."""

# Exact text replacements for page markup, interface strings and illustration labels.
PAIRS = [
 # header
 ('<a class="brand" href="#top" aria-label="Dr. Kshitij Lochab, home">', '<a class="brand" href="#top" aria-label="डॉ. क्षितिज लोचब, होम">'),
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
 ('<p class="eyebrow">Gastroenterologist · Gurugram</p>', '<p class="eyebrow">गैस्ट्रोएंटेरोलॉजिस्ट · गुरुग्राम</p>'),
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
 ('<h2>Common gut and liver problems</h2>', '<h2>पेट और लिवर की आम बीमारियाँ</h2>'),
 ('<p class="lede">Tap a part of the digestive system to see the conditions that affect it. Open any card to read the signs, what helps, and when to get checked.</p>',
  '<p class="lede">पाचन तंत्र के किसी हिस्से पर टैप करें और उससे जुड़ी बीमारियाँ देखें। किसी भी कार्ड को खोलकर पढ़ें कि लक्षण क्या हैं, क्या मदद करता है, और जाँच कब करवानी चाहिए।</p>'),
 ('aria-label="Digestive system map"', 'aria-label="पाचन तंत्र का नक्शा"'),
 ('role="button" aria-label="Intestines"', 'role="button" aria-label="आँतें"'),
 ('role="button" aria-label="Pancreas"', 'role="button" aria-label="पैंक्रियास"'),
 ('role="button" aria-label="Liver"', 'role="button" aria-label="लिवर"'),
 ('role="button" aria-label="Gallbladder and bile ducts"', 'role="button" aria-label="पित्ताशय और पित्त नली"'),
 ('role="button" aria-label="Food pipe and stomach"', 'role="button" aria-label="खाने की नली और पेट"'),
 ('<p class="map-cap">Tap an organ. Tap it again to show all.</p>', '<p class="map-cap">किसी अंग पर टैप करें। सब देखने के लिए दोबारा टैप करें।</p>'),
 ('aria-label="Filter by organ"', 'aria-label="अंग के हिसाब से देखें"'),

 # procedures
 ('<p class="eyebrow">Tests &amp; procedures</p>', '<p class="eyebrow">जाँच और इलाज</p>'),
 ('<h2>What to expect from an endoscopy</h2>', '<h2>एंडोस्कोपी में क्या होता है</h2>'),
 ('<p class="lede">Most procedures use a thin, flexible tube with a camera. There are no cuts, and most people go home the same day. The simple drawings show where the scope goes and what it does.</p>',
  '<p class="lede">ज़्यादातर प्रोसीजर में कैमरे वाली एक पतली, मुड़ने वाली नली इस्तेमाल होती है। कोई चीरा नहीं लगता और ज़्यादातर लोग उसी दिन घर चले जाते हैं। आसान चित्रों में दिखाया गया है कि स्कोप कहाँ जाता है और क्या करता है।</p>'),

 # myths
 ('<p class="eyebrow">Myths and facts</p>', '<p class="eyebrow">भ्रम और सच</p>'),
 ('<h2>Things patients often believe</h2>', '<h2>मरीज़ अक्सर ये बातें मानते हैं</h2>'),

 # about
 ('<h2>Dr. Kshitij Lochab<span>Consultant Gastroenterologist &amp; Therapeutic Endoscopist</span></h2>',
  '<h2>डॉ. क्षितिज लोचब<span>कंसल्टेंट गैस्ट्रोएंटेरोलॉजिस्ट और थेराप्यूटिक एंडोस्कोपिस्ट</span></h2>'),
 ('<p class="lede">I treat diseases of the food pipe, stomach, intestines, liver, gallbladder and pancreas. My special training is in advanced endoscopy, which lets many problems that once needed surgery be treated through a scope instead. I take time to explain your condition and your options, so that every decision is one we make together.</p>',
  '<p class="lede">मैं खाने की नली, पेट, आँतों, लिवर, पित्ताशय और पैंक्रियास की बीमारियों का इलाज करता हूँ। मेरी विशेष ट्रेनिंग एडवांस्ड एंडोस्कोपी में है, जिससे कई ऐसी बीमारियाँ, जिनके लिए पहले ऑपरेशन करना पड़ता था, अब स्कोप से ठीक हो जाती हैं। मैं आपकी बीमारी और इलाज के विकल्प आराम से समझाता हूँ, ताकि हर फ़ैसला हम मिलकर लें।</p>'),
 ('>Areas of care</p>', '>इलाज के क्षेत्र</p>'),
 ('<span>Fatty liver &amp; hepatitis</span><span>Cirrhosis &amp; GI bleeding</span><span>Bile duct &amp; pancreas</span><span>Acidity &amp; ulcers</span><span>IBS &amp; IBD</span><span>Colon polyps &amp; screening</span><span>Swallowing problems</span>',
  '<span>फैटी लिवर और हेपेटाइटिस</span><span>सिरोसिस और पेट से खून आना</span><span>पित्त नली और पैंक्रियास</span><span>एसिडिटी और अल्सर</span><span>IBS और IBD</span><span>आँत के पॉलिप और जाँच</span><span>निगलने में तकलीफ़</span>'),
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
 ('<address id="addr"><strong>Arcura Clinic</strong><br>M2K Corporate Park &amp; Shopping Plaza<br>14, Mayfield Garden, Sector 51<br>Gurugram, Haryana 122018</address>',
  '<address id="addr"><strong>आर्क्योरा क्लिनिक (Arcura Clinic)</strong><br>M2K कॉर्पोरेट पार्क एंड शॉपिंग प्लाज़ा<br>14, मेफ़ील्ड गार्डन, सेक्टर 51<br>गुरुग्राम, हरियाणा 122018</address>'),
 ('rel="noopener">Get directions</a>', 'rel="noopener">रास्ता देखें</a>'),
 ('id="copyAddr" type="button">Copy address</button>', 'id="copyAddr" type="button">पता कॉपी करें</button>'),
 ('<p>Visited recently? You can share your experience on <a href="https://g.page/r/CYmK8BpICDd6EBM/review" target="_blank" rel="noopener" style="color:var(--warm)">Google</a>. It helps others find the right care.</p>',
  '<p>हाल ही में आए थे? अपना अनुभव <a href="https://g.page/r/CYmK8BpICDd6EBM/review" target="_blank" rel="noopener" style="color:var(--warm)">Google</a> पर शेयर करें। इससे दूसरों को सही इलाज ढूँढने में मदद मिलती है।</p>'),
 ('<p>Also consulting at Apollo Hospitals, Golf Course Road, Gurugram.</p>', '<p>अपोलो हॉस्पिटल्स, गोल्फ़ कोर्स रोड, गुरुग्राम में भी देखते हैं।</p>'),
 ('aria-label="Book on WhatsApp">', 'aria-label="WhatsApp पर अपॉइंटमेंट">'),
 ('</svg>\n  Book\n</a>', '</svg>\n  अपॉइंटमेंट\n</a>'),

 # footer
 ('<p>This website is for general health education. It does not replace a consultation with a doctor, and nothing here is a diagnosis or treatment plan for any individual.</p>',
  '<p>यह वेबसाइट सामान्य स्वास्थ्य जानकारी के लिए है। यह डॉक्टर की सलाह की जगह नहीं ले सकती, और यहाँ लिखी कोई भी बात किसी व्यक्ति के लिए डायग्नोसिस या इलाज की योजना नहीं है।</p>'),
 ('<p>In a medical emergency, call 112 or go to the nearest emergency department.</p>', '<p>मेडिकल इमरजेंसी में 112 पर कॉल करें या सबसे पास की इमरजेंसी में जाएँ।</p>'),
 ('<p>Dr. Kshitij Lochab · Haryana Medical Council Reg. No. HN-23524 · +91 96671 04882</p>', '<p>डॉ. क्षितिज लोचब · हरियाणा मेडिकल काउंसिल रजि. नं. HN-23524 · +91 96671 04882</p>'),
 ('<p>© 2026 Dr. Kshitij Lochab</p>', '<p>© 2026 डॉ. क्षितिज लोचब</p>'),

 # script: interface strings
 ('`<span class="pill ${cls}">${lbl}</span><h3>${esc(x.l)}</h3><dl><div><dt>Common causes</dt><dd>${esc(x.c)}</dd></div><div><dt>What to do</dt>',
  '`<span class="pill ${cls}">${lbl}</span><h3>${esc(x.l)}</h3><dl><div><dt>आम वजहें</dt><dd>${esc(x.c)}</dd></div><div><dt>क्या करें</dt>'),
 ('[["all","All"],...Object.entries(ORGANS)]', '[["all","सभी"],...Object.entries(ORGANS)]'),
 ('count.textContent=k==="all"?`Showing all ${items.length} conditions`:`${items.length} condition${items.length>1?"s":""} affecting the ${ORGANS[k].toLowerCase()}`;',
  'count.textContent=k==="all"?`सभी ${items.length} बीमारियाँ`:`${ORGANS[k]} की ${items.length} बीमारियाँ`;'),
 ('<h4>Common signs</h4>', '<h4>आम लक्षण</h4>'),
 ('<h4>What helps</h4>', '<h4>क्या मदद करता है</h4>'),
 ('<h4>When to see a gastroenterologist</h4>', '<h4>गैस्ट्रोएंटेरोलॉजिस्ट को कब दिखाएँ</h4>'),
 ('<span class="lbl">Myth</span>', '<span class="lbl">भ्रम</span>'),
 ('<span class="lbl">Fact</span>', '<span class="lbl">सच</span>'),
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
 {il:"dil",n:"डाइलेटेशन और स्टेंटिंग",a:"सिकुड़न खोलना",w:"खाने की नली, पित्त नली या आँत के सिकुड़े हिस्से को बैलून से चौड़ा किया जाता है, या स्कोप से स्टेंट डालकर खुला रखा जाता है।",d:[["तैयारी","6 से 8 घंटे कुछ न खाएँ"],["समय","लगभग 20 से 45 मिनट"],["आराम","हल्की बेहोशी में"],["बाद में","खाना धीरे-धीरे बढ़ाया जाता है"]]}
];

const MYTHS=[
 ["फैटी लिवर से कोई नुकसान नहीं, इलाज की ज़रूरत नहीं।","फैटी लिवर धीरे-धीरे लिवर में स्कारिंग कर सकता है। अच्छी बात यह है कि शुरुआती फैटी लिवर वज़न घटाने और व्यायाम से ठीक हो सकता है।"],
 ["एंडोस्कोपी में बहुत दर्द होता है।","एंडोस्कोपी में आम तौर पर कुछ ही मिनट लगते हैं और यह गले के स्प्रे या हल्की बेहोशी के साथ होती है। ज़्यादातर लोग हैरान होते हैं कि यह कितनी आसान थी।"],
 ["लिवर की बीमारी सिर्फ़ शराब पीने वालों को होती है।","वज़न और डायबिटीज़ से फैटी लिवर, हेपेटाइटिस B और C, और कुछ दवाइयाँ व जड़ी-बूटी वाले सप्लीमेंट भी लिवर को नुकसान पहुँचा सकते हैं।"],
 ["पीलिया आराम और घरेलू नुस्खों से अपने आप ठीक हो जाएगा।","पीलिया एक संकेत है जिसकी वजह जाननी ज़रूरी है। कुछ वजहों, जैसे पित्त नली में रुकावट, का जल्दी इलाज ज़रूरी है।"],
 ["आँत का कैंसर सिर्फ़ बुढ़ापे में होता है।","यह अब कम उम्र के लोगों में भी बढ़ रहा है। मल में खून या शौच की आदत में लंबा बदलाव हो तो किसी भी उम्र में जाँच करवाएँ।"]
];

'''

# Replaces the GUIDES array in the English source.
GUIDES_JS = r'''const GUIDES=[
 {n:"फैटी लिवर",more:["हर खाने में सब्ज़ियाँ और सलाद","साबुत अनाज: चोकर वाला आटा, बाजरा-रागी, ओट्स, ब्राउन राइस","प्रोटीन के लिए दाल, चना, राजमा और अंकुरित अनाज","जूस की जगह साबुत फल","कम चीनी वाली सादी चाय या कॉफ़ी"],less:["कोल्ड ड्रिंक, पैकेट वाले जूस और मिठाइयाँ","तले स्नैक्स, नमकीन और बेकरी की चीज़ें","मैदा: सफ़ेद ब्रेड, बिस्किट, नूडल्स","प्रोसेस्ड और रेड मीट","शराब, जिसे पूरी तरह छोड़ना सबसे अच्छा है"],know:["शरीर का 7 से 10% वज़न घटाने से शुरुआती फैटी लिवर ठीक हो सकता है","हफ़्ते में लगभग 150 मिनट तेज़ चलना वज़न घटने से पहले ही फ़ायदा देता है","स्कारिंग की जाँच के लिए लिवर स्टिफ़नेस टेस्ट करवाएँ"]},
 {n:"एसिडिटी और रिफ़्लक्स",more:["थोड़ा-थोड़ा, बार-बार खाना","सोने से कम से कम 3 घंटे पहले रात का खाना","ओट्स, पकी सब्ज़ियाँ, केला और पपीता जैसे कम खट्टे फल","खाने के बीच में पानी","खाने के बाद थोड़ी देर टहलना"],less:["देर रात भारी खाना","तला और बहुत चिकना खाना","ज़्यादा चाय, कॉफ़ी और सोडा","चॉकलेट और पुदीना, जो अक्सर जलन बढ़ाते हैं","शराब और तंबाकू"],know:["हर व्यक्ति में जलन बढ़ाने वाली चीज़ें अलग होती हैं; दो हफ़्ते की खाने की डायरी से अपनी चीज़ें पहचानें","रात की तकलीफ़ में पलंग का सिर वाला हिस्सा 6 से 8 इंच ऊँचा करें","निगलने में दिक्कत या वज़न घटे तो विशेषज्ञ को दिखाएँ"]},
 {n:"IBS और पेट फूलना",more:["खाने का तय समय","घुलने वाला फ़ाइबर: ओट्स, इसबगोल, पकी सब्ज़ियाँ","दही और छाछ, अगर सूट करें","दिन भर में पर्याप्त पानी","धीरे-धीरे, चबाकर खाना"],less:["राजमा, चना, प्याज़ और लहसुन ज़्यादा मात्रा में, अगर इनसे तकलीफ़ बढ़े","सोडा और कोल्ड ड्रिंक","सॉर्बिटॉल वाली शुगर-फ़्री च्युइंग गम और मिठाइयाँ","ज़्यादा चाय और कॉफ़ी","बहुत तीखा या तैलीय खाना"],know:["सही मार्गदर्शन में लो-FODMAP डाइट कई लोगों की मदद करती है","तनाव और कम नींद से लक्षण बढ़ते हैं","45 के बाद नए लक्षण, खून आना या वज़न घटे तो पहले जाँच ज़रूरी है"]},
 {n:"कब्ज़",more:["रोज़ 25 से 30 ग्राम फ़ाइबर, धीरे-धीरे बढ़ाएँ","छिलके वाले फल: अमरूद, नाशपाती, सेब; और पपीता","साबुत अनाज, दाल और सब्ज़ियाँ","इतना पानी कि पेशाब हल्का पीला रहे","रोज़ टहलना या व्यायाम"],less:["मैदा और पैकेट वाले स्नैक्स","नाश्ता छोड़ना","शौच की इच्छा को रोकना","बिना सलाह लंबे समय तक तेज़ जुलाब"],know:["नाश्ते के बाद छोटे स्टूल पर पैर रखकर शौच के लिए बैठें","इसबगोल पर्याप्त पानी के साथ ही काम करता है","45 के बाद नई कब्ज़ या मल में खून हो तो जाँच करवाएँ"]},
 {n:"पीलिया के बाद",more:["पर्याप्त कैलोरी वाला सामान्य, संतुलित घर का खाना","दाल, दही, फल और सब्ज़ियाँ","भरपूर साफ़, उबला या फ़िल्टर किया पानी","भूख कम हो तो थोड़ा-थोड़ा बार-बार खाना","थकान रहने तक आराम"],less:["शराब, पूरी तरह","डॉक्टर के लिखे बिना जड़ी-बूटी और दवाइयाँ","सड़क का खाना और असुरक्षित पानी"],know:["आम खाने में डलने वाली हल्दी, तेल या नमक छोड़ने की ज़रूरत नहीं","सिर्फ़ उबला खाना खाने से कमज़ोरी आती है और ठीक होने में देर लगती है","बुखार, भ्रम, ज़्यादा नींद या खून आए तो तुरंत दिखाएँ"]},
 {n:"सिरोसिस",more:["पर्याप्त प्रोटीन: दाल, पनीर, दही, अंडे, मछली या चिकन","हर 3 से 4 घंटे में थोड़ा खाना","सोने से पहले हल्का नाश्ता, जैसे रोटी के साथ दूध या पोहा","ताज़ा घर का खाना"],less:["ऊपर से नमक, पापड़, अचार, नमकीन और पैकेट वाला खाना, अगर सूजन है","शराब, पूरी तरह","कच्चा या अधपका मीट और सी-फ़ूड"],know:["डॉक्टर न कहें तो प्रोटीन कम न करें","सोने से पहले का नाश्ता माँसपेशियों को बचाता है","सूजन हो तो पानी की मात्रा पर डॉक्टर की सलाह मानें"]},
 {n:"पैंक्रियाटाइटिस के बाद",more:["थोड़ा-थोड़ा, बार-बार, कम चिकनाई वाला खाना","उबला, भाप में पका या हल्का पका खाना","कम चर्बी वाला प्रोटीन: दाल, दही, अंडे की सफ़ेदी, मछली, चिकन","भरपूर पानी और तरल"],less:["तला और तैलीय खाना","शराब, पूरी तरह","धूम्रपान","एक बार में बहुत ज़्यादा खाना"],know:["क्रॉनिक पैंक्रियाटाइटिस में खाने के साथ एंज़ाइम कैप्सूल दिए जा सकते हैं","तैलीय, बदबूदार मल का मतलब पाचन की दोबारा जाँच ज़रूरी है","उल्टी के साथ अचानक तेज़ दर्द में इमरजेंसी इलाज चाहिए"]},
 {n:"दस्त (लूज़ मोशन)",more:["ORS, घूँट-घूँट बार-बार","खिचड़ी, दही-चावल, केला, दाल का पानी","नारियल पानी और पतला सूप","आराम"],less:["तला और तीखा खाना","दूध, अगर इससे दस्त बढ़ें","फलों के जूस और कोल्ड ड्रिंक","खून या बुखार हो तो बिना सलाह दस्त रोकने की गोली"],know:["घर का ORS: 1 लीटर साफ़ पानी में 6 चम्मच (समतल) चीनी और आधा चम्मच नमक","मल में खून, तेज़ बुखार या बहुत कम पेशाब हो तो डॉक्टर को दिखाएँ","दो हफ़्ते से ज़्यादा दस्त में जाँच ज़रूरी है"]}
];'''

PAIRS += [
 ('const PFX="/";', 'const PFX="/hi/";'),
 ('const MORE="Read the full guide →";', 'const MORE="पूरी जानकारी पढ़ें →";'),
 ('const MOREP="Read more about this procedure →";', 'const MOREP="इस प्रोसीजर के बारे में और पढ़ें →";'),
 ('<p class="eyebrow">Your questions answered</p>', '<p class="eyebrow">आपके सवालों के जवाब</p>'),
 ('<h2>Answers to questions patients often ask</h2>', '<h2>मरीज़ों के आम सवालों के जवाब</h2>'),
]
