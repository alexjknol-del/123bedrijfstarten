"""Rekentools: waarde-indicatie bedrijf en webshop."""

from .common import OA_MERK, WO_MERK, oa, wo

CALC_BEDRIJF = """
<div class="calc">
<div class="row">
  <label for="b_ebitda">Genormaliseerde EBITDA per jaar
    <small>Bedrijfsresultaat voor rente, belasting en afschrijvingen, gecorrigeerd
    voor eenmalige posten en een marktconform ondernemersloon.</small></label>
  <input type="number" id="b_ebitda" value="200000" min="0" step="5000" inputmode="numeric">
</div>
<div class="row">
  <label for="b_sector">Sector
    <small>Bandbreedtes gebaseerd op de Overname Barometer van Brookz en Dealsuite
    over de tweede helft van 2025.</small></label>
  <select id="b_sector">
    <option value="7.5">Softwareontwikkeling</option>
    <option value="6.7">IT-dienstverlening</option>
    <option value="6.5">Zorg en farmacie</option>
    <option value="5.0" selected>Overig, gemiddelde over alle sectoren</option>
    <option value="3.3">Horeca, toerisme en recreatie</option>
    <option value="2.5">Retail</option>
  </select>
</div>
<div class="row">
  <label for="b_groei">Omzetontwikkeling laatste drie jaar</label>
  <select id="b_groei">
    <option value="0.9">Dalend</option>
    <option value="1" selected>Stabiel</option>
    <option value="1.1">Groeiend</option>
    <option value="1.2">Sterk groeiend</option>
  </select>
</div>
<div class="row">
  <label for="b_eigenaar">Afhankelijkheid van de eigenaar
    <small>Hoeveel omzet en kennis loopt via de huidige eigenaar persoonlijk.</small></label>
  <select id="b_eigenaar">
    <option value="0.8">Groot, eigenaar is het bedrijf</option>
    <option value="0.9" selected>Gemiddeld</option>
    <option value="1.05">Klein, managementteam draait zelfstandig</option>
  </select>
</div>
<div class="row">
  <label for="b_klant">Grootste klant in de omzet</label>
  <select id="b_klant">
    <option value="0.85">Meer dan 30 procent</option>
    <option value="0.95" selected>10 tot 30 procent</option>
    <option value="1.05">Minder dan 10 procent</option>
  </select>
</div>
<div class="row">
  <label for="b_terug">Terugkerende omzet
    <small>Contracten, abonnementen of onderhoud.</small></label>
  <select id="b_terug">
    <option value="0.95">Vrijwel geen</option>
    <option value="1" selected>Een deel</option>
    <option value="1.12">Overwegend terugkerend</option>
  </select>
</div>
<div class="row">
  <label for="b_schuld">Rentedragende schulden minus liquide middelen
    <small>Positief bedrag bij netto schuld, negatief bedrag bij overtollige kas.</small></label>
  <input type="number" id="b_schuld" value="0" step="5000" inputmode="numeric">
</div>
<div class="out">
  <div class="big" id="b_uit">&nbsp;</div>
  <div class="sub" id="b_sub">&nbsp;</div>
  <div class="bars">
    <div><span>Toegepaste multiple</span><span id="b_mult"></span></div>
    <div><span>Ondernemingswaarde</span><span id="b_ov"></span></div>
    <div><span>Netto schuld</span><span id="b_ns"></span></div>
  </div>
</div>
</div>
"""

JS_BEDRIJF = """
(function(){
  var f=new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR',
    maximumFractionDigits:0});
  var ids=['b_ebitda','b_sector','b_groei','b_eigenaar','b_klant','b_terug','b_schuld'];
  function g(id){return parseFloat(document.getElementById(id).value)||0;}
  function calc(){
    var e=g('b_ebitda');
    var m=g('b_sector')*g('b_groei')*g('b_eigenaar')*g('b_klant')*g('b_terug');
    if(m<1)m=1;
    var ov=e*m, ns=g('b_schuld'), aw=ov-ns;
    var lo=aw*0.85, hi=aw*1.15;
    var uit=document.getElementById('b_uit'), sub=document.getElementById('b_sub');
    if(e<=0){uit.textContent='Vul een positief resultaat in';
      sub.textContent='Bij een negatief of nul resultaat werkt een multiple niet. '+
      'De waarde wordt dan bepaald op basis van activa of vooruitzichten.';
      document.getElementById('b_mult').textContent='-';
      document.getElementById('b_ov').textContent='-';
      document.getElementById('b_ns').textContent='-';return;}
    uit.textContent=f.format(Math.max(lo,0))+' tot '+f.format(Math.max(hi,0));
    sub.textContent='Indicatieve bandbreedte voor de waarde van de aandelen, '+
      'op basis van de ingevulde gegevens.';
    document.getElementById('b_mult').textContent=m.toFixed(1).replace('.',',')+' x EBITDA';
    document.getElementById('b_ov').textContent=f.format(ov);
    document.getElementById('b_ns').textContent=f.format(ns);
  }
  ids.forEach(function(id){var el=document.getElementById(id);
    el.addEventListener('input',calc);el.addEventListener('change',calc);});
  calc();
})();
"""

