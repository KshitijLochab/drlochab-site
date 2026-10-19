# Content log
Newest first. Add every new post here so topics are not repeated.

## 19 Oct 2026 (social)
- Four-tools promo (Food of the day, Gut Health Tracker, Stool check, Diet charts + diary): Instagram carousel (6), Instagram story / WhatsApp status (6 frames), LinkedIn single image + PDF, captions, WhatsApp messages EN + HI. Generator: social/four_tools_promo.py.
- New-features promo (diet charts, food diary, comorbidity advice, Thali 120+ foods, winter guide, WhatsApp booking, print, home screen): Instagram carousel (7 slides), WhatsApp status (3) with EN and HI broadcast messages, LinkedIn document (PDF) and caption. Generator: social/diet_charts_promo.py.

## 19 Oct 2026 (site)
- Site audit: fixed broken photo in the Hindi trust strip, low-contrast WhatsApp buttons and links, unreadable home cards and tracker tab in dark mode, tiny Myth Buster dots, a long heading overflowing on small phones, and diary picker keyboard focus. Added self-hosted fonts (no Google requests), a branded 404 page, web app manifest and icons, print layout for diet charts and guides. axe-core: 0 issues on 13 templates in light and dark mode.
- Diet charts: 'Colitis and Crohn's' renamed 'Ulcerative colitis and Crohn's disease' (EN + HI). New third stage, 'Crohn's disease with a narrowing (stricture)': its own sample day, targets and diary rules (low residue for as long as the stricture is present; foods that can get stuck marked 'Avoid'), and a section explaining inflammatory, stricturing and penetrating disease, how strictures are found and treated (medicines, endoscopic balloon dilatation, surgery), patency capsule before capsule endoscopy, and the warning signs of a blocked bowel.
- Diet charts section: /diet-charts/ plus 12 condition charts (gut health, fatty liver, acidity, IBS, constipation, gallstones, cirrhosis, jaundice, pancreatitis, colitis/Crohn's, celiac, loose motions), EN + HI, each with key goals, a sample day (veg, egg, non-veg and Western options), daily targets, eat more/cut down, caveats for diabetes, BP/heart, kidney disease, pregnancy and over-65, FAQs and when to see a doctor. Private food diary: log meals by slot, see protein, fibre, fat, vegetables, fruit and water against the chart, warnings for foods to avoid, and suggestions for the rest of the day. 24 foods added (dalia, ragi, quinoa, pasta, sandwich, curd rice, moong chilla, hung curd, grilled fish, chicken salad, soups, kiwi, prunes, walnuts, makhana, isabgol, ORS, burger, pickle, papad, chocolate…), 121 in all.
- Home: trust strip on phones with live clinic status; booking reason and time chips that pre-fill WhatsApp; diet charts card and nav link.
- Every article page: WhatsApp share links and booking messages that name the page.
- Winter and wedding season guide (EN + HI) and a banner calendar to Oct 2027 (seasonal_calendar.md).
- Search titles and descriptions shortened on all pages. Fix: header "Book a visit" text colour on inner pages.

## 18 Oct 2026 (profiles)
- Practo cover images: wide 1920x480 (teal, credentials, no contact details) and 16:9 1920x1080 with portrait. Generator: social/practo_cover.py.

## 18 Oct 2026 (site)
- Capsule endoscopy added as the 10th procedure tile on the home page (EN + HI) with a new pill-camera drawing (small intestine, capsule, recorder); tile links to the existing answer page, which now shows the drawing too. Hindi screen-reader text for all procedure drawings. Fix: breadcrumbs and guide contents chips were hidden below 1060 px on inner pages (header nav CSS was unscoped).
- Thali meter: 47 everyday foods added (97 in all) — new Tea, coffee & drinks group (chai, coffee, lassi, juice, cold drink, coconut water); puri, bhatura, aloo paratha, poha, upma, chilla, khichdi, masala dosa; sambar, kadhi, sprouts; new Eggs, chicken, fish & meat group (omelette, egg curry, tandoori chicken, butter chicken, biryani, fish fry, mutton, momos); mango, watermelon, grapes, dates; kachori, vada, pav bhaji, pizza, noodles, rusk; new Sweets group. 'Jump to' category chips. Note says sugar is not counted.
- Site SEO: 'Gurgaon (Gurugram)' in home, condition and procedure titles and headings; new pages gastroenterologist-in-gurgaon and about-dr-kshitij-lochab (EN + HI) with Physician/MedicalClinic and ProfilePage data; Arcura hours (Mon–Fri 6–8 pm, Sun 9 am–1 pm, Sat closed) on home, every page's side panel and in structured data; sameAs links to Google Business Profile, Instagram and LinkedIn; Hinglish 'also searched as' line on 44 Hindi pages (hinglish.py); footer links to About, Gurgaon page and tracker on every page.

## 17 Oct 2026 (social)
- LinkedIn document post (PDF, 6 slides) + professional caption: same new-tools carousel, last slide without 'link in bio'. Generator: social/new_tools_promo.py.
- Instagram carousel (6 slides, EN): Your gut, tracked and decoded (Gut Health Tracker, privacy, stool check, Food of the day, CTA with Diwali guide). Generator: social/new_tools_promo.py.

## 17 Oct 2026 (site)
- Site: tablet layout fixes: name no longer squeezed or overlapped by the menu (menu links step down by width, only 'Book a visit' on tablets), home cards use the full width in single-column tablet view; checked 360 to 1280 px with no sideways scrolling.
- Site: Gut Health Tracker highlighted as the first card on the home page (teal, 'New · Private · free', Start tracking); returning users with entries see 'Log today'.
- Site: private Gut Health Tracker (tools/gut-tracker, EN + HI): daily log of bowel movements, stool type, bloating/pain/acidity, warning signs (with booking prompt), triggers, water, activity, weight, waist and notes; graphs for 7/14/30 days; trigger vs symptom comparison; printable doctor report, CSV, WhatsApp summary; backup/restore; optional PIN encryption; data only on the user's device, page blocked from sending data (CSP connect-src 'none'). Linked from IBS corner, stool check and IBS, constipation, acidity, IBD and H. pylori pages.
- Site: stool check now gives separate answers for shape and colour (no combined verdict); brown no longer says 'no action needed'; hard, lumpy and loose shapes advise when to see a gastroenterologist, with a WhatsApp booking button on any abnormal result.
- Site: 'What does your stool say?' tool (tools/stool-check, EN + HI: 7 shapes, 6 colours, result with next step, original drawings). Food of the day card (36 foods rotating daily, EN + HI, share button, 'tomorrow' teaser; food_day.py). Hero now has 4 promo cards (myth, thali, food of the day, stool check; swipe row on phones). New WhatsApp shares: Thali meter result and myth 'ask your family' before guessing; all share buttons now WhatsApp green. WhatsApp Channel link ready but hidden until WA_CHANNEL is set in build_pages.py.
- Site: 18 new answer pages (EN + HI), each with diet box and FAQs: hepatitis A and E, Gilbert's syndrome, supplement liver injury, Wilson's disease, alcohol and the liver, ultrasound report terms, long-term pantoprazole, vomiting blood/black stools, hiatus hernia, burping and hiccups, weight-loss injections (GLP-1), diabetes and the gut, worms, chronic diarrhoea and mucus, appendicitis or gas, typhoid, traveller's diarrhoea, probiotics (answers_more3_en/hi.py). Diwali food guide (guides/diwali-food-guide, EN + HI) with its own illustration; site banner switches from Navratri to Diwali on 21 Oct and ends 12 Nov.
- Site: diet advice review. Pancreatitis guide corrected (no long-term low-fat or egg-white-only diet; normal diet after a single attack; fat with enzymes in chronic pancreatitis; gallstone and triglyceride notes). Fatty liver (3 to 5% for slim people), acidity (weight loss), IBS (wheat bran), constipation (kiwi, prunes), cirrhosis (5 g salt, no potassium salt substitutes), loose motions (packaged WHO ORS first) updated; lactose tolerance corrected to about one cup. New diet boxes on 7 condition pages: H. pylori/ulcer, swallowing difficulty, hepatitis B/C, gallstones, pancreatic cysts, IBD, colon polyps/cancer (cond_diet_en/hi.py).
- Site: body map stomach redrawn as a full J-shaped stomach (fundus, body, antrum to pylorus) instead of a thin crescent.
- Site: diet box (eat more / cut down / good to know) and 3 to 4 common questions added to the 32 newer answer pages (EN + HI), from alcoholic hepatitis to TB medicines and the liver; FAQs also in the FAQPage structured data. Content in answers_extra_en.py / answers_extra_hi.py.
- Site: body map redrawn as a labelled infographic (full-colour organs, name buttons with counts and leader lines). 14 new pages (EN + HI): cholecystitis, cholangitis, gallbladder polyps, gallbladder cancer, blocked bile duct, bile duct cancer, choledochal cyst, pain after gallbladder removal, chronic pancreatitis, pancreatic cancer, pseudocyst and walled-off necrosis, food pipe cancer, abdominal TB, TB medicines and the liver. Liver cancer (HCC) now shown as a liver problem card.
- Site: home page overhaul. New 'Explore your digestive system' hub (body map + organ tabs, one organ at a time, conditions + questions + procedures per organ, A to Z list) replaces the conditions list and the answers section; compact procedure tiles; guides and procedures swipe on phones. Home page about 9,300 px tall on desktop (was 13,900) and 14,400 px on phones (was 27,900).
- Site: 16 new answer pages (EN + HI): high SGPT/SGOT, ascites, hepatic encephalopathy, liver abscess, liver cancer screening, liver transplant, FibroScan, fatty liver grade, piles/fissure/fistula, celiac, stomach infection, lactose intolerance, stomach cancer signs, achalasia, capsule endoscopy, stool tests. Home answers grouped into Liver / Stomach and bowel / Tests.
- Site: new answer pages (EN + HI): alcoholic hepatitis; ACLF (acute-on-chronic liver failure). Linked from cirrhosis and hepatitis B/C pages.
- Site: Myth Buster is now a swipeable carousel (12 playable myths). 6 new myths added: thin people and fatty liver, gallstone home remedies, daily stool, daily acidity tablets, jaundice diet, colonoscopy prevents cancer (fact).
- Site: all 9 procedure pages expanded (EN + HI, about 800 to 1,100 words each, 6 FAQs, Gurugram section), aimed at searches like EUS in Gurugram, ERCP, endoscopy procedure.
- Promo for the new site features (Myth or fact? + Thali meter): Instagram story (EN), WhatsApp Status (HI and EN), Google Business Profile post (Learn more: drlochab.com). Generator: social/site_games_promo.py.
- Site: fibre counter became the Thali meter (fibre, protein and fat gauges; 51 foods incl. milk, paneer, eggs, meat, oil, ghee and snacks).
- Site: Myth Buster section (guess myth or fact, new entry Mon and Thu from myths.json) and fibre counter tab (31 foods incl. 13 vegetables), both promoted as cards at the top of the home page, EN + HI.

## 17 Oct 2026
- WhatsApp Status (HI + EN): Know your hepatitis B status (shield, 2 facts, who should get tested checklist, test and vaccine steps; replaces the plain wa-status-3). Generator: social/hepb_status.py.

## 16 Oct 2026
- Instagram post (EN): Hepatitis B is preventable, redesigned (teal, shield, 3 facts, test and vaccine cards; replaces the plain version from week_2026_10_12). Generator: social/hepb_post.py.

## 15 Oct 2026
- Site: Navratri fasting guide live (guides/navratri-fasting-guide, EN + HI) with a festival banner on every page until 20 Oct.
- Instagram story (EN): Navratri fasting guide (vrat thali, 4 ticks, space for a link sticker). Generator: social/navratri_guide_promo.py.
- WhatsApp Status (HI): बिना एसिडिटी के व्रत, promoting the Hindi guide. Generator: social/navratri_guide_promo.py.

## 14 Oct 2026 (Navratri day 4)
- Instagram post (EN): Fast, but keep your stomach light (vrat thali; roast don't fry, small meals every 3 to 4 hours, fluids; ask a doctor first if diabetic, pregnant or with a stomach problem). Generator: social/navratri_14oct.py.
- Google Business Profile (HI): व्रत में भी पेट रहे हल्का, same tips (Learn more: hi/conditions/acidity-reflux-gerd).
- WhatsApp Status (HI): पेट रहे हल्का, same tips, posted today instead of Thu 15 Oct.
- Instagram carousel (6 slides, EN): Fasting without the acidity (fried to roasted swaps, a vrat day of meals every 3 to 4 hours, 3 acidity traps, who should ask a doctor first, when to break the fast; fresh kuttu atta tip). Generator: social/navratri_carousel.py.

## 12 Oct 2026
- Instagram carousel (5 slides, EN): 3 free guides for special times of life (pregnancy, children, after 60; cover, one slide per guide, CTA to drlochab.com Special guides). Generator: social/guides_launch.py.
- WhatsApp Status: 3 free guides (pregnancy, children, after 60). Generator: social/guides_launch.py.
- Visiting card, 3.5 x 2 in with bleed (front: name, degrees, role, gold medal, phone, QR; back: Apollo Hospitals Golf Course Road morning OPD as Associate Consultant, Apollo Clinic Sector 52 2 to 5 pm, Arcura Sector 51 6 to 8 pm). Generator: social/visiting_card.py.
- Google Business Profile logo (720x720) and cover photo (1920x1080, portrait + credentials). Generator: social/gbp_brand.py.

## Week of 12 Oct 2026 (Navratri, 11 to 19 Oct)
Generator: social/week_2026_10_12.py (output in _src/out/week-2026-10-12/).
- Instagram carousel (5 slides, EN): Feel like a balloon after meals? Gas and bloating: swallowed air, gassy foods, constipation, warning signs. Links to answers/gas-and-bloating.
- Instagram post (HI): Navratri vrat, व्रत में भी पेट रहे हल्का (roast not fry, small meals every 3 to 4 hours, fluids; check with a doctor first if diabetic, pregnant or with a gut illness).
- Instagram post (EN): Hepatitis B is preventable (HBsAg test, vaccine if negative). Links to conditions/hepatitis-b-c.
- Google Business Profile: Gas and bloating, common and usually harmless (Learn more: answers/gas-and-bloating).
- WhatsApp Status: 3 quick fixes for bloating; Navratri vrat (HI); Know your hepatitis B status.
- WhatsApp broadcast: new answer page, Why do I get so much gas and bloating?
- Instagram story (Mon 12 Oct): Bloated after meals? (balloon stomach, space for a poll sticker, points to the carousel). Generator: social/story_bloat.py.
- Site: new answer page gas-and-bloating (EN and HI).

## 11 Oct 2026
- Instagram story: Chai on an empty stomach? (chai glass into empty stomach with flames; almonds, fruit, then chai). Generator: social/story_chai.py.

## 10 Oct 2026
- Google Business Profile post: Is your gut running on empty? (fibre gauge, 1200x900). Generator: social/google_fibre.py.
- Instagram story: Is your gut running on empty? (fibre fuel gauge; sprouts, guava, dal, chokar roti). Generator: social/story_fibre.py.

## 9 Oct 2026
- Instagram carousel (6 slides): The gut-friendly thali (half vegetables, quarter protein, quarter grains, 3 swaps, CTA). Generator: social/thali.py.
- Instagram story: Does your plate look like this? (with a poll sticker).

## Week of 5 Oct 2026 (launch)
- Instagram posts made: 1 Meet your gastroenterologist; 2 Acidity warning signs (carousel); 3 Fatty liver (carousel); 4 Living with IBS (carousel); 5 Myth: spicy food causes ulcers; 6 What happens in an endoscopy (carousel).
- Google Business Profile posts drafted: wk1 Now consulting in Sector 51 (rejected for a phone number in the text; repost without it); wk2 Fatty liver is often silent (image: fatty liver diet guide); wk3 When acidity needs a check-up; wk4 Living with IBS.
- WhatsApp catalogue images: clinic consultation, video consultation, upper GI endoscopy, colonoscopy, EUS, ERCP, fatty liver care, IBS care, IBD care, pancreatitis care.
- Print: Google review QR card; fatty liver A4 diet handout.
