#!/usr/bin/env python3
"""Generator voor 123bedrijfstarten.nl. Alleen standaardbibliotheek."""

import html
import os
import re
import shutil
from datetime import date

from content import PAGES, NEWS_ORDER

SITE = "https://123bedrijfstarten.nl"
NAAM = "123 Bedrijf Starten"
MAIL = "info@123bedrijfstarten.nl"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")

NAV = [
    ("Starten of overnemen", "/starten-of-overnemen/"),
    ("Checklists", "/checklists/"),
    ("Rekentools", "/tools/"),
    ("Verkopen", "/verkopen/"),
    ("Kennisbank", "/kennisbank/"),
    ("Nieuws", "/nieuws/"),
    ("Over", "/over/"),
]

FOOTER_COLS = [
    ("Beginnen", [
        ("Starten of overnemen", "/starten-of-overnemen/"),
        ("Waarom overnemen", "/starten-of-overnemen/waarom-overnemen/"),
        ("Cijfers en onderzoek", "/starten-of-overnemen/cijfers-en-onderzoek/"),
        ("Checklist bedrijf beginnen", "/checklists/bedrijf-beginnen/"),
        ("Checklist webshop beginnen", "/checklists/webshop-beginnen/"),
    ]),
    ("Rekenen", [
        ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
        ("Wat is mijn webshop waard", "/tools/wat-is-mijn-webshop-waard/"),
        ("Waardebepaling", "/kennisbank/waardebepaling/"),
        ("Multiples", "/kennisbank/multiples/"),
        ("Goodwill", "/kennisbank/goodwill/"),
    ]),
    ("Verkopen", [
        ("Wanneer verkopen", "/verkopen/wanneer-verkopen/"),
        ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
        ("Verkoopklaar ondernemen", "/verkopen/verkoopklaar-ondernemen/"),
        ("Vijf stappen", "/verkopen/vijf-stappen/"),
        ("Begrippenlijst", "/kennisbank/begrippenlijst/"),
    ]),
    ("Platform", [
        ("Over dit platform", "/over/"),
        ("Uitgelichte platforms", "/platforms/"),
        ("Video", "/video/"),
        ("Nieuws", "/nieuws/"),
        ("Contact", "/contact/"),
    ]),
]

