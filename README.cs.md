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

## Technická architektura (základní koncept)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Originál**: Komunikační objekt (zpráva) vytvořený odesílatelem zůstává vždy neměnný.
2. **Sémantická interpretace**: Systém analyzuje nejen slova, ale i skutečný význam.
3. **Reprezentace cílového jazyka**: Umělá inteligence pouze vytváří dočasnou nebo uloženou reprezentaci originálu pro příslušného příjemce na základě preferovaného jazyka. Překlady nikdy nepřepisují původní zprávu.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## AI-Assisted Moderation (WP 1.8.4)

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. Basic Principle
The most important sentence for the architecture is: **The moderation AI is a review system, not an autonomous ruling system.**
It is designed to assist humans in moderation, not to determine itself which opinions are allowed to exist on Nexus Gaja.
We differentiate between three levels:
- **Detection:** "There could be a rule violation here."
- **Evaluation:** "The probability of a rule violation is, for example, 94%."
- **Decision:** "What action is actually taken?"
The third level must be controlled by a human in severe cases.

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

### 4. Why the Context Engine is Crucial
A pure keyword search would be insufficient. "I could kill him from laughing" semantically contains violence but is a figure of speech. "Tomorrow at 8 PM I will shoot him in front of his house" is a completely different situation. The AI must understand what the statement means in its specific context.

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

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

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. Umělá inteligence musí být schopna zdůvodnit svá rozhodnutí
DSA vyžaduje jasné a konkrétní důvody. Umělá inteligence poskytuje strukturované uvažování: Pravidlo (NG-CONDUCT-004), Zjištěno (Potenciální konkrétní hrozba), Důvěra (0,94), Relevantní kontext (Předchozí 4 zprávy), Doporučená akce (Hodnocení člověkem).

### 13. Umělá inteligence nesmí tajně měnit obsah
**Moderační umělá inteligence nikdy nesmí bez povšimnutí změnit původní obsah.** Během automatické opravy, překladu nebo sumarizace je originál vždy zachován.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Označování obsahu AI a vrstva původu AI
Podle pravidel transparentnosti zákona EU o umělé inteligenci (s účinností od srpna 2026) musí být obsah generovaný umělou inteligencí identifikovatelný. Poskytujeme vrstvu AI Provenance Layer, která ukládá metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
Architektura si klade za cíl detekovat syntetické obrazy, klonované hlasy a deepfakes. Detekce však není automaticky důkazem.

### 17. Žádný automatický „stroj na pravdu“ (umírnění ≠ prověřování faktů)
Jeden systém kontroluje: "Porušuje obsah pravidla?" (Content Moderation), další poskytuje: "Jaké informace a zdroje jsou k dispozici?" (Informační asistence). Názory nejsou jednoduše vymazány, protože jsou „špatné“.

### 18. Ochrana proti kulturní dezinterpretaci
AI vyžaduje **modely kulturního kontextu**, aby se zabránilo tomu, že komunikační normy jedné země budou považovány za globální standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. Žádný trest na základě jediného skóre AI
Žádný závažný zásah moderování nesmí být založen pouze na jediném výsledku automatické klasifikace (Text + Kontext + Chování + Jazyk + Média + Modul pravidel = Hodnocení rizik).

### 21. Signály chování uživatelů a žádný systém sociálního kreditu
Týká se to signálů technického zneužití (např. hromadného rozesílání spamu), nikoli obecného systému sociálního hodnocení. Nexus Gaja neudržuje systém sociálního kreditu – umírněnost slouží bezpečnosti, nikoli hodnocení hodnoty člověka.

### 22. Umělá inteligence moderování musí být auditovatelná
Všechna relevantní automatizovaná rozhodnutí jsou protokolována (ID události, ID pravidla, důvěra, kontrola člověkem atd.), aby byla zajištěna sledovatelnost.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Financing Principles and Revenue Model (WP 1.10.1)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Princip NG-FIN-001
Nexus Gaja financuje své operace prostřednictvím transparentních toků příjmů oddělených od zájmů uživatelů, nikoli prostřednictvím zpeněžení pozornosti nebo osobních údajů svých uživatelů.

### 2. Žádná tradiční reklama
Konkrétně zakázané jsou:
- Bannerové reklamy
- Pop-up reklamy
- Automatické přehrávání videoreklam
- Sponzorované příspěvky ve standardním zdroji
- Personalizované reklamní profily
- Prodej uživatelských profilů nebo osobních údajů
- Reklama odvozená ze soukromých konverzací.

Nexus Gaja zůstává **komunikačním prostorem spíše než reklamním prostorem**.

