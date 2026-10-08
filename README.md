# drlochab.com

Website of Dr. Kshitij Lochab, Consultant Gastroenterologist, Gurugram.

## Files
- `index.html`: the whole website
- `tips.json`: the Gut Health Daily tips. Each tip has a `date` (YYYY-MM-DD). The site shows the latest tip whose date is today or earlier (India time). Tips with future dates stay hidden until their day comes.
- `dr-lochab.jpg`, `logo-mark.*`, `favicon.png`, `apple-touch-icon.png`, `og-image.jpg`: images
- `CNAME`: tells GitHub Pages to serve the site at drlochab.com
- `robots.txt`, `sitemap.xml`: help Google find the site

## Adding a tip
Add an entry to `tips.json`:

```json
{"date":"2026-11-07","cat":"Diet","title":"Short title","body":"Two or three plain sentences.","try":"One practical action for today."}
```

Categories in use: Diet, Acidity, Liver, Bowel, Safety, Myth.
