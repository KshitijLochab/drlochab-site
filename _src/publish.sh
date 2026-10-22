#!/bin/sh
# Rebuild the site from _src and copy it to the repository root, leaving the live tip and myth files alone.
set -e
cd "$(dirname "$0")"
PREVIEW= python3 build_site.py   # never publish held content
# stop here if the build has broken links, search tags or privacy settings
python3 tests/check_site.py site
(cd .. && python3 _src/tests/check_data.py)
cd site
tar --exclude=./tips.json --exclude=./ibs.json --exclude=./hi/tips.json --exclude=./hi/ibs.json --exclude=./myths.json --exclude=./hi/myths.json -cf - . | tar -xf - -C ../..
echo "Published to repository root."
