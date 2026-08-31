# Nexus Gaja

![Nexus Gaja-logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** er et intelligent, kontekstsensitivt kommunikasjonsnettverk designet for å revolusjonere global kommunikasjon.

## Formål og visjon
I en globalisert verden er språket ofte den største barrieren. Hovedmålet til Nexus Gaja er å muliggjøre sømløs, barrierefri og kontekstuelt nøyaktig kommunikasjon mellom mennesker – uavhengig av om de snakker et felles språk.

Det handler ikke bare om å stivt oversette ord, men om å **overføre mening**. Nexus Gaja forbinder mennesker på et dypere nivå ved å forstå kulturelle, regionale og kontekstuelle nyanser, og muliggjør dermed ekte, autentiske samtaler.

## Muligheter og funksjoner
- **Multimediakommunikasjon**: Systemet behandler ikke bare tekst, men også bilde, lyd og video. Dette gir mulighet for fullstendig oppslukende samtaler (f.eks. videosamtaler eller talemeldinger) i sanntid på tvers av språkbarrierer.
- **Kontekstsensitivitet**: Gjenkjennelse av ironi, idiomer, sjargong og regionale dialekter som ofte blir misforstått av konvensjonelle oversettere.
- **Tverrplattformnettverk**: Fungerer som et grunnlag for private chatter, forumtråder (innlegg med kommentarer) og globale fellesskapsinteraksjoner.

---

## Teknisk arkitektur (kjernekonsept)

Den tekniske kjernen i Nexus Gaja er en spesialbygd kommunikasjonsmodell som er strengt delt inn i tre lag:

1. **Original**: Kommunikasjonsobjektet (meldingen) opprettet av avsenderen forblir alltid uforanderlig.
2. **Semantisk tolkning**: Systemet analyserer ikke bare ordene, men den faktiske betydningen.
3. **Representasjon av målspråk**: AI-en lager bare en midlertidig eller bufret representasjon av originalen for den respektive mottakeren basert på deres foretrukne språk. Oversettelser overskriver aldri den opprinnelige meldingen.

### Kontekstavhengighet
Oversettelser i Nexus Gaja ser aldri meldinger isolert. Motoren vurderer hele hierarkiet:
`Melding` → `Tidligere meldinger` → `Trådkontekst` → `Fellesskapskontekst` → `Språk / region` → `Brukerinnstillinger`

### Effektivitet gjennom On-Demand-oversettelse
Oversettelse skjer ressurseffektivt kun **på forespørsel** (On-Demand). Når en bruker ber om innhold, blir det oversatt til det forhåndsinnstilte språket. Når en oversettelse for et spesifikt språk er generert, lagres den permanent (bufring) for å drastisk fremskynde fremtidige forespørsler.

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

### 2. Moderasjons-AI som et undersystem
I stedet for en enkelt AI, etableres et robust delsystem:
```tekst
                 NEXUS GAJA AI MODERASJON
                          │
       ┌──────────────────┼────────────────
       │ │ │
  Språk AI Sikkerhet AI Fraud AI
       │ │ │
       ├──────────────┬───┴────────────────
       │ │ │
 Oversettelsesatferdsidentitet
 Analyse Analysesignaler
       │ │ │
       └──────────────┼────────────────
                      ▼
               Risikovurdering
                      │
                      ▼
               Menneskelig gjennomgang
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
Arkitekturen tar sikte på å oppdage syntetiske bilder, klonede stemmer og dype forfalskninger. Deteksjon er imidlertid ikke automatisk bevis.

### 17. Ingen automatisk "sannhetsmaskin" (moderering ≠ faktasjekking)
Ett system sjekker: "Bretter innholdet i strid med regler?" (Innholdsmoderering), en annen gir: "Hvilken informasjon og kilder er tilgjengelig?" (Informasjonshjelp). Meninger blir ikke bare slettet for å være "feil".

### 18. Beskyttelse mot kulturell feiltolkning
AI krever **Cultural Context Models** for å forhindre at kommunikasjonsnormene til ett land blir antatt som en global standard.

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

### 25. Arkitekturforslag og policymotor
Regler (Policy Engine) er ikke hardkodet inn i AI-modellene. AI gir funn; policymotoren bestemmer basert på gjeldende regler. Dette gir mulighet for **modellendringer uten regelendringer**.

### 26. Mennesket forblir den endelige autoriteten
- **NG-AI-MOD-001**: AI hjelper til med deteksjon og klassifisering, men erstatter ikke menneskelig vurdering ved alvorlige avgjørelser.
- **NG-AI-MOD-002**: Automatiserte modereringsbeslutninger må være sporbare, loggbare og verifiserbare.

**Sammendrag**: Vi bygger et fire-trinns system: AI-deteksjon, kontekst- og risikoanalyse, policymotor og menneskelig styring. Dette muliggjør sterk automatisering uten å skape en farlig «AI as Judge»-arkitektur.

## Prosjektstatus
Prosjektet er for tiden i den aktive arkitektur- og planleggingsfasen.
Løpende arkitektoniske beslutninger dokumenteres i mappen `/docs`.