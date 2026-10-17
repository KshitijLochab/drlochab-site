"""'What does your stool say?' tool page (EN + HI), 17 Oct 2026. Built by build_pages.build() at /tools/stool-check/ and /hi/tools/stool-check/.
Shapes follow the 7 types of the Bristol stool form scale (drawings are original). Everything runs in the browser; nothing is sent or stored."""
import json

SLUG = "stool-check"
UPD = ("2026-10-17", "17 October 2026", "17 अक्टूबर 2026")

# ---- original drawings (viewBox 0 0 120 64) ----
B, D, L = "#8A5530", "#5E3518", "#B07A4C"
def _shape(k):
    if k == 1:
        return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{B}" stroke="{D}" stroke-width="2"/>' for x, y, r in [(22,38,9),(42,28,8),(60,40,9),(78,30,7),(96,38,8),(50,48,5),(86,46,5)])
    if k == 2:
        return (f'<path d="M14 34 q6 -14 16 -6 q8 -12 18 -2 q8 -12 18 -2 q8 -12 18 -2 q10 -6 16 6 q6 14 -10 14 q-8 8 -16 0 q-8 8 -18 0 q-8 8 -18 0 q-8 8 -16 0 q-12 2 -8 -8 Z" fill="{B}" stroke="{D}" stroke-width="2" stroke-linejoin="round"/>')
    if k == 3:
        return (f'<rect x="12" y="20" width="96" height="26" rx="13" fill="{B}" stroke="{D}" stroke-width="2"/>'
                f'<path d="M34 20 l3 8 M54 46 l2 -8 M72 20 l-2 9 M90 46 l3 -8" stroke="{D}" stroke-width="2.4" stroke-linecap="round"/>')
    if k == 4:
        return (f'<path d="M14 40 C30 18 46 18 60 32 S92 48 106 24" fill="none" stroke="{D}" stroke-width="20" stroke-linecap="round"/>'
                f'<path d="M14 40 C30 18 46 18 60 32 S92 48 106 24" fill="none" stroke="{B}" stroke-width="16" stroke-linecap="round"/>'
                f'<path d="M24 31 C34 22 44 22 52 28" fill="none" stroke="{L}" stroke-width="3" stroke-linecap="round" opacity=".7"/>')
    if k == 5:
        return "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{L}" stroke="{D}" stroke-width="2"/>' for x, y, rx, ry in [(24,36,13,9),(52,30,12,9),(78,38,13,8),(100,30,10,8)])
    if k == 6:
        return (f'<path d="M14 40 l6 -10 l5 4 l6 -12 l6 8 l7 -9 l5 7 l8 -6 l4 8 l9 -5 l3 9 l9 -3 l-1 9 l8 4 l-7 5 l3 7 l-10 -2 l-5 6 l-7 -5 l-8 5 l-6 -6 l-8 4 l-5 -6 l-9 3 l-2 -7 l-8 -1 Z" fill="{L}" stroke="{D}" stroke-width="2" stroke-linejoin="round"/>'
                f'<circle cx="40" cy="38" r="3" fill="{B}"/><circle cx="66" cy="34" r="2.5" fill="{B}"/><circle cx="84" cy="42" r="3" fill="{B}"/>')
    return (f'<path d="M10 44 C20 30 40 34 52 28 C66 22 86 30 98 26 C112 22 116 40 104 46 C88 54 30 56 10 44 Z" fill="#C9A06A" stroke="#9C7444" stroke-width="2"/>'
            '<path d="M30 42 q8 -4 16 0 M62 38 q8 -4 16 0" fill="none" stroke="#E5C99C" stroke-width="3" stroke-linecap="round"/>')

COLOURS = {"brown": ("#7B4A24", "#5A3216"), "green": ("#5E7A2E", "#3F5420"), "yellow": ("#D8B54A", "#A88A2A"),
           "pale": ("#DCD3C3", "#A99F8E"), "black": ("#1F1B18", "#000000"), "red": ("#8E1F1F", "#5E1212")}