CALC_WEBSHOP = """
<div class="calc">
<div class="row">
  <label for="w_omzet">Jaaromzet exclusief btw</label>
  <input type="number" id="w_omzet" value="400000" min="0" step="5000" inputmode="numeric">
</div>
<div class="row">
  <label for="w_winst">Genormaliseerde jaarwinst
    <small>Winst voor belasting, gecorrigeerd voor eenmalige posten en voor de
    uren die de eigenaar zelf in de shop steekt.</small></label>
  <input type="number" id="w_winst" value="60000" step="1000" inputmode="numeric">
</div>
<div class="row">
  <label for="w_uren">Eigen uren per week
    <small>Wordt gecorrigeerd tegen 45 euro per uur, omdat een koper die uren moet
    invullen of betalen.</small></label>
  <input type="number" id="w_uren" value="10" min="0" max="80" step="1" inputmode="numeric">
</div>
<div class="row">
  <label for="w_groei">Omzetontwikkeling laatste twee jaar</label>
  <select id="w_groei">
    <option value="0.75">Dalend</option>
    <option value="1" selected>Stabiel</option>
    <option value="1.2">Groeiend</option>
    <option value="1.4">Sterk groeiend</option>
  </select>
</div>
<div class="row">
  <label for="w_verkeer">Belangrijkste bron van bezoekers</label>
  <select id="w_verkeer">
    <option value="0.8">Overwegend betaalde advertenties</option>
    <option value="1" selected>Gemengd</option>
    <option value="1.2">Overwegend organisch en direct</option>
  </select>
</div>
<div class="row">
  <label for="w_herhaal">Aandeel herhaalaankopen</label>
  <select id="w_herhaal">
    <option value="0.9">Laag, onder 15 procent</option>
    <option value="1" selected>Gemiddeld</option>
    <option value="1.15">Hoog, boven 35 procent</option>
  </select>
</div>
<div class="row">
  <label for="w_afh">Afhankelijkheid van een marktplaats of een leverancier</label>
  <select id="w_afh">
    <option value="0.8">Groot</option>
    <option value="0.95" selected>Gemiddeld</option>
    <option value="1.1">Klein</option>
  </select>
</div>
<div class="row">
  <label for="w_voorraad">Voorraadwaarde die mee overgaat
    <small>Wordt bovenop de waarde van de onderneming geteld.</small></label>
  <input type="number" id="w_voorraad" value="25000" min="0" step="1000" inputmode="numeric">
</div>
<div class="out">
  <div class="big" id="w_uit">&nbsp;</div>
  <div class="sub" id="w_sub">&nbsp;</div>
  <div class="bars">
    <div><span>Gecorrigeerde winst</span><span id="w_sde"></span></div>
    <div><span>Toegepaste factor</span><span id="w_fac"></span></div>
    <div><span>Winst als percentage van de omzet</span><span id="w_marge"></span></div>
  </div>
</div>
</div>
"""

