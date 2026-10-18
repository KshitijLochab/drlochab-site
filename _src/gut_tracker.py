"""Personal Gut Health Tracker (EN + HI), 17 Oct 2026. Built by build_pages.build() at /tools/gut-tracker/ and /hi/tools/gut-tracker/.

Privacy design (do not weaken):
- Everything is stored only in this browser's localStorage on the user's own device. There is no server, account, analytics or upload.
- The page carries a Content-Security-Policy with connect-src 'none' and form-action 'none', so the page itself cannot send data anywhere.
- Optional PIN: entries are encrypted with AES-GCM using a key derived from the PIN (PBKDF2, SHA-256, 200,000 rounds). The PIN is never stored.
- Data leaves the device only when the user chooses to print, download a file or share text on WhatsApp.
"""
import json
from stool_check import _shape

SLUG = "gut-tracker"
UPD = ("2026-10-17", "17 October 2026", "17 अक्टूबर 2026")

CSP = ("default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; "
       "font-src 'self'; img-src 'self' data: blob:; connect-src 'none'; form-action 'none'; base-uri 'none'; object-src 'none'")

T_EN = dict(
 title="Gut Health Tracker: log bowel habits, symptoms and triggers | Dr. Kshitij Lochab",
 h1="Your gut health tracker",
 desc="A free, private tracker for bowel movements, stool type, bloating, pain, acidity, food triggers, water, activity, weight and waist, with weekly graphs and a summary to show your doctor.",
 eyebrow="Private tracker",
 lead="Log a few things each day: bowel habits, symptoms, possible triggers, water and activity. The weekly graphs show patterns, and the report gives your doctor a clear picture in two minutes.",
 privacy_h="Your data stays on your phone",
 privacy=["Entries are saved only in this browser on this device. Nothing is sent to Dr. Lochab, to this website or to anyone else.",
          "There is no account, no sign-in and no tracking. This page is technically blocked from sending data anywhere.",
          "You can lock your entries with a PIN, which encrypts them on this phone.",
          "Your data leaves this phone only if you print it, download it or share it yourself."],
 tabs=dict(log="Daily log", week="My graphs", report="Report for doctor", data="Entries and privacy"),
 date="Date", today="Today",
 bm="Bowel movements", st="Usual stool type", st_hint="Tap the closest shape.", st_link="What does each shape mean?",
 types=["Hard lumps", "Lumpy", "Cracked", "Smooth", "Soft blobs", "Mushy", "Watery"],
 sym="Symptoms", syms=dict(b="Bloating", p="Belly pain", a="Acidity or heartburn"), sev=["None", "Mild", "Moderate", "Severe"],
 rf="Any warning signs today?",
 rfs=dict(blood="Blood in stool", black="Black, tarry stool", vomit="Repeated vomiting", fever="Fever", night="Woke at night with pain or loose motions", swallow="Difficulty swallowing", wt="Losing weight without trying"),
 rf_alert="These need a doctor. Black or tarry stools, vomiting blood or severe pain are an emergency: call 112 or go to the nearest emergency department. For the others, book a consultation soon.",
 book="Book a consultation on WhatsApp",
 tr="Possible triggers today",
 trs=dict(milk="Milk", tea="Lots of tea or coffee", fried="Fried food", spicy="Very spicy food", wheat="Wheat (roti, bread)", onion="Onion or garlic", beans="Rajma, chana or beans", fizzy="Fizzy drinks",
          sweet="Sweets or sugar-free sweets", outside="Outside food", alcohol="Alcohol", late="Late or heavy dinner", stress="Stress", sleep="Poor sleep"),
 tr_other="Other triggers (type them)",
 water="Water (glasses)", act="Walking or exercise (minutes)", kg="Weight (kg)", cm="Waist (cm)",
 body_hint="Once a week is enough. Measure the waist at the level of the navel, after breathing out.",
 note="Notes", note_ph="Anything else, such as a new medicine or travel",
 saved="Saved on this phone", nostore="Your browser is blocking storage, so entries cannot be saved here. Try a normal (not private) window.",
 range="Show", ranges={"7": "7 days", "14": "14 days", "30": "30 days"},
 ch=dict(bm="Bowel movements per day", st="Stool type each day", band="Normal: types 3 to 5 (1 = hard, 7 = watery)", hard="Hard", loose="Loose", water="Water, glasses", goal_w="Goal: 8",
         act="Activity, minutes", goal_a="Goal: 30", kg="Weight, kg", cm="Waist, cm", sym="Total symptom score per day (0 to 9)"),
 nodata="No entries in this period yet. Start with today's log.",
 tiles=dict(days="Days logged", bm="Bowel movements a day", normal="Days with normal stool", sym="Days with any symptom", rf="Days with warning signs"),
 top="Possible triggers and symptoms", top_p="Average symptom score on days with each trigger, compared with days without it.",
 with_="with", without="without", pattern="This shows a pattern, not proof. Talk to your doctor before cutting out foods.",
 rep_h="Summary for your doctor", rep_p="Choose a period, then print it, save it as a PDF or share it. Show it at your next visit.",
 name="Name (optional, only printed on the report)", period="Period", print="Print or save as PDF", csv="Download as a spreadsheet (CSV)",
 wa="Send summary on WhatsApp", wa_note="This shares your health details with whoever you send it to.",
 r=dict(title="Gut health summary", logged="Days logged", bowel="Bowel habit", avg="Average bowel movements a day", types="Stool types (days)", sym="Symptoms",
        days_any="days with any", mean="average score", rf="Warning signs logged", none="None logged", tr="Possible triggers", life="Water and activity",
        water="Average water", act="Average activity", body="Weight and waist", first="first", last="latest", notes="Notes",
        foot="Recorded by the patient with the Gut Health Tracker on drlochab.com. This is not a medical record.", glasses="glasses a day", mins="minutes a day"),
 hist="Your entries", edit="Edit", del_="Delete", backup="Download a backup", restore="Restore from a backup",
 restore_ok="Backup restored.", restore_bad="That file could not be read.",
 pin_h="PIN lock", pin_p="Add a 4 to 8 digit PIN to encrypt your entries on this phone. If you forget it, the entries cannot be recovered.",
 pin_ph="4 to 8 digits", pin_set="Turn on PIN lock", pin_remove="Turn off PIN lock", pin_on="PIN lock is on. Your entries are encrypted on this phone.", lock="Lock now",
 pin_bad="Use 4 to 8 digits.", unlock_h="Enter your PIN", unlock="Unlock", wrong="Wrong PIN. Try again.",
 forgot="Forgot your PIN? The entries cannot be opened without it. You can delete them and start again.",
 wipe="Delete all my data", wipe2="Tap again to permanently delete everything", wiped="All entries were deleted from this phone.", nopin="PIN lock needs a secure (https) connection.",
 empty="No entries yet.",
 faqs=[["Can Dr. Lochab or anyone else see my entries?", "No. Entries are stored only in the browser on your phone. They are never uploaded, and the page is blocked from sending data. Only you can print or share them."],
       ["What happens if I change phones or clear my browser?", "Clearing browser data deletes the entries. Use 'Download a backup' to save a file, and 'Restore from a backup' on the new phone."],
       ["How long should I track before seeing a doctor?", "Two to four weeks of entries give a useful picture. Do not wait to track if you have warning signs such as blood in the stool, black stools, weight loss or vomiting."]],
)

