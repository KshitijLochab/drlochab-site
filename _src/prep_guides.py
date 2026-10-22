"""Preparation guides for colonoscopy and upper GI endoscopy (EN + HI), 22 Oct 2026.
Pages: /guides/colonoscopy-preparation/ and /guides/endoscopy-preparation/ (and /hi/...).
Each page has a planner: the patient picks the date and time of the test and gets a dated, timed plan,
which can be saved to the phone calendar (.ics made in the browser) or sent on WhatsApp. Nothing is stored or sent by the site.
Timings follow the existing procedure pages: low-fibre diet from 2 days before, clear liquids from noon the day before,
split bowel preparation (evening before, then starting about 5 hours before and finishing 2 hours before), nothing to eat
for at least 6 hours before an endoscopy and sips of water until 2 hours before. No brand names or doses."""
import json, html as _html
e = lambda x: _html.escape(x, quote=True)
UPD = ("2026-10-22", "22 October 2026", "22 अक्टूबर 2026")
SLUGS = {"colonoscopy": "colonoscopy-preparation", "endoscopy": "endoscopy-preparation"}
PROC_OF = {"colonoscopy": 1, "endoscopy": 0}          # index in seo_en.PROCS (illustration and links)
# procedure pages that link to a preparation guide
PROC_LINK = {"upper-gi-endoscopy": "endoscopy", "colonoscopy": "colonoscopy", "endoscopic-ultrasound-eus": "endoscopy",
             "variceal-banding-evl": "endoscopy", "polyp-removal-emr": "colonoscopy"}

# step timing: ("day", n, "HH:MM" or None) = n days before at a clock time; ("rel", minutes) = minutes before the test
STEPS = {
 "colonoscopy": [("day", 7, None), ("day", 2, None), ("day", 1, "12:00"), ("day", 1, "19:00"), ("rel", 300), ("rel", 120), ("rel", 30), ("rel", 0)],
 "endoscopy": [("day", 1, None), ("meal", 360), ("rel", 120), ("rel", 30), ("rel", 0)],
}

T = {
"en": dict(
 planner_h="Your plan, with dates and times", planner_p="Enter the date and time of your test. The plan below updates to show exactly when to do each step.",
 date_lbl="Date of the test", time_lbl="Time of the test", ics="Save reminders to my calendar", wa="Send this plan on WhatsApp",
 plan_note="This is a general plan. If your hospital gives you a different instruction sheet, follow theirs.",
 early="The second half falls very early in the morning. Some hospitals give the whole preparation the evening before for early tests, so check your instruction sheet.",
 wa_head="My {n} plan (from drlochab.com):", print="Print or save as PDF", bring_h="What to bring", bring_p="Tick them off the night before.",
 after_h="After the test", alarm_h="Call the hospital or go to an emergency department if you have", read_h="Read next",
 eyebrow="Before your test", short_lbl="In short", toc_lbl="On this page", book="Questions about your preparation? Message on WhatsApp",
 asap="As soon as possible", rel={"day": ["the day of the test", "1 day before", "{n} days before"], "at": "at", "before_m": "{n} minutes before", "before_h": "{n} hours before", "time0": "At the test time", "dinner": "The night before, by 10 pm"},
),
"hi": dict(
 planner_h="तारीख़ और समय के साथ आपका प्लान", planner_p="अपनी जाँच की तारीख़ और समय डालें। नीचे का प्लान बता देगा कि हर काम ठीक कब करना है।",
 date_lbl="जाँच की तारीख़", time_lbl="जाँच का समय", ics="रिमाइंडर मेरे कैलेंडर में सेव करें", wa="यह प्लान WhatsApp पर भेजें",
 plan_note="यह एक सामान्य प्लान है। अगर आपके अस्पताल ने अलग निर्देश दिए हैं, तो उन्हीं का पालन करें।",
 early="दूसरी खुराक बहुत सुबह पड़ रही है। सुबह जल्दी की जाँच के लिए कुछ अस्पताल पूरी दवा एक रात पहले देते हैं, इसलिए अपना निर्देश पत्र देखें।",
 wa_head="मेरा {n} प्लान (drlochab.com से):", print="प्रिंट करें या PDF सेव करें", bring_h="साथ क्या लाएँ", bring_p="एक रात पहले इन्हें टिक कर लें।",
 after_h="जाँच के बाद", alarm_h="इनमें से कुछ हो तो अस्पताल को फ़ोन करें या इमरजेंसी में जाएँ", read_h="आगे पढ़ें",
 eyebrow="जाँच से पहले", short_lbl="संक्षेप में", toc_lbl="इस पेज पर", book="तैयारी के बारे में सवाल? WhatsApp पर मैसेज करें",
 asap="जितनी जल्दी हो सके", rel={"day": ["जाँच के दिन", "1 दिन पहले", "{n} दिन पहले"], "at": "", "before_m": "{n} मिनट पहले", "before_h": "{n} घंटे पहले", "time0": "जाँच के समय", "dinner": "एक रात पहले, 10 बजे तक"},
),
}

