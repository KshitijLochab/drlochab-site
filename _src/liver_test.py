"""'Understand your liver test (LFT)' tool page (EN + HI), 22 Oct 2026.
URL: /tools/liver-function-test/ and /hi/tools/liver-function-test/.

HELD FOR CLINICAL REVIEW: LIVE = False keeps the page out of the build and out of every link list.
`python3 liver_test.py --preview` writes both pages into site/ for a local look (a normal rebuild wipes them again).
Set LIVE = True once Dr. Lochab has approved the wording and cut-offs below.

The patient types values from their report. Each value has an editable 'upper limit on your report' box, prefilled with a
common adult limit, because labs differ. Everything runs in the browser: nothing is stored or sent (CSP connect-src 'none').
No diagnosis, no medicine names or doses."""
import json, sys, html as _html

LIVE = False
SLUG = "liver-function-test"
UPD = ("2026-10-22", "22 October 2026", "22 अक्टूबर 2026")
CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
       "font-src 'self'; img-src 'self' data:; connect-src 'none'; form-action 'none'; base-uri 'self'")

# key, default limit, unit, kind ("upper" = high is abnormal, "lower" = low is abnormal), step
TESTS = [("alt", 40, "U/L", "upper", "1"), ("ast", 40, "U/L", "upper", "1"), ("alp", 130, "U/L", "upper", "1"),
         ("ggt", 55, "U/L", "upper", "1"), ("tbil", 1.2, "mg/dL", "upper", "0.1"), ("dbil", 0.3, "mg/dL", "upper", "0.1"),
         ("alb", 3.5, "g/dL", "lower", "0.1")]
# values outside these are probably typing mistakes (or a different unit)
SANE = {"alt": 10000, "ast": 10000, "alp": 3000, "ggt": 3000, "tbil": 40, "dbil": 30, "alb": 7}

