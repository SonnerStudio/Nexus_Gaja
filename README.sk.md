# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** is an intelligent, context-sensitive communication network designed to revolutionize global communication.

## Purpose and Vision
In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

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

### Závislosť od kontextu
Preklady v Nexus Gaja nikdy nezobrazujú správy izolovane. Motor berie do úvahy celú hierarchiu:
`Správa` → `Predchádzajúce správy` → `Kontext vlákna` → `Kontext komunity` → `Jazyk/región` → `Predvoľby používateľa`

### Efektívnosť prostredníctvom prekladu na požiadanie
Preklad prebieha efektívne len **na požiadanie** (On-Demand). Keď používateľ požaduje obsah, preloží sa do jeho predvoleného jazyka. Po vygenerovaní prekladu pre konkrétny jazyk sa tento natrvalo uloží (do vyrovnávacej pamäte), aby sa výrazne urýchlili budúce požiadavky.

## Moderovanie za pomoci AI (WP 1.8.4)

S moderovaním za pomoci AI robíme významný krok od nápadu produktu k technickej architektúre, pričom zohľadňujeme súčasné nariadenia EÚ (požiadavky na transparentnosť zákona EÚ o AI podľa čl. 50; zákona o digitálnych službách so zrozumiteľným odôvodnením a možnosťami odvolania).

### 1. Základný princíp
Najdôležitejšia veta pre architektúru je: **Moderačná umelá inteligencia je systém kontroly, nie autonómny riadiaci systém.**
Je navrhnutý tak, aby pomáhal ľuďom s mierou, nie aby sám určoval, ktoré názory môžu na Nexus Gaja existovať.
Rozlišujeme tri úrovne:
- **Detekcia:** "Mohlo by tu dôjsť k porušeniu pravidiel."
- **Vyhodnotenie:** "Pravdepodobnosť porušenia pravidla je napríklad 94 %."
- **Rozhodnutie:** "Aká akcia sa vlastne podnikne?"
Tretiu úroveň musí v závažných prípadoch ovládať človek.

### 2. Umelá inteligencia moderovania ako subsystém
Namiesto jednej AI je vytvorený robustný subsystém:
```text
                 NEXUS GAJA AI MODERÁCIA
                          │
       ┌──────────────────┼─────────└─—└─  
       │ │ │
  Jazyk AI Bezpečnosť AI Podvod AI
       │ │ │
       ├──────────────┬───┴─────────└──└─‬
       │ │ │
 Identita správania pri preklade
 Analýza Analýza signálov
       │ │ │
       └──────────────┼────────────────└─—
                      ▼
               Hodnotenie rizika
                      │
                      ▼
               Human Review
```

### 3. Najdôležitejšie moduly AI
Nexus Gaja využíva deväť špecializovaných oblastí analýzy:
- **M1 – Jazykové porozumenie**: Zisťuje jazyk, dialekt, slang, indikátory irónie, problémy s prekladom.
- **M2 – Toxicity / Abuse Detection**: Detekuje urážky, osobné útoky, obťažovanie.
- **M3 – Detekcia hrozieb**: Detekuje potenciálne hrozby, vydieranie, násilie.
- **M4 – Detekcia nenávisti/dehumanizácie**: Zisťuje cielené útoky na ľudí na základe konkrétnej príslušnosti.
- **M5 – Detekcia spamu / manipulácie**: Detekuje spam, správanie robotov, koordinovanú manipuláciu.
- **M6 – Fraud Detection**: Detekuje podozrivé pokusy o podvod, phishing, sociálne inžinierstvo.
- **M7 – Integrita identity**: Kontroluje signály týkajúce sa prevzatia účtu, viacerých účtov, vyhýbania sa zákazu.
- **M8 – Bezpečnosť médií**: Analyzuje obrázky, zvuk, video, dokumenty.
- **M9 – Context Engine**: Najdôležitejší modul. Spája jednotlivé zistenia.

