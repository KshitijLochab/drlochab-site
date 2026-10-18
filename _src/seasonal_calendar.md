# Seasonal content calendar (set up 19 Oct 2026)

Banners go live about two weeks before each season so Google has time to index the page. The banner list is `SEASONS` in
`winter_guide.py` (appended to `seo_en.SEASONAL` / `seo_hi.SEASONAL`). Each banner has `start` and `until`; the site hides it
outside those dates on its own, so no rebuild is needed when a banner switches.

| Season | Banner live | Links to | Status |
|---|---|---|---|
| Navratri 2026 | until 21 Oct 2026 | guides/navratri-fasting-guide | live |
| Diwali 2026 (8 Nov) | 21 Oct – 12 Nov 2026 | guides/diwali-food-guide | live |
| Wedding season | 12 Nov – 22 Dec 2026 | guides/winter-wedding-season-guide | written 18 Oct 2026 |
| Christmas and New Year parties | 22 Dec 2026 – 2 Jan 2027 | answers/how-much-alcohol-is-safe-for-liver | scheduled |
| Winter, Lohri (13 Jan), Sankranti (15 Jan) | 2 Jan – 1 Feb 2027 | guides/winter-wedding-season-guide | scheduled |
| Ramzan (about 9 Feb – 10 Mar 2027) | from about 26 Jan 2027 | guide not written yet | **write by 10 Jan 2027**: roza without acidity, sehri and iftar plates, diabetes and fasting, when to break the fast |
| Holi (22 Mar 2027) | from about 8 Mar 2027 | guide not written yet | **write by 20 Feb 2027**: bhang and the liver, gujiya and fried snacks, food safety, colours swallowed by children |
| Chaitra Navratri (about 7 – 15 Apr 2027) | 24 Mar – 16 Apr 2027 | guides/navratri-fasting-guide | scheduled (guide is undated, reused) |
| Summer | 16 Apr – 1 Jul 2027 | answers/hepatitis-a-and-e | scheduled (a full summer guide on water, heat, typhoid and street food would be better; write by 1 Apr 2027) |
| Monsoon | 1 Jul – 16 Sep 2027 | answers/stomach-infection-gastroenteritis | scheduled |
| Sharad Navratri (from 30 Sep 2027) | 16 Sep – 9 Oct 2027 | guides/navratri-fasting-guide | scheduled |
| Diwali 2027 (29 Oct) | from about 15 Oct 2027 | guides/diwali-food-guide | update the year in the text, then add the banner |

When a new guide is written, add it to `SPECIAL` (as `diwali_guide.py` and `winter_guide.py` do), add its banner to `SEASONS`
with EN and HI text, and draw its illustration in `guide_art.py`.