EN = dict(
 eyebrow="Free tool", h1="Understand your liver test (LFT) report",
 title="Liver function test (LFT) report explained | Dr. Lochab",
 desc="Type in SGPT, SGOT, ALP, GGT, bilirubin and albumin from your liver test report and see what each value means in plain language, and when to see a doctor.",
 lead="Liver test reports are full of short forms and numbers. Type in the values from your report and this page explains, in plain language, what each one means, what pattern they make together, and how soon to see a doctor. Leave out any test that is not on your report.",
 private="Nothing you type is saved or sent anywhere. The page works on your phone only.",
 values_h="1. Your values", value_lbl="Your value", limit_lbl="Upper limit on your report", limit_lbl_low="Lower limit on your report",
 limit_help="Labs use slightly different normal ranges. If your report prints a different limit next to the value, change it here.",
 names={"alt": ("SGPT (ALT)", "Released when liver cells are irritated or damaged."),
        "ast": ("SGOT (AST)", "Also from liver cells, and from muscle and heart."),
        "alp": ("Alkaline phosphatase (ALP)", "Rises when bile flow slows; also made by bone."),
        "ggt": ("GGT (gamma GT)", "Rises with bile flow problems, alcohol and fatty liver."),
        "tbil": ("Bilirubin, total", "The yellow pigment; high levels cause jaundice."),
        "dbil": ("Bilirubin, direct (conjugated)", "The part already processed by the liver."),
        "alb": ("Albumin", "A protein made by the liver; low in long-standing liver disease.")},
 teen="This report is for a teenager (12 to 17 years)",
 flags_h="2. Do you also have any of these?",
 flags=[("yellow", "Yellow eyes or skin"), ("urine", "Dark, tea-coloured urine"), ("confused", "Confusion or unusual drowsiness"),
        ("bleed", "Vomiting blood, or black, tarry stools"), ("pain", "Severe belly pain, or high fever with shivering"), ("swell", "Swelling of the belly or legs")],
 go="Explain my report", again="Clear and start again", print="Print or save as PDF",
 empty="Type at least one value from your report.",
 res_h="What your report shows", table_h="Value by value", th=["Test", "Your value", "Limit", "Result"],
 levels=["Within range", "Routine visit", "See a doctor within a few days", "See a doctor today"],
 bands={"ok": "In range", "low": "Low", "mild": "Mildly high", "mod": "Moderately high", "marked": "Markedly high", "very": "Very high", "teen": "Normal for age"},
 times="{x}× the limit", odd="Please check this value: it looks unusually high or low. Is the unit the same as on your report?",
 head={0: "Your values are within the ranges on your report.",
       1: "Some values are raised. This is common and usually needs a routine visit, not an emergency.",
       2: "Some values need a doctor's attention within the next few days.",
       3: "Please see a doctor today."},
 p_flag3="You mentioned a warning sign. Go to a doctor or an emergency department today, and take this report with you.",
 p_flag2="Yellow eyes, dark urine or a swelling belly with these results should be seen by a doctor within a few days, sooner if you feel unwell.",
 p_normal="Normal liver tests are reassuring, but they do not rule out every liver problem: fatty liver and early scarring can exist with normal numbers. If you are overweight, have diabetes or drink alcohol regularly, ask about an ultrasound or a liver stiffness test (FibroScan).",
 p_gilbert="Bilirubin is raised but mostly the indirect type, and the liver enzymes are normal. This pattern often fits Gilbert's syndrome, a common and harmless condition in which the liver processes bilirubin a little slowly, especially when fasting, unwell or tired. A doctor can confirm it once; it does not need treatment.",
 p_hep="The pattern points to the liver cells (SGPT and SGOT higher than ALP). Common causes are fatty liver, hepatitis B or C, alcohol, and medicines or supplements, including herbal and 'liver tonic' products. A recent viral infection can do this too.",
 p_hep_very="Values this high usually mean a sudden injury to the liver, such as viral hepatitis (A, E or B), a reaction to a medicine or herbal product, or a stone passing through the bile duct. This should be checked without delay.",
 p_chol="The pattern points to bile flow (ALP and GGT, or direct bilirubin, raised more than SGPT). Causes include a stone or narrowing in the bile duct, fatty liver and some medicines. An ultrasound of the abdomen is usually the first test.",
 p_ratio="SGOT is more than twice SGPT. This can be seen with alcohol-related liver injury and with more advanced scarring. Tell your doctor honestly how much alcohol you drink; a liver stiffness test (FibroScan) helps check for scarring.",
 p_bone="ALP is raised but GGT is normal, so the extra ALP may come from bone rather than the liver. ALP is also naturally higher in pregnancy.",
 p_teen="In teenagers, ALP is normally much higher than in adults because the bones are growing, so a raised ALP on its own is usually expected.",
 p_ggt="Only GGT is raised. On its own this is usually from alcohol, fatty liver or some medicines, and is rarely a sign of serious disease.",
 p_jaund="Bilirubin is high enough to cause jaundice, with the direct (processed) part raised. The usual next steps are an ultrasound and tests for hepatitis.",
 p_alb="Albumin is low. This can follow long-standing liver disease, but also protein loss through the kidneys, poor nutrition or any serious illness.",
 p_alb_liver="Low albumin together with raised bilirubin or SGOT can be a sign of longer-standing liver disease. A review by a liver specialist is worthwhile.",
 next_h="What doctors usually check next", next=["Repeat the liver test after a few weeks, if the rise is mild", "Ultrasound of the abdomen", "Tests for hepatitis B and C", "A liver stiffness test (FibroScan) to check for scarring", "A review of all medicines, supplements and herbal products"],
 dont="Do not start or stop any medicine, supplement or 'liver tonic' on your own because of these numbers.",
 read="Read more", book="Book a visit to discuss my report", book_msg="Hello Dr. Lochab, I would like to book a consultation about my liver test report.",
 disc="This tool explains common patterns using general adult ranges. It is not a diagnosis, and it does not replace a doctor who can see your full report and history. It is not meant for children under 12. If you are already under follow-up for a liver condition, the targets your doctor gave you come first.",
 links={"hep": ("answers/high-sgpt-sgot-liver-function-test", "High SGPT or SGOT: what it means"), "gilbert": ("answers/gilberts-syndrome", "Gilbert's syndrome"),
        "chol": ("answers/blocked-bile-duct-obstructive-jaundice", "Blocked bile duct and jaundice"), "fibro": ("answers/fibroscan-test", "FibroScan explained"),
        "jaund": ("conditions/jaundice", "Jaundice"), "fatty": ("conditions/fatty-liver", "Fatty liver"), "herbal": ("answers/herbal-supplement-liver-damage", "Herbal supplements and the liver")},
 faqs=[["What is a normal SGPT level?", "Most labs in India use an upper limit of about 35 to 45 U/L for SGPT (ALT). Always compare with the range printed on your own report, as it differs between labs."],
       ["Can a high SGPT come down?", "Yes. When the cause is treated, such as losing weight in fatty liver, stopping alcohol or stopping a harmful supplement, SGPT often returns to normal within weeks to months."],
       ["Is high bilirubin always jaundice?", "No. Visible jaundice usually appears when bilirubin goes above about 2.5 to 3 mg/dL. A mild rise with normal liver enzymes is often Gilbert's syndrome, which is harmless."],
       ["Do I need to fast for a liver test?", "Fasting is not essential for a liver test alone. Labs often ask for 8 to 10 hours of fasting when sugar or cholesterol are tested at the same time."],
       ["My liver tests are normal but the ultrasound shows fatty liver. Why?", "Fatty liver often causes no rise in liver enzymes. Normal numbers do not mean the liver is free of fat or scarring, which is why an ultrasound or FibroScan is sometimes advised."]],
)

