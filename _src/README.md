# Source for drlochab.com

This folder is not published (Jekyll skips folders starting with `_`). It holds everything needed to rebuild the site and make social media images.

## Rebuild and publish the site
Requirements: Python 3 with Pillow, Node.js.

    sh _src/publish.sh

This runs `build_site.py` (English home, Hindi home, and all condition, procedure and answer pages via `build_pages.py`) into `_src/site/`, then copies the result to the repository root. The live tip files (`/tips.json`, `/ibs.json`, `/hi/tips.json`, `/hi/ibs.json`) are never overwritten; the copies in `_src` only exist so the build runs.

## Where content lives
- `lochab-gastro.html`: the English home page (markup, styles, script, data for symptoms, conditions, procedures, myths, diet guides, illustrations).
- `hindi.py`: Hindi text for the home page. Every English string it lists must still exist, or the build stops, so English edits need a matching Hindi update.
- `seo_en.py` / `seo_hi.py`: extra content for condition, procedure and answer pages (same order as the home page lists). Add a new answer page by appending to `ANSWERS` in both files. The 16 pages added on 17 Oct 2026 live in `answers_more_en.py` / `answers_more_hi.py`, and 14 biliary, pancreatic, cancer and TB pages in `answers_more2_en.py` / `answers_more2_hi.py`, and 18 everyday topics in `answers_more3_en.py` / `answers_more3_hi.py` (all are appended to `ANSWERS`, so `seo_en.ANSWERS` is the full list) (with `COND_LINKS` adding them to condition pages); the home page groups answers into Liver, Stomach and bowel, and Tests (sets in `build_site.py`). Every new answer page also gets a diet box and 3 to 4 common questions in `answers_extra_en.py` / `answers_extra_hi.py` (keyed by slug; the build checks both languages match). Condition pages without a home-page diet guide get their diet box from `cond_diet_en.py` / `cond_diet_hi.py` (keyed by condition slug).
- `SPECIAL` in `seo_en.py` / `seo_hi.py`: longer guides for a group of patients (for example pregnancy) at `/guides/<slug>/`. Each gets a card in the home page "Guides" section and a callout on the condition and procedure pages listed in its `conds` and `procs`. Each guide lists its sections in `blocks` (cards, probs, attn, urgent, pre, diet, test, care, who) and its "On this page" labels in `toc`. Illustrations are in `guide_art.py`. `SEASONAL` in `seo_en.py` / `seo_hi.py` adds a slim banner under the header of every page linking to a timely guide; it disappears after its `until` date, both at build time and in the browser. Current guides: Navratri fasting (banner until 21 Oct 2026), pregnancy, children (Dr. Lochab sees teenagers 12+; younger children are referred to their paediatrician) and adults over 60.
- `seo_proc_en.py` / `seo_proc_hi.py`: the longer procedure-page content (how it works, before, on the day, after, risks, warning signs, other options, a Gurugram section and extra FAQs), added 17 Oct 2026. The home page keeps its short procedure summaries.
- `build_pages.py` + `pages.css`: template for those pages, with structured data, breadcrumbs and hreflang.
- `brand/`, `fonts/`, `dr-lochab.jpg`: logo, fonts (Young Serif, Figtree, and Devanagari subsets of Tiro Devanagari Hindi and Mukta for Hindi images, all OFL licensed) and portrait.

## Explore your digestive system (home page hub)
`hub.py` builds the conditions section on the home page: a body map and organ tabs, with one organ panel shown at a time (common problems, questions and tests, procedures) and a collapsed A to Z list of every topic. It replaced the long conditions list and the separate answers section on 17 Oct 2026. Condition cards come from `CONDITIONS` in the page source; answer pages that describe a condition are listed in `PROBLEMS`, other answers in `QS`, procedures in `PROCS`, all by organ. When a new answer page is added, add its slug to `PROBLEMS` or `QS` so it appears in the hub (it is always in the A to Z list only if it is in one of these). Procedures on the home page are compact tiles (a swipeable row on phones) linking to their full pages.