T_HI = dict(
 title="पेट की सेहत का ट्रैकर: मल की आदत, लक्षण और ट्रिगर लिखें | डॉ. क्षितिज लोचब",
 h1="आपका पेट की सेहत का ट्रैकर",
 desc="मल त्याग, मल के प्रकार, पेट फूलना, दर्द, एसिडिटी, खाने के ट्रिगर, पानी, गतिविधि, वज़न और कमर के लिए मुफ़्त, निजी ट्रैकर, हफ़्ते के ग्राफ़ और डॉक्टर को दिखाने के लिए सारांश के साथ।",
 eyebrow="निजी ट्रैकर",
 lead="हर दिन कुछ बातें लिखें: मल की आदत, लक्षण, संभावित ट्रिगर, पानी और गतिविधि। हफ़्ते के ग्राफ़ पैटर्न दिखाते हैं, और रिपोर्ट से डॉक्टर को दो मिनट में साफ़ तस्वीर मिलती है।",
 privacy_h="आपका डेटा आपके फ़ोन पर ही रहता है",
 privacy=["एंट्री सिर्फ़ इस डिवाइस के इसी ब्राउज़र में सेव होती हैं। कुछ भी डॉ. लोचब, इस वेबसाइट या किसी और को नहीं भेजा जाता।",
          "कोई अकाउंट, साइन-इन या ट्रैकिंग नहीं है। इस पेज को तकनीकी रूप से कहीं भी डेटा भेजने से रोका गया है।",
          "आप अपनी एंट्री PIN से लॉक कर सकते हैं, जो उन्हें इस फ़ोन पर एन्क्रिप्ट कर देता है।",
          "आपका डेटा इस फ़ोन से तभी बाहर जाता है जब आप ख़ुद उसे प्रिंट, डाउनलोड या शेयर करें।"],
 tabs=dict(log="रोज़ की एंट्री", week="मेरे ग्राफ़", report="डॉक्टर के लिए रिपोर्ट", data="एंट्री और गोपनीयता"),
 date="तारीख़", today="आज",
 bm="मल त्याग (कितनी बार)", st="आम तौर पर मल का प्रकार", st_hint="सबसे मिलता आकार चुनें।", st_link="हर आकार का क्या मतलब है?",
 types=["सख़्त गाँठें", "गाँठदार", "दरारों वाला", "चिकना", "नरम टुकड़े", "गीला", "पानी जैसा"],
 sym="लक्षण", syms=dict(b="पेट फूलना", p="पेट दर्द", a="एसिडिटी या सीने में जलन"), sev=["नहीं", "हल्का", "मध्यम", "तेज़"],
 rf="आज कोई ख़तरे का संकेत?",
 rfs=dict(blood="मल में ख़ून", black="काला, तारकोल जैसा मल", vomit="बार-बार उल्टी", fever="बुखार", night="रात में दर्द या दस्त से नींद खुली", swallow="निगलने में दिक़्क़त", wt="बिना कोशिश वज़न घटना"),
 rf_alert="इनमें डॉक्टर को दिखाना ज़रूरी है। काला या तारकोल जैसा मल, ख़ून की उल्टी या तेज़ दर्द इमरजेंसी है: 112 पर कॉल करें या नज़दीकी इमरजेंसी में जाएँ। बाक़ी में जल्दी अपॉइंटमेंट लें।",
 book="WhatsApp पर अपॉइंटमेंट लें",
 tr="आज के संभावित ट्रिगर",
 trs=dict(milk="दूध", tea="ज़्यादा चाय या कॉफ़ी", fried="तला खाना", spicy="बहुत तीखा खाना", wheat="गेहूँ (रोटी, ब्रेड)", onion="प्याज़ या लहसुन", beans="राजमा, चना या बीन्स", fizzy="सोडा या कोल्ड ड्रिंक",
          sweet="मिठाई या शुगर-फ़्री मिठाई", outside="बाहर का खाना", alcohol="शराब", late="देर से या भारी डिनर", stress="तनाव", sleep="कम नींद"),
 tr_other="दूसरे ट्रिगर (लिखें)",
 water="पानी (गिलास)", act="टहलना या कसरत (मिनट)", kg="वज़न (किलो)", cm="कमर (सेमी)",
 body_hint="हफ़्ते में एक बार काफ़ी है। साँस छोड़ने के बाद नाभि की ऊँचाई पर कमर नापें।",
 note="नोट", note_ph="कुछ और, जैसे नई दवा या यात्रा",
 saved="इस फ़ोन पर सेव हुआ", nostore="आपका ब्राउज़र स्टोरेज रोक रहा है, इसलिए एंट्री यहाँ सेव नहीं हो सकतीं। सामान्य (प्राइवेट नहीं) विंडो में खोलें।",
 range="दिखाएँ", ranges={"7": "7 दिन", "14": "14 दिन", "30": "30 दिन"},
 ch=dict(bm="हर दिन मल त्याग", st="हर दिन मल का प्रकार", band="सामान्य: टाइप 3 से 5 (1 = सख़्त, 7 = पानी जैसा)", hard="सख़्त", loose="पतला", water="पानी, गिलास", goal_w="लक्ष्य: 8",
         act="गतिविधि, मिनट", goal_a="लक्ष्य: 30", kg="वज़न, किलो", cm="कमर, सेमी", sym="हर दिन कुल लक्षण स्कोर (0 से 9)"),
 nodata="इस अवधि में अभी कोई एंट्री नहीं। आज की एंट्री से शुरू करें।",
 tiles=dict(days="एंट्री वाले दिन", bm="रोज़ मल त्याग", normal="सामान्य मल वाले दिन", sym="किसी लक्षण वाले दिन", rf="ख़तरे के संकेत वाले दिन"),
 top="संभावित ट्रिगर और लक्षण", top_p="हर ट्रिगर वाले दिनों में औसत लक्षण स्कोर, बिना उस ट्रिगर वाले दिनों से तुलना में।",
 with_="के साथ", without="के बिना", pattern="यह एक पैटर्न दिखाता है, सबूत नहीं। खाना बंद करने से पहले डॉक्टर से बात करें।",
 rep_h="डॉक्टर के लिए सारांश", rep_p="एक अवधि चुनें, फिर प्रिंट करें, PDF के रूप में सेव करें या शेयर करें। अगली बार डॉक्टर को दिखाएँ।",
 name="नाम (वैकल्पिक, सिर्फ़ रिपोर्ट पर छपेगा)", period="अवधि", print="प्रिंट करें या PDF सेव करें", csv="स्प्रेडशीट (CSV) डाउनलोड करें",
 wa="सारांश WhatsApp पर भेजें", wa_note="इससे आपकी सेहत की जानकारी उसे जाती है जिसे आप भेजते हैं।",
 r=dict(title="पेट की सेहत का सारांश", logged="एंट्री वाले दिन", bowel="मल की आदत", avg="रोज़ औसत मल त्याग", types="मल के प्रकार (दिन)", sym="लक्षण",
        days_any="किसी भी स्तर वाले दिन", mean="औसत स्कोर", rf="दर्ज ख़तरे के संकेत", none="कोई नहीं", tr="संभावित ट्रिगर", life="पानी और गतिविधि",
        water="औसत पानी", act="औसत गतिविधि", body="वज़न और कमर", first="पहला", last="ताज़ा", notes="नोट",
        foot="मरीज़ द्वारा drlochab.com के पेट की सेहत ट्रैकर से दर्ज। यह मेडिकल रिकॉर्ड नहीं है।", glasses="गिलास रोज़", mins="मिनट रोज़"),
 hist="आपकी एंट्री", edit="बदलें", del_="हटाएँ", backup="बैकअप डाउनलोड करें", restore="बैकअप से वापस लाएँ",
 restore_ok="बैकअप वापस आ गया।", restore_bad="यह फ़ाइल पढ़ी नहीं जा सकी।",
 pin_h="PIN लॉक", pin_p="इस फ़ोन पर अपनी एंट्री एन्क्रिप्ट करने के लिए 4 से 8 अंकों का PIN लगाएँ। भूल गए तो एंट्री वापस नहीं मिल सकतीं।",
 pin_ph="4 से 8 अंक", pin_set="PIN लॉक चालू करें", pin_remove="PIN लॉक बंद करें", pin_on="PIN लॉक चालू है। आपकी एंट्री इस फ़ोन पर एन्क्रिप्टेड हैं।", lock="अभी लॉक करें",
 pin_bad="4 से 8 अंक इस्तेमाल करें।", unlock_h="अपना PIN डालें", unlock="खोलें", wrong="ग़लत PIN। फिर कोशिश करें।",
 forgot="PIN भूल गए? इसके बिना एंट्री नहीं खुल सकतीं। आप उन्हें हटाकर फिर से शुरू कर सकते हैं।",
 wipe="मेरा सारा डेटा हटाएँ", wipe2="सब कुछ हमेशा के लिए हटाने के लिए फिर टैप करें", wiped="इस फ़ोन से सारी एंट्री हटा दी गईं।", nopin="PIN लॉक के लिए सुरक्षित (https) कनेक्शन चाहिए।",
 empty="अभी कोई एंट्री नहीं।",
 faqs=[["क्या डॉ. लोचब या कोई और मेरी एंट्री देख सकता है?", "नहीं। एंट्री सिर्फ़ आपके फ़ोन के ब्राउज़र में रहती हैं। ये कभी अपलोड नहीं होतीं, और पेज को डेटा भेजने से रोका गया है। सिर्फ़ आप उन्हें प्रिंट या शेयर कर सकते हैं।"],
       ["फ़ोन बदलने या ब्राउज़र साफ़ करने पर क्या होगा?", "ब्राउज़र का डेटा साफ़ करने से एंट्री हट जाती हैं। 'बैकअप डाउनलोड करें' से फ़ाइल सेव करें, और नए फ़ोन पर 'बैकअप से वापस लाएँ' इस्तेमाल करें।"],
       ["डॉक्टर को दिखाने से पहले कितने दिन ट्रैक करें?", "दो से चार हफ़्ते की एंट्री से अच्छी तस्वीर मिलती है। मल में ख़ून, काला मल, वज़न घटना या उल्टी जैसे ख़तरे के संकेत हों तो ट्रैक करने का इंतज़ार न करें।"]],
)

