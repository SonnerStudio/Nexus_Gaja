# Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** je inteligentná, kontextovo citlivá komunikačná sieť navrhnutá tak, aby spôsobila revolúciu v globálnej komunikácii.

## Účel a vízia

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

V globalizovanom svete je jazyk často najväčšou bariérou. Hlavným cieľom Nexus Gaja je umožniť bezproblémovú, bezbariérovú a kontextovo presnú komunikáciu medzi ľuďmi – bez ohľadu na to, či hovoria spoločným jazykom.

Nejde len o strnulé prekladanie slov, ale o **prenášanie významu**. Nexus Gaja spája ľudí na hlbšej úrovni pochopením kultúrnych, regionálnych a kontextových nuancií, čím umožňuje skutočné, autentické rozhovory.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technická architektúra (základný koncept)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

Technickým jadrom Nexus Gaja je na mieru vytvorený komunikačný model, ktorý je striktne rozdelený do troch vrstiev:

1. **Originál**: Komunikačný objekt (správa) vytvorený odosielateľom zostáva vždy nemenný.
2. **Sémantická interpretácia**: Systém analyzuje nielen slová, ale aj skutočný význam.
3. **Cieľová jazyková reprezentácia**: AI iba vytvorí dočasnú alebo uloženú reprezentáciu originálu pre príslušného príjemcu na základe preferovaného jazyka. Preklady nikdy neprepíšu pôvodnú správu.

### Závislosť od kontextu
Preklady v Nexus Gaja nikdy nezobrazujú správy izolovane. Motor berie do úvahy celú hierarchiu:
`Správa` → `Predchádzajúce správy` → `Kontext vlákna` → `Kontext komunity` → `Jazyk/región` → `Predvoľby používateľa`

### Efektívnosť prostredníctvom prekladu na požiadanie
Preklad prebieha efektívne len **na požiadanie** (On-Demand). Keď používateľ požaduje obsah, preloží sa do jeho predvoleného jazyka. Po vygenerovaní prekladu pre konkrétny jazyk sa tento natrvalo uloží (do vyrovnávacej pamäte), aby sa výrazne urýchlili budúce požiadavky.

## Moderovanie za pomoci AI (WP 1.8.4)

![Moderovanie AI Nexus Gaja](assets/img/nexus_moderation.jpg)

S moderovaním za pomoci AI robíme významný krok od nápadu produktu k technickej architektúre, pričom zohľadňujeme súčasné nariadenia EÚ (požiadavky na transparentnosť zákona EÚ o AI podľa čl. 50; zákona o digitálnych službách so zrozumiteľným odôvodnením a možnosťami odvolania).

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

### 4. Prečo je kontextový nástroj rozhodujúci
Čisté vyhľadávanie kľúčových slov by nestačilo. „Mohol by som ho zabiť od smiechu“ sémanticky obsahuje násilie, ale je to len slovné spojenie. "Zajtra o 20:00 ho zastrelím pred jeho domom" je úplne iná situácia. Umelá inteligencia musí pochopiť, čo daný výrok znamená v jeho konkrétnom kontexte.

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

### 6. Pôvodný jazyk + preklad
Originál a preklad sa analyzujú oddelene. Až potom sa uskutoční „Combined Moderation Assessment“. To umožňuje Nexus Gaja určiť, či samotný preklad mohol eskalovať alebo zmeniť fakty.

### 7. Confidence Score
Every AI evaluation receives a confidence score (e.g., Threat probability: 0.96). However: **Confidence Score ≠ Truth.** A score of 96% only means the model is highly certain of its classification, not necessarily that the user is guilty.

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. Four Decision Zones
- 🟢 **GREEN**: Highly likely compliant. → no action.
- 🟡 **YELLOW**: Possible violation. → monitor / provide a warning if necessary.
- 🟠 **ORANGE**: Probable violation. → moderation review.
- 🔴 **RED**: Severe possible violation. → immediate protective measure + human review.

### 10. Žiadny „trest AI“
**Umelá inteligencia neukladá žiadne konečné sankcie.** V prípade vážnych bezpečnostných problémov môže spustiť technické okamžité opatrenia (napr. dočasné zadržanie správy), ale konečné rozhodnutie zostáva overiteľné.

### 11. Ochranné opatrenia môžu nastať automaticky
V prípade konkrétnej hrozby (Zistená hrozba → Vysoká spoľahlivosť → Dočasné obmedzenie → Kontrola človekom → Rozhodnutie) chránime ohrozeného používateľa bez toho, aby sme z AI urobili sudcu.