def _swatch(k):
    f, s = COLOURS[k]
    extra = '<ellipse cx="50" cy="26" rx="10" ry="4" fill="#FFFFFF" opacity=".35"/>' if k in ("black", "yellow") else ""
    return (f'<ellipse cx="60" cy="34" rx="34" ry="18" fill="{f}" stroke="{s}" stroke-width="2.5"/>{extra}')

# level: 0 normal, 1 watch, 2 see a doctor soon, 3 urgent
EN = dict(
 title="What does your stool say? Shape and colour checker | Dr. Kshitij Lochab",
 h1="What does your stool say?",
 desc="Check what your stool's shape and colour mean: constipation, normal, loose motions, black, pale, green, yellow or red stools, and when to see a doctor. A free tool in English and Hindi.",
 eyebrow="Gut check",
 lead="Your stool is a daily report from your gut. Pick the shape and the colour closest to yours to see what they usually mean and whether you need a doctor. Everything stays on your phone; nothing is saved or sent.",
 step1="1. Which shape is closest?", step2="2. What colour is it?",
 pick="Pick a shape and a colour to see what they mean.",
 shapeSays="The shape says", colourSays="The colour says", next="What to do next",
 levels=["Looks normal", "Keep an eye on it", "See a doctor soon", "Get medical care today"],
 share="Share this check on WhatsApp", shareText="What does your stool say? A quick shape and colour check from Dr. Kshitij Lochab:",
 again="Start again", read="Read more",
 shapes=[
  dict(n="Type 1", d="Separate hard lumps, like nuts", lvl=1, m="This is constipation. Stool has stayed in the bowel too long and lost its water.",
       a="Add fibre slowly (fruit with peel, dal, whole grains, isabgol with water), drink enough water and walk daily.", link="conditions/constipation"),
  dict(n="Type 2", d="Lumpy, sausage-shaped", lvl=1, m="Mild constipation. Stool is passing more slowly than ideal.",
       a="Increase fibre and fluids, keep regular toilet times after breakfast, and do not hold back the urge.", link="conditions/constipation"),
  dict(n="Type 3", d="Sausage-shaped with cracks", lvl=0, m="This is normal.", a="Keep up your fibre, fluids and activity.", link=""),
  dict(n="Type 4", d="Smooth, soft sausage or snake", lvl=0, m="This is the ideal stool.", a="Whatever you are doing is working.", link=""),
  dict(n="Type 5", d="Soft blobs with clear edges", lvl=0, m="Near normal, though it can mean a diet low in fibre or a slightly fast gut.",
       a="Add a little more fibre, such as oats, isabgol or a fruit.", link=""),
  dict(n="Type 6", d="Mushy, fluffy pieces", lvl=1, m="Loose stool. Often a passing infection, a food that did not suit you, stress or IBS.",
       a="Drink ORS or fluids and eat light food. If it lasts more than two weeks, get checked.", link="answers/chronic-diarrhoea-mucus-in-stool"),
  dict(n="Type 7", d="Watery, no solid pieces", lvl=1, m="Diarrhoea. The main risk is losing too much water and salt.",
       a="ORS after every loose stool. See a doctor the same day for blood, high fever, very little urine, or if it lasts more than 2 to 3 days.", link="answers/stomach-infection-gastroenteritis"),
 ],
 colours=[
  dict(k="brown", n="Brown", lvl=0, m="Any shade of brown is normal.", a="No action needed.", link=""),
  dict(k="green", n="Green", lvl=0, m="Usually from green vegetables, food colouring, iron tablets, or stool passing quickly during loose motions.", a="Usually harmless. Check with a doctor if it continues with other symptoms.", link=""),
  dict(k="yellow", n="Yellow, greasy, hard to flush", lvl=2, m="Greasy, foul-smelling stool that floats can mean fat is not being absorbed, from pancreas problems, celiac disease or an infection such as giardia.", a="See a doctor, especially if it keeps happening or comes with weight loss.", link="answers/chronic-pancreatitis"),
  dict(k="pale", n="Pale, clay or white", lvl=2, m="Bile may not be reaching the gut, from a blocked bile duct or a liver problem. A barium X-ray test can also turn stools white for a day or two.", a="See a doctor soon. If you also have yellow eyes, dark urine, itching or fever, go the same day.", link="answers/blocked-bile-duct-obstructive-jaundice"),
  dict(k="black", n="Black and tarry", lvl=3, m="Black, sticky, foul-smelling stool can mean bleeding from the food pipe, stomach or duodenum. Iron tablets also turn stool black, but firm and not sticky.", a="If it is sticky and tar-like, or you feel dizzy or weak, this is an emergency: call 112 or go to the emergency department.", link="answers/vomiting-blood-black-stools"),
  dict(k="red", n="Red or maroon", lvl=2, m="Blood in the stool can come from piles or a fissure, but also from polyps, colitis or cancer. Beetroot and red food colouring can also turn stool red.", a="See a doctor for any new bleeding. Heavy bleeding, dizziness or fainting needs emergency care.", link="answers/blood-in-stool-always-piles"),
 ],
 more_h="Good to know",
 more=[("How often is normal?", "Anywhere from three times a day to three times a week can be normal. A change from your usual pattern matters more than the number."),
       ("Mucus in the stool", "A little mucus is normal, and more is common with IBS. Mucus with blood, pain or fever needs a check-up."),
       ("Stools that float", "Floating stools are usually from gas and are harmless. Greasy, foul-smelling stools that are hard to flush are different and should be checked."),
       ("Urgency at night", "Loose motions that wake you from sleep are not typical of IBS and should be checked.")],
 see_h="See a doctor if you notice",
 see=["Blood in the stool, or black, sticky stools", "A change in bowel habit lasting more than three weeks, especially after age 45", "Pale stools with yellow eyes or dark urine",
      "Weight loss, anaemia or fever with bowel symptoms", "Loose motions for more than two weeks, or constipation that does not respond to fibre and fluids"],
 faqs=[["Is it normal not to pass stool every day?", "Yes. Many healthy people go every other day. It is constipation when stools are hard, painful or fewer than three times a week."],
       ["Why is my stool green?", "Usually from green leafy vegetables, food colouring, iron tablets or loose motions. It is rarely a sign of disease on its own."],
       ["Is black stool always dangerous?", "No. Iron tablets and some stomach medicines turn stools black but firm. Black, sticky, tar-like stools with weakness or dizziness are an emergency."]],
 disc="This tool explains common patterns. It does not diagnose. If you are worried, or symptoms continue, see a doctor.",
)

