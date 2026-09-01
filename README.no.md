# Nexus Gaja

![Nexus Gaja-logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** er et intelligent, kontekstsensitivt kommunikasjonsnettverk designet for å revolusjonere global kommunikasjon.

## Purpose and Vision
In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

Det handler ikke bare om å stivt oversette ord, men om å **overføre mening**. Nexus Gaja forbinder mennesker på et dypere nivå ved å forstå kulturelle, regionale og kontekstuelle nyanser, og muliggjør dermed ekte, autentiske samtaler.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

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

### 4. Why the Context Engine is Crucial
A pure keyword search would be insufficient. "I could kill him from laughing" semantically contains violence but is a figure of speech. "Tomorrow at 8 PM I will shoot him in front of his house" is a completely different situation. The AI must understand what the statement means in its specific context.

### 5. Flerspråklig moderering
Moderasjon kan ikke bare sammenligne ord. Den må analysere det semantiske nivået (f.eks. tyske idiomer vs. japanske idiomer vs. regionale uttrykk).

### 6. Original Language + Translation
Original and translation are analyzed separately. Only then does the "Combined Moderation Assessment" take place. This allows Nexus Gaja to determine whether the translation itself may have escalated or altered the facts.

### 7. Confidence Score
Every AI evaluation receives a confidence score (e.g., Threat probability: 0.96). However: **Confidence Score ≠ Truth.** A score of 96% only means the model is highly certain of its classification, not necessarily that the user is guilty.

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. Four Decision Zones
- 🟢 **GREEN**: Highly likely compliant. → no action.
- 🟡 **YELLOW**: Possible violation. → monitor / provide a warning if necessary.
- 🟠 **ORANGE**: Probable violation. → moderation review.
- 🔴 **RED**: Severe possible violation. → immediate protective measure + human review.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Beskyttende tiltak kan skje automatisk
I tilfelle en konkret trussel (trussel oppdaget → Høy tillit → Midlertidig begrensning → Menneskelig vurdering → Avgjørelse), beskytter vi den truede brukeren uten å gjøre AI til en dommer.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI må ikke i hemmelighet endre innhold
**Moderasjon AI må aldri endre det originale innholdet ubemerket.** Under automatisk korrigering, oversettelse eller oppsummering blir originalen alltid bevart.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Merking av AI-innhold og AI-opprinnelseslag
I henhold til gjennomsiktighetsreglene i EUs AI-lov (gjelder fra august 2026), må AI-generert innhold være identifiserbart. Vi tilbyr et AI-opprinnelseslag som lagrer metadata (AI-opprinnelse, modell, tidsstempel, menneskelig vurdering).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. Ingen straff basert på en enkelt AI-poengsum
Ingen alvorlig moderasjonsintervensjon kan være basert utelukkende på et enkelt automatisk klassifiseringsresultat (tekst + kontekst + atferd + språk + media + regelmotor = risikovurdering).

### 21. Brukeratferdssignaler og ingen sosial kredittsystem
Dette gjelder tekniske misbrukssignaler (f.eks. masseoppslag av spam), ikke et generelt sosialt rangeringssystem. Nexus Gaja opprettholder ikke et sosialt kredittsystem – moderasjon tjener sikkerhet, ikke vurderingen av en persons verdi.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Arkitekturforslag og policymotor
Regler (Policy Engine) er ikke hardkodet inn i AI-modellene. AI gir funn; policymotoren bestemmer basert på gjeldende regler. Dette gir mulighet for **modellendringer uten regelendringer**.

### 26. Mennesket forblir den endelige autoriteten
- **NG-AI-MOD-001**: AI hjelper til med deteksjon og klassifisering, men erstatter ikke menneskelig vurdering ved alvorlige avgjørelser.
- **NG-AI-MOD-002**: Automatiserte modereringsbeslutninger må være sporbare, loggbare og verifiserbare.

**Sammendrag**: Vi bygger et fire-trinns system: AI-deteksjon, kontekst- og risikoanalyse, policymotor og menneskelig styring. Dette muliggjør sterk automatisering uten å skape en farlig «AI as Judge»-arkitektur.

## Finansieringsprinsipper og inntektsmodell (WP 1.10.1)

For Nexus Gaja gjelder et svært viktig økonomisk prinsipp: **Ingen tradisjonell annonsering på plattformen.**
Dette skiller Nexus Gaja fundamentalt fra mange av dagens sosiale nettverk. Dette betyr imidlertid ikke at Nexus Gaja ikke kan ha en kommersiell karakter. Tvert imot må plattformen være økonomisk levedyktig slik at dens sosiale formål kan bestå. Økonomisk aktivitet er et middel til et mål, ikke det primære formålet med plattformen.

### 1. Principle NG-FIN-001
Nexus Gaja finances its operations through transparent revenue streams separated from user interests, and not through the monetization of its users' attention or personal data.

### 2. Ingen tradisjonell annonsering
Spesielt forbudt er:
- Bannerannonser
- Popup-annonser
- Automatisk avspilling av videoannonser
- Sponsede innlegg i standardfeeden
- Personlig tilpassede annonseprofiler
- Salg av brukerprofiler eller personopplysninger
- Reklame avledet fra private samtaler.

Nexus Gaja forblir en **kommunikasjonsplass i stedet for en reklameplass**.

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

#### Pillar 5 – Institutional Funding
Foundations, cultural funding programs, or state programs.
**NG-FIN-002:** Financial support does not buy editorial or technical control (Independence).

#### Pillar 6 – Commercial Services
B2B services like **Translation-as-a-Service** (API), organizational communication, or international conference rooms, without burdening the standard user feed.

### 4. No Data Monetization & Surveillance Economy
**NG-FIN-003:** Personal user data is not a commodity. No sale of lists, profiles, or histories. Nexus Gaja does not profit from psychological surveillance (Surveillance Economy).

### 5. Finansiell åpenhet og fondsreskontro
**Nexus Gaja Financial Transparency:** Publisering av aggregerte finansielle strukturer. Øremerkede donasjoner mottar teknisk regnskap (Fonds-ID → Formål → Saldo → Tildeling). Ingen krysssubsidiering av sosiale formål inn i bedriftsmarkedsføring.

### 6. Solidarity-Based Financing Model
Pricing is based on cost-orientation, fairness, and solidarity.
**Solidarity Premium:** A voluntary option for Premium users to finance a portion of another user's access. Forced solidarity or a premium class society (less respect/moderation for free users) is strictly prohibited.

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

### 9. Preliminary Financial Architecture
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
          USERS          ORGANIZATIONS      ENTERPRISE
             │                │                │
             └────────────────┼────────────────┘
                              │
                       PLATFORM SERVICES
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       PREMIUM             DONATIONS            API
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
               GENERAL FUND       RESTRICTED FUNDS
                                        │
                                        ▼
                                  SOCIAL PURPOSE
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

## MVP-domenemodell (WP 1.12)

Nexus Gaja bruker en strengt domenedrevet MVP-arkitektur (ADR-025), designet som en modulær monolitt med klare domenegrenser. Denne strukturen forhindrer for tidlig mikrotjenestekompleksitet samtidig som den beholder fleksibiliteten til å dele ut spesifikke domener senere.

### Kjernedomeneenheter
Arkitekturen skiller eksplisitt distinkte konsepter for å sikre dataintegritet og unngå strukturelle fallgruver som "Brukernavn = Menneske":
- **Identitet og kontoer:** `Person` ≠ `Brukerkonto` ≠ `Identitetsbekreftelse`. En verifisert person deltar via en konto, men enhetene forblir separate.
- **Kommunikasjon:** "Beskjed" ≠ "Oversettelse". Den opprinnelige meldingen forblir uforanderlig; oversettelser er koblede enheter.
- **Moderasjon:** `Rapport` ≠ `Moderasjonsbeslutning`. En rapport er bare en påstand; en moderasjonssak gjennomfører etterforskningen.
- **Økonomi:** `Donasjon` ≠ `Fondsaldo`. Betalinger bokføres via en uforanderlig hovedbok til et fond, noe som sikrer økonomisk åpenhet.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Prosjektstatus
Prosjektet er for tiden i den aktive arkitektur- og planleggingsfasen.
Løpende arkitektoniske beslutninger dokumenteres i mappen `/docs`.