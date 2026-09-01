# Nexus Gaja

![Nexus Gaja-logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** is een intelligent, contextgevoelig communicatienetwerk dat is ontworpen om een ​​revolutie teweeg te brengen in de wereldwijde communicatie.

## Doel en visie
In een geglobaliseerde wereld is taal vaak de grootste barrière. Het belangrijkste doel van Nexus Gaja is om naadloze, barrièrevrije en contextueel nauwkeurige communicatie tussen mensen mogelijk te maken, ongeacht of ze een gemeenschappelijke taal spreken.

Het gaat niet alleen om het rigide vertalen van woorden, maar om het **overbrengen van betekenis**. Nexus Gaja verbindt mensen op een dieper niveau door culturele, regionale en contextuele nuances te begrijpen, waardoor echte, authentieke gesprekken mogelijk worden.

## Mogelijkheden en functies
- **Multimediacommunicatie**: het systeem verwerkt niet alleen tekst, maar ook beeld, audio en video. Dit maakt volledig meeslepende gesprekken (bijvoorbeeld video-oproepen of spraakberichten) in realtime mogelijk, over taalbarrières heen.
- **Contextgevoeligheid**: Herkenning van ironie, idiomen, jargon en regionale dialecten die vaak verkeerd worden begrepen door conventionele vertalers.
- **Platformoverschrijdend netwerk**: dient als basis voor privéchats, forumthreads (berichten met commentaar) en wereldwijde community-interacties.

---

## Technische Architectuur (Kernconcept)

De technische kern van Nexus Gaja is een op maat gemaakt communicatiemodel dat strikt in drie lagen is verdeeld:

1. **Origineel**: het door de afzender aangemaakte communicatieobject (bericht) blijft altijd onveranderlijk.
2. **Semantische interpretatie**: het systeem analyseert niet alleen de woorden, maar ook de werkelijke betekenis.
3. **Doeltaalweergave**: de AI creëert slechts een tijdelijke of in de cache opgeslagen weergave van het origineel voor de betreffende ontvanger op basis van de voorkeurstaal. Vertalingen overschrijven nooit het originele bericht.

### Contextafhankelijkheid
Vertalingen in Nexus Gaja bekijken berichten nooit afzonderlijk. De engine houdt rekening met de volledige hiërarchie:
`Bericht` → `Eerdere berichten` → `Threadcontext` → `Communitycontext` → `Taal/regio` → `Gebruikersvoorkeuren`

### Efficiëntie door vertaling op aanvraag
De vertaling gebeurt alleen op hulpbronnenefficiënte wijze **op verzoek** (on-demand). Wanneer een gebruiker inhoud opvraagt, wordt deze vertaald in de vooraf ingestelde taal. Zodra een vertaling voor een specifieke taal is gegenereerd, wordt deze permanent opgeslagen (caching) om toekomstige verzoeken drastisch te versnellen.

## AI-ondersteunde moderatie (WP 1.8.4)

Met AI-Assisted Moderation zetten we een belangrijke stap van productidee naar technische architectuur, rekening houdend met de huidige EU-regelgeving (transparantievereisten van de EU AI-wet onder artikel 50; Wet op digitale diensten met begrijpelijke rechtvaardigingen en beroepsmogelijkheden).

### 1. Basisprincipe
De belangrijkste zin voor de architectuur is: **De moderatie-AI is een beoordelingssysteem, geen autonoom bestuurssysteem.**
Het is bedoeld om mensen met mate te helpen, niet om zelf te bepalen welke meningen over Nexus Gaja mogen bestaan.
We onderscheiden drie niveaus:
- **Detectie:** "Er kan hier sprake zijn van een regelovertreding."
- **Evaluatie:** "De kans op een regelovertreding is bijvoorbeeld 94%."
- **Beslissing:** "Welke actie wordt er feitelijk ondernomen?"
In ernstige gevallen moet het derde niveau door een mens worden gecontroleerd.

### 2. De moderatie-AI als subsysteem
In plaats van één enkele AI wordt een robuust subsysteem opgezet:
```tekst
                 NEXUS GAJA AI MODERATIE
                          │
       ┌──────────────────┼──────────────────┐
       │ │ │
  Taal AI Veiligheid AI Fraude AI
       │ │ │
       ├──────────────┬───┴──────────────┬───┤
       │ │ │
 Vertaalgedrag Identiteit
 Analyse Analysesignalen
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Risicobeoordeling
                      │
                      ▼
               Menselijke beoordeling
```

### 3. The Most Important AI Modules
Nexus Gaja utilizes nine specialized analysis areas:
- **M1 – Language Understanding**: Detects language, dialect, slang, irony indicators, translation issues.
- **M2 – Toxicity / Abuse Detection**: Detects insults, personal attacks, harassment.
- **M3 – Threat Detection**: Detects potential threats, blackmail, violence announcements.
- **M4 – Hate / Dehumanization Detection**: Detects targeted attacks on people based on specific affiliations.
- **M5 – Spam / Manipulation Detection**: Detects spam, bot behavior, coordinated manipulation.
- **M6 – Fraud Detection**: Detects suspicious fraud attempts, phishing, social engineering.
- **M7 – Identity Integrity**: Checks signals regarding account takeovers, multiple accounts, ban evasion.
- **M8 – Media Safety**: Analyzes images, audio, video, documents.
- **M9 – Context Engine**: The most important module. It merges the individual findings.

### 4. Waarom de Context Engine cruciaal is
Een puur zoeken op trefwoord zou onvoldoende zijn. 'Ik zou hem kunnen vermoorden door te lachen' bevat semantisch geweld, maar is stijlfiguur. "Morgen om 20.00 uur schiet ik hem voor zijn huis neer" is een heel andere situatie. De AI moet begrijpen wat de verklaring in zijn specifieke context betekent.

### 5. Meertalige moderatie
Matiging kan niet zomaar woorden vergelijken. Het moet het semantische niveau analyseren (bijvoorbeeld Duitse idiomen versus Japanse idiomen versus regionale uitdrukkingen).

### 6. Originele taal + vertaling
Origineel en vertaling worden afzonderlijk geanalyseerd. Alleen dan vindt de ‘Gecombineerde Moderatie Assessment’ plaats. Hierdoor kan Nexus Gaja bepalen of de vertaling zelf de feiten heeft geëscaleerd of gewijzigd.

### 7. Vertrouwensscore
Elke AI-evaluatie krijgt een betrouwbaarheidsscore (bijvoorbeeld dreigingskans: 0,96). Echter: **Vertrouwensscore ≠ Waarheid.** Een score van 96% betekent alleen dat het model zeer zeker is van zijn classificatie, niet noodzakelijkerwijs dat de gebruiker schuldig is.

### 8. Onzekerheid wordt zelf een signaal
Als de AI onzeker is (bijvoorbeeld dreiging: 0,62, satire: 0,54), mag deze niet simpelweg harde regels afdwingen. In plaats daarvan is onzekerheid rechtstreeks in de architectuur ingebouwd: **Menselijke beoordeling vereist**.

### 9. Vier beslissingszones
- 🟢 **GROEN**: Zeer waarschijnlijk conform. → geen actie.
- 🟡 **GEEL**: Mogelijke overtreding. → monitoren/waarschuwing geven indien nodig.
- 🟠 **ORANJE**: waarschijnlijke overtreding. → moderatiebeoordeling.
- 🔴 **ROOD**: Ernstige mogelijke overtreding. → onmiddellijke beschermingsmaatregel + menselijke beoordeling.

### 10. Geen "AI-straf"
**De AI legt geen definitieve sancties op.** Het kan leiden tot onmiddellijke technische maatregelen (bijvoorbeeld het tijdelijk achterhouden van een bericht) bij ernstige veiligheidsproblemen, maar de uiteindelijke beslissing blijft verifieerbaar.

### 11. Beschermende maatregelen kunnen automatisch plaatsvinden
In het geval van een concrete dreiging (bedreiging gedetecteerd → groot vertrouwen → tijdelijke beperking → menselijke beoordeling → besluit) beschermen we de bedreigde gebruiker zonder de AI in een rechter te veranderen.

### 12. De AI moet zijn beslissingen kunnen rechtvaardigen
De DSA vereist duidelijke en specifieke redenen. De AI biedt gestructureerde redenering: Regel (NG-CONDUCT-004), Gedetecteerd (Potentiële concrete dreiging), Vertrouwen (0,94), Relevante context (Vorige 4 berichten), Aanbevolen actie (Menselijke beoordeling).

### 13. AI mag de inhoud niet in het geheim wijzigen
** Moderatie AI mag de originele inhoud nooit onopgemerkt wijzigen. ** Tijdens automatische correctie, vertaling of samenvatting blijft het origineel altijd behouden.

### 14. AI-gegenereerde inhoud
We maken onderscheid tussen: door mensen gecreëerd, door AI ondersteund, door AI gegenereerd en door AI gemanipuleerd. Dit wordt onderdeel van de contentmetadata.

### 15. Labeling van AI-inhoud en AI-herkomstlaag
Volgens de transparantieregels van de EU AI Act (van kracht vanaf augustus 2026) moet door AI gegenereerde inhoud identificeerbaar zijn. We bieden een AI-herkomstlaag die metadata opslaat (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake-detectie
De architectuur is bedoeld om synthetische beelden, gekloonde stemmen en deepfakes te detecteren. Detectie is echter niet automatisch bewijs.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. Geen straf gebaseerd op een enkele AI-score
Geen enkele ernstige moderatie-interventie mag uitsluitend gebaseerd zijn op een enkel geautomatiseerd classificatieresultaat (Tekst + Context + Gedrag + Taal + Media + Regelengine = Risicobeoordeling).

### 21. Signalen van gebruikersgedrag en geen sociaal kredietsysteem
Dit heeft betrekking op signalen van technisch misbruik (bijvoorbeeld het massaal posten van spam), en niet op een algemeen sociaal beoordelingssysteem. Nexus Gaja hanteert geen sociaal kredietsysteem – gematigdheid dient de veiligheid, niet de beoordeling van iemands waarde.

### 22. Moderatie-AI moet controleerbaar zijn
Alle relevante geautomatiseerde beslissingen worden geregistreerd (Event-ID, Rule-ID, Confidence, Human-Review, etc.) om de traceerbaarheid te garanderen.

### 23. Valse positieven, valse negatieven en kwaliteitsstatistieken
Fouttypen worden gecontroleerd. Een dashboard meet precisie, herinnering en vooral het **Beroepsomkeringspercentage** (aantal succesvolle beroepen).

### 24. Taalgelijkheid en vertaalbias
De moderatiekwaliteit moet vergelijkbaar zijn in alle ondersteunde talen (Multilingual Moderation Benchmark). Als de moderatieresultaten verschillen tussen het origineel en de vertaling (Vertaalconflict), moet dit specifiek worden beoordeeld.

### 25. Architectuurvoorstel en beleidsengine
Regels (Policy Engine) zijn niet hardgecodeerd in de AI-modellen. De AI levert bevindingen; de Policy Engine beslist op basis van de huidige regels. Hierdoor zijn **modelwijzigingen mogelijk zonder regelwijzigingen**.

### 26. De mens blijft de uiteindelijke autoriteit
- **NG-AI-MOD-001**: De AI helpt bij detectie en classificatie, maar vervangt niet de menselijke beoordeling bij ernstige beslissingen.
- **NG-AI-MOD-002**: Geautomatiseerde moderatiebeslissingen moeten traceerbaar, logbaar en verifieerbaar zijn.

**Samenvatting**: We bouwen een systeem in vier fasen: AI-detectie, context- en risicoanalyse, beleidsengine en menselijk bestuur. Dit maakt sterke automatisering mogelijk zonder dat er een gevaarlijke ‘AI as Judge’-architectuur ontstaat.

## Financieringsprincipes en verdienmodel (WP 1.10.1)

Voor Nexus Gaja geldt een zeer belangrijk economisch principe: **Geen traditionele advertenties binnen het platform.**
Dit onderscheidt Nexus Gaja fundamenteel van veel van de hedendaagse sociale netwerken. Dit betekent echter niet dat Nexus Gaja geen commercieel karakter kan hebben. Integendeel, het platform moet economisch levensvatbaar zijn, zodat het sociale doel ervan kan blijven bestaan. Economische activiteit is een middel om een ​​doel te bereiken, niet het primaire doel van het platform.

### 1. Principe NG-FIN-001
Nexus Gaja financiert zijn activiteiten via transparante inkomstenstromen die gescheiden zijn van de interesses van gebruikers, en niet via het genereren van inkomsten uit de aandacht van zijn gebruikers of persoonlijke gegevens.

### 2. Geen traditionele reclame
Specifiek verboden zijn:
- Banneradvertenties
- Pop-upadvertenties
- Automatisch afspelen van videoadvertenties
- Gesponsorde berichten in de standaardfeed
- Gepersonaliseerde advertentieprofielen
- Verkoop van gebruikersprofielen of persoonlijke gegevens
- Advertenties afgeleid van privégesprekken.

Nexus Gaja blijft een **communicatieruimte in plaats van een advertentieruimte**.

### 3. Financiering zonder reclame (de 6 pijlers)
De financiering is gebaseerd op zes pijlers:
```tekst
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PREMIUM ORGANISATIE DONATIES
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    VERLEENT PARTNERSCHAPPENDIENSTEN
```

#### Pijler 1 – Gratis basislidmaatschap
**Nexus Gaja Free** maakt gratis basisinternationaal begrip voor iedereen mogelijk (profiel, internationale communicatie, berichten, communities, chats, basisvertaling).

#### Pijler 2 – Premiumaanbod
Vrijwillige betaalde aanbiedingen (**Nexus Gaja Plus**) die grotere opslaglimieten, hogere mediakwaliteit, uitgebreide AI-quota en organisatorische functies bieden.
**Belangrijk (Freemium in plaats van Dark Freemium):** Basiscommunicatie mag nooit kunstmatig worden verslechterd.

#### Pijler 3 – Organisaties
Speciale accounts voor scholen, universiteiten, NGO's, bedrijven en gemeenten (**Nexus Gaja Organization**). Scholen kunnen worden ondersteund via institutionele tarieven als vermenigvuldigers van internationaal begrip.

#### Pijler 4 – Donaties
De **Nexus Gaja Funding Pool** accepteert algemene en geoormerkte donaties (bijvoorbeeld "voor internationale jeugdcommunicatie"). Een **Fund Allocation Ledger** zorgt voor een transparante toewijzing van fondsen.
**Doelfonds & Tombola:** Een deel van de donaties voedt een pool voor gratis/met korting gebruik. Een loterij-/tombolamechanisme kan deze fondsen op transparante en controleerbare wijze toewijzen.

#### Pillar 5 – Institutional Funding
Foundations, cultural funding programs, or state programs.
**NG-FIN-002:** Financial support does not buy editorial or technical control (Independence).

#### Pijler 6 – Commerciële dienstverlening
B2B-diensten zoals **Translation-as-a-Service** (API), organisatorische communicatie of internationale vergaderruimtes, zonder de standaard gebruikersfeed te belasten.

### 4. Geen data-inkomsten- en surveillance-economie
**NG-FIN-003:** Persoonlijke gebruikersgegevens zijn geen handelswaar. Geen verkoop van lijsten, profielen of geschiedenissen. Nexus Gaja profiteert niet van psychologisch toezicht (Surveillance Economy).

### 5. Financial Transparency & Fund Ledger
**Nexus Gaja Financial Transparency:** Publication of aggregated financial structures. Earmarked donations receive technical accounting (Fund ID → Purpose → Balance → Allocation). No cross-subsidization of social purposes into corporate marketing.

### 6. Op solidariteit gebaseerd financieringsmodel
De prijsstelling is gebaseerd op kostenoriëntatie, eerlijkheid en solidariteit.
**Solidarity Premium:** Een vrijwillige optie voor Premium-gebruikers om een ​​deel van de toegang van een andere gebruiker te financieren. Gedwongen solidariteit of een premiumklassemaatschappij (minder respect/matiging voor gratis gebruikers) is ten strengste verboden.

### 7. Economische KPI's in plaats van engagementeconomie
Geen afhankelijkheid van het ‘zo lang mogelijk online houden’ van gebruikers (geen ragebait, oneindige feeds).
In plaats daarvan gebruiken we statistieken zoals:
- **Global Communication Index (GCI):** Succesvolle communicatierelaties tussen mensen uit verschillende taal-/culturele regio's.
- **Platform Sustainability Ratio (PSR):** Terugkerende inkomsten / terugkerende bedrijfskosten (doel ≥ 1).

### 8. Wat we expliciet niet willen (negatieve lijst)
Nexus Gaja wordt **niet** gefinancierd door:
❌ Verkoop van persoonlijke gegevens
❌ Gepersonaliseerde traditionele reclame
❌ Monitoren van gebruikersgedrag voor reclamedoeleinden
❌ Verkoop van privécommunicatiegegevens
❌ Verborgen AI-datagebruik
❌ Manipulatieve premium betaalmuren
❌ Kunstmatige bereikbeperking voor het genereren van inkomsten
❌ Betaalde politieke invloed
❌ Aankoop van bevoorrechte moderatiebeslissingen.

### 9. Voorlopige financiële architectuur
```tekst
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          GEBRUIKERS ORGANISATIES ONDERNEMING
             │ │ │
             └────────────────┼────────────────┘
                              │
                       PLATFORMDIENSTEN
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       PREMIUM DONATIES API
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               ALGEMEEN FONDS BEPERKTE FONDSEN
                                        │
                                        ▼
                                  SOCIAAL DOEL
```

### Samenvatting van de financieringsbeginselen (NG-FIN)
- **NG-FIN-001:** Geen financiering via traditionele reclame.
- **NG-FIN-002:** Geen redactionele/technische controle via financiële steun.
- **NG-FIN-003:** Persoonlijke gegevens zijn geen handelswaar.
- **NG-FIN-004:** Basiscommunicatie blijft toegankelijk zonder betaling.
- **NG-FIN-005:** Premium-aanbiedingen mogen gratis gebruikers niet degraderen.
- **NG-FIN-006:** Bestemmingsfondsen worden beheerd op basis van hun doel.
- **NG-FIN-007:** Transparant beheer van donaties en subsidies.
- **NG-FIN-008:** Commerciële B2B-diensten brengen de onafhankelijkheid niet in gevaar.
- **NG-FIN-009:** Focus op duurzaamheid in plaats van maximale inkomsten genereren.
- **NG-FIN-010:** De structuur waarborgt permanent het sociale doel.

## API, interfaces en communicatiearchitectuur (WP 1.11.3)

Om systeemstabiliteit, veiligheid en schaalbaarheid te garanderen, volgt Nexus Gaja een strikt API-first en gebeurtenisgestuurde architectuur.

### Kernprincipes
- **Geen directe databasetoegang:** Componenten communiceren uitsluitend via gedefinieerde interfaces (API's of gebeurtenissen), nooit via directe databasequery's van andere services.
- **API Gateway:** Alle externe clientverzoeken lopen via een API Gateway die de authenticatie, routering en snelheidsbeperking afhandelt.
- **Abstractie van providers:** Externe diensten (AI-modellen, betalingsproviders, vertaalmachines) worden geïntegreerd via abstractielagen, waardoor hardgecodeerde afhankelijkheden worden vermeden en flexibel wisselen van provider mogelijk wordt gemaakt.

### Communicatiepatronen
- **Synchrone API's (REST/HTTPS):** Gebruikt voor directe verzoeken zoals inloggen, profielinstellingen of directe vertalingen.
- **Asynchrone gebeurtenissen (gebeurtenisbus):** Het centrale zenuwstelsel van Nexus Gaja voor vertraagde, ontkoppelde verwerking (bijvoorbeeld 'Message.Created' die moderatie, vertaling en melding asynchroon activeert).
- **Realtime (WebSocket):** Speciale kanalen voor livechat en type-indicatoren.

### Beveiliging en betrouwbaarheid
- **Zero-Trust-model:** Intern netwerkverkeer wordt niet automatisch vertrouwd; gevoelige service-to-service-communicatie vereist authenticatie.
- **Idempotentie en Outbox-patroon:** Kritieke bewerkingen (zoals donaties of berichten) zijn ontworpen om idempotent te zijn om dubbele verwerking te voorkomen, waarbij gebruik wordt gemaakt van het Outbox-patroon om ervoor te zorgen dat gebeurtenissen nooit verloren gaan, zelfs niet tijdens databasetransacties.

## MVP-domeinmodel (WP 1.12)

Nexus Gaja maakt gebruik van een strikt domeingestuurde MVP-architectuur (ADR-025), ontworpen als een modulaire monoliet met duidelijke domeingrenzen. Deze structuur voorkomt voortijdige complexiteit van microservices, terwijl de flexibiliteit behouden blijft om specifieke domeinen later op te splitsen.

### Kerndomeinentiteiten
De architectuur scheidt expliciet verschillende concepten om de gegevensintegriteit te garanderen en structurele valkuilen zoals "Gebruikersnaam = Mens" te vermijden:
- **Identiteit en accounts:** `Persoon` ≠ `Gebruikersaccount` ≠ `Identiteitsverificatie`. Een geverifieerd persoon neemt deel via een account, maar de entiteiten blijven gescheiden.
- **Communicatie:** `Bericht` ≠ `Vertaling`. Het oorspronkelijke bericht blijft onveranderlijk; vertalingen zijn gekoppelde entiteiten.
- **Moderatie:** `Rapport` ≠ `Moderatiebesluit`. Een rapport is slechts een claim; een moderatiezaak voert het onderzoek uit.
- **Financiën:** `Donatie` ≠ `Fondssaldo`. Betalingen worden via een onveranderlijk grootboek in een fonds geboekt, waardoor financiële transparantie wordt gewaarborgd.

### Onderling verbonden domeinen
Het systeem is verdeeld in duidelijke logische domeinen (begrensde contexten): identiteit, account, organisatie, communicatie, gemeenschap, taal, moderatie, kennisgeving, financiën en bestuur. Deze domeinen brengen het hele traject in kaart, van entiteiten uit de echte wereld (gebruikers, scholen, NGO's) tot hun digitale interacties en het daarmee samenhangende bestuur.

## Projectstatus
Het project bevindt zich momenteel in de actieve architectuur- en planningsfase.
Lopende architecturale beslissingen worden gedocumenteerd in de map `/docs`.