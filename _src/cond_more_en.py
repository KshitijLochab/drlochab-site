"""Deeper sections for condition pages (shown after 'Treatment') and for some answer pages (after their sections), English.
Approved by Dr. Lochab on 31 Oct 2026 ("add longer sections for the condition pages"). Content lives in deep/part*_en.py, merged here.
Each entry: slug -> list of (heading, [items]); an item starting with "- " is a bullet, others are paragraphs.
The English and Hindi files must have the same slugs, sections and item counts (checked in medical_review.check()).
No first-person voice, no medicine names, brand names or doses; conservative and guideline-consistent; warning signs carry the 112 line."""
import importlib, pkgutil, os
MORE = {}
for _m in sorted(pkgutil.iter_modules([os.path.join(os.path.dirname(os.path.abspath(__file__)), "deep")]), key=lambda m: m.name):
    if _m.name.endswith("_en"):
        _d = importlib.import_module("deep." + _m.name).MORE
        assert not set(_d) & set(MORE), set(_d) & set(MORE)
        MORE.update(_d)
