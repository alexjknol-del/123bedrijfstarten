"""Kennisbank: begrippen en onderwerpen uit het overnameproces."""

from .common import OA_MERK, WO_MERK, oa, wo

TERMEN = [
 ("Activatransactie", "Verkoop van losse bedrijfsonderdelen zoals inventaris, "
  "voorraad, klantenbestand en goodwill, in plaats van de aandelen."),
 ("Aandelentransactie", "Verkoop van de aandelen van een bv. De onderneming gaat "
  "in zijn geheel over, inclusief het verleden."),
 ("Bad leaver", "Bepaling in een aandeelhoudersovereenkomst die regelt tegen welke "
  "voorwaarden een vertrekkende aandeelhouder zijn aandelen moet aanbieden bij "
  "verwijtbaar vertrek."),
 ("Bezitseis", "Eis in de bedrijfsopvolgingsregeling dat de overdrager de "
  "onderneming een bepaalde periode in bezit had voordat de vrijstelling geldt."),
 ("Boekenonderzoek", "Nederlandse term voor due diligence: het onderzoek dat een "
  "koper doet naar de financiële, juridische en operationele situatie."),
 ("Cash and debt free", "Waarderingsafspraak waarbij het bedrijf zonder schulden "
  "en zonder overtollige kas wordt overgedragen."),
 ("Closing", "Het moment waarop de transactie daadwerkelijk wordt uitgevoerd en "
  "de aandelen of activa overgaan."),
 ("Discounted cash flow", "Waarderingsmethode die toekomstige kasstromen "
  "terugrekent naar de waarde van vandaag."),
 ("Deelnemingsvrijstelling", "Fiscale regeling waardoor winst op de verkoop van "
  "een deelneming binnen een holdingstructuur onbelast blijft."),
 ("Due diligence", "Boekenonderzoek door de koper voordat de koopovereenkomst "
  "wordt getekend."),
 ("Earn-out", "Deel van de koopsom dat later wordt betaald, afhankelijk van de "
  "resultaten na de overdracht."),
 ("EBITDA", "Resultaat voor rente, belasting, afschrijvingen en amortisatie. De "
  "meest gebruikte basis voor een multiple."),
 ("Escrow", "Geblokkeerde rekening waarop een deel van de koopsom tijdelijk staat "
  "als dekking voor eventuele claims."),
 ("Exitstrategie", "Het plan van de ondernemer voor het moment en de manier waarop "
  "hij het bedrijf verlaat."),
 ("Fairness opinion", "Onafhankelijk oordeel over de redelijkheid van een prijs of "
  "een transactie."),
 ("Garanties", "Verklaringen van de verkoper over feiten en cijfers, met een "
  "regeling voor het geval die niet blijken te kloppen."),
 ("Goodwill", "Het deel van de koopsom dat uitstijgt boven de waarde van de "
  "materiële bezittingen. Betaald voor klanten, naam en verdiencapaciteit."),
 ("Herinvesteringsreserve", "Fiscale reserve waarmee de boekwinst op een verkocht "
  "bedrijfsmiddel onder voorwaarden kan worden doorgeschoven."),
 ("Holding", "Vennootschap die de aandelen in de werkmaatschappij houdt. Maakt een "
  "latere verkoop fiscaal eenvoudiger."),
 ("Indicatief bod", "Vrijblijvend bod met de belangrijkste voorwaarden, uitgebracht "
  "voordat het boekenonderzoek plaatsvindt."),
 ("Intentieverklaring", "Ook wel letter of intent: schriftelijke vastlegging van "
  "prijs, structuur, exclusiviteit en planning, onder voorbehoud."),
 ("Intrinsieke waarde", "Het eigen vermogen volgens de balans, gecorrigeerd naar "
  "actuele waarde van bezittingen en schulden."),
 ("Locked box", "Afspraak waarbij de prijs wordt vastgesteld op basis van een "
  "balans van een eerdere datum, zonder nacalculatie achteraf."),
 ("Management buy-in", "Overname door een externe manager die zelf de leiding gaat "
  "voeren."),
 ("Management buy-out", "Overname door het zittende management of personeel."),
 ("Multiple", "Factor waarmee de winst wordt vermenigvuldigd om tot een "
  "ondernemingswaarde te komen."),
 ("Non-concurrentiebeding", "Afspraak die de verkoper verbiedt om na de overdracht "
  "opnieuw in dezelfde markt actief te worden."),
 ("Normaliseren", "Corrigeren van de cijfers voor eenmalige posten en voor een "
  "marktconform ondernemersloon, zodat resultaten vergelijkbaar worden."),
 ("Ondernemingswaarde", "De waarde van de onderneming zelf, los van de manier "
  "waarop die gefinancierd is."),
 ("Overdrachtsdocument", "Document waarin wordt vastgelegd wat er feitelijk "
  "overgaat, van wachtwoorden en contracten tot sleutels en accounts."),
 ("Sellers discretionary earnings", "Winst inclusief het ondernemersloon en "
  "privéposten. Veel gebruikt bij kleine bedrijven en webshops."),
 ("Term sheet", "Beknopte vastlegging van de hoofdlijnen van een transactie, "
  "voorafgaand aan de uitgewerkte contracten."),
 ("Vendor loan", "Lening van de verkoper aan de koper voor een deel van de "
  "koopsom."),
 ("Verkoopmemorandum", "Uitgebreide beschrijving van het bedrijf, bedoeld voor "
  "serieuze gegadigden na ondertekening van een geheimhoudingsverklaring."),
 ("Voortzettingseis", "Eis in de bedrijfsopvolgingsregeling dat de verkrijger de "
  "onderneming een bepaalde periode voortzet."),
 ("Vrijwaring", "Afspraak waarbij de verkoper een specifiek bekend risico ook na "
  "de overdracht voor eigen rekening neemt."),
 ("Werkkapitaal", "Het geld dat vastzit in voorraad en debiteuren, verminderd met "
  "de openstaande schulden aan leveranciers."),
 ("Geheimhoudingsverklaring", "Overeenkomst waarin een gegadigde zich verplicht om "
  "de ontvangen informatie vertrouwelijk te behandelen."),
]