CSS = """
:root{
  --paper:#fbfaf7; --soft:#f3efe7; --ink:#15201e; --muted:#5b6663;
  --teal:#0d5b52; --teal-dark:#08403a; --amber:#a9640f; --line:#dcd6c9;
  --sans:"Segoe UI",system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif;
  --wrap:1080px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:17px;line-height:1.65}
img,svg{max-width:100%}
a{color:var(--teal-dark);overflow-wrap:anywhere}
a:hover{color:var(--amber)}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-9999px}
.skip:focus{left:8px;top:8px;background:#fff;padding:8px 12px;z-index:99;border:2px solid var(--teal)}

/* header */
.top{background:var(--teal-dark);color:#f4f1ea}
.top .wrap{display:flex;align-items:center;gap:24px;flex-wrap:wrap;padding-top:14px;padding-bottom:14px}
.brand{display:flex;align-items:center;gap:11px;text-decoration:none;color:#fff;flex:0 0 auto}
.brand .mark{display:flex;gap:3px}
.brand .mark span{width:20px;height:26px;border:2px solid #d9a441;border-radius:3px;
  display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#d9a441}
.brand b{font-size:17px;letter-spacing:.02em;font-weight:700;line-height:1.15}
.brand small{display:block;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:#a8c0bb;font-weight:600}
nav.main{margin-left:auto}
nav.main ul{list-style:none;display:flex;flex-wrap:wrap;gap:2px;margin:0;padding:0}
nav.main a{display:block;padding:7px 11px;color:#e7e2d8;text-decoration:none;font-size:14.5px;
  border-radius:4px}
nav.main a:hover,nav.main a[aria-current]{background:rgba(255,255,255,.12);color:#fff}

/* breadcrumb */
.crumbs{background:var(--soft);border-bottom:1px solid var(--line);font-size:13.5px}
.crumbs .wrap{padding-top:9px;padding-bottom:9px}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:7px;color:var(--muted)}
.crumbs li+li::before{content:"›";margin-right:7px;color:#a9a396}
.crumbs a{color:var(--muted)}

/* hero */
.hero{background:var(--soft);border-bottom:1px solid var(--line)}
.hero .wrap{padding-top:46px;padding-bottom:46px;max-width:920px}
h1{font-size:clamp(28px,4.4vw,44px);line-height:1.14;letter-spacing:-.02em;margin:0 0 16px}
.lead{font-size:19.5px;line-height:1.6;color:#3b4644;margin:0;max-width:66ch}
.kicker{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--amber);
  font-weight:700;margin:0 0 12px}

main{padding:44px 0 8px}
main .wrap,.crumbs .wrap{max-width:920px}
.wrap{min-width:0}
article{max-width:100%;min-width:0}
h2{font-size:27px;line-height:1.22;letter-spacing:-.01em;margin:40px 0 12px}
h3{font-size:19.5px;line-height:1.3;margin:28px 0 8px}
p{margin:0 0 16px;max-width:74ch}
article ul,article ol{margin:0 0 18px;padding-left:22px}
article li{margin-bottom:7px}
.small{font-size:14.5px;color:var(--muted)}

/* blokken */
.panel{background:#fff;border:1px solid var(--line);border-radius:8px;padding:22px 24px;margin:24px 0}
.panel h3{margin-top:0}
.panel p:last-child,.panel ul:last-child{margin-bottom:0}
.quote{border-left:4px solid var(--amber);background:#fff;padding:16px 20px;margin:24px 0;
  border-radius:0 6px 6px 0}
.quote p:last-child{margin-bottom:0}

.steps{list-style:none;margin:24px 0;padding:0;counter-reset:s}
.steps li{counter-increment:s;position:relative;padding:0 0 20px 58px;border-left:2px solid var(--line);
  margin-left:17px}
.steps li:last-child{border-left-color:transparent;padding-bottom:0}
.steps li::before{content:counter(s);position:absolute;left:-18px;top:-2px;width:34px;height:34px;
  background:var(--teal);color:#fff;border-radius:50%;display:flex;align-items:center;
  justify-content:center;font-weight:700;font-size:15px}
.steps b{display:block;font-size:17.5px;margin-bottom:4px}
.steps p{margin:0}

.tick{list-style:none;padding-left:0;margin:0 0 18px}
.tick li{position:relative;padding-left:28px;margin-bottom:9px}
.tick li::before{content:"";position:absolute;left:4px;top:9px;width:8px;height:8px;
  background:var(--amber);border-radius:2px;transform:rotate(45deg)}

.tbl{overflow-x:auto;max-width:100%;margin:24px 0;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:15.5px;background:#fff}
th,td{border:1px solid var(--line);padding:9px 12px;text-align:left;vertical-align:top}
th{background:var(--soft);font-weight:700}

.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(285px,1fr));gap:16px;margin:26px 0}
.card{background:#fff;border:1px solid var(--line);border-radius:8px;padding:20px;display:block;
  text-decoration:none;color:inherit}
.card:hover{border-color:var(--teal);box-shadow:0 3px 14px rgba(13,91,82,.09)}
.card b{display:block;font-size:17px;margin-bottom:6px;color:var(--teal-dark)}
.card span{display:block;font-size:14.5px;color:var(--muted);line-height:1.5}
.full{max-width:none}

.plat{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin:26px 0}
.plat .box{background:#fff;border:1px solid var(--line);border-top:4px solid var(--teal);
  border-radius:8px;padding:24px}
.plat .box h3{margin-top:0}
.plat .box .url{font-size:14.5px;word-break:break-all}
.plat .box ul{margin-bottom:14px}

/* video */
.vid{margin:26px 0}
.vidbox{position:relative;background:var(--teal-dark);border-radius:8px;overflow:hidden;
  aspect-ratio:16/9}
.vidbox iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.vidbox button{position:absolute;inset:0;width:100%;height:100%;border:0;cursor:pointer;
  background:linear-gradient(150deg,#08403a,#0d5b52 60%,#12766a);color:#fff;
  font-family:var(--sans);font-size:16px;display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;padding:20px;text-align:center}
.vidbox button:hover .play{background:#d9a441;border-color:#d9a441;color:#08403a}
.play{width:64px;height:64px;border:3px solid #d9a441;border-radius:50%;display:flex;
  align-items:center;justify-content:center;color:#d9a441;font-size:22px;line-height:1}
.vid figcaption{font-size:14.5px;color:var(--muted);margin-top:9px}

/* rekentool */
.calc{background:#fff;border:1px solid var(--line);border-radius:8px;padding:24px;margin:26px 0}
.calc .row{display:grid;grid-template-columns:1fr 150px;gap:12px;align-items:center;
  padding:9px 0;border-bottom:1px solid var(--soft)}
.calc label{font-size:15.5px}
.calc label small{display:block;color:var(--muted);font-size:13px;line-height:1.4}
.calc input,.calc select{width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:5px;
  font-family:var(--sans);font-size:15.5px;background:var(--paper);color:var(--ink)}
.calc input:focus,.calc select:focus{outline:2px solid var(--teal);border-color:var(--teal)}
.calc .out{margin-top:20px;background:var(--soft);border-radius:6px;padding:18px 20px}
.calc .out .big{font-size:29px;font-weight:700;color:var(--teal-dark);letter-spacing:-.01em}
.calc .out .sub{font-size:14.5px;color:var(--muted);margin-top:4px}
.calc .bars{margin-top:14px;font-size:14.5px}
.calc .bars div{display:flex;justify-content:space-between;padding:5px 0;border-top:1px solid var(--line)}

/* nieuws */
.list{list-style:none;padding:0;margin:26px 0}
.list li{border-top:1px solid var(--line);padding:18px 0}
.list li:last-child{border-bottom:1px solid var(--line)}
.list time{font-size:13px;letter-spacing:.09em;text-transform:uppercase;color:var(--amber);
  font-weight:700}
.list a{font-size:20px;text-decoration:none;display:block;margin:4px 0 5px;line-height:1.3}
.list p{margin:0;font-size:15.5px;color:var(--muted)}
.meta{font-size:14px;color:var(--muted);margin:-6px 0 22px}

.related{border-top:1px solid var(--line);margin-top:48px;padding-top:24px}
.related h2{font-size:19px;margin:0 0 12px}
.related ul{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;gap:8px}
.related a{display:block;background:#fff;border:1px solid var(--line);border-radius:20px;
  padding:6px 15px;font-size:14.5px;text-decoration:none}
.related a:hover{border-color:var(--teal)}

/* footer */
footer{background:var(--teal-dark);color:#cfdbd8;margin-top:56px;font-size:15px}
footer .wrap{padding-top:40px;padding-bottom:26px}
.fgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:28px}
footer h4{color:#fff;font-size:13px;letter-spacing:.14em;text-transform:uppercase;margin:0 0 12px}
footer ul{list-style:none;margin:0;padding:0}
footer li{margin-bottom:7px}
footer a{color:#cfdbd8;text-decoration:none}
footer a:hover{color:#e8c27a}
.fbot{border-top:1px solid rgba(255,255,255,.15);margin-top:30px;padding-top:18px;
  display:flex;flex-wrap:wrap;gap:8px 20px;font-size:14px;color:#a8bab6}
.fbot a{color:#a8bab6}

@media(max-width:760px){
  body{font-size:16.5px}
  .top .wrap{gap:12px}
  nav.main{margin-left:0;width:100%}
  nav.main a{padding:6px 9px;font-size:14px}
  .calc .row{grid-template-columns:1fr;gap:5px}
  .steps li{padding-left:46px}
}
"""