### 12. Umelá inteligencia musí byť schopná odôvodniť svoje rozhodnutia
DSA vyžaduje jasné a konkrétne dôvody. Umelá inteligencia poskytuje štruktúrované zdôvodnenie: Pravidlo (NG-CONDUCT-004), Zistené (Potenciálna konkrétna hrozba), Dôvera (0,94), Relevantný kontext (Predchádzajúce 4 správy), Odporúčaná akcia (Hodnotenie človekom).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. Obsah generovaný AI
Rozlišujeme medzi: vytvorené ľuďmi, s pomocou AI, generované AI a manipulované AI. Toto sa stane súčasťou metadát obsahu.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
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

![Finančný model Nexus Gaja](assets/img/nexus_finance.jpg)

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

#### Pillar 2 – Premium Offerings
Voluntary paid offerings (**Nexus Gaja Plus**) providing greater storage limits, higher media quality, expanded AI quotas, and organizational features.
**Important (Freemium instead of Dark Freemium):** Basic communication must never be artificially degraded.

#### Pilier 3 – Organizácie
Špeciálne účty pre školy, univerzity, mimovládne organizácie, firmy a samosprávy (**Nexus Gaja Organization**). Školy môžu byť podporované prostredníctvom inštitucionálnych sadzieb ako multiplikátorov medzinárodného porozumenia.

#### Pillar 4 – Donations
The **Nexus Gaja Funding Pool** accepts general and earmarked donations (e.g., "for international youth communication"). A **Fund Allocation Ledger** ensures transparent allocation of funds.
**Purpose Fund & Tombola:** A portion of donations feeds a pool for free/discounted usage. A lottery/tombola mechanism can allocate these funds transparently and auditably.

#### Pilier 5 – Inštitucionálne financovanie
Nadácie, programy financovania kultúry alebo štátne programy.
**NG-FIN-002:** Finančná podpora nezahŕňa redakčnú ani technickú kontrolu (nezávislosť).

#### Pilier 6 – Obchodné služby
B2B služby ako **Translation-as-a-Service** (API), organizačná komunikácia alebo medzinárodné konferenčné miestnosti bez zaťažovania štandardného informačného kanála používateľov.

### 4. Žiadne speňaženie údajov a hospodárnosť dohľadu
**NG-FIN-003:** Osobné údaje používateľa nie sú tovar. Žiadny predaj zoznamov, profilov alebo histórie. Nexus Gaja neprofituje z psychologického dohľadu (Surveillance Economy).

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

### Súhrn princípov financovania (NG-FIN)
- **NG-FIN-001:** Žiadne financovanie prostredníctvom tradičnej reklamy.
- **NG-FIN-002:** Žiadna redakčná/technická kontrola prostredníctvom finančnej podpory.
- **NG-FIN-003:** Osobné údaje nie sú tovar.
- **NG-FIN-004:** Základná komunikácia zostáva dostupná bez platenia.
- **NG-FIN-005:** Prémiové ponuky nesmú znižovať úroveň bezplatných používateľov.
- **NG-FIN-006:** Účelovo viazané prostriedky sa spravujú podľa ich účelu.
- **NG-FIN-007:** Transparentná správa darov a grantov.
- **NG-FIN-008:** Komerčné B2B služby neohrozujú nezávislosť.
- **NG-FIN-009:** Zamerajte sa skôr na udržateľnosť než na maximálne speňaženie.
- **NG-FIN-010:** Štruktúra trvalo zabezpečuje spoločenský účel.

## API, Interfaces, and Communication Architecture (WP 1.11.3)

Na zaistenie stability, bezpečnosti a škálovateľnosti systému sa Nexus Gaja riadi striktne architektúrou založenou na rozhraní API a riadenou udalosťami.

### Základné princípy
- **Žiadny priamy prístup k databáze:** Komponenty komunikujú výlučne prostredníctvom definovaných rozhraní (API alebo Events), nikdy nie prostredníctvom priamych databázových dotazov iných služieb.
- **Brána API:** Všetky požiadavky externých klientov smerujú cez bránu API, ktorá spravuje autentifikáciu, smerovanie a obmedzenie rýchlosti.
- **Abstrakcia poskytovateľov:** Externé služby (modely AI, poskytovatelia platieb, prekladové nástroje) sú integrované prostredníctvom vrstiev abstrakcie, čím sa vyhýbajú pevne zakódovaným závislostiam a umožňujú flexibilnú výmenu poskytovateľov.

### Komunikačné vzory
- **Synchrónne API (REST/HTTPS):** Používa sa na okamžité požiadavky, ako je prihlásenie, nastavenia profilu alebo priame preklady.
– **Asynchrónne udalosti (zbernica udalostí):** Centrálny nervový systém zariadenia Nexus Gaja na oneskorené, oddelené spracovanie (napr. „Message.Created“ spúšťa asynchrónne moderovanie, preklad a upozornenia).
- **V reálnom čase (WebSocket):** Vyhradené kanály pre živý chat a indikátory písania.