CSS = r"""
.gt-priv{background:var(--accent-soft);border-radius:18px;padding:16px 18px;margin:18px 0}
.gt-priv h2{margin:0 0 6px;font-size:1.05rem;font-family:var(--body);font-weight:700}
.gt-priv ul{margin:0;padding-left:20px;font-size:.95rem}
.gt-tabs{display:flex;gap:6px;flex-wrap:wrap;margin:20px 0 8px}
.gt-tab{font:inherit;font-weight:700;font-size:.92rem;padding:9px 14px;border-radius:999px;border:1.5px solid var(--line);background:var(--surface);color:var(--ink);cursor:pointer}
.gt-tab[aria-selected="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.gt-panel{padding-top:8px}
.gt-row{display:grid;gap:8px;margin:18px 0;padding-bottom:18px;border-bottom:1px solid var(--line)}
.gt-row>label,.gt-lbl{font-weight:700}
.gt-hint{font-size:.85rem;color:var(--muted)}
.gt-step{display:inline-flex;align-items:center;gap:8px}
.gt-step button{width:40px;height:40px;border-radius:50%;border:1.5px solid var(--line);background:var(--surface);font-size:1.3rem;cursor:pointer;color:var(--ink)}
.gt-step output{min-width:44px;text-align:center;font-size:1.3rem;font-weight:700}
.gt-types{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.gt-type{font:inherit;display:grid;justify-items:center;gap:2px;padding:6px 2px;border-radius:12px;border:1.5px solid var(--line);background:var(--surface);cursor:pointer;color:var(--ink);font-size:.72rem;line-height:1.2}
.gt-type svg{width:100%;max-width:64px;height:auto}
.gt-type b{font-size:.8rem}
.gt-type[aria-pressed="true"],.gt-chip[aria-pressed="true"],.gt-sev button[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 2px var(--accent-soft)}
.gt-sym{display:grid;grid-template-columns:minmax(120px,1fr) 2.4fr;gap:8px 12px;align-items:center}
.gt-sev{display:grid;grid-template-columns:repeat(4,1fr);gap:4px}
.gt-sev button,.gt-chip{font:inherit;font-size:.86rem;padding:8px 6px;border-radius:10px;border:1.5px solid var(--line);background:var(--surface);cursor:pointer;color:var(--ink)}
.gt-chips{display:flex;flex-wrap:wrap;gap:6px}
.gt-chip{border-radius:999px;padding:7px 12px}
.gt-rf .gt-chip[aria-pressed="true"]{border-color:var(--urgent);background:#FFF1EE;box-shadow:none}
.gt-alert{background:#FFF1EE;border:1.5px solid var(--urgent);border-radius:14px;padding:12px 14px;font-size:.93rem}
.gt-alert .btn{margin-top:8px}
.gt-in{font:inherit;padding:9px 12px;border-radius:10px;border:1.5px solid var(--line);background:var(--surface);color:var(--ink);width:100%;max-width:360px}
.gt-two{display:flex;gap:16px;flex-wrap:wrap}.gt-two>div{display:grid;gap:6px}
.gt-two .gt-in{max-width:140px}
.gt-status{position:sticky;bottom:12px;display:inline-block;background:var(--ink);color:#fff;border-radius:999px;padding:8px 14px;font-size:.88rem;font-weight:600;opacity:0;transition:opacity .2s;pointer-events:none}
.gt-status.on{opacity:1}
.gt-warn{background:#FFF6E0;border:1px solid #E0A93A;border-radius:12px;padding:10px 12px;font-size:.9rem}
.gt-tiles{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:14px 0}
.gt-tile{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px}
.gt-tile b{display:block;font-size:1.5rem;font-family:var(--display);font-weight:400}
.gt-tile span{font-size:.82rem;color:var(--muted)}
.gt-charts{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
.gt-chart{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:12px 12px 6px}
.gt-chart h3{margin:0 0 4px;font-size:.92rem;font-family:var(--body);font-weight:700}
.gt-chart svg{width:100%;height:auto;display:block}
.gt-chart h3 .gt-hint{display:block;font-weight:400;font-size:.78rem}
.gt-chart .ax{font-size:9px;fill:var(--muted)}
.gt-tr{width:100%;border-collapse:collapse;font-size:.9rem;margin-top:8px}
.gt-tr th,.gt-tr td{text-align:left;padding:7px 6px;border-bottom:1px solid var(--line)}
.gt-tr td.n{text-align:right;font-variant-numeric:tabular-nums}
.gt-bar{display:inline-block;height:8px;border-radius:4px;background:var(--accent);vertical-align:middle}
.gt-bar.w{background:#C9D6D3}
.gt-hist{list-style:none;padding:0;margin:0}
.gt-hist li{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px;padding:10px 0;border-bottom:1px solid var(--line);font-size:.92rem}
.gt-hist li span{flex:1 1 200px;color:var(--muted)}
.gt-hist li b{min-width:96px}
.gt-act{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}
.gt-lock{max-width:360px;margin:30px auto;text-align:center;display:grid;gap:12px}
.gt-lock .gt-in{text-align:center;font-size:1.4rem;letter-spacing:.3em;margin:auto}
.gt-danger{color:var(--urgent);border-color:var(--urgent)}
.gt-report{background:#fff;border:1px solid var(--line);border-radius:14px;padding:18px;color:#12302C}
.gt-report h3{font-family:var(--body);font-size:1rem;margin:16px 0 6px}
.gt-report table{width:100%;border-collapse:collapse;font-size:.9rem}
.gt-report td,.gt-report th{border-bottom:1px solid #DDE6E3;padding:5px 6px;text-align:left}
@media (max-width:560px){.gt-types{grid-template-columns:repeat(4,1fr)}.gt-sym{grid-template-columns:1fr}}
@media print{
 body *{visibility:hidden}
 #gtReport,#gtReport *{visibility:visible}
 #gtReport{position:absolute;left:0;top:0;width:100%;border:0;padding:0}
 .season,.fab,header{display:none!important}
}
"""