HI = dict(
 eyebrow="मुफ़्त टूल", h1="अपनी लिवर टेस्ट (LFT) रिपोर्ट समझें",
 title="लिवर फ़ंक्शन टेस्ट (LFT) रिपोर्ट को समझें | डॉ. लोचब",
 desc="अपनी लिवर टेस्ट रिपोर्ट से SGPT, SGOT, ALP, GGT, बिलीरुबिन और एल्ब्यूमिन भरें और आसान भाषा में जानें कि हर नंबर का क्या मतलब है और डॉक्टर को कब दिखाएँ।",
 lead="लिवर टेस्ट की रिपोर्ट में छोटे नाम और बहुत सारे नंबर होते हैं। अपनी रिपोर्ट के नंबर भरें, और यह पेज आसान भाषा में बताएगा कि हर नंबर का क्या मतलब है, सब मिलकर कौन-सा पैटर्न बनाते हैं, और डॉक्टर को कितनी जल्दी दिखाना चाहिए। जो टेस्ट आपकी रिपोर्ट में नहीं है, उसे ख़ाली छोड़ दें।",
 private="आप जो भी भरते हैं, वह न कहीं सेव होता है न कहीं भेजा जाता है। यह पेज सिर्फ़ आपके फ़ोन पर काम करता है।",
 values_h="1. आपके नंबर", value_lbl="आपका नंबर", limit_lbl="आपकी रिपोर्ट में ऊपरी सीमा", limit_lbl_low="आपकी रिपोर्ट में निचली सीमा",
 limit_help="हर लैब की सामान्य सीमा थोड़ी अलग होती है। अगर आपकी रिपोर्ट में नंबर के आगे अलग सीमा छपी है, तो उसे यहाँ बदल दें।",
 names={"alt": ("SGPT (ALT)", "लिवर की कोशिकाओं में जलन या नुकसान होने पर निकलता है।"),
        "ast": ("SGOT (AST)", "यह भी लिवर की कोशिकाओं से आता है, और मांसपेशियों व दिल से भी।"),
        "alp": ("एल्कलाइन फ़ॉस्फ़ेटेज़ (ALP)", "पित्त का बहाव धीमा होने पर बढ़ता है; हड्डियाँ भी इसे बनाती हैं।"),
        "ggt": ("GGT (गामा GT)", "पित्त की रुकावट, शराब और फैटी लिवर में बढ़ता है।"),
        "tbil": ("बिलीरुबिन, टोटल", "पीला रंग देने वाला पदार्थ; ज़्यादा होने पर पीलिया होता है।"),
        "dbil": ("बिलीरुबिन, डायरेक्ट", "वह हिस्सा जिसे लिवर प्रोसेस कर चुका है।"),
        "alb": ("एल्ब्यूमिन", "लिवर में बनने वाला प्रोटीन; पुरानी लिवर बीमारी में कम हो जाता है।")},
 teen="यह रिपोर्ट किसी किशोर (12 से 17 साल) की है",
 flags_h="2. क्या इनमें से कुछ भी है?",
 flags=[("yellow", "आँखें या त्वचा पीली"), ("urine", "गहरा, चाय जैसे रंग का पेशाब"), ("confused", "भ्रम या असामान्य नींद"),
        ("bleed", "ख़ून की उल्टी, या काला, तारकोल जैसा मल"), ("pain", "पेट में तेज़ दर्द, या कँपकँपी के साथ तेज़ बुख़ार"), ("swell", "पेट या पैरों में सूजन")],
 go="मेरी रिपोर्ट समझाएँ", again="साफ़ करें और फिर से शुरू करें", print="प्रिंट करें या PDF सेव करें",
 empty="अपनी रिपोर्ट से कम से कम एक नंबर भरें।",
 res_h="आपकी रिपोर्ट क्या बताती है", table_h="हर नंबर अलग से", th=["टेस्ट", "आपका नंबर", "सीमा", "नतीजा"],
 levels=["सीमा के अंदर", "सामान्य अपॉइंटमेंट", "कुछ दिनों में डॉक्टर को दिखाएँ", "आज ही डॉक्टर को दिखाएँ"],
 bands={"ok": "सीमा में", "low": "कम", "mild": "थोड़ा ज़्यादा", "mod": "मध्यम ज़्यादा", "marked": "काफ़ी ज़्यादा", "very": "बहुत ज़्यादा", "teen": "उम्र के हिसाब से सामान्य"},
 times="सीमा का {x} गुना", odd="कृपया यह नंबर दोबारा देखें: यह असामान्य रूप से ज़्यादा या कम लग रहा है। क्या यूनिट वही है जो आपकी रिपोर्ट में है?",
 head={0: "आपके नंबर आपकी रिपोर्ट की सीमा के अंदर हैं।",
       1: "कुछ नंबर बढ़े हुए हैं। यह आम है और आम तौर पर सामान्य अपॉइंटमेंट काफ़ी है, इमरजेंसी नहीं।",
       2: "कुछ नंबरों पर अगले कुछ दिनों में डॉक्टर का ध्यान ज़रूरी है।",
       3: "कृपया आज ही डॉक्टर को दिखाएँ।"},
 p_flag3="आपने ख़तरे का एक संकेत बताया है। आज ही डॉक्टर या इमरजेंसी विभाग में जाएँ, और यह रिपोर्ट साथ ले जाएँ।",
 p_flag2="इन नतीजों के साथ आँखें पीली, गहरा पेशाब या पेट में सूजन हो तो कुछ दिनों के अंदर डॉक्टर को दिखाएँ, तबीयत ख़राब लगे तो और जल्दी।",
 p_normal="लिवर टेस्ट सामान्य होना तसल्ली की बात है, पर इससे हर लिवर बीमारी ख़ारिज नहीं होती: फैटी लिवर और शुरुआती स्कारिंग सामान्य नंबरों के साथ भी हो सकती है। अगर वज़न ज़्यादा है, डायबिटीज़ है या नियमित शराब पीते हैं, तो अल्ट्रासाउंड या लिवर स्टिफ़नेस टेस्ट (FibroScan) के बारे में पूछें।",
 p_gilbert="बिलीरुबिन बढ़ा है पर ज़्यादातर इनडायरेक्ट हिस्सा, और लिवर एंज़ाइम सामान्य हैं। यह पैटर्न अक्सर गिल्बर्ट सिंड्रोम से मेल खाता है, एक आम और हानिरहित स्थिति जिसमें लिवर बिलीरुबिन को थोड़ा धीरे प्रोसेस करता है, ख़ासकर भूखे रहने, बीमारी या थकान में। डॉक्टर एक बार इसकी पुष्टि कर सकते हैं; इसका इलाज ज़रूरी नहीं।",
 p_hep="पैटर्न लिवर की कोशिकाओं की ओर इशारा करता है (SGPT और SGOT, ALP से ज़्यादा बढ़े)। आम वजहें हैं फैटी लिवर, हेपेटाइटिस B या C, शराब, और दवाएँ या सप्लीमेंट, जिनमें हर्बल और 'लिवर टॉनिक' भी शामिल हैं। हाल का कोई वायरल इंफ़ेक्शन भी ऐसा कर सकता है।",
 p_hep_very="इतने ज़्यादा नंबर आम तौर पर लिवर को अचानक हुए नुकसान का संकेत होते हैं, जैसे वायरल हेपेटाइटिस (A, E या B), किसी दवा या हर्बल चीज़ का असर, या पित्त की नली से गुज़रती पथरी। इसकी जाँच बिना देर किए होनी चाहिए।",
 p_chol="पैटर्न पित्त के बहाव की ओर इशारा करता है (ALP और GGT, या डायरेक्ट बिलीरुबिन, SGPT से ज़्यादा बढ़े)। वजहों में पित्त की नली में पथरी या सिकुड़न, फैटी लिवर और कुछ दवाएँ शामिल हैं। आम तौर पर पहली जाँच पेट का अल्ट्रासाउंड होती है।",
 p_ratio="SGOT, SGPT के दोगुने से ज़्यादा है। ऐसा शराब से लिवर को हुए नुकसान में और ज़्यादा स्कारिंग में देखा जा सकता है। डॉक्टर को ईमानदारी से बताएँ कि आप कितनी शराब पीते हैं; लिवर स्टिफ़नेस टेस्ट (FibroScan) स्कारिंग की जाँच में मदद करता है।",
 p_bone="ALP बढ़ा है पर GGT सामान्य है, इसलिए बढ़ा हुआ ALP शायद लिवर से नहीं, हड्डियों से आ रहा है। गर्भावस्था में भी ALP स्वाभाविक रूप से ज़्यादा होता है।",
 p_teen="किशोरों में हड्डियाँ बढ़ रही होती हैं, इसलिए उनका ALP बड़ों से काफ़ी ज़्यादा होना सामान्य है; सिर्फ़ ALP बढ़ा हो तो आम तौर पर यह अपेक्षित है।",
 p_ggt="सिर्फ़ GGT बढ़ा है। अकेले ऐसा आम तौर पर शराब, फैटी लिवर या कुछ दवाओं से होता है, और यह शायद ही किसी गंभीर बीमारी का संकेत होता है।",
 p_jaund="बिलीरुबिन इतना ज़्यादा है कि पीलिया हो सकता है, और डायरेक्ट (प्रोसेस हो चुका) हिस्सा बढ़ा है। आम तौर पर अगली जाँचें अल्ट्रासाउंड और हेपेटाइटिस के टेस्ट होती हैं।",
 p_alb="एल्ब्यूमिन कम है। ऐसा पुरानी लिवर बीमारी में हो सकता है, पर किडनी से प्रोटीन निकलने, कम पोषण या किसी भी गंभीर बीमारी में भी।",
 p_alb_liver="कम एल्ब्यूमिन के साथ बढ़ा बिलीरुबिन या SGOT पुरानी लिवर बीमारी का संकेत हो सकता है। लिवर विशेषज्ञ को दिखाना ठीक रहेगा।",
 next_h="डॉक्टर आम तौर पर आगे क्या जाँचते हैं", next=["बढ़त थोड़ी हो तो कुछ हफ़्ते बाद लिवर टेस्ट दोबारा", "पेट का अल्ट्रासाउंड", "हेपेटाइटिस B और C के टेस्ट", "स्कारिंग देखने के लिए लिवर स्टिफ़नेस टेस्ट (FibroScan)", "सभी दवाओं, सप्लीमेंट और हर्बल चीज़ों की समीक्षा"],
 dont="इन नंबरों की वजह से कोई दवा, सप्लीमेंट या 'लिवर टॉनिक' ख़ुद से शुरू या बंद न करें।",
 read="और पढ़ें", book="अपनी रिपोर्ट पर बात करने के लिए अपॉइंटमेंट लें", book_msg="नमस्ते डॉ. लोचब, मुझे अपनी लिवर टेस्ट रिपोर्ट के बारे में अपॉइंटमेंट लेना है।",
 disc="यह टूल बड़ों की सामान्य सीमाओं के आधार पर आम पैटर्न समझाता है। यह निदान नहीं है, और उस डॉक्टर की जगह नहीं ले सकता जो आपकी पूरी रिपोर्ट और इतिहास देख सकते हैं। यह 12 साल से छोटे बच्चों के लिए नहीं है। अगर आप पहले से किसी लिवर बीमारी के फ़ॉलो-अप में हैं, तो आपके डॉक्टर के दिए लक्ष्य पहले आते हैं।",
 links={"hep": ("answers/high-sgpt-sgot-liver-function-test", "SGPT या SGOT बढ़ा हो: इसका मतलब"), "gilbert": ("answers/gilberts-syndrome", "गिल्बर्ट सिंड्रोम"),
        "chol": ("answers/blocked-bile-duct-obstructive-jaundice", "पित्त की नली में रुकावट और पीलिया"), "fibro": ("answers/fibroscan-test", "FibroScan क्या है"),
        "jaund": ("conditions/jaundice", "पीलिया"), "fatty": ("conditions/fatty-liver", "फैटी लिवर"), "herbal": ("answers/herbal-supplement-liver-damage", "हर्बल सप्लीमेंट और लिवर")},
 faqs=[["SGPT का सामान्य स्तर क्या है?", "भारत में ज़्यादातर लैब SGPT (ALT) की ऊपरी सीमा करीब 35 से 45 U/L रखती हैं। हमेशा अपनी रिपोर्ट में छपी सीमा से मिलाएँ, क्योंकि यह हर लैब में अलग होती है।"],
       ["क्या बढ़ा हुआ SGPT कम हो सकता है?", "हाँ। जब वजह का इलाज होता है, जैसे फैटी लिवर में वज़न घटाना, शराब छोड़ना या नुकसान करने वाला सप्लीमेंट बंद करना, तो SGPT अक्सर कुछ हफ़्तों से महीनों में सामान्य हो जाता है।"],
       ["क्या बढ़ा बिलीरुबिन हमेशा पीलिया होता है?", "नहीं। दिखने वाला पीलिया आम तौर पर तब होता है जब बिलीरुबिन करीब 2.5 से 3 mg/dL से ऊपर जाता है। लिवर एंज़ाइम सामान्य हों और बिलीरुबिन थोड़ा बढ़ा हो, तो यह अक्सर गिल्बर्ट सिंड्रोम होता है, जो हानिरहित है।"],
       ["क्या लिवर टेस्ट के लिए खाली पेट जाना ज़रूरी है?", "सिर्फ़ लिवर टेस्ट के लिए खाली पेट रहना ज़रूरी नहीं। शुगर या कोलेस्ट्रॉल साथ में जाँचे जा रहे हों तो लैब अक्सर 8 से 10 घंटे खाली पेट रहने को कहती हैं।"],
       ["मेरे लिवर टेस्ट सामान्य हैं पर अल्ट्रासाउंड में फैटी लिवर है। ऐसा क्यों?", "फैटी लिवर में अक्सर लिवर एंज़ाइम नहीं बढ़ते। सामान्य नंबरों का मतलब यह नहीं कि लिवर में चर्बी या स्कारिंग नहीं है, इसीलिए कभी-कभी अल्ट्रासाउंड या FibroScan की सलाह दी जाती है।"]],
)

