# drlochab.com: how releases, checks and rollback work

Plain-language notes for Dr. Lochab and anyone who works on the site.

## What the site is
- A static website: plain HTML pages, no database, no logins, no server code, no analytics or third-party scripts.
- Source files live in `_src/`. The build (`python3 build_site.py`) writes the finished pages to `_src/site/`, and `publish.sh` copies them to the repository root.
- Hosting is GitHub Pages (repository `KshitijLochab/drlochab-site`, branch `main`, custom domain `drlochab.com` via the `CNAME` file). A change pushed to `main` is live in 1 to 2 minutes.

## Backups
- Every change is a commit in Git, so the complete history of every page is kept on GitHub. Nothing else needs backing up.
- For an extra offline copy: on GitHub, choose Code → Download ZIP.

## How a change goes live
1. Edit the source in `_src/` (or, for daily tips, the weekly pull request edits `tips.json`, `ibs.json`, `myths.json` and their `hi/` copies).
2. `bash _src/publish.sh` builds the site, **runs the checks**, and copies the pages to the root only if the checks pass.
3. Commit and push to `main`.
4. GitHub runs the **Site checks** automatically (the Actions tab). A green tick means the published site passed; a red cross means look before anything else.

## The checks (`_src/tests/`)
| Check | What it catches |
|---|---|
| `check_data.py` | Tip, IBS-tip and myth files: missing fields, bad or repeated dates, English and Hindi files out of step, myth links to pages that do not exist. Warns when fewer than 7 days of tips are left. |
| `check_site.py` | Every page: title, description, one main heading, canonical and English–Hindi links, valid structured data, broken links or anchors, missing images, wrong phone or WhatsApp numbers, sitemap coverage, and privacy (no outside scripts; tracker, stool check and diet pages keep their "send nothing" setting). |
| `browser_check.js` | In a real browser at phone and desktop width: no script errors, nothing wider than the screen, today's tip loads, a symptom gives a booking button, the WhatsApp booking link is right, a link to #visit lands on the booking section, the preparation planner makes a calendar file, the diet diary adds food, the stool check answers, the tracker keeps its privacy setting. |

Run them locally from the repository root:
```
python3 _src/tests/check_data.py
python3 _src/tests/check_site.py            # the published files
python3 -m http.server 8765 &  &&  node _src/tests/browser_check.js
```

## Weekly tip pull requests
- They are opened automatically and **never merged automatically**.
- Wait for the green tick on the pull request before merging. If there is a red cross, open "Details" to see which item is wrong.

## Staging (trying a change before it is live)
- Build locally (`python3 build_site.py`), then open `_src/site/` with `python3 -m http.server 8765` and look at http://localhost:8765.
- For a bigger change, put it on a separate branch and open a pull request: the checks run on it before anything reaches the live site.

## Rollback (undo a bad release)
- **Fastest:** on GitHub, open the commit that caused the problem → "Revert". Merge the revert; the site is back in 1 to 2 minutes.
- **From a computer:** `git revert <commit>` then `git push`. This keeps history and is always safe.
- Never use `git push --force` on `main`.

## Things that must not change without Dr. Lochab's say-so
- No analytics, trackers, cookies or third-party scripts.
- No patient testimonials or "best doctor" claims (NMC rules). No medicine brand names or doses.
- Medical content changes are reviewed by Dr. Lochab before they go live.