JS_WEBSHOP = """
(function(){
  var f=new Intl.NumberFormat('nl-NL',{style:'currency',currency:'EUR',
    maximumFractionDigits:0});
  var ids=['w_omzet','w_winst','w_uren','w_groei','w_verkeer','w_herhaal','w_afh',
    'w_voorraad'];
  function g(id){return parseFloat(document.getElementById(id).value)||0;}
  function calc(){
    var omzet=g('w_omzet');
    var sde=g('w_winst')-(g('w_uren')*45*46);
    var fac=2.4*g('w_groei')*g('w_verkeer')*g('w_herhaal')*g('w_afh');
    if(omzet<100000&&fac>3)fac=3;
    if(fac<1)fac=1;
    var basis=sde*fac, tot=basis+g('w_voorraad');
    var lo=tot*0.85, hi=tot*1.15;
    var uit=document.getElementById('w_uit'), sub=document.getElementById('w_sub');
    document.getElementById('w_sde').textContent=f.format(sde);
    document.getElementById('w_fac').textContent=fac.toFixed(1).replace('.',',')+' x';
    document.getElementById('w_marge').textContent= omzet>0 ?
      (sde/omzet*100).toFixed(1).replace('.',',')+' procent' : '-';
    if(sde<=0){
      uit.textContent='Geen waarde op basis van winst';
      sub.textContent='Na correctie voor de eigen uren blijft er geen winst over. '+
        'De waarde wordt dan bepaald door voorraad, merk, domein en klantenbestand.';
      return;}
    uit.textContent=f.format(lo)+' tot '+f.format(hi);
    sub.textContent='Indicatieve bandbreedte, inclusief de opgegeven voorraad.';
  }
  ids.forEach(function(id){var el=document.getElementById(id);
    el.addEventListener('input',calc);el.addEventListener('change',calc);});
  calc();
})();
"""

DISCLAIMER = [
 ("p", "De uitkomst is een rekenkundige indicatie op basis van de ingevulde "
       "gegevens en algemene marktcijfers. Het is geen waardering en geen bod. "
       "Een echte waardebepaling kijkt naar jaarrekeningen, contracten, "
       "investeringsbehoefte en de markt waarin het bedrijf opereert. Aan de "
       "uitkomst zijn geen rechten te ontlenen."),
]

