# Nexus Gaja

![Nexus Gaja-logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** er et intelligent, kontekstsensitivt kommunikasjonsnettverk designet for å revolusjonere global kommunikasjon.

## Formål og visjon

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

I en globalisert verden er språket ofte den største barrieren. Hovedmålet til Nexus Gaja er å muliggjøre sømløs, barrierefri og kontekstuelt nøyaktig kommunikasjon mellom mennesker – uavhengig av om de snakker et felles språk.

Det handler ikke bare om å stivt oversette ord, men om å **overføre mening**. Nexus Gaja forbinder mennesker på et dypere nivå ved å forstå kulturelle, regionale og kontekstuelle nyanser, og muliggjør dermed ekte, autentiske samtaler.

## Muligheter og funksjoner
- **Multimediakommunikasjon**: Systemet behandler ikke bare tekst, men også bilde, lyd og video. Dette gir mulighet for fullstendig oppslukende samtaler (f.eks. videosamtaler eller talemeldinger) i sanntid på tvers av språkbarrierer.
- **Kontekstsensitivitet**: Gjenkjennelse av ironi, idiomer, sjargong og regionale dialekter som ofte blir misforstått av konvensjonelle oversettere.
- **Tverrplattformnettverk**: Fungerer som et grunnlag for private chatter, forumtråder (innlegg med kommentarer) og globale fellesskapsinteraksjoner.

---

## Technical Architecture (Core Concept)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

Den tekniske kjernen i Nexus Gaja er en spesialbygd kommunikasjonsmodell som er strengt delt inn i tre lag:

1. **Original**: Kommunikasjonsobjektet (meldingen) opprettet av avsenderen forblir alltid uforanderlig.
2. **Semantisk tolkning**: Systemet analyserer ikke bare ordene, men den faktiske betydningen.
3. **Representasjon av målspråk**: AI-en lager bare en midlertidig eller bufret representasjon av originalen for den respektive mottakeren basert på deres foretrukne språk. Oversettelser overskriver aldri den opprinnelige meldingen.

### Kontekstavhengighet
Oversettelser i Nexus Gaja ser aldri meldinger isolert. Motoren vurderer hele hierarkiet:
`Melding` → `Tidligere meldinger` → `Trådkontekst` → `Fellesskapskontekst` → `Språk / region` → `Brukerinnstillinger`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## AI-assistert moderering (WP 1.8.4)

![Nexus Gaja AI-moderasjon](assets/img/nexus_moderation.jpg)

Med AI-assistert moderering tar vi et betydelig skritt fra produktidé til teknisk arkitektur, med hensyn til gjeldende EU-regelverk (transparenskrav i EU AI-loven under Art. 50; Digital Services Act med forståelige begrunnelser og klagemuligheter).

### 1. Grunnleggende prinsipp
Den viktigste setningen for arkitekturen er: **Moderasjons-AI er et gjennomgangssystem, ikke et autonomt styringssystem.**
Den er designet for å hjelpe mennesker med måte, ikke for å bestemme selv hvilke meninger som får eksistere på Nexus Gaja.
Vi skiller mellom tre nivåer:
- **Deteksjon:** "Det kan være et regelbrudd her."
- **Evaluering:** "Sannsynligheten for regelbrudd er for eksempel 94 %."
- **Beslutning:** "Hvilke tiltak er egentlig iverksatt?"
Det tredje nivået må kontrolleres av et menneske i alvorlige tilfeller.

### 2. The Moderation AI as a Subsystem
Instead of a single AI, a robust subsystem is established:
```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Language AI        Safety AI          Fraud AI
       │                  │                  │
       ├──────────────┬───┴──────────────┬───┤
       │              │                  │
 Translation      Behaviour          Identity
 Analysis         Analysis            Signals
       │              │                  │
       └──────────────┼──────────────────┘
                      ▼
               Risk Assessment
                      │
                      ▼
               Human Review
```

### 3. De viktigste AI-modulene
Nexus Gaja bruker ni spesialiserte analyseområder:
- **M1 – Språkforståelse**: Oppdager språk, dialekt, slang, ironiindikatorer, oversettelsesproblemer.
- **M2 – Deteksjon av toksisitet/misbruk**: Oppdager fornærmelser, personlige angrep, trakassering.
- **M3 – Trusseldeteksjon**: Oppdager potensielle trusler, utpressing, voldskunngjøringer.
- **M4 – Oppdagelse av hat/dehumanisering**: Oppdager målrettede angrep på mennesker basert på spesifikke tilknytninger.
- **M5 – Spam / Manipulation Detection**: Oppdager spam, botatferd, koordinert manipulasjon.
- **M6 – Svindeldeteksjon**: Oppdager mistenkelige svindelforsøk, phishing, sosial manipulering.
- **M7 – Identitetsintegritet**: Sjekker signaler angående kontoovertakelser, flere kontoer, unndragelse av forbud.
- **M8 – Mediesikkerhet**: Analyserer bilder, lyd, video, dokumenter.
- **M9 – Context Engine**: Den viktigste modulen. Den slår sammen de enkelte funnene.

### 4. Hvorfor kontekstmotoren er avgjørende
Et rent nøkkelordsøk ville være utilstrekkelig. "Jeg kunne drept ham av å le" inneholder semantisk vold, men er en talemåte. «I morgen klokken 20 skal jeg skyte ham foran huset hans» er en helt annen situasjon. AI-en må forstå hva utsagnet betyr i sin spesifikke kontekst.

### 5. Flerspråklig moderering
Moderasjon kan ikke bare sammenligne ord. Den må analysere det semantiske nivået (f.eks. tyske idiomer vs. japanske idiomer vs. regionale uttrykk).

### 6. Originalspråk + oversettelse
Original og oversettelse analyseres separat. Først da finner "Kombinert moderasjonsvurdering" sted. Dette lar Nexus Gaja avgjøre om oversettelsen i seg selv kan ha eskalert eller endret fakta.

### 7. Tillitspoeng
Hver AI-evaluering får en konfidenspoengsum (f.eks. trusselsannsynlighet: 0,96). Imidlertid: **Confidence Score ≠ Truth.** En poengsum på 96 % betyr bare at modellen er svært sikker på sin klassifisering, ikke nødvendigvis at brukeren er skyldig.

### 8. Usikkerhet blir et signal i seg selv
Hvis AI er usikker (f.eks. Trussel: 0,62, Satire: 0,54), må den ikke bare håndheve strenge regler. I stedet bygges usikkerhet direkte inn i arkitekturen: **Human Review Required**.

### 9. Fire beslutningssoner
- **GRØNN**: Høyst sannsynlig kompatibel. → ingen handling.
- 🟡 **GUL**: Mulig brudd. → overvåk / gi en advarsel om nødvendig.
- 🟠 **ORANSJE**: Sannsynlig brudd. → moderasjonsgjennomgang.
- 🔴 **RØD**: Alvorlig mulig brudd. → øyeblikkelig beskyttelsestiltak + menneskelig vurdering.

### 10. Ingen "AI-straff"
**AI-en pålegger ingen endelige sanksjoner.** Det kan utløse tekniske umiddelbare tiltak (f.eks. midlertidig holde tilbake en melding) for alvorlige sikkerhetshensyn, men den endelige avgjørelsen forblir verifiserbar.

### 11. Beskyttende tiltak kan skje automatisk
I tilfelle en konkret trussel (trussel oppdaget → Høy tillit → Midlertidig begrensning → Menneskelig vurdering → Avgjørelse), beskytter vi den truede brukeren uten å gjøre AI til en dommer.

### 12. AI-en må være i stand til å rettferdiggjøre sine avgjørelser
DSA krever klare og spesifikke grunner. AI gir strukturert resonnement: Regel (NG-CONDUCT-004), oppdaget (potensiell konkret trussel), tillit (0,94), relevant kontekst (tidligere 4 meldinger), anbefalt handling (menneskelig vurdering).

### 13. AI må ikke i hemmelighet endre innhold
**Moderasjon AI må aldri endre det originale innholdet ubemerket.** Under automatisk korrigering, oversettelse eller oppsummering blir originalen alltid bevart.

### 14. AI-generert innhold
Vi skiller mellom: Menneskeskapt, AI-assistert, AI-generert og AI-manipulert. Dette vil bli en del av innholdets metadata.

### 15. Merking av AI-innhold og AI-opprinnelseslag
I henhold til gjennomsiktighetsreglene i EUs AI-lov (gjelder fra august 2026), må AI-generert innhold være identifiserbart. Vi tilbyr et AI-opprinnelseslag som lagrer metadata (AI-opprinnelse, modell, tidsstempel, menneskelig vurdering).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. Ingen automatisk "sannhetsmaskin" (moderering ≠ faktasjekking)
Ett system sjekker: "Bretter innholdet i strid med regler?" (Innholdsmoderering), en annen gir: "Hvilken informasjon og kilder er tilgjengelig?" (Informasjonshjelp). Meninger blir ikke bare slettet for å være "feil".

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Ironi, satire og humor
AI bruker kontekst, emojier, samtalehistorie og kjente ironistrukturer, men må tillate usikkerhet når betydningene er tvetydige.

### 20. Ingen straff basert på en enkelt AI-poengsum
Ingen alvorlig moderasjonsintervensjon kan være basert utelukkende på et enkelt automatisk klassifiseringsresultat (tekst + kontekst + atferd + språk + media + regelmotor = risikovurdering).

### 21. Brukeratferdssignaler og ingen sosial kredittsystem
Dette gjelder tekniske misbrukssignaler (f.eks. masseoppslag av spam), ikke et generelt sosialt rangeringssystem. Nexus Gaja opprettholder ikke et sosialt kredittsystem – moderasjon tjener sikkerhet, ikke vurderingen av en persons verdi.

### 22. Moderasjon AI må kunne kontrolleres
Alle relevante automatiserte avgjørelser loggføres (Event-ID, Rule-ID, Confidence, Human-Review, etc.) for å sikre sporbarhet.

### 23. Falske positive, falske negative og kvalitetsmålinger
Feiltyper overvåkes. Et dashbord måler presisjon, tilbakekalling og spesielt **Reverseringsfrekvensen for anke** (antall vellykkede anker).

### 24. Språklikhet og oversettelsesskjevhet
Modereringskvaliteten må være sammenlignbar på tvers av alle støttede språk (Multilingual Modereringsbenchmark). Hvis modereringsresultatene er forskjellige mellom originalen og oversettelsen (Oversettelseskonflikt), må dette spesifikt gjennomgås.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. Mennesket forblir den endelige autoriteten
- **NG-AI-MOD-001**: AI hjelper til med deteksjon og klassifisering, men erstatter ikke menneskelig vurdering ved alvorlige avgjørelser.
- **NG-AI-MOD-002**: Automatiserte modereringsbeslutninger må være sporbare, loggbare og verifiserbare.

**Sammendrag**: Vi bygger et fire-trinns system: AI-deteksjon, kontekst- og risikoanalyse, policymotor og menneskelig styring. Dette muliggjør sterk automatisering uten å skape en farlig «AI as Judge»-arkitektur.

## Finansieringsprinsipper og inntektsmodell (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Prinsipp NG-FIN-001
Nexus Gaja finansierer sin virksomhet gjennom transparente inntektsstrømmer atskilt fra brukerinteresser, og ikke gjennom å tjene penger på brukernes oppmerksomhet eller personlige data.

### 2. Ingen tradisjonell annonsering
Spesielt forbudt er:
- Bannerannonser
- Popup-annonser
- Automatisk avspilling av videoannonser
- Sponsede innlegg i standardfeeden
- Personlig tilpassede annonseprofiler
- Salg av brukerprofiler eller personopplysninger
- Reklame avledet fra private samtaler.

Nexus Gaja remains a **communication space rather than an advertising space**.

### 3. Finansiering uten reklame (De 6 søylene)
Finansiering er bygget på seks pilarer:
```tekst
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PREMIUM ORGANISASJONSDONASJONER
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    GIR PARTNERSKAP-TJENESTER
```

#### Pilar 1 – Gratis grunnleggende medlemskap
**Nexus Gaja Free** muliggjør grunnleggende internasjonal forståelse for alle (profiler, internasjonal kommunikasjon, innlegg, fellesskap, chatter, grunnleggende oversettelse) uten kostnad.

#### Pilar 2 – Premium-tilbud
Frivillige betalte tilbud (**Nexus Gaja Plus**) som gir større lagringsgrenser, høyere mediekvalitet, utvidede AI-kvoter og organisatoriske funksjoner.
**Viktig (Freemium i stedet for Dark Freemium):** Grunnleggende kommunikasjon må aldri forringes kunstig.

#### Pilar 3 – Organisasjoner
Spesialkontoer for skoler, universiteter, frivillige organisasjoner, bedrifter og kommuner (**Nexus Gaja Organization**). Skoler kan støttes via institusjonelle priser som multiplikatorer av internasjonal forståelse.

#### Pilar 4 – Donasjoner
**Nexus Gaja Funding Pool** godtar generelle og øremerkede donasjoner (f.eks. "for internasjonal ungdomskommunikasjon"). En **Fundallokeringsreskontro** sikrer transparent tildeling av midler.
**Formålsfond og Tombola:** En del av donasjonene mater et basseng for gratis/rabatterte bruk. En lotteri/tombola-mekanisme kan tildele disse midlene transparent og kontrollerbart.

#### Pilar 5 – Institusjonell finansiering
Stiftelser, kulturelle finansieringsprogrammer eller statlige programmer.
**NG-FIN-002:** Økonomisk støtte kjøper ikke redaksjonell eller teknisk kontroll (Uavhengighet).

#### Pilar 6 – Kommersielle tjenester
B2B-tjenester som **Translation-as-a-Service** (API), organisasjonskommunikasjon eller internasjonale konferanserom, uten å belaste standard brukerfeed.

### 4. Ingen inntektsgenerering og overvåkingsøkonomi
**NG-FIN-003:** Personlige brukerdata er ikke en vare. Ikke salg av lister, profiler eller historier. Nexus Gaja tjener ikke på psykologisk overvåking (Surveillance Economy).

### 5. Finansiell åpenhet og fondsreskontro
**Nexus Gaja Financial Transparency:** Publisering av aggregerte finansielle strukturer. Øremerkede donasjoner mottar teknisk regnskap (Fonds-ID → Formål → Saldo → Tildeling). Ingen krysssubsidiering av sosiale formål inn i bedriftsmarkedsføring.

### 6. Solidaritetsbasert finansieringsmodell
Prissetting er basert på kostnadsorientering, rettferdighet og solidaritet.
**Solidarity Premium:** Et frivillig alternativ for Premium-brukere til å finansiere en del av en annen brukers tilgang. Tvunget solidaritet eller et premiumklassesamfunn (mindre respekt/moderasjon for gratisbrukere) er strengt forbudt.

### 7. Økonomiske KPIer i stedet for engasjementsøkonomi
Ingen avhengighet av å holde brukere "online så lenge som mulig" (ingen ragebait, uendelig innmating).
I stedet bruker vi beregninger som:
- **Global Communication Index (GCI):** Vellykkede kommunikasjonsforhold mellom mennesker fra forskjellige språklige/kulturelle regioner.
- **Plattform Sustainability Ratio (PSR):** Gjentakende inntekter / tilbakevendende driftskostnader (Mål ≥ 1).

### 8. Hva vi eksplisitt ikke ønsker (negativ liste)
Nexus Gaja er **ikke** finansiert av:
❌ Salg av personopplysninger
❌ Personlig tilpasset tradisjonell reklame
❌ Overvåke brukeratferd for reklameformål
❌ Salg av privat kommunikasjonsdata
❌ Skjult AI-databruk
❌ Manipulative Premium betalingsmurer
❌ Kunstig rekkeviddebegrensning for inntektsgenerering
❌ Betalt politisk innflytelse
❌ Kjøp av privilegerte modereringsbeslutninger.

### 9. Foreløpig finansiell arkitektur
```tekst
                         NEXUS GAJA
                              │
             ┌────────────────┼──────────────
             │ │ │
             ▼ ▼ ▼
          BRUKERORGANISASJONER FORRETNING
             │ │ │
             └────────────────┼──────────────
                              │
                       PLATTFORMTJENESTER
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
                                  SOSIALT FORMÅL
```

### Sammendrag av finansieringsprinsipper (NG-FIN)
- **NG-FIN-001:** Ingen finansiering gjennom tradisjonell annonsering.
- **NG-FIN-002:** Ingen redaksjonell/teknisk kontroll gjennom økonomisk støtte.
- **NG-FIN-003:** Personopplysninger er ikke en vare.
- **NG-FIN-004:** Grunnleggende kommunikasjon forblir tilgjengelig uten betaling.
- **NG-FIN-005:** Premium-tilbud må ikke forringe gratisbrukere.
- **NG-FIN-006:** Øremerkede midler forvaltes i henhold til formålet.
- **NG-FIN-007:** Transparent håndtering av donasjoner og tilskudd.
- **NG-FIN-008:** Kommersielle B2B-tjenester går ikke på akkord med uavhengighet.
- **NG-FIN-009:** Fokuser på bærekraft i stedet for maksimal inntektsgenerering.
- **NG-FIN-010:** Strukturen sikrer varig det sosiale formålet.

## API, grensesnitt og kommunikasjonsarkitektur (WP 1.11.3)

For å sikre systemstabilitet, sikkerhet og skalerbarhet følger Nexus Gaja en strengt API-først og hendelsesdrevet arkitektur.

### Kjerneprinsipper
- **Ingen direkte databasetilgang:** Komponenter kommuniserer utelukkende via definerte grensesnitt (APIer eller hendelser), aldri gjennom direkte databasespørringer fra andre tjenester.
- **API-gateway:** Alle eksterne klientforespørsler rutes gjennom en API-gateway som håndterer autentisering, ruting og hastighetsbegrensning.
- **Tilbyderabstraksjon:** Eksterne tjenester (AI-modeller, betalingsleverandører, oversettelsesmotorer) er integrert via abstraksjonslag, og unngår hardkodede avhengigheter og muliggjør fleksibel leverandørbytte.

### Kommunikasjonsmønstre
- **Synkrone APIer (REST/HTTPS):** Brukes for umiddelbare forespørsler som pålogging, profilinnstillinger eller direkte oversettelser.
– **Asynkrone hendelser (Event Bus):** Sentralnervesystemet til Nexus Gaja for forsinket, frakoblet behandling (f.eks. «Message.Created» som utløser moderering, oversettelse og varsling asynkront).
- **Sanntid (WebSocket):** Dedikerte kanaler for live chat og skriveindikatorer.

### Sikkerhet og pålitelighet
- **Zero-Trust Model:** Intern nettverkstrafikk er ikke automatisk klarert; sensitiv tjeneste-til-tjeneste-kommunikasjon krever autentisering.
- **Idempotens og utboksmønster:** Kritiske operasjoner (som donasjoner eller meldinger) er designet for å være idempotente for å forhindre duplikatbehandling, ved å bruke utboksmønsteret for å sikre at hendelser aldri går tapt selv under databasetransaksjoner.

## MVP Domain Model (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja employs a strictly Domain-Driven MVP Architecture (ADR-025), designed as a modular monolith with clear domain boundaries. This structure prevents premature microservice complexity while retaining the flexibility to split out specific domains later.

### Core Domain Entities
The architecture explicitly separates distinct concepts to ensure data integrity and avoid structural pitfalls like "Username = Human":
- **Identity & Accounts:** `Person` ≠ `User Account` ≠ `Identity Verification`. A verified person participates via an account, but the entities remain separate.
- **Communication:** `Message` ≠ `Translation`. The original message remains immutable; translations are linked entities.
- **Moderation:** `Report` ≠ `Moderation Decision`. A report is merely a claim; a moderation case conducts the investigation.
- **Finances:** `Donation` ≠ `Fund Balance`. Payments are booked via an immutable ledger to a fund, ensuring financial transparency.

### Sammenkoblede domener
Systemet er delt inn i klare logiske domener (Bounded Contexts): Identitet, Konto, Organisasjon, Kommunikasjon, Fellesskap, Språk, Moderasjon, Varsling, Økonomi og Styring. Disse domenene kartlegger hele reisen fra virkelige enheter (brukere, skoler, frivillige organisasjoner) til deres digitale interaksjoner og relatert styring.

## Project Status
The project is currently in the active architecture and planning phase.
Ongoing architectural decisions are documented in the `/docs` folder.