JS_VIDEO = """
document.addEventListener('click',function(e){
  var b=e.target.closest('.vidbox button');if(!b)return;
  var f=document.createElement('iframe');
  f.src=b.getAttribute('data-src');f.title=b.getAttribute('data-title');
  f.allow='accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture';
  f.setAttribute('allowfullscreen','');f.setAttribute('loading','lazy');
  b.parentNode.replaceChild(f,b);
});
"""


def esc(t):
    return html.escape(t, quote=False)


def ext(url, text=None):
    return ('<a href="%s" target="_blank" rel="nofollow noopener">%s</a>'
            % (url, esc(text or url)))


# ---------------------------------------------------------------- rendering

def render_blocks(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append("<p>%s</p>" % b[1])
        elif kind == "h2":
            out.append('<h2 id="%s">%s</h2>' % (slug_id(b[1]), esc(b[1])))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % esc(b[1]))
        elif kind == "ul":
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "tick":
            out.append('<ul class="tick">%s</ul>'
                       % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "ol":
            out.append("<ol>%s</ol>" % "".join("<li>%s</li>" % i for i in b[1]))
        elif kind == "steps":
            items = "".join("<li><b>%s</b><p>%s</p></li>" % (esc(t), x) for t, x in b[1])
            out.append('<ol class="steps">%s</ol>' % items)
        elif kind == "panel":
            out.append('<div class="panel"><h3>%s</h3>%s</div>'
                       % (esc(b[1]), render_blocks(b[2])))
        elif kind == "quote":
            out.append('<div class="quote">%s</div>' % render_blocks(b[1]))
        elif kind == "table":
            head = "".join("<th>%s</th>" % esc(h) for h in b[1])
            rows = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r)
                           for r in b[2])
            out.append('<div class="tbl"><table><thead><tr>%s</tr></thead>'
                       "<tbody>%s</tbody></table></div>" % (head, rows))
        elif kind == "cards":
            cards = "".join('<a class="card" href="%s"><b>%s</b><span>%s</span></a>'
                            % (h, esc(t), esc(d)) for t, d, h in b[1])
            out.append('<div class="cards full">%s</div>' % cards)
        elif kind == "video":
            _, listid, label, caption = b
            src = ("https://www.youtube-nocookie.com/embed/videoseries?list=%s&rel=0"
                   % listid)
            out.append(
                '<figure class="vid"><div class="vidbox">'
                '<button type="button" data-src="%s" data-title="%s">'
                '<span class="play" aria-hidden="true">&#9654;</span>'
                "<span>%s<br><small>Video laadt pas na een klik, via youtube-nocookie.com"
                "</small></span></button></div>"
                "<figcaption>%s</figcaption></figure>"
                % (src, esc(label), esc(label), caption))
        elif kind == "raw":
            out.append(b[1])
        else:
            raise ValueError("onbekend blok: %s" % kind)
    return "".join(out)


def slug_id(text):
    s = text.lower()
    s = s.replace("&", "en")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s or "kop"


def crumbs_for(path, title):
    if path == "":
        return ""
    parts = [p for p in path.strip("/").split("/") if p]
    items = ['<li><a href="/">Home</a></li>']
    acc = ""
    for i, p in enumerate(parts):
        acc += p + "/"
        last = i == len(parts) - 1
        label = PAGE_TITLES.get(acc, p.replace("-", " ").capitalize())
        if last:
            items.append("<li>%s</li>" % esc(title))
        else:
            items.append('<li><a href="/%s">%s</a></li>' % (acc, esc(label)))
    return ('<div class="crumbs"><div class="wrap"><nav aria-label="Kruimelpad">'
            "<ol>%s</ol></nav></div></div>" % "".join(items))


def page_html(page):
    path = page["path"]
    url = SITE + "/" + path
    title = page["title"]
    nav_items = []
    for label, href in NAV:
        cur = ""
        if href != "/" and path.startswith(href.strip("/") + "/"):
            cur = ' aria-current="page"'
        elif href.strip("/") == path.strip("/"):
            cur = ' aria-current="page"'
        nav_items.append('<li><a href="%s"%s>%s</a></li>' % (href, cur, esc(label)))

    fcols = []
    for head, links in FOOTER_COLS:
        li = "".join('<li><a href="%s">%s</a></li>' % (h, esc(t)) for t, h in links)
        fcols.append("<div><h4>%s</h4><ul>%s</ul></div>" % (esc(head), li))

    related = ""
    if page.get("related"):
        li = "".join('<li><a href="%s">%s</a></li>' % (h, esc(t))
                     for t, h in page["related"])
        related = ('<div class="related"><h2>Verder lezen</h2><ul>%s</ul></div>' % li)

    hero_cls = "hero"
    body = render_blocks(page["blocks"])
    needs_js = "vidbox" in body
    extra_js = page.get("js", "")

    meta_time = ""
    if page.get("date"):
        meta_time = ('<p class="meta">Gepubliceerd op %s</p>'
                     % nl_date(page["date"]))

    doc = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta property="og:type" content="%(ogtype)s">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<meta property="og:site_name" content="%(naam)s">
