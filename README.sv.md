# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** är ett intelligent, sammanhangskänsligt kommunikationsnätverk designat för att revolutionera global kommunikation.

## Syfte och vision
I en globaliserad värld är språket ofta den största barriären. Huvudmålet med Nexus Gaja är att möjliggöra sömlös, barriärfri och kontextuellt korrekt kommunikation mellan människor – oavsett om de talar ett gemensamt språk.

Det handlar inte bara om att stelbent översätta ord, utan om att **överföra betydelse**. Nexus Gaja förbinder människor på en djupare nivå genom att förstå kulturella, regionala och kontextuella nyanser, vilket möjliggör genuina, autentiska konversationer.

## Möjligheter och funktioner
- **Multimediakommunikation**: Systemet bearbetar inte bara text utan även bild, ljud och video. Detta möjliggör helt uppslukande konversationer (t.ex. videosamtal eller röstmeddelanden) i realtid över språkbarriärer.
- **Kontextkänslighet**: Erkännande av ironi, idiom, jargong och regionala dialekter som ofta missförstås av konventionella översättare.
- **Cross-Platform Network**: Fungerar som en grund för privata chattar, forumtrådar (inlägg med kommentarer) och globala gemenskapsinteraktioner.

---

## Teknisk arkitektur (kärnkoncept)

Den tekniska kärnan i Nexus Gaja är en specialbyggd kommunikationsmodell som är strikt uppdelad i tre lager:

1. **Original**: Kommunikationsobjektet (meddelandet) skapat av avsändaren förblir alltid oföränderligt.
2. **Semantisk tolkning**: Systemet analyserar inte bara orden, utan den faktiska betydelsen.
3. **Representation av målspråk**: AI:n skapar bara en tillfällig eller cachad representation av originalet för respektive mottagare baserat på deras föredragna språk. Översättningar skriver aldrig över det ursprungliga meddelandet.

### Kontextberoende
Översättningar i Nexus Gaja ser aldrig meddelanden isolerat. Motorn tar hänsyn till hela hierarkin:
`Meddelande` → `Tidigare meddelanden` → `Trådkontext` → `Community Context` → `Språk/region` → `Användarinställningar`

### Effektivitet genom översättning på begäran
Översättning sker resurseffektivt endast **på begäran** (On-Demand). När en användare begär innehåll översätts det till deras förinställda språk. När en översättning för ett specifikt språk har genererats lagras den permanent (cache) för att drastiskt påskynda framtida förfrågningar.

## AI-assisterad moderering (WP 1.8.4)

Med AI-assisterad moderering tar vi ett betydande steg från produktidé till teknisk arkitektur, med hänsyn tagen till gällande EU-förordningar (transparenskrav i EU:s AI-lag enligt art. 50; Digital Services Act med begripliga motiveringar och överklagandemöjligheter).

### 1. Grundprincip
Den viktigaste meningen för arkitekturen är: **Moderationen AI är ett granskningssystem, inte ett autonomt härskarsystem.**
Den är utformad för att hjälpa människor med måtta, inte för att själv avgöra vilka åsikter som tillåts finnas på Nexus Gaja.
Vi skiljer på tre nivåer:
- **Detektering:** "Det kan finnas ett regelbrott här."
- **Utvärdering:** "Sannolikheten för ett regelbrott är till exempel 94 %."
- **Beslut:** "Vilka åtgärder vidtas egentligen?"
Den tredje nivån måste kontrolleras av en människa i allvarliga fall.

### 2. Modererings-AI som ett delsystem
Istället för en enda AI etableras ett robust delsystem:
```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼────────────────
       │ │ │
  Språk AI Säkerhet AI Bedrägeri AI
       │ │ │
       ├──────────────┬───┴────────────────
       │ │ │
 Översättningsbeteendeidentitet
 Analys Analyssignaler
       │ │ │
       └──────────────┼────────────────
                      ▼
               Riskbedömning
                      │
                      ▼
               Mänsklig recension
```

### 3. De viktigaste AI-modulerna
Nexus Gaja använder nio specialiserade analysområden:
- **M1 – Språkförståelse**: Upptäcker språk, dialekt, slang, ironiindikatorer, översättningsproblem.
- **M2 – Detektering av toxicitet/missbruk**: Upptäcker förolämpningar, personangrepp, trakasserier.
- **M3 – Hotdetektion**: Upptäcker potentiella hot, utpressning, meddelanden om våld.
- **M4 – Detektering av hat/avhumanisering**: Upptäcker riktade attacker mot människor baserat på specifika tillhörigheter.
- **M5 – Spam / Manipulation Detection**: Upptäcker spam, botbeteende, koordinerad manipulation.
- **M6 – Bedrägeriupptäckt**: Upptäcker misstänkta bedrägeriförsök, nätfiske, social ingenjörskonst.
- **M7 – Identitetsintegritet**: Kontrollerar signaler om kontoövertaganden, flera konton, förbudsflykt.
- **M8 – Mediasäkerhet**: Analyserar bilder, ljud, video, dokument.
- **M9 – Context Engine**: Den viktigaste modulen. Det slår samman de individuella fynden.

### 4. Varför Context Engine är avgörande
En ren nyckelordssökning skulle vara otillräcklig. "Jag skulle kunna döda honom av att skratta" innehåller semantiskt våld men är ett tal. "I morgon kl 20 skjuter jag honom framför hans hus" är en helt annan situation. AI:n måste förstå vad uttalandet betyder i sitt specifika sammanhang.

### 5. Flerspråkig moderering
Måttlighet kan inte bara jämföra ord. Den måste analysera den semantiska nivån (t.ex. tyska idiom vs. japanska idiom vs. regionala uttryck).

### 6. Originalspråk + översättning
Original och översättning analyseras separat. Först därefter sker "Combined Moderation Assessment". Detta gör att Nexus Gaja kan avgöra om översättningen i sig kan ha eskalerat eller ändrat fakta.

### 7. Förtroendepoäng
Varje AI-utvärdering får ett konfidenspoäng (t.ex. Hotsannolikhet: 0,96). Men: **Förtroendepoäng ≠ Sanning.** En poäng på 96% betyder bara att modellen är mycket säker på sin klassificering, inte nödvändigtvis att användaren är skyldig.

### 8. Osäkerhet blir en signal i sig
Om AI:n är osäker (t.ex. Hot: 0,62, Satir: 0,54), får den inte bara genomdriva hårda regler. Istället byggs osäkerheten in direkt i arkitekturen: **Human Review Required**.

### 9. Fyra beslutszoner
- **GRÖN**: Högst sannolikt kompatibel. → ingen åtgärd.
- 🟡 **GUL**: Möjlig överträdelse. → övervaka / ge en varning vid behov.
- **ORANGE**: Trolig överträdelse. → moderationsgranskning.
- 🔴 **RÖD**: Allvarlig möjlig överträdelse. → omedelbar skyddsåtgärd + mänsklig granskning.

### 10. Inget "AI-straff"
**AI:n inför inga slutgiltiga sanktioner.** Det kan utlösa tekniska omedelbara åtgärder (t.ex. tillfälligt hålla tillbaka ett meddelande) för allvarliga säkerhetsproblem, men det slutliga beslutet förblir verifierbart.

### 11. Skyddsåtgärder kan ske automatiskt
I händelse av ett konkret hot (Hot upptäckt → Högt förtroende → Tillfällig begränsning → Mänsklig granskning → Beslut) skyddar vi den hotade användaren utan att förvandla AI:n till en domare.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI får inte ändra innehåll i hemlighet
**Moderation AI får aldrig ändra det ursprungliga innehållet obemärkt.** Under automatisk korrigering, översättning eller sammanfattning bevaras originalet alltid.

### 14. AI-genererat innehåll
Vi skiljer på: Människoskapad, AI-assisterad, AI-genererad och AI-manipulerad. Detta kommer att bli en del av innehållets metadata.

### 15. Märkning av AI-innehåll & AI-härkomstskikt
Enligt öppenhetsreglerna i EU AI Act (gäller i augusti 2026) måste AI-genererat innehåll vara identifierbart. Vi tillhandahåller ett AI-härkomstlager som lagrar metadata (AI-ursprung, modell, tidsstämpel, mänsklig granskning).

### 16. Deepfake Detection
Arkitekturen syftar till att upptäcka syntetiska bilder, klonade röster och deepfakes. Detektering är dock inte automatiskt bevis.

### 17. Ingen automatisk "Sanningsmaskin" (Moderation ≠ Faktakontroll)
Ett system kontrollerar: "Bretter innehållet mot reglerna?" (Innehållsmoderering), en annan ger: "Vilken information och källor finns tillgängliga?" (Informationshjälp). Åsikter raderas inte bara för att de är "fel".

### 18. Skydd mot kulturell misstolkning
AI kräver **Cultural Context Models** för att förhindra att kommunikationsnormerna i ett land antas vara en global standard.

### 19. Ironi, satir och humor
AI:n använder sammanhang, emojis, konversationshistorik och kända ironistrukturer, men måste tillåta osäkerhet när betydelser är tvetydiga.

### 20. Inget straff baserat på en enda AI-poäng
Inget allvarligt modereringsingrepp får baseras enbart på ett enda automatiskt klassificeringsresultat (Text + Kontext + Beteende + Språk + Media + Regelmotor = Riskbedömning).

### 21. Signaler för användarbeteende och inget socialt kreditsystem
Detta gäller tekniska missbrukssignaler (t.ex. masspublicering av spam), inte ett allmänt socialt klassificeringssystem. Nexus Gaja har inget socialt kreditsystem – måttfullhet tjänar trygghet, inte bedömningen av en persons värde.

### 22. Moderering AI måste kunna granskas
Alla relevanta automatiserade beslut loggas (Event-ID, Rule-ID, Confidence, Human-Review, etc.) för att säkerställa spårbarhet.

### 23. Falska positiva, falska negativa och kvalitetsmått
Feltyper övervakas. En instrumentbräda mäter precision, återkallelse och särskilt **frekvens för överklagande** (antal lyckade överklaganden).

### 24. Språkjämlikhet och översättningsbias
Modereringskvaliteten måste vara jämförbar på alla språk som stöds (Multilingual Modereringsbenchmark). Om modereringsresultaten skiljer sig mellan originalet och översättningen (Översättningskonflikt), måste detta granskas specifikt.

### 25. Arkitekturförslag och policymotor
Regler (Policy Engine) är inte hårdkodade i AI-modellerna. AI ger resultat; Policymotorn bestämmer utifrån gällande regler. Detta möjliggör **modelländringar utan regeländringar**.

### 26. Människan förblir den slutliga auktoriteten
- **NG-AI-MOD-001**: AI:n hjälper till med upptäckt och klassificering, men ersätter inte mänsklig granskning vid allvarliga beslut.
- **NG-AI-MOD-002**: Automatiserade modereringsbeslut måste vara spårbara, loggbara och verifierbara.

**Sammanfattning**: Vi bygger ett system i fyra steg: AI-detektion, kontext- och riskanalys, policymotor och mänsklig styrning. Detta möjliggör stark automatisering utan att skapa en farlig "AI as Judge"-arkitektur.

## Finansieringsprinciper och intäktsmodell (WP 1.10.1)

För Nexus Gaja gäller en mycket viktig ekonomisk princip: **Ingen traditionell reklam inom plattformen.**
Detta skiljer Nexus Gaja i grunden från många av dagens sociala nätverk. Det betyder dock inte att Nexus Gaja inte kan ha en kommersiell karaktär. Tvärtom måste plattformen vara ekonomiskt gångbar så att dess sociala syfte kan bestå. Ekonomisk aktivitet är ett medel för att uppnå ett mål, inte det primära syftet med plattformen.

### 1. Princip NG-FIN-001
Nexus Gaja finansierar sin verksamhet genom transparenta intäktsströmmar separerade från användarintressen, och inte genom att tjäna pengar på användarnas uppmärksamhet eller personliga data.

### 2. Ingen traditionell reklam
Specifikt förbjudna är:
- Bannerannonser
- Popup-annonser
- Videoannonser som spelas upp automatiskt
- Sponsrade inlägg i standardflödet
- Personliga annonsprofiler
- Försäljning av användarprofiler eller personuppgifter
- Reklam härrör från privata samtal.

Nexus Gaja förblir ett **kommunikationsutrymme snarare än ett reklamutrymme**.

### 3. Finansiering utan reklam (de 6 pelarna)
Finansieringen bygger på sex pelare:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PREMIUM ORGANISATION DONATIONER
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    BIDRAR PARTNERSKAP TJÄNSTER
```

#### Pelare 1 – Gratis grundläggande medlemskap
**Nexus Gaja Free** möjliggör grundläggande internationell förståelse för alla (profiler, internationell kommunikation, inlägg, gemenskaper, chattar, grundläggande översättning) utan kostnad.

#### Pelare 2 – Premiumerbjudanden
Frivilliga betalda erbjudanden (**Nexus Gaja Plus**) som ger större lagringsgränser, högre mediekvalitet, utökade AI-kvoter och organisatoriska funktioner.
**Viktigt (Freemium istället för Dark Freemium):** Grundläggande kommunikation får aldrig försämras på konstgjord väg.

#### Pelare 3 – Organisationer
Särskilda konton för skolor, universitet, icke-statliga organisationer, företag och kommuner (**Nexus Gaja Organization**). Skolor kan få stöd via institutionella priser som multiplikatorer av internationell förståelse.

#### Pelare 4 – Donationer
**Nexus Gaja Funding Pool** tar emot allmänna och öronmärkta donationer (t.ex. "för internationell ungdomskommunikation"). En **Fondsallokeringsreskontra** säkerställer en transparent allokering av medel.
**Purpose Fund & Tombola:** En del av donationerna matar en pool för gratis/rabatterad användning. En lotteri-/tombolamekanism kan fördela dessa medel på ett transparent och auditibelt sätt.

#### Pelare 5 – Institutionell finansiering
Stiftelser, kulturfinansieringsprogram eller statliga program.
**NG-FIN-002:** Ekonomiskt stöd köper inte redaktionell eller teknisk kontroll (Oberoende).

#### Pelare 6 – Kommersiella tjänster
B2B-tjänster som **Translation-as-a-Service** (API), organisationskommunikation eller internationella konferensrum, utan att belasta standardanvändarflödet.

### 4. Ingen datainkomst och övervakningsekonomi
**NG-FIN-003:** Personlig användardata är inte en handelsvara. Ingen försäljning av listor, profiler eller historier. Nexus Gaja tjänar inte på psykologisk övervakning (Surveillance Economy).

### 5. Finansiell insyn och fondbok
**Nexus Gaja Financial Transparency:** Publicering av aggregerade finansiella strukturer. Öronmärkta donationer får teknisk redovisning (Fond-ID → Syfte → Saldo → Allokering). Ingen korssubventionering av sociala ändamål till företagsmarknadsföring.

### 6. Solidaritetsbaserad finansieringsmodell
Prissättningen baseras på kostnadsorientering, rättvisa och solidaritet.
**Solidarity Premium:** Ett frivilligt alternativ för Premium-användare att finansiera en del av en annan användares åtkomst. Påtvingad solidaritet eller ett premiumklasssamhälle (mindre respekt/måttfullhet för fria användare) är strängt förbjudet.

### 7. Ekonomiska nyckeltal istället för engagemangsekonomi
Inget beroende av att hålla användarna "online så länge som möjligt" (ingen ragebait, oändliga flöden).
Istället använder vi statistik som:
- **Global Communication Index (GCI):** Framgångsrika kommunikationsrelationer mellan människor från olika språkliga/kulturella regioner.
- **Platform Sustainability Ratio (PSR):** Återkommande intäkter / återkommande driftskostnader (Mål ≥ 1).

### 8. Vad vi uttryckligen inte vill ha (negativ lista)
Nexus Gaja finansieras **inte** av:
❌ Försäljning av personuppgifter
❌ Personlig traditionell reklam
❌ Övervaka användarbeteende i reklamsyfte
❌ Försäljning av privat kommunikationsdata
❌ Dold AI-dataanvändning
❌ Manipulativa Premium-betalväggar
❌ Artificiell räckviddsbegränsning för intäktsgenerering
❌ Betalt politiskt inflytande
❌ Köp av privilegierade modereringsbeslut.

### 9. Preliminär finansiell arkitektur
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼──────────────
             │ │ │
             ▼ ▼ ▼
          ANVÄNDARORGANISATIONER FÖRETAG
             │ │ │
             └────────────────┼──────────────
                              │
                       PLATTFORMTJÄNSTER
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       PREMIUM DONATIONS API
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               ALLMÄNNA FONDBEGRÄNSADE MEDEL
                                        │
                                        ▼
                                  SOCIALT SYFTE
```

### Sammanfattning av finansieringsprinciper (NG-FIN)
- **NG-FIN-001:** Ingen finansiering genom traditionell reklam.
- **NG-FIN-002:** Ingen redaktionell/teknisk kontroll genom ekonomiskt stöd.
- **NG-FIN-003:** Personuppgifter är inte en handelsvara.
- **NG-FIN-004:** Grundläggande kommunikation förblir tillgänglig utan betalning.
- **NG-FIN-005:** Premiumerbjudanden får inte försämra gratisanvändare.
- **NG-FIN-006:** Öronmärkta medel förvaltas enligt deras syfte.
- **NG-FIN-007:** Transparent hantering av donationer och bidrag.
- **NG-FIN-008:** Kommersiella B2B-tjänster äventyrar inte oberoendet.
- **NG-FIN-009:** Fokusera på hållbarhet snarare än maximal intäktsgenerering.
- **NG-FIN-010:** Strukturen säkrar permanent det sociala syftet.

## API, gränssnitt och kommunikationsarkitektur (WP 1.11.3)

För att säkerställa systemstabilitet, säkerhet och skalbarhet följer Nexus Gaja en strikt API-först och händelsedriven arkitektur.

### Kärnprinciper
- **Ingen direkt databasåtkomst:** Komponenter kommunicerar uteslutande via definierade gränssnitt (API eller händelser), aldrig genom direkta databasfrågor från andra tjänster.
- **API Gateway:** Alla externa klientförfrågningar dirigeras genom en API Gateway som hanterar autentisering, routing och hastighetsbegränsning.
- **Provider Abstraction:** Externa tjänster (AI-modeller, betalningsleverantörer, översättningsmotorer) är integrerade via abstraktionslager, vilket undviker hårdkodade beroenden och möjliggör flexibelt leverantörsbyte.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Säkerhet och tillförlitlighet
- **Zero-Trust Model:** Intern nätverkstrafik är inte automatiskt betrodd; känslig tjänst-till-tjänst-kommunikation kräver autentisering.
- **Idempotens och utkorgsmönster:** Kritiska operationer (som donationer eller meddelanden) är utformade för att vara idempotenta för att förhindra dubbelbearbetning, genom att använda utkorgsmönstret för att säkerställa att händelser aldrig går förlorade även under databastransaktioner.

## MVP-domänmodell (WP 1.12)

Nexus Gaja använder en strikt domändriven MVP-arkitektur (ADR-025), designad som en modulär monolit med tydliga domängränser. Denna struktur förhindrar för tidig mikrotjänstkomplexitet samtidigt som den behåller flexibiliteten att dela upp specifika domäner senare.

### Core Domain Entities
The architecture explicitly separates distinct concepts to ensure data integrity and avoid structural pitfalls like "Username = Human":
- **Identity & Accounts:** `Person` ≠ `User Account` ≠ `Identity Verification`. A verified person participates via an account, but the entities remain separate.
- **Communication:** `Message` ≠ `Translation`. The original message remains immutable; translations are linked entities.
- **Moderation:** `Report` ≠ `Moderation Decision`. A report is merely a claim; a moderation case conducts the investigation.
- **Finances:** `Donation` ≠ `Fund Balance`. Payments are booked via an immutable ledger to a fund, ensuring financial transparency.

### Sammankopplade domäner
Systemet är uppdelat i tydliga logiska domäner (Bounded Contexts): Identitet, Konto, Organisation, Kommunikation, Gemenskap, Språk, Moderering, Notifiering, Ekonomi och Styrning. Dessa domäner kartlägger hela resan från verkliga enheter (användare, skolor, icke-statliga organisationer) till deras digitala interaktioner och relaterade styrning.

## Projektstatus
Projektet befinner sig för närvarande i den aktiva arkitektur- och planeringsfasen.
Pågående arkitekturbeslut dokumenteras i mappen `/docs`.