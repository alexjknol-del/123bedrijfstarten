"""Home, over, platforms, video, contact en juridische pagina's."""

from .common import (OA_MERK, OA_NAKED, OA_URL, WO_MERK, WO_NAKED, WO_URL,
                     oa, wo, YT_OA, YT_WO)
from .nieuws import ARTIKELEN, _nl

_laatste = ARTIKELEN[:3]
_nieuws_items = "".join(
    '<li><time datetime="%s">%s</time><a href="/%s">%s</a><p>%s</p></li>'
    % (p["date"], _nl(p["date"]), p["path"], p["h1"], p["desc"])
    for p in _laatste)

PLATFORM_BLOK = """
<div class="plat">
  <div class="box">
    <h3>OvernameAdvies.nl</h3>
    <p>Overnameplatform en adviesbureau voor het Nederlandse MKB. Gericht op
    bedrijven in alle branches, van installatietechniek en groothandel tot zorg,
    horeca en dienstverlening.</p>
    <ul>
      <li>aanbod van bedrijven te koop, per branche en regio</li>
      <li>waardebepaling en begeleiding van het verkoopproces</li>
      <li>actieve zoekopdracht voor kopers met een concreet zoekprofiel</li>
      <li>kennisbank en begrippenlijst over het overnameproces</li>
    </ul>
    <p class="url">%s<br>%s</p>
  </div>
  <div class="box">
    <h3>WebshopOvername.nl</h3>
    <p>Overnameplatform voor webshops, e-commercemerken, marketplace-accounts en
    online bedrijven. Gespecialiseerd in het segment waar de waarde in verkeer,
    merk en klantenbestand zit.</p>
    <ul>
      <li>aanbod van webshops en e-commercebedrijven te koop</li>
      <li>waardebepaling en scans op techniek, vindbaarheid en juridische punten</li>
      <li>begeleiding bij verkoop en bij aankoop</li>
      <li>kennisbank over waardering, platforms en overdracht</li>
    </ul>
    <p class="url">%s<br>%s</p>
  </div>
</div>
""" % (OA_MERK, oa("bedrijven-te-koop"), WO_MERK, wo("bedrijven-te-koop"))


