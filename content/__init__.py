"""Alle pagina's van 123bedrijfstarten.nl, in menuvolgorde."""

from . import core, starten, checklists, tools, verkopen, kennisbank, nieuws

PAGES = (
    core.PAGES[:1]              # home
    + starten.PAGES
    + checklists.PAGES
    + tools.PAGES
    + verkopen.PAGES
    + kennisbank.PAGES
    + nieuws.PAGES
    + core.PAGES[1:]            # over, platforms, video, contact, juridisch
)

NEWS_ORDER = nieuws.NEWS_ORDER

_paden = [p["path"] for p in PAGES]
assert len(_paden) == len(set(_paden)), "dubbele paden: %s" % [
    p for p in _paden if _paden.count(p) > 1]
