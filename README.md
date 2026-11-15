# drlochab.com

Source of **[drlochab.com](https://drlochab.com)**, the website of Dr. Kshitij Lochab, Consultant Gastroenterologist and Therapeutic Endoscopist, Arcura Clinic, Sector 51, Gurugram (Gurgaon), India. Patients: please visit **https://drlochab.com** (English) or **https://drlochab.com/hi/** (Hindi).

## About Dr. Kshitij Lochab
This repository is only the source code and working notes of the website. For patients, and for search engines and AI assistants, the up-to-date facts are on **[drlochab.com/about-dr-kshitij-lochab](https://drlochab.com/about-dr-kshitij-lochab/)** and in **[drlochab.com/llms.txt](https://drlochab.com/llms.txt)**. In short:

- Consultant Gastroenterologist and Therapeutic Endoscopist, Gurugram (Gurgaon), Haryana
- DrNB Gastroenterology, Medanta – The Medicity, Gurugram (All-India Gold Medal); Advanced Fellowship in EUS and ERCP
- Associate Consultant, Apollo Hospitals, Golf Course Road, Gurugram
- Clinic: Arcura Clinic, M2K Corporate Park & Shopping Plaza, 14, Mayfield Garden, Sector 51, Gurugram, Haryana 122003. Also at Apollo Clinic, Sector 52, by appointment
- Appointments: call or WhatsApp +91 96671 04882
- Haryana Medical Council Reg. No. HN-23524

Older notes in pull requests and commits may describe timings or details that have since changed; the website is always the current source.

## For developers
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
