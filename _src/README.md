# Source for drlochab.com

This folder is not published (Jekyll skips folders starting with `_`). It holds everything needed to rebuild the site and make social media images.

## Rebuild and publish the site
Requirements: Python 3 with Pillow, Node.js.

    sh _src/publish.sh

This runs `build_site.py` (English home, Hindi home, and all condition, procedure and answer pages via `build_pages.py`) into `_src/site/`, then copies the result to the repository root. The live tip files (`/tips.json`, `/ibs.json`, `/hi/tips.json`, `/hi/ibs.json`) are never overwritten; the copies in `_src` only exist so the build runs.

## Where content lives
- `lochab-gastro.html`: the English home page (markup, styles, script, data for symptoms, conditions, procedures, myths, diet guides, illustrations).
- `hindi.py`: Hindi text for the home page. Every English string it lists must still exist, or the build stops, so English edits need a matching Hindi update.
- `seo_en.py` / `seo_hi.py`: extra content for condition, procedure and answer pages (same order as the home page lists). Add a new answer page by appending to `ANSWERS` in both files.
- `build_pages.py` + `pages.css`: template for those pages, with structured data, breadcrumbs and hreflang.
- `brand/`, `fonts/`, `dr-lochab.jpg`: logo, fonts (Young Serif, Figtree, and Devanagari subsets of Tiro Devanagari Hindi and Mukta for Hindi images, all OFL licensed) and portrait.

## Social media images
Requirements: Python Playwright with Chromium (`python3 -m playwright install chromium`). Run `build_site.py` first, which writes `data-en.json`.
- `social/make_posts.py`: Instagram posts and carousels (1080x1350) to `_src/out/instagram/`. Edit the `POSTS` dictionary.
- `social/fatty_liver.py`: Google post image (1200x900) and A4 patient handout.
- `social/make_catalogue.py` + `social/condition_art.py`: square WhatsApp catalogue images and custom condition drawings.
- `social/week_2026_10_12.py`: example of a full week (Instagram EN and HI, Google post, WhatsApp Status) in one script.
- `social/log.md`: what has already been made and posted, to avoid repeats.

See `BRAND.md` for colours, type, voice and rules.