### 3. Financování bez reklamy (6 pilířů)
Financování je postaveno na šesti pilířích:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   PRÉMIOVÉ DARY ORGANIZACE
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    UDĚLUJE SLUŽBY PARTNERSTVÍ
```

#### Pilíř 1 – Základní členství zdarma
**Nexus Gaja Free** umožňuje základní mezinárodní porozumění pro každého (profil, mezinárodní komunikace, příspěvky, komunity, chaty, základní překlady) zdarma.

#### Pilíř 2 – Prémiové nabídky
Dobrovolné placené nabídky (**Nexus Gaja Plus**) poskytující větší limity úložiště, vyšší kvalitu médií, rozšířené kvóty AI a organizační funkce.
**Důležité (Freemium místo Dark Freemium):** Základní komunikace nesmí být nikdy uměle degradována.

#### Pilíř 3 – Organizace
Speciální účty pro školy, univerzity, nevládní organizace, firmy a obce (**Nexus Gaja Organization**). Školy mohou být podporovány prostřednictvím institucionálních sazeb jako multiplikátorů mezinárodního porozumění.

#### Pilíř 4 – Dary
Fond **Nexus Gaja Funding Pool** přijímá obecné a účelové dary (např. „pro mezinárodní komunikaci s mládeží“). **Fond Allocation Ledger** zajišťuje transparentní alokaci finančních prostředků.
**Účelový fond a tombola:** Část darů slouží jako zdroj pro bezplatné/zlevněné použití. Mechanismus loterie/tomboly může tyto prostředky přidělit transparentně a kontrolovatelně.

#### Pilíř 5 – institucionální financování
nadace, programy financování kultury nebo státní programy.
**NG-FIN-002:** Finanční podpora nezahrnuje redakční ani technickou kontrolu (nezávislost).

#### Pillar 6 – Commercial Services
B2B services like **Translation-as-a-Service** (API), organizational communication, or international conference rooms, without burdening the standard user feed.

### 4. No Data Monetization & Surveillance Economy
**NG-FIN-003:** Personal user data is not a commodity. No sale of lists, profiles, or histories. Nexus Gaja does not profit from psychological surveillance (Surveillance Economy).

### 5. Finanční transparentnost a účetní kniha fondů
**Finanční transparentnost Nexus Gaja:** Zveřejnění agregovaných finančních struktur. Účelově vázané dary jsou technicky vyúčtovány (ID fondu → Účel → Zůstatek → Alokace). Žádné křížové dotování sociálních účelů do firemního marketingu.

### 6. Solidarity-Based Financing Model
Pricing is based on cost-orientation, fairness, and solidarity.
**Solidarity Premium:** A voluntary option for Premium users to finance a portion of another user's access. Forced solidarity or a premium class society (less respect/moderation for free users) is strictly prohibited.

### 7. Economic KPIs Instead of Engagement Economy
No dependence on keeping users "online as long as possible" (no ragebait, infinite feeds).
Instead, we use metrics like:
- **Global Communication Index (GCI):** Successful communication relationships between people from different linguistic/cultural regions.
- **Platform Sustainability Ratio (PSR):** Recurring revenue / recurring operating costs (Target ≥ 1).

### 8. Co výslovně nechceme (negativní seznam)
Nexus Gaja **není** financováno:
❌ Prodej osobních údajů
❌ Personalizovaná tradiční reklama
❌ Sledování chování uživatelů pro reklamní účely
❌ Prodej dat soukromé komunikace
❌ Skryté využití dat AI
❌ Manipulativní prémiové paywally
❌ Omezení umělého dosahu pro zpeněžení
❌ Placený politický vliv
❌ Nákup privilegovaných moderačních rozhodnutí.

### 9. Předběžná finanční architektura
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼───────────└─ —
             │ │ │
             ▼ ▼ ▼
          UŽIVATELSKÉ ORGANIZACE PODNIK
             │ │ │
             └────────────────┼──────────────└─—
                              │
                       SLUŽBY PLATFORMY
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               OBECNÝ FOND OMEZENÉ FONDY
                                        │
                                        ▼
                                  SOCIÁLNÍ ÚČEL
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

### Základní principy
- **Žádný přímý přístup k databázi:** Komponenty komunikují výhradně přes definovaná rozhraní (API nebo události), nikdy prostřednictvím přímých databázových dotazů jiných služeb.
- **Brána API:** Všechny požadavky externích klientů směřují přes bránu API, která zajišťuje ověřování, směrování a omezení rychlosti.
- **Abstrakce poskytovatelů:** Externí služby (modely umělé inteligence, poskytovatelé plateb, překladatelské nástroje) jsou integrovány prostřednictvím abstrakčních vrstev, čímž se vyhnete napevno zakódovaným závislostem a umožňují flexibilní výměnu poskytovatelů.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Bezpečnost a spolehlivost
- **Model nulové důvěry:** Interní síťový provoz není automaticky důvěryhodný; citlivá komunikace mezi službami vyžaduje ověření.
- **Idempotency & Outbox Pattern:** Kritické operace (jako dary nebo zasílání zpráv) jsou navrženy tak, aby byly idempotentní, aby se zabránilo duplicitnímu zpracování, s využitím vzoru Outbox, aby se zajistilo, že se události nikdy neztratí ani během databázových transakcí.

## Model domény MVP (WP 1.12)

Nexus Gaja employs a strictly Domain-Driven MVP Architecture (ADR-025), designed as a modular monolith with clear domain boundaries. This structure prevents premature microservice complexity while retaining the flexibility to split out specific domains later.

### Entity hlavní domény
Architektura explicitně odděluje různé koncepty, aby byla zajištěna integrita dat a zabránilo se strukturálním nástrahám, jako je „Uživatelské jméno = Člověk“:
- **Identita a účty:** `Osoba` ≠ `Uživatelský účet` ≠ `Ověření identity`. Ověřená osoba se účastní prostřednictvím účtu, ale subjekty zůstávají oddělené.
- **Komunikace:** `Zpráva` ≠ `Překlad`. Původní zpráva zůstává neměnná; překlady jsou propojené entity.
- **Moderování:** `Zpráva` ≠ `Rozhodnutí o moderování`. Zpráva je pouze tvrzení; moderační případ vede vyšetřování.
- **Finance:** `Darování` ≠ `Zůstatek fondu`. Platby jsou zaúčtovány prostřednictvím neměnné knihy do fondu, což zajišťuje finanční transparentnost.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Stav projektu
Projekt je v současné době ve fázi aktivní architektury a plánování.
Probíhající architektonická rozhodnutí jsou dokumentována ve složce `/docs`.