G = {
"colonoscopy": {
"en": dict(
 n="colonoscopy", name="Colonoscopy preparation",
 h1="How to prepare for a colonoscopy: a day-by-day plan",
 title="Colonoscopy preparation: day-by-day plan | Dr. Lochab",
 desc="How to prepare for a colonoscopy: low-fibre diet, clear liquids, when to drink the bowel preparation, medicines to check and what to bring, with a dated plan.",
 lead="A colonoscopy is only as good as the bowel preparation. When the bowel is clean, even small polyps can be seen and removed; when it is not, the test may have to be repeated. Preparing takes two days of simple changes and one evening and morning of drinking the cleansing solution. This page turns that into a plan with your own dates and times.",
 short="Eat low-fibre food for 2 days before, switch to clear liquids from noon the day before, and drink the bowel preparation in two halves: the evening before and again starting about 5 hours before the test. Stop all drinks 2 hours before, and come with someone who can take you home.",
 toc=["Your plan", "What to eat", "Drinking the preparation", "Medicines", "What to bring", "After the test"],
 steps=["Stop iron tablets. Ask your doctor about blood thinners, diabetes medicines and insulin.",
        "Start the low-fibre diet: no seeds, salads, whole grains or fruit with peel.",
        "Low-fibre breakfast in the morning, then clear liquids only from 12 noon.",
        "First half of the bowel preparation. Drink it over 1 to 2 hours, then keep sipping clear liquids.",
        "Second half of the bowel preparation. Finish it within about an hour.",
        "Stop all drinks, including water.",
        "Reach the hospital with an adult who can take you home.",
        "Colonoscopy"],
 food_h="What to eat before a colonoscopy",
 food_p="Fibre and seeds stay in the bowel and hide the lining, so the two days before are about plain, soft, low-fibre food.",
 eat_h="Eat (2 days before)", eat=["White rice, khichdi made with dhuli moong, suji upma or idli", "White bread, plain dosa, poha without peanuts", "Curd, paneer, eggs, fish or chicken without skin", "Boiled potato without peel, bottle gourd or pumpkin cooked soft", "Banana, papaya without seeds"],
 avoid_h="Avoid (2 days before)", avoid=["Seeds: til, flax, chia, tomato and cucumber seeds, guava", "Salads, leafy greens, peas, corn, rajma, chana and dal with skins", "Whole wheat, bajra, oats, multigrain atta and brown rice", "Nuts, dry fruits and fruit with peel", "Iron tablets (from a week before)"],
 clear_h="Clear liquids (from noon the day before)", clear=["Water, ORS and coconut water", "Clear soup without bits", "Tea or coffee without milk", "Light-coloured juice without pulp, nimbu pani", "No milk, lassi, red or purple drinks"],
 drink_h="Drinking the preparation",
 drink_p="The cleansing solution is the hardest part. These tips make it easier:",
 drink=["Chill it in the fridge and drink it through a straw", "Drink a glass every 10 to 15 minutes rather than all at once", "Walk around between glasses; it helps the bowel move", "Suck a lemon slice or sip clear juice between glasses", "If you feel sick, pause for 30 minutes, then continue more slowly", "Stay near a toilet; loose motions start within 1 to 3 hours"],
 clear_scale_h="How do you know the bowel is clean?", clear_scale=["Brown and thick", "Dark yellow with bits", "Clear yellow, like urine"], clear_scale_lbl=["Not ready", "Almost", "Ready"],
 clear_scale_p="By the end of the second half, your stool should be clear, yellow liquid. If it is still brown, call the hospital before you leave.",
 meds_h="Medicines to check a week before", meds_p="Do not stop any medicine on your own. Tell your doctor about these when the test is booked:",
 meds=[("Blood thinners", "Aspirin, clopidogrel and other blood thinners may need to be paused if polyps are removed. This is decided with the doctor who prescribed them."),
       ("Diabetes medicines and insulin", "You eat less during the preparation, so the dose usually needs to change for a day or two to avoid low sugar. Check your sugar more often."),
       ("Iron tablets", "Stop them about a week before. They make the bowel dark and sticky."),
       ("BP, heart and thyroid tablets", "Usually continued, with a small sip of water on the morning of the test."),
       ("Kidney or heart disease, older age", "The preparation causes fluid loss. Tell the doctor, as you may need a different solution or extra care.")],
 bring=["An adult to take you home (you cannot drive after sedation)", "Previous colonoscopy and biopsy reports", "A list of all your medicines", "Your appointment details and ID", "Loose, comfortable clothes", "Leave jewellery and valuables at home"],
 after=["You rest for about an hour. Bloating and passing wind for a few hours are normal.", "Eat a light meal first, then your normal food, unless you are told otherwise after polyp removal.", "Do not drive, work with machines or sign important papers for the rest of the day.", "Biopsy and polyp reports usually take about a week."],
 alarm=["Severe or worsening belly pain, or a hard, swollen belly", "More than a few spoonfuls of blood from the back passage", "Fever, dizziness or fainting", "During the preparation: vomiting that stops you drinking it, or feeling faint"],
 faqs=[["Can I drink tea on the day before?", "Yes, tea or coffee without milk is a clear liquid. Stop all drinks 2 hours before the test."],
       ["What if I vomit the preparation?", "Stop for 30 minutes, then drink more slowly. If you cannot keep it down at all, call the hospital, as the test may need to be rescheduled."],
       ["What if my stool is not clear by the morning?", "Call the hospital before you leave home. A poorly prepared bowel can hide polyps, and the team may give you extra preparation or a new date."],
       ["Why the low-fibre diet?", "Fibre, seeds and peels stay in the bowel even after the cleansing drink and can hide the lining or block the scope."],
       ["Is a colonoscopy painful?", "It is usually done under sedation. You may feel some cramping or wind, which settles soon after. The preparation is often the hardest part."],
       ["Do I need someone with me?", "Yes. After sedation you should not drive or travel alone for the rest of the day."]],
),
"hi": dict(
 n="कोलोनोस्कोपी", name="कोलोनोस्कोपी की तैयारी",
 h1="कोलोनोस्कोपी की तैयारी कैसे करें: दिन-ब-दिन प्लान",
 title="कोलोनोस्कोपी की तैयारी: दिन-ब-दिन प्लान | डॉ. लोचब",
 desc="कोलोनोस्कोपी की तैयारी: कम फ़ाइबर वाला खाना, साफ़ तरल, पेट साफ़ करने की दवा कब पिएँ, कौन-सी दवाएँ पूछें और साथ क्या लाएँ, तारीख़ वाले प्लान के साथ।",
 lead="कोलोनोस्कोपी उतनी ही अच्छी होती है जितनी आँत की सफ़ाई। आँत साफ़ हो तो छोटे पॉलिप भी दिख जाते हैं और निकाले जा सकते हैं; साफ़ न हो तो जाँच दोबारा करनी पड़ सकती है। तैयारी में दो दिन खाने में आसान बदलाव और एक शाम व सुबह आँत साफ़ करने की दवा पीना शामिल है। यह पेज इसे आपकी अपनी तारीख़ और समय के साथ एक प्लान में बदल देता है।",
 short="जाँच से 2 दिन पहले कम फ़ाइबर वाला खाना खाएँ, एक दिन पहले दोपहर 12 बजे से सिर्फ़ साफ़ तरल लें, और आँत साफ़ करने की दवा दो हिस्सों में पिएँ: एक रात पहले, और फिर जाँच से करीब 5 घंटे पहले। जाँच से 2 घंटे पहले सब कुछ पीना बंद करें, और किसी को साथ लाएँ जो आपको घर ले जा सके।",
 toc=["आपका प्लान", "क्या खाएँ", "दवा पीना", "दवाइयाँ", "साथ क्या लाएँ", "जाँच के बाद"],
 steps=["आयरन की गोलियाँ बंद करें। ख़ून पतला करने की दवा, डायबिटीज़ की दवा और इंसुलिन के बारे में डॉक्टर से पूछें।",
        "कम फ़ाइबर वाला खाना शुरू करें: बीज, सलाद, साबुत अनाज और छिलके वाले फल नहीं।",
        "सुबह कम फ़ाइबर वाला नाश्ता, फिर दोपहर 12 बजे से सिर्फ़ साफ़ तरल।",
        "आँत साफ़ करने की दवा का पहला हिस्सा। इसे 1 से 2 घंटे में पिएँ, फिर साफ़ तरल लेते रहें।",
        "दवा का दूसरा हिस्सा। इसे करीब एक घंटे में ख़त्म करें।",
        "पानी समेत सब कुछ पीना बंद करें।",
        "किसी बड़े व्यक्ति के साथ अस्पताल पहुँचें जो आपको घर ले जा सके।",
        "कोलोनोस्कोपी"],
 food_h="कोलोनोस्कोपी से पहले क्या खाएँ",
 food_p="फ़ाइबर और बीज आँत में रह जाते हैं और अंदर की परत को ढक देते हैं, इसलिए पिछले दो दिन सादा, नरम, कम फ़ाइबर वाला खाना खाना है।",
 eat_h="खाएँ (2 दिन पहले से)", eat=["सफ़ेद चावल, धुली मूँग की खिचड़ी, सूजी उपमा या इडली", "सफ़ेद ब्रेड, सादा डोसा, बिना मूँगफली का पोहा", "दही, पनीर, अंडा, बिना खाल की मछली या चिकन", "बिना छिलके का उबला आलू, नरम पकी लौकी या कद्दू", "केला, बिना बीज का पपीता"],
 avoid_h="न खाएँ (2 दिन पहले से)", avoid=["बीज: तिल, अलसी, चिया, टमाटर और खीरे के बीज, अमरूद", "सलाद, हरी पत्तेदार सब्ज़ियाँ, मटर, भुट्टा, राजमा, चना और छिलके वाली दाल", "आटा, बाजरा, ओट्स, मल्टीग्रेन आटा और ब्राउन राइस", "मेवे, ड्राई फ़्रूट और छिलके वाले फल", "आयरन की गोलियाँ (एक हफ़्ते पहले से)"],
 clear_h="साफ़ तरल (एक दिन पहले दोपहर से)", clear=["पानी, ORS और नारियल पानी", "बिना टुकड़ों का साफ़ सूप", "बिना दूध की चाय या कॉफ़ी", "बिना गूदे का हल्के रंग का जूस, नींबू पानी", "दूध, लस्सी, लाल या बैंगनी ड्रिंक नहीं"],
 drink_h="आँत साफ़ करने की दवा पीना",
 drink_p="यह दवा पीना सबसे मुश्किल हिस्सा है। ये तरीके इसे आसान बनाते हैं:",
 drink=["इसे फ़्रिज में ठंडा करें और स्ट्रॉ से पिएँ", "एक साथ नहीं, हर 10 से 15 मिनट में एक गिलास पिएँ", "गिलासों के बीच टहलें; इससे आँत चलती है", "बीच में नींबू की फाँक चूसें या साफ़ जूस का घूँट लें", "जी मिचलाए तो 30 मिनट रुकें, फिर धीरे-धीरे पिएँ", "टॉयलेट के पास रहें; 1 से 3 घंटे में दस्त शुरू हो जाते हैं"],
 clear_scale_h="कैसे पता चले कि आँत साफ़ हो गई?", clear_scale=["भूरा और गाढ़ा", "गहरा पीला, टुकड़ों के साथ", "साफ़ पीला, पेशाब जैसा"], clear_scale_lbl=["अभी नहीं", "लगभग", "तैयार"],
 clear_scale_p="दूसरे हिस्से के अंत तक मल साफ़, पीला पानी जैसा हो जाना चाहिए। अगर अब भी भूरा है, तो निकलने से पहले अस्पताल को फ़ोन करें।",
 meds_h="एक हफ़्ते पहले ये दवाएँ पूछ लें", meds_p="कोई भी दवा ख़ुद से बंद न करें। जाँच बुक करते समय डॉक्टर को इनके बारे में बताएँ:",
 meds=[("ख़ून पतला करने की दवाएँ", "पॉलिप निकालने हों तो एस्पिरिन, क्लोपिडोग्रेल और दूसरी ख़ून पतला करने की दवाएँ रोकनी पड़ सकती हैं। यह दवा लिखने वाले डॉक्टर के साथ तय होता है।"),
       ("डायबिटीज़ की दवा और इंसुलिन", "तैयारी में आप कम खाते हैं, इसलिए शुगर कम होने से बचाने के लिए एक-दो दिन दवा बदलनी पड़ती है। शुगर ज़्यादा बार जाँचें।"),
       ("आयरन की गोलियाँ", "करीब एक हफ़्ते पहले बंद करें। इनसे आँत काली और चिपचिपी हो जाती है।"),
       ("BP, दिल और थायरॉइड की गोलियाँ", "आम तौर पर चलती रहती हैं, जाँच की सुबह पानी के छोटे घूँट के साथ।"),
       ("किडनी या दिल की बीमारी, ज़्यादा उम्र", "तैयारी में शरीर से पानी निकलता है। डॉक्टर को बताएँ, क्योंकि अलग दवा या ज़्यादा देखभाल की ज़रूरत हो सकती है।")],
 bring=["एक बड़ा व्यक्ति जो आपको घर ले जाए (बेहोशी की दवा के बाद गाड़ी नहीं चला सकते)", "पुरानी कोलोनोस्कोपी और बायोप्सी रिपोर्ट", "अपनी सभी दवाओं की सूची", "अपॉइंटमेंट की जानकारी और पहचान पत्र", "ढीले, आरामदायक कपड़े", "गहने और कीमती सामान घर पर छोड़ें"],
 after=["आप करीब एक घंटा आराम करते हैं। कुछ घंटे पेट फूलना और गैस निकलना आम है।", "पहले हल्का खाना खाएँ, फिर सामान्य खाना, जब तक पॉलिप निकालने के बाद कुछ और न कहा जाए।", "बाकी दिन गाड़ी न चलाएँ, मशीन पर काम न करें और ज़रूरी काग़ज़ों पर दस्तख़त न करें।", "बायोप्सी और पॉलिप की रिपोर्ट में आम तौर पर करीब एक हफ़्ता लगता है।"],
 alarm=["पेट में तेज़ या बढ़ता दर्द, या सख़्त, फूला हुआ पेट", "मल द्वार से कुछ चम्मच से ज़्यादा ख़ून", "बुख़ार, चक्कर या बेहोशी", "तैयारी के दौरान: इतनी उल्टी कि दवा न पी सकें, या बेहोशी जैसा लगना"],
 faqs=[["क्या एक दिन पहले चाय पी सकते हैं?", "हाँ, बिना दूध की चाय या कॉफ़ी साफ़ तरल है। जाँच से 2 घंटे पहले सब कुछ पीना बंद करें।"],
       ["दवा पीते हुए उल्टी हो जाए तो?", "30 मिनट रुकें, फिर धीरे-धीरे पिएँ। अगर बिल्कुल नहीं रुक रही, तो अस्पताल को फ़ोन करें, जाँच की तारीख़ बदलनी पड़ सकती है।"],
       ["सुबह तक मल साफ़ न हो तो?", "घर से निकलने से पहले अस्पताल को फ़ोन करें। ठीक से साफ़ न हुई आँत में पॉलिप छिप सकते हैं, और टीम आपको और दवा या नई तारीख़ दे सकती है।"],
       ["कम फ़ाइबर वाला खाना क्यों?", "फ़ाइबर, बीज और छिलके दवा के बाद भी आँत में रह जाते हैं और परत को ढक सकते हैं या स्कोप में फँस सकते हैं।"],
       ["क्या कोलोनोस्कोपी में दर्द होता है?", "यह आम तौर पर बेहोशी की हल्की दवा देकर की जाती है। कुछ ऐंठन या गैस महसूस हो सकती है, जो जल्दी ठीक हो जाती है। तैयारी अक्सर सबसे मुश्किल हिस्सा होती है।"],
       ["क्या किसी को साथ लाना ज़रूरी है?", "हाँ। बेहोशी की दवा के बाद बाकी दिन गाड़ी चलाना या अकेले सफ़र करना ठीक नहीं।"]],
),
},
"endoscopy": {
"en": dict(
 n="endoscopy", name="Endoscopy preparation",
 h1="How to prepare for an endoscopy: fasting, medicines and what to bring",
 title="Endoscopy preparation: fasting and what to bring | Dr. Lochab",
 desc="How to prepare for an upper GI endoscopy: when to stop eating and drinking, which medicines to check, what to bring and what happens after, with a timed plan.",
 lead="An upper GI endoscopy needs very little preparation: an empty stomach, a check of your medicines and someone to take you home if you have sedation. An empty stomach lets the doctor see the lining clearly and keeps you safe during the test. Enter your test time below to get your own plan.",
 short="Nothing to eat for at least 6 hours before the test. Small sips of plain water are fine until 2 hours before, then nothing at all. Take BP and thyroid tablets with a small sip of water, check diabetes medicines and blood thinners with your doctor, and come with an adult if you will have sedation.",
 toc=["Your plan", "Eating and drinking", "Medicines", "What to bring", "After the test"],
 steps=["Confirm your medicine plan with your doctor: blood thinners, diabetes medicines and insulin.",
        "Last light meal. Nothing to eat after this.",
        "Last sips of plain water. Nothing by mouth after this.",
        "Reach the hospital with an adult who can take you home if you have sedation.",
        "Endoscopy"],
 food_h="Eating and drinking before an endoscopy",
 food_p="Food left in the stomach hides the lining and can be brought up during the test.",
 eat_h="Until 6 hours before", eat=["A light meal: khichdi, idli, poha, toast or dal-chawal", "Avoid heavy, fried or very spicy food the night before", "For a morning test, have dinner by about 10 pm"],
 avoid_h="In the last 6 hours", avoid=["No food, chewing gum, paan or tobacco", "No milk, tea with milk or juice", "No smoking on the morning of the test"],
 clear_h="Until 2 hours before", clear=["Small sips of plain water", "Your morning BP and thyroid tablets with a sip of water", "Nothing at all in the last 2 hours"],
 meds_h="Medicines to check before the test", meds_p="Do not stop any medicine on your own. Tell your doctor about these when the test is booked:",
 meds=[("Blood thinners", "Some can continue for a simple endoscopy; others are paused if biopsies or treatment are likely. This is planned with the doctor who prescribed them."),
       ("Diabetes medicines and insulin", "You will be fasting, so the morning dose usually needs to change. Bring your glucometer and something sweet for after the test."),
       ("Acidity tablets", "If the test is to look for H. pylori, you may be asked to stop acidity tablets for about 2 weeks before, as they can hide the infection."),
       ("BP, heart and thyroid tablets", "Usually taken as normal on the morning of the test with a small sip of water.")],
 bring=["An adult to take you home if you will have sedation", "Previous endoscopy and biopsy reports", "A list of all your medicines", "Your appointment details and ID", "Your glucometer, if you have diabetes", "Remove dentures and spectacles before the test"],
 after=["If you had sedation, you rest for 30 to 60 minutes. Do not drive or sign important papers for the rest of the day.", "Eat and drink once the throat numbness wears off, usually after about an hour. Start with something light.", "A mild sore throat or bloating for a few hours is common.", "The doctor explains the findings the same day. Biopsy reports usually take 5 to 7 days."],
 alarm=["Severe chest, neck or belly pain after the test", "Vomiting blood or black, tarry stools", "Fever, breathlessness or difficulty swallowing"],
 faqs=[["Can I drink water before an endoscopy?", "Small sips of plain water are usually fine until 2 hours before the test. After that, nothing at all."],
       ["Can I take my BP tablet?", "Yes, BP, heart and thyroid tablets are usually taken in the morning with a small sip of water. Diabetes medicines are different: ask your doctor."],
       ["How long does an endoscopy take?", "The test itself takes about 5 to 10 minutes. With preparation and recovery, plan for 1 to 2 hours at the hospital."],
       ["Is an endoscopy painful?", "No, for most people. With a throat spray or light sedation you may feel pressure or the urge to burp, but not pain."],
       ["When can I eat after the test?", "Once the throat numbness wears off, usually after about an hour. Start with something light, such as water, then a light meal."]],
),
"hi": dict(
 n="एंडोस्कोपी", name="एंडोस्कोपी की तैयारी",
 h1="एंडोस्कोपी की तैयारी कैसे करें: खाली पेट, दवाइयाँ और साथ क्या लाएँ",
 title="एंडोस्कोपी की तैयारी: खाली पेट और साथ क्या लाएँ | डॉ. लोचब",
 desc="अपर GI एंडोस्कोपी की तैयारी: कब खाना-पीना बंद करें, कौन-सी दवाएँ पूछें, साथ क्या लाएँ और बाद में क्या होता है, समय वाले प्लान के साथ।",
 lead="अपर GI एंडोस्कोपी में बहुत कम तैयारी लगती है: खाली पेट, दवाओं की जाँच, और बेहोशी की दवा लेनी हो तो कोई साथ जो घर ले जाए। खाली पेट से डॉक्टर अंदर की परत साफ़ देख पाते हैं और जाँच सुरक्षित रहती है। अपना प्लान पाने के लिए नीचे जाँच का समय डालें।",
 short="जाँच से कम से कम 6 घंटे पहले तक कुछ न खाएँ। 2 घंटे पहले तक सादे पानी के छोटे घूँट ठीक हैं, उसके बाद कुछ भी नहीं। BP और थायरॉइड की गोली पानी के छोटे घूँट से लें, डायबिटीज़ की दवा और ख़ून पतला करने की दवा के बारे में डॉक्टर से पूछें, और बेहोशी की दवा लेनी हो तो किसी बड़े को साथ लाएँ।",
 toc=["आपका प्लान", "खाना-पीना", "दवाइयाँ", "साथ क्या लाएँ", "जाँच के बाद"],
 steps=["दवाओं का प्लान डॉक्टर से पक्का करें: ख़ून पतला करने की दवा, डायबिटीज़ की दवा और इंसुलिन।",
        "आख़िरी हल्का खाना। इसके बाद कुछ न खाएँ।",
        "सादे पानी के आख़िरी घूँट। इसके बाद मुँह से कुछ नहीं।",
        "बेहोशी की दवा लेनी हो तो किसी बड़े व्यक्ति के साथ अस्पताल पहुँचें।",
        "एंडोस्कोपी"],
 food_h="एंडोस्कोपी से पहले खाना-पीना",
 food_p="पेट में बचा खाना अंदर की परत को ढक देता है और जाँच के दौरान ऊपर आ सकता है।",
 eat_h="6 घंटे पहले तक", eat=["हल्का खाना: खिचड़ी, इडली, पोहा, टोस्ट या दाल-चावल", "एक रात पहले भारी, तला या बहुत मसालेदार खाना न खाएँ", "सुबह की जाँच हो तो रात का खाना करीब 10 बजे तक खा लें"],
 avoid_h="आख़िरी 6 घंटों में", avoid=["कोई खाना, च्युइंग गम, पान या तंबाकू नहीं", "दूध, दूध वाली चाय या जूस नहीं", "जाँच की सुबह धूम्रपान नहीं"],
 clear_h="2 घंटे पहले तक", clear=["सादे पानी के छोटे घूँट", "सुबह की BP और थायरॉइड की गोली पानी के घूँट से", "आख़िरी 2 घंटों में बिल्कुल कुछ नहीं"],
 meds_h="जाँच से पहले ये दवाएँ पूछ लें", meds_p="कोई भी दवा ख़ुद से बंद न करें। जाँच बुक करते समय डॉक्टर को इनके बारे में बताएँ:",
 meds=[("ख़ून पतला करने की दवाएँ", "साधारण एंडोस्कोपी में कुछ दवाएँ चलती रह सकती हैं; बायोप्सी या इलाज की संभावना हो तो कुछ रोकनी पड़ती हैं। यह दवा लिखने वाले डॉक्टर के साथ तय होता है।"),
       ("डायबिटीज़ की दवा और इंसुलिन", "आप खाली पेट रहेंगे, इसलिए सुबह की दवा आम तौर पर बदलनी पड़ती है। ग्लूकोमीटर और जाँच के बाद के लिए कुछ मीठा साथ लाएँ।"),
       ("एसिडिटी की गोलियाँ", "अगर जाँच H. pylori देखने के लिए है, तो करीब 2 हफ़्ते पहले एसिडिटी की गोलियाँ बंद करने को कहा जा सकता है, क्योंकि ये इंफ़ेक्शन को छिपा सकती हैं।"),
       ("BP, दिल और थायरॉइड की गोलियाँ", "आम तौर पर जाँच की सुबह पानी के छोटे घूँट के साथ हमेशा की तरह ली जाती हैं।")],
 bring=["बेहोशी की दवा लेनी हो तो एक बड़ा व्यक्ति जो घर ले जाए", "पुरानी एंडोस्कोपी और बायोप्सी रिपोर्ट", "अपनी सभी दवाओं की सूची", "अपॉइंटमेंट की जानकारी और पहचान पत्र", "डायबिटीज़ हो तो अपना ग्लूकोमीटर", "जाँच से पहले नकली दाँत और चश्मा उतार दें"],
 after=["बेहोशी की दवा ली हो तो 30 से 60 मिनट आराम करते हैं। बाकी दिन गाड़ी न चलाएँ और ज़रूरी काग़ज़ों पर दस्तख़त न करें।", "गले का सुन्नपन जाने के बाद खाएँ-पिएँ, आम तौर पर करीब एक घंटे बाद। हल्के खाने से शुरू करें।", "कुछ घंटे हल्की गले की ख़राश या पेट फूलना आम है।", "डॉक्टर उसी दिन नतीजे बताते हैं। बायोप्सी रिपोर्ट में आम तौर पर 5 से 7 दिन लगते हैं।"],
 alarm=["जाँच के बाद सीने, गर्दन या पेट में तेज़ दर्द", "ख़ून की उल्टी या काला, तारकोल जैसा मल", "बुख़ार, साँस फूलना या निगलने में तकलीफ़"],
 faqs=[["क्या एंडोस्कोपी से पहले पानी पी सकते हैं?", "आम तौर पर जाँच से 2 घंटे पहले तक सादे पानी के छोटे घूँट ठीक हैं। उसके बाद बिल्कुल कुछ नहीं।"],
       ["क्या मैं अपनी BP की गोली ले सकता हूँ?", "हाँ, BP, दिल और थायरॉइड की गोलियाँ आम तौर पर सुबह पानी के छोटे घूँट से ली जाती हैं। डायबिटीज़ की दवा अलग है: डॉक्टर से पूछें।"],
       ["एंडोस्कोपी में कितना समय लगता है?", "जाँच ख़ुद करीब 5 से 10 मिनट की होती है। तैयारी और आराम मिलाकर अस्पताल में 1 से 2 घंटे का समय रखें।"],
       ["क्या एंडोस्कोपी में दर्द होता है?", "ज़्यादातर लोगों को नहीं। गले के स्प्रे या हल्की बेहोशी की दवा के साथ दबाव या डकार जैसा लग सकता है, दर्द नहीं।"],
       ["जाँच के बाद कब खा सकते हैं?", "गले का सुन्नपन जाने के बाद, आम तौर पर करीब एक घंटे बाद। पहले पानी, फिर हल्के खाने से शुरू करें।"]],
),
},
}