HI = dict(
 title="आपका मल क्या कहता है? आकार और रंग की जाँच | डॉ. क्षितिज लोचब",
 h1="आपका मल क्या कहता है?",
 desc="मल के आकार और रंग का मतलब जानें: क़ब्ज़, सामान्य, दस्त, काला, हल्का, हरा, पीला या लाल मल, और कब डॉक्टर को दिखाएँ। हिंदी और अंग्रेज़ी में मुफ़्त जाँच।",
 eyebrow="पेट की जाँच",
 lead="आपका मल आपकी आँतों की रोज़ की रिपोर्ट है। अपने मल से सबसे मिलता-जुलता आकार और रंग चुनें और जानें कि आमतौर पर उनका क्या मतलब है और क्या डॉक्टर को दिखाना चाहिए। सब कुछ आपके फ़ोन पर ही रहता है; कुछ भी सेव या भेजा नहीं जाता।",
 step1="1. कौन-सा आकार सबसे मिलता है?", step2="2. इसका रंग कैसा है?",
 pick="मतलब जानने के लिए एक आकार और एक रंग चुनें।",
 shapeSays="आकार बताता है", colourSays="रंग बताता है", next="आगे क्या करें",
 levels=["सामान्य लगता है", "नज़र रखें", "जल्दी डॉक्टर को दिखाएँ", "आज ही इलाज लें"],
 share="यह जाँच WhatsApp पर भेजें", shareText="आपका मल क्या कहता है? डॉ. क्षितिज लोचब की आकार और रंग की आसान जाँच:",
 again="फिर से शुरू करें", read="और पढ़ें",
 shapes=[
  dict(n="टाइप 1", d="अलग-अलग सख़्त गाँठें, मेवे जैसी", m="यह क़ब्ज़ है। मल आँत में बहुत देर रहा और उसका पानी सूख गया।",
       a="धीरे-धीरे फ़ाइबर बढ़ाएँ (छिलके वाले फल, दाल, साबुत अनाज, पानी के साथ इसबगोल), पर्याप्त पानी पिएँ और रोज़ टहलें।"),
  dict(n="टाइप 2", d="गाँठदार, सॉसेज जैसा", m="हल्की क़ब्ज़। मल सामान्य से धीरे निकल रहा है।",
       a="फ़ाइबर और पानी बढ़ाएँ, नाश्ते के बाद शौच का तय समय रखें, और इच्छा को न रोकें।"),
  dict(n="टाइप 3", d="दरारों वाला सॉसेज जैसा", m="यह सामान्य है।", a="फ़ाइबर, पानी और चलना-फिरना जारी रखें।"),
  dict(n="टाइप 4", d="चिकना, नरम सॉसेज या साँप जैसा", m="यह सबसे अच्छा मल है।", a="आप जो कर रहे हैं वह काम कर रहा है।"),
  dict(n="टाइप 5", d="साफ़ किनारों वाले नरम टुकड़े", m="लगभग सामान्य, हालाँकि इसका मतलब कम फ़ाइबर वाला खाना या थोड़ी तेज़ आँत हो सकता है।",
       a="थोड़ा और फ़ाइबर जोड़ें, जैसे ओट्स, इसबगोल या एक फल।"),
  dict(n="टाइप 6", d="गीले, फूले हुए टुकड़े", m="पतला मल। अक्सर थोड़े समय का इंफ़ेक्शन, कोई खाना जो सूट न किया, तनाव या IBS।",
       a="ORS या तरल पिएँ और हल्का खाना खाएँ। दो हफ़्ते से ज़्यादा चले तो जाँच कराएँ।"),
  dict(n="टाइप 7", d="पानी जैसा, बिना ठोस टुकड़ों के", m="दस्त। मुख्य ख़तरा बहुत ज़्यादा पानी और नमक निकल जाना है।",
       a="हर पतले दस्त के बाद ORS। ख़ून, तेज़ बुखार, बहुत कम पेशाब, या 2 से 3 दिन से ज़्यादा चले तो उसी दिन डॉक्टर को दिखाएँ।"),
 ],
 colours=[
  dict(n="भूरा", m="भूरे का कोई भी शेड सामान्य है।", a="कुछ करने की ज़रूरत नहीं।"),
  dict(n="हरा", m="आमतौर पर हरी सब्ज़ियों, खाने के रंग, आयरन की गोलियों, या दस्त में मल के जल्दी निकलने से।", a="आमतौर पर नुकसान रहित। दूसरे लक्षणों के साथ जारी रहे तो डॉक्टर से पूछें।"),
  dict(n="पीला, चिकना, फ़्लश न होने वाला", m="चिकना, बदबूदार, तैरने वाला मल का मतलब हो सकता है कि फ़ैट नहीं पच रहा, पैंक्रियास की समस्या, सीलिएक बीमारी या जियार्डिया जैसे इंफ़ेक्शन से।", a="डॉक्टर को दिखाएँ, ख़ासकर अगर बार-बार हो या वज़न घटे।"),
  dict(n="हल्का, मिट्टी जैसा या सफ़ेद", m="हो सकता है पित्त आँत तक न पहुँच रहा हो, पित्त की नली बंद होने या लिवर की समस्या से। बेरियम X-ray जाँच से भी एक-दो दिन मल सफ़ेद हो सकता है।", a="जल्दी डॉक्टर को दिखाएँ। साथ में आँखें पीली, गहरा पेशाब, खुजली या बुखार हो तो उसी दिन जाएँ।"),
  dict(n="काला और तारकोल जैसा", m="काला, चिपचिपा, बदबूदार मल खाने की नली, पेट या ड्यूओडेनम से ब्लीडिंग का मतलब हो सकता है। आयरन की गोलियाँ भी मल काला करती हैं, पर वह सख़्त होता है, चिपचिपा नहीं।", a="अगर यह चिपचिपा और तारकोल जैसा है, या चक्कर या कमज़ोरी है, तो यह इमरजेंसी है: 112 पर कॉल करें या इमरजेंसी में जाएँ।"),
  dict(n="लाल या गहरा लाल", m="मल में ख़ून बवासीर या फ़िशर से हो सकता है, पर पॉलिप, कोलाइटिस या कैंसर से भी। चुकंदर और लाल खाने का रंग भी मल लाल कर सकते हैं।", a="किसी भी नई ब्लीडिंग में डॉक्टर को दिखाएँ। ज़्यादा ब्लीडिंग, चक्कर या बेहोशी में इमरजेंसी इलाज चाहिए।"),
 ],
 more_h="जानने लायक",
 more=[("कितनी बार सामान्य है?", "दिन में तीन बार से लेकर हफ़्ते में तीन बार तक सामान्य हो सकता है। संख्या से ज़्यादा ज़रूरी है आपकी सामान्य आदत में बदलाव।"),
       ("मल में आँव", "थोड़ी आँव सामान्य है, और IBS में ज़्यादा आम है। ख़ून, दर्द या बुखार के साथ आँव में जाँच चाहिए।"),
       ("तैरने वाला मल", "तैरने वाला मल आमतौर पर गैस से होता है और नुकसान रहित है। चिकना, बदबूदार, मुश्किल से फ़्लश होने वाला मल अलग है और उसकी जाँच होनी चाहिए।"),
       ("रात में जल्दी जाना", "नींद से जगाने वाले दस्त IBS में आम नहीं हैं और इनकी जाँच होनी चाहिए।")],
 see_h="डॉक्टर को दिखाएँ अगर",
 see=["मल में ख़ून, या काला, चिपचिपा मल", "मल की आदत में तीन हफ़्ते से ज़्यादा बदलाव, ख़ासकर 45 की उम्र के बाद", "आँखें पीली या गहरे पेशाब के साथ हल्के रंग का मल",
      "पेट के लक्षणों के साथ वज़न घटना, ख़ून की कमी या बुखार", "दो हफ़्ते से ज़्यादा दस्त, या फ़ाइबर और पानी से ठीक न होने वाली क़ब्ज़"],
 faqs=[["क्या रोज़ मल न आना सामान्य है?", "हाँ। बहुत से स्वस्थ लोग एक दिन छोड़कर जाते हैं। क़ब्ज़ तब है जब मल सख़्त हो, दर्द हो या हफ़्ते में तीन बार से कम हो।"],
       ["मेरा मल हरा क्यों है?", "आमतौर पर हरी पत्तेदार सब्ज़ियों, खाने के रंग, आयरन की गोलियों या दस्त से। अकेले यह कम ही किसी बीमारी का संकेत होता है।"],
       ["क्या काला मल हमेशा ख़तरनाक है?", "नहीं। आयरन की गोलियाँ और पेट की कुछ दवाएँ मल को काला पर सख़्त करती हैं। कमज़ोरी या चक्कर के साथ काला, चिपचिपा, तारकोल जैसा मल इमरजेंसी है।"]],
 disc="यह जाँच आम पैटर्न समझाती है। यह बीमारी की पहचान नहीं करती। चिंता हो, या लक्षण जारी रहें, तो डॉक्टर को दिखाएँ।",
)
# Hindi entries reuse level, link and colour key from English.
for _h, _e in zip(HI["shapes"], EN["shapes"]): _h.update(lvl=_e["lvl"], link=_e["link"])
for _h, _e in zip(HI["colours"], EN["colours"]): _h.update(lvl=_e["lvl"], link=_e["link"], k=_e["k"])