## Myth Buster and fibre counter
- Myth Buster (home page, `#myths`, plus a teaser in the hero) reads `/myths.json` and `/hi/myths.json`. Each entry: `date` (YYYY-MM-DD, IST), `answer` (`myth` or `fact`), `claim`, `verdict`, `truth`, `do`, `doctor` (may be empty), `art` (one of milk, drop, stones, pill, shield, liver, scope, glass, eye, colon, roll, tablets) and `link` (site path without slashes, may be empty). Every entry dated today or earlier is shown in a swipeable carousel (newest first, up to 20), each with its own Myth/Fact buttons; the newest carries a "New" badge. A new myth goes live every Monday and Thursday, added a week ahead in the Sunday tips pull request. The Hindi file keeps the same `date`, `answer`, `art` and `link` as English. Like the tip files, these live files are never overwritten by `publish.sh`; the copies in `_src` (`myths.json`, `myths-hi.json`) only exist so the build runs. `_src/myths/make_myths.py` was the one-off seed.
- Thali meter (fibre, protein and fat gauges) is a tab in Gut Health Daily (`#fibre` opens it, as does the card at the top of the home page). Foods are in `FOODS` inside the `/*PLAY*/` block of `lochab-gastro.html`, each with category `c` and grams of fibre `f`, protein `p` and fat `t` per serving; targets and zones are in `METERS` (fibre at least 25 g, protein 45 g, total fat limit 60 g). Values were reviewed on 17 Oct 2026 against IFCT 2017 and USDA FoodData Central; cooked dishes include about 1 tsp oil per katori. `thali_foods.py` keeps the reviewed table with the basis for every number. The Hindi block is `PLAY_JS` in `hindi.py` and must list the same foods in the same order. Saved lists are keyed by position in `FOODS`, so add new foods at the end (category headings follow the key order of `FT.cats`, not the array order); generate both arrays with `thali_foods.js("en")` / `js("hi")`. 47 foods and drinks were added on 18 Oct 2026 (97 in all), with new groups for drinks (`k`), eggs/chicken/fish/meat (`n`) and sweets (`s`). Visitors' guesses and today's fibre list are kept only in their own browser.

## Social media images
Requirements: Python Playwright with Chromium (`python3 -m playwright install chromium`). Run `build_site.py` first, which writes `data-en.json`.
- `social/make_posts.py`: Instagram posts and carousels (1080x1350) to `_src/out/instagram/`. Edit the `POSTS` dictionary.
- `social/fatty_liver.py`: Google post image (1200x900) and A4 patient handout.
- `social/make_catalogue.py` + `social/condition_art.py`: square WhatsApp catalogue images and custom condition drawings.
- `social/week_2026_10_12.py`: example of a full week (Instagram EN and HI, Google post, WhatsApp Status) in one script.
- `social/log.md`: what has already been made and posted, to avoid repeats.

See `BRAND.md` for colours, type, voice and rules.


## Festival guides and banners
- The Diwali guide lives in `diwali_guide.py` (EN, HI and its banner text) and is inserted first in `SPECIAL`. `seo_en.SEASONAL` is a list of banners with `slug`, optional `start` and `until`; `seo_hi.SEASONAL` holds the Hindi text in the same order. Each banner shows only between its start and until (checked at build time and in the browser), so several festivals can be queued ahead.

- Winter and wedding season guide: `winter_guide.py` (EN, HI), inserted after Diwali in `SPECIAL`; its `SEASONS` list also holds the banner calendar to Oct 2027. `seasonal_calendar.md` lists every season, the dates and the guides still to write (Ramzan by 10 Jan 2027, Holi by 20 Feb 2027). Banners can link to an answer page with `kind="answers"`.

## Technical (19 Oct 2026 audit)
- Fonts are self-hosted (no Google requests): `webfonts/` (woff2 + `fonts.css` Latin, `fonts-hi.css` Devanagari, OFL licence), copied to /assets/fonts/ by `build_site.py`. Devanagari uses font-display: optional so Hindi pages never jump. The older `fonts/` folder is only for the social-image scripts.
- `site.webmanifest` and icons (192, 512, maskable) are generated by `build_site.py`; `404.html` by `not_found.py`.
- Print styles in `pages.css` give clean diet charts and guides on paper (header, booking panel, diary and share links hidden).
- WhatsApp green is #167A3E (passes 4.5:1 contrast with white text). Check new colours with axe-core in light and dark mode.