PAGES = [

{
 "path": "tools/",
 "crumb": "Rekentools",
 "title": "Rekentools: waarde van een bedrijf of webshop berekenen",
 "desc": "Twee rekentools die op basis van winst, sector en risicofactoren een "
         "indicatieve bandbreedte geven voor de waarde van een bedrijf of een "
         "webshop.",
 "kicker": "Rekentools",
 "h1": "Rekentools",
 "lead": "Twee rekenmodellen die in de browser draaien. Er wordt niets verstuurd "
         "en niets opgeslagen: de berekening gebeurt op het apparaat zelf.",
 "blocks": [
  ("cards", [
   ("Wat is mijn bedrijf waard",
    "Waarde-indicatie op basis van genormaliseerde EBITDA, sector, groei en "
    "risicofactoren.",
    "/tools/wat-is-mijn-bedrijf-waard/"),
   ("Wat is mijn webshop waard",
    "Waarde-indicatie voor webshops en e-commercebedrijven, op basis van "
    "gecorrigeerde winst, verkeersmix en afhankelijkheden.",
    "/tools/wat-is-mijn-webshop-waard/"),
  ]),
  ("h2", "Wat een rekentool wel en niet doet"),
  ("p", "Een rekentool zet een aantal bekende vuistregels om in een getal. Dat "
        "helpt bij de eerste oriëntatie: is de orde van grootte een ton of een "
        "miljoen. Wat een rekentool niet doet, is beoordelen of de cijfers kloppen, "
        "hoe hard de contracten zijn en wat er in de markt gebeurt."),
  ("p", "Voor een onderbouwde waardering wordt in de praktijk gekeken naar meerdere "
        "methoden naast elkaar. Die staan uitgelegd op "
        "<a href=\"/kennisbank/waardebepaling/\">waardebepaling</a> en "
        "<a href=\"/kennisbank/multiples/\">multiples</a>."),
  ("h2", "Verschil tussen waarde en prijs"),
  ("p", "Waarde is een berekening, prijs is de uitkomst van een onderhandeling. "
        "Twee kopers komen bij hetzelfde bedrijf op verschillende bedragen uit, "
        "omdat de een synergie ziet en de ander een opvolgingsprobleem oplost. De "
        "berekening bepaalt vooral vanaf welk punt dat gesprek begint."),
  ("h2", "Een echte waardebepaling"),
  ("p", "Wie verder wil dan een indicatie, kan een waardebepaling laten uitvoeren. "
        "Voor bedrijven in het algemeen loopt dat via %s, met uitleg op %s. Voor "
        "webshops en e-commercebedrijven via %s, met uitleg op %s."
        % (OA_MERK, oa("bedrijf-waarderen"), WO_MERK, wo("overnameadvies/waardebepaling"))),
 ],
 "related": [
  ("Waardebepaling", "/kennisbank/waardebepaling/"),
  ("Multiples", "/kennisbank/multiples/"),
  ("Goodwill", "/kennisbank/goodwill/"),
 ],
},

{
 "path": "tools/wat-is-mijn-bedrijf-waard/",
 "crumb": "Wat is mijn bedrijf waard",
 "title": "Wat is mijn bedrijf waard: rekentool met sectormultiples",
 "desc": "Bereken een indicatieve waarde van een bedrijf op basis van "
         "genormaliseerde EBITDA, sector, groei, afhankelijkheid van de eigenaar "
         "en klantconcentratie.",
 "kicker": "Rekentool",
 "h1": "Wat is mijn bedrijf waard",
 "lead": "Vul de genormaliseerde EBITDA in en de belangrijkste risicofactoren. De "
         "tool rekent daar een bandbreedte uit, op basis van gepubliceerde "
         "sectormultiples.",
 "blocks": [
  ("raw", CALC_BEDRIJF),
  ("panel", "Let op", DISCLAIMER),

  ("h2", "Hoe de berekening werkt"),
  ("p", "De tool vermenigvuldigt de genormaliseerde EBITDA met een multiple. Die "
        "multiple begint bij het sectorgemiddelde en wordt vervolgens aangepast "
        "voor groei, afhankelijkheid van de eigenaar, klantconcentratie en het "
        "aandeel terugkerende omzet. Van de uitkomst wordt de netto schuld "
        "afgetrokken, omdat een koper een bedrijf koopt inclusief de schulden die "
        "erin zitten."),
  ("table",
   ["Begrip", "Betekenis"],
   [
    ["EBITDA", "Resultaat voor rente, belasting, afschrijvingen en amortisatie"],
    ["Normaliseren", "Corrigeren voor eenmalige posten en voor een marktconform "
     "loon van de eigenaar, zodat de winst vergelijkbaar wordt"],
    ["Multiple", "Het aantal keren de winst dat kopers in een sector betalen"],
    ["Ondernemingswaarde", "De waarde van het bedrijf zonder rekening te houden "
     "met financiering"],
    ["Netto schuld", "Rentedragende schulden verminderd met liquide middelen"],
    ["Aandelenwaarde", "Ondernemingswaarde minus netto schuld, het bedrag dat "
     "de verkoper ontvangt"],
   ]),

  ("h2", "Waar de sectorcijfers vandaan komen"),
  ("p", "De multiples in de keuzelijst zijn gebaseerd op de Overname Barometer van "
        "Brookz en Dealsuite over de tweede helft van 2025, gepubliceerd in "
        "februari 2026. Dat onderzoek werd uitgevoerd onder 291 Nederlandse "
        "overnameadviesbureaus en gaat over bedrijven met een omzet tussen 0,5 en "
        "50 miljoen euro. Het gemiddelde over alle sectoren kwam uit op 5,0."),

  ("h2", "Wat de uitkomst omhoog of omlaag brengt"),
  ("h3", "Omhoog"),
  ("tick", [
    "terugkerende omzet uit contracten of onderhoud",
    "een gespreid klantenbestand zonder dominante afnemer",
    "een team dat het bedrijf draaiend houdt zonder de eigenaar",
    "een aantoonbaar groeiende omzet over meerdere jaren",
    "een administratie die snel en volledig aan te leveren is",
  ]),
  ("h3", "Omlaag"),
  ("tick", [
    "een eigenaar die zelf de belangrijkste verkoper of vakman is",
    "een klant die meer dan dertig procent van de omzet levert",
    "achterstallig onderhoud aan machines, software of pand",
    "aflopende contracten zonder verlenging",
    "cijfers die alleen als samenvatting beschikbaar zijn",
  ]),
  ("p", "Wat er te doen valt om die factoren te verbeteren staat op "
        "<a href=\"/verkopen/verkoopklaar-ondernemen/\">verkoopklaar ondernemen</a>."),

  ("h2", "Wanneer een multiple niet werkt"),
  ("p", "Bij een verlieslatend bedrijf, bij een bedrijf dat vooral uit vastgoed of "
        "machines bestaat, en bij bedrijven met sterk wisselende resultaten geeft "
        "een multiple een misleidend beeld. Dan wordt gekeken naar de intrinsieke "
        "waarde, naar de kasstroom over meerdere jaren, of naar wat de losse "
        "onderdelen opbrengen. Meer daarover op "
        "<a href=\"/kennisbank/waardebepaling/\">waardebepaling</a>."),
  ("p", "Een uitgewerkte waardebepaling voor het MKB verzorgt %s. De toelichting "
        "staat op %s."
        % (OA_MERK, oa("bedrijf-waarderen"))),
 ],
 "js": JS_BEDRIJF,
 "related": [
  ("Wat is mijn webshop waard", "/tools/wat-is-mijn-webshop-waard/"),
  ("Multiples", "/kennisbank/multiples/"),
  ("Goodwill", "/kennisbank/goodwill/"),
  ("Optimaal verkopen", "/verkopen/optimaal-verkopen/"),
 ],
},

{
 "path": "tools/wat-is-mijn-webshop-waard/",
 "crumb": "Wat is mijn webshop waard",
 "title": "Wat is mijn webshop waard: rekentool voor e-commerce",
 "desc": "Bereken een indicatieve waarde van een webshop op basis van "
         "gecorrigeerde winst, eigen uren, verkeersbronnen, herhaalaankopen en "
         "afhankelijkheid van marktplaatsen.",
 "kicker": "Rekentool",
 "h1": "Wat is mijn webshop waard",
 "lead": "Webshops worden gewaardeerd op de winst die er na correctie voor de "
         "eigen uren overblijft, met een factor die afhangt van groei, "
         "verkeersbronnen en afhankelijkheden.",
 "blocks": [
  ("raw", CALC_WEBSHOP),
  ("panel", "Let op", DISCLAIMER),

  ("h2", "Waarom de eigen uren eraf gaan"),
  ("p", "Bij veel webshops doet de eigenaar zelf de inkoop, de content, de "
        "verzending en de klantvragen. Die uren staan niet in de winst-en-"
        "verliesrekening, maar een koper moet ze wel invullen of betalen. De tool "
        "rekent daarom 45 euro per uur, over 46 werkbare weken per jaar, van de "
        "winst af. Een shop die 60.000 euro winst maakt met 20 uur eigen werk per "
        "week houdt daardoor aanzienlijk minder over dan een shop die hetzelfde "
        "verdient met vijf uur."),

  ("h2", "Wat de factor bepaalt"),
  ("table",
   ["Factor", "Effect op de waarde"],
   [
    ["Groei van de omzet", "Een dalende omzet drukt de factor het hardst van alle "
     "variabelen, omdat een koper de daling doortrekt"],
    ["Bron van het verkeer", "Organisch en direct verkeer is stabieler dan "
     "verkeer dat elke maand opnieuw ingekocht moet worden"],
    ["Herhaalaankopen", "Terugkerende klanten maken de omzet voorspelbaar"],
    ["Afhankelijkheid", "Een shop die vooral op een marktplaats of een "
     "leverancier draait, verkoopt lastiger"],
    ["Omvang", "Kleine shops halen structureel lagere factoren dan grotere "
     "e-commercebedrijven"],
   ]),

  ("h2", "Voorraad en losse onderdelen"),
  ("p", "Voorraad wordt bij een webshopovername meestal apart afgerekend, tegen "
        "inkoopwaarde en gecorrigeerd voor incourante artikelen. De tool telt de "
        "opgegeven voorraadwaarde daarom bovenop de berekende waarde. Ook zaken als "
        "een geregistreerde merknaam, een sterke domeinnaam of een e-maillijst "
        "kunnen los waarde hebben, ook als de winst laag is."),

  ("h2", "Als er geen winst is"),
  ("p", "Een webshop zonder winst is niet automatisch waardeloos. De waarde zit dan "
        "in het merk, het domein, het klantenbestand, de voorraad en de posities in "
        "zoekresultaten. Kopers rekenen in dat geval eerder met wat het kost om "
        "hetzelfde zelf op te bouwen. Dat is een andere rekensom dan een factor "
        "maal de winst."),

  ("h2", "Volgende stap"),
  ("p", "Wat er bij een verkoop of overname van een webshop komt kijken staat in de "
        "<a href=\"/checklists/webshop-overnemen/\">checklist webshop overnemen</a> "
        "en in de gids <a href=\"/verkopen/\">bedrijf verkopen</a>. Een "
        "waardebepaling voor webshops en e-commercebedrijven verzorgt %s, met "
        "uitleg op %s."
        % (WO_MERK, wo("overnameadvies/waardebepaling"))),
 ],
 "js": JS_WEBSHOP,
 "related": [
  ("Checklist webshop overnemen", "/checklists/webshop-overnemen/"),
  ("Checklist webshop beginnen", "/checklists/webshop-beginnen/"),
  ("Wat is mijn bedrijf waard", "/tools/wat-is-mijn-bedrijf-waard/"),
  ("Uitgelichte platforms", "/platforms/"),
 ],
},
]