CSS = """
.lt-priv{display:flex;gap:10px;align-items:flex-start;background:var(--accent-soft,#E3F0EC);border-radius:14px;padding:12px 14px;font-size:.92rem;margin:4px 0 18px}
.lt-priv svg{flex:none;width:18px;height:18px;margin-top:2px}
.lt-step{font-size:1.15rem;margin:26px 0 6px}
.lt-help{font-size:.88rem;color:var(--muted);margin:0 0 12px}
.lt-rows{display:grid;gap:10px}
.lt-row{display:grid;grid-template-columns:minmax(0,1fr) 120px 110px;gap:8px 12px;align-items:end;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:12px 14px}
.lt-row .lt-n{align-self:center}
.lt-row .lt-n b{display:block;font-size:1rem}
.lt-row .lt-n span{display:block;font-size:.84rem;color:var(--muted);line-height:1.35}
.lt-row label{display:grid;gap:4px;font-size:.78rem;font-weight:600;color:var(--muted)}
.lt-row input{font:inherit;font-size:1.05rem;width:100%;padding:9px 10px;border:1.5px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);min-width:0}
.lt-row input:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.lt-row .lt-lim input{font-size:.92rem;padding:7px 8px;color:var(--muted)}
.lt-u{font-weight:500}
@media (max-width:560px){.lt-row{grid-template-columns:1fr 1fr}.lt-row .lt-n{grid-column:1/-1}}
.lt-teen{display:flex;gap:10px;align-items:center;margin:12px 0 0;font-size:.95rem}
.lt-flags{display:flex;flex-wrap:wrap;gap:8px}
.lt-flags label{display:flex;align-items:center;gap:8px;padding:9px 13px;border:1.5px solid var(--line);border-radius:999px;background:var(--surface);font-size:.92rem;cursor:pointer}
.lt-flags input,.lt-teen input{width:18px;height:18px;accent-color:var(--accent)}
.lt-flags label:has(input:checked){border-color:var(--urgent);background:var(--urgent-soft,#FBE9E7)}
.lt-act{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.lt-err{color:var(--urgent);font-weight:600;margin-top:10px}
.lt-res{margin-top:24px;border-radius:20px;border:1px solid var(--line);background:var(--surface);padding:20px;scroll-margin-top:90px}
.lt-badge{display:inline-block;color:#fff;font-weight:700;font-size:.82rem;letter-spacing:.04em;padding:5px 11px;border-radius:999px}
.lt-res[data-l="0"] .lt-badge{background:#1F7F6B}.lt-res[data-l="1"] .lt-badge{background:#9A6A12}.lt-res[data-l="2"] .lt-badge{background:#B4531C}.lt-res[data-l="3"] .lt-badge{background:var(--urgent)}
.lt-res h2{font-size:1.3rem;margin:12px 0 10px}
.lt-res h3{font-family:var(--body);font-size:1rem;font-weight:700;margin:18px 0 6px}
.lt-res p{margin:0 0 10px}
.lt-res .lt-warn{font-weight:600;color:var(--urgent)}
.lt-tbl{width:100%;border-collapse:collapse;font-size:.95rem;margin-top:4px}
.lt-tbl th,.lt-tbl td{text-align:left;padding:9px 6px;border-bottom:1px solid var(--line);vertical-align:top}
.lt-tbl th{font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.lt-tbl td small{display:block;color:var(--muted);font-size:.8rem}
.lt-chip{display:inline-block;font-size:.82rem;font-weight:700;padding:3px 9px;border-radius:999px;background:var(--line);color:var(--ink);white-space:nowrap}
.lt-chip[data-b="ok"],.lt-chip[data-b="teen"]{background:#DDF0E9;color:#0F5A4B}
.lt-chip[data-b="mild"]{background:#F6E7C4;color:#6B4A08}
.lt-chip[data-b="mod"],.lt-chip[data-b="low"]{background:#F8D9C4;color:#7A3410}
.lt-chip[data-b="marked"],.lt-chip[data-b="very"]{background:#F4C7C1;color:#7D1C12}
.lt-tw{overflow-x:auto}
.lt-tbl td:nth-child(3){white-space:nowrap}
@media (max-width:420px){.lt-tbl{font-size:.86rem}.lt-tbl th,.lt-tbl td{padding:8px 3px}.lt-chip{white-space:normal;font-size:.76rem;padding:3px 7px}.lt-res{padding:16px 12px}}
.lt-links{display:flex;flex-wrap:wrap;gap:8px}
.lt-links a{padding:7px 12px;border-radius:999px;border:1.5px solid var(--line);text-decoration:none;font-weight:600;font-size:.9rem;background:var(--bg)}
.lt-res .btn-wa{background:#167A3E;color:#fff;border-color:#167A3E}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .lt-chip[data-b="ok"],:root:not([data-theme="light"]) .lt-chip[data-b="teen"]{background:#163F36;color:#BFE8DB}
 :root:not([data-theme="light"]) .lt-chip[data-b="mild"]{background:#3F3214;color:#F3DDA6}:root:not([data-theme="light"]) .lt-chip[data-b="mod"],:root:not([data-theme="light"]) .lt-chip[data-b="low"]{background:#45291A;color:#F6C9AC}
 :root:not([data-theme="light"]) .lt-chip[data-b="marked"],:root:not([data-theme="light"]) .lt-chip[data-b="very"]{background:#4A1D18;color:#F6BDB5}
 :root:not([data-theme="light"]) .lt-flags label:has(input:checked){background:#3A1A16}}
@media print{.lt-act,.lt-flags,.lt-rows,.lt-step,.lt-help,.lt-teen,.lt-priv{display:none!important}.lt-res{border:0;padding:0}}
"""

LOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'

JS = r"""(function(){
const D=__DATA__, T=D.t, $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const num=el=>{const v=parseFloat(String(el.value).replace(',','.'));return isFinite(v)?v:null;};
const fmt=x=>(Math.round(x*10)/10).toString();
function band(k,v,lim,teen){
  if(k==='alb'){return v<lim?{b:'low',lvl:v<3?2:1}:{b:'ok',lvl:0};}
  const x=v/lim;
  if(x<=1)return {b:'ok',lvl:0,x};
  if(k==='alp'&&teen&&x<=3)return {b:'teen',lvl:0,x};
  if(k==='tbil'){if(v>10)return {b:'very',lvl:3,x};if(v>2.5)return {b:'marked',lvl:2,x};return {b:'mild',lvl:1,x};}
  if(k==='dbil'){return x>3?{b:'marked',lvl:2,x}:{b:'mild',lvl:1,x};}
  if(k==='alt'||k==='ast'){if(x>15)return {b:'very',lvl:3,x};if(x>5)return {b:'marked',lvl:2,x};if(x>2)return {b:'mod',lvl:1,x};return {b:'mild',lvl:1,x};}
  if(k==='alp'){return x>2?{b:'mod',lvl:2,x}:{b:'mild',lvl:1,x};}
  return x>3?{b:'mod',lvl:1,x}:{b:'mild',lvl:1,x};   // ggt
}
function explain(){
  const teen=$('ltTeen').checked, V={}, R={}, odd=[];
  D.tests.forEach(([k])=>{const v=num($('lt-'+k)),lim=num($('lt-'+k+'-lim'))||D.def[k];if(v===null||v<0)return;if(v>D.sane[k]||(k==='alb'&&v<1)){odd.push([k,v]);return;}V[k]=v;R[k]=band(k,v,lim,teen);R[k].lim=lim;});
  const keys=Object.keys(V), err=$('ltErr'), out=$('ltRes');
  if(!keys.length){err.textContent=odd.length?T.odd:T.empty;err.hidden=false;out.hidden=true;return;}
  err.hidden=true;
  const flags=[...document.querySelectorAll('.lt-flags input:checked')].map(i=>i.value);
  let lvl=Math.max(0,...keys.map(k=>R[k].lvl));
  const P=[], L=new Set(), up=k=>R[k]&&R[k].lvl>0&&R[k].b!=='low', x=k=>R[k]?(R[k].x||0):0;
  const enzOK=['alt','ast','alp'].every(k=>!R[k]||R[k].b==='ok'||R[k].b==='teen');
  const cellUp=up('alt')||up('ast'), cell=Math.max(x('alt'),x('ast'));
  // patterns
  if(up('tbil')&&V.tbil<=5&&enzOK&&(!R.dbil||R.dbil.b==='ok'||(V.dbil/V.tbil)<0.2)){P.push(T.p_gilbert);L.add('gilbert');}
  else if(up('tbil')&&V.tbil>2.5&&R.dbil&&up('dbil')){P.push(T.p_jaund);L.add('jaund');lvl=Math.max(lvl,2);}
  if(cellUp&&cell>15){P.push(T.p_hep_very);L.add('hep');}
  else if(cellUp&&cell>=Math.max(x('alp'),1)*1.5){P.push(T.p_hep);L.add('hep');L.add('fatty');L.add('herbal');}
  const cholUp=(up('alp')&&R.alp.b!=='teen'&&(up('ggt')||up('dbil')))||(up('dbil')&&up('ggt'));
  if(cholUp&&cell<5&&x('alp')>=cell/1.5){P.push(T.p_chol);L.add('chol');}
  if(R.ast&&R.alt&&up('ast')&&V.ast>=2*V.alt){P.push(T.p_ratio);L.add('fibro');}
  if(R.alp&&R.alp.b==='teen'){P.push(T.p_teen);}
  else if(up('alp')&&R.ggt&&R.ggt.b==='ok'){P.push(T.p_bone);}
  if(up('ggt')&&keys.filter(k=>up(k)).length===1){P.push(T.p_ggt);L.add('fatty');}
  if(R.alb&&R.alb.b==='low'){if(up('tbil')||up('ast')){P.push(T.p_alb_liver);lvl=Math.max(lvl,2);}else P.push(T.p_alb);}
  if(lvl===0&&!P.length){P.push(T.p_normal);L.add('fibro');L.add('fatty');}
  // warning signs
  const f3=flags.some(f=>['confused','bleed','pain'].includes(f)), f2=flags.some(f=>['yellow','urine','swell'].includes(f));
  let warn='';
  if(f3){lvl=3;warn=T.p_flag3;}else if(f2&&lvl<3){lvl=2;warn=T.p_flag2;}
  // table
  const rows=keys.map(k=>{const r=R[k],[n]=D.names[k];const xs=r.x&&r.x>1&&k!=='alb'?`<small>${T.times.replace('{x}',fmt(r.x))}</small>`:'';
    return `<tr><td>${esc(n)}</td><td><b>${fmt(V[k])}</b> <small>${D.unit[k]}</small></td><td>${(k==='alb'?'≥ ':'≤ ')+fmt(r.lim)}</td><td><span class="lt-chip" data-b="${r.b}">${T.bands[r.b]}</span>${xs}</td></tr>`;}).join('');
  const links=[...L].map(k=>`<a href="${D.pre}${D.links[k][0]}/">${esc(D.links[k][1])}&nbsp;→</a>`).join('');
  out.dataset.l=lvl;
  out.innerHTML=`<span class="lt-badge">${T.levels[lvl]}</span><h2>${esc(T.head[lvl])}</h2>`
   +(warn?`<p class="lt-warn">${esc(warn)}</p>`:'')+P.map(p=>`<p>${esc(p)}</p>`).join('')
   +`<h3>${T.table_h}</h3><div class="lt-tw"><table class="lt-tbl"><thead><tr>${T.th.map(h=>`<th>${h}</th>`).join('')}</tr></thead><tbody>${rows}${odd.map(([k,v])=>`<tr><td>${esc(D.names[k][0])}</td><td><b>${fmt(v)}</b></td><td></td><td><small class="lt-warn">${esc(T.odd)}</small></td></tr>`).join('')}</tbody></table></div>`
   +(lvl>0?`<h3>${T.next_h}</h3><ul>${T.next.map(n=>`<li>${esc(n)}</li>`).join('')}</ul><p><b>${esc(T.dont)}</b></p>`:'')
   +(links?`<h3>${T.read}</h3><div class="lt-links">${links}</div>`:'')
   +`<div class="lt-act">${lvl===3?'':`<a class="btn btn-wa btn-sm" href="${D.wa}?text=${encodeURIComponent(T.book_msg+'\n'+D.src)}" target="_blank" rel="noopener">${T.book}</a>`}<button type="button" class="btn btn-ghost btn-sm" onclick="print()">${T.print}</button></div>`;
  out.hidden=false;
  out.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'start'});
  out.focus({preventScroll:true});
}
$('ltGo').addEventListener('click',explain);
document.querySelector('.lt-rows').addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();explain();}});
$('ltAgain').addEventListener('click',()=>{D.tests.forEach(([k])=>{$('lt-'+k).value='';$('lt-'+k+'-lim').value=D.def[k];});document.querySelectorAll('.lt-flags input,#ltTeen').forEach(i=>i.checked=false);$('ltRes').hidden=true;$('ltErr').hidden=true;$('lt-alt').focus();});
})();"""


