"""Checks the daily tips, IBS tips and myths that the weekly pull requests add. Run from the repository root:
    python3 _src/tests/check_data.py
Fails (exit code 1) on missing fields, bad dates, duplicate dates, English and Hindi files that do not match,
or myth links to pages that do not exist. Warns when fewer than 7 days of tips are left."""
import json, os, re, sys, datetime

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
TIP_KEYS = {"date", "cat", "title", "body", "try"}
MYTH_KEYS = {"date", "answer", "art", "link", "claim", "verdict", "truth", "do", "doctor"}
errors, warnings = [], []
today = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).date()

def load(rel):
    try:
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as ex:
        errors.append(f"{rel}: cannot read ({ex})"); return []
    if not isinstance(data, list):
        errors.append(f"{rel}: should be a list"); return []
    return data

def check(rel, keys):
    data = load(rel)
    seen = set()
    for i, x in enumerate(data):
        where = f"{rel} item {i + 1} ({x.get('date', '?')})"
        missing = keys - set(x)
        if missing: errors.append(f"{where}: missing {', '.join(sorted(missing))}")
        for k in keys & set(x):
            if k not in ("link", "doctor") and (not isinstance(x[k], str) or not x[k].strip()): errors.append(f"{where}: '{k}' is empty")
        d = x.get("date", "")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d):
            errors.append(f"{where}: date should look like 2026-11-14"); continue
        try: datetime.date.fromisoformat(d)
        except ValueError: errors.append(f"{where}: not a real date")
        if d in seen and keys is TIP_KEYS: errors.append(f"{where}: date used twice")
        seen.add(d)
        if keys is MYTH_KEYS:
            if x.get("answer") not in ("myth", "fact"): errors.append(f"{where}: answer must be 'myth' or 'fact'")
            link = x.get("link")
            if link:
                prefix = "hi/" if rel.startswith("hi/") else ""
                if not os.path.exists(os.path.join(ROOT, prefix + link, "index.html")): errors.append(f"{where}: link '{link}' does not exist")
    return data

for name, keys in (("tips.json", TIP_KEYS), ("ibs.json", TIP_KEYS), ("myths.json", MYTH_KEYS)):
    en, hi = check(name, keys), check("hi/" + name, keys)
    de, dh = [x.get("date") for x in en], [x.get("date") for x in hi]
    if sorted(de) != sorted(dh):
        errors.append(f"{name} and hi/{name} cover different dates (English {len(de)}, Hindi {len(dh)})")
    if keys is TIP_KEYS and de:
        last = max(datetime.date.fromisoformat(d) for d in de if re.fullmatch(r"\d{4}-\d{2}-\d{2}", d or ""))
        if (last - today).days < 7: warnings.append(f"{name}: tips run out on {last}; add more soon")

for w in warnings: print("  warning:", w)
if errors:
    print(f"{len(errors)} problem(s) in the tip and myth files:")
    for e in errors: print("  ✗", e)
    sys.exit(1)
print("Tip, IBS and myth files are valid.")
