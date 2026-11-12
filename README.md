# drlochab.com

Source of **[drlochab.com](https://drlochab.com)**, the website of Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist, Arcura Clinic, Sector 51, Gurugram (Gurgaon), India. Patients: please visit **https://drlochab.com** (English) or **https://drlochab.com/hi/** (Hindi).

The pages in this repository are built from `_src/` (see `_src/README.md`); do not edit the built pages by hand.

## Files
- `index.html`: the home page
- `tips.json`: the Gut Health Daily tips. Each tip has a `date` (YYYY-MM-DD). The site shows the latest tip whose date is today or earlier (India time). Tips with future dates stay hidden until their day comes.
- `ibs.json`: the IBS Corner tips, same format and date rule as `tips.json`. Categories: Food, Habits, Mind, Know.
- `dr-lochab.jpg`, `logo-mark.*`, `favicon.png`, `apple-touch-icon.png`, `og-image.jpg`: images
- `hi/`: the Hindi version of the site. `hi/tips.json` and `hi/ibs.json` hold the Hindi translations of the tips, with the same dates as the English files.
- `conditions/`, `procedures/`, `answers/` (and the same under `hi/`): one page per condition, procedure and common question, generated from the home page content. Edit them through Claude so the English, Hindi and home page stay in sync.
- `CNAME`: tells GitHub Pages to serve the site at drlochab.com
- `robots.txt`, `sitemap.xml`: help Google find the site

## Adding a tip
Add an entry to `tips.json`:

```json
{"date":"2026-11-07","cat":"Diet","title":"Short title","body":"Two or three plain sentences.","try":"One practical action for today."}
```

Categories in use: Diet, Acidity, Liver, Bowel, Safety, Myth.
