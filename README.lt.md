# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** yra išmanus, kontekstui jautrus komunikacijos tinklas, sukurtas pakeisti pasaulinį bendravimą.

## Purpose and Vision
In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Techninė architektūra (pagrindinė koncepcija)

Techninė „Nexus Gaja“ šerdis yra pagal užsakymą sukurtas ryšio modelis, griežtai suskirstytas į tris sluoksnius:

1. **Original**: siuntėjo sukurtas komunikacijos objektas (pranešimas) visada išlieka nepakitęs.
2. **Semantinis aiškinimas**: sistema analizuoja ne tik žodžius, bet ir tikrąją reikšmę.
3. **Target Language Representation**: AI tik sukuria laikiną arba talpykloje saugomą originalo atvaizdą atitinkamam gavėjui pagal pageidaujamą kalbą. Vertimai niekada neperrašo pradinio pranešimo.

### Konteksto priklausomybė
„Nexus Gaja“ vertimai niekada nežiūri pranešimų atskirai. Variklis atsižvelgia į visą hierarchiją:
"Pranešimas" → "Ankstesni pranešimai" → "Gijos kontekstas" → "Bendruomenės kontekstas" → "Kalba / regionas" → "Naudotojo nuostatos"

### Efektyvumas naudojant vertimą pagal pareikalavimą
Vertimas atliekamas efektyviai naudojant išteklius tik **pareikalavus** (pagal poreikį). Kai vartotojas prašo turinio, jis išverčiamas į iš anksto nustatytą kalbą. Sukūrus konkrečios kalbos vertimą, jis išsaugomas visam laikui (talpykloje), kad būtų drastiškai paspartintas būsimų užklausų pateikimas.

## AI padedamas moderavimas (WP 1.8.4)

Naudodami AI padedamą moderavimą žengiame reikšmingą žingsnį nuo produkto idėjos iki techninės architektūros, atsižvelgdami į galiojančius ES reglamentus (ES AI įstatymo skaidrumo reikalavimus pagal 50 str.; Skaitmeninių paslaugų įstatymas su suprantamais pagrindimais ir apeliacijos galimybėmis).

### 1. Pagrindinis principas
Svarbiausias sakinys architektūrai yra toks: **Moderavimo AI yra peržiūros sistema, o ne autonominė valdymo sistema.**
Jis skirtas padėti žmonėms saikingai, o ne pačiam nustatyti, kurioms nuomonėms leidžiama egzistuoti „Nexus Gaja“.
Mes skiriame tris lygius:
– **Aptikimas:** „Čia gali būti taisyklių pažeidimas“.
- **Įvertinimas:** "Taisyklės pažeidimo tikimybė yra, pavyzdžiui, 94 %."
– **Sprendimas:** „Kokių veiksmų iš tikrųjų imamasi?
Trečiąjį lygį sunkiais atvejais turi valdyti žmogus.

### 2. Moderavimo AI kaip posistemė
Vietoj vieno AI sukuriamas tvirtas posistemis:
``` tekstas
                 NEXUS GAJA AI MODERACIJA
                          │
       ┌─────────────────┼─────────────-──
       │ │ │
  Kalba AI sauga AI sukčiavimas AI
       │ │ │
       ├-
       │ │ │
 Vertimo elgesio tapatybė
 Analizė Analizės signalai
       │ │ │
       └──────────────┼───────────────────
                      ▼
               Rizikos vertinimas
                      │
                      ▼
               Žmogaus apžvalga
```

### 3. Svarbiausi AI moduliai
„Nexus Gaja“ naudoja devynias specializuotas analizės sritis:
- **M1 – kalbos supratimas**: aptinka kalbos, dialekto, slengo, ironijos rodiklius, vertimo problemas.
- **M2 – toksiškumo / piktnaudžiavimo aptikimas**: aptinka įžeidimus, asmeninius išpuolius, priekabiavimą.
- **M3 – grėsmių aptikimas**: aptinka galimus grasinimus, šantažą, pranešimus apie smurtą.
- **M4 – neapykantos / nužmoginimo aptikimas**: aptinka tikslinius išpuolius prieš žmones pagal konkrečią priklausomybę.
- **M5 – Šlamšto / manipuliavimo aptikimas**: aptinka šlamštą, robotų elgesį, suderintą manipuliavimą.
- **M6 – sukčiavimo aptikimas**: aptinka įtartinus bandymus sukčiauti, sukčiavimą, socialinę inžineriją.
- **M7 – tapatybės vientisumas**: tikrina signalus dėl paskyros perėmimo, kelių paskyrų, draudimo vengimo.
- **M8 – medijos sauga**: analizuoja vaizdus, ​​garsą, vaizdo įrašus, dokumentus.
- **M9 – kontekstinis variklis**: svarbiausias modulis. Jis sujungia atskiras išvadas.

