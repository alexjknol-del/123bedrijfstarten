"""Gids: wanneer en hoe een bedrijf verkopen."""

from .common import OA_MERK, OA_NAKED, WO_MERK, oa, wo, YT_OA

PAGES = [

{
 "path": "verkopen/",
 "crumb": "Verkopen",
 "title": "Bedrijf verkopen: gids over timing, proces en opbrengst",
 "desc": "Wanneer een bedrijf verkopen, hoe het verkoopproces verloopt en wat de "
         "opbrengst bepaalt. Met de vijf fases van een overdracht en een "
         "uitwerking van verkoopklaar ondernemen.",
 "kicker": "Hoofdgids",
 "h1": "Bedrijf verkopen",
 "lead": "De verkoop van een onderneming is voor de meeste ondernemers een "
         "eenmalige gebeurtenis, terwijl de koper aan de andere kant van de tafel "
         "het vaker doet. Voorbereiding is het enige middel om dat verschil te "
         "verkleinen.",
 "blocks": [
  ("cards", [
   ("Wanneer verkopen",
    "Het juiste moment bepalen op basis van cijfers, leeftijd, markt en "
    "persoonlijke situatie.",
    "/verkopen/wanneer-verkopen/"),
   ("Optimaal verkopen",
    "Wat de opbrengst bepaalt, en welke voorbereidingen in de laatste twee jaar "
    "het meeste effect hebben.",
    "/verkopen/optimaal-verkopen/"),
   ("Verkoopklaar ondernemen",
    "Een bedrijf vanaf het begin zo inrichten dat het later goed verkoopbaar is.",
    "/verkopen/verkoopklaar-ondernemen/"),
   ("Vijf stappen",
    "Voorbereiden, te koop zetten, promoten, onderhandelen en overdragen.",
    "/verkopen/vijf-stappen/"),
  ]),

  ("h2", "Waarom voorbereiding het verschil maakt"),
  ("p", "Uit de Overname Barometer van Brookz en Dealsuite blijkt dat 30 procent "
        "van de MKB-trajecten inmiddels langer dan een jaar duurt. Dat is niet "
        "alleen een gevolg van de markt: trajecten lopen vertraging op doordat "
        "cijfers ontbreken, contracten niet op orde zijn of het bedrijf te sterk "
        "aan de eigenaar hangt."),
  ("p", "Datzelfde onderzoek laat zien dat verkopers jonger worden. De gemiddelde "
        "leeftijd van verkopende ondernemers daalde van 59 jaar in 2015 naar 54 "
        "jaar in 2025. Verkopen is minder vaak het sluitstuk van een loopbaan en "
        "vaker een bewuste stap halverwege."),

  ("h2", "De opbrengst zit in vier dingen"),
  ("steps", [
   ("Aantoonbare winst",
    "Genormaliseerde cijfers over meerdere jaren, met een toelichting op eenmalige "
    "posten. Wat niet te onderbouwen is, telt een koper niet mee."),
   ("Beperkte afhankelijkheid",
    "Van de eigenaar, van een grote klant, van een leverancier of van een enkel "
    "product. Elke afhankelijkheid kost direct in de prijs."),
   ("Een geloofwaardige toekomst",
    "Een koper betaalt voor wat er na de overdracht gebeurt. Een onderbouwd beeld "
    "van de komende jaren telt zwaarder dan een terugblik."),
   ("Het aantal serieuze gegadigden",
    "Een proces met meerdere kandidaten levert een andere prijs op dan een gesprek "
    "met een enkele geinteresseerde die zich meldde."),
  ]),

  ("h2", "Waar bedrijven te koop worden gezet"),
  ("p", "Voor het MKB verloopt een verkoop meestal via een overnameplatform, een "
        "adviseur of een combinatie van beide. %s richt zich op bedrijven in het "
        "algemeen en licht de werkwijze toe op %s. %s richt zich op webshops, "
        "e-commercemerken en marketplace-accounts, met een toelichting op %s."
        % (OA_MERK, oa("hoe-werkt-het/mijn-bedrijf-verkopen"),
           WO_MERK, wo("onze-diensten/webshop-verkopen"))),

  ("video", YT_OA, "Video's van het kanaal Overnameadvies",
   "Uitleg over waardering, verkoopproces en onderhandeling, van het YouTube-"
   "kanaal Overnameadvies."),

  ("h2", "Veelgestelde vragen"),
  ("h3", "Hoe lang duurt een verkooptraject"),
  ("p", "In het MKB is zes tot twaalf maanden gebruikelijk, gerekend vanaf het "
        "moment dat het bedrijf te koop staat. Bij 30 procent van de trajecten "
        "duurt het langer dan een jaar. Voorbereiding vooraf, waaronder het op orde "
        "brengen van cijfers en contracten, kost daarnaast al snel enkele maanden."),
  ("h3", "Kan een bedrijf anoniem te koop staan"),
  ("p", "Ja. In de praktijk wordt een profiel geplaatst zonder naam en zonder "
        "herleidbare gegevens, en krijgen gegadigden pas details na ondertekening "
        "van een geheimhoudingsverklaring. Zie "
        "<a href=\"/kennisbank/nda/\">geheimhoudingsverklaring</a>."),
  ("h3", "Wat als een koper zich rechtstreeks meldt"),
  ("p", "Dat gebeurt regelmatig. Direct in gesprek gaan zonder voorbereiding is "
        "zelden verstandig, omdat de eerste indruk en de eerste genoemde bedragen "
        "de rest van het traject sturen. Gebruikelijk is om de interesse te "
        "bevestigen en een afspraak in te plannen nadat de eigen cijfers en de "
        "waardering op orde zijn."),
  ("h3", "Wat als het bedrijf niet verkocht wordt"),
  ("p", "Dan blijft de eigenaar achter met een bedrijf dat wel is doorgelicht en "
        "opgeschoond. In de praktijk wordt een opdracht aan een adviseur voor een "
        "bepaalde periode gegeven, vaak twaalf maanden, waarna beide partijen vrij "
        "zijn. De voorbereiding zelf gaat niet verloren."),
 ],
 "related": [
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Belasting bij overdracht", "/kennisbank/belasting/"),
  ("Begrippenlijst", "/kennisbank/begrippenlijst/"),
 ],
},

# ------------------------------------------------------------ wanneer
{
 "path": "verkopen/wanneer-verkopen/",
 "crumb": "Wanneer verkopen",
 "title": "Wanneer is het juiste moment om een bedrijf te verkopen",
 "desc": "Timing van een bedrijfsverkoop: de invloed van cijfers, leeftijd, markt "
         "en rente, en de signalen dat het moment gekomen is of juist nog niet.",
 "kicker": "Timing",
 "h1": "Wanneer verkopen",
 "lead": "Het beste moment om te verkopen valt zelden samen met het moment waarop "
         "de ondernemer eraan toe is. Wie beide op elkaar wil laten aansluiten, "
         "begint een paar jaar eerder.",
 "blocks": [
  ("h2", "Drie klokken die niet gelijk lopen"),
  ("table",
   ["Klok", "Wat die bepaalt"],
   [
    ["De bedrijfsklok", "Groei, marge, contracten en investeringen. Verkopen op "
     "een piek levert meer op dan verkopen na twee mindere jaren."],
    ["De persoonlijke klok", "Leeftijd, energie, gezondheid en de vraag wat er na "
     "de verkoop komt. Wie geen beeld heeft van daarna, stelt de beslissing uit."],
    ["De marktklok", "Rente, kredietruimte, sectorontwikkeling en het aantal "
     "kopers dat actief zoekt."],
   ]),
  ("p", "Deze drie lopen bijna nooit gelijk. De praktische vraag is dan ook niet "
        "wanneer het perfecte moment is, maar wanneer de drie dicht genoeg bij "
        "elkaar liggen."),

  ("h2", "Signalen dat het moment nadert"),
  ("tick", [
    "de omzet groeit al twee tot drie jaar, met een marge die stabiel of stijgend is",
    "het bedrijf draait grotendeels zonder dagelijkse bemoeienis van de eigenaar",
    "de belangrijkste contracten zijn recent verlengd",
    "er staat geen grote investering voor de deur die de koper meteen moet doen",
    "de ondernemer merkt dat de energie voor de volgende groeistap ontbreekt",
  ]),

  ("h2", "Signalen om nog even te wachten"),
  ("tick", [
    "de laatste jaarcijfers zijn vertekend door eenmalige posten",
    "een grote klant heeft opgezegd of staat op het punt dat te doen",
    "de administratie loopt achter of is niet controleerbaar",
    "er loopt een geschil dat eerst afgerond moet worden",
    "de eigenaar is nog onmisbaar in verkoop of uitvoering",
  ]),
  ("p", "Elk van deze punten is binnen een tot twee jaar te repareren. Wat er dan "
        "gedaan moet worden staat op "
        "<a href=\"/verkopen/optimaal-verkopen/\">optimaal verkopen</a>."),

  ("h2", "De markt in 2026"),
  ("p", "De Europese Centrale Bank hield de depositorente op 23 juli 2026 "
        "ongewijzigd op 2,25 procent. Voor overnames telt vooral wat een koper met "
        "die rente kan financieren: naarmate geld duurder is, daalt het bedrag dat "
        "uit dezelfde kasstroom te betalen valt."),
  ("p", "Aan de aanbodkant komt er de komende jaren veel op de markt. Uit onderzoek "
        "van Ipsos I&O voor ABN AMRO, gepubliceerd in februari 2026, blijkt dat "
        "ruim twee derde van de ondernemers binnen tien jaar wil stoppen, terwijl "
        "22 procent geen concrete opvolgingsplannen heeft. Meer aanbod betekent meer "
        "concurrentie tussen verkopers, en daarmee een groter verschil tussen goed "
        "en slecht voorbereide bedrijven."),

  ("h2", "Verkopen in fases"),
  ("p", "Een verkoop hoeft geen alles-of-nietsmoment te zijn. In het MKB komen drie "
        "tussenvormen regelmatig voor."),
  ("steps", [
   ("Gedeeltelijke verkoop",
    "Een deel van de aandelen gaat over, de ondernemer blijft betrokken en verkoopt "
    "de rest later. Vaak in combinatie met een investeerder."),
   ("Verkoop aan personeel of medeaandeelhouder",
    "Een management buy-out. De koper kent het bedrijf, wat het boekenonderzoek "
    "verkort, maar de financiering is meestal het knelpunt."),
   ("Overdracht binnen de familie",
    "Fiscaal anders geregeld dan een verkoop aan een derde. De "
    "bedrijfsopvolgingsregeling speelt daarbij een grote rol, zie "
    "<a href=\"/kennisbank/belasting/\">belasting bij overdracht</a>."),
  ]),

  ("h2", "Beginnen met de voorbereiding"),
  ("p", "Wie over twee jaar wil verkopen, begint nu. Cijfers over drie boekjaren "
        "wegen mee, en juist die drie jaren zijn te beinvloeden. De pagina "
        "<a href=\"/verkopen/verkoopklaar-ondernemen/\">verkoopklaar ondernemen</a> "
        "gaat over het inrichten van een bedrijf met de verkoop als uitgangspunt."),
  ("p", "Een vrijblijvend gesprek over de haalbaarheid en de waarde is bij de "
        "meeste adviesbureaus onderdeel van de intake. Voor bedrijven in het "
        "algemeen loopt dat via %s, voor webshops via %s."
        % (OA_NAKED, wo("onze-diensten/hoe-werkt-het"))),
 ],
 "related": [
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
  ("Belasting bij overdracht", "/kennisbank/belasting/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
 ],
},

# ------------------------------------------------------------ optimaal
{
 "path": "verkopen/optimaal-verkopen/",
 "crumb": "Optimaal verkopen",
 "title": "Optimaal verkopen: zo wordt de opbrengst hoger",
 "desc": "Stappen die de verkoopopbrengst van een bedrijf verhogen: normaliseren, "
         "afhankelijkheden afbouwen, contracten vastleggen en het proces met "
         "meerdere kandidaten inrichten.",
 "kicker": "Opbrengst",
 "h1": "Optimaal verkopen",
 "lead": "De prijs van een bedrijf wordt maar deels bepaald door de winst. Het "
         "andere deel zit in risico, en risico is te verlagen.",
 "blocks": [
  ("h2", "Twee jaar voor de verkoop"),
  ("steps", [
   ("Normaliseer de cijfers",
    "Haal privéposten uit de boekhouding, breng eenmalige kosten en opbrengsten in "
    "kaart en reken met een marktconform loon voor de eigenaar. Een koper doet dit "
    "toch, en doet het in zijn eigen voordeel als de verkoper het niet heeft "
    "voorbereid."),
   ("Bouw de afhankelijkheid van de eigenaar af",
    "Draag klantcontacten over, leg werkwijzen vast en zorg dat er iemand anders "
    "is die het bedrijf een maand kan draaien. Dit is de maatregel met het "
    "grootste effect op de prijs, en de maatregel die de meeste tijd kost."),
   ("Leg contracten vast",
    "Mondelinge afspraken met klanten en leveranciers hebben in een "
    "boekenonderzoek geen waarde. Verlengingen die vlak voor de verkoop rondkomen "
    "tellen wel mee."),
   ("Ruim de balans op",
    "Overtollige voorraad, oninbare debiteuren, ongebruikte bedrijfsmiddelen en "
    "privébezit dat in de bv zit. Elke post die niet bij het bedrijf hoort, roept "
    "vragen op."),
   ("Zorg voor een investeringsplan",
    "Een koper die direct grote vervangingsinvesteringen ziet aankomen, trekt die "
    "van de prijs af. Recent onderhoud werkt de andere kant op."),
  ]),

  ("h2", "In het jaar van de verkoop"),
  ("tick", [
    "een verkoopmemorandum dat het bedrijf feitelijk en compleet beschrijft",
    "een dossier met cijfers, contracten en vergunningen dat direct te delen is",
    "een onderbouwde prognose voor de komende drie jaar",
    "een lijst met kandidaten die breder is dan de partijen die zich vanzelf melden",
    "duidelijkheid over de rol van de verkoper na de overdracht",
  ]),

  ("h2", "Waarom meerdere kandidaten uitmaken"),
  ("p", "Een verkoop aan de enige gegadigde is geen onderhandeling maar een "
        "gesprek over de voorwaarden van die ene partij. Met meerdere serieuze "
        "kandidaten verandert de dynamiek: niet alleen de prijs, ook de "
        "voorwaarden rond garanties, betaaltermijn en de rol van de verkoper na de "
        "overdracht."),
  ("p", "Dat is de reden dat MKB-verkopen doorgaans niet via één gesprek lopen, "
        "maar via een proces met een profiel, een geheimhoudingsverklaring, een "
        "memorandum en een vaste termijn voor indicatieve biedingen."),

  ("h2", "Wat kopers van de prijs afhalen"),
  ("table",
   ["Bevinding in het boekenonderzoek", "Gebruikelijk gevolg"],
   [
    ["Winst die deels uit eenmalige posten bestaat", "Correctie op de winst, en "
     "daarmee op de hele multiple"],
    ["Klant met meer dan dertig procent van de omzet", "Lagere multiple of een "
     "earn-out die aan die klant gekoppeld is"],
    ["Achterstallig onderhoud", "Directe aftrek van de geschatte kosten"],
    ["Personeelsdossiers niet op orde", "Vrijwaring in het contract en soms een "
     "hoger deel in escrow"],
    ["Eigenaar is onmisbaar", "Langere overdrachtsperiode en een groter deel van "
     "de prijs afhankelijk van resultaten"],
   ]),

  ("h2", "Fiscale voorbereiding"),
  ("p", "De structuur bepaalt wat er netto overblijft. Een verkoop van aandelen "
        "vanuit een holding verloopt fiscaal anders dan een verkoop van activa uit "
        "een eenmanszaak, en een overdracht binnen de familie kent eigen regels. "
        "Herstructureren vlak voor een verkoop is meestal te laat, omdat er "
        "wachttermijnen gelden. Meer daarover op "
        "<a href=\"/kennisbank/belasting/\">belasting bij overdracht</a> en "
        "<a href=\"/kennisbank/activa-of-aandelen/\">activa of aandelen</a>."),

  ("h2", "Begeleiding"),
  ("p", "Een adviseur verdient zich in het MKB meestal terug in de voorwaarden, "
        "niet alleen in de prijs. De werkwijze en tarieven van %s staan op %s. Voor "
        "webshops en e-commercebedrijven staat de vergelijkbare uitleg op %s."
        % (OA_MERK, oa("hoe-werkt-het/tarieven"), wo("onze-diensten/tarieven"))),
 ],
 "related": [
  ("Verkoopklaar ondernemen", "/verkopen/verkoopklaar-ondernemen/"),
  ("Vijf stappen", "/verkopen/vijf-stappen/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Earn-out", "/kennisbank/earn-out/"),
 ],
},

# ------------------------------------------------------------ verkoopklaar
{
 "path": "verkopen/verkoopklaar-ondernemen/",
 "crumb": "Verkoopklaar ondernemen",
 "title": "Verkoopklaar ondernemen: bouwen aan een verkoopbaar bedrijf",
 "desc": "Een onderneming vanaf de start zo inrichten dat die later voor een goede "
         "prijs over te dragen is: structuur, contracten, processen en de rol van "
         "de eigenaar.",
 "kicker": "Lange termijn",
 "h1": "Verkoopklaar ondernemen",
 "lead": "De meeste ondernemers denken pas aan verkopen als het zover is. De "
         "beslissingen die de verkoopbaarheid bepalen worden echter in de eerste "
         "jaren genomen.",
 "blocks": [
  ("h2", "Het uitgangspunt"),
  ("p", "Een bedrijf dat is opgebouwd rond de persoon van de eigenaar levert bij "
        "verkoop weinig op, hoe goed het ook draait. Een bedrijf dat is opgebouwd "
        "rond processen, contracten en mensen levert bij dezelfde winst een hoger "
        "bedrag op. Dat verschil ontstaat niet in het laatste jaar."),
  ("p", "Verkoopklaar ondernemen betekent niet dat een verkoop het doel is. Het "
        "betekent dat de keuzes die een bedrijf overdraagbaar maken samenvallen met "
        "de keuzes die het bedrijf robuuster maken: minder afhankelijk van één "
        "persoon, minder afhankelijk van één klant, beter vastgelegd."),

  ("h2", "Zes keuzes met effect op de lange termijn"),
  ("steps", [
   ("De rechtsvorm",
    "Een bv is over te dragen als aandelenpakket, een eenmanszaak alleen als "
    "verzameling activa. Dat verschil raakt zowel de fiscaliteit als de "
    "aantrekkelijkheid voor kopers. Een holdingstructuur maakt een latere verkoop "
    "fiscaal eenvoudiger, maar moet ruim van tevoren staan."),
   ("De naam en het merk",
    "Een bedrijfsnaam die de eigen achternaam is, gaat lastiger over dan een "
    "zelfstandige merknaam. Merkregistratie en eigendom van de domeinnaam horen "
    "bij de onderneming, niet bij de privépersoon."),
   ("De contracten",
    "Klantafspraken, leveranciersvoorwaarden, huur en licenties op naam van de "
    "onderneming, met een looptijd en een overdraagbaarheidsclausule die een "
    "overname niet blokkeert."),
   ("De administratie",
    "Een boekhouding die maandelijks klopt levert bij een verkoop maanden "
    "tijdwinst op, en voorkomt dat een koper een korting bedingt voor "
    "onzekerheid."),
   ("De rol van de eigenaar",
    "Wie zelf de belangrijkste verkoper, vakman of relatiebeheerder blijft, bouwt "
    "een baan op in plaats van een bedrijf. Taken overdragen kost omzet op korte "
    "termijn en levert waarde op lange termijn."),
   ("De spreiding van klanten",
    "Eén grote klant is comfortabel en gevaarlijk tegelijk. Een gespreid "
    "klantenbestand met terugkerende omzet is de meest waardevolle vorm van "
    "omzet die er is."),
  ]),

  ("h2", "Wat een koper drie jaar later ziet"),
  ("table",
   ["", "Bedrijf zonder voorbereiding", "Verkoopklaar bedrijf"],
   [
    ["Cijfers", "Jaarrekening met privéposten erin", "Genormaliseerde cijfers over "
     "drie jaar met toelichting"],
    ["Klanten", "Mondelinge afspraken, één dominante klant", "Contracten met "
     "looptijd, gespreid bestand"],
    ["Kennis", "In het hoofd van de eigenaar", "Vastgelegd in processen en systemen"],
    ["Personeel", "Afhankelijk van de eigenaar", "Zelfstandig werkend team"],
    ["Overdracht", "Lange periode nodig, hoge earn-out", "Korte periode, groter "
     "deel bij levering betaald"],
   ]),

  ("h2", "Voor webshops en e-commerce"),
  ("p", "Bij een webshop komt daar een aantal specifieke punten bij: eigendom van "
        "de domeinnaam en de merknaam, toegang tot advertentie- en analytics-"
        "accounts op naam van het bedrijf, een klantenbestand dat volgens de regels "
        "is opgebouwd, en verkeer dat niet volledig van één kanaal afhangt. Die "
        "punten staan uitgewerkt in de "
        "<a href=\"/checklists/webshop-overnemen/\">checklist webshop overnemen</a>, "
        "die aan de koperskant precies hetzelfde onderzoekt."),
  ("p", "Wat dat voor de waarde betekent is te zien in de "
        "<a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool voor webshops</a>: "
        "dezelfde winst levert bij overwegend organisch verkeer een aanzienlijk "
        "hogere uitkomst op dan bij overwegend ingekocht verkeer."),

  ("h2", "Beginnen bij het begin"),
  ("p", "Voor wie nu start: de "
        "<a href=\"/checklists/bedrijf-beginnen/\">checklist bedrijf beginnen</a> "
        "en de <a href=\"/checklists/webshop-beginnen/\">checklist webshop "
        "beginnen</a> bevatten de keuzes die later het zwaarst wegen. Voor wie een "
        "bestaand bedrijf overweegt te kopen geldt de omgekeerde blik: precies "
        "deze punten bepalen of een overnamekandidaat de vraagprijs waard is."),
 ],
 "related": [
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
  ("Checklist bedrijf beginnen", "/checklists/bedrijf-beginnen/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Activa of aandelen", "/kennisbank/activa-of-aandelen/"),
 ],
},

# ------------------------------------------------------------ vijf stappen
{
 "path": "verkopen/vijf-stappen/",
 "crumb": "Vijf stappen",
 "title": "Het verkoopproces in vijf stappen",
 "desc": "Voorbereiden, te koop zetten, promoten, onderhandelen en overdragen: de "
         "vijf fases van een bedrijfsverkoop, met per fase de documenten en de "
         "doorlooptijd.",
 "kicker": "Proces",
 "h1": "Het verkoopproces in vijf stappen",
 "lead": "Vrijwel elke bedrijfsoverdracht doorloopt dezelfde vijf fases. De "
         "doorlooptijd verschilt, de volgorde niet.",
 "blocks": [
  ("steps", [
   ("Voorbereiden",
    "Waardebepaling, normalisatie van de cijfers, opschonen van de balans en het "
    "opstellen van een verkoopmemorandum. In deze fase wordt ook bepaald wat er "
    "precies verkocht wordt: aandelen of activa. Doorlooptijd: één tot zes "
    "maanden, afhankelijk van de staat van de administratie."),
   ("Te koop zetten",
    "Een anoniem profiel op de relevante platformen, aangevuld met een lijst van "
    "partijen die gericht benaderd worden. Geinteresseerden tekenen eerst een "
    "geheimhoudingsverklaring voordat er cijfers gedeeld worden. Doorlooptijd: "
    "doorlopend."),
   ("Promoten",
    "Actief benaderen van kandidaten, gesprekken voeren en het bedrijf toelichten. "
    "Doel is meerdere serieuze gegadigden tegelijk in het proces te hebben, met "
    "een gelijke informatiepositie. Doorlooptijd: één tot zes maanden."),
   ("Onderhandelen",
    "Indicatieve biedingen, selectie van een kandidaat, intentieverklaring en "
    "boekenonderzoek. In deze fase worden prijs, structuur, garanties en de rol "
    "van de verkoper na de overdracht vastgelegd. Doorlooptijd: twee tot vier "
    "maanden."),
   ("Overdragen",
    "Koopovereenkomst, notariële levering bij een aandelentransactie, "
    "financiering rond en de feitelijke overdracht van klanten, personeel en "
    "systemen. Daarna volgt de afgesproken overdrachtsperiode. Doorlooptijd: "
    "enkele weken tot enkele maanden."),
  ]),

  ("h2", "Documenten per fase"),
  ("table",
   ["Fase", "Belangrijkste documenten"],
   [
    ["Voorbereiden", "Waardebepaling, genormaliseerde cijfers, verkoopmemorandum"],
    ["Te koop zetten", "Anoniem profiel, geheimhoudingsverklaring"],
    ["Promoten", "Informatiememorandum, prognose, vragenlijsten"],
    ["Onderhandelen", "Indicatief bod, intentieverklaring, due diligence-rapport"],
    ["Overdragen", "Koopovereenkomst, akte van levering, overdrachtsdocument"],
   ]),
  ("p", "De begrippen uit deze tabel staan toegelicht in de "
        "<a href=\"/kennisbank/begrippenlijst/\">begrippenlijst</a>."),

  ("h2", "Waar trajecten vastlopen"),
  ("tick", [
    "<b>Bij de cijfers.</b> Als het boekenonderzoek een ander beeld geeft dan het "
    "memorandum, staat de prijs opnieuw ter discussie.",
    "<b>Bij de financiering.</b> Een koper die de financiering niet rondkrijgt, "
    "kost het traject maanden. Toetsen vooraf voorkomt dat.",
    "<b>Bij de garanties.</b> Verkopers onderschatten hoe lang zij nog aansprakelijk "
    "blijven, kopers vragen meer dan gebruikelijk is.",
    "<b>Bij de rol na de overdracht.</b> Verwachtingen over de betrokkenheid van de "
    "verkoper lopen vaak uiteen en worden te laat besproken.",
  ]),

  ("h2", "Na de overdracht"),
  ("p", "De laatste fase eindigt niet bij de notaris. Er volgt een periode waarin "
        "de verkoper beschikbaar blijft voor vragen, klanten en personeel. Hoe lang "
        "die periode duurt en wat daar tegenover staat, hoort in de "
        "koopovereenkomst te staan, inclusief een einddatum."),
  ("p", "Wanneer een deel van de prijs afhankelijk is van resultaten na de "
        "overdracht, blijft ook de betaling doorlopen. Hoe dat werkt staat op "
        "<a href=\"/kennisbank/earn-out/\">earn-out</a>."),
  ("p", "Een uitgewerkte beschrijving van het stappenplan door een adviesbureau "
        "staat op %s. Voor webshops staat de vergelijkbare uitleg op %s."
        % (oa("stappenplan"), wo("kennisbank/bedrijf-verkopen-5-stappen"))),
 ],
 "related": [
  ("Intentieverklaring", "/kennisbank/intentieverklaring/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Geheimhoudingsverklaring", "/kennisbank/nda/"),
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
 ],
},
]
