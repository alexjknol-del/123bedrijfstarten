# 123bedrijfstarten.nl

Statische site over het starten, overnemen en verkopen van bedrijven.

## Bouwen

```
python3 build.py     # bouwt dist/
python3 check.py     # controleert de gebouwde site
```

Geen dependencies, alleen de Python-standaardbibliotheek.

## Cloudflare Pages

- Framework preset: None
- Build command: leeg
- Output directory: `dist`
- Production branch: `main`

`dist/` is meegecommit, zodat Cloudflare niets hoeft te bouwen.

## Structuur

- `build.py` bevat de sjablonen, de CSS en de navigatie
- `content/` bevat de pagina's per rubriek
- `check.py` controleert interne links, dubbele titels, ankerteksten van
  uitgaande links, aanspreekvormen, em-dashes en de sitemap