PAGES = [

# ------------------------------------------------------------------ home
{
 "path": "",
 "crumb": "Home",
 "title": "123 Bedrijf Starten: gids over starten en bedrijfsovername",
 "desc": "Onafhankelijke gids over een bedrijf beginnen of een bestaande "
         "onderneming overnemen. Met checklists, twee rekentools voor "
         "waardebepaling, een kennisbank en actueel nieuws.",
 "kicker": "Starten of overnemen",
 "h1": "Een bedrijf beginnen, of er een overnemen",
 "lead": "Er zijn twee manieren om ondernemer te worden. De ene krijgt alle "
         "aandacht, de andere levert vaker een bedrijf op dat na vijf jaar nog "
         "bestaat. Deze site legt beide routes uit, met de cijfers erbij.",
 "blocks": [
  ("h2", "Waar te beginnen"),
  ("cards", [
   ("Starten of overnemen",
    "De hoofdgids: cijfers, kosten, financiering en de vraag welke route bij welke "
    "ondernemer past.",
    "/starten-of-overnemen/"),
   ("Checklists",
    "Vier lijsten die stap voor stap door de uitvoering lopen, voor een bedrijf en "
    "voor een webshop.",
    "/checklists/"),
   ("Rekentools",
    "Wat is een bedrijf waard en wat is een webshop waard. Twee rekenmodellen die "
    "in de browser draaien.",
    "/tools/"),
   ("Bedrijf verkopen",
    "Wanneer verkopen, hoe de opbrengst hoger wordt en hoe het proces in vijf "
    "stappen verloopt.",
    "/verkopen/"),
  ]),

  ("h2", "Waarom overnemen vaker slaagt"),
  ("p", "Uit de Eurobarometer-enquete blijkt dat 65 procent van de ondervraagden "
        "liever zelf een bedrijf begint en 35 procent liever een bestaand bedrijf "
        "overneemt. De uitkomsten wijzen precies de andere kant op. Oostenrijks "
        "onderzoek komt uit op 96 procent van de overgenomen bedrijven die na vijf "
        "jaar nog operationeel is, tegenover 75 procent van de startups. Nederlands "
        "onderzoek van lector Lex van Teeffelen komt op ruim 90 procent tegenover "
        "ongeveer de helft."),
  ("p", "De Europese Commissie telde daarnaast ongeveer 610.000 overnames per jaar "
        "van kleine bedrijven in Europa, en stelde vast dat een geslaagde overname "
        "gemiddeld vijf banen oplevert, tegenover twee bij een startup. De volledige "
        "onderbouwing staat op "
        "<a href=\"/starten-of-overnemen/cijfers-en-onderzoek/\">cijfers en "
        "onderzoek</a>."),

  ("h2", "Twee platformen die dit segment bedienen"),
  ("p", "Wie een bedrijf wil kopen of verkopen, komt in Nederland een beperkt "
        "aantal partijen tegen die zich op het MKB richten. Twee daarvan worden op "
        "deze site aanbevolen, omdat ze samen het volledige terrein afdekken: "
        "bedrijven in het algemeen en webshops en online bedrijven in het "
        "bijzonder."),
  ("raw", PLATFORM_BLOK),
  ("p", "Een uitgebreidere beschrijving van beide platformen, met de onderdelen "
        "waar ze zich in onderscheiden, staat op "
        "<a href=\"/platforms/\">uitgelichte platforms</a>."),

  ("h2", "Rekenen aan een bedrijf"),
  ("p", "De twee rekentools geven een eerste indicatie van de waarde, op basis van "
        "gepubliceerde sectorcijfers. Er wordt niets verstuurd en niets opgeslagen: "
        "de berekening gebeurt in de browser."),
  ("cards", [
   ("Wat is mijn bedrijf waard",
    "Genormaliseerde EBITDA, sector, groei en risicofactoren, met een indicatieve "
    "bandbreedte als uitkomst.",
    "/tools/wat-is-mijn-bedrijf-waard/"),
   ("Wat is mijn webshop waard",
    "Gecorrigeerde winst, eigen uren, verkeersmix en afhankelijkheden, toegepast op "
    "webshops en e-commercebedrijven.",
    "/tools/wat-is-mijn-webshop-waard/"),
  ]),

  ("h2", "Laatste nieuws"),
  ("raw", '<ul class="list">%s</ul>' % _nieuws_items),
  ("p", 'Het volledige overzicht staat op <a href="/nieuws/">nieuws</a>.'),

  ("h2", "Video"),
  ("p", "Twee kanalen met uitleg over waardering, verkoopproces en de overdracht "
        "zelf. De uitgelichte video's staan gebundeld op "
        "<a href=\"/video/\">video</a>."),
  ("video", YT_OA, "Video's van het kanaal Overnameadvies",
   "Uitleg over bedrijfsverkoop, waardering en het overnameproces."),
 ],
 "related": [
  ("Waarom overnemen", "/starten-of-overnemen/waarom-overnemen/"),
  ("Checklist bedrijf beginnen", "/checklists/bedrijf-beginnen/"),
  ("Kennisbank", "/kennisbank/"),
  ("Over dit platform", "/over/"),
 ],
},

# ------------------------------------------------------------------ over
{
 "path": "over/",
 "crumb": "Over",
 "title": "Over 123 Bedrijf Starten: wat deze gids is en doet",
 "desc": "123 Bedrijf Starten is een redactioneel platform over het starten, "
         "overnemen en verkopen van bedrijven in Nederland. Uitleg over de opzet, "
         "de bronnen en de manier van werken.",
 "kicker": "Over",
 "h1": "Over dit platform",
 "lead": "123 Bedrijf Starten is een gids over de twee manieren om ondernemer te "
         "worden, en over de derde stap die daar altijd op volgt: het bedrijf ooit "
         "weer overdragen.",
 "blocks": [
  ("h2", "Waarom deze site bestaat"),
  ("p", "Over het starten van een bedrijf is veel geschreven. Over het overnemen "
        "van een bestaand bedrijf aanzienlijk minder, terwijl overnames van kleine "
        "ondernemingen de meerderheid van alle transacties vormen en betere "
        "overlevingscijfers laten zien. Deze site brengt beide routes bij elkaar en "
        "behandelt ze met dezelfde diepgang."),
  ("p", "Daar komt een derde onderwerp bij dat in de praktijk te laat aan bod komt: "
        "de verkoop. De keuzes die een bedrijf later verkoopbaar maken, worden in "
        "de eerste jaren gemaakt. Die samenhang is de rode draad van de site."),

  ("h2", "Wat er te vinden is"),
  ("table",
   ["Onderdeel", "Inhoud"],
   [
    ["Starten of overnemen", "De hoofdgids: cijfers, kosten, financiering en de "
     "afweging tussen beide routes"],
    ["Checklists", "Vier uitgewerkte lijsten voor het beginnen en overnemen van "
     "een bedrijf of webshop"],
    ["Rekentools", "Twee rekenmodellen voor een indicatie van de waarde van een "
     "bedrijf of webshop"],
    ["Verkopen", "Timing, opbrengst, verkoopklaar ondernemen en het proces in vijf "
     "stappen"],
    ["Kennisbank", "Begrippen en onderwerpen uit het overnameproces, plus een "
     "begrippenlijst"],
    ["Nieuws", "Artikelen over de overnamemarkt, waarderingen, financiering en "
     "regelgeving"],
   ]),

  ("h2", "Hoe de teksten tot stand komen"),
  ("p", "Bij elk cijfer staat de bron en het jaar waarop het betrekking heeft. De "
        "gebruikte bronnen zijn onder meer onderzoek van de Europese Commissie, "
        "cijfers van KVK, de Overname Barometer van Brookz en Dealsuite, onderzoek "
        "van Ipsos I&O in opdracht van ABN AMRO, de Thuiswinkel Markt Monitor en "
        "het onderzoek van lector Lex van Teeffelen naar bedrijfsoverdrachten in "
        "het Nederlandse MKB."),
  ("p", "Onderzoek veroudert. Een cijfer uit een onderzoek over 2025 blijft een "
        "cijfer over 2025, ook als het hier in 2026 wordt aangehaald. Daarom staat "
        "de periode er steeds bij."),

  ("h2", "Onafhankelijkheid en beperkingen"),
  ("p", "Deze site geeft algemene informatie en is geen adviesbureau. Er wordt geen "
        "bemiddeling verzorgd, geen waardering afgegeven en geen fiscaal of "
        "juridisch advies gegeven. Voor een concrete situatie zijn een accountant, "
        "een fiscalist of een overnameadviseur nodig."),
  ("p", "Op verschillende plaatsen wordt verwezen naar twee platformen die zich op "
        "dit segment richten: %s voor bedrijven in het algemeen en %s voor webshops "
        "en online bedrijven. Die verwijzingen staan er omdat ze bij het onderwerp "
        "horen, en zijn te herkennen: uitgaande links openen in een nieuw tabblad "
        "en gebruiken de merknaam of de volledige URL als linktekst."
        % (OA_MERK, WO_MERK)),

  ("h2", "Techniek en privacy"),
  ("p", "De site bestaat uit statische pagina's zonder trackingsoftware, zonder "
        "advertentienetwerken en zonder analytics. De rekentools werken volledig in "
        "de browser: er wordt niets verstuurd en niets opgeslagen. Video's laden "
        "pas na een klik, via youtube-nocookie.com. Meer daarover staat in het "
        "<a href=\"/cookiebeleid/\">cookiebeleid</a> en het "
        "<a href=\"/privacybeleid/\">privacybeleid</a>."),

  ("h2", "Reageren"),
  ("p", "Correcties, aanvullingen en vragen zijn welkom via de "
        "<a href=\"/contact/\">contactpagina</a>. Feitelijke onjuistheden worden "
        "gecorrigeerd, met vermelding van de wijziging als die inhoudelijk is."),
 ],
 "related": [
  ("Uitgelichte platforms", "/platforms/"),
  ("Contact", "/contact/"),
  ("Cijfers en onderzoek", "/starten-of-overnemen/cijfers-en-onderzoek/"),
 ],
},

# ------------------------------------------------------------------ platforms
{
 "path": "platforms/",
 "crumb": "Uitgelichte platforms",
 "title": "Uitgelichte platforms voor bedrijfsovername en webshopovername",
 "desc": "Twee Nederlandse overnameplatformen uitgelicht: OvernameAdvies.nl voor "
         "bedrijven in het MKB en WebshopOvername.nl voor webshops, "
         "e-commercemerken en marketplace-accounts.",
 "kicker": "Aanbevolen",
 "h1": "Uitgelichte platforms",
 "lead": "Twee platformen die het Nederlandse MKB-segment bedienen, elk met een "
         "eigen specialisme. Samen dekken ze het hele terrein van deze site.",
 "blocks": [
  ("h2", "OvernameAdvies.nl"),
  ("p", "%s richt zich op bedrijfsverkoop en bedrijfsovername in het MKB, in alle "
        "branches. Het platform combineert een marktplaats met begeleiding: van "
        "waardebepaling en verkoopmemorandum tot onderhandeling en overdracht."
        % OA_MERK),
  ("table",
   ["Onderdeel", "Waar te vinden"],
   [
    ["Bedrijven te koop", oa("bedrijven-te-koop")],
    ["Waardebepaling", oa("bedrijf-waarderen")],
    ["Hoe het werkt", oa("hoe-werkt-het")],
    ["Bedrijf verkopen", oa("bedrijf-verkopen")],
    ["Zoekopdracht voor kopers", oa("zoekopdracht-bedrijf-aankopen")],
    ["Kennisbank", oa("kennisbank")],
    ["Begrippenlijst", oa("begrippenlijst")],
    ["Stappenplan", oa("stappenplan")],
   ]),
  ("p", "Voor wie een bedrijf zoekt buiten het bestaande aanbod, biedt het platform "
        "een actieve zoekopdracht: gericht benaderen van ondernemingen die niet te "
        "koop staan. De hoofdpagina staat op %s." % OA_URL),

  ("video", YT_OA, "Video's van het kanaal Overnameadvies",
   "Uitleg over waardering, het verkoopproces en de rol van de overnameadviseur."),

  ("h2", "WebshopOvername.nl"),
  ("p", "%s is gespecialiseerd in webshops, e-commercemerken, marketplace-accounts "
        "en online bedrijven. Dat segment vraagt om ander onderzoek dan een "
        "gewone bedrijfsovername: de waarde zit in verkeer, merk, klantenbestand en "
        "techniek, en die posten vragen om eigen controles."
        % WO_MERK),
  ("table",
   ["Onderdeel", "Waar te vinden"],
   [
    ["Webshops te koop", wo("aanbod/Webshops%20te%20koop")],
    ["Startups en kleinere shops", wo("aanbod/startups")],
    ["Waardebepaling", wo("overnameadvies/waardebepaling")],
    ["Bedrijfsscans op techniek en vindbaarheid", wo("overnameadvies/bedrijfsscans")],
    ["Webshop verkopen", wo("onze-diensten/webshop-verkopen")],
    ["Webshop kopen", wo("onze-diensten/webshop-kopen")],
    ["Kennisbank", wo("kennisbank")],
    ["Handboek webshopovername", wo("handboek")],
   ]),
  ("p", "De hoofdpagina staat op %s." % WO_URL),

  ("video", YT_WO, "Video's van het kanaal WebshopOvername.nl",
   "Uitleg over het kopen en verkopen van webshops en e-commercebedrijven."),

  ("h2", "Welk platform bij welke vraag"),
  ("table",
   ["Situatie", "Meest voor de hand liggend"],
   [
    ["Een installatiebedrijf, groothandel, praktijk of dienstverlener kopen of "
     "verkopen", OA_NAKED],
    ["Een webshop, e-commercemerk of marketplace-account kopen of verkopen",
     WO_NAKED],
    ["Een bedrijf met zowel een fysieke als een online tak",
     "Beide, afhankelijk van waar het zwaartepunt in de omzet ligt"],
    ["Een waardebepaling als eerste stap", "Beide bieden dit aan voor het eigen "
     "segment"],
   ]),

  ("h2", "Waarom deze twee"),
  ("p", "Beide platformen bedienen het MKB-segment waar deze site over gaat: "
        "bedrijven die te klein zijn voor de grote fusie- en overnamepraktijk en te "
        "groot om zonder begeleiding over te dragen. Ze publiceren daarnaast "
        "openbare kennisbanken, wat het mogelijk maakt om naar concrete uitleg te "
        "verwijzen in plaats van naar een contactformulier."),
  ("p", "Deze site is redactioneel en geen onderdeel van een van beide platformen. "
        "Meer daarover staat op <a href=\"/over/\">over dit platform</a>."),
 ],
 "related": [
  ("Over dit platform", "/over/"),
  ("Video", "/video/"),
  ("Kennisbank", "/kennisbank/"),
 ],
},

# ------------------------------------------------------------------ video
{
 "path": "video/",
 "crumb": "Video",
 "title": "Video over bedrijfsovername en webshopovername",
 "desc": "Uitgelichte video's van de kanalen Overnameadvies en WebshopOvername.nl "
         "over waardering, het verkoopproces, financiering en de overdracht.",
 "kicker": "Video",
 "h1": "Video",
 "lead": "Twee kanalen die het overnameproces in beeld uitleggen. De video's laden "
         "pas na een klik, via youtube-nocookie.com, zodat er zonder die klik geen "
         "verbinding met YouTube wordt gemaakt.",
 "blocks": [
  ("h2", "Overnameadvies"),
  ("p", "Het kanaal van %s behandelt bedrijfsverkoop in het MKB: waardering, het "
        "verkoopproces, de rol van de adviseur en de onderwerpen die tijdens een "
        "traject langskomen." % OA_MERK),
  ("video", YT_OA, "Video's van het kanaal Overnameadvies",
   "De uploadlijst van het kanaal Overnameadvies. De speler doorloopt de video's "
   "in volgorde van publicatie."),

  ("h2", "WebshopOvername.nl"),
  ("p", "Het kanaal van %s richt zich op webshops en online bedrijven: waardering "
        "van e-commerce, het verkoopproces en waar kopers bij een webshop op "
        "letten." % WO_MERK),
  ("video", YT_WO, "Video's van het kanaal WebshopOvername.nl",
   "De uploadlijst van het kanaal WebshopOvername.nl."),

  ("h2", "Bij welk onderwerp welke uitleg"),
  ("table",
   ["Vraag", "Waar op deze site"],
   [
    ["Wat is een bedrijf waard", "<a href=\"/kennisbank/waardebepaling/\">"
     "waardebepaling</a> en de <a href=\"/tools/wat-is-mijn-bedrijf-waard/\">"
     "rekentool</a>"],
    ["Hoe loopt een verkooptraject", "<a href=\"/verkopen/vijf-stappen/\">"
     "het proces in vijf stappen</a>"],
    ["Wat onderzoekt een koper", "<a href=\"/kennisbank/due-diligence/\">"
     "due diligence</a>"],
    ["Hoe wordt een overname betaald", "<a href=\"/kennisbank/financiering/\">"
     "financiering</a>"],
    ["Waar staat het aanbod", "<a href=\"/platforms/\">uitgelichte platforms</a>"],
   ]),
 ],
 "related": [
  ("Uitgelichte platforms", "/platforms/"),
  ("Kennisbank", "/kennisbank/"),
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
 ],
},

# ------------------------------------------------------------------ contact
{
 "path": "contact/",
 "crumb": "Contact",
 "title": "Contact met de redactie van 123 Bedrijf Starten",
 "desc": "Vragen, correcties of aanvullingen over de inhoud van 123 Bedrijf "
         "Starten kunnen per e-mail naar de redactie.",
 "kicker": "Contact",
 "h1": "Contact",
 "lead": "Vragen over de inhoud, correcties en aanvullingen zijn welkom per "
         "e-mail.",
 "blocks": [
  ("panel", "E-mail", [
   ("p", 'Berichten kunnen naar '
         '<a href="mailto:info@123bedrijfstarten.nl">info@123bedrijfstarten.nl</a>.'),
   ("p", "Er staat bewust geen contactformulier op deze site. Een e-mail komt "
         "direct aan, laat een spoor achter aan beide kanten en vraagt geen "
         "opslag van gegevens op deze website."),
  ]),

  ("h2", "Waar de redactie op reageert"),
  ("tick", [
    "feitelijke onjuistheden in cijfers, jaartallen of bronvermelding",
    "verouderde informatie, bijvoorbeeld na een wetswijziging",
    "kapotte links of pagina's die niet goed werken",
    "suggesties voor onderwerpen die ontbreken",
  ]),

  ("h2", "Waar de redactie niet op ingaat"),
  ("p", "Deze site geeft algemene informatie en geen advies over een concrete "
        "situatie. Vragen over de waarde van een specifiek bedrijf, over de "
        "fiscale gevolgen van een overdracht of over een lopend traject horen thuis "
        "bij een accountant, een fiscalist of een overnameadviseur."),
  ("p", "Voor een waardebepaling of begeleiding bij verkoop of aankoop staan de "
        "ingangen op <a href=\"/platforms/\">uitgelichte platforms</a>: %s voor "
        "bedrijven in het algemeen, %s voor webshops en online bedrijven."
        % (OA_NAKED, WO_NAKED)),

  ("h2", "Aanbiedingen"),
  ("p", "Ongevraagde aanbiedingen voor linkplaatsingen, gesponsorde artikelen of "
        "advertenties worden niet in behandeling genomen."),
 ],
 "related": [
  ("Over dit platform", "/over/"),
  ("Privacybeleid", "/privacybeleid/"),
  ("Cookiebeleid", "/cookiebeleid/"),
 ],
},

# ------------------------------------------------------------------ privacy
{
 "path": "privacybeleid/",
 "crumb": "Privacybeleid",
 "title": "Privacybeleid van 123 Bedrijf Starten",
 "desc": "Welke gegevens deze website verwerkt, wat er met een e-mail gebeurt en "
         "welke rechten bezoekers hebben op grond van de AVG.",
 "kicker": "Juridisch",
 "h1": "Privacybeleid",
 "lead": "Deze website verzamelt geen persoonsgegevens van bezoekers. Hieronder "
         "staat wat er wel gebeurt.",
 "blocks": [
  ("h2", "Welke gegevens worden verwerkt"),
  ("p", "De site bestaat uit statische pagina's. Er staat geen contactformulier op, "
        "er is geen inlog, er worden geen accounts aangemaakt en er wordt geen "
        "nieuwsbrief verstuurd. Er is geen analytics- of trackingsoftware "
        "geïnstalleerd en er zijn geen advertentienetwerken actief."),
  ("h3", "Serverlogs"),
  ("p", "De hostingpartij legt voor de werking en beveiliging van de dienst "
        "technische gegevens vast, zoals het IP-adres, het opgevraagde adres, het "
        "tijdstip en het type browser. Die gegevens worden niet gebruikt om "
        "bezoekers te volgen of te profileren."),
  ("h3", "E-mail"),
  ("p", "Wie een bericht stuurt naar info@123bedrijfstarten.nl, deelt daarmee een "
        "e-mailadres en de inhoud van het bericht. Die gegevens worden alleen "
        "gebruikt om het bericht te beantwoorden en worden niet gedeeld met "
        "anderen. Berichten worden bewaard zolang dat voor de afhandeling nodig is."),

  ("h2", "Rekentools"),
  ("p", "De rekentools op deze site werken volledig in de browser van de bezoeker. "
        "De ingevulde bedragen worden niet verstuurd, niet opgeslagen en niet "
        "gedeeld. Zodra de pagina wordt gesloten, zijn de ingevoerde gegevens weg."),

  ("h2", "Video van derden"),
  ("p", "Op enkele pagina's staan video's van YouTube. Die worden pas geladen nadat "
        "de bezoeker op de afspeelknop klikt. Tot dat moment wordt er geen "
        "verbinding met YouTube gemaakt. Na het klikken laadt de video via "
        "youtube-nocookie.com, een variant waarbij Google minder gegevens "
        "vastlegt. Vanaf dat moment gelden ook de voorwaarden en het privacybeleid "
        "van Google."),

  ("h2", "Links naar andere websites"),
  ("p", "Deze site verwijst naar externe websites. Voor de verwerking van "
        "persoonsgegevens op die websites gelden hun eigen voorwaarden. Deze site "
        "heeft daar geen invloed op en draagt daarvoor geen verantwoordelijkheid."),

  ("h2", "Rechten"),
  ("p", "Op grond van de Algemene verordening gegevensbescherming bestaat het recht "
        "op inzage, correctie en verwijdering van persoonsgegevens, en het recht om "
        "bezwaar te maken tegen verwerking. Omdat deze site nauwelijks gegevens "
        "verwerkt, gaat dat in de praktijk om e-mailcorrespondentie. Verzoeken "
        "kunnen naar info@123bedrijfstarten.nl."),
  ("p", "Er bestaat daarnaast het recht om een klacht in te dienen bij de Autoriteit "
        "Persoonsgegevens."),

  ("h2", "Wijzigingen"),
  ("p", "Dit privacybeleid wordt aangepast wanneer de opzet van de site verandert. "
        "De actuele versie staat altijd op deze pagina."),
 ],
 "related": [
  ("Cookiebeleid", "/cookiebeleid/"),
  ("Contact", "/contact/"),
  ("Over dit platform", "/over/"),
 ],
},

# ------------------------------------------------------------------ cookies
{
 "path": "cookiebeleid/",
 "crumb": "Cookiebeleid",
 "title": "Cookiebeleid van 123 Bedrijf Starten",
 "desc": "Deze website plaatst geen cookies. Uitleg over wat er wel gebeurt bij "
         "het afspelen van een video en waarom er geen cookiemelding staat.",
 "kicker": "Juridisch",
 "h1": "Cookiebeleid",
 "lead": "Deze website plaatst zelf geen cookies, ook geen functionele. Er is "
         "daarom geen cookiemelding.",
 "blocks": [
  ("h2", "Wat er niet gebeurt"),
  ("tick", [
    "geen analytics, statistieken of bezoekersmetingen",
    "geen advertentie- of retargetingcookies",
    "geen sociale-mediaknoppen die gegevens doorgeven",
    "geen ingesloten lettertypen of scripts van externe partijen",
    "geen opslag van ingevulde gegevens uit de rekentools",
  ]),
  ("p", "De pagina's laden daardoor zonder enig verzoek naar een andere website. De "
        "rekentools rekenen in de browser zelf."),

  ("h2", "Wat er gebeurt bij een video"),
  ("p", "Op een paar pagina's staan video's. Die worden niet vooraf geladen: er "
        "staat een afbeelding met een afspeelknop, en pas na een klik daarop wordt "
        "de speler geladen via youtube-nocookie.com."),
  ("p", "Vanaf dat moment kan YouTube gegevens vastleggen die nodig zijn om de "
        "video af te spelen, en gelden de voorwaarden van Google. Wie dat niet "
        "wil, hoeft alleen niet op de afspeelknop te klikken. De rest van de "
        "pagina werkt gewoon."),

  ("h2", "Cookies weigeren of verwijderen"),
  ("p", "Omdat deze site geen cookies plaatst, valt er niets te weigeren. Cookies "
        "die na het afspelen van een video door YouTube zijn geplaatst, zijn te "
        "verwijderen via de instellingen van de browser. Elke browser heeft daar "
        "een eigen menu voor, meestal onder privacy of website-instellingen."),

  ("h2", "Wijzigingen"),
  ("p", "Als er in de toekomst wel cookies gebruikt worden, wordt deze pagina "
        "aangepast en komt er een melding met een keuzemogelijkheid, voordat er "
        "iets geplaatst wordt."),
  ("p", "Wat er met persoonsgegevens gebeurt staat in het "
        "<a href=\"/privacybeleid/\">privacybeleid</a>."),
 ],
 "related": [
  ("Privacybeleid", "/privacybeleid/"),
  ("Contact", "/contact/"),
 ],
},
]