### Bezpečnosť a spoľahlivosť
- **Model nulovej dôvery:** Interná sieťová prevádzka nie je automaticky dôveryhodná; citlivá komunikácia medzi službami vyžaduje autentifikáciu.
- **Idempotency & Outbox Pattern:** Kritické operácie (ako dary alebo posielanie správ) sú navrhnuté tak, aby boli idempotentné, aby sa zabránilo duplicitnému spracovaniu, využívajúc vzor Outbox, aby sa zabezpečilo, že udalosti sa nikdy nestratia ani počas databázových transakcií.

## Model domény MVP (WP 1.12)

![Modulárny monolit Nexus Gaja](assets/img/nexus_architecture.jpg)

Nexus Gaja využíva striktne doménovú architektúru MVP (ADR-025), ktorá je navrhnutá ako modulárny monolit s jasnými hranicami domén. Táto štruktúra zabraňuje predčasnej zložitosti mikroslužieb a zároveň zachováva flexibilitu na neskoršie rozdelenie špecifických domén.

### Entity hlavnej domény
Architektúra explicitne oddeľuje odlišné koncepty, aby sa zabezpečila integrita údajov a zabránilo sa štrukturálnym nástrahám, ako je „Používateľské meno = človek“:
– **Identita a účty:** „Osoba“ ≠ „Používateľský účet“ ≠ „Overenie totožnosti“. Overená osoba sa zúčastňuje prostredníctvom účtu, ale subjekty zostávajú oddelené.
- **Komunikácia:** `Správa` ≠ `Preklad`. Pôvodná správa zostáva nemenná; preklady sú prepojené entity.
- **Moderovanie:** „Správa“ ≠ „Rozhodnutie o moderovaní“. Správa je len tvrdenie; moderovaný prípad vedie vyšetrovanie.
- **Financie:** „Dar“ ≠ „Zostatok fondu“. Platby sa účtujú do fondu prostredníctvom nemennej účtovnej knihy, čím sa zabezpečuje finančná transparentnosť.

### Prepojené domény
Systém je rozdelený do jasných logických oblastí (Bounded Contexts): Identita, Účet, Organizácia, Komunikácia, Komunita, Jazyk, Moderovanie, Oznamovanie, Financie a Riadenie. Tieto domény mapujú celú cestu od subjektov v reálnom svete (používateľov, škôl, mimovládnych organizácií) až po ich digitálne interakcie a súvisiace riadenie.

## Stav projektu
Projekt je momentálne vo fáze aktívnej architektúry a plánovania.
Prebiehajúce architektonické rozhodnutia sú zdokumentované v priečinku `/docs`.

---

---

## Licencia a duševné vlastníctvo

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Všetky práva vyhradené.**

**Nexus Gaja** je výhradným duševným vlastníctvom **Jana Sonnera**, ktorý pôsobí v rámci **SonnerStudio**.

Jan Friske je jediným tvorcom, architektom a vlastníkom Nexus Gaja – vrátane všetkých konceptov, architektúry, modelov domén, identity značky a súvisiacej dokumentácie.

**Žiadne tretie strany nevlastnia žiadne práva, licencie ani vlastnícke podiely**, bez ohľadu na ich veľkosť, postavenie na trhu alebo vplyv v technologickom priemysle.

### Čo NIE je dovolené bez výslovného písomného súhlasu:
- Kopírovanie, reprodukovanie alebo distribúcia tohto softvéru alebo jeho dokumentácie
- Úprava, prispôsobovanie alebo vytváranie odvodených diel
- Komerčné využitie akejkoľvek časti Nexus Gaja
- Používanie obsahu tohto úložiska ako tréningových údajov pre systémy AI alebo LLM
- Poskytovanie sublicencie alebo prevod akýchkoľvek práv na tretie strany

### Chránené duševné vlastníctvo
Nasledujúce originálne koncepty sú chránené ako obchodné tajomstvá a vlastné výtvory Jana Sonnera:
- Vrstvený komunikačný model (originál, sémantická interpretácia, preložený výstup)
- Princíp oddelenia identity (osoba nie je účet nie je overenie totožnosti)
- Model oddelenia správy a prekladu (správa nie je preklad)
- Rámec riadenia moderovania AI

### Kontakt
Pre otázky týkajúce sa licencií: https://github.com/SonnerStudio

Nexus Gaja a logo Nexus Gaja sú ochranné známky spoločnosti Jan Friske. Neoprávnené používanie názvu alebo značky je zakázané.

Pozrite si úplné licenčné podmienky v súbore LICENSE.
