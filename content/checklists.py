"""Checklists voor beginnen en overnemen."""

from .common import OA_MERK, WO_MERK, WO_NAKED, oa, wo, YT_WO

PAGES = [

{
 "path": "checklists/",
 "crumb": "Checklists",
 "title": "Checklists: bedrijf of webshop beginnen en overnemen",
 "desc": "Vier uitgewerkte checklists voor het beginnen en overnemen van een "
         "bedrijf of webshop, van eerste idee tot de eerste honderd dagen na de "
         "overdracht.",
 "kicker": "Checklists",
 "h1": "Checklists",
 "lead": "Vier lijsten die stap voor stap door de uitvoering lopen. Twee voor wie "
         "zelf begint, twee voor wie iets bestaands koopt.",
 "blocks": [
  ("cards", [
   ("Bedrijf beginnen",
    "Van idee en marktonderzoek tot rechtsvorm, administratie, verzekeringen en "
    "de eerste klanten.",
    "/checklists/bedrijf-beginnen/"),
   ("Webshop beginnen",
    "Niche, platform, voorraad, betaalmethoden, juridische verplichtingen en de "
    "marketing die de shop op gang brengt.",
    "/checklists/webshop-beginnen/"),
   ("Bedrijf overnemen",
    "Zoekprofiel, eerste gesprek, waardering, intentieverklaring, boekenonderzoek "
    "en overdracht.",
    "/checklists/bedrijf-overnemen/"),
   ("Webshop overnemen",
    "Wat er bij een webshop extra gecontroleerd moet worden: verkeer, "
    "afhankelijkheden, techniek, accounts en klantdata.",
    "/checklists/webshop-overnemen/"),
  ]),
  ("h2", "Hoe deze lijsten bedoeld zijn"),
  ("p", "Een checklist vervangt geen advies en geen boekenonderzoek. De lijsten "
        "hieronder zijn bedoeld om de volgorde vast te houden en te voorkomen dat "
        "grote posten pas laat in beeld komen. Wie een concreet traject ingaat "
        "combineert ze met een accountant, een jurist en, bij een overname van "
        "enige omvang, een overnameadviseur."),
  ("h2", "Volgorde die in de praktijk werkt"),
  ("steps", [
   ("Eerst rekenen, dan bouwen",
    "Zowel bij een start als bij een overname is de eerste stap een som: wat kost "
    "het, wat levert het op, hoe lang duurt het voordat er inkomen is."),
   ("Dan de structuur",
    "Rechtsvorm, financiering en contracten bepalen wat er later nog mogelijk is. "
    "Achteraf veranderen kost geld en tijd."),
   ("Dan pas de uitvoering",
    "Inrichting, website, voorraad en marketing volgen op de keuzes daarboven, "
    "niet andersom."),
  ]),
 ],
 "related": [
  ("Starten of overnemen", "/starten-of-overnemen/"),
  ("Rekentools", "/tools/"),
  ("Kennisbank", "/kennisbank/"),
 ],
},

# ------------------------------------------------------------ bedrijf beginnen
{
 "path": "checklists/bedrijf-beginnen/",
 "crumb": "Bedrijf beginnen",
 "title": "Checklist: zelf een bedrijf beginnen in twaalf stappen",
 "desc": "Checklist voor het starten van een eigen bedrijf: idee, marktonderzoek, "
         "ondernemingsplan, rechtsvorm, inschrijving, administratie, prijzen en de "
         "eerste klanten.",
 "kicker": "Checklist",
 "h1": "Checklist bedrijf beginnen",
 "lead": "Twaalf stappen van eerste idee tot draaiend bedrijf, in de volgorde "
         "waarin ze het minste geld en de minste tijd kosten.",
 "blocks": [
  ("steps", [
   ("Scherp het idee aan",
    "Een bedrijfsidee wordt pas concreet bij drie antwoorden: welk probleem het "
    "oplost, voor wie precies, en waarom die groep daarvoor zou betalen. Een idee "
    "dat in twee zinnen uit te leggen is, is verkoopbaar. Een idee dat een alinea "
    "nodig heeft nog niet."),
   ("Onderzoek de markt",
    "Breng vraag en aanbod in kaart. Wie levert dit nu, tegen welke prijs, en wat "
    "zeggen klanten daarover. Zoekwoorden opzoeken, concurrenten doorlopen en "
    "tien gesprekken voeren met potentiele klanten levert meer op dan een rapport "
    "van honderd pagina's."),
   ("Reken het model door",
    "Omzet per klant, aantal klanten per maand, inkoop, vaste lasten en het eigen "
    "inkomen. Het punt waarop de omzet de kosten dekt is het belangrijkste getal "
    "van het hele plan."),
   ("Schrijf een ondernemingsplan",
    "Niet voor de bank alleen, maar als toetssteen voor latere beslissingen. Een "
    "sterkte-zwakteanalyse dwingt tot het benoemen van wat er mis kan gaan."),
   ("Kies de rechtsvorm",
    "Eenmanszaak, vof of bv. De keuze raakt aansprakelijkheid, belasting en de "
    "verkoopbaarheid van het bedrijf op langere termijn. Een bv is later te "
    "verkopen als aandelenpakket, een eenmanszaak alleen als activa."),
   ("Schrijf in bij het Handelsregister",
    "Inschrijving bij KVK levert een KVK-nummer op en, via de Belastingdienst, een "
    "btw-identificatienummer. Reserveer tegelijk de domeinnaam en de belangrijkste "
    "socialemediakanalen."),
   ("Regel de administratie",
    "Een zakelijke rekening, boekhoudsoftware en een vast moment per week. "
    "Administratie die achterloopt kost bij een latere verkoop direct waarde, "
    "omdat een koper cijfers wil zien die kloppen."),
   ("Dek de risico's af",
    "Aansprakelijkheidsverzekering, rechtsbijstand, arbeidsongeschiktheid en, waar "
    "van toepassing, beroepsaansprakelijkheid. Ook algemene voorwaarden horen in "
    "deze stap."),
   ("Bepaal de prijs",
    "Prijs volgt uit positionering, niet uit de kostprijs alleen. Te laag "
    "beginnen is later moeilijk te herstellen, omdat bestaande klanten aan het "
    "oude tarief gewend zijn."),
   ("Bouw de vindbaarheid",
    "Een website die uitlegt wat het bedrijf doet en voor wie, plus de kanalen "
    "waar de doelgroep werkelijk zit. Een profiel op elk platform kost tijd zonder "
    "resultaat."),
   ("Haal de eerste klanten binnen",
    "Het eigen netwerk levert bij vrijwel elk nieuw bedrijf de eerste opdrachten. "
    "Vraag na elke opdracht om een review en om een introductie."),
   ("Meet en stuur bij",
    "Omzet per kanaal, marge per product of dienst, en de tijd die aan niet-"
    "declarabele zaken opgaat. Wie dat drie maanden bijhoudt, weet waar het geld "
    "verdiend wordt."),
  ]),

  ("h2", "Wat vaak vergeten wordt"),
  ("tick", [
    "<b>Werkkapitaal.</b> Klanten betalen later dan leveranciers. Dat gat moet "
    "overbrugd worden, ook bij een winstgevend bedrijf.",
    "<b>Belasting.</b> Btw en inkomstenbelasting apart zetten op een tweede "
    "rekening voorkomt een vervelende verrassing in het tweede jaar.",
    "<b>Pensioen.</b> Er is geen werkgever meer die dit regelt.",
    "<b>De exit.</b> De rechtsvorm, de contracten en de mate waarin het bedrijf "
    "van de oprichter afhangt bepalen wat het bedrijf over tien jaar waard is. "
    "Zie <a href=\"/verkopen/verkoopklaar-ondernemen/\">verkoopklaar ondernemen</a>.",
  ]),

  ("h2", "Vergelijken met de overnameroute"),
  ("p", "Voordat de eerste euro geinvesteerd wordt is het de moeite waard om te "
        "kijken wat er in dezelfde branche te koop staat. Een bestaand bedrijf met "
        "klanten en omzet verandert de rekensom volledig. Het aanbod staat op %s, "
        "webshops en e-commercebedrijven op %s."
        % (oa("bedrijven-te-koop"), wo("bedrijven-te-koop"))),
  ("p", "De vergelijking tussen beide routes staat uitgewerkt in "
        "<a href=\"/starten-of-overnemen/kosten-vergelijken/\">kosten vergelijken</a>."),
 ],
 "related": [
  ("Checklist webshop beginnen", "/checklists/webshop-beginnen/"),
  ("Checklist bedrijf overnemen", "/checklists/bedrijf-overnemen/"),
  ("Verkoopklaar ondernemen", "/verkopen/verkoopklaar-ondernemen/"),
  ("Kosten vergelijken", "/starten-of-overnemen/kosten-vergelijken/"),
 ],
},

# ------------------------------------------------------------ webshop beginnen
{
 "path": "checklists/webshop-beginnen/",
 "crumb": "Webshop beginnen",
 "title": "Checklist: een webshop beginnen in tien stappen",
 "desc": "Van niche en marktonderzoek tot platformkeuze, voorraad, betaalmethoden, "
         "juridische verplichtingen en marketing. Met de cijfers over de "
         "Nederlandse e-commercemarkt in 2025.",
 "kicker": "Checklist",
 "h1": "Checklist webshop beginnen",
 "lead": "Een webshop opzetten is technisch eenvoudiger geworden en commercieel "
         "moeilijker. De techniek kost een paar honderd euro per jaar, bezoekers "
         "krijgen kost het meeste.",
 "blocks": [
  ("h2", "De markt in cijfers"),
  ("p", "Nederlandse consumenten besteedden in 2025 volgens de Thuiswinkel Markt "
        "Monitor 35,7 miljard euro online, 1 procent minder dan in 2024. Daarbinnen "
        "groeiden de bestedingen aan producten met 2 procent, terwijl die aan "
        "diensten met 5 procent daalden. Het aantal online aankopen bleef vrijwel "
        "gelijk op 347 miljoen."),
  ("p", "Een groeiende markt op productniveau, dus, maar geen markt waarin de vraag "
        "vanzelf toeneemt. Elk plan dat op autonome groei rekent, rekent te "
        "optimistisch."),

  ("steps", [
   ("Kies een niche",
    "Een afgebakende doelgroep verkoopt beter dan een breed assortiment. Kennis van "
    "het onderwerp helpt bij inkoop, bij teksten en bij de vraag welke klant welk "
    "product nodig heeft."),
   ("Onderzoek de markt",
    "Zoekvolume op de belangrijkste zoektermen, het aantal concurrenten dat er al "
    "staat en de prijzen die zij voeren. Een niche zonder zoekvolume vraagt een "
    "volledig ander marketingplan dan een niche waar mensen actief zoeken."),
   ("Maak een ondernemingsplan",
    "Inclusief de vraag hoeveel een bezoeker mag kosten. Bij een gemiddelde "
    "orderwaarde van 45 euro en een marge van 40 procent is er 18 euro per order "
    "beschikbaar voor alle kosten samen, inclusief advertenties."),
   ("Kies een platform",
    "Gehost of zelf beheerd, dat is de eerste keuze. Gehoste platformen kosten een "
    "maandbedrag en nemen onderhoud en beveiliging over. Zelf beheerde software "
    "geeft meer vrijheid en vraagt meer technisch onderhoud. Kosten, koppelingen "
    "met boekhouding en verzending, en de mogelijkheid om later te verhuizen "
    "wegen zwaarder dan de vormgeving."),
   ("Bouw de shop",
    "Snelle laadtijden, een werkbaar mobiel scherm en een afrekenproces met zo "
    "min mogelijk stappen. Productfoto's en teksten bepalen de conversie meer dan "
    "het thema."),
   ("Regel de juridische kant",
    "Algemene voorwaarden, privacyverklaring, cookiemelding, het herroepingsrecht "
    "van veertien dagen, duidelijke verzendkosten en de wettelijke informatie over "
    "het bedrijf. Deze punten zijn niet optioneel en worden actief gecontroleerd."),
   ("Regel voorraad en logistiek",
    "Zelf opslaan, uitbesteden aan een fulfilmentpartij of dropshipping. Elke keuze "
    "raakt marge, levertijd en de mate waarin de shop grip houdt op de "
    "klantervaring. Levertijden die niet gehaald worden kosten reviews."),
   ("Bepaal prijs en betaalmethoden",
    "Concurreren op prijs werkt alleen bij lage kosten en volume. Voor de "
    "betaalmix geldt: iDEAL is in Nederland onmisbaar, creditcard en achteraf "
    "betalen verhogen de conversie in specifieke doelgroepen."),
   ("Zet de marketing op",
    "Zoekmachineoptimalisatie voor de lange termijn, advertenties voor de eerste "
    "omzet, e-mail voor herhaalaankopen. Het duurste verkeer is verkeer dat "
    "eenmalig koopt."),
   ("Meet en optimaliseer",
    "Conversie per bron, gemiddelde orderwaarde, retourpercentage en de kosten per "
    "order. Zonder die vier cijfers is elke optimalisatie een gok."),
  ]),

  ("h2", "De snellere route: een bestaande webshop overnemen"),
  ("p", "Wat bij een nieuwe webshop het langst duurt en het meest kost, is precies "
        "wat bij een overname wordt meegekocht: bezoekers, een klantenbestand, "
        "reviews, leveranciersafspraken en een positie in zoekresultaten. Voor "
        "wie de niche belangrijker vindt dan het bouwen zelf, is dat een serieuze "
        "afweging."),
  ("tick", [
    "directe toegang tot een bestaande klantgroep en marktpositie",
    "een model dat in de praktijk al winst maakt of aantoonbaar break-even draait",
    "geen aanloopperiode waarin alles uit eigen middelen betaald wordt",
    "financiering is bespreekbaar, omdat er cijfers over meerdere jaren zijn",
  ]),
  ("p", "Het aanbod van webshops, e-commercemerken en marketplace-accounts staat op "
        "%s. Startups en kleinere shops staan apart op %s."
        % (WO_MERK, wo("aanbod/startups"))),

  ("video", YT_WO, "Video's van het kanaal WebshopOvername.nl",
   "De uploadlijst van het YouTube-kanaal van WebshopOvername.nl, met uitleg over "
   "het kopen en verkopen van webshops."),

  ("h2", "Kosten die onderschat worden"),
  ("table",
   ["Post", "Waarom het tegenvalt"],
   [
    ["Content", "Foto's, video en productteksten voor honderden artikelen kosten "
     "meer tijd dan het bouwen van de shop."],
    ["Retouren", "In mode en schoenen loopt het retourpercentage op tot een "
     "niveau dat de marge bepaalt."],
    ["Advertenties", "De kosten per klik stijgen in populaire niches sneller dan "
     "de marges."],
    ["Voorraad", "Geld dat in dozen zit, is geld dat niet in marketing zit."],
    ["Klantcontact", "Vragen, klachten en verzendproblemen kosten structureel "
     "uren per week."],
   ]),
  ("p", "Wat een webshop waard is en welke factoren de prijs bepalen staat in de "
        "<a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool voor webshops</a>."),
 ],
 "related": [
  ("Checklist webshop overnemen", "/checklists/webshop-overnemen/"),
  ("Wat is mijn webshop waard", "/tools/wat-is-mijn-webshop-waard/"),
  ("Uitgelichte platforms", "/platforms/"),
  ("Cijfers en onderzoek", "/starten-of-overnemen/cijfers-en-onderzoek/"),
 ],
},

# ------------------------------------------------------------ bedrijf overnemen
{
 "path": "checklists/bedrijf-overnemen/",
 "crumb": "Bedrijf overnemen",
 "title": "Checklist: een bedrijf overnemen in tien stappen",
 "desc": "Van zoekprofiel en eerste gesprek tot waardering, intentieverklaring, "
         "boekenonderzoek, financiering en de eerste honderd dagen na de "
         "overdracht.",
 "kicker": "Checklist",
 "h1": "Checklist bedrijf overnemen",
 "lead": "Een overname verloopt in een vaste volgorde. Wie stappen overslaat, "
         "betaalt dat meestal terug in de prijs of in de overdracht.",
 "blocks": [
  ("steps", [
   ("Stel een zoekprofiel op",
    "Sector, omvang, regio, gewenste omzet en het bedrag dat beschikbaar is. Een "
    "scherp profiel scheelt maanden aan gesprekken die nergens toe leiden."),
   ("Toets de eigen financiering",
    "Voordat er gesprekken gevoerd worden: hoeveel eigen geld is er, en wat kan "
    "een financier daarbovenop doen. Verkopers nemen kopers zonder dat antwoord "
    "minder serieus."),
   ("Zoek en selecteer",
    "Aanbod staat op overnameplatformen, komt via adviseurs en via het eigen "
    "netwerk. Ook een actieve zoekopdracht is mogelijk: benaderen van bedrijven "
    "die niet te koop staan."),
   ("Teken een geheimhoudingsverklaring",
    "Zonder NDA krijgt een koper geen cijfers te zien. De verklaring beschermt de "
    "verkoper tegen onrust bij personeel, klanten en concurrenten."),
   ("Voer het eerste gesprek",
    "Doel is begrijpen waarom de eigenaar verkoopt, hoe het bedrijf draait en hoe "
    "afhankelijk het is van die eigenaar. Prijzen noemen kan later."),
   ("Maak een eigen waardering",
    "Genormaliseerde winst, kasstroom, investeringsbehoefte en de risico's in het "
    "klantenbestand. De vraagprijs is een startpunt, geen uitkomst."),
   ("Breng een indicatief bod uit",
    "Vrijblijvend, met de belangrijkste voorwaarden en aannames erbij. Het "
    "voorkomt dat beide partijen maanden doorwerken op onverenigbare "
    "verwachtingen."),
   ("Leg de afspraken vast in een intentieverklaring",
    "De letter of intent legt prijs, structuur, exclusiviteit en planning vast, "
    "onder voorbehoud van boekenonderzoek en financiering."),
   ("Doe boekenonderzoek",
    "Financieel, fiscaal, juridisch en operationeel. Contracten, personeel, "
    "vergunningen, verzekeringen, lopende geschillen en de staat van de "
    "bedrijfsmiddelen."),
   ("Teken en draag over",
    "Koopovereenkomst met garanties en vrijwaringen, financiering rond, en een "
    "overdrachtsperiode waarin de verkoper beschikbaar blijft voor klanten en "
    "personeel."),
  ]),

  ("h2", "Waar in het boekenonderzoek naar gekeken wordt"),
  ("table",
   ["Onderdeel", "Aandachtspunten"],
   [
    ["Financieel", "Genormaliseerde winst, eenmalige posten, werkkapitaal, "
     "achterstallige investeringen"],
    ["Klanten", "Concentratie, contractduur, opzegtermijnen, historisch verloop"],
    ["Personeel", "Contracten, cao, verlofsaldi, ziekteverzuim, sleutelfiguren"],
    ["Juridisch", "Huur, leveranciers, licenties, lopende geschillen, "
     "concurrentiebedingen"],
    ["Fiscaal", "Openstaande aanslagen, btw-positie, fiscale eenheid"],
    ["Operationeel", "Staat van machines, software, voorraadwaarde, ICT en "
     "beveiliging"],
   ]),
  ("p", "Toelichting op dit onderdeel staat op "
        "<a href=\"/kennisbank/due-diligence/\">due diligence</a>."),

  ("h2", "De eerste honderd dagen"),
  ("p", "Het traject eindigt niet bij de handtekening. Wat in de eerste maanden "
        "gebeurt, bepaalt of de betaalde prijs terugverdiend wordt."),
  ("tick", [
    "personeel informeren voordat het via een ander kanaal bekend wordt",
    "de belangrijkste klanten persoonlijk spreken, samen met de verkoper",
    "leveranciers en verzekeringen op naam van de nieuwe eigenaar zetten",
    "geen grote veranderingen in de eerste maand, behalve waar dat niet anders kan",
    "afspraken over de rol van de verkoper vastleggen, inclusief einddatum",
  ]),

  ("h2", "Begeleiding en aanbod"),
  ("p", "Voor het MKB-segment verzorgt %s waardering, zoekopdrachten en "
        "begeleiding van het proces. De werkwijze staat op %s, het aanbod op %s."
        % (OA_MERK, oa("hoe-werkt-het"), oa("bedrijven-te-koop"))),
 ],
 "related": [
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Intentieverklaring", "/kennisbank/intentieverklaring/"),
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Financiering en risico", "/starten-of-overnemen/financiering-en-risico/"),
 ],
},

# ------------------------------------------------------------ webshop overnemen
{
 "path": "checklists/webshop-overnemen/",
 "crumb": "Webshop overnemen",
 "title": "Checklist: een webshop overnemen en wat te controleren",
 "desc": "Wat er bij het kopen van een webshop extra onderzocht moet worden: "
         "verkeersbronnen, afhankelijkheden, techniek, accounts, klantdata en de "
         "overdracht van het domein.",
 "kicker": "Checklist",
 "h1": "Checklist webshop overnemen",
 "lead": "Bij een webshop zit de waarde in verkeer, klanten en merk. Precies die "
         "drie zijn het gevoeligst voor wat er tijdens en na de overdracht "
         "gebeurt.",
 "blocks": [
  ("h2", "Eerst de gewone stappen"),
  ("p", "De volgorde van een webshopovername is dezelfde als bij elk ander bedrijf: "
        "zoekprofiel, geheimhouding, gesprek, waardering, intentieverklaring, "
        "boekenonderzoek en overdracht. Die staat uitgewerkt in de "
        "<a href=\"/checklists/bedrijf-overnemen/\">checklist bedrijf overnemen</a>. "
        "Hieronder staat wat daar bij een webshop bovenop komt."),

  ("h2", "Verkeer en vindbaarheid"),
  ("tick", [
    "<b>Bronnen van bezoekers.</b> Organisch, betaald, e-mail, sociale kanalen of "
    "marktplaatsen. Een shop die voor 80 procent op betaalde advertenties draait "
    "is een ander bedrijf dan een shop met organisch verkeer.",
    "<b>Toegang tot de meetgegevens.</b> Inzage in de analytics en de "
    "zoekmachineconsole van de shop zelf, niet alleen een screenshot of een export.",
    "<b>Verloop over drie jaar.</b> Verkeer per maand, niet alleen het laatste "
    "kwartaal. Seizoenspieken en dalingen na algoritmewijzigingen worden pas "
    "zichtbaar over een langere reeks.",
    "<b>Merkverkeer.</b> Bezoekers die op de merknaam zoeken hebben meer waarde "
    "dan bezoekers op algemene zoektermen, omdat die groep terugkomt.",
    "<b>Linkprofiel.</b> Ingekochte links die na de overname wegvallen, nemen een "
    "deel van de positie mee.",
  ]),

  ("h2", "Afhankelijkheden"),
  ("p", "De grootste risico's bij webshops zijn zelden financieel. Ze zitten in "
        "afhankelijkheid van een partij die buiten de deal staat."),
  ("table",
   ["Afhankelijkheid", "Wat te controleren"],
   [
    ["Een enkele leverancier", "Exclusiviteit, contractduur, of het contract "
     "overdraagbaar is naar de nieuwe eigenaar"],
    ["Een marketplace-account", "Accountgezondheid, of het account overdraagbaar "
     "is en of de historie van reviews meegaat"],
    ["Een advertentieaccount", "Wie de eigenaar is, hoeveel historie er in het "
     "account zit en of het mee overgaat"],
    ["Een enkel product", "Aandeel in de omzet, patent- of merkbescherming, "
     "hoe eenvoudig het te kopieren is"],
    ["De verkoper zelf", "Wie de inkoop doet, de content maakt en de "
     "klantvragen beantwoordt"],
   ]),

  ("h2", "Techniek en accounts"),
  ("tick", [
    "eigendom en verhuisbaarheid van de domeinnaam, inclusief alle varianten",
    "het platform en de versie waarop de shop draait, plus de kosten van "
    "achterstallig onderhoud",
    "welke koppelingen er zijn met boekhouding, voorraad, verzending en betaling",
    "of maatwerk zelf ontwikkeld is of van een bureau, en wie de rechten heeft",
    "de lijst met accounts die mee overgaan, van hosting tot e-mail en "
    "reviewplatform",
    "merkregistratie, of die er is en op welke naam die staat",
  ]),

  ("h2", "Klantenbestand en privacy"),
  ("p", "Een klantenbestand is bij een webshop vaak de waardevolste post, en "
        "tegelijk de post met de meeste regels. Persoonsgegevens mogen niet zomaar "
        "worden overgedragen: het doel waarvoor ze verzameld zijn en de informatie "
        "die klanten daarover hebben gekregen bepalen wat is toegestaan. Bij een "
        "overname van de hele onderneming ligt dat anders dan bij het los kopen van "
        "een bestand."),
  ("p", "Praktisch betekent dat: vastleggen hoe het bestand is opgebouwd, wat er "
        "met klanten gecommuniceerd is, en welke toestemming er voor e-mail is "
        "gegeven. Dit punt hoort thuis in het boekenonderzoek en in de garanties in "
        "het contract."),

  ("h2", "Waardering van een webshop"),
  ("p", "Webshops worden meestal gewaardeerd op basis van de winst die de eigenaar "
        "eruit haalt, gecorrigeerd voor eigen uren en eenmalige posten, met een "
        "factor die afhangt van omvang, groei en afhankelijkheid. De "
        "<a href=\"/tools/wat-is-mijn-webshop-waard/\">rekentool</a> geeft daar een "
        "eerste indicatie van, met een toelichting op de factoren die de uitkomst "
        "omhoog of omlaag brengen."),
  ("p", "Aanbod, waardebepaling en begeleiding voor dit segment lopen via %s. Het "
        "actuele aanbod staat op %s en de dienstenpagina op %s."
        % (WO_NAKED, wo("bedrijven-te-koop"), wo("onze-diensten"))),
 ],
 "related": [
  ("Wat is mijn webshop waard", "/tools/wat-is-mijn-webshop-waard/"),
  ("Checklist webshop beginnen", "/checklists/webshop-beginnen/"),
  ("Due diligence", "/kennisbank/due-diligence/"),
  ("Uitgelichte platforms", "/platforms/"),
 ],
},
]