CSS = """
.sc-step{margin:28px 0 12px;font-family:var(--body);font-size:1rem;font-weight:700}
.sc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:10px}
.sc-opt{display:grid;gap:4px;justify-items:center;text-align:center;background:var(--surface);border:1.5px solid var(--line);border-radius:16px;padding:12px 10px;cursor:pointer;font:inherit;color:var(--ink);transition:border-color .15s,transform .15s}
.sc-opt:hover{transform:translateY(-2px)}
.sc-opt svg{width:100%;max-width:120px;height:auto}
.sc-opt b{font-size:.9rem}.sc-opt span{font-size:.82rem;color:var(--muted);line-height:1.3}
.sc-opt[aria-pressed="true"]{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
.sc-res{margin-top:24px;border-radius:20px;border:1.5px solid var(--line);background:var(--surface);padding:20px}
.sc-res[data-l="0"]{border-color:#2E9C86}.sc-res[data-l="1"]{border-color:#E0A93A}.sc-res[data-l="2"]{border-color:#E07A3A}.sc-res[data-l="3"]{border-color:var(--urgent);background:#FFF4F2}
.sc-badge{display:inline-block;font-weight:800;font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:#fff;padding:5px 10px;border-radius:8px}
.sc-res[data-l="0"] .sc-badge{background:#1F7F6B}.sc-res[data-l="1"] .sc-badge{background:#A8741A}.sc-res[data-l="2"] .sc-badge{background:#B4531C}.sc-res[data-l="3"] .sc-badge{background:var(--urgent)}
.sc-res h3{margin:14px 0 4px;font-size:1rem;font-family:var(--body);font-weight:700}
.sc-res p{margin:0 0 6px}
.sc-act{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.btn-wa{background:#1E8E4E;color:#fff;border-color:#1E8E4E}
.btn-wa svg{width:18px;height:18px;vertical-align:-3px;margin-right:6px}
"""

