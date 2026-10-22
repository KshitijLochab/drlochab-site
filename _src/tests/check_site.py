"""Static checks on the published site (no browser needed). Run from the repository root:
    python3 _src/tests/check_site.py            # checks the published files in the repo root
    python3 _src/tests/check_site.py _src/site  # checks a fresh local build
Exits with code 1 if anything is broken. Warnings (long titles etc.) do not fail the run.
Uses only the Python standard library, so it runs anywhere (including GitHub Actions)."""
import os, re, sys, json, html
from html.parser import HTMLParser
from posixpath import normpath, join
from urllib.parse import urldefrag, unquote

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
SITE = "https://drlochab.com"
PHONE, WA = "tel:+919667104882", "https://wa.me/919667104882"
SKIP_DIRS = {"_src", ".git", ".github", "node_modules"}
PRIVATE_PAGES = ("/tools/", "/hi/tools/", "/diet-charts/", "/hi/diet-charts/")   # must block outgoing data (CSP connect-src 'none')

pages, files = {}, set()
for d, dirs, fs in os.walk(ROOT):
    dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
    for f in fs:
        rel = "/" + os.path.relpath(os.path.join(d, f), ROOT).replace(os.sep, "/")
        files.add(rel)
        if f.endswith(".html"):
            pages[rel[:-len("index.html")] if f == "index.html" else rel] = open(os.path.join(d, f), encoding="utf-8").read()


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.imgs, self.ld, self.scripts, self.iframes = [], set(), [], [], [], []
        self.meta, self.alt, self.title, self.canon, self.h1, self._in = {}, {}, "", None, 0, None

    def handle_starttag(self, t, a):
        a = dict(a)
        if "id" in a: self.ids.add(a["id"])
        if t == "a" and a.get("href") is not None: self.links.append(a["href"])
        if t == "img": self.imgs.append(a)
        if t == "iframe": self.iframes.append(a.get("src", ""))
        if t == "script":
            self.scripts.append(a.get("src"))
            self._in = "ld" if a.get("type") == "application/ld+json" else "js"
            if self._in == "ld": self.ld.append("")
        if t == "title": self._in = "title"
        if t == "meta":
            k = a.get("name") or a.get("property") or a.get("http-equiv")
            if k: self.meta[k.lower()] = a.get("content", "")
        if t == "link" and a.get("rel") == "canonical": self.canon = a.get("href")
        if t == "link" and a.get("rel") == "alternate" and a.get("hreflang"): self.alt[a["hreflang"]] = a.get("href")
        if t == "h1": self.h1 += 1

    def handle_endtag(self, t):
        if t in ("script", "title"): self._in = None

    def handle_data(self, d):
        if self._in == "ld": self.ld[-1] += d
        elif self._in == "title": self.title += d


errors, warnings = [], []
def err(u, msg): errors.append(f"{u}: {msg}")
def warn(u, msg): warnings.append(f"{u}: {msg}")

parsed = {}
def get(u):
    if u not in parsed:
        p = Page(); p.feed(pages[u]); parsed[u] = p
    return parsed[u]

def resolve(base, href):
    target, frag = urldefrag(href)
    if not target:
        return base, frag
    full = normpath(join(base if base.endswith("/") else base.rsplit("/", 1)[0] + "/", unquote(target))) if not target.startswith("/") else normpath(unquote(target))
    if target.endswith("/") and not full.endswith("/"): full += "/"
    return full, frag

for u in sorted(pages):
    p = get(u)
    is404 = u.endswith("404.html")
    if not p.title.strip(): err(u, "no <title>")
    elif len(p.title.strip()) > 70: warn(u, f"title is {len(p.title.strip())} characters")
    if not is404:
        if p.h1 != 1: err(u, f"{p.h1} <h1> headings (should be 1)")
        if not p.meta.get("description"): err(u, "no meta description")
        if p.canon != SITE + u: err(u, f"canonical is {p.canon}")
        for k in ("en", "hi", "x-default"):
            if k not in p.alt: err(u, f"missing hreflang {k}")
        other = u[3:] if u.startswith("/hi/") else "/hi" + u
        if other not in pages: err(u, f"language twin {other} does not exist")
        elif p.alt.get("hi" if not u.startswith("/hi/") else "en") != SITE + other: err(u, "hreflang points to the wrong page")
    for block in p.ld:
        try: json.loads(block)
        except ValueError as ex: err(u, f"invalid JSON-LD ({ex})")
    for a in p.imgs:
        if "alt" not in a: err(u, f"image without alt: {a.get('src')}")
        s = a.get("src", "")
        if s.startswith("/") and s not in files: err(u, f"missing image {s}")
    # privacy: no third-party scripts or frames, ever
    for s in p.scripts:
        if s and re.match(r"(https?:)?//", s): err(u, f"external script {s}")
    for s in p.iframes:
        if re.match(r"(https?:)?//", s): err(u, f"external iframe {s}")
    if re.search(r"fetch\(\s*['\"`]https?://", pages[u]): err(u, "script fetches an external address")
    if u.startswith(PRIVATE_PAGES) and "connect-src 'none'" not in p.meta.get("content-security-policy", ""):
        err(u, "private tool page lost its Content-Security-Policy (connect-src 'none')")
    # links
    for h in p.links:
        h = html.unescape(h)
        if h.startswith("tel:"):
            if h not in (PHONE, "tel:112"): err(u, f"unexpected phone link {h}")
            continue
        if h.startswith("https://wa.me/"):
            if not (h.startswith(WA) or h.startswith("https://wa.me/?text=")): err(u, f"unexpected WhatsApp link {h[:60]}")
            continue
        if re.match(r"(https?:|mailto:|javascript:|data:)", h) or h.startswith("//"):
            continue
        full, frag = resolve(u, h)
        if full == u or (not urldefrag(h)[0]):
            if frag and frag not in p.ids: err(u, f"link to missing #{frag}")
            continue
        if full in pages or full + "/" in pages:
            tgt = full if full in pages else full + "/"
            if frag and frag not in get(tgt).ids: err(u, f"link to missing {tgt}#{frag}")
        elif full not in files:
            err(u, f"broken link {h}")

# sitemap
sm = open(os.path.join(ROOT, "sitemap.xml"), encoding="utf-8").read()
locs = {l[len(SITE):] for l in re.findall(r"<loc>([^<]+)</loc>", sm)}
for u in pages:
    if not u.endswith("404.html") and u not in locs: err(u, "not in sitemap.xml")
for u in locs:
    if u not in pages: err(u, "listed in sitemap.xml but the page does not exist")

print(f"Checked {len(pages)} pages and {len(files)} files in {ROOT}")
for w in warnings[:15]: print("  warning:", w)
if len(warnings) > 15: print(f"  ... and {len(warnings) - 15} more warnings")
if errors:
    print(f"\n{len(errors)} problem(s):")
    for e in errors[:80]: print("  ✗", e)
    sys.exit(1)
print("All static checks passed.")
