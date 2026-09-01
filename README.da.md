# Nexus Gaja

> *For global fred og gensidig forståelse*


![Nexus Gaja-logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** er et intelligent, kontekstfølsomt kommunikationsnetværk designet til at revolutionere global kommunikation.

## Formål og vision

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

I en globaliseret verden er sproget ofte den største barriere. Hovedmålet med Nexus Gaja er at muliggøre problemfri, barrierefri og kontekstuelt nøjagtig kommunikation mellem mennesker – uanset om de taler et fælles sprog.

Det handler ikke kun om stift oversættelse af ord, men om at **overføre betydning**. Nexus Gaja forbinder mennesker på et dybere niveau ved at forstå kulturelle, regionale og kontekstuelle nuancer og muliggør derved ægte, autentiske samtaler.

## Muligheder og funktioner
- **Multimediekommunikation**: Systemet behandler ikke kun tekst, men også billede, lyd og video. Dette giver mulighed for fuldstændig fordybende samtaler (f.eks. videoopkald eller talebeskeder) i realtid på tværs af sprogbarrierer.
- **Kontekstfølsomhed**: Anerkendelse af ironi, idiomer, jargon og regionale dialekter, der ofte misforstås af konventionelle oversættere.
- **Netværk på tværs af platforme**: Fungerer som grundlag for private chats, forumtråde (indlæg med kommentarer) og globale fællesskabsinteraktioner.

---

## Teknisk arkitektur (kernekoncept)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

Den tekniske kerne i Nexus Gaja er en specialbygget kommunikationsmodel, der er strengt opdelt i tre lag:

1. **Original**: Kommunikationsobjektet (meddelelsen) skabt af afsenderen forbliver altid uforanderligt.
2. **Semantisk fortolkning**: Systemet analyserer ikke kun ordene, men den faktiske betydning.
3. **Repræsentation af målsprog**: AI'en opretter blot en midlertidig eller cachelagret repræsentation af originalen for den respektive modtager baseret på deres foretrukne sprog. Oversættelser overskriver aldrig den originale besked.

### Kontekstafhængighed
Oversættelser i Nexus Gaja ser aldrig meddelelser isoleret. Motoren betragter hele hierarkiet:
`Besked` → `Tidligere beskeder` → `Trådkontekst` → `Fællesskabskontekst` → `Sprog/region` → `Brugerpræferencer`

### Effektivitet gennem On-Demand-oversættelse
Oversættelse sker kun ressourceeffektivt **efter anmodning** (On-Demand). Når en bruger anmoder om indhold, oversættes det til deres forudindstillede sprog. Når en oversættelse til et specifikt sprog er genereret, gemmes den permanent (caching) for at fremskynde fremtidige anmodninger drastisk.

## AI-assisteret moderering (WP 1.8.4)

![Nexus Gaja AI Moderering](assets/img/nexus_moderation.jpg)

Med AI-assisteret moderation tager vi et væsentligt skridt fra produktidé til teknisk arkitektur under hensyntagen til gældende EU-regler (gennemsigtighedskrav i EU AI-loven under art. 50; Digital Services Act med forståelige begrundelser og appelmuligheder).

### 1. Grundprincip
Den vigtigste sætning for arkitekturen er: **Moderation AI er et gennemgangssystem, ikke et autonomt styringssystem.**
Det er designet til at hjælpe mennesker med mådehold, ikke til selv at bestemme, hvilke meninger der må eksistere på Nexus Gaja.
Vi skelner mellem tre niveauer:
- **Opdagelse:** "Der kan være en regelovertrædelse her."
- **Evaluering:** "Sandsynligheden for en regelovertrædelse er f.eks. 94 %."
- **Beslutning:** "Hvilke handlinger tages der egentlig?"
Det tredje niveau skal kontrolleres af et menneske i alvorlige tilfælde.

### 2. Moderation AI som et undersystem
I stedet for en enkelt AI etableres et robust undersystem:
``` tekst
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼────────────────
       │ │ │
  Sprog AI Sikkerhed AI Fraud AI
       │ │ │
       ├──────────────┬───┴────────────────
       │ │ │
 Oversættelsesadfærdsidentitet
 Analyse Analyse Signaler
       │ │ │
       └──────────────┼────────────────
                      ▼
               Risikovurdering
                      │
                      ▼
               Menneskelig gennemgang
```

### 3. De vigtigste AI-moduler
Nexus Gaja anvender ni specialiserede analyseområder:
- **M1 – Sprogforståelse**: Registrerer sprog, dialekt, slang, ironiindikatorer, oversættelsesproblemer.
- **M2 – Toksicitet / Misbrugsdetektion**: Registrerer fornærmelser, personlige angreb, chikane.
- **M3 – Trusselsdetektion**: Registrerer potentielle trusler, afpresning, meddelelser om vold.
- **M4 – Opdagelse af had/dehumanisering**: Registrerer målrettede angreb på mennesker baseret på specifikke tilhørsforhold.
- **M5 – Spam / Manipulation Detection**: Detekterer spam, botadfærd, koordineret manipulation.
- **M6 – Detektion af svindel**: Registrerer mistænkelige svindelforsøg, phishing, social engineering.
- **M7 – Identitetsintegritet**: Kontrollerer signaler vedrørende kontoovertagelser, flere konti, unddragelse af forbud.
- **M8 – Mediesikkerhed**: Analyserer billeder, lyd, video, dokumenter.
- **M9 – Context Engine**: Det vigtigste modul. Det forener de enkelte fund.

### 4. Hvorfor kontekstmotoren er afgørende
En ren søgeordssøgning ville være utilstrækkelig. "Jeg kunne dræbe ham af at grine" indeholder semantisk vold, men er en talemåde. "I morgen kl. 20 skyder jeg ham foran hans hus" er en helt anden situation. AI'en skal forstå, hvad udsagnet betyder i dens specifikke kontekst.

### 5. Flersproget moderation
Mådehold kan ikke bare sammenligne ord. Den skal analysere det semantiske niveau (f.eks. tyske idiomer vs. japanske idiomer vs. regionale udtryk).

### 6. Originalsprog + Oversættelse
Original og oversættelse analyseres separat. Først derefter finder "Combined Moderation Assessment" sted. Dette giver Nexus Gaja mulighed for at afgøre, om oversættelsen i sig selv kan have eskaleret eller ændret fakta.

### 7. Tillidsresultat
Hver AI-evaluering modtager en konfidensscore (f.eks. trusselsandsynlighed: 0,96). Dog: **Confidence Score ≠ Truth.** En score på 96% betyder kun, at modellen er meget sikker på sin klassificering, ikke nødvendigvis, at brugeren er skyldig.

### 8. Usikkerhed bliver et signal i sig selv
Hvis AI'en er usikker (f.eks. Trussel: 0,62, Satire: 0,54), må den ikke blot håndhæve skrappe regler. I stedet er usikkerhed indbygget direkte i arkitekturen: **Human Review Required**.

### 9. Fire beslutningszoner
- **GRØN**: Højst sandsynligt kompatibel. → ingen handling.
- 🟡 **GUL**: Mulig overtrædelse. → overvåg / giv en advarsel om nødvendigt.
- 🟠 **ORANGE**: Sandsynlig overtrædelse. → moderationsgennemgang.
- 🔴 **RØD**: Alvorlig mulig overtrædelse. → øjeblikkelig beskyttelsesforanstaltning + menneskelig vurdering.

### 10. Ingen "AI-straf"
**AI'en pålægger ingen endelige sanktioner.** Det kan udløse tekniske øjeblikkelige foranstaltninger (f.eks. midlertidigt tilbageholde en besked) for alvorlige sikkerhedsproblemer, men den endelige beslutning forbliver verificerbar.

### 11. Beskyttende foranstaltninger kan forekomme automatisk
I tilfælde af en konkret trussel (Trussel opdaget → Høj tillid → Midlertidig begrænsning → Menneskelig gennemgang → Beslutning), beskytter vi den truede bruger uden at gøre AI'en til en dommer.

### 12. AI'en skal være i stand til at retfærdiggøre sine beslutninger
DSA kræver klare og specifikke begrundelser. AI'en giver struktureret ræsonnement: Regel (NG-CONDUCT-004), Opdaget (Potentiel konkret trussel), Tillid (0,94), Relevant kontekst (Tidligere 4 meddelelser), Anbefalet handling (Menneskelig gennemgang).

### 13. AI må ikke hemmeligt ændre indhold
**Moderation AI må aldrig ændre det originale indhold ubemærket.** Under automatisk rettelse, oversættelse eller opsummering bevares originalen altid.

### 14. AI-genereret indhold
Vi skelner mellem: Menneskeskabt, AI-assisteret, AI-genereret og AI-manipuleret. Dette bliver en del af indholdets metadata.

### 15. Mærkning af AI-indhold & AI-herkomstlag
I henhold til gennemsigtighedsreglerne i EU's AI-lov (med virkning fra august 2026) skal AI-genereret indhold være identificerbart. Vi leverer et AI-herkomstlag, der gemmer metadata (AI-oprindelse, model, tidsstempel, menneskelig gennemgang).

### 16. Deepfake Detection
Arkitekturen har til formål at detektere syntetiske billeder, klonede stemmer og deepfakes. Detektion er dog ikke automatisk bevis.

### 17. Ingen automatisk "sandhedsmaskine" (moderering ≠ faktatjek)
Et system tjekker: "Krænker indholdet reglerne?" (Content Moderation), en anden giver: "Hvilke oplysninger og kilder er tilgængelige?" (Informationshjælp). Udtalelser slettes ikke blot for at være "forkerte".

### 18. Beskyttelse mod kulturel misfortolkning
AI'en kræver **Cultural Context Models** for at forhindre, at et lands kommunikationsnormer antages som en global standard.

### 19. Ironi, satire og humor
AI'en bruger kontekst, emojis, samtalehistorie og kendte ironistrukturer, men skal give mulighed for usikkerhed, når betydninger er tvetydige.

### 20. Ingen straf baseret på en enkelt AI-score
Ingen alvorlig moderationsintervention må udelukkende være baseret på et enkelt automatisk klassificeringsresultat (tekst + kontekst + adfærd + sprog + medier + regelmotor = risikovurdering).

### 21. Brugeradfærdssignaler og intet socialt kreditsystem
Dette vedrører tekniske misbrugssignaler (f.eks. masseudsendelse af spam), ikke et generelt socialt klassificeringssystem. Nexus Gaja opretholder ikke et socialt kreditsystem – mådehold tjener sikkerhed, ikke vurderingen af ​​en persons værd.

### 22. Moderering AI skal kunne kontrolleres
Alle relevante automatiserede beslutninger logges (Begivenheds-ID, Regel-ID, Tillid, Menneskelig gennemgang osv.) for at sikre sporbarhed.

### 23. Falske positive, falske negative og kvalitetsmålinger
Fejltyper overvåges. Et dashboard måler præcision, tilbagekaldelse og især **appeltilbageførselsfrekvensen** (antal vellykkede appeller).

### 24. Sproglighed og oversættelsesbias
Modereringskvalitet skal være sammenlignelig på tværs af alle understøttede sprog (Multilingual Moderation Benchmark). Hvis modereringsresultaterne er forskellige mellem originalen og oversættelsen (Oversættelseskonflikt), skal dette specifikt gennemgås.

### 25. Arkitekturforslag og politikmotor
Regler (Policy Engine) er ikke hårdkodet i AI-modellerne. AI'en giver resultater; Policy Engine beslutter ud fra gældende regler. Dette giver mulighed for **modelændringer uden regelændringer**.

### 26. Mennesket forbliver den endelige autoritet
- **NG-AI-MOD-001**: AI'en hjælper med detektion og klassificering, men erstatter ikke menneskelig gennemgang i alvorlige beslutninger.
- **NG-AI-MOD-002**: Automatiserede modereringsbeslutninger skal kunne spores, logges og verificeres.

**Sammendrag**: Vi bygger et firetrinssystem: AI-detektion, kontekst- og risikoanalyse, politikmotor og menneskelig styring. Dette muliggør stærk automatisering uden at skabe en farlig "AI as Judge"-arkitektur.

## Finansieringsprincipper og indtægtsmodel (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

For Nexus Gaja gælder et meget vigtigt økonomisk princip: **Ingen traditionel annoncering på platformen.**
Dette adskiller Nexus Gaja fundamentalt fra mange af nutidens sociale netværk. Det betyder dog ikke, at Nexus Gaja ikke kan have en kommerciel karakter. Tværtimod skal platformen være økonomisk levedygtig, så dens sociale formål kan bestå. Økonomisk aktivitet er et middel til et mål, ikke det primære formål med platformen.

### 1. Princip NG-FIN-001
Nexus Gaja finansierer sin drift gennem gennemsigtige indtægtsstrømme adskilt fra brugerinteresser og ikke gennem indtægtsgenerering af sine brugeres opmærksomhed eller personlige data.

### 2. Ingen traditionel reklame
Specifikt forbudte er:
- Bannerannoncer
- Pop-up annoncer
- Automatisk afspilning af videoannoncer
- Sponsorerede indlæg i standardfeedet
- Personlige annonceprofiler
- Salg af brugerprofiler eller persondata
- Annoncering afledt af private samtaler.

Nexus Gaja forbliver et **kommunikationsområde snarere end et reklameområde**.

### 3. Finansiering uden reklame (De 6 søjler)
Finansiering bygger på seks søjler:
``` tekst
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PREMIUM ORGANISATION DONATIONER
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    TILDELER PARTNERSKABER-TJENESTER
```

#### Pillar 1 – Free Basic Membership
**Nexus Gaja Free** enables basic international understanding for everyone (profile, international communication, posts, communities, chats, basic translation) at no cost.

#### Søjle 2 – Premium-tilbud
Frivillige betalte tilbud (**Nexus Gaja Plus**) giver større lagergrænser, højere mediekvalitet, udvidede AI-kvoter og organisatoriske funktioner.
**Vigtigt (Freemium i stedet for Dark Freemium):** Grundlæggende kommunikation må aldrig forringes kunstigt.

#### Søjle 3 – Organisationer
Særlige konti for skoler, universiteter, ngo'er, virksomheder og kommuner (**Nexus Gaja Organisation**). Skoler kan støttes via institutionelle takster som multiplikatorer af international forståelse.

#### Søjle 4 – Donationer
**Nexus Gaja Funding Pool** accepterer generelle og øremærkede donationer (f.eks. "til international ungdomskommunikation"). En **Fundallokeringsledger** sikrer gennemsigtig fordeling af midler.
**Purpose Fund & Tombola:** En del af donationerne tilfører en pulje til gratis/rabat. En lotteri/tombola-mekanisme kan allokere disse midler gennemsigtigt og kontrollerbart.

#### Pillar 5 – Institutional Funding
Foundations, cultural funding programs, or state programs.
**NG-FIN-002:** Financial support does not buy editorial or technical control (Independence).

#### Søjle 6 – Kommercielle tjenester
B2B-tjenester som **Translation-as-a-Service** (API), organisatorisk kommunikation eller internationale konferencelokaler, uden at belaste standardbrugerfeedet.

### 4. Ingen indtægtsgenerering og overvågningsøkonomi
**NG-FIN-003:** Personlige brugerdata er ikke en handelsvare. Intet salg af lister, profiler eller historier. Nexus Gaja tjener ikke på psykologisk overvågning (Surveillance Economy).

### 5. Financial Transparency & Fund Ledger
**Nexus Gaja Financial Transparency:** Publication of aggregated financial structures. Earmarked donations receive technical accounting (Fund ID → Purpose → Balance → Allocation). No cross-subsidization of social purposes into corporate marketing.

### 6. Solidarity-Based Financing Model
Pricing is based on cost-orientation, fairness, and solidarity.
**Solidarity Premium:** A voluntary option for Premium users to finance a portion of another user's access. Forced solidarity or a premium class society (less respect/moderation for free users) is strictly prohibited.

### 7. Økonomiske KPI'er i stedet for engagementsøkonomi
Ingen afhængighed af at holde brugere "online så længe som muligt" (ingen ragebait, uendelige feeds).
I stedet bruger vi metrics som:
- **Global Communication Index (GCI):** Succesfulde kommunikationsforhold mellem mennesker fra forskellige sproglige/kulturelle regioner.
- **Platform Sustainability Ratio (PSR):** Tilbagevendende omsætning / tilbagevendende driftsomkostninger (Mål ≥ 1).

### 8. Hvad vi udtrykkeligt ikke ønsker (negativ liste)
Nexus Gaja er **ikke** finansieret af:
❌ Salg af persondata
❌ Personlig traditionel reklame
❌ Overvågning af brugeradfærd til reklameformål
❌ Salg af private kommunikationsdata
❌ Skjult AI-databrug
❌ Manipulative Premium betalingsvægge
❌ Kunstig rækkeviddebegrænsning for indtægtsgenerering
❌ Betalt politisk indflydelse
❌ Køb af privilegerede moderationsbeslutninger.

### 9. Foreløbig finansiel arkitektur
``` tekst
                         NEXUS GAJA
                              │
             ┌────────────────┼──────────────
             │ │ │
             ▼ ▼ ▼
          BRUGERORGANISATIONER VIRKSOMHEDEN
             │ │ │
             └────────────────┼──────────────
                              │
                       PLATFORMTJENESTER
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       PREMIUM DONATIONS API
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               GENERELLE FONDSBEGRENSEDE MIDLER
                                        │
                                        ▼
                                  SOCIALT FORMÅL
```

### Sammenfatning af finansieringsprincipper (NG-FIN)
- **NG-FIN-001:** Ingen finansiering gennem traditionel reklame.
- **NG-FIN-002:** Ingen redaktionel/teknisk kontrol gennem økonomisk støtte.
- **NG-FIN-003:** Personlige data er ikke en handelsvare.
- **NG-FIN-004:** Grundlæggende kommunikation forbliver tilgængelig uden betaling.
- **NG-FIN-005:** Premium-tilbud må ikke forringe gratis brugere.
- **NG-FIN-006:** Øremærkede midler forvaltes i overensstemmelse med deres formål.
- **NG-FIN-007:** Gennemsigtig håndtering af donationer og tilskud.
- **NG-FIN-008:** Kommercielle B2B-tjenester kompromitterer ikke uafhængighed.
- **NG-FIN-009:** Fokus på bæredygtighed frem for maksimal indtægtsgenerering.
- **NG-FIN-010:** Strukturen sikrer permanent det sociale formål.

## API, grænseflader og kommunikationsarkitektur (WP 1.11.3)

For at sikre systemstabilitet, sikkerhed og skalerbarhed følger Nexus Gaja en strengt API-først og begivenhedsdrevet arkitektur.

### Kerneprincipper
- **Ingen direkte databaseadgang:** Komponenter kommunikerer udelukkende via definerede grænseflader (API'er eller hændelser), aldrig gennem direkte databaseforespørgsler fra andre tjenester.
- **API-gateway:** Alle eksterne klientanmodninger rutes gennem en API-gateway, der håndterer godkendelse, routing og hastighedsbegrænsning.
- **Udbyderabstraktion:** Eksterne tjenester (AI-modeller, betalingsudbydere, oversættelsesmotorer) er integreret via abstraktionslag, der undgår hårdkodede afhængigheder og muliggør fleksibel udbyderbytning.

### Kommunikationsmønstre
- **Synkrone API'er (REST/HTTPS):** Bruges til øjeblikkelige anmodninger som login, profilindstillinger eller direkte oversættelser.
- **Asynkrone hændelser (hændelsesbus):** Centralnervesystemet i Nexus Gaja til forsinket, afkoblet behandling (f.eks. "Message.Created", der udløser moderering, oversættelse og meddelelse asynkront).
- **Realtid (WebSocket):** Dedikerede kanaler til livechat og skriveindikatorer.

### Sikkerhed og pålidelighed
- **Nul-Trust Model:** Intern netværkstrafik er ikke automatisk tillid til; Følsom service-til-service-kommunikation kræver godkendelse.
- **Idempotens og udbakkemønster:** Kritiske operationer (som donationer eller meddelelser) er designet til at være idempotente for at forhindre duplikatbehandling ved at bruge udbakkemønsteret til at sikre, at begivenheder aldrig går tabt, selv under databasetransaktioner.

## MVP-domænemodel (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja anvender en strengt domænedrevet MVP-arkitektur (ADR-025), designet som en modulær monolit med klare domænegrænser. Denne struktur forhindrer for tidlig mikroservicekompleksitet, mens den bevarer fleksibiliteten til at opdele specifikke domæner senere.

### Kernedomæneenheder
Arkitekturen adskiller eksplicit forskellige begreber for at sikre dataintegritet og undgå strukturelle faldgruber som "Brugernavn = Menneske":
- **Identitet og konti:** `Person` ≠ `Brugerkonto` ≠ `Identitetsbekræftelse`. En verificeret person deltager via en konto, men enhederne forbliver adskilte.
- **Kommunikation:** `Besked` ≠ `Oversættelse`. Den oprindelige besked forbliver uforanderlig; oversættelser er sammenkædede enheder.
- **Moderation:** `Rapport` ≠ `Moderationsbeslutning`. En rapport er blot en påstand; en moderationssag varetager undersøgelsen.
- **Økonomi:** `Donation` ≠ `Fondssaldo`. Betalinger bogføres via en uforanderlig hovedbog til en fond, hvilket sikrer finansiel gennemsigtighed.

### Sammenkoblede domæner
Systemet er opdelt i klare logiske domæner (Bounded Contexts): Identitet, Konto, Organisation, Kommunikation, Fællesskab, Sprog, Moderering, Notifikation, Økonomi og Governance. Disse domæner kortlægger hele rejsen fra enheder i den virkelige verden (brugere, skoler, ngo'er) til deres digitale interaktioner og relaterede styring.

## Projektstatus
Projektet er i øjeblikket i den aktive arkitektur- og planlægningsfase.
Løbende arkitektoniske beslutninger dokumenteres i mappen `/docs`.

---

---

## Licens og intellektuel ejendom

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Alle rettigheder forbeholdes.**

**Nexus Gaja** er den eksklusive intellektuelle ejendom tilhørende **Jan Friske**, der opererer under **SonnerStudio**.

Jan Friske er den eneste skaber, arkitekt og ejer af Nexus Gaja - inklusive alle koncepter, arkitektur, domænemodeller, brandidentitet og tilhørende dokumentation.

**Ingen rettigheder, licenser eller ejerskab er ejet af nogen tredjepart**, uanset deres størrelse, markedsposition eller indflydelse i teknologiindustrien.

### Hvad er IKKE tilladt uden udtrykkeligt skriftligt samtykke:
- Kopiering, reproduktion eller distribution af denne software eller dens dokumentation
- Ændring, tilpasning eller skabelse af afledte værker
- Kommerciel brug af enhver del af Nexus Gaja
- Brug af indholdet af dette lager som træningsdata for AI- eller LLM-systemer
- Underlicensering eller overførsel af rettigheder til tredjepart

### Beskyttet intellektuel ejendom
Følgende originale koncepter er beskyttet som forretningshemmeligheder og proprietære kreationer af Jan Friske:
- Den lagdelte kommunikationsmodel (original, semantisk fortolkning, oversat output)
- Identitetsadskillelsesprincippet (Person er ikke konto er ikke identitetsbekræftelse)
- Message-Translation afkoblingsmodellen (Meddelelsen er ikke oversættelse)
- AI-moderationsstyringsrammerne

### Kontakt
For licensforespørgsler: https://github.com/SonnerStudio

Nexus Gaja og Nexus Gaja-logoet er varemærker tilhørende Jan Friske. Uautoriseret brug af navnet eller mærket er forbudt.

Se de fulde licensvilkår i LICENS-filen.
