"""Gedeelde helpers voor de contentmodules."""

import html


def esc(t):
    return html.escape(t, quote=False)


def ext(url, text=None):
    """Externe link. Ankertekst is altijd merknaam of URL."""
    return ('<a href="%s" target="_blank" rel="nofollow noopener">%s</a>'
            % (url, esc(text or url)))


def a(href, text):
    return '<a href="%s">%s</a>' % (href, esc(text))


# vaste ankerteksten
OA = "https://www.overnameadvies.nl/"
WO = "https://www.webshopovername.nl/"

OA_MERK = ext(OA, "OvernameAdvies.nl")
OA_NAKED = ext(OA, "www.overnameadvies.nl")
OA_URL = ext(OA, "https://www.overnameadvies.nl/")
WO_MERK = ext(WO, "WebshopOvername.nl")
WO_NAKED = ext(WO, "www.webshopovername.nl")
WO_URL = ext(WO, "https://www.webshopovername.nl/")


def oa(pad):
    """Deeplink naar overnameadvies.nl met de volledige URL als ankertekst."""
    url = OA + pad.lstrip("/")
    return ext(url, url)


def wo(pad):
    url = WO + pad.lstrip("/")
    return ext(url, url)


# geverifieerde uploadlijsten van de twee YouTube-kanalen
YT_OA = "UUTzxlRd3FCenSuvfT3UOODA"
YT_WO = "UUnOhIOkTf9dhOVrcthv4x1A"
