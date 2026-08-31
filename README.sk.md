# Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** je inteligentná, kontextovo citlivá komunikačná sieť navrhnutá tak, aby spôsobila revolúciu v globálnej komunikácii.

## Účel a vízia
V globalizovanom svete je jazyk často najväčšou bariérou. Hlavným cieľom Nexus Gaja je umožniť bezproblémovú, bezbariérovú a kontextovo presnú komunikáciu medzi ľuďmi – bez ohľadu na to, či hovoria spoločným jazykom.

Nejde len o strnulé prekladanie slov, ale o **prenášanie významu**. Nexus Gaja spája ľudí na hlbšej úrovni pochopením kultúrnych, regionálnych a kontextových nuancií, čím umožňuje skutočné, autentické rozhovory.

## Možnosti a funkcie
- **Multimediálna komunikácia**: Systém spracováva nielen text, ale aj obraz, zvuk a video. To umožňuje plne pohlcujúce konverzácie (napr. videohovory alebo hlasové správy) v reálnom čase bez ohľadu na jazykové bariéry.
- **Kontextová citlivosť**: Rozpoznanie irónie, idiómov, žargónu a regionálnych dialektov, ktorým konvenční prekladatelia často nerozumejú.
- **Sieť naprieč platformami**: Slúži ako základ pre súkromné ​​rozhovory, vlákna fóra (príspevky s komentármi) a interakcie s globálnou komunitou.

---

## Technická architektúra (základný koncept)

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

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. Basic Principle
The most important sentence for the architecture is: **The moderation AI is a review system, not an autonomous ruling system.**
It is designed to assist humans in moderation, not to determine itself which opinions are allowed to exist on Nexus Gaja.
We differentiate between three levels:
- **Detection:** "There could be a rule violation here."
- **Evaluation:** "The probability of a rule violation is, for example, 94%."
- **Decision:** "What action is actually taken?"
The third level must be controlled by a human in severe cases.

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

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

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
Umelá inteligencia používa kontext, emotikony, históriu konverzácií a známe ironické štruktúry, ale musí počítať s neistotou, keď sú významy nejednoznačné.

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

## Stav projektu
Projekt je momentálne vo fáze aktívnej architektúry a plánovania.
Prebiehajúce architektonické rozhodnutia sú zdokumentované v priečinku `/docs`.