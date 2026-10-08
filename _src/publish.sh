#!/bin/sh
# Rebuild the site from _src and copy it to the repository root, leaving the live tip files alone.
set -e
cd "$(dirname "$0")"
python3 build_site.py
cd site
tar --exclude=./tips.json --exclude=./ibs.json --exclude=./hi/tips.json --exclude=./hi/ibs.json -cf - . | tar -xf - -C ../..
echo "Published to repository root."