<meta property="og:locale" content="nl_NL">
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="Nieuws van %(naam)s" href="/rss.xml">
</head>
<body>
<a class="skip" href="#inhoud">Naar de inhoud</a>
<header class="top"><div class="wrap">
<a class="brand" href="/">
<span class="mark" aria-hidden="true"><span>1</span><span>2</span><span>3</span></span>
<span><b>Bedrijf Starten</b><small>Starten of overnemen</small></span>
</a>
<nav class="main" aria-label="Hoofdmenu"><ul>%(nav)s</ul></nav>
</div></header>
%(crumbs)s
<div class="%(herocls)s"><div class="wrap">
%(kicker)s<h1>%(h1)s</h1>
<p class="lead">%(lead)s</p>
</div></div>
<main id="inhoud"><div class="wrap"><article>
%(metatime)s
%(body)s
%(related)s
</article></div></main>
<footer><div class="wrap">
<div class="fgrid">%(fcols)s</div>
<div class="fbot">
<span>&copy; %(jaar)s %(naam)s</span>
<a href="/privacybeleid/">Privacybeleid</a>
<a href="/cookiebeleid/">Cookiebeleid</a>
<a href="/contact/">Contact</a>
<a href="/sitemap.xml">Sitemap</a>
<span>%(mail)s</span>
</div>
</div></footer>
%(js)s
</body>
</html>
""" % {
        "title": esc(title),
        "desc": esc(page["desc"]),
        "url": url,
        "ogtype": "article" if page.get("date") else "website",
        "naam": esc(NAAM),
        "nav": "".join(nav_items),
        "crumbs": crumbs_for(path, page.get("crumb", page["h1"])),
        "herocls": hero_cls,
        "kicker": '<p class="kicker">%s</p>' % esc(page["kicker"]) if page.get("kicker") else "",
        "h1": esc(page["h1"]),
        "lead": page["lead"],
        "metatime": meta_time,
        "body": body,
        "related": related,
        "fcols": "".join(fcols),
        "jaar": date.today().year,
        "mail": MAIL,
        "js": ("<script>%s</script>" % JS_VIDEO if needs_js else "")
              + (("<script>%s</script>" % extra_js) if extra_js else ""),
    }
    return doc


MAANDEN = ["januari", "februari", "maart", "april", "mei", "juni", "juli",
           "augustus", "september", "oktober", "november", "december"]


def nl_date(iso):
    y, m, d = [int(x) for x in iso.split("-")]
    return "%d %s %d" % (d, MAANDEN[m - 1], y)


def rfc822(iso):
    y, m, d = [int(x) for x in iso.split("-")]
    dt = date(y, m, d)
    dagen = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    mnd = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep",
           "Oct", "Nov", "Dec"]
    return "%s, %02d %s %d 08:00:00 +0200" % (dagen[dt.weekday()], d, mnd[m - 1], y)


PAGE_TITLES = {}

FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<rect width="64" height="64" rx="10" fill="#08403a"/>
<text x="32" y="42" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="26"
 font-weight="700" fill="#d9a441" text-anchor="middle">123</text></svg>
"""


def build():
    for p in PAGES:
        PAGE_TITLES[p["path"]] = p.get("crumb", p["h1"])

    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "assets"))

    with open(os.path.join(OUT, "assets", "site.css"), "w", encoding="utf-8") as f:
        f.write(CSS.strip() + "\n")
    with open(os.path.join(OUT, "assets", "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)

    for p in PAGES:
        path = p["path"]
        d = os.path.join(OUT, path)
        if path:
            os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page_html(p))

    # 404
    p404 = {
        "path": "", "title": "Pagina niet gevonden | " + NAAM,
        "desc": "Deze pagina bestaat niet of is verplaatst. Via het menu en de "
                "onderstaande ingangen zijn de gidsen, checklists en rekentools bereikbaar.",
        "h1": "Deze pagina bestaat niet",
        "kicker": "404",
        "lead": "Het adres klopt niet meer of er is een typefout gemaakt. "
                "Onderstaande ingangen leiden naar de rest van de site.",
        "blocks": [("cards", [
            ("Starten of overnemen", "De hoofdgids met de afweging tussen zelf beginnen "
             "en een bestaand bedrijf kopen.", "/starten-of-overnemen/"),
            ("Checklists", "Stap voor stap een bedrijf of webshop beginnen of overnemen.",
             "/checklists/"),
            ("Rekentools", "Een eerste indicatie van de waarde van een bedrijf of webshop.",
             "/tools/"),
            ("Kennisbank", "Begrippen en onderwerpen uit het overnameproces.",
             "/kennisbank/"),
        ])],
    }
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(page_html(p404))

    # sitemap
    today = date.today().isoformat()
    urls = []
    for p in PAGES:
        lastmod = p.get("date", today)
        urls.append("<url><loc>%s/%s</loc><lastmod>%s</lastmod></url>"
                    % (SITE, p["path"], lastmod))
    sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sm)

    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)

    # rss
    news = [p for p in PAGES if p.get("date")]
    news.sort(key=lambda x: x["date"], reverse=True)
    items = []
    for p in news:
        items.append(
            "<item><title>%s</title><link>%s/%s</link>"
            "<guid isPermaLink=\"true\">%s/%s</guid><pubDate>%s</pubDate>"
            "<description>%s</description></item>"
            % (esc(p["h1"]), SITE, p["path"], SITE, p["path"],
               rfc822(p["date"]), esc(p["desc"])))
    rss = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<rss version="2.0"><channel>\n'
           "<title>Nieuws van %s</title>\n<link>%s/nieuws/</link>\n"
           "<description>Actuele artikelen over bedrijven starten, overnemen en "
           "verkopen in Nederland.</description>\n<language>nl-nl</language>\n"
           % (NAAM, SITE) + "\n".join(items) + "\n</channel></rss>\n")
    with open(os.path.join(OUT, "rss.xml"), "w", encoding="utf-8") as f:
        f.write(rss)

    print("%d pagina's gebouwd in %s" % (len(PAGES) + 1, OUT))


if __name__ == "__main__":
    build()