def render(lang, bp):
    """Returns (path, path_en, path_hi, html). bp is the build_pages module."""
    X = EN if lang == "en" else HI
    e = bp.e
    path, path_en, path_hi = bp.url(lang, "tools", SLUG), bp.url("en", "tools", SLUG), bp.url("hi", "tools", SLUG)
    rows = ""
    for k, lim, unit, kind, step in TESTS:
        n, d = X["names"][k]
        ll = X["limit_lbl_low"] if kind == "lower" else X["limit_lbl"]
        rows += (f'<div class="lt-row"><div class="lt-n"><b id="lt-{k}-n">{e(n)}</b><span>{e(d)}</span></div>'
                 f'<label><span>{e(X["value_lbl"])} <span class="lt-u">({unit})</span></span>'
                 f'<input id="lt-{k}" type="number" inputmode="decimal" step="{step}" min="0" aria-describedby="lt-{k}-n"></label>'
                 f'<label class="lt-lim"><span>{e(ll)}</span><input id="lt-{k}-lim" type="number" inputmode="decimal" step="{step}" min="0" value="{lim}"></label></div>')
    flags = "".join(f'<label><input type="checkbox" value="{k}">{e(t)}</label>' for k, t in X["flags"])
    t = bp.L[lang]
    src = bp.SHARE_TXT[lang][4]
    data = dict(tests=[[k] for k, *_ in TESTS], def_={}, sane=SANE, unit={k: u for k, _, u, *_ in TESTS}, names=X["names"],
                links=X["links"], pre=bp.pre(lang), wa=bp.WA, src=src,
                t={k: X[k] for k in ("empty", "levels", "bands", "times", "odd", "head", "p_flag3", "p_flag2", "p_normal", "p_gilbert", "p_hep", "p_hep_very",
                                     "p_chol", "p_ratio", "p_bone", "p_teen", "p_ggt", "p_jaund", "p_alb", "p_alb_liver", "next_h", "next", "dont",
                                     "read", "book", "book_msg", "table_h", "th", "print")})
    data["def"] = {k: lim for k, lim, *_ in TESTS}; del data["def_"]
    body = (f'<p class="lead">{e(X["lead"])}</p>'
            f'<p class="lt-priv">{LOCK}<span>{e(X["private"])}</span></p>'
            f'<h2 class="lt-step">{e(X["values_h"])}</h2><p class="lt-help">{e(X["limit_help"])}</p>'
            f'<div class="lt-rows">{rows}</div>'
            f'<label class="lt-teen"><input type="checkbox" id="ltTeen">{e(X["teen"])}</label>'
            f'<h2 class="lt-step">{e(X["flags_h"])}</h2><div class="lt-flags" role="group" aria-label="{e(X["flags_h"])}">{flags}</div>'
            f'<div class="lt-act"><button type="button" class="btn btn-solid" id="ltGo">{e(X["go"])}</button>'
            f'<button type="button" class="btn btn-ghost" id="ltAgain">{e(X["again"])}</button></div>'
            f'<p class="lt-err" id="ltErr" role="alert" hidden></p>'
            f'<section class="lt-res" id="ltRes" tabindex="-1" aria-live="polite" hidden></section>'
            f'<p class="small" style="margin-top:16px">{e(X["disc"])}</p>'
            + bp.faq_html(lang, X["faqs"]))
    ld = bp.ld_page(lang, path, X["h1"], X["desc"], "MedicalCondition", X["h1"], X["faqs"], t["tools"], "daily", UPD)
    head = bp.head(lang, X["title"], X["desc"], path_en, path_hi, ld).replace("</head>", f"<style>{CSS}</style></head>", 1)
    head = head.replace("<head>", f'<head>\n<meta http-equiv="Content-Security-Policy" content="{CSP}">\n<meta name="referrer" content="no-referrer">', 1)
    page = (head + bp.header(lang, path_hi if lang == "en" else path_en)
            + f'<main class="wrap grid"><article>{bp.crumbs(lang, t["tools"], "daily", X["h1"])}'
            + f'<p class="eyebrow">{e(X["eyebrow"])}</p><h1>{e(X["h1"])}</h1>{bp.byline(lang, UPD)}' + body
            + f"</article>{bp.aside(lang)}</main><script>{JS.replace('__DATA__', json.dumps(data, ensure_ascii=False))}</script>" + bp.footer(lang))
    return path, path_en, path_hi, page


def _check():
    for X in (EN, HI):
        assert set(X["names"]) == {k for k, *_ in TESTS}
        assert len(X["levels"]) == 4 and set(X["head"]) == {0, 1, 2, 3} and len(X["flags"]) == 6 and len(X["next"]) == 5
    assert set(EN) == set(HI), set(EN) ^ set(HI)
    assert set(EN["links"]) == set(HI["links"])

_check()

if __name__ == "__main__" and "--preview" in sys.argv:
    import build_pages as bp
    for lang in ("en", "hi"):
        path, *_, page = render(lang, bp)
        bp.write(path, page)
        print("preview written:", path)
