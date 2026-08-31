# Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** je inteligentní, kontextově citlivá komunikační síť navržená tak, aby způsobila revoluci v globální komunikaci.

## Účel a vize
V globalizovaném světě je jazyk často největší bariérou. Hlavním cílem Nexus Gaja je umožnit bezproblémovou, bezbariérovou a kontextově přesnou komunikaci mezi lidmi – bez ohledu na to, zda mluví společným jazykem.

Nejde jen o strnulé překládání slov, ale o **přenášení významu**. Nexus Gaja spojuje lidi na hlubší úrovni pochopením kulturních, regionálních a kontextových nuancí, a umožňuje tak skutečné, autentické konverzace.

## Možnosti a funkce
- **Multimediální komunikace**: Systém zpracovává nejen text, ale také obraz, zvuk a video. To umožňuje plně pohlcující konverzace (např. videohovory nebo hlasové zprávy) v reálném čase přes jazykové bariéry.
- **Kontextová citlivost**: Rozpoznání ironie, idiomů, žargonu a regionálních dialektů, které jsou běžnými překladateli často nepochopeny.
- **Síť napříč platformami**: Slouží jako základ pro soukromé chaty, vlákna na fóru (příspěvky s komentáři) a interakce s globální komunitou.

---

## Technická architektura (základní koncept)

Technické jádro Nexus Gaja je na zakázku vytvořený komunikační model, který je striktně rozdělen do tří vrstev:

1. **Originál**: Komunikační objekt (zpráva) vytvořený odesílatelem zůstává vždy neměnný.
2. **Sémantická interpretace**: Systém analyzuje nejen slova, ale i skutečný význam.
3. **Reprezentace cílového jazyka**: AI pouze vytváří dočasnou nebo uloženou reprezentaci originálu pro příslušného příjemce na základě preferovaného jazyka. Překlady nikdy nepřepisují původní zprávu.

### Kontextová závislost
Překlady v Nexus Gaja nikdy nezobrazují zprávy izolovaně. Motor bere v úvahu celou hierarchii:
`Zpráva` → `Předchozí zprávy` → `Kontext vlákna` → `Kontext komunity` → `Jazyk / oblast` → `Předvolby uživatele`

### Efektivita díky překladu na vyžádání
Překlad probíhá efektivně pouze **na vyžádání** (On-Demand). Když uživatel požaduje obsah, je přeložen do jeho přednastaveného jazyka. Jakmile je vygenerován překlad pro konkrétní jazyk, je trvale uložen (cachován), aby se výrazně urychlily budoucí požadavky.

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

### 4. Proč je kontextový modul zásadní
Čisté vyhledávání klíčových slov by nestačilo. „Mohl bych ho zabít smíchem“ sémanticky obsahuje násilí, ale je to slovní spojení. "Zítra ve 20:00 ho zastřelím před jeho domem" je úplně jiná situace. Umělá inteligence musí rozumět tomu, co prohlášení znamená v jeho konkrétním kontextu.

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

### 6. Original Language + Translation
Original and translation are analyzed separately. Only then does the "Combined Moderation Assessment" take place. This allows Nexus Gaja to determine whether the translation itself may have escalated or altered the facts.

### 7. Skóre důvěry
Každé hodnocení AI obdrží skóre spolehlivosti (např. pravděpodobnost ohrožení: 0,96). Nicméně: **Skóre důvěry ≠ Pravda.** Skóre 96 % pouze znamená, že model si je velmi jistý svou klasifikací, nikoli nutně, že je vinen uživatel.

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

### 14. Obsah generovaný umělou inteligencí
Rozlišujeme mezi: vytvořené lidmi, asistované AI, AI generované a AI manipulované. To se stane součástí metadat obsahu.

### 15. Označování obsahu AI a vrstva původu AI
Podle pravidel transparentnosti zákona EU o umělé inteligenci (s účinností od srpna 2026) musí být obsah generovaný umělou inteligencí identifikovatelný. Poskytujeme vrstvu AI Provenance Layer, která ukládá metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
Architektura si klade za cíl detekovat syntetické obrazy, klonované hlasy a deepfakes. Detekce však není automaticky důkazem.

### 17. Žádný automatický „stroj na pravdu“ (umírnění ≠ prověřování faktů)
Jeden systém kontroluje: "Porušuje obsah pravidla?" (Content Moderation), další poskytuje: "Jaké informace a zdroje jsou k dispozici?" (Informační asistence). Názory nejsou jednoduše vymazány, protože jsou „špatné“.

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Jazyková rovnost a zkreslení překladu
Kvalita moderování musí být srovnatelná ve všech podporovaných jazycích (Multilingual Moderation Benchmark). Pokud se výsledky moderování liší mezi originálem a překladem (konflikt překladu), je třeba to konkrétně zkontrolovat.

### 25. Návrh architektury a nástroj politiky
Pravidla (Policy Engine) nejsou pevně zakódována do modelů AI. AI poskytuje zjištění; Policy Engine rozhoduje na základě aktuálních pravidel. To umožňuje **změny modelu bez změn pravidel**.

### 26. Člověk zůstává konečnou autoritou
- **NG-AI-MOD-001**: AI pomáhá při detekci a klasifikaci, ale nenahrazuje kontrolu člověkem při závažných rozhodnutích.
- **NG-AI-MOD-002**: Automatická rozhodnutí o moderování musí být sledovatelná, logovatelná a ověřitelná.

**Shrnutí**: Stavíme čtyřstupňový systém: detekce umělé inteligence, analýza kontextu a rizik, nástroj politiky a řízení lidí. To umožňuje silnou automatizaci bez vytváření nebezpečné architektury „AI jako soudce“.

## Stav projektu
Projekt je v současné době ve fázi aktivní architektury a plánování.
Probíhající architektonická rozhodnutí jsou dokumentována ve složce `/docs`.