JS = r"""
(function(){
const T=__T__, WA=__WA__, PRE=__PRE__, TYPES_SVG=__SVG__;
const KEY="gt-v1", LOCK="gt-v1-lock";
const $=s=>document.querySelector(s), esc=s=>String(s==null?"":s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const IST=new Intl.DateTimeFormat("en-CA",{timeZone:"Asia/Kolkata",year:"numeric",month:"2-digit",day:"2-digit"});
const TODAY=IST.format(new Date());
const addDays=(d,n)=>{const t=new Date(d+"T00:00:00Z");t.setUTCDate(t.getUTCDate()+n);return t.toISOString().slice(0,10);};
const short=d=>new Intl.DateTimeFormat(document.documentElement.lang==="hi"?"hi-IN":"en-IN",{day:"numeric",month:"short",timeZone:"UTC"}).format(new Date(d+"T00:00:00Z"));
let DB={e:{},name:""}, KEYC=null, CAN=true, LOCKED=false;
/* ---------- storage (local only) ---------- */
function lsGet(k){try{return localStorage.getItem(k);}catch(e){CAN=false;return null;}}
function lsSet(k,v){try{localStorage.setItem(k,v);return true;}catch(e){CAN=false;return false;}}
function lsDel(k){try{localStorage.removeItem(k);}catch(e){}}
const b64=a=>btoa(String.fromCharCode(...new Uint8Array(a))), unb64=s=>Uint8Array.from(atob(s),c=>c.charCodeAt(0));
const HAS_CRYPTO=!!(window.crypto&&crypto.subtle&&window.isSecureContext);
async function derive(pin,salt){const base=await crypto.subtle.importKey("raw",new TextEncoder().encode(pin),"PBKDF2",false,["deriveKey"]);
  return crypto.subtle.deriveKey({name:"PBKDF2",salt,iterations:200000,hash:"SHA-256"},base,{name:"AES-GCM",length:256},false,["encrypt","decrypt"]);}
async function encSave(){const iv=crypto.getRandomValues(new Uint8Array(12));
  const ct=await crypto.subtle.encrypt({name:"AES-GCM",iv},KEYC.key,new TextEncoder().encode(JSON.stringify(DB)));
  lsSet(LOCK,JSON.stringify({v:1,salt:b64(KEYC.salt),iv:b64(iv),ct:b64(ct)}));}
let saveTimer;
function save(){
  clearTimeout(saveTimer);
  saveTimer=setTimeout(async()=>{
    let ok;
    if(KEYC){await encSave();ok=CAN;} else ok=lsSet(KEY,JSON.stringify(DB));
    const s=$("#gtStatus"); if(ok){s.textContent=T.saved;s.classList.add("on");clearTimeout(s._t);s._t=setTimeout(()=>s.classList.remove("on"),1400);}
    $("#gtNoStore").hidden=CAN;
  },250);
}
function load(){
  const lock=lsGet(LOCK);
  if(lock){LOCKED=true;return;}
  const raw=lsGet(KEY);
  if(raw){try{const d=JSON.parse(raw);if(d&&d.e)DB=d;}catch(e){}}
}
/* ---------- daily log ---------- */
let CUR=TODAY;
const blank=()=>({bm:null,st:null,s:{b:0,p:0,a:0},rf:[],tr:[],tx:"",w:null,act:null,kg:"",cm:"",note:""});
const ent=d=>DB.e[d]||blank();
function put(d,o){const empty=o.bm===null&&o.st===null&&!o.s.b&&!o.s.p&&!o.s.a&&!o.rf.length&&!o.tr.length&&!o.tx&&o.w===null&&o.act===null&&!o.kg&&!o.cm&&!o.note;
  if(empty)delete DB.e[d]; else DB.e[d]=o; save();}
function stepper(id,val,step){return `<span class="gt-step"><button type="button" data-step="${id}" data-d="-${step}" aria-label="−">−</button><output id="${id}">${val===null?"–":val}</output><button type="button" data-step="${id}" data-d="${step}" aria-label="+">+</button></span>`;}
function renderLog(){
  const o=ent(CUR);
  const types=TYPES_SVG.map((svg,i)=>`<button type="button" class="gt-type" data-st="${i+1}" aria-pressed="${o.st===i+1}"><svg viewBox="0 0 120 64" aria-hidden="true">${svg}</svg><b>${i+1}</b>${esc(T.types[i])}</button>`).join("");
  const sym=Object.keys(T.syms).map(k=>`<span class="gt-lbl">${esc(T.syms[k])}</span><div class="gt-sev" role="group" aria-label="${esc(T.syms[k])}">${T.sev.map((s,i)=>`<button type="button" data-sym="${k}" data-v="${i}" aria-pressed="${o.s[k]===i}">${esc(s)}</button>`).join("")}</div>`).join("");
  const chips=(grp,dict,sel)=>Object.keys(dict).map(k=>`<button type="button" class="gt-chip" data-${grp}="${k}" aria-pressed="${sel.includes(k)}">${esc(dict[k])}</button>`).join("");
  $("#gtLog").innerHTML=`
   <div class="gt-row"><label for="gtDate">${T.date}</label><div class="gt-two"><input class="gt-in" type="date" id="gtDate" max="${TODAY}" value="${CUR}"><button type="button" class="btn btn-ghost btn-sm" id="gtToday">${T.today}</button></div></div>
   <div class="gt-row"><span class="gt-lbl">${T.bm}</span>${stepper("gtBm",o.bm,1)}</div>
   <div class="gt-row"><span class="gt-lbl">${T.st}</span><span class="gt-hint">${T.st_hint} <a href="${PRE}tools/stool-check/">${T.st_link}</a></span><div class="gt-types" role="group" aria-label="${esc(T.st)}">${types}</div></div>
   <div class="gt-row"><span class="gt-lbl">${T.sym}</span><div class="gt-sym">${sym}</div></div>
   <div class="gt-row gt-rf"><span class="gt-lbl">${T.rf}</span><div class="gt-chips">${chips("rf",T.rfs,o.rf)}</div><div class="gt-alert" id="gtAlert" ${o.rf.length?"":"hidden"}>${esc(T.rf_alert)}<br><a class="btn btn-wa btn-sm" href="${WA}" target="_blank" rel="noopener">${esc(T.book)}</a></div></div>
   <div class="gt-row"><span class="gt-lbl">${T.tr}</span><div class="gt-chips">${chips("tr",T.trs,o.tr)}</div><label class="gt-hint" for="gtTx">${T.tr_other}</label><input class="gt-in" id="gtTx" maxlength="80" value="${esc(o.tx)}"></div>
   <div class="gt-row"><div class="gt-two"><div><span class="gt-lbl">${T.water}</span>${stepper("gtW",o.w,1)}</div><div><span class="gt-lbl">${T.act}</span>${stepper("gtAct",o.act,10)}</div></div></div>
   <div class="gt-row"><div class="gt-two"><div><label for="gtKg">${T.kg}</label><input class="gt-in" id="gtKg" type="number" inputmode="decimal" min="20" max="250" step="0.1" value="${esc(o.kg)}"></div><div><label for="gtCm">${T.cm}</label><input class="gt-in" id="gtCm" type="number" inputmode="decimal" min="40" max="200" step="0.5" value="${esc(o.cm)}"></div></div><span class="gt-hint">${T.body_hint}</span></div>
   <div class="gt-row"><label for="gtNote">${T.note}</label><textarea class="gt-in" id="gtNote" rows="2" maxlength="200" placeholder="${esc(T.note_ph)}">${esc(o.note)}</textarea></div>`;
}
function onLog(e){
  const b=e.target.closest("button"); if(!b)return;
  const o=JSON.parse(JSON.stringify(ent(CUR)));
  if(b.id==="gtToday"){CUR=TODAY;renderLog();return;}
  if(b.dataset.step){const k={gtBm:"bm",gtW:"w",gtAct:"act"}[b.dataset.step],max={bm:15,w:20,act:300}[k];o[k]=Math.max(0,Math.min(max,(o[k]||0)+(+b.dataset.d)));$("#"+b.dataset.step).textContent=o[k];}
  else if(b.dataset.st){const v=+b.dataset.st;o.st=o.st===v?null:v;document.querySelectorAll(".gt-type").forEach(x=>x.setAttribute("aria-pressed",String(+x.dataset.st===o.st)));}
  else if(b.dataset.sym){o.s[b.dataset.sym]=+b.dataset.v;document.querySelectorAll(`[data-sym="${b.dataset.sym}"]`).forEach(x=>x.setAttribute("aria-pressed",String(+x.dataset.v===o.s[b.dataset.sym])));}
  else if(b.dataset.rf||b.dataset.tr){const g=b.dataset.rf?"rf":"tr",k=b.dataset[g],i=o[g].indexOf(k);if(i<0)o[g].push(k);else o[g].splice(i,1);b.setAttribute("aria-pressed",String(i<0));if(g==="rf")$("#gtAlert").hidden=!o.rf.length;}
  else return;
  put(CUR,o);
}
function onLogInput(e){
  const t=e.target; if(t.id==="gtDate"){if(t.value&&t.value<=TODAY){CUR=t.value;renderLog();}return;}
  const map={gtTx:"tx",gtKg:"kg",gtCm:"cm",gtNote:"note"}; if(!map[t.id])return;
  const o=JSON.parse(JSON.stringify(ent(CUR))); o[map[t.id]]=t.value.slice(0,t.id==="gtNote"?200:80); put(CUR,o);
}
/* ---------- charts (single series each, one axis) ---------- */
function days(n){const a=[];for(let i=n-1;i>=0;i--)a.push(addDays(TODAY,-i));return a;}
const W=300,H=130,PL=26,PR=6,PT=10,PB=22;
function frame(dd,max,ticks){const iw=W-PL-PR,ih=H-PT-PB,x=i=>PL+(i+.5)*iw/dd.length,y=v=>PT+ih-(v/max)*ih;
  let g=ticks.map(t=>`<line x1="${PL}" x2="${W-PR}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)" stroke-width="1"/><text class="ax" x="${PL-4}" y="${y(t)+3}" text-anchor="end">${t}</text>`).join("");
  const step=Math.ceil(dd.length/7); g+=dd.map((d,i)=>i%step===0||i===dd.length-1?`<text class="ax" x="${x(i)}" y="${H-6}" text-anchor="middle">${short(d)}</text>`:"").join("");
  return {x,y,iw,ih,g};}
function bars(dd,vals,max,ticks,goal,unit){
  const f=frame(dd,max,ticks), bw=Math.max(3,Math.min(22,f.iw/dd.length-2));
  let s=f.g;
  if(goal!=null)s+=`<line x1="${PL}" x2="${W-PR}" y1="${f.y(goal)}" y2="${f.y(goal)}" stroke="var(--ink)" stroke-width="1" stroke-dasharray="3 3" opacity=".55"/>`;
  s+=vals.map((v,i)=>v==null?"":`<g><title>${short(dd[i])}: ${v}${unit||""}</title><rect x="${f.x(i)-bw/2}" y="${f.y(Math.min(v,max))}" width="${bw}" height="${Math.max(1,f.y(0)-f.y(Math.min(v,max)))}" rx="3" fill="#0D7466"/></g>`).join("");
  return `<svg viewBox="0 0 ${W} ${H}" role="img">${s}</svg>`;}
function dots(dd,vals){
  const f=frame(dd,7,[1,4,7]); f.y=v=>PT+(v-1)/6*f.ih;
  let s=`<rect x="${PL}" y="${PT+2/6*f.ih}" width="${f.iw}" height="${2/6*f.ih}" fill="#DCEFE9"/>`;
  s+=[1,4,7].map(t=>`<text class="ax" x="${PL-4}" y="${f.y(t)+3}" text-anchor="end">${t}</text>`).join("");
  const step=Math.ceil(dd.length/7); s+=dd.map((d,i)=>i%step===0||i===dd.length-1?`<text class="ax" x="${f.x(i)}" y="${H-6}" text-anchor="middle">${short(d)}</text>`:"").join("");
  s+=vals.map((v,i)=>v==null?"":`<g><title>${short(dd[i])}: ${v} (${T.types[v-1]})</title><circle cx="${f.x(i)}" cy="${f.y(v)}" r="5" fill="${v>=3&&v<=5?"#0D7466":"#B4531C"}" stroke="#fff" stroke-width="2"/></g>`).join("");
  return `<svg viewBox="0 0 ${W} ${H}" role="img">${s}</svg>`;}
function line(pts,unit){
  if(pts.length<1)return `<p class="gt-hint">${T.nodata}</p>`;
  const vs=pts.map(p=>p[1]),lo=Math.floor(Math.min(...vs)-1),hi=Math.ceil(Math.max(...vs)+1);
  const iw=W-PL-PR,ih=H-PT-PB,n=pts.length,x=i=>PL+(n===1?iw/2:i*iw/(n-1)),y=v=>PT+ih-(v-lo)/(hi-lo)*ih;
  let s=[lo,hi].map(t=>`<line x1="${PL}" x2="${W-PR}" y1="${y(t)}" y2="${y(t)}" stroke="var(--line)"/><text class="ax" x="${PL-4}" y="${y(t)+3}" text-anchor="end">${t}</text>`).join("");
  s+=`<polyline points="${pts.map((p,i)=>x(i)+","+y(p[1])).join(" ")}" fill="none" stroke="#0D7466" stroke-width="2"/>`;
  s+=pts.map((p,i)=>`<g><title>${short(p[0])}: ${p[1]} ${unit}</title><circle cx="${x(i)}" cy="${y(p[1])}" r="4.5" fill="#0D7466" stroke="#fff" stroke-width="2"/></g>`).join("");
  s+=`<text class="ax" x="${x(0)}" y="${H-6}" text-anchor="${n===1?"middle":"start"}">${short(pts[0][0])}</text>`+(n>1?`<text class="ax" x="${x(n-1)}" y="${H-6}" text-anchor="end">${short(pts[n-1][0])}</text>`:"");
  return `<svg viewBox="0 0 ${W} ${H}" role="img">${s}</svg>`;}
/* ---------- stats ---------- */
const symScore=o=>o.s.b+o.s.p+o.s.a;
function stats(n){
  const dd=days(n), L=dd.filter(d=>DB.e[d]).map(d=>[d,DB.e[d]]);
  const bm=L.filter(([,o])=>o.bm!=null), st=L.filter(([,o])=>o.st!=null);
  const S={dd,L,n:L.length,avgBm:bm.length?(bm.reduce((a,[,o])=>a+o.bm,0)/bm.length):null,
    normal:st.filter(([,o])=>o.st>=3&&o.st<=5).length,stN:st.length,symDays:L.filter(([,o])=>symScore(o)>0).length,rfDays:L.filter(([,o])=>o.rf.length),
    types:[1,2,3,4,5,6,7].map(t=>st.filter(([,o])=>o.st===t).length),
    sym:Object.keys(T.syms).map(k=>({k,days:L.filter(([,o])=>o.s[k]>0).length,mean:L.length?L.reduce((a,[,o])=>a+o.s[k],0)/L.length:0})),
    water:avg(L.map(([,o])=>o.w)),act:avg(L.map(([,o])=>o.act)),
    kg:L.filter(([,o])=>o.kg).map(([d,o])=>[d,+o.kg]),cm:L.filter(([,o])=>o.cm).map(([d,o])=>[d,+o.cm]),notes:L.filter(([,o])=>o.note).map(([d,o])=>[d,o.note]),
    tr:[]};
  const keys=new Set();L.forEach(([,o])=>{o.tr.forEach(k=>keys.add("k:"+k));if(o.tx)o.tx.split(/[,;]/).map(s=>s.trim().toLowerCase()).filter(Boolean).forEach(s=>keys.add("t:"+s));});
  keys.forEach(key=>{const has=([,o])=>key.startsWith("k:")?o.tr.includes(key.slice(2)):(o.tx||"").toLowerCase().split(/[,;]/).map(s=>s.trim()).includes(key.slice(2));
    const yes=L.filter(has),no=L.filter(x=>!has(x));
    S.tr.push({name:key.startsWith("k:")?T.trs[key.slice(2)]:key.slice(2),n:yes.length,w:avg(yes.map(([,o])=>symScore(o))),wo:no.length?avg(no.map(([,o])=>symScore(o))):null});});
  S.tr.sort((a,b)=>b.n-a.n||((b.w||0)-(a.w||0)));
  return S;}
function avg(a){a=a.filter(v=>v!=null&&v!=="");return a.length?a.reduce((x,y)=>x+(+y),0)/a.length:null;}
const r1=v=>v==null?"–":(Math.round(v*10)/10).toString();
function trTable(S){
  if(!S.tr.length)return "";
  return `<table class="gt-tr"><thead><tr><th></th><th class="n">#</th><th>${T.with_} / ${T.without}</th></tr></thead><tbody>${S.tr.slice(0,8).map(t=>`<tr><td>${esc(t.name)}</td><td class="n">${t.n}</td><td><span class="gt-bar" style="width:${Math.round((t.w||0)/9*120)+2}px"></span> ${r1(t.w)} &nbsp; <span class="gt-bar w" style="width:${Math.round((t.wo||0)/9*120)+2}px"></span> ${r1(t.wo)}</td></tr>`).join("")}</tbody></table><p class="gt-hint">${T.top_p} ${T.pattern}</p>`;}
/* ---------- graphs tab ---------- */
let RANGE="14";
function renderWeek(){
  const S=stats(+RANGE), dd=S.dd, v=f=>dd.map(d=>DB.e[d]?f(DB.e[d]):null);
  const sel=`<div class="gt-act" role="group" aria-label="${T.range}">${Object.keys(T.ranges).map(k=>`<button type="button" class="gt-chip" data-range="${k}" aria-pressed="${k===RANGE}">${T.ranges[k]}</button>`).join("")}</div>`;
  if(!S.n){$("#gtWeek").innerHTML=sel+`<p>${T.nodata}</p>`;return;}
  const tile=(b,s)=>`<div class="gt-tile"><b>${b}</b><span>${s}</span></div>`;
  const ch=(t,svg)=>`<div class="gt-chart"><h3>${t}</h3>${svg}</div>`;
  const sym=Object.keys(T.syms).map(k=>ch(`${T.syms[k]} <span class="gt-hint">(0–3)</span>`,bars(dd,v(o=>o.s[k]),3,[0,1,2,3],null,""))).join("");
  $("#gtWeek").innerHTML=sel+`<div class="gt-tiles">${tile(S.n+"/"+dd.length,T.tiles.days)}${tile(r1(S.avgBm),T.tiles.bm)}${tile(S.normal+"/"+S.stN,T.tiles.normal)}${tile(S.symDays,T.tiles.sym)}${S.rfDays.length?tile(S.rfDays.length,T.tiles.rf):""}</div>
   <div class="gt-charts">${ch(T.ch.bm,bars(dd,v(o=>o.bm),Math.max(4,...v(o=>o.bm).filter(x=>x!=null)),[0,2,4],null,""))}${ch(T.ch.st+` <span class="gt-hint">${T.ch.band}</span>`,dots(dd,v(o=>o.st)))}${sym}
   ${ch(T.ch.water+` <span class="gt-hint">${T.ch.goal_w}</span>`,bars(dd,v(o=>o.w),Math.max(10,...v(o=>o.w).filter(x=>x!=null)),[0,4,8],8,""))}${ch(T.ch.act+` <span class="gt-hint">${T.ch.goal_a}</span>`,bars(dd,v(o=>o.act),Math.max(60,...v(o=>o.act).filter(x=>x!=null)),[0,30,60],30,""))}
   ${S.kg.length?ch(T.ch.kg,line(S.kg,"kg")):""}${S.cm.length?ch(T.ch.cm,line(S.cm,"cm")):""}</div>
   ${S.tr.length?`<h2 style="font-size:1.1rem;margin-top:22px">${T.top}</h2>${trTable(S)}`:""}`;
}
/* ---------- report tab ---------- */
let RRANGE="30";
function reportHtml(S){
  const R=T.r, from=S.dd[0], to=S.dd[S.dd.length-1];
  const name=DB.name?`<p><b>${esc(DB.name)}</b></p>`:"";
  const types=`<table><tr>${[1,2,3,4,5,6,7].map(t=>`<th>${t}</th>`).join("")}</tr><tr>${S.types.map(c=>`<td>${c}</td>`).join("")}</tr></table>`;
  const sym=`<table>${S.sym.map(s=>`<tr><td>${esc(T.syms[s.k])}</td><td>${s.days} ${R.days_any}</td><td>${R.mean} ${r1(s.mean)}</td></tr>`).join("")}</table>`;
  const rf=S.rfDays.length?`<ul>${S.rfDays.map(([d,o])=>`<li>${short(d)}: ${o.rf.map(k=>esc(T.rfs[k])).join(", ")}</li>`).join("")}</ul>`:`<p>${R.none}</p>`;
  const body=(arr,u)=>arr.length?`${R.first} ${arr[0][1]} ${u} (${short(arr[0][0])}), ${R.last} ${arr[arr.length-1][1]} ${u} (${short(arr[arr.length-1][0])})`:"–";
  return `${name}<h2 style="margin:0">${R.title}</h2><p>${T.period}: ${short(from)} – ${short(to)} · ${R.logged}: ${S.n}/${S.dd.length}</p>
   <h3>${R.bowel}</h3><p>${R.avg}: <b>${r1(S.avgBm)}</b></p><p>${R.types}:</p>${types}
   <div class="gt-charts" style="margin-top:10px"><div class="gt-chart"><h3>${T.ch.st} <span class="gt-hint">${T.ch.band}</span></h3>${dots(S.dd,S.dd.map(d=>DB.e[d]?DB.e[d].st:null))}</div><div class="gt-chart"><h3>${T.ch.sym}</h3>${bars(S.dd,S.dd.map(d=>DB.e[d]?symScore(DB.e[d]):null),9,[0,3,6,9],null,"")}</div></div>
   <h3>${R.sym}</h3>${sym}<h3>${R.rf}</h3>${rf}
   <h3>${R.tr}</h3>${S.tr.length?trTable(S):`<p>${R.none}</p>`}
   <h3>${R.life}</h3><p>${R.water}: ${r1(S.water)} ${R.glasses} · ${R.act}: ${r1(S.act)} ${R.mins}</p>
   <h3>${R.body}</h3><p>${T.kg}: ${body(S.kg,"kg")}</p><p>${T.cm}: ${body(S.cm,"cm")}</p>
   ${S.notes.length?`<h3>${R.notes}</h3><ul>${S.notes.map(([d,t])=>`<li>${short(d)}: ${esc(t)}</li>`).join("")}</ul>`:""}
   <p class="gt-hint" style="margin-top:14px">${R.foot}</p>`;
}
function reportText(S){
  const R=T.r, L=[`${R.title} (${short(S.dd[0])} – ${short(S.dd[S.dd.length-1])})`,`${R.logged}: ${S.n}/${S.dd.length}`,`${R.avg}: ${r1(S.avgBm)}`,
   `${R.types}: `+S.types.map((c,i)=>`${i+1}:${c}`).join(" "),...S.sym.map(s=>`${T.syms[s.k]}: ${s.days} ${R.days_any}, ${R.mean} ${r1(s.mean)}`),
   `${R.rf}: `+(S.rfDays.length?S.rfDays.map(([d,o])=>short(d)+" "+o.rf.map(k=>T.rfs[k]).join("/")).join("; "):R.none),
   `${R.tr}: `+(S.tr.slice(0,5).map(t=>`${t.name} (${t.n}; ${r1(t.w)}/${r1(t.wo)})`).join(", ")||R.none),
   `${R.water}: ${r1(S.water)} · ${R.act}: ${r1(S.act)}`];
  if(S.kg.length)L.push(`${T.kg}: ${S.kg[0][1]} → ${S.kg[S.kg.length-1][1]}`);
  return L.join("\n");}
function renderReport(){
  const S=stats(+RRANGE);
  $("#gtRep").innerHTML=`<p>${T.rep_p}</p>
   <div class="gt-row"><label for="gtName">${T.name}</label><input class="gt-in" id="gtName" maxlength="60" value="${esc(DB.name||"")}" autocomplete="off"></div>
   <div class="gt-act" role="group" aria-label="${T.period}">${Object.keys(T.ranges).map(k=>`<button type="button" class="gt-chip" data-rrange="${k}" aria-pressed="${k===RRANGE}">${T.ranges[k]}</button>`).join("")}</div>
   <div class="gt-act"><button type="button" class="btn btn-solid btn-sm" id="gtPrint">${T.print}</button><button type="button" class="btn btn-ghost btn-sm" id="gtCsv">${T.csv}</button><a class="btn btn-wa btn-sm" id="gtWa" target="_blank" rel="noopener" href="https://wa.me/?text=${encodeURIComponent(reportText(S))}">${T.wa}</a></div>
   <p class="gt-hint">${T.wa_note}</p>
   <div class="gt-report" id="gtReport">${S.n?reportHtml(S):`<p>${T.nodata}</p>`}</div>`;
}
function csv(){
  const head=["date","bowel_movements","stool_type","bloating","pain","acidity","warning_signs","triggers","other_triggers","water_glasses","activity_min","weight_kg","waist_cm","note"];
  const q=v=>`"${String(v==null?"":v).replace(/"/g,'""')}"`;
  const rows=Object.keys(DB.e).sort().map(d=>{const o=DB.e[d];return [d,o.bm,o.st,o.s.b,o.s.p,o.s.a,o.rf.join("|"),o.tr.join("|"),o.tx,o.w,o.act,o.kg,o.cm,o.note].map(q).join(",");});
  download("gut-tracker.csv","﻿"+head.join(",")+"\n"+rows.join("\n"),"text/csv");}
function download(name,text,type){const u=URL.createObjectURL(new Blob([text],{type}));const a=document.createElement("a");a.href=u;a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),2000);}
/* ---------- entries and privacy tab ---------- */
let WIPE=false;
function renderData(){
  const ds=Object.keys(DB.e).sort().reverse();
  const sum=o=>[o.bm!=null?`${T.bm}: ${o.bm}`:"",o.st?`${T.st}: ${o.st}`:"",symScore(o)?Object.keys(T.syms).filter(k=>o.s[k]).map(k=>`${T.syms[k]} ${T.sev[o.s[k]]}`).join(", "):""].filter(Boolean).join(" · ");
  const pin=!HAS_CRYPTO?`<p class="gt-hint">${T.nopin}</p>`:KEYC?`<p>${T.pin_on}</p><div class="gt-act"><button type="button" class="btn btn-ghost btn-sm" id="gtLockNow">${T.lock}</button><button type="button" class="btn btn-ghost btn-sm" id="gtPinOff">${T.pin_remove}</button></div>`
     :`<p class="gt-hint">${T.pin_p}</p><div class="gt-two"><input class="gt-in" id="gtPin" type="password" inputmode="numeric" pattern="[0-9]*" maxlength="8" placeholder="${T.pin_ph}" autocomplete="new-password"><button type="button" class="btn btn-solid btn-sm" id="gtPinOn">${T.pin_set}</button></div><p class="gt-hint" id="gtPinMsg"></p>`;
  $("#gtData").innerHTML=`<h2 style="font-size:1.1rem">${T.hist}</h2>${ds.length?`<ul class="gt-hist">${ds.map(d=>`<li><b>${short(d)}</b><span>${esc(sum(DB.e[d]))||"–"}</span><button type="button" class="chip" data-edit="${d}">${T.edit}</button><button type="button" class="chip" data-del="${d}">${T.del_}</button></li>`).join("")}</ul>`:`<p>${T.empty}</p>`}
   <div class="gt-act"><button type="button" class="btn btn-ghost btn-sm" id="gtBackup">${T.backup}</button><label class="btn btn-ghost btn-sm" style="cursor:pointer">${T.restore}<input type="file" id="gtRestore" accept="application/json,.json" hidden></label></div><p class="gt-hint" id="gtRestoreMsg"></p>
   <h2 style="font-size:1.1rem;margin-top:22px">${T.pin_h}</h2>${pin}
   <div class="gt-act" style="margin-top:22px"><button type="button" class="btn btn-ghost btn-sm gt-danger" id="gtWipe">${T.wipe}</button></div><p class="gt-hint" id="gtWipeMsg"></p>`;
}
async function onData(e){
  const b=e.target.closest("button"); if(!b)return;
  if(b.dataset.edit){CUR=b.dataset.edit;show("log");return;}
  if(b.dataset.del){delete DB.e[b.dataset.del];save();renderData();return;}
  if(b.id==="gtBackup"){download("gut-tracker-backup.json",JSON.stringify({app:"drlochab-gut-tracker",v:1,data:DB}),"application/json");return;}
  if(b.id==="gtPinOn"){const p=$("#gtPin").value;if(!/^[0-9]{4,8}$/.test(p)){$("#gtPinMsg").textContent=T.pin_bad;return;}
    const salt=crypto.getRandomValues(new Uint8Array(16));KEYC={salt,key:await derive(p,salt)};await encSave();lsDel(KEY);renderData();return;}
  if(b.id==="gtPinOff"){KEYC=null;lsDel(LOCK);lsSet(KEY,JSON.stringify(DB));renderData();return;}
  if(b.id==="gtLockNow"){KEYC=null;DB={e:{},name:""};LOCKED=true;boot();return;}
  if(b.id==="gtWipe"){if(!WIPE){WIPE=true;b.textContent=T.wipe2;setTimeout(()=>{WIPE=false;if(document.body.contains(b))b.textContent=T.wipe;},5000);return;}
    WIPE=false;lsDel(KEY);lsDel(LOCK);DB={e:{},name:""};KEYC=null;renderData();$("#gtWipeMsg").textContent=T.wiped;return;}
}
function onRestore(e){
  const f=e.target.files&&e.target.files[0]; if(!f)return;
  const r=new FileReader(); r.onload=()=>{try{const j=JSON.parse(r.result);if(j.app!=="drlochab-gut-tracker"||!j.data||typeof j.data.e!=="object")throw 0;
      DB={e:Object.assign({},DB.e,j.data.e),name:DB.name||j.data.name||""};save();renderData();$("#gtRestoreMsg").textContent=T.restore_ok;}catch(x){$("#gtRestoreMsg").textContent=T.restore_bad;}};
  r.readAsText(f);
}
/* ---------- tabs, lock screen, boot ---------- */
function show(k){document.querySelectorAll(".gt-tab").forEach(t=>t.setAttribute("aria-selected",String(t.dataset.tab===k)));
  ["log","week","report","data"].forEach(x=>{$("#gtP-"+x).hidden=x!==k;});
  if(k==="log")renderLog(); if(k==="week")renderWeek(); if(k==="report")renderReport(); if(k==="data")renderData();}
function boot(){
  const app=$("#gtApp"), lockEl=$("#gtLockScr");
  if(LOCKED){app.hidden=true;lockEl.hidden=false;lockEl.innerHTML=`<h2>${T.unlock_h}</h2><input class="gt-in" id="gtUnpin" type="password" inputmode="numeric" pattern="[0-9]*" maxlength="8" autocomplete="current-password" aria-label="PIN"><button type="button" class="btn btn-solid" id="gtUnlock">${T.unlock}</button><p class="gt-hint" id="gtUnMsg"></p><p class="gt-hint">${T.forgot}</p><button type="button" class="btn btn-ghost btn-sm gt-danger" id="gtWipe2">${T.wipe}</button>`;
    const go=async()=>{try{const j=JSON.parse(lsGet(LOCK)),salt=unb64(j.salt),key=await derive($("#gtUnpin").value,salt);
        const pt=await crypto.subtle.decrypt({name:"AES-GCM",iv:unb64(j.iv)},key,unb64(j.ct));DB=JSON.parse(new TextDecoder().decode(pt));KEYC={salt,key};LOCKED=false;boot();}
      catch(x){$("#gtUnMsg").textContent=T.wrong;}};
    $("#gtUnlock").onclick=go; $("#gtUnpin").onkeydown=e=>{if(e.key==="Enter")go();};
    let w=false;$("#gtWipe2").onclick=e=>{if(!w){w=true;e.target.textContent=T.wipe2;return;}lsDel(LOCK);lsDel(KEY);DB={e:{},name:""};LOCKED=false;boot();};
    return;}
  lockEl.hidden=true;app.hidden=false;show("log");
}
$("#gtTabs").addEventListener("click",e=>{const t=e.target.closest(".gt-tab");if(t)show(t.dataset.tab);});
$("#gtLog").addEventListener("click",onLog); $("#gtLog").addEventListener("input",onLogInput);
$("#gtWeek").addEventListener("click",e=>{const b=e.target.closest("[data-range]");if(b){RANGE=b.dataset.range;renderWeek();}});
$("#gtRep").addEventListener("click",e=>{const b=e.target.closest("[data-rrange]");if(b){RRANGE=b.dataset.rrange;renderReport();return;}
  if(e.target.id==="gtPrint")window.print(); if(e.target.id==="gtCsv")csv();});
$("#gtRep").addEventListener("input",e=>{if(e.target.id==="gtName"){DB.name=e.target.value.slice(0,60);save();const r=$("#gtReport");const S=stats(+RRANGE);if(S.n)r.innerHTML=reportHtml(S);}});
$("#gtData").addEventListener("click",onData); $("#gtData").addEventListener("change",e=>{if(e.target.id==="gtRestore")onRestore(e);});
load(); if(lsGet("__t")===null){lsSet("__t","1");lsDel("__t");}
$("#gtNoStore").hidden=CAN;
boot();
})();
"""


