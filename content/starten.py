"""Gids: zelf beginnen of een bestaand bedrijf overnemen."""

from .common import OA_MERK, OA_NAKED, WO_MERK, WO_NAKED, oa, wo, YT_OA

PAGES = [

# ------------------------------------------------------------------ hub
{
 "path": "starten-of-overnemen/",
 "crumb": "Starten of overnemen",
 "title": "Bedrijf starten of overnemen: de complete afweging",
 "desc": "Zelf een bedrijf beginnen of een bestaande onderneming kopen. Deze gids "
         "zet cijfers, kosten, risico en financiering naast elkaar per route.",
 "kicker": "Hoofdgids",
 "h1": "Bedrijf starten of overnemen",
 "lead": "Wie ondernemer wil worden heeft twee routes: iets nieuws opbouwen of "
         "iets bestaands kopen. De eerste route krijgt de meeste aandacht, de "
         "tweede levert statistisch gezien vaker een bedrijf op dat na vijf jaar "
         "nog bestaat. Deze gids zet beide routes naast elkaar.",
 "blocks": [
  ("p", "Startups domineren al tien jaar het ondernemersverhaal in Nederland. "
        "Overnames van kleine en middelgrote bedrijven vormen intussen de stille "
        "meerderheid van alle transacties, en die route blijft in de beeldvorming "
        "onderbelicht. Dat is opmerkelijk, want de overlevingscijfers wijzen "
        "consequent de andere kant op."),
  ("p", "Deze gids behandelt de afweging in vier delen: het onderzoek achter de "
        "overlevingscijfers, de kosten van beide routes, de financiering en het "
        "risico, en de vraag welke route bij welk type ondernemer past."),

  ("cards", [
    ("Waarom overnemen",
     "De argumenten voor de overnameroute, en de situaties waarin zelf beginnen "
     "juist logischer is.",
     "/starten-of-overnemen/waarom-overnemen/"),
    ("Cijfers en onderzoek",
     "Eurobarometer, Oostenrijks onderzoek en de Nederlandse cijfers van lector "
     "Lex van Teeffelen.",
     "/starten-of-overnemen/cijfers-en-onderzoek/"),
    ("Kosten vergelijken",
     "Wat een start kost tegenover wat een overname kost, en waar het verschil "
     "in werkelijkheid zit.",
     "/starten-of-overnemen/kosten-vergelijken/"),
    ("Financiering en risico",
     "Bankfinanciering, vendor loan, earn-out en de risico's die bij elke route "
     "horen.",
     "/starten-of-overnemen/financiering-en-risico/"),
  ]),

  ("h2", "De twee routes in het kort"),
  ("table",
   ["", "Zelf beginnen", "Overnemen"],
   [
    ["Omzet op dag een", "Nul", "Bestaande omzet en klanten"],
    ["Investering vooraf", "Vaak laag tot gemiddeld", "Hoger, koopsom plus werkkapitaal"],
    ["Financierbaarheid", "Lastig, geen historie", "Beter, cijfers over meerdere jaren"],
    ["Vrijheid in de opzet", "Volledig", "Beperkt door wat er staat"],
    ["Tijd tot inkomen", "Maanden tot jaren", "Direct, mits de overdracht goed loopt"],
    ["Grootste risico", "Geen markt vinden", "Te veel betalen of verborgen gebreken"],
   ]),

  ("h2", "Voor wie welke route"),
  ("p", "Er bestaat geen route die voor iedereen beter uitpakt. De keuze hangt "
        "samen met het type idee, de beschikbare middelen en de ervaring van de "
        "ondernemer."),
  ("h3", "Zelf beginnen ligt voor de hand bij"),
  ("tick", [
    "een product of dienst die nog niet bestaat, of een duidelijk nieuwe aanpak",
    "een markt die zo snel verandert dat bestaande bedrijven eerder ballast dan "
    "voorsprong zijn",
    "beperkt startkapitaal in combinatie met een model dat klein kan beginnen",
    "de wens om zelf alles te bepalen, van merknaam tot personeelsbestand",
  ]),
  ("h3", "Overnemen ligt voor de hand bij"),
  ("tick", [
    "een bewezen markt waar het vooral om uitvoering en schaal gaat",
    "de behoefte aan inkomen vanaf het eerste jaar",
    "beschikbare financiering of een verkoper die bereid is mee te financieren",
    "een sector waarin vergunningen, certificaten of een klantenbestand jaren "
    "kosten om op te bouwen",
  ]),

  ("h2", "De vergrijzing maakt overnemen makkelijker"),
  ("p", "Uit onderzoek van Ipsos I&O in opdracht van ABN AMRO, gepubliceerd in "
        "februari 2026, blijkt dat ruim twee derde van de Nederlandse ondernemers "
        "binnen tien jaar wil stoppen. Van de ondervraagden had 22 procent geen "
        "concrete opvolgingsplannen en zocht 20 procent al naar een opvolger "
        "zonder er een gevonden te hebben. Bijna 13 procent van de ondernemers is "
        "65 jaar of ouder, tegen 7 procent in 2010."),
  ("p", "Voor kopers betekent dat een ruime markt. Voor verkopers betekent het "
        "concurrentie: hoe meer bedrijven tegelijk te koop komen, hoe belangrijker "
        "de voorbereiding wordt. Die kant van het verhaal staat in de gids "
        "<a href=\"/verkopen/\">bedrijf verkopen</a>."),

  ("h2", "Waar bedrijven te koop staan"),
  ("p", "Het Nederlandse aanbod van bedrijven en webshops staat verspreid over "
        "een handvol platformen. Twee daarvan komen op deze site regelmatig terug, "
        "omdat ze het MKB-segment bedienen waar deze gids over gaat: %s voor "
        "bedrijven in het algemeen en %s voor webshops, e-commercemerken en "
        "marketplace-accounts."
        % (OA_MERK, WO_MERK)),
  ("p", "Het volledige aanbod van beide platformen staat op %s en %s."
        % (oa("bedrijven-te-koop"), wo("bedrijven-te-koop"))),

  ("video", YT_OA, "Video's van het kanaal Overnameadvies",
   "De uploadlijst van het YouTube-kanaal Overnameadvies, met uitleg over "
   "waardering, het verkoopproces en de rol van de adviseur."),

  ("h2", "Volgorde van deze gids"),
  ("steps", [
   ("Bepaal de route",
    "Lees de argumenten en de cijfers, en bepaal of starten of overnemen past bij "
    "het idee en de middelen die er zijn."),
   ("Reken de kosten door",
    "Zet de kosten van beide routes naast elkaar, inclusief werkkapitaal en de "
    "maanden zonder inkomen."),
   ("Toets de financiering",
    "Een bank kijkt bij een overname naar historische cijfers, bij een start naar "
    "een plan. Dat verschil bepaalt vaak de uitkomst."),
   ("Werk de checklist af",
    "De checklists voor <a href=\"/checklists/bedrijf-beginnen/\">bedrijf "
    "beginnen</a>, <a href=\"/checklists/webshop-beginnen/\">webshop beginnen</a>, "
    "<a href=\"/checklists/bedrijf-overnemen/\">bedrijf overnemen</a> en "
    "<a href=\"/checklists/webshop-overnemen/\">webshop overnemen</a> lopen stap "
    "voor stap door de uitvoering."),
  ]),
 ],
 "related": [
  ("Checklist bedrijf beginnen", "/checklists/bedrijf-beginnen/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Kennisbank", "/kennisbank/"),
 ],
},

# ------------------------------------------------------------ waarom overnemen
{
 "path": "starten-of-overnemen/waarom-overnemen/",
 "crumb": "Waarom overnemen",
 "title": "Waarom overnemen vaker slaagt dan zelf beginnen",
 "desc": "Overgenomen bedrijven halen hogere overlevingspercentages dan startups "
         "en leveren gemiddeld meer banen op. De argumenten en de keerzijde.",
 "kicker": "Deel 1",
 "h1": "Waarom overnemen",
 "lead": "Al jaren gaat vrijwel alle aandacht naar startups. De cijfers laten "
         "zien dat de andere manier van starten, via een overname, vaker tot een "
         "bedrijf leidt dat na vijf jaar nog draait.",
 "blocks": [
  ("h2", "De kern van het argument"),
  ("p", "Een startende ondernemer moet vier dingen tegelijk bewijzen: dat er vraag "
        "is, dat het product klopt, dat de kosten kloppen en dat er iemand wil "
        "betalen. Een koper van een bestaand bedrijf neemt die vier antwoorden over "
        "en houdt een andere vraag over: valt dit bedrijf beter te laten draaien "
        "dan nu het geval is."),
  ("p", "Dat verschil verklaart een groot deel van de kloof in overlevingskansen. "
        "Het bedrijf heeft klanten, leveranciers, personeel, vergunningen en een "
        "boekhouding met historie. Wat er misgaat bij een overname zit zelden in de "
        "vraag of de markt bestaat, en vaker in de prijs, de financiering of de "
        "overdracht zelf."),

  ("quote", [
   ("p", "De Eurobarometer-enquete laat zien dat 65 procent van de ondervraagden "
         "de voorkeur geeft aan zelf beginnen en 35 procent aan overnemen. "
         "Uitgerekend die kleinste groep haalt de hoogste overlevingscijfers."),
  ]),

  ("h2", "Vijf voordelen van de overnameroute"),
  ("steps", [
   ("Omzet vanaf dag een",
    "Het bedrijf draait al. Er is kasstroom om salaris, financiering en "
    "leveranciers uit te betalen, in plaats van een aanloopperiode die uit eigen "
    "middelen betaald moet worden."),
   ("Een bewezen model",
    "Prijzen, marges en inkoop zijn getest in de praktijk. Dat maakt een prognose "
    "beter onderbouwd dan een prognose die op aannames rust."),
   ("Betere financierbaarheid",
    "Banken en financiers beoordelen een overname aan de hand van jaarcijfers. "
    "Een startplan zonder historie is voor dezelfde financier veel lastiger te "
    "beoordelen."),
   ("Kennis en mensen blijven",
    "Personeel, leveranciersafspraken en werkwijzen gaan mee. In sectoren waar "
    "vakmensen schaars zijn weegt dat zwaar."),
   ("Meer werkgelegenheid",
    "Onderzoek van de Europese Commissie wijst uit dat een geslaagde overname "
    "gemiddeld vijf banen oplevert, tegenover gemiddeld twee bij een startup."),
  ]),

  ("h2", "De keerzijde"),
  ("p", "Een overname is geen garantie. De risico's verschuiven alleen naar een "
        "ander deel van het traject."),
  ("tick", [
    "<b>Te veel betalen.</b> De prijs wordt bepaald door onderhandeling, niet door "
    "een formule. Wie zonder waardering aan tafel gaat, betaalt structureel meer.",
    "<b>Verborgen gebreken.</b> Achterstallig onderhoud, een aflopend "
    "huurcontract, een klant die 40 procent van de omzet levert of software die "
    "aan het einde van de levensduur zit.",
    "<b>Afhankelijkheid van de verkoper.</b> Als de eigenaar zelf de belangrijkste "
    "verkoper, monteur of relatiebeheerder is, vertrekt een deel van het bedrijf "
    "mee bij de overdracht.",
    "<b>Cultuur en personeel.</b> Een nieuwe eigenaar met andere plannen zorgt "
    "vrijwel altijd voor onrust. Zonder plan voor de eerste honderd dagen kost dat "
    "mensen.",
  ]),
  ("p", "Het gereedschap om die risico's te beperken bestaat: een waardering, een "
        "<a href=\"/kennisbank/due-diligence/\">due diligence</a>, garanties en "
        "vrijwaringen in het contract, en een deel van de koopsom dat later betaald "
        "wordt via een <a href=\"/kennisbank/earn-out/\">earn-out</a>."),

  ("h2", "Wanneer zelf beginnen toch beter uitpakt"),
  ("p", "De overnameroute is geen standaardadvies. Zelf beginnen is logischer als "
        "het idee nieuw is, als er geen bedrijven te koop staan die aansluiten, of "
        "als het beschikbare kapitaal simpelweg te klein is voor een serieuze "
        "koopsom. Ook geldt: een bedrijf dat te koop staat omdat het structureel "
        "verliesgevend is, lost geen enkel probleem op."),
  ("panel", "Combinatie van beide routes", [
   ("p", "Een tussenvorm die in de praktijk veel voorkomt: een kleine bestaande "
         "onderneming of webshop overnemen als basis, en daar een nieuw concept "
         "bovenop bouwen. De koper krijgt dan omzet, klanten en vindbaarheid mee, "
         "en houdt de vrijheid om het aanbod te veranderen. Webshops in dat "
         "segment staan onder meer op %s." % WO_NAKED),
  ]),

  ("h2", "Waar het aanbod staat"),
  ("p", "Bedrijven in het MKB komen op een beperkt aantal plaatsen op de markt. "
        "Voor bedrijven in het algemeen is dat %s, met het volledige aanbod op %s. "
        "Voor webshops, e-commercemerken en marketplace-accounts is dat %s, met "
        "het aanbod op %s."
        % (OA_MERK, oa("bedrijven-te-koop"), WO_MERK, wo("aanbod/Webshops%20te%20koop"))),
 ],
 "related": [
  ("Cijfers en onderzoek", "/starten-of-overnemen/cijfers-en-onderzoek/"),
  ("Kosten vergelijken", "/starten-of-overnemen/kosten-vergelijken/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
 ],
},

# ------------------------------------------------------------ cijfers
{
 "path": "starten-of-overnemen/cijfers-en-onderzoek/",
 "crumb": "Cijfers en onderzoek",
 "title": "Cijfers: overlevingskans van overnames en startups",
 "desc": "Eurobarometer, Oostenrijks onderzoek, het werk van lector Lex van "
         "Teeffelen en cijfers van KVK en de Europese Commissie over overnames, "
         "startups en werkgelegenheid.",
 "kicker": "Deel 2",
 "h1": "Cijfers en onderzoek",
 "lead": "De stelling dat overnemen vaker slaagt dan starten rust op onderzoek uit "
         "meerdere landen. Hieronder staan de cijfers, met vermelding van de bron "
         "en het jaar waarop ze betrekking hebben.",
 "blocks": [
  ("h2", "Voorkeur tegenover uitkomst"),
  ("p", "De Eurobarometer-enquete naar ondernemerschap laat een duidelijke "
        "voorkeur zien: 65 procent van de ondervraagden zou liever zelf een bedrijf "
        "opstarten, 35 procent zou liever een bestaand bedrijf overnemen. De "
        "uitkomsten per route wijzen de andere kant op."),
  ("table",
   ["Onderzoek", "Overgenomen bedrijven", "Startups"],
   [
    ["Oostenrijks onderzoek, nog operationeel na vijf jaar", "96 procent", "75 procent"],
    ["Nederlands onderzoek, nog bestaand na vijf jaar",
     "ruim 90 procent", "ongeveer de helft"],
   ]),
  ("p", "Het Nederlandse onderzoek komt van lector Lex van Teeffelen, verbonden aan "
        "Hogeschool Utrecht, die al jaren onderzoek doet naar bedrijfsoverdrachten "
        "en opheffingen in het Nederlandse MKB."),

  ("h2", "Overnames en werkgelegenheid"),
  ("p", "De Europese Commissie onderzocht de markt voor overnames van kleinere "
        "ondernemingen. Op Europees niveau gaat het om ongeveer 610.000 overnames "
        "per jaar van bedrijven tot 10 miljoen euro omzet. Daar zijn miljoenen "
        "banen mee gemoeid."),
  ("p", "Een opvallende uitkomst uit datzelfde onderzoek: een geslaagde overname "
        "levert gemiddeld vijf banen op, terwijl een startup er gemiddeld twee "
        "oplevert. Overnames van kleine bedrijven vormen de meerderheid van alle "
        "deals, maar krijgen een fractie van de aandacht."),

  ("h2", "De Nederlandse bedrijvenpopulatie in 2026"),
  ("p", "KVK publiceerde op 17 april 2026 de cijfers over het eerste kwartaal. Op "
        "31 maart 2026 stonden er 2.601.125 bedrijven in het Handelsregister, "
        "0,9 procent meer dan een jaar eerder. Het aantal starters lag 2,0 procent "
        "hoger dan in het eerste kwartaal van 2025, het aantal stoppers 7,2 procent "
        "lager en het aantal faillissementen 10,9 procent lager."),
  ("p", "Die cijfers volgden op een jaar met historisch lage groei. Voor kopers is "
        "vooral het aantal stoppers relevant: elke stopper is een bedrijf dat "
        "opgeheven wordt in plaats van overgedragen."),

  ("h2", "Wie er wil stoppen"),
  ("p", "Ipsos I&O ondervroeg voor de ABN AMRO Sectorprognoses 2026-2027 een groep "
        "van 519 ondernemers. Ruim twee derde wil binnen tien jaar stoppen met "
        "ondernemen. Van hen heeft 22 procent geen concrete opvolgingsplannen en "
        "zoekt 20 procent al naar een opvolger zonder resultaat. Het onderzoek "
        "verscheen op 11 februari 2026."),
  ("p", "De vergrijzing zit ook in de leeftijdsopbouw: bijna 13 procent van de "
        "ondernemers is 65 jaar of ouder, tegenover 7 procent in 2010."),

  ("h2", "Wat bedrijven opbrengen"),
  ("p", "De Overname Barometer van Brookz en Dealsuite, gebaseerd op een enquete "
        "onder 291 Nederlandse overnameadviesbureaus, kwam in februari 2026 uit op "
        "een gemiddelde EBITDA-multiple van 5,0 voor de tweede helft van 2025. Het "
        "onderzoek gaat over bedrijven met een omzet tussen 0,5 en 50 miljoen euro."),
  ("table",
   ["Sector", "Gemiddelde EBITDA-multiple, tweede helft 2025"],
   [
    ["Softwareontwikkeling", "7,5"],
    ["IT-dienstverlening", "6,7"],
    ["Zorg en farmacie", "6,5"],
    ["Gemiddelde over alle sectoren", "5,0"],
    ["Horeca, toerisme en recreatie", "3,3"],
    ["Retail", "2,5"],
   ]),
  ("p", "Uit hetzelfde onderzoek: het aantal transacties lag in de tweede helft van "
        "2025 8 procent hoger dan in de eerste helft, de gemiddelde leeftijd van "
        "verkopende ondernemers daalde van 59 jaar in 2015 naar 54 jaar in 2025, en "
        "30 procent van de trajecten duurt inmiddels langer dan een jaar."),
  ("p", "Wat een multiple betekent en waarom hij per sector zo sterk verschilt "
        "staat op de pagina <a href=\"/kennisbank/multiples/\">multiples</a>. Een "
        "eerste eigen berekening kan met de "
        "<a href=\"/tools/wat-is-mijn-bedrijf-waard/\">rekentool</a>."),

  ("h2", "E-commerce in cijfers"),
  ("p", "Voor wie een webshop overweegt is de Thuiswinkel Markt Monitor de "
        "standaardbron. In 2025 gaven Nederlandse consumenten 35,7 miljard euro uit "
        "in webwinkels, 1 procent minder dan in 2024. De bestedingen aan producten "
        "stegen met 2 procent, die aan diensten daalden met 5 procent. Het aantal "
        "online aankopen bleef vrijwel gelijk op 347 miljoen."),
  ("p", "Een markt die op productniveau licht groeit en op dienstenniveau krimpt "
        "vraagt om nuance in elk businessplan dat met een groeipercentage rekent. "
        "De pagina <a href=\"/checklists/webshop-beginnen/\">checklist webshop "
        "beginnen</a> gaat daar verder op in."),

  ("panel", "Verantwoording", [
   ("p", "De cijfers hierboven komen uit gepubliceerd onderzoek van de Europese "
         "Commissie, KVK, Ipsos I&O in opdracht van ABN AMRO, Brookz en Dealsuite, "
         "Thuiswinkel.org en het werk van lector Lex van Teeffelen. Onderzoek "
         "veroudert: bij elk cijfer staat het jaar waarop het betrekking heeft."),
  ]),
 ],
 "related": [
  ("Waarom overnemen", "/starten-of-overnemen/waarom-overnemen/"),
  ("Multiples", "/kennisbank/multiples/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Nieuws", "/nieuws/"),
 ],
},

# ------------------------------------------------------------ kosten
{
 "path": "starten-of-overnemen/kosten-vergelijken/",
 "crumb": "Kosten vergelijken",
 "title": "Wat kost starten en wat kost overnemen",
 "desc": "De kostenposten van een start naast die van een overname, inclusief "
         "werkkapitaal, adviseurskosten en de maanden zonder inkomen die bij een "
         "start horen.",
 "kicker": "Deel 3",
 "h1": "Kosten vergelijken",
 "lead": "Zelf beginnen lijkt goedkoper omdat de koopsom ontbreekt. Wie de "
         "aanloopperiode meerekent, komt vaak op een ander beeld uit.",
 "blocks": [
  ("h2", "De zichtbare kosten"),
  ("p", "Bij een start bestaan de kosten uit inschrijving, inrichting, voorraad of "
        "gereedschap, een website en marketing. Bij een overname bestaan ze uit de "
        "koopsom, het werkkapitaal en de begeleiding. Die tweede lijst oogt hoger, "
        "maar staat tegenover een bedrijf dat vanaf de eerste dag omzet maakt."),
  ("table",
   ["Kostenpost", "Zelf beginnen", "Overnemen"],
   [
    ["Inschrijving Handelsregister", "Eenmalig, tientallen euro's", "Vaak niet van toepassing"],
    ["Koopsom", "Geen", "De grootste post, meestal een veelvoud van de winst"],
    ["Werkkapitaal", "Beperkt bij de start, groeit mee", "Direct nodig voor voorraad en debiteuren"],
    ["Inrichting en middelen", "Volledig zelf op te bouwen", "Aanwezig, staat in de balans"],
    ["Marketing om te beginnen", "Substantieel, er is nog geen naamsbekendheid",
     "Lager, er is bestaand verkeer en een klantenbestand"],
    ["Advies en juridisch", "Beperkt", "Waardering, contract en due diligence"],
    ["Eigen inkomen in de aanloop", "Maanden tot jaren zelf te dragen",
     "Uit de bestaande kasstroom"],
   ]),

  ("h2", "De post die het vaakst vergeten wordt"),
  ("p", "Het eigen inkomen tijdens de aanloopperiode is bij een start de grootste "
        "verborgen kostenpost. Een bedrijf dat pas na anderhalf jaar kostendekkend "
        "draait, kost achttien maanden aan levensonderhoud. Bij een modaal "
        "huishouden loopt dat bedrag al snel op tot een bedrag dat vergelijkbaar is "
        "met de koopsom van een klein bedrijf."),
  ("p", "Daar komt bij dat een startende ondernemer die achttien maanden ook zelf "
        "moet financieren. Een bank financiert geen levensonderhoud, een verkoper "
        "die meefinanciert bij een overname doet dat indirect wel, doordat het "
        "bedrijf vanaf dag een salaris kan uitbetalen."),

  ("h2", "Werkkapitaal bij een overname"),
  ("p", "Werkkapitaal is het geld dat vastzit in voorraad en openstaande facturen, "
        "verminderd met wat er nog aan leveranciers openstaat. Bij een overname "
        "wordt vaak alleen naar de koopsom gekeken, terwijl het werkkapitaal er "
        "bovenop komt. Een groothandel met veel voorraad vraagt daardoor een fors "
        "hoger totaalbedrag dan de koopsom suggereert."),
  ("p", "De afspraken hierover horen expliciet in de koopovereenkomst thuis. Wat "
        "daar speelt staat op de pagina "
        "<a href=\"/kennisbank/activa-of-aandelen/\">activa of aandelen</a>."),

  ("h2", "Kosten van een webshop"),
  ("p", "Bij webshops ligt de verhouding anders. Een webshop opzetten kan technisch "
        "gezien voor een paar honderd euro per jaar, met een abonnement op een "
        "platform en een domeinnaam. De kosten zitten in voorraad, in fotografie en "
        "content, en vooral in het verwerven van bezoekers. Adverteren en "
        "vindbaarheid opbouwen kost in de meeste niches meer dan de techniek."),
  ("p", "Een bestaande webshop overnemen betekent betalen voor precies dat wat het "
        "duurst is om zelf op te bouwen: verkeer, klantenbestand, reviews en "
        "positie in zoekresultaten. Het aanbod van webshops en e-commercemerken "
        "staat op %s. Een eerste indicatie van de waarde geeft de "
        "<a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool voor webshops</a>."
        % WO_MERK),

  ("h2", "Rekenvoorbeeld"),
  ("p", "Twee ondernemers beginnen in dezelfde branche, met hetzelfde doel: een "
        "eigen inkomen van 60.000 euro per jaar."),
  ("table",
   ["", "Ondernemer A start zelf", "Ondernemer B neemt over"],
   [
    ["Investering jaar 1", "25.000 euro opbouw en marketing", "180.000 euro koopsom en kosten"],
    ["Eigen inkomen jaar 1", "0 euro", "60.000 euro"],
    ["Eigen inkomen jaar 2", "20.000 euro", "60.000 euro"],
    ["Eigen inkomen jaar 3", "55.000 euro", "65.000 euro"],
    ["Financiering", "Eigen middelen", "Bank, eigen inbreng en vendor loan"],
    ["Kans dat het bedrijf na vijf jaar nog bestaat",
     "Ongeveer de helft, volgens Nederlands onderzoek",
     "Ruim 90 procent, volgens Nederlands onderzoek"],
   ]),
  ("p", "Het voorbeeld is een illustratie, geen norm. De verhoudingen verschillen "
        "sterk per sector en per bedrijf. De strekking blijft: de koopsom is niet "
        "het enige bedrag dat telt, en gemiste inkomsten tellen mee."),
 ],
 "related": [
  ("Financiering en risico", "/starten-of-overnemen/financiering-en-risico/"),
  ("Checklist bedrijf beginnen", "/checklists/bedrijf-beginnen/"),
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Wat is mijn webshop waard", "/tools/wat-is-mijn-webshop-waard/"),
 ],
},

# ------------------------------------------------------------ financiering
{
 "path": "starten-of-overnemen/financiering-en-risico/",
 "crumb": "Financiering en risico",
 "title": "Financiering van een overname en de risico's per route",
 "desc": "Bankfinanciering, eigen inbreng, vendor loan en earn-out bij een "
         "bedrijfsovername, plus de risico's die horen bij zelf beginnen en bij "
         "overnemen.",
 "kicker": "Deel 4",
 "h1": "Financiering en risico",
 "lead": "Een overname wordt zelden uit een enkele bron betaald. De gebruikelijke "
         "opbouw is een stapeling van eigen geld, bankfinanciering en een deel dat "
         "de verkoper zelf laat staan.",
 "blocks": [
  ("h2", "De gebruikelijke opbouw"),
  ("steps", [
   ("Eigen inbreng",
    "Financiers verwachten dat de koper zelf een substantieel deel inbrengt. "
    "Zonder eigen geld is het gesprek met een bank in de praktijk kort."),
   ("Bankfinanciering",
    "Een bank beoordeelt de kasstroom van de afgelopen jaren, de zekerheden en de "
    "ervaring van de koper. Bij een overname is er historie om op te beoordelen, "
    "bij een start niet."),
   ("Vendor loan",
    "De verkoper laat een deel van de koopsom staan als lening aan de koper. Dat "
    "verlaagt het bedrag dat direct gefinancierd moet worden en geeft een signaal: "
    "de verkoper gelooft zelf in de continuiteit."),
   ("Earn-out",
    "Een deel van de prijs wordt later betaald, afhankelijk van resultaten na de "
    "overdracht. Het overbrugt een verschil van inzicht over de prognose."),
   ("Aanvullende bronnen",
    "Kredietunies, informele investeerders, achtergestelde leningen of "
    "crowdfunding vullen aan wat bank en eigen inbreng niet dekken."),
  ]),

  ("h2", "Rente in 2026"),
  ("p", "De Europese Centrale Bank hield de depositorente op 23 juli 2026 "
        "ongewijzigd op 2,25 procent. Het rentepeil bepaalt niet alleen de "
        "maandlast van een overnamefinanciering, maar indirect ook de prijs: hoe "
        "duurder geld, hoe lager het bedrag dat een koper uit dezelfde kasstroom "
        "kan financieren."),
  ("p", "Dat effect is zichtbaar in de manier waarop overnames worden gestructureerd. "
        "Naarmate bancaire financiering minder ruim is, groeit het aandeel van "
        "vendor loans en earn-outs in de dealstructuur."),

  ("h2", "Risico's bij zelf beginnen"),
  ("tick", [
    "<b>Marktrisico.</b> De belangrijkste vraag, of er genoeg mensen willen betalen, "
    "wordt pas beantwoord nadat de investering al gedaan is.",
    "<b>Aanlooprisico.</b> Vrijwel elk plan onderschat hoe lang het duurt voordat "
    "de omzet de kosten dekt.",
    "<b>Financieringsrisico.</b> Zonder historie is externe financiering lastig, "
    "waardoor het risico grotendeels privé blijft liggen.",
    "<b>Concentratie op de oprichter.</b> Alles hangt in het begin aan een persoon, "
    "van verkoop tot uitvoering.",
  ]),

  ("h2", "Risico's bij overnemen"),
  ("tick", [
    "<b>Prijsrisico.</b> Te veel betalen is niet te repareren met hard werken. "
    "Een onderbouwde <a href=\"/kennisbank/waardebepaling/\">waardebepaling</a> is "
    "de eerste verdedigingslinie.",
    "<b>Informatierisico.</b> De verkoper kent het bedrijf beter dan de koper. "
    "Daar zijn <a href=\"/kennisbank/due-diligence/\">due diligence</a>, garanties "
    "en vrijwaringen voor bedoeld.",
    "<b>Overdrachtsrisico.</b> Klanten, personeel of leveranciers die na de "
    "overdracht vertrekken. Een overdrachtsperiode waarin de verkoper aanblijft "
    "beperkt dat.",
    "<b>Financieringsrisico.</b> Een zware financiering laat weinig ruimte voor "
    "tegenvallers in de eerste jaren.",
  ]),

  ("h2", "Risico verdelen in het contract"),
  ("p", "Het verschil tussen een dure en een verstandige overname zit vaak niet in "
        "de prijs, maar in de verdeling van het risico. Vier instrumenten komen in "
        "vrijwel elk MKB-traject terug."),
  ("table",
   ["Instrument", "Wat het doet"],
   [
    ["Garanties", "De verkoper staat in voor feiten over het bedrijf, bijvoorbeeld "
     "dat de administratie klopt en er geen lopende procedures zijn."],
    ["Vrijwaringen", "De verkoper draagt een specifiek bekend risico, bijvoorbeeld "
     "een lopend geschil, ook na de overdracht."],
    ["Escrow", "Een deel van de koopsom staat een periode op een geblokkeerde "
     "rekening, als dekking voor claims."],
    ["Earn-out", "Een deel van de prijs hangt af van de resultaten na de overdracht."],
   ]),
  ("p", "Toelichting op deze begrippen staat in de "
        "<a href=\"/kennisbank/begrippenlijst/\">begrippenlijst</a>."),

  ("h2", "Begeleiding"),
  ("p", "Een overnametraject in het MKB loopt in de regel via een adviseur die de "
        "waardering, het proces en de onderhandeling begeleidt. Voor bedrijven in "
        "het algemeen biedt %s dat aan, met een toelichting op de werkwijze op %s. "
        "Voor webshops en e-commercebedrijven doet %s hetzelfde, met een overzicht "
        "van de diensten op %s."
        % (OA_MERK, oa("hoe-werkt-het"), WO_MERK, wo("onze-diensten"))),
 ],
 "related": [
  ("Kennisbank financiering", "/kennisbank/financiering/"),
  ("Earn-out", "/kennisbank/earn-out/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
 ],
},
]