### 4. Kodėl konteksto variklis yra labai svarbus
Vienos raktinių žodžių paieškos neužtektų. „Galėčiau jį nužudyti iš juoko“ semantiškai apima smurtą, bet yra kalbos figūra. „Rytoj 20 val. aš jį nušausiu priešais jo namus“ – visai kita situacija. AI turi suprasti, ką šis teiginys reiškia konkrečiame kontekste.

### 5. Daugiakalbis moderavimas
Saikingumas negali tiesiog lyginti žodžių. Ji turi išanalizuoti semantinį lygmenį (pvz., vokiečių kalbos ir japonų idiomos, palyginti su regioninėmis išraiškomis).

### 6. Originalo kalba + vertimas
Originalas ir vertimas analizuojami atskirai. Tik tada vyksta „Kombinuotas moderacijos vertinimas“. Tai leidžia „Nexus Gaja“ nustatyti, ar pats vertimas galėjo eskaluoti ar pakeisti faktus.

### 7. Pasitikėjimo balas
Kiekvienas AI įvertinimas gauna pasitikėjimo balą (pvz., grėsmės tikimybė: 0,96). Tačiau: **Pasitikėjimo balas ≠ Tiesa.** 96 % balas reiškia tik tai, kad modelis yra visiškai tikras dėl savo klasifikacijos, o nebūtinai kaltas vartotojas.

### 8. Neapibrėžtumas pats tampa signalu
Jei dirbtinis intelektas yra neaiškus (pvz., grėsmė: 0,62, satyra: 0,54), ji neturi tiesiog priversti laikytis griežtų taisyklių. Vietoj to, neapibrėžtumas yra tiesiogiai įterptas į architektūrą: **Reikalingas žmogaus patikrinimas**.

### 9. Keturios sprendimų zonos
- 🟢 **ŽALIA**: labai tikėtina, kad atitinka reikalavimus. → jokių veiksmų.
- 🟡 **GELTONA**: galimas pažeidimas. → stebėti / prireikus įspėti.
- 🟠 **ORANŽINĖ**: galimas pažeidimas. → moderavimo apžvalga.
- 🔴 **RAAUDONA**: galimas rimtas pažeidimas. → neatidėliotina apsaugos priemonė + žmogaus peržiūra.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Apsaugos priemonės gali atsirasti automatiškai
Konkrečios grėsmės atveju (Aptikta grėsmė → Didelis pasitikėjimas → Laikinas apribojimas → Žmogaus peržiūra → Sprendimas), apsaugome vartotoją, kuriam gresia pavojus, nepaversdami AI teisėju.

### 12. AI turi sugebėti pagrįsti savo sprendimus
DSA reikalauja aiškių ir konkrečių priežasčių. AI pateikia struktūrizuotus argumentus: taisyklė (NG-CONDUCT-004), aptikta (galima konkreti grėsmė), pasitikėjimas (0,94), atitinkamas kontekstas (ankstesni 4 pranešimai), rekomenduojamas veiksmas (žmogaus apžvalga).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. AI sukurtas turinys
Skiriame: žmogaus sukurtą, dirbtinio intelekto padedamą, dirbtinio intelekto sukurtą ir dirbtinio intelekto manipuliuotą. Tai taps turinio metaduomenų dalimi.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Gilus klastotės aptikimas
Architektūra siekiama aptikti sintetinius vaizdus, klonuotus balsus ir gilius klastotes. Tačiau aptikimas nėra automatinis įrodymas.

### 17. Nėra automatinio „tiesos mašinos“ (nuosaikumas ≠ faktų tikrinimas)
Viena sistema tikrina: "Ar turinys pažeidžia taisykles?" (Turinio moderavimas), kitas pateikia: "Kokia informacija ir šaltiniai yra prieinami?" (Informacinė pagalba). Nuomonės nėra tiesiog ištrinamos dėl to, kad jos yra „klaidingos“.

### 18. Apsauga nuo klaidingo kultūrinio interpretavimo
AI reikalauja **Kultūrinio konteksto modelių**, kad vienos šalies komunikacijos normos nebūtų laikomos pasauliniu standartu.

### 19. Ironija, satyra ir humoras
AI naudoja kontekstą, jaustukus, pokalbių istoriją ir žinomas ironijos struktūras, tačiau turi leisti neapibrėžtumą, kai reikšmės yra dviprasmiškos.

### 20. Jokios bausmės remiantis vienu AI balu
Jokia rimta moderavimo intervencija negali būti grindžiama tik vienu automatizuotu klasifikavimo rezultatu (tekstas + kontekstas + elgsena + kalba + medija + taisyklių variklis = rizikos vertinimas).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Kalbos teisingumas ir vertimo šališkumas
Moderavimo kokybė turi būti palyginama visomis palaikomomis kalbomis (Multilingual Moderation Benchmark). Jei moderavimo rezultatai skiriasi nuo originalo ir vertimo (vertimo konfliktas), tai reikia konkrečiai peržiūrėti.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Projekto būsena
Šiuo metu projektas yra aktyvaus architektūros ir planavimo etape.
Vykdomi architektūriniai sprendimai dokumentuojami aplanke „/docs“.