def render(lang, bp):
    X = T_EN if lang == "en" else T_HI
    e = bp.e
    path, path_en, path_hi = bp.url(lang, "tools", SLUG), bp.url("en", "tools", SLUG), bp.url("hi", "tools", SLUG)
    keys = [k for k in X if k not in ("title", "h1", "desc", "eyebrow", "lead", "privacy_h", "privacy", "faqs")]
    js = (JS.replace("__T__", json.dumps({k: X[k] for k in keys}, ensure_ascii=False))
            .replace("__WA__", json.dumps(bp.WA)).replace("__PRE__", json.dumps(bp.pre(lang)))
            .replace("__SVG__", json.dumps([_shape(i) for i in range(1, 8)])))
    tabs = "".join(f'<button type="button" class="gt-tab" role="tab" data-tab="{k}" aria-selected="{str(k == "log").lower()}">{e(v)}</button>' for k, v in X["tabs"].items())
    t = bp.L[lang]
    body = (f'<p class="lead">{e(X["lead"])}</p>'
            f'<section class="gt-priv" aria-labelledby="gt-priv-h"><h2 id="gt-priv-h">{e(X["privacy_h"])}</h2>{bp.ul(X["privacy"])}</section>'
            f'<p class="gt-warn" id="gtNoStore" hidden>{e(X["nostore"])}</p>'
            f'<div class="gt-lock" id="gtLockScr" hidden></div>'
            f'<div id="gtApp"><div class="gt-tabs" id="gtTabs" role="tablist">{tabs}</div>'
            f'<div class="gt-panel" id="gtP-log"><div id="gtLog"></div><span class="gt-status" id="gtStatus" role="status" aria-live="polite"></span></div>'
            f'<div class="gt-panel" id="gtP-week" hidden><div id="gtWeek"></div></div>'
            f'<div class="gt-panel" id="gtP-report" hidden><h2 style="font-size:1.15rem">{e(X["rep_h"])}</h2><div id="gtRep"></div></div>'
            f'<div class="gt-panel" id="gtP-data" hidden><div id="gtData"></div></div></div>'
            + bp.faq_html(lang, X["faqs"]))
    ld = bp.ld_page(lang, path, X["h1"], X["desc"], "MedicalCondition", X["h1"], X["faqs"], t["answers"], "conditions", UPD)
    head = bp.head(lang, X["title"], X["desc"], path_en, path_hi, ld)
    head = head.replace("<head>", f'<head>\n<meta http-equiv="Content-Security-Policy" content="{CSP}">\n<meta name="referrer" content="no-referrer">', 1)
    head = head.replace("</head>", f"<style>{CSS}</style></head>", 1)
    html = (head + bp.header(lang, path_hi if lang == "en" else path_en)
            + f'<main class="wrap grid"><article>{bp.crumbs(lang, t["answers"], "conditions", X["h1"])}'
            + f'<p class="eyebrow">{e(X["eyebrow"])}</p><h1>{e(X["h1"])}</h1>{bp.byline(lang, UPD)}' + body
            + f"</article>{bp.aside(lang)}</main><script>{js}</script>" + bp.footer(lang))
    return path, path_en, path_hi, html