## Diet charts and food diary (19 Oct 2026)
- Pages: /diet-charts/ (index with the food diary) and 12 chart pages, EN + HI, built by `diet_charts.py` from `build_pages.build()`.
- Rules (language-independent): `diet_rules.py` — food tags (group, flags, meal fit) for every food in `thali_foods.F`, 14 diary plans with targets (protein per kg, fibre, fat limit, vegetables, fruit, water, fried/sugary/salty limits, small meals, bedtime snack) and good/limit/avoid rules, comorbidity rules (diabetes, BP/heart, kidney, pregnancy, lactose, over 65), and the chart pages. `check()` stops the build if a food has no tags or a rule names an unknown food.
- Text: `diet_text_en.py` / `diet_text_hi.py` (same keys, list lengths and veg/egg/non-veg codes; checked at build). Chart options start with V, E or N (W = Western).
- Food diary privacy is the same as the gut tracker: localStorage only (`dd-set`, `dd-day-YYYY-MM-DD`, cleared after 30 days), CSP with connect-src 'none'. Never add analytics or fetch calls.
- New foods go at the end of `thali_foods.F` with tags in `diet_rules.TAGS`; the Thali meter arrays are regenerated with `thali_foods.js()`.
- Linked from the home page (hook card, nav, Thali tab), every page header and footer, and the diet section of matching condition pages.

## Booking and sharing (19 Oct 2026)
- Home: a trust strip on phones (photo, credentials, live open/closed status from Arcura hours in India time) and reason/time chips that pre-fill the WhatsApp booking message, ending "(Found you on drlochab.com)".
- Inner pages: `page_extras()` in `build_pages.py` adds WhatsApp share links (under the byline and at the end of the article) and makes the booking buttons pre-fill a message naming the page the visitor was reading.
- Search snippets: `fit_title()` / `fit_desc()` in `build_pages.head()` shorten titles (about 60 characters) and descriptions (about 158) for every generated page.

## Daily features
- Food of the day: `food_day.py` (EN, HI, labels), injected at `/*FOOD*/` by `build_site.py`; one food per IST day, same order in both languages.
- Stool check tool: `stool_check.py`, built at /tools/stool-check/ by `build_pages.build()`.
- WhatsApp Channel: set `WA_CHANNEL` in `build_pages.py` to the channel invite link; the join block then appears under today's tip and in every page footer.
- Gut Health Tracker: `gut_tracker.py`, built at /tools/gut-tracker/. Privacy rules are in the module docstring: localStorage only, CSP with connect-src 'none', optional AES-GCM PIN encryption. Never add analytics, fetch calls or third-party scripts to this page.

## Local SEO (18 Oct 2026)
- `local_pages.py`: Gurgaon landing page and About page (EN + HI), plus the shared Physician structured data (hours, address, sameAs) used on the home page. Update hours and sameAs there.
- `hinglish.py`: Roman-script Hindi search phrases shown on Hindi pages; add entries for new pages.
- Titles use 'Gurgaon (Gurugram)' (`city` and `where` in `build_pages.L`).

### 21 Oct 2026: one diet section
- The "Diet guides" tab in Gut Health Daily is now a "Diet charts" tab: cards for the 12 chart pages (from `diet_rules.PAGES` and `diet_text_*.PAGES`), the food diary button and "All diet charts". Built by `build_site.diet_tab()` into `<!--DIET_TAB-->`.
- The `const GUIDES` data stays in `lochab-gastro.html`: `extract.js` uses it for the diet sections on condition pages. Only the picker UI was removed.
- Phones (≤760px): a floating "Diet charts" pill bottom left (`build_pages.diet_fab()`, class `fab fab-diet`), on the home page and all inner pages except the diet chart pages themselves (`footer(lang, diet=False)`).
- Tablets: the header keeps the "Diet charts" link (`.nav-diet`) when the other text links hide. Inner-page header nav now hides at 760px, same as the home page.

### 22 Oct 2026: audit fixes
- Home page no longer jumps while loading (layout shift 0.17 → 0.04 on phones): the gut tracker card is rendered in HTML by `build_site.trk_card()` (`<!--TRK_CARD-->`), and the card and hook tiles sit above the heading in the source instead of being moved there with CSS `order`. JS only swaps the wording for returning tracker users.
- Seasonal banner is one compact row on phones (button shows only the arrow, with an aria-label).
- Gut Health Daily tabs fit on a 360px phone without sideways scrolling.
- Diet chart pages have a "Print or save as PDF" button (`print_btn`).
- Tracker and stool check breadcrumbs say "Tools" and link to Gut Health Daily, not "Answers".
- Condition pages: the diet box heading is "What to eat" ("क्या खाएँ"), since full diet charts are separate.
- Breadcrumb links are at least 24px tall (tap targets).
- Favicon: SVG first, 96px PNG fallback (was a 58 KB 512px PNG).
- The build joins " →" with a non-breaking space so arrows never wrap alone onto a new line.
