#!/usr/bin/env python3
"""Controle op de gegenereerde site in dist/."""

import os
import re
import sys
from collections import Counter
from html.parser import HTMLParser

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
fouten = []
waarschuwingen = []


class Doc(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.title = ""
        self.desc = ""
        self.canonical = ""
        self.h1 = []
        self._in_title = False
        self._in_h1 = False
        self.text = []
        self._skip = 0
        self.imgs_without_alt = 0
        self.iframes = 0

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self._in_h1 = True
            self.h1.append("")
        elif tag == "a" and "href" in d:
            self.links.append((d["href"], d.get("rel", ""), d.get("target", "")))
        elif tag == "meta":
            if d.get("name") == "description":
                self.desc = d.get("content", "")
        elif tag == "link" and d.get("rel") == "canonical":
            self.canonical = d.get("href", "")
        elif tag in ("script", "style"):
            self._skip += 1
        elif tag == "img" and not d.get("alt"):
            self.imgs_without_alt += 1
        elif tag == "iframe":
            self.iframes += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "h1":
            self._in_h1 = False
        elif tag in ("script", "style"):
            self._skip = max(0, self._skip - 1)

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_h1 and self.h1:
            self.h1[-1] += data
        if not self._skip:
            self.text.append(data)


def lees(pad):
    with open(pad, encoding="utf-8") as f:
        return f.read()


pagina_paden = set()
docs = {}

for dirpath, dirnames, filenames in os.walk(ROOT):
    for fn in filenames:
        if not fn.endswith(".html"):
            continue
        full = os.path.join(dirpath, fn)
        rel = os.path.relpath(full, ROOT)
        d = Doc()
        d.feed(lees(full))
        docs[rel] = d
        if fn == "index.html":
            url = "/" + os.path.dirname(rel).replace(os.sep, "/")
            if url != "/":
                url += "/"
            url = url.replace("//", "/")
            pagina_paden.add(url)

pagina_paden.add("/rss.xml")
pagina_paden.add("/sitemap.xml")
pagina_paden.add("/robots.txt")
pagina_paden.add("/assets/site.css")
pagina_paden.add("/assets/favicon.svg")

# ---------------------------------------------------------------- links
inkomend = Counter()
for rel, d in sorted(docs.items()):
    for href, relattr, target in d.links:
        if href.startswith(("http://", "https://")):
            if "nofollow" not in relattr:
                fouten.append("%s: externe link zonder nofollow: %s" % (rel, href))
            if "noopener" not in relattr:
                fouten.append("%s: externe link zonder noopener: %s" % (rel, href))
            if target != "_blank":
                fouten.append("%s: externe link zonder target: %s" % (rel, href))
            continue
        if href.startswith(("mailto:", "#")):
            continue
        doel = href.split("#")[0]
        if not doel:
            continue
        if doel not in pagina_paden:
            fouten.append("%s: gebroken interne link: %s" % (rel, doel))
        else:
            inkomend[doel] += 1

for pad in sorted(pagina_paden):
    if pad.endswith("/") and inkomend[pad] == 0 and pad != "/":
        fouten.append("verweesde pagina, nergens naar gelinkt: %s" % pad)

# ---------------------------------------------------------------- meta
titels = Counter()
descs = Counter()
for rel, d in sorted(docs.items()):
    t = d.title.strip()
    titels[t] += 1
    descs[d.desc.strip()] += 1
    if len(t) > 70:
        waarschuwingen.append("%s: title %d tekens: %s" % (rel, len(t), t))
    if not (70 <= len(d.desc.strip()) <= 175):
        waarschuwingen.append("%s: description %d tekens" % (rel, len(d.desc.strip())))
    if len(d.h1) != 1:
        fouten.append("%s: %d h1-koppen" % (rel, len(d.h1)))
    if not d.canonical and rel != "404.html":
        fouten.append("%s: geen canonical" % rel)
    if d.imgs_without_alt:
        fouten.append("%s: %d afbeeldingen zonder alt" % (rel, d.imgs_without_alt))
    if d.iframes:
        fouten.append("%s: iframe staat direct in de html" % rel)

for t, n in titels.items():
    if n > 1:
        fouten.append("dubbele title (%dx): %s" % (n, t))
for t, n in descs.items():
    if n > 1:
        fouten.append("dubbele description (%dx): %s" % (n, t[:60]))

# ---------------------------------------------------------------- tekst
VERBODEN_WOORDEN = [
    r"\bje\b", r"\bjij\b", r"\bjou\b", r"\bjouw\b", r"\bjullie\b",
    r"\buw\b", r"\bwij\b", r"\bwe\b", r"\bons\b", r"\bonze\b",
    r"\bhoi\b", r"\blorem\b", r"\bipsum\b", r"\bplaceholder\b",
    r"\bTODO\b", r"\bTBD\b", r"\bXXX\b", r"\bvoorbeeldtekst\b",
    r"\bnog in te vullen\b", r"\bdummy\b",
]
UITZONDERING = re.compile(r"(Onze Diensten|onze-diensten)")

for rel, d in sorted(docs.items()):
    tekst = " ".join(d.text)
    tekst = re.sub(r"https?://\S+", " ", tekst)
    tekst = re.sub(r"\s+", " ", tekst)
    for pat in VERBODEN_WOORDEN:
        for m in re.finditer(pat, tekst, re.IGNORECASE):
            fragment = tekst[max(0, m.start() - 45):m.end() + 45]
            if UITZONDERING.search(fragment):
                continue
            fouten.append("%s: verboden woord %r in: ...%s..."
                          % (rel, m.group(0), fragment.strip()))
    for teken, naam in [("—", "em-dash"), ("–", "en-dash")]:
        if teken in tekst:
            i = tekst.index(teken)
            fouten.append("%s: %s in: ...%s..."
                          % (rel, naam, tekst[max(0, i - 40):i + 40]))

# ---------------------------------------------------------------- ankerteksten
TOEGESTAAN = re.compile(
    r"^(OvernameAdvies\.nl|WebshopOvername\.nl"
    r"|www\.overnameadvies\.nl|www\.webshopovername\.nl"
    r"|https://www\.(overnameadvies|webshopovername)\.nl/[^\s]*)$")

anker = re.compile(
    r'<a href="(https://[^"]+)"[^>]*rel="nofollow noopener">([^<]*)</a>')
externe_hosts = Counter()
for rel in sorted(docs):
    html = lees(os.path.join(ROOT, rel))
    for url, tekst in anker.findall(html):
        host = url.split("/")[2]
        externe_hosts[host] += 1
        if host not in ("www.overnameadvies.nl", "www.webshopovername.nl"):
            fouten.append("%s: externe link naar %s" % (rel, host))
        if not TOEGESTAAN.match(tekst.strip()):
            fouten.append("%s: ankertekst niet toegestaan: %r" % (rel, tekst))

# ---------------------------------------------------------------- sitemap
sitemap = lees(os.path.join(ROOT, "sitemap.xml"))
locs = re.findall(r"<loc>([^<]+)</loc>", sitemap)
sm_paden = {re.sub(r"^https://123bedrijfstarten\.nl", "", u) for u in locs}
sm_paden = {p if p else "/" for p in sm_paden}
site_paden = {p for p in pagina_paden if p.endswith("/")}
if sm_paden != site_paden:
    for p in sorted(site_paden - sm_paden):
        fouten.append("ontbreekt in sitemap: %s" % p)
    for p in sorted(sm_paden - site_paden):
        fouten.append("staat wel in sitemap maar bestaat niet: %s" % p)

# ---------------------------------------------------------------- rapport
print("pagina's: %d" % len(docs))
print("interne bestemmingen: %d" % len(pagina_paden))
print("externe links: %s" % dict(externe_hosts))
woorden = sum(len(" ".join(d.text).split()) for d in docs.values())
print("woorden in de html: ongeveer %d" % woorden)

if waarschuwingen:
    print("\nWAARSCHUWINGEN (%d)" % len(waarschuwingen))
    for w in waarschuwingen:
        print("  " + w)
if fouten:
    print("\nFOUTEN (%d)" % len(fouten))
    for f in fouten:
        print("  " + f)
    sys.exit(1)
print("\nGeen fouten.")