def _check():
    for k in G:
        en, hi = G[k]["en"], G[k]["hi"]
        assert set(en) == set(hi), (k, set(en) ^ set(hi))
        for f in en:
            if isinstance(en[f], list):
                assert len(en[f]) == len(hi[f]), (k, f)
        assert len(en["steps"]) == len(STEPS[k]), k
_check()

def rel_label(lang, s):
    R = T[lang]["rel"]
    if s[0] == "day":
        n = s[1]; d = R["day"][0] if n == 0 else R["day"][1] if n == 1 else R["day"][2].format(n=n)
        if s[2]:
            h, m = map(int, s[2].split(":"))
            if lang == "en":
                tm = f"{(h - 1) % 12 + 1}{':%02d' % m if m else ''} {'am' if h < 12 else 'pm'}"
                tm = "12 noon" if (h, m) == (12, 0) else tm
                return f"{d}, {tm}"
            tm = f"{'दोपहर' if (h, m) == (12, 0) else 'शाम' if h >= 17 else 'सुबह'} {(h - 1) % 12 + 1}{':%02d' % m if m else ''} बजे"
            return f"{d}, {tm}"
        return d
    if s[0] == "meal":
        return R["before_h"].format(n=s[1] // 60)
    n = s[1]
    if n == 0: return R["time0"]
    return R["before_h"].format(n=n // 60) if n % 60 == 0 else R["before_m"].format(n=n)

CSS = """
.pp-plan{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:20px;margin:8px 0 28px;scroll-margin-top:90px}
.pp-plan h2{margin-bottom:6px}
.pp-in{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0 6px}
.pp-in label{display:grid;gap:6px;font-weight:600;font-size:.92rem;flex:1 1 150px}
.pp-in input,.pp-in select{font:inherit;font-weight:500;padding:10px 12px;border-radius:12px;border:1.5px solid var(--line);background:var(--bg);color:var(--ink);min-height:46px;width:100%}
.pp-steps{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:0}
.pp-steps li{display:grid;grid-template-columns:22px minmax(0,1fr);gap:2px 12px;position:relative;padding-bottom:16px}
.pp-steps li::before{content:"";width:14px;height:14px;border-radius:50%;background:var(--surface);border:3px solid var(--accent);margin-top:5px;grid-row:1/3;z-index:1}
.pp-steps li::after{content:"";position:absolute;left:8px;top:22px;bottom:-2px;width:3px;background:var(--accent-soft)}
.pp-steps li:last-child::after{display:none}
.pp-steps li:last-child::before{background:var(--accent)}
.pp-when{font-weight:700;color:var(--accent);font-size:.95rem}
.pp-what{grid-column:2}
.pp-past .pp-when{color:var(--urgent)}
.pp-act{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}
.pp-act[hidden]{display:none}
.pp-early{background:var(--warm-soft);border-radius:12px;padding:10px 14px;font-size:.92rem;margin:4px 0 12px}
.pp-cols{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.pp-cols .gcol.clear h3{color:var(--warm-text)}
.pp-scale{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:14px 0}
.pp-scale div{display:grid;justify-items:center;gap:6px;text-align:center;font-size:.88rem;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px 8px}
.pp-scale i{width:56px;height:56px;border-radius:50%;border:3px solid rgba(0,0,0,.08)}
.pp-scale b{font-size:.78rem;letter-spacing:.08em;text-transform:uppercase}
.pp-meds{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(260px,100%),1fr));gap:12px}
.pp-meds div{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:16px 18px}
.pp-meds h3{font-family:var(--body);font-weight:700;font-size:1rem}
.pp-meds p{margin:0;font-size:.95rem;color:var(--muted)}
.pp-check{list-style:none;padding:0;margin:12px 0 0;display:grid;gap:8px}
.pp-check label{display:flex;gap:12px;align-items:flex-start;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 14px;cursor:pointer}
.pp-check input{width:22px;height:22px;margin:2px 0 0;accent-color:var(--accent);flex:none}
.pp-check input:checked+span{text-decoration:line-through;color:var(--muted)}
@media (max-width:720px){.pp-cols{grid-template-columns:1fr}}
@media print{.pp-in,.pp-act,.pp-early{display:none!important}.pp-plan{border:0;padding:0}}
"""

JS = r"""(function(){
const D=__DATA__;
const dIn=document.getElementById('ppDate'),tIn=document.getElementById('ppTime'),list=document.getElementById('ppSteps'),act=document.getElementById('ppAct'),early=document.getElementById('ppEarly');
const loc=D.lang==='hi'?'hi-IN':'en-IN';
const fd=new Intl.DateTimeFormat(loc,{weekday:'short',day:'numeric',month:'short'}),fe=new Intl.DateTimeFormat('en-IN',{hour:'numeric',minute:'2-digit'});
const ft={format:x=>{if(D.lang!=='hi')return fe.format(x);const h=x.getHours(),pd=h>=4&&h<12?'सुबह':h>=12&&h<16?'दोपहर':h>=16&&h<20?'शाम':'रात';return pd+' '+((h+11)%12+1)+':'+String(x.getMinutes()).padStart(2,'0')+' बजे';}};
const p2=n=>String(n).padStart(2,'0');
const lbl=x=>fd.format(x.t)+(x.timed?', '+ft.format(x.t):'');
function past(x){const now=new Date(),today=new Date(now.getFullYear(),now.getMonth(),now.getDate());return x.timed?x.t<now:x.t<today;}
function times(){
  if(!dIn.value)return null;
  const [y,m,d]=dIn.value.split('-').map(Number),[h,mi]=tIn.value.split(':').map(Number);
  const T=new Date(y,m-1,d,h,mi);
  return D.steps.map(s=>{
    if(s[0]==='day'){const x=new Date(y,m-1,d-s[1]);if(s[2]){const [a,b]=s[2].split(':').map(Number);x.setHours(a,b);return {t:x,timed:true};}return {t:x,timed:false};}
    if(s[0]==='meal'){let x=new Date(T-s[1]*6e4);if(x.getHours()<6){x=new Date(y,m-1,d-1,22,0);}return {t:x,timed:true};}
    return {t:new Date(T-s[1]*6e4),timed:true};});
}
function render(){
  const ts=times();
  list.querySelectorAll('li').forEach((li,i)=>{const w=li.querySelector('.pp-when');const p=ts&&past(ts[i]);li.classList.toggle('pp-past',!!p);w.textContent=ts?(p?D.asap+' ('+lbl(ts[i])+')':lbl(ts[i])):D.rel[i];});
  act.hidden=!ts;
  if(early){const k=D.steps.findIndex(s=>s[0]==='rel'&&s[1]===300);early.hidden=!(ts&&k>=0&&ts[k].t.getHours()<4);}
  if(ts){
    const lines=ts.map((x,i)=>'• '+(past(x)?D.asap:lbl(x))+': '+D.what[i]);
    document.getElementById('ppWa').href='https://wa.me/?text='+encodeURIComponent(D.waHead+'\n'+lines.join('\n')+'\n'+D.url);
  }
}
document.getElementById('ppIcs').addEventListener('click',()=>{
  const ts=times();if(!ts)return;
  const f=x=>x.getFullYear()+p2(x.getMonth()+1)+p2(x.getDate())+'T'+p2(x.getHours())+p2(x.getMinutes())+'00';
  const fdOnly=x=>x.getFullYear()+p2(x.getMonth()+1)+p2(x.getDate());
  const esc=s=>s.replace(/[\\,;]/g,m=>'\\'+m);
  const stamp=f(new Date());
  let ics='BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//drlochab.com//prep//EN\r\nCALSCALE:GREGORIAN\r\n';
  ts.forEach((x,i)=>{
    if(past(x))return;
    ics+='BEGIN:VEVENT\r\nUID:'+D.slug+'-'+i+'-'+stamp+'@drlochab.com\r\nDTSTAMP:'+stamp+'\r\n';
    if(x.timed){const e2=new Date(+x.t+30*6e4);ics+='DTSTART:'+f(x.t)+'\r\nDTEND:'+f(e2)+'\r\n';}
    else{const n=new Date(x.t);n.setDate(n.getDate()+1);ics+='DTSTART;VALUE=DATE:'+fdOnly(x.t)+'\r\nDTEND;VALUE=DATE:'+fdOnly(n)+'\r\n';}
    ics+='SUMMARY:'+esc(D.short[i])+'\r\nDESCRIPTION:'+esc(D.what[i]+' '+D.url)+'\r\n';
    ics+='BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:'+esc(D.short[i])+'\r\nTRIGGER:'+(x.timed?'-PT15M':'PT8H')+'\r\nEND:VALARM\r\nEND:VEVENT\r\n';
  });
  ics+='END:VCALENDAR\r\n';
  const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([ics],{type:'text/calendar'}));a.download=D.slug+'.ics';document.body.appendChild(a);a.click();
  setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},1000);
});
dIn.addEventListener('change',render);tIn.addEventListener('change',render);
const t0=new Date();t0.setDate(t0.getDate());dIn.min=t0.getFullYear()+'-'+p2(t0.getMonth()+1)+'-'+p2(t0.getDate());
render();
})();"""

SHORT = {  # calendar event titles (short)
 "colonoscopy": {"en": ["Stop iron tablets; check medicines", "Start low-fibre diet", "Clear liquids only from now", "Bowel prep: first half", "Bowel prep: second half", "Stop all drinks", "Leave for the hospital", "Colonoscopy"],
                 "hi": ["आयरन बंद करें; दवाएँ पूछें", "कम फ़ाइबर वाला खाना शुरू", "अब से सिर्फ़ साफ़ तरल", "आँत की दवा: पहला हिस्सा", "आँत की दवा: दूसरा हिस्सा", "सब कुछ पीना बंद", "अस्पताल के लिए निकलें", "कोलोनोस्कोपी"]},
 "endoscopy": {"en": ["Confirm medicine plan", "Last light meal", "Last sips of water", "Leave for the hospital", "Endoscopy"],
               "hi": ["दवाओं का प्लान पक्का करें", "आख़िरी हल्का खाना", "पानी के आख़िरी घूँट", "अस्पताल के लिए निकलें", "एंडोस्कोपी"]},
}

SCALE_COLOURS = ["#7A4A22", "#C99A2E", "#F2DC7A"]

def time_options(lang):
    out = []
    for h in range(7, 19):
        for m in (0, 30):
            if h == 18 and m: continue
            v = f"{h:02d}:{m:02d}"
            if lang == "en":
                lbl = f"{(h - 1) % 12 + 1}:{m:02d} {'am' if h < 12 else 'pm'}"
            else:
                lbl = f"{'सुबह' if h < 12 else 'दोपहर' if h < 16 else 'शाम'} {(h - 1) % 12 + 1}:{m:02d}"
            out.append(f'<option value="{v}"{" selected" if v == "09:00" else ""}>{lbl}</option>')
    return "".join(out)

def render(lang, bp, kind, D):
    import seo_en
    X, U = G[kind][lang], T[lang]
    slug = SLUGS[kind]
    path, path_en, path_hi = bp.url(lang, "guides", slug), bp.url("en", "guides", slug), bp.url("hi", "guides", slug)
    t = bp.L[lang]
    pj = PROC_OF[kind]
    pr = D["PROCS"][pj]
    rels = [rel_label(lang, s) for s in STEPS[kind]]
    data = dict(lang=lang, slug=slug, steps=STEPS[kind], rel=rels, what=X["steps"], short=SHORT[kind][lang],
                waHead=U["wa_head"].format(n=X["n"]), url=bp.SITE + path, asap=U["asap"])
    steps = "".join(f'<li><span class="pp-when">{e(r)}</span><span class="pp-what">{e(w)}</span></li>' for r, w in zip(rels, X["steps"]))
    ids = ["plan", "food", "drink", "medicines", "bring", "after"] if kind == "colonoscopy" else ["plan", "food", "medicines", "bring", "after"]
    toc = (f'<nav class="toc" aria-label="{e(U["toc_lbl"])}"><p class="lbl">{e(U["toc_lbl"])}</p>'
           + "".join(f'<a href="#{i}">{e(l_)}</a>' for i, l_ in zip(ids, X["toc"])) + "</nav>")
    plan = (f'<section class="pp-plan" id="plan"><h2>{e(U["planner_h"])}</h2><p>{e(U["planner_p"])}</p>'
            f'<div class="pp-in"><label>{e(U["date_lbl"])}<input type="date" id="ppDate"></label>'
            f'<label>{e(U["time_lbl"])}<select id="ppTime">{time_options(lang)}</select></label></div>'
            + (f'<p class="pp-early" id="ppEarly" hidden>{e(U["early"])}</p>' if kind == "colonoscopy" else "")
            + f'<ol class="pp-steps" id="ppSteps">{steps}</ol>'
            f'<div class="pp-act" id="ppAct" hidden><button type="button" class="btn btn-solid btn-sm" id="ppIcs">{e(U["ics"])}</button>'
            f'<a class="btn btn-wa btn-sm" id="ppWa" href="#" target="_blank" rel="noopener">{e(U["wa"])}</a></div>'
            f'<p class="small" style="margin:12px 0 0">{e(U["plan_note"])}</p></section>')
    food = (f'<section id="food"><h2>{e(X["food_h"])}</h2><p>{e(X["food_p"])}</p><div class="pp-cols">'
            f'<div class="gcol more"><h3>{e(X["eat_h"])}</h3>{bp.ul(X["eat"])}</div>'
            f'<div class="gcol less"><h3>{e(X["avoid_h"])}</h3>{bp.ul(X["avoid"])}</div>'
            f'<div class="gcol clear"><h3>{e(X["clear_h"])}</h3>{bp.ul(X["clear"])}</div></div></section>')
    drink = ""
    if kind == "colonoscopy":
        scale = "".join(f'<div><i style="background:{c}"></i><b>{e(l_)}</b><span>{e(s)}</span></div>'
                        for c, l_, s in zip(SCALE_COLOURS, X["clear_scale_lbl"], X["clear_scale"]))
        drink = (f'<section id="drink"><h2>{e(X["drink_h"])}</h2><p>{e(X["drink_p"])}</p>{bp.ul(X["drink"])}'
                 f'<h3 style="margin-top:18px">{e(X["clear_scale_h"])}</h3><div class="pp-scale">{scale}</div><p>{e(X["clear_scale_p"])}</p></section>')
    meds = (f'<section id="medicines"><h2>{e(X["meds_h"])}</h2><p>{e(X["meds_p"])}</p><div class="pp-meds">'
            + "".join(f'<div><h3>{e(h)}</h3><p>{e(p_)}</p></div>' for h, p_ in X["meds"]) + "</div></section>")
    bring = (f'<section id="bring"><h2>{e(U["bring_h"])}</h2><p>{e(U["bring_p"])}</p><ul class="pp-check">'
             + "".join(f'<li><label><input type="checkbox"><span>{e(b)}</span></label></li>' for b in X["bring"]) + "</ul></section>")
    after = (f'<section id="after"><h2>{e(U["after_h"])}</h2>{bp.ul(X["after"])}</section>'
             f'<section class="alarm"><h2>{e(U["alarm_h"])}</h2>{bp.ul(X["alarm"])}</section>')
    acts = (f'<p class="dc-jump" style="display:flex;flex-wrap:wrap;gap:10px"><a class="btn btn-solid btn-sm" href="#plan">{e(U["planner_h"])} →</a>'
            f'<button type="button" class="btn btn-ghost btn-sm" onclick="print()">{e(U["print"])}</button></p>')
    import seo_hi
    reads = [(bp.url(lang, "procedures", seo_en.PROCS[pj]["slug"]), pr["n"])] + bp.answer_links(lang, seo_en if lang == "en" else seo_hi, ["is-endoscopy-painful"]) + [
             (bp.url(lang, "guides", SLUGS["endoscopy" if kind == "colonoscopy" else "colonoscopy"]), G["endoscopy" if kind == "colonoscopy" else "colonoscopy"][lang]["name"])]
    body = (f'<figure class="fig">{D["IL"][pr["il"]]}</figure><p class="lead">{e(X["lead"])}</p>'
            f'<div class="short"><p class="lbl">{e(U["short_lbl"])}</p><p>{e(X["short"])}</p></div>' + acts + toc
            + plan + food + drink + meds + bring + after + bp.faq_html(lang, X["faqs"])
            + f'<section><h2>{e(U["read_h"])}</h2>{bp.links(reads)}</section>')
    js = "<script>" + JS.replace("__DATA__", json.dumps(data, ensure_ascii=False)) + "</script>"
    ld = bp.ld_page(lang, path, X["h1"], X["desc"], "MedicalProcedure", pr["n"], X["faqs"], t["procs"], "procedures", UPD)
    page = (bp.head(lang, X["title"], X["desc"], path_en, path_hi, ld).replace("</head>", f"<style>{CSS}</style></head>", 1)
            + bp.header(lang, path_hi if lang == "en" else path_en)
            + f'<main class="wrap grid"><article>{bp.crumbs(lang, t["procs"], "procedures", X["name"])}'
            + f'<p class="eyebrow">{e(U["eyebrow"])}</p><h1>{e(X["h1"])}</h1>{bp.byline(lang, UPD)}' + body
            + f"</article>{bp.aside(lang)}</main>" + js + bp.footer(lang))
    return path, path_en, path_hi, page

def proc_note(lang, bp, slug):
    """Callout on a procedure page pointing to its preparation guide."""
    k = PROC_LINK.get(slug)
    if not k: return ""
    X = G[k][lang]
    txt = ("Getting ready for the test? Get a day-by-day plan with your own dates and times." if lang == "en"
           else "जाँच की तैयारी कर रहे हैं? अपनी तारीख़ और समय के साथ दिन-ब-दिन प्लान पाएँ।")
    return (f'<section class="note"><p><b>{e(X["name"])}.</b> {e(txt)}</p>'
            f'<p><a class="btn btn-solid btn-sm" href="{bp.url(lang, "guides", SLUGS[k])}">{e(X["name"])} →</a></p></section>')

def home_links(lang):
    """Links shown in the home page procedures section."""
    h = "Getting ready for a test?" if lang == "en" else "जाँच की तैयारी?"
    return (f'<p class="prep-links"><b>{h}</b> '
            + "".join(f'<a href="guides/{SLUGS[k]}/">{e(G[k][lang]["name"])} →</a>' for k in ("colonoscopy", "endoscopy")) + "</p>")