def _termen_rows():
    return [[t, u] for t, u in sorted(TERMEN, key=lambda x: x[0].lower())]


PAGES = [

{
 "path": "kennisbank/",
 "crumb": "Kennisbank",
 "title": "Kennisbank bedrijfsovername: begrippen en onderwerpen",
 "desc": "Uitleg over waardebepaling, multiples, goodwill, due diligence, "
         "intentieverklaring, earn-out, financiering en belasting bij een "
         "bedrijfsovername.",
 "kicker": "Kennisbank",
 "h1": "Kennisbank",
 "lead": "De onderwerpen die in vrijwel elk overnametraject terugkomen, in gewone "
         "taal uitgelegd.",
 "blocks": [
  ("h2", "Waarde en prijs"),
  ("cards", [
   ("Waardebepaling", "De methoden waarmee de waarde van een onderneming wordt "
    "berekend, en wanneer welke methode past.", "/kennisbank/waardebepaling/"),
   ("Multiples", "Wat een multiple is, waarom die per sector verschilt en hoe "
    "die wordt toegepast.", "/kennisbank/multiples/"),
   ("Goodwill", "Waar het bedrag boven de boekwaarde vandaan komt en waarom "
    "kopers dat betalen.", "/kennisbank/goodwill/"),
  ]),
  ("h2", "Het proces"),
  ("cards", [
   ("Geheimhoudingsverklaring", "Waarom een NDA de eerste stap is en wat er in "
    "hoort te staan.", "/kennisbank/nda/"),
   ("Intentieverklaring", "Wat een letter of intent vastlegt en wat er bindend "
    "aan is.", "/kennisbank/intentieverklaring/"),
   ("Due diligence", "Het boekenonderzoek: wat er onderzocht wordt en wat de "
    "uitkomsten met de prijs doen.", "/kennisbank/due-diligence/"),
   ("Earn-out", "Een deel van de prijs achteraf, gekoppeld aan resultaten.",
    "/kennisbank/earn-out/"),
  ]),
  ("h2", "Structuur, geld en fiscaliteit"),
  ("cards", [
   ("Activa of aandelen", "Twee manieren om een bedrijf over te dragen, met "
    "verschillende gevolgen.", "/kennisbank/activa-of-aandelen/"),
   ("Financiering", "Hoe een overname in het MKB betaald wordt.",
    "/kennisbank/financiering/"),
   ("Belasting bij overdracht", "Deelnemingsvrijstelling, "
    "bedrijfsopvolgingsregeling en de wijzigingen per 2025 en 2026.",
    "/kennisbank/belasting/"),
   ("Begrippenlijst", "Achtendertig termen uit de overnamepraktijk, alfabetisch.",
    "/kennisbank/begrippenlijst/"),
  ]),
  ("h2", "Verder lezen bij de bron"),
  ("p", "Uitgebreidere naslag over deze onderwerpen staat in de kennisbanken van de "
        "twee platformen die op deze site worden uitgelicht: %s en %s."
        % (oa("kennisbank"), wo("kennisbank"))),
 ],
 "related": [
  ("Starten of overnemen", "/starten-of-overnemen/"),
  ("Verkopen", "/verkopen/"),
  ("Rekentools", "/tools/"),
 ],
},

{
 "path": "kennisbank/waardebepaling/",
 "crumb": "Waardebepaling",
 "title": "Waardebepaling van een bedrijf: methoden en verschillen",
 "desc": "Intrinsieke waarde, rentabiliteitswaarde, discounted cash flow en de "
         "multiplemethode naast elkaar, met uitleg over normaliseren en over het "
         "verschil tussen waarde en prijs.",
 "kicker": "Waarde",
 "h1": "Waardebepaling",
 "lead": "Er bestaat geen enkele juiste waarde van een onderneming. Er bestaan "
         "methoden die vanuit verschillende invalshoeken tot een bedrag komen, en "
         "een onderhandeling die daar een prijs van maakt.",
 "blocks": [
  ("h2", "Vier methoden"),
  ("table",
   ["Methode", "Uitgangspunt", "Past bij"],
   [
    ["Intrinsieke waarde", "Bezittingen minus schulden, tegen actuele waarde",
     "Bedrijven met veel machines, vastgoed of voorraad"],
    ["Rentabiliteitswaarde", "Genormaliseerde winst gedeeld door een "
     "rendementseis", "Stabiele bedrijven met een voorspelbaar resultaat"],
    ["Discounted cash flow", "Toekomstige vrije kasstromen, teruggerekend naar nu",
     "Bedrijven met een onderbouwde prognose en investeringsplan"],
    ["Multiplemethode", "Genormaliseerde EBITDA maal een sectorfactor",
     "De meeste MKB-transacties, als toets en als startpunt"],
   ]),
  ("p", "In de praktijk worden meerdere methoden naast elkaar gelegd. Als de "
        "uitkomsten ver uiteenlopen, zegt dat iets: meestal dat de winst sterk "
        "wisselt of dat er veel vermogen in het bedrijf vastzit dat geen rendement "
        "oplevert."),

  ("h2", "Normaliseren is de eerste stap"),
  ("p", "Voordat er gerekend wordt, worden de cijfers vergelijkbaar gemaakt. Dat "
        "betekent: eenmalige baten en lasten eruit, privékosten eruit, een "
        "marktconform loon voor de eigenaar erin, en huur tegen marktniveau als het "
        "pand van de eigenaar is."),
  ("p", "Een bedrijf met 250.000 euro winst waarin de eigenaar zichzelf 40.000 euro "
        "uitkeert, heeft na normalisatie een ander resultaat dan een bedrijf met "
        "dezelfde winst waarin de eigenaar een marktconform salaris opneemt. Zonder "
        "die correctie zijn de twee niet te vergelijken."),

  ("h2", "Waarde tegenover prijs"),
  ("p", "Waarde komt uit een berekening, prijs uit een onderhandeling. Een "
        "strategische koper die klanten of capaciteit zoekt komt op een ander bedrag "
        "uit dan een particuliere koper die een baan met eigendom zoekt. Beide "
        "bedragen kunnen kloppen."),
  ("p", "Wat de prijs daarnaast beïnvloedt: het aantal serieuze gegadigden, de "
        "financierbaarheid, de betaalstructuur en de mate waarin de verkoper haast "
        "heeft. Een lagere prijs met betaling ineens kan gunstiger uitpakken dan een "
        "hogere prijs die voor de helft uit een earn-out bestaat."),

  ("h2", "Wat de waarde drukt"),
  ("tick", [
    "afhankelijkheid van de eigenaar of van één medewerker",
    "een klant die een groot deel van de omzet levert",
    "resultaten die sterk wisselen per jaar",
    "achterstallige investeringen in machines, software of pand",
    "een administratie die niet snel te controleren is",
  ]),

  ("h2", "Zelf rekenen"),
  ("p", "Een eerste indicatie is te maken met de "
        "<a href=\"/tools/wat-is-mijn-bedrijf-waard/\">rekentool</a>, of voor "
        "webshops met de <a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool "
        "voor webshops</a>. Een uitgewerkte waardebepaling voor het MKB verzorgt "
        "%s, zie %s. Voor webshops en e-commercebedrijven doet %s dat, zie %s."
        % (OA_MERK, oa("bedrijf-waarderen"), WO_MERK,
           wo("overnameadvies/waardebepaling"))),
 ],
 "related": [
  ("Multiples", "/kennisbank/multiples/"),
  ("Goodwill", "/kennisbank/goodwill/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
 ],
},

{
 "path": "kennisbank/multiples/",
 "crumb": "Multiples",
 "title": "Multiples: wat kopers per sector betalen voor winst",
 "desc": "Uitleg over de EBITDA-multiple, de sectorverschillen volgens de Overname "
         "Barometer over de tweede helft van 2025 en de factoren die een multiple "
         "omhoog of omlaag brengen.",
 "kicker": "Waarde",
 "h1": "Multiples",
 "lead": "Een multiple is het aantal keren de jaarwinst dat een koper voor een "
         "bedrijf betaalt. De hoogte zegt vooral iets over risico en groei, niet "
         "over kwaliteit.",
 "blocks": [
  ("h2", "Hoe een multiple werkt"),
  ("p", "De rekensom is eenvoudig: genormaliseerde EBITDA maal de multiple geeft de "
        "ondernemingswaarde. Daar gaat de netto schuld af om tot de waarde van de "
        "aandelen te komen. Een bedrijf met 300.000 euro EBITDA en een multiple van "
        "5,0 heeft een ondernemingswaarde van 1,5 miljoen euro. Staat er 400.000 "
        "euro aan bankschuld tegenover, dan resteert 1,1 miljoen euro voor de "
        "aandelen."),

  ("h2", "Sectorverschillen"),
  ("p", "De Overname Barometer van Brookz en Dealsuite, gebaseerd op een enquete "
        "onder 291 Nederlandse overnameadviesbureaus, kwam over de tweede helft van "
        "2025 uit op een gemiddelde van 5,0. De verschillen per sector zijn groot."),
  ("table",
   ["Sector", "Gemiddelde multiple, tweede helft 2025"],
   [
    ["Softwareontwikkeling", "7,5"],
    ["IT-dienstverlening", "6,7"],
    ["Zorg en farmacie", "6,5"],
    ["Alle sectoren samen", "5,0"],
    ["Horeca, toerisme en recreatie", "3,3"],
    ["Retail", "2,5"],
   ]),
  ("p", "Het verschil tussen softwareontwikkeling en retail is niet dat de ene "
        "sector beter is dan de andere. Software kent terugkerende omzet, hoge "
        "marges en beperkte voorraad. Retail kent dunne marges, voorraadrisico en "
        "gevoeligheid voor conjunctuur. Kopers rekenen dat verschil in risico "
        "terug in de factor."),

  ("h2", "Wat de multiple binnen een sector beweegt"),
  ("table",
   ["Naar boven", "Naar beneden"],
   [
    ["Terugkerende omzet uit contracten", "Omzet die per opdracht opnieuw "
     "gewonnen moet worden"],
    ["Gespreid klantenbestand", "Eén klant met een groot aandeel"],
    ["Zelfstandig werkend team", "Eigenaar die onmisbaar is"],
    ["Meerjarige groei", "Dalende omzet of wisselende resultaten"],
    ["Grotere omvang", "Zeer kleine bedrijven, waar de koperskring kleiner is"],
   ]),

  ("h2", "Waarschuwing bij het gebruik van multiples"),
  ("p", "Een multiple is een marktgemiddelde en geen waardering. Twee valkuilen "
        "komen vaak voor. De eerste is rekenen met een niet-genormaliseerde winst, "
        "waardoor het bedrag te hoog uitvalt. De tweede is het overnemen van een "
        "multiple uit een sector waarin veel grotere bedrijven worden verhandeld: "
        "bedrijven met een paar ton winst worden structureel tegen lagere factoren "
        "verhandeld dan bedrijven met miljoenen winst."),
  ("p", "Voor webshops en e-commercebedrijven wordt vaker gerekend met een factor "
        "op de gecorrigeerde winst inclusief ondernemersloon. Die methode staat in "
        "de <a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool voor "
        "webshops</a>."),
 ],
 "related": [
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Cijfers en onderzoek", "/starten-of-overnemen/cijfers-en-onderzoek/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
 ],
},

{
 "path": "kennisbank/goodwill/",
 "crumb": "Goodwill",
 "title": "Goodwill bij een bedrijfsovername: waar het bedrag vandaan komt",
 "desc": "Wat goodwill is, waarom kopers boven de boekwaarde betalen, hoe goodwill "
         "wordt onderbouwd en wat het fiscale verschil is tussen een activa- en een "
         "aandelentransactie.",
 "kicker": "Waarde",
 "h1": "Goodwill",
 "lead": "Goodwill is het deel van de koopsom dat niet terug te vinden is in de "
         "spullen. Het staat voor klanten, naam, kennis en het vermogen om winst "
         "te maken.",
 "blocks": [
  ("h2", "Wat er onder valt"),
  ("tick", [
    "een bestaand klantenbestand met herhaalaankopen",
    "een naam die in de markt herkend wordt",
    "personeel met kennis en ervaring dat blijft",
    "werkwijzen, systemen en leveranciersafspraken",
    "vergunningen, certificaten en marktposities die tijd kosten om te krijgen",
  ]),
  ("p", "Wat er niet onder valt: de inspanning die de verkoper er ooit in heeft "
        "gestoken. Goodwill wordt bepaald door wat de koper met het bedrijf kan "
        "verdienen, niet door wat het de verkoper heeft gekost."),

  ("h2", "Hoe goodwill wordt onderbouwd"),
  ("p", "In de praktijk komt goodwill uit het verschil tussen de berekende waarde "
        "en de gecorrigeerde intrinsieke waarde. Een bedrijf met 500.000 euro aan "
        "materiële bezittingen en een berekende waarde van 1,2 miljoen euro heeft "
        "700.000 euro goodwill. De onderbouwing zit in de winst die het bedrijf "
        "structureel maakt en in de zekerheid dat die winst blijft."),
  ("p", "Precies daarom drukt afhankelijkheid van de eigenaar de goodwill zo hard: "
        "als de winst met de eigenaar vertrekt, is er weinig te kopen."),

  ("h2", "Fiscaal verschil"),
  ("table",
   ["", "Activatransactie", "Aandelentransactie"],
   [
    ["Voor de koper", "Goodwill is te activeren en over meerdere jaren af te "
     "schrijven, wat de belastbare winst drukt", "Geen afschrijving op goodwill, "
     "de koper koopt aandelen"],
    ["Voor de verkoper", "Boekwinst wordt in de onderneming belast",
     "Bij verkoop vanuit een holding vaak onbelast via de "
     "deelnemingsvrijstelling"],
   ]),
  ("p", "Dat verschil verklaart waarom kopers vaker naar een activatransactie "
        "neigen en verkopers vaker naar een aandelentransactie. Het is een van de "
        "eerste onderhandelpunten. Zie "
        "<a href=\"/kennisbank/activa-of-aandelen/\">activa of aandelen</a>."),

  ("h2", "Goodwill bij kleine bedrijven en webshops"),
  ("p", "Bij kleine ondernemingen bestaat de koopsom vaak vrijwel volledig uit "
        "goodwill, omdat er nauwelijks bezittingen zijn. Bij webshops zit de "
        "goodwill in het domein, de merknaam, de positie in zoekresultaten, het "
        "klantenbestand en de reviews. Dat maakt de onderbouwing kwetsbaarder: die "
        "posities kunnen na een overdracht bewegen. Wat daarbij gecontroleerd wordt "
        "staat in de <a href=\"/checklists/webshop-overnemen/\">checklist webshop "
        "overnemen</a>."),
 ],
 "related": [
  ("Activa of aandelen", "/kennisbank/activa-of-aandelen/"),
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Belasting bij overdracht", "/kennisbank/belasting/"),
 ],
},

{
 "path": "kennisbank/nda/",
 "crumb": "Geheimhoudingsverklaring",
 "title": "Geheimhoudingsverklaring bij een bedrijfsovername",
 "desc": "Waarom een NDA de eerste stap is in een verkooptraject, wat erin hoort "
         "te staan en hoe anonimiteit tijdens de verkoop wordt bewaakt.",
 "kicker": "Proces",
 "h1": "Geheimhoudingsverklaring",
 "lead": "Een verkoop die uitlekt kost klanten, personeel en onderhandelingsruimte. "
         "De geheimhoudingsverklaring is het eerste document dat een gegadigde "
         "tekent.",
 "blocks": [
  ("h2", "Waarom anonimiteit telt"),
  ("p", "Zolang een verkoop niet rond is, is elk gerucht schadelijk. Personeel gaat "
        "solliciteren, klanten stellen bestellingen uit en concurrenten gebruiken "
        "de onzekerheid in hun eigen verkoopgesprekken. Daarom staat een bedrijf in "
        "het MKB doorgaans anoniem te koop, met een profiel dat de branche, de orde "
        "van grootte en de regio noemt zonder herleidbaar te zijn."),

  ("h2", "Wat er in een NDA hoort"),
  ("tick", [
    "welke informatie vertrouwelijk is, en dat het bestaan van het gesprek zelf "
    "daar ook onder valt",
    "voor welk doel de informatie gebruikt mag worden",
    "wie de informatie binnen de organisatie van de gegadigde mag zien",
    "hoe lang de verplichting duurt, gebruikelijk twee tot vijf jaar",
    "wat er met documenten gebeurt als het traject stopt",
    "een verbod op het rechtstreeks benaderen van personeel en klanten",
  ]),

  ("h2", "Wat een NDA niet oplost"),
  ("p", "Een geheimhoudingsverklaring is lastig te handhaven. Aantonen dat er "
        "schade is ontstaan door schending is in de praktijk moeilijk. De echte "
        "bescherming zit daarom in de volgorde waarin informatie wordt gedeeld: "
        "eerst een profiel, dan een memorandum, en pas na een indicatief bod de "
        "gevoelige gegevens zoals klantnamen, marges per klant en "
        "personeelsdossiers."),
  ("p", "Bij een concurrent als gegadigde wordt die volgorde nog strikter "
        "aangehouden, waarbij de gevoeligste stukken pas in de laatste fase van het "
        "boekenonderzoek beschikbaar komen, soms alleen voor een adviseur en niet "
        "voor de koper zelf."),

  ("h2", "Praktisch"),
  ("p", "Overnameplatformen werken met een standaardverklaring die gegadigden "
        "digitaal ondertekenen voordat zij toegang krijgen tot de gegevens van een "
        "bedrijf. Voorbeelden van die werkwijze staan op %s en %s."
        % (oa("nda"), wo("over-ons/geheimhoudingsverklaring"))),
 ],
 "related": [
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
  ("Intentieverklaring", "/kennisbank/intentieverklaring/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
 ],
},

{
 "path": "kennisbank/intentieverklaring/",
 "crumb": "Intentieverklaring",
 "title": "Intentieverklaring bij een overname: wat een LOI vastlegt",
 "desc": "Wat er in een letter of intent staat, welke onderdelen bindend zijn, "
         "hoe exclusiviteit werkt en waarom de LOI het belangrijkste document van "
         "het traject is.",
 "kicker": "Proces",
 "h1": "Intentieverklaring",
 "lead": "De intentieverklaring lijkt een tussenstap, maar bepaalt in de praktijk "
         "de uitkomst. Wat hier niet in staat, valt later moeilijk alsnog te "
         "regelen.",
 "blocks": [
  ("h2", "Wat erin staat"),
  ("tick", [
    "de prijs of de manier waarop de prijs berekend wordt",
    "de structuur: aandelen of activa, en wat er wel en niet meegaat",
    "de betaling: ineens, in delen, met vendor loan of met earn-out",
    "de voorbehouden: boekenonderzoek, financiering, toestemming van derden",
    "exclusiviteit en de duur daarvan",
    "de planning tot aan de overdracht",
    "de rol van de verkoper na de overdracht",
    "geheimhouding en de verdeling van de kosten",
  ]),

  ("h2", "Bindend of niet"),
  ("p", "Een intentieverklaring is meestal deels bindend. De afspraken over "
        "geheimhouding, exclusiviteit en kostenverdeling zijn dat wel, de prijs en "
        "de transactie zelf niet, omdat die afhangen van het boekenonderzoek. Die "
        "verdeling hoort expliciet in het document te staan."),
  ("p", "Naar Nederlands recht kan het afbreken van onderhandelingen in een "
        "vergevorderd stadium onder omstandigheden tot schadeplichtigheid leiden. "
        "Een duidelijke clausule over wanneer en hoe partijen mogen stoppen "
        "voorkomt discussie."),

  ("h2", "Exclusiviteit"),
  ("p", "Exclusiviteit betekent dat de verkoper gedurende een afgesproken periode "
        "niet met anderen onderhandelt. Voor de koper is dat noodzakelijk: "
        "boekenonderzoek kost geld. Voor de verkoper is het een risico, omdat de "
        "onderhandelingspositie verzwakt zodra de andere kandidaten zijn "
        "afgehaakt."),
  ("p", "In het MKB is zes tot twaalf weken gebruikelijk, gekoppeld aan een "
        "planning met tussentijdse momenten. Een exclusiviteit zonder einddatum is "
        "voor de verkoper ongunstig."),

  ("h2", "De meest gemaakte fout"),
  ("p", "De prijs wordt vastgelegd, de rest niet. Als pas na het boekenonderzoek "
        "blijkt dat partijen anders dachten over werkkapitaal, over de omvang van "
        "de garanties of over de rol van de verkoper na de overdracht, is de "
        "onderhandelingspositie van de verkoper inmiddels verslechterd. Die punten "
        "horen in de intentieverklaring, niet in de koopovereenkomst."),
 ],
 "related": [
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Earn-out", "/kennisbank/earn-out/"),
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
 ],
},

{
 "path": "kennisbank/due-diligence/",
 "crumb": "Due diligence",
 "title": "Due diligence: het boekenonderzoek bij een overname",
 "desc": "Wat een koper onderzoekt voor de koopovereenkomst getekend wordt, welke "
         "onderdelen er zijn, hoe lang het duurt en wat bevindingen met de prijs "
         "doen.",
 "kicker": "Proces",
 "h1": "Due diligence",
 "lead": "Het boekenonderzoek is het moment waarop het verhaal van de verkoper "
         "getoetst wordt aan de stukken. Wat daar naar boven komt, bepaalt de "
         "laatste ronde van de onderhandeling.",
 "blocks": [
  ("h2", "Onderdelen"),
  ("table",
   ["Onderdeel", "Waar naar gekeken wordt"],
   [
    ["Financieel", "Jaarrekeningen, tussentijdse cijfers, normalisaties, "
     "werkkapitaal, debiteuren"],
    ["Fiscaal", "Aangiften, openstaande aanslagen, btw-positie, fiscale eenheid"],
    ["Juridisch", "Statuten, contracten, huur, licenties, lopende geschillen"],
    ["Personeel", "Arbeidsovereenkomsten, cao, verlofsaldi, verzuim, pensioen"],
    ["Operationeel", "Staat van bedrijfsmiddelen, voorraad, leveranciers, "
     "afhankelijkheden"],
    ["ICT en data", "Systemen, licenties, beveiliging, verwerking van "
     "persoonsgegevens"],
   ]),

  ("h2", "Hoe het loopt"),
  ("p", "De koper stuurt een vragenlijst, de verkoper zet de stukken in een "
        "digitale dataroom. Vervolgens komen er vervolgvragen en een of meer "
        "sessies met de eigenaar. In het MKB duurt dit twee tot zes weken, "
        "afhankelijk van de omvang en van hoe snel de stukken beschikbaar zijn."),
  ("p", "Snelheid is in het belang van de verkoper. Elke week vertraging vergroot "
        "de kans dat er iets tussenkomt: een klant die opzegt, een tegenvallend "
        "kwartaal of een koper die van gedachten verandert."),

  ("h2", "Wat bevindingen doen"),
  ("tick", [
    "<b>Prijsaanpassing</b> bij structurele afwijkingen, bijvoorbeeld winst die "
    "deels eenmalig blijkt",
    "<b>Vrijwaring</b> bij een bekend en afgebakend risico, zoals een lopend "
    "geschil",
    "<b>Garantie</b> bij onzekerheid over feiten, met een regeling als het anders "
    "blijkt",
    "<b>Escrow</b> bij risico's die pas later zichtbaar worden",
    "<b>Afbreken</b> bij bevindingen die het uitgangspunt onderuit halen",
  ]),

  ("h2", "Voorbereiding aan de verkoperskant"),
  ("p", "Verkopers die het dossier vooraf op orde brengen, houden de regie. Dat "
        "betekent: jaarcijfers en tussentijdse cijfers klaar, contracten "
        "gebundeld, personeelsdossiers compleet, vergunningen actueel en een "
        "toelichting op eenmalige posten. Een deel van de bevindingen is dan al "
        "besproken voordat de koper ernaar vraagt."),
  ("p", "Bij webshops en online bedrijven hoort daar een technisch en commercieel "
        "onderzoek bij: verkeersbronnen, meetgegevens over meerdere jaren, "
        "accounts, koppelingen en de opbouw van het klantenbestand. Zie de "
        "<a href=\"/checklists/webshop-overnemen/\">checklist webshop overnemen</a> "
        "en de scans die %s daarvoor aanbiedt op %s."
        % (WO_MERK, wo("overnameadvies/bedrijfsscans"))),
 ],
 "related": [
  ("Intentieverklaring", "/kennisbank/intentieverklaring/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
 ],
},

{
 "path": "kennisbank/earn-out/",
 "crumb": "Earn-out",
 "title": "Earn-out: een deel van de koopsom achteraf",
 "desc": "Hoe een earn-out werkt, waarom die wordt afgesproken, welke maatstaf "
         "gekozen wordt en welke afspraken discussie achteraf voorkomen.",
 "kicker": "Proces",
 "h1": "Earn-out",
 "lead": "Een earn-out overbrugt een verschil van inzicht over de toekomst. De "
         "verkoper gelooft in de prognose, de koper wil dat eerst zien.",
 "blocks": [
  ("h2", "Hoe het werkt"),
  ("p", "Een deel van de koopsom wordt bij levering betaald, een ander deel later, "
        "afhankelijk van de resultaten in de eerste een tot drie jaar na de "
        "overdracht. In het MKB gaat het vaak om tien tot dertig procent van de "
        "prijs."),
  ("p", "De constructie komt vooral voor bij bedrijven met sterk wisselende "
        "resultaten, bij een sterke afhankelijkheid van de verkoper, en bij "
        "prognoses die uitgaan van groei die nog niet zichtbaar is in de cijfers."),

  ("h2", "Welke maatstaf"),
  ("table",
   ["Maatstaf", "Voordeel", "Nadeel"],
   [
    ["Omzet", "Eenvoudig te meten en moeilijk te beïnvloeden",
     "Zegt niets over marge, koper kan omzet kopen met korting"],
    ["Brutomarge", "Dichter bij het resultaat", "Gevoelig voor inkoopkeuzes van "
     "de koper"],
    ["EBITDA", "Sluit aan bij de waardering", "Sterk te beïnvloeden door kosten "
     "die de koper toerekent"],
    ["Behoud van klanten", "Direct gekoppeld aan het risico dat de koper loopt",
     "Vraagt een heldere definitie van behoud"],
   ]),

  ("h2", "Afspraken die discussie voorkomen"),
  ("tick", [
    "een precieze definitie van de maatstaf, inclusief wat er wel en niet in "
    "meetelt",
    "de manier waarop kosten van de koper of van een moedermaatschappij worden "
    "behandeld",
    "de bevoegdheden van de verkoper in de periode waarin de earn-out loopt",
    "recht op inzage in de cijfers waarop de berekening rust",
    "een regeling voor het geval de koper het bedrijf tussentijds doorverkoopt",
    "een geschillenregeling met een onafhankelijke deskundige",
  ]),

  ("h2", "De belangrijkste waarschuwing"),
  ("p", "Een earn-out is geen prijsverhoging maar een risicoverschuiving. Een "
        "verkoper die de earn-out volledig meerekent in de opbrengst, rekent zich "
        "rijk: na de overdracht ligt de zeggenschap bij de koper. De praktische "
        "vuistregel is dat het bedrag dat bij levering wordt betaald, op zichzelf "
        "aanvaardbaar moet zijn."),
  ("p", "Alternatieven met minder discussie zijn een vendor loan met vaste "
        "aflossing, of een lagere prijs met betaling ineens. Zie ook "
        "<a href=\"/kennisbank/financiering/\">financiering</a>."),
 ],
 "related": [
  ("Financiering", "/kennisbank/financiering/"),
  ("Intentieverklaring", "/kennisbank/intentieverklaring/"),
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
 ],
},

{
 "path": "kennisbank/activa-of-aandelen/",
 "crumb": "Activa of aandelen",
 "title": "Activatransactie of aandelentransactie: het verschil",
 "desc": "De twee manieren om een onderneming over te dragen, met de gevolgen voor "
         "aansprakelijkheid, personeel, contracten en belasting.",
 "kicker": "Structuur",
 "h1": "Activa of aandelen",
 "lead": "Er zijn twee manieren om een bedrijf over te dragen. De keuze bepaalt "
         "wie welk verleden meeneemt, en wat er fiscaal gebeurt.",
 "blocks": [
  ("h2", "Het onderscheid"),
  ("p", "Bij een aandelentransactie koopt de koper de aandelen van de "
        "vennootschap. De onderneming blijft dezelfde rechtspersoon: alle "
        "contracten, vergunningen, schulden en risico's gaan mee, ook die uit het "
        "verleden."),
  ("p", "Bij een activatransactie koopt de koper losse onderdelen: inventaris, "
        "voorraad, klantenbestand, goodwill en soms het personeel. Wat niet in de "
        "koopovereenkomst staat, blijft achter bij de verkoper."),

  ("h2", "De gevolgen naast elkaar"),
  ("table",
   ["", "Aandelentransactie", "Activatransactie"],
   [
    ["Verleden", "Gaat mee, inclusief onbekende risico's",
     "Blijft in beginsel achter bij de verkoper"],
    ["Contracten", "Lopen door zonder overdracht", "Moeten stuk voor stuk worden "
     "overgezet, vaak met toestemming van de wederpartij"],
    ["Vergunningen", "Blijven in de vennootschap", "Moeten opnieuw worden "
     "aangevraagd of overgezet"],
    ["Personeel", "Blijft in dienst van dezelfde werkgever",
     "Gaat over via overgang van onderneming, met behoud van arbeidsvoorwaarden"],
    ["Goodwill voor de koper", "Niet af te schrijven",
     "Te activeren en af te schrijven"],
    ["Opbrengst voor de verkoper", "Vaak onbelast via de deelnemingsvrijstelling "
     "bij verkoop vanuit een holding", "Belast in de onderneming"],
    ["Notaris", "Nodig voor de levering van aandelen", "Niet altijd nodig"],
   ]),

  ("h2", "Waarom partijen tegenover elkaar staan"),
  ("p", "De koper heeft baat bij een activatransactie: minder onbekend risico en "
        "een afschrijfbare goodwill. De verkoper heeft baat bij een "
        "aandelentransactie: schoon uit de vennootschap en fiscaal gunstiger. Dat "
        "is een van de eerste onderhandelpunten, en het gaat om substantiële "
        "bedragen."),
  ("p", "Bij eenmanszaken en vennootschappen onder firma is er geen keuze: die "
        "worden altijd als activatransactie overgedragen, omdat er geen aandelen "
        "zijn. Dat is een van de redenen om bij een groeiend bedrijf tijdig naar "
        "de rechtsvorm te kijken, zie "
        "<a href=\"/verkopen/verkoopklaar-ondernemen/\">verkoopklaar ondernemen</a>."),

  ("h2", "Personeel"),
  ("p", "Bij een activatransactie waarbij een onderneming of een onderdeel daarvan "
        "overgaat, geldt de regeling voor overgang van onderneming. Werknemers gaan "
        "van rechtswege mee, met behoud van hun arbeidsvoorwaarden. Ontslag wegens "
        "de overgang zelf is niet toegestaan. Dit is een van de punten die in het "
        "boekenonderzoek zorgvuldig wordt bekeken."),
 ],
 "related": [
  ("Goodwill", "/kennisbank/goodwill/"),
  ("Belasting bij overdracht", "/kennisbank/belasting/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
 ],
},

{
 "path": "kennisbank/financiering/",
 "crumb": "Financiering",
 "title": "Financiering van een bedrijfsovername in het MKB",
 "desc": "De opbouw van een overnamefinanciering: eigen inbreng, bankkrediet, "
         "vendor loan, achtergestelde leningen en het effect van de rentestand in "
         "2026.",
 "kicker": "Geld",
 "h1": "Financiering",
 "lead": "Een overname in het MKB wordt vrijwel nooit uit één bron betaald. De "
         "financiering is een stapeling, en elke laag heeft eigen voorwaarden.",
 "blocks": [
  ("h2", "De lagen"),
  ("table",
   ["Laag", "Kenmerken"],
   [
    ["Eigen inbreng", "Financiers verwachten een substantieel deel uit eigen "
     "middelen. Zonder dat deel komt de rest niet rond."],
    ["Bancair krediet", "Beoordeeld op historische kasstroom, zekerheden en de "
     "ervaring van de koper. Aflossing meestal in vijf tot zeven jaar."],
    ["Vendor loan", "De verkoper laat een deel van de koopsom staan. Vaak "
     "achtergesteld bij de bank, met rente en een aflosschema."],
    ["Achtergestelde lening", "Van een investeerder of kredietunie, met een hogere "
     "rente omdat het risico groter is."],
    ["Earn-out", "Geen financiering in strikte zin, maar wel een manier om het "
     "bedrag bij levering te verlagen."],
   ]),

  ("h2", "Waar een bank naar kijkt"),
  ("tick", [
    "of de kasstroom na de overname de rente en aflossing kan dragen, met marge",
    "de kwaliteit en spreiding van het klantenbestand",
    "de zekerheden: voorraad, machines, debiteuren of vastgoed",
    "de ervaring van de koper in dezelfde branche",
    "of de verkoper zelf meefinanciert, wat als vertrouwenssignaal telt",
  ]),
  ("p", "Dat laatste punt wordt onderschat. Een verkoper die weigert een deel te "
        "laten staan, roept bij financiers de vraag op waarom niet."),

  ("h2", "Rente in 2026"),
  ("p", "De Europese Centrale Bank hield de depositorente op 23 juli 2026 "
        "ongewijzigd op 2,25 procent. Het rentepeil werkt op twee manieren door in "
        "een overname: in de maandlast van de financiering, en in het bedrag dat "
        "een koper uit dezelfde kasstroom kan lenen. Bij een hogere rente daalt dat "
        "bedrag, en daarmee de prijs die betaald kan worden."),

  ("h2", "Financiering bij een start"),
  ("p", "Bij een nieuw bedrijf ontbreekt de historie waarop een bank beoordeelt. "
        "Financiering komt dan eerder uit eigen middelen, familie, "
        "microfinanciering of crowdfunding. Dat verschil is een van de redenen dat "
        "een overname in de praktijk vaker financierbaar is dan een start, ondanks "
        "het hogere bedrag. Zie "
        "<a href=\"/starten-of-overnemen/financiering-en-risico/\">financiering en "
        "risico</a>."),

  ("h2", "Bij webshops"),
  ("p", "Webshops en e-commercebedrijven kennen weinig zekerheden: de waarde zit in "
        "goodwill, merk en klantenbestand, niet in machines. Financiering loopt "
        "daardoor vaker via een vendor loan, een earn-out of een combinatie. "
        "Toelichting op de mogelijkheden in dit segment staat op %s."
        % wo("kennisbank/financiering-webshop-overname")),
 ],
 "related": [
  ("Earn-out", "/kennisbank/earn-out/"),
  ("Financiering en risico", "/starten-of-overnemen/financiering-en-risico/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
 ],
},

{
 "path": "kennisbank/belasting/",
 "crumb": "Belasting bij overdracht",
 "title": "Belasting bij bedrijfsoverdracht: BOR en deelnemingsvrijstelling",
 "desc": "De fiscale kant van een bedrijfsoverdracht: deelnemingsvrijstelling, "
         "stakingswinst en de bedrijfsopvolgingsregeling met de wijzigingen per "
         "2025 en 2026.",
 "kicker": "Fiscaal",
 "h1": "Belasting bij overdracht",
 "lead": "Wat er netto van een verkoop overblijft, hangt sterk af van de structuur "
         "en van de vraag of er binnen of buiten de familie wordt overgedragen.",
 "blocks": [
  ("panel", "Geen fiscaal advies", [
   ("p", "Deze pagina geeft een overzicht op hoofdlijnen. De regels zijn "
         "gedetailleerd, kennen voorwaarden en veranderen regelmatig. Voor een "
         "concrete situatie is een fiscalist of accountant nodig."),
  ]),

  ("h2", "Verkoop vanuit een holding"),
  ("p", "Wordt een werkmaatschappij verkocht vanuit een holding, dan valt de winst "
        "op die verkoop onder de deelnemingsvrijstelling en blijft die op het "
        "niveau van de holding onbelast. Het geld zit dan wel in de holding: bij "
        "uitkering naar privé volgt heffing in box 2."),
  ("p", "Deze structuur moet ruim van tevoren staan. Een holding oprichten vlak "
        "voor een verkoop werkt niet, omdat er termijnen gelden waarbinnen een "
        "herstructurering niet zonder fiscale gevolgen blijft."),

  ("h2", "Verkoop van een eenmanszaak of vof"),
  ("p", "Bij het staken van een onderneming in de inkomstenbelasting wordt "
        "afgerekend over de stakingswinst: het verschil tussen de opbrengst en de "
        "boekwaarde, inclusief de goodwill en de vrijval van reserves. Er bestaan "
        "faciliteiten om die heffing te verzachten of uit te stellen, waaronder de "
        "stakingsaftrek, de mogelijkheid om een lijfrente te bedingen en, bij "
        "herinvestering, de herinvesteringsreserve."),

  ("h2", "Overdracht binnen de familie"),
  ("p", "Bij schenking of vererving van een onderneming speelt de "
        "bedrijfsopvolgingsregeling. Die maakt het mogelijk om een onderneming "
        "grotendeels vrijgesteld over te dragen, mits aan voorwaarden wordt "
        "voldaan over bezit vooraf en voortzetting achteraf."),
  ("h3", "Wijzigingen per 1 januari 2025"),
  ("tick", [
    "de vrijstelling bedraagt 100 procent van de goingconcernwaarde tot ongeveer "
    "1,5 miljoen euro, en 75 procent over het meerdere, waar dat eerder 83 procent "
    "was. Het drempelbedrag wordt jaarlijks geïndexeerd",
    "de voortzettingseis is verkort van vijf naar drie jaar",
    "er geldt een minimumleeftijd van 21 jaar bij schenking, niet bij vererving",
    "de doelmatigheidsmarge van 5 procent voor beleggingsvermogen is vervallen",
    "voor panden die zowel zakelijk als privé worden gebruikt gelden strengere "
    "regels",
  ]),
  ("h3", "Wijzigingen per 1 januari 2026"),
  ("tick", [
    "de regeling geldt alleen nog voor gewone aandelen waarbij de schenker of "
    "erflater een belang van ten minste 5 procent heeft",
    "er zijn maatregelen tegen misbruik ingevoerd, waaronder een langere bezitseis "
    "bij overdrachten door mensen die de AOW-leeftijd ruim gepasseerd zijn, en een "
    "regeling die dubbel gebruik van de vrijstelling voorkomt",
    "een herstructurering laat de bezits- en voortzettingstermijn niet meer opnieuw "
    "beginnen zolang het belang gelijk blijft",
  ]),
  ("p", "Voor ondernemers die overdracht binnen de familie overwegen, betekent dit "
        "dat het tijdpad langer is dan vaak gedacht. Bezitseis en voortzettingseis "
        "samen bestrijken meerdere jaren."),

  ("h2", "Btw en overdrachtsbelasting"),
  ("p", "De overdracht van een gehele onderneming valt onder een regeling waardoor "
        "er geen btw over de overdracht verschuldigd is, mits de koper de "
        "onderneming voortzet. Gaat het om losse goederen, dan ligt dat anders. "
        "Zit er onroerend goed in de transactie, dan komt overdrachtsbelasting in "
        "beeld, ook bij een aandelentransactie in bepaalde gevallen."),
  ("p", "Verdere uitleg over de fiscale onderwerpen rond bedrijfsoverdracht staat "
        "in de kennisbank op %s." % oa("kennisbank/belasting")),
 ],
 "related": [
  ("Activa of aandelen", "/kennisbank/activa-of-aandelen/"),
  ("Wanneer verkopen", "/verkopen/wanneer-verkopen/"),
  ("Goodwill", "/kennisbank/goodwill/"),
 ],
},

{
 "path": "kennisbank/begrippenlijst/",
 "crumb": "Begrippenlijst",
 "title": "Begrippenlijst bedrijfsovername van A tot Z",
 "desc": "Achtendertig termen uit de overnamepraktijk in gewone taal uitgelegd, "
         "van activatransactie en due diligence tot vendor loan en werkkapitaal.",
 "kicker": "Naslag",
 "h1": "Begrippenlijst",
 "lead": "De termen die in een overnametraject langskomen, alfabetisch en in "
         "gewone taal.",
 "blocks": [
  ("table", ["Term", "Betekenis"], _termen_rows()),
  ("p", "Uitgebreidere naslag staat in de woordenboeken van de twee uitgelichte "
        "platformen: %s en %s."
        % (oa("kennisbank/woordenboek"), wo("kennisbank"))),
 ],
 "related": [
  ("Kennisbank", "/kennisbank/"),
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
 ],
},
]