ICON_SHARE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 20l1.4-4.2A8 8 0 1 1 8.6 19z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9 10.5c.5 2 2 3.5 4.5 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'


def render(lang, bp):
    """Returns (path, path_en, path_hi, html). bp is the build_pages module (helpers)."""
    X = EN if lang == "en" else HI
    e = bp.e
    path, path_en, path_hi = bp.url(lang, "tools", SLUG), bp.url("en", "tools", SLUG), bp.url("hi", "tools", SLUG)
    pre = bp.pre(lang)
    opt = lambda kind, i, svg, n, d: (f'<button type="button" class="sc-opt" data-kind="{kind}" data-i="{i}" aria-pressed="false">'
                                      f'<svg viewBox="0 0 120 64" aria-hidden="true">{svg}</svg><b>{e(n)}</b>{f"<span>{e(d)}</span>" if d else ""}</button>')
    shapes = "".join(opt("s", i, _shape(i + 1), s["n"], s["d"]) for i, s in enumerate(X["shapes"]))
    cols = "".join(opt("c", i, _swatch(c["k"]), c["n"], "") for i, c in enumerate(X["colours"]))
    data = {"shapes": [{k: s[k] for k in ("n", "d", "m", "a", "lvl", "link")} for s in X["shapes"]],
            "colours": [{k: c[k] for k in ("n", "m", "a", "lvl", "link")} for c in X["colours"]],
            "levels": X["levels"], "t": {k: X[k] for k in ("shapeSays", "colourSays", "next", "read", "pick", "again")}, "pre": pre}
    share = "https://wa.me/?text=" + bp.quote(f'{X["shareText"]} {bp.SITE}{path}')
    js = ("<script>(function(){const D=" + json.dumps(data, ensure_ascii=False) + ";"
          "const sel={s:null,c:null},res=document.getElementById('scRes');"
          "const esc=s=>String(s).replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]));"
          "const blk=(h,x)=>`<h3>${h}</h3><p>${esc(x.m)}</p><p>${esc(x.a)}</p>${x.link?`<p><a href=\"${D.pre}${x.link}/\">${D.t.read} →</a></p>`:''}`;"
          "function draw(){const s=sel.s!==null?D.shapes[sel.s]:null,c=sel.c!==null?D.colours[sel.c]:null;"
          "if(!s&&!c){res.hidden=true;return;}const l=Math.max(s?s.lvl:0,c?c.lvl:0);res.hidden=false;res.dataset.l=l;"
          "res.innerHTML=`<span class=\"sc-badge\">${D.levels[l]}</span>`+(s?blk(D.t.shapeSays+': '+esc(s.n)+', '+esc(s.d).toLowerCase(),s):'')+(c?blk(D.t.colourSays+': '+esc(c.n),c):'')+(!s||!c?`<p class=\"small\">${D.t.pick}</p>`:'');}"
          "document.querySelectorAll('.sc-opt').forEach(b=>b.addEventListener('click',()=>{const k=b.dataset.kind,i=+b.dataset.i;sel[k]=sel[k]===i?null:i;"
          "document.querySelectorAll(`.sc-opt[data-kind=\"${k}\"]`).forEach(o=>o.setAttribute('aria-pressed',String(+o.dataset.i===sel[k])));draw();"
          "if(sel.s!==null&&sel.c!==null)res.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth',block:'nearest'});}));"
          "document.getElementById('scAgain').addEventListener('click',()=>{sel.s=sel.c=null;document.querySelectorAll('.sc-opt').forEach(o=>o.setAttribute('aria-pressed','false'));draw();scrollTo({top:0});});"
          "})();</script>")
    t = bp.L[lang]
    body = (f'<p class="lead">{e(X["lead"])}</p>'
            f'<h2 class="sc-step">{e(X["step1"])}</h2><div class="sc-grid" role="group" aria-label="{e(X["step1"])}">{shapes}</div>'
            f'<h2 class="sc-step">{e(X["step2"])}</h2><div class="sc-grid" role="group" aria-label="{e(X["step2"])}">{cols}</div>'
            f'<div class="sc-res" id="scRes" role="status" aria-live="polite" hidden></div>'
            f'<div class="sc-act"><a class="btn btn-wa btn-sm" href="{share}" target="_blank" rel="noopener">{ICON_SHARE}{e(X["share"])}</a>'
            f'<button type="button" class="btn btn-ghost btn-sm" id="scAgain">{e(X["again"])}</button></div>'
            f'<p class="small" style="margin-top:12px">{e(X["disc"])}</p>'
            f'<section><h2>{e(X["more_h"])}</h2><div class="faqs">' + "".join(f'<div class="faq"><h3>{e(h)}</h3><p>{e(p)}</p></div>' for h, p in X["more"]) + '</div></section>'
            f'<section class="see"><h2>{e(X["see_h"])}</h2>{bp.ul(X["see"])}</section>'
            + bp.faq_html(lang, X["faqs"]))
    ld = bp.ld_page(lang, path, X["h1"], X["desc"], "MedicalCondition", X["h1"], X["faqs"], t["answers"], "conditions", UPD)
    html = (bp.head(lang, X["title"], X["desc"], path_en, path_hi, ld).replace("</head>", f"<style>{CSS}</style></head>", 1)
            + bp.header(lang, path_hi if lang == "en" else path_en)
            + f'<main class="wrap grid"><article>{bp.crumbs(lang, t["answers"], "conditions", X["h1"])}'
            + f'<p class="eyebrow">{e(X["eyebrow"])}</p><h1>{e(X["h1"])}</h1>{bp.byline(lang, UPD)}' + body
            + f"</article>{bp.aside(lang)}</main>" + js + bp.footer(lang))
    return path, path_en, path_hi, html
