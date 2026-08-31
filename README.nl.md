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

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

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

### 3. De belangrijkste AI-modules
Nexus Gaja maakt gebruik van negen gespecialiseerde analysegebieden:
- **M1 – Taalbegrip**: Detecteert taal, dialect, slang, ironie-indicatoren, vertaalproblemen.
- **M2 – Detectie van toxiciteit/misbruik**: Detecteert beledigingen, persoonlijke aanvallen en intimidatie.
- **M3 – Bedreigingsdetectie**: Detecteert potentiële bedreigingen, chantage en aankondigingen van geweld.
- **M4 – Detectie van haat/ontmenselijking**: Detecteert gerichte aanvallen op mensen op basis van specifieke voorkeuren.
- **M5 – Spam-/manipulatiedetectie**: detecteert spam, botgedrag en gecoördineerde manipulatie.
- **M6 – Fraudedetectie**: Detecteert verdachte fraudepogingen, phishing, social engineering.
- **M7 – Identiteitsintegriteit**: Controleert signalen met betrekking tot accountovernames, meerdere accounts, ontduiking van verboden.
- **M8 – Mediaveiligheid**: analyseert afbeeldingen, audio, video en documenten.
- **M9 – Context Engine**: de belangrijkste module. Het voegt de afzonderlijke bevindingen samen.

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
** Moderatie-AI mag de originele inhoud nooit onopgemerkt wijzigen. ** Tijdens automatische correctie, vertaling of samenvatting blijft het origineel altijd behouden.

### 14. AI-gegenereerde inhoud
We maken onderscheid tussen: door mensen gecreëerd, door AI ondersteund, door AI gegenereerd en door AI gemanipuleerd. Dit wordt onderdeel van de contentmetadata.

### 15. Labeling van AI-inhoud en AI-herkomstlaag
Volgens de transparantieregels van de EU AI Act (van kracht vanaf augustus 2026) moet door AI gegenereerde inhoud identificeerbaar zijn. We bieden een AI-herkomstlaag die metadata opslaat (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake-detectie
De architectuur is bedoeld om synthetische beelden, gekloonde stemmen en deepfakes te detecteren. Detectie is echter niet automatisch bewijs.

### 17. Geen automatische ‘waarheidsmachine’ (moderatie ≠ feitencontrole)
Eén systeem controleert: "Schendt de inhoud de regels?" (Contentmoderatie), zegt een ander: "Welke informatie en bronnen zijn beschikbaar?" (Informatiehulp). Meningen worden niet simpelweg verwijderd omdat ze ‘fout’ zijn.

### 18. Bescherming tegen culturele misinterpretatie
De AI heeft **Culturele Contextmodellen** nodig om te voorkomen dat de communicatienormen van één land als mondiale standaard worden aangenomen.

### 19. Ironie, satire en humor
De AI maakt gebruik van context, emoji's, gespreksgeschiedenis en bekende ironische structuren, maar moet onzekerheid mogelijk maken wanneer betekenissen dubbelzinnig zijn.

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. Signalen van gebruikersgedrag en geen sociaal kredietsysteem
Dit heeft betrekking op signalen van technisch misbruik (bijvoorbeeld het massaal posten van spam), en niet op een algemeen sociaal beoordelingssysteem. Nexus Gaja hanteert geen sociaal kredietsysteem – gematigdheid dient de veiligheid, niet de beoordeling van iemands waarde.

### 22. Moderatie-AI moet controleerbaar zijn
Alle relevante geautomatiseerde beslissingen worden geregistreerd (Event-ID, Rule-ID, Confidence, Human-Review, etc.) om de traceerbaarheid te garanderen.

### 23. Valse positieven, valse negatieven en kwaliteitsstatistieken
Fouttypen worden gecontroleerd. Een dashboard meet precisie, herinnering en vooral het **Beroepsomkeringspercentage** (aantal succesvolle beroepen).

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Architectuurvoorstel en beleidsengine
Regels (Policy Engine) zijn niet hardgecodeerd in de AI-modellen. De AI levert bevindingen; de Policy Engine beslist op basis van de huidige regels. Hierdoor zijn **modelwijzigingen mogelijk zonder regelwijzigingen**.

### 26. De mens blijft de uiteindelijke autoriteit
- **NG-AI-MOD-001**: De AI helpt bij detectie en classificatie, maar vervangt niet de menselijke beoordeling bij ernstige beslissingen.
- **NG-AI-MOD-002**: Geautomatiseerde moderatiebeslissingen moeten traceerbaar, logbaar en verifieerbaar zijn.

**Samenvatting**: We bouwen een systeem in vier fasen: AI-detectie, context- en risicoanalyse, beleidsengine en menselijk bestuur. Dit maakt sterke automatisering mogelijk zonder dat er een gevaarlijke ‘AI as Judge’-architectuur ontstaat.

## Projectstatus
Het project bevindt zich momenteel in de actieve architectuur- en planningsfase.
Lopende architecturale beslissingen worden gedocumenteerd in de map `/docs`.