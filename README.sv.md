# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** is an intelligent, context-sensitive communication network designed to revolutionize global communication.

## Purpose and Vision
In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

Det handlar inte bara om att stelbent översätta ord, utan om att **överföra betydelse**. Nexus Gaja förbinder människor på en djupare nivå genom att förstå kulturella, regionala och kontextuella nyanser, vilket möjliggör genuina, autentiska konversationer.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

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

### 12. AI:n måste kunna motivera sina beslut
DSA kräver tydliga och specifika skäl. AI:n ger strukturerade resonemang: Regel (NG-CONDUCT-004), Upptäckt (potentiellt konkret hot), Förtroende (0,94), Relevant sammanhang (Tidigare 4 meddelanden), Rekommenderad åtgärd (Humanöversyn).

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

## Projektstatus
Projektet befinner sig för närvarande i den aktiva arkitektur- och planeringsfasen.
Pågående arkitekturbeslut dokumenteras i mappen `/docs`.