### 4. Prečo je kontextový nástroj rozhodujúci
Čisté vyhľadávanie kľúčových slov by nestačilo. „Mohol by som ho zabiť od smiechu“ sémanticky obsahuje násilie, ale je to len slovné spojenie. "Zajtra o 20:00 ho zastrelím pred jeho domom" je úplne iná situácia. Umelá inteligencia musí pochopiť, čo daný výrok znamená v jeho konkrétnom kontexte.

### 5. Viacjazyčné moderovanie
Moderovanie nemôže jednoducho porovnávať slová. Musí analyzovať sémantickú úroveň (napr. nemecké idiómy vs. japonské idiómy vs. regionálne výrazy).

### 6. Pôvodný jazyk + preklad
Originál a preklad sa analyzujú oddelene. Až potom sa uskutoční „Combined Moderation Assessment“. To umožňuje Nexus Gaja určiť, či samotný preklad mohol eskalovať alebo zmeniť fakty.

### 7. Skóre dôvery
Každé hodnotenie AI dostane skóre spoľahlivosti (napr. pravdepodobnosť hrozby: 0,96). Avšak: **Skóre spoľahlivosti ≠ Pravda.** Skóre 96 % znamená iba to, že model si je veľmi istý svojou klasifikáciou, nie nevyhnutne, že je vinný používateľ.

### 8. Neistota sa sama stáva signálom
Ak je AI neistá (napr. hrozba: 0,62, satira: 0,54), nesmie jednoducho presadzovať prísne pravidlá. Namiesto toho je neistota zabudovaná priamo do architektúry: **Vyžaduje sa kontrola človekom**.

### 9. Štyri rozhodovacie zóny
- 🢢 **ZELENÁ**: S vysokou pravdepodobnosťou vyhovuje. → žiadna akcia.
- 🡥 **ŽLTÁ**: Možné porušenie. → monitorovať / v prípade potreby poskytnúť varovanie.
- **ORANŽOVÁ**: Pravdepodobné porušenie. → hodnotenie moderovania.
- 🔴 **ČERVENÁ**: Možné závažné porušenie. → okamžité ochranné opatrenie + kontrola človekom.

### 10. Žiadny „trest AI“
**Umelá inteligencia neukladá žiadne konečné sankcie.** V prípade vážnych bezpečnostných problémov môže spustiť technické okamžité opatrenia (napr. dočasné zadržanie správy), ale konečné rozhodnutie zostáva overiteľné.

### 11. Ochranné opatrenia môžu nastať automaticky
V prípade konkrétnej hrozby (Zistená hrozba → Vysoká spoľahlivosť → Dočasné obmedzenie → Kontrola človekom → Rozhodnutie) chránime ohrozeného používateľa bez toho, aby sme z AI urobili sudcu.

### 12. Umelá inteligencia musí byť schopná odôvodniť svoje rozhodnutia
DSA vyžaduje jasné a konkrétne dôvody. Umelá inteligencia poskytuje štruktúrované zdôvodnenie: Pravidlo (NG-CONDUCT-004), Zistené (Potenciálna konkrétna hrozba), Dôvera (0,94), Relevantný kontext (Predchádzajúce 4 správy), Odporúčaná akcia (Hodnotenie človekom).

### 13. Umelá inteligencia nesmie tajne meniť obsah
**Moderačná umelá inteligencia nikdy nesmie bez povšimnutia zmeniť pôvodný obsah.** Počas automatickej opravy, prekladu alebo sumarizácie sa originál vždy zachová.

### 14. Obsah generovaný AI
Rozlišujeme medzi: vytvorené ľuďmi, s pomocou AI, generované AI a manipulované AI. Toto sa stane súčasťou metadát obsahu.

### 15. Označovanie obsahu AI a vrstva pôvodu AI
Podľa pravidiel transparentnosti zákona EÚ o umelej inteligencii (s účinnosťou od augusta 2026) musí byť obsah generovaný umelou inteligenciou identifikovateľný. Poskytujeme vrstvu AI Provenance Layer, ktorá ukladá metadáta (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detekcia
Architektúra sa zameriava na detekciu syntetických obrázkov, klonovaných hlasov a deepfakes. Detekcia však nie je automaticky dôkazom.

### 17. Žiadny automatický „stroj na pravdu“ (umiernenosť ≠ overovanie faktov)
Jeden systém skontroluje: "Porušuje obsah pravidlá?" (Moderovanie obsahu), ďalšia poskytuje: "Aké informácie a zdroje sú dostupné?" (Informačná pomoc). Názory nie sú jednoducho vymazané, pretože sú „nesprávne“.

### 18. Ochrana proti kultúrnej dezinterpretácii
AI vyžaduje **modely kultúrneho kontextu**, aby zabránila tomu, aby sa komunikačné normy jednej krajiny považovali za globálny štandard.

### 19. Irónia, satira a humor
Umelá inteligencia používa kontext, emotikony, históriu konverzácií a známe iróniové štruktúry, ale musí počítať s neistotou, keď sú významy nejednoznačné.

### 20. Žiadny trest na základe jediného skóre AI
Žiadna závažná moderačná intervencia nesmie byť založená len na jednom výsledku automatizovanej klasifikácie (text + kontext + správanie + jazyk + médiá + nástroj pravidiel = hodnotenie rizika).

### 21. Signály správania používateľov a žiadny systém sociálneho kreditu
Týka sa to signálov technického zneužitia (napr. hromadného odosielania spamu), nie všeobecného systému sociálneho hodnotenia. Nexus Gaja neudržiava systém sociálneho kreditu – moderovanie slúži bezpečnosti, nie posudzovaniu hodnoty človeka.

### 22. Umelá inteligencia moderovania musí byť kontrolovateľná
Všetky relevantné automatizované rozhodnutia sa zaznamenávajú (ID udalosti, ID pravidiel, dôvera, kontrola človekom atď.), aby sa zabezpečila sledovateľnosť.

### 23. Falošné pozitíva, falošné negatíva a metriky kvality
Typy chýb sú monitorované. Na informačnom paneli sa meria presnosť, odvolanie a najmä **miera zvrátenia odvolaní** (počet úspešných odvolaní).

### 24. Jazyková rovnosť a zaujatosť prekladu
Kvalita moderovania musí byť porovnateľná vo všetkých podporovaných jazykoch (Multilingual Moderation Benchmark). Ak sa výsledky moderovania líšia medzi originálom a prekladom (konflikt prekladov), musí sa to osobitne preskúmať.

### 25. Návrh architektúry a nástroj politiky
Pravidlá (Policy Engine) nie sú pevne zakódované do modelov AI. AI poskytuje zistenia; Policy Engine rozhoduje na základe aktuálnych pravidiel. To umožňuje **zmeny modelu bez zmien pravidiel**.

### 26. Človek zostáva konečnou autoritou
- **NG-AI-MOD-001**: AI pomáha pri detekcii a klasifikácii, ale nenahrádza kontrolu človekom pri závažných rozhodnutiach.
- **NG-AI-MOD-002**: Automatické rozhodnutia o moderovaní musia byť sledovateľné, zapisovateľné a overiteľné.

**Zhrnutie**: Vytvárame štvorstupňový systém: detekcia AI, analýza kontextu a rizík, nástroj politiky a riadenie ľudí. To umožňuje silnú automatizáciu bez vytvárania nebezpečnej architektúry „AI ako sudca“.

## Princípy financovania a model výnosov (WP 1.10.1)

Pre Nexus Gaja platí veľmi dôležitý ekonomický princíp: **Žiadna tradičná reklama v rámci platformy.**
To zásadne odlišuje Nexus Gaja od mnohých dnešných sociálnych sietí. To však neznamená, že Nexus Gaja nemôže mať komerčný charakter. Naopak, platforma musí byť ekonomicky životaschopná, aby jej sociálny účel vydržal. Ekonomická činnosť je prostriedkom na dosiahnutie cieľa, nie primárnym účelom platformy.

### 1. Princíp NG-FIN-001
Nexus Gaja financuje svoje operácie prostredníctvom transparentných tokov príjmov oddelených od záujmov používateľov, a nie prostredníctvom speňažovania pozornosti alebo osobných údajov používateľov.

### 2. Žiadna tradičná reklama
Konkrétne sú zakázané:
- Bannerové reklamy
- Vyskakovacie reklamy
- Automaticky sa prehrávajúce videoreklamy
- Sponzorované príspevky v štandardnom informačnom kanáli
- Personalizované reklamné profily
- Predaj užívateľských profilov alebo osobných údajov
- Reklama odvodená zo súkromných rozhovorov.

Nexus Gaja zostáva skôr **komunikačným priestorom než reklamným priestorom**.

### 3. Financovanie bez reklamy (6 pilierov)
Financovanie je postavené na šiestich pilieroch:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PRÉMIOVÉ DARY ORGANIZÁCIÍ
       │ │ │
       ├─────────────┼──────────────.
       ▼ ▼ ▼
    GRANTUJE SLUŽBY PARTNERSTVA
```

#### Pilier 1 – Bezplatné základné členstvo
**Nexus Gaja Free** umožňuje základné medzinárodné porozumenie pre každého (profil, medzinárodná komunikácia, príspevky, komunity, čety, základný preklad) zadarmo.

#### Pilier 2 – Prémiové ponuky
Dobrovoľné platené ponuky (**Nexus Gaja Plus**) poskytujúce väčšie limity úložiska, vyššiu kvalitu médií, rozšírené kvóty AI a organizačné funkcie.
**Dôležité (Freemium namiesto Dark Freemium):** Základná komunikácia nesmie byť nikdy umelo degradovaná.

#### Pilier 3 – Organizácie
Špeciálne účty pre školy, univerzity, mimovládne organizácie, firmy a samosprávy (**Nexus Gaja Organization**). Školy môžu byť podporované prostredníctvom inštitucionálnych sadzieb ako multiplikátorov medzinárodného porozumenia.

#### Pilier 4 – Dary
**Nexus Gaja Funding Pool** prijíma všeobecné a účelové dary (napr. „na medzinárodnú komunikáciu s mládežou“). **Fond Allocation Ledger** zabezpečuje transparentné prideľovanie finančných prostriedkov.
**Účelový fond a tombola:** Časť darov slúži ako zdroj na bezplatné/zľavnené použitie. Mechanizmus lotérie/tomboly môže tieto prostriedky prideliť transparentne a kontrolovateľne.

#### Pilier 5 – Inštitucionálne financovanie
Nadácie, programy financovania kultúry alebo štátne programy.
**NG-FIN-002:** Finančná podpora nezahŕňa redakčnú ani technickú kontrolu (nezávislosť).

#### Pillar 6 – Commercial Services
B2B services like **Translation-as-a-Service** (API), organizational communication, or international conference rooms, without burdening the standard user feed.

### 4. No Data Monetization & Surveillance Economy
**NG-FIN-003:** Personal user data is not a commodity. No sale of lists, profiles, or histories. Nexus Gaja does not profit from psychological surveillance (Surveillance Economy).

### 5. Finančná transparentnosť a kniha fondov
**Finančná transparentnosť Nexus Gaja:** Zverejňovanie súhrnných finančných štruktúr. Účelovo viazané dary sú technicky vyúčtované (ID fondu → Účel → Zostatok → Pridelenie). Žiadne krížové dotovanie sociálnych účelov do firemného marketingu.

### 6. Model financovania založený na solidarite
Ceny sú založené na nákladovej orientácii, spravodlivosti a solidarite.
**Solidarity Premium:** Dobrovoľná možnosť pre používateľov Premium na financovanie časti prístupu iného používateľa. Nútená solidarita alebo spoločnosť prémiovej triedy (menej rešpektu/umiernenosti pre slobodných používateľov) sú prísne zakázané.

### 7. Ekonomické KPI namiesto Ekonomiky zapojenia
Žiadna závislosť na udržiavaní používateľov "čo najdlhšie online" (žiadne ragebait, nekonečné feedy).
Namiesto toho používame metriky ako:
- **Global Communication Index (GCI):** Úspešné komunikačné vzťahy medzi ľuďmi z rôznych jazykových/kultúrnych oblastí.
- **Platform Sustainability Ratio (PSR):** Opakujúce sa príjmy / opakujúce sa prevádzkové náklady (Cieľ ≥ 1).

### 8. Čo výslovne nechceme (negatívny zoznam)
Nexus Gaja **nefinancuje**:
❌ Predaj osobných údajov
❌ Prispôsobená tradičná reklama
❌ Monitorovanie správania používateľov na reklamné účely
❌ Predaj údajov o súkromnej komunikácii
❌ Skryté využitie dát AI
❌ Manipulatívne prémiové paywally
❌ Obmedzenie umelého dosahu na speňaženie
❌ Platený politický vplyv
❌ Nákup privilegovaných rozhodnutí o moderovaní.

### 9. Predbežná finančná architektúra
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼───────────└───── 
             │ │ │
             ▼ ▼ ▼
          POUŽÍVATEĽSKÉ ORGANIZÁCIE PODNIK
             │ │ │
             └────────────────┼──────────────└─ —
                              │
                       SLUŽBY PLATFORMY
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS API
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               VŠEOBECNÝ FOND OBMEDZENÉ FONDY
                                        │
                                        ▼
                                  SOCIÁLNY ÚČEL
```

### Summary of Financing Principles (NG-FIN)
- **NG-FIN-001:** No financing through traditional advertising.
- **NG-FIN-002:** No editorial/technical control through financial support.
- **NG-FIN-003:** Personal data is not a commodity.
- **NG-FIN-004:** Basic communication remains accessible without payment.
- **NG-FIN-005:** Premium offerings must not degrade free users.
- **NG-FIN-006:** Earmarked funds are managed according to their purpose.
- **NG-FIN-007:** Transparent management of donations and grants.
- **NG-FIN-008:** Commercial B2B services do not compromise independence.
- **NG-FIN-009:** Focus on sustainability rather than maximum monetization.
- **NG-FIN-010:** The structure permanently secures the social purpose.

## API, Interfaces, and Communication Architecture (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### Core Principles
- **No Direct Database Access:** Components communicate exclusively via defined interfaces (APIs or Events), never through direct database queries of other services.
- **API Gateway:** All external client requests route through an API Gateway handling authentication, routing, and rate limiting.
- **Provider Abstraction:** External services (AI models, payment providers, translation engines) are integrated via abstraction layers, avoiding hardcoded dependencies and enabling flexible provider swapping.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Security and Reliability
- **Zero-Trust Model:** Internal network traffic is not automatically trusted; sensitive service-to-service communication requires authentication.
- **Idempotency & Outbox Pattern:** Critical operations (like donations or messaging) are designed to be idempotent to prevent duplicate processing, utilizing the Outbox pattern to ensure events are never lost even during database transactions.

## MVP Domain Model (WP 1.12)

Nexus Gaja employs a strictly Domain-Driven MVP Architecture (ADR-025), designed as a modular monolith with clear domain boundaries. This structure prevents premature microservice complexity while retaining the flexibility to split out specific domains later.

### Core Domain Entities
The architecture explicitly separates distinct concepts to ensure data integrity and avoid structural pitfalls like "Username = Human":
- **Identity & Accounts:** `Person` ≠ `User Account` ≠ `Identity Verification`. A verified person participates via an account, but the entities remain separate.
- **Communication:** `Message` ≠ `Translation`. The original message remains immutable; translations are linked entities.
- **Moderation:** `Report` ≠ `Moderation Decision`. A report is merely a claim; a moderation case conducts the investigation.
- **Finances:** `Donation` ≠ `Fund Balance`. Payments are booked via an immutable ledger to a fund, ensuring financial transparency.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Stav projektu
Projekt je momentálne vo fáze aktívnej architektúry a plánovania.
Prebiehajúce architektonické rozhodnutia sú zdokumentované v priečinku `/docs`.