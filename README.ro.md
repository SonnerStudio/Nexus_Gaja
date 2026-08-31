# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** este o rețea de comunicare inteligentă, sensibilă la context, concepută pentru a revoluționa comunicarea globală.

## Scop și viziune
Într-o lume globalizată, limba este adesea cea mai mare barieră. Scopul principal al Nexus Gaja este de a permite comunicarea fără probleme, fără bariere și precisă din punct de vedere contextual între oameni, indiferent dacă vorbesc o limbă comună.

Nu este vorba doar despre traducerea rigidă a cuvintelor, ci despre **transferarea sensului**. Nexus Gaja conectează oamenii la un nivel mai profund prin înțelegerea nuanțelor culturale, regionale și contextuale, permițând astfel conversații autentice și autentice.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

Miezul tehnic al Nexus Gaja este un model de comunicare personalizat, care este strict împărțit în trei straturi:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Dependența de context
Traducerile din Nexus Gaja nu vizualizează niciodată mesajele izolat. Motorul ia în considerare întreaga ierarhie:
`Mesaj` → `Mesaje anterioare` → `Contextul firului` → `Contextul comunității` → `Limbă/Regiune` → `Preferințe utilizator`

### Eficiență prin traducere la cerere
Traducerea are loc eficient din punct de vedere al resurselor doar **la cerere** (la cerere). Când un utilizator solicită conținut, acesta este tradus în limba lor prestabilită. Odată ce o traducere pentru o anumită limbă este generată, aceasta este stocată permanent (caching) pentru a accelera drastic solicitările viitoare.

## Moderare asistată de IA (WP 1.8.4)

Cu AI-Assisted Moderation, facem un pas semnificativ de la ideea de produs la arhitectura tehnică, ținând cont de reglementările UE actuale (cerințele de transparență ale Legii UE AI în conformitate cu art. 50; Legea privind serviciile digitale cu justificări și opțiuni de recurs inteligibile).

### 1. Principiul de bază
Cea mai importantă propoziție pentru arhitectură este: ** AI de moderare este un sistem de revizuire, nu un sistem de guvernare autonom.**
Este conceput pentru a ajuta oamenii cu moderație, nu pentru a determina singur ce opinii au permisiunea de a exista pe Nexus Gaja.
Facem diferența între trei niveluri:
- **Detecție:** „Ar putea exista o încălcare a regulilor aici.”
- **Evaluare:** „Probabilitatea unei încălcări a regulilor este, de exemplu, de 94%.
- **Decizie:** "Ce măsuri se întreprind de fapt?"
Al treilea nivel trebuie controlat de un om în cazuri severe.

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

### 3. Cele mai importante module AI
Nexus Gaja utilizează nouă domenii de analiză specializate:
- **M1 – Înțelegerea limbii**: detectează limbă, dialect, argo, indicatori de ironie, probleme de traducere.
- **M2 – Detectare toxicitate/abuz**: detectează insulte, atacuri personale, hărțuire.
- **M3 – Detectare amenințări**: detectează potențiale amenințări, șantaj, anunțuri de violență.
- **M4 – Detectarea urii/dezumanizării**: detectează atacuri direcționate asupra persoanelor pe baza unor afilieri specifice.
- **M5 – Detectare spam/manipulare**: detectează spam-ul, comportamentul botului, manipularea coordonată.
- **M6 – Detectare fraudă**: detectează tentative de fraudă suspecte, phishing, inginerie socială.
- **M7 – Identity Integrity**: Verifică semnalele privind preluarea de conturi, mai multe conturi, evaziunea interzicerii.
- **M8 – Media Safety**: analizează imagini, audio, video, documente.
- **M9 – Context Engine**: Cel mai important modul. Acesta îmbină constatările individuale.

### 4. De ce este crucial motorul de context
O căutare pură de cuvinte cheie ar fi insuficientă. „L-aș putea ucide de râs” conține violență din punct de vedere semantic, dar este o figură de stil. „Mâine la 20.00 îl voi împușca în fața casei lui” este cu totul altă situație. AI trebuie să înțeleagă ce înseamnă declarația în contextul său specific.

### 5. Moderare multilingvă
Moderația nu poate compara pur și simplu cuvintele. Trebuie să analizeze nivelul semantic (de exemplu, idiomuri germane vs. idiomuri japoneze vs. expresii regionale).

### 6. Limba originală + traducere
Originalul și traducerea sunt analizate separat. Abia atunci are loc „Evaluarea Moderației Combinate”. Acest lucru îi permite lui Nexus Gaja să determine dacă traducerea în sine ar fi putut escalada sau modificat faptele.

### 7. Scorul de încredere
Fiecare evaluare AI primește un scor de încredere (de exemplu, Probabilitatea de amenințare: 0,96). Cu toate acestea: **Scor de încredere ≠ Adevăr**. Un scor de 96% înseamnă doar că modelul este foarte sigur de clasificarea sa, nu neapărat că utilizatorul este vinovat.

### 8. Incertitudinea devine în sine un semnal
Dacă IA este incertă (de exemplu, Amenințare: 0,62, Satira: 0,54), nu trebuie să impună pur și simplu reguli dure. În schimb, incertitudinea este construită direct în arhitectură: **Este necesară o revizuire umană**.

### 9. Four Decision Zones
- 🟢 **GREEN**: Highly likely compliant. → no action.
- 🟡 **YELLOW**: Possible violation. → monitor / provide a warning if necessary.
- 🟠 **ORANGE**: Probable violation. → moderation review.
- 🔴 **RED**: Severe possible violation. → immediate protective measure + human review.

### 10. Fără „Pedeapsă AI”
**AI nu impune sancțiuni finale.** Poate declanșa măsuri tehnice imediate (de exemplu, reținerea temporară a unui mesaj) pentru probleme grave de securitate, dar decizia finală rămâne verificabilă.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI nu trebuie să modifice în secret conținutul
**Moderarea AI nu trebuie să modifice niciodată conținutul original neobservat.** În timpul corectării, traducerii sau rezumarii automate, originalul este întotdeauna păstrat.

### 14. Conținut generat de AI
Facem distincție între: creat de om, asistat de inteligență artificială, generat de inteligență artificială și manipulat de inteligență artificială. Aceasta va deveni parte din metadatele de conținut.

### 15. Etichetarea conținutului AI și a stratului de proveniență AI
În conformitate cu regulile de transparență ale Actului UE AI (în vigoare din august 2026), conținutul generat de IA trebuie să fie identificabil. Oferim un strat de proveniență AI care stochează metadate (Origine AI, Model, Timp, Human Review).

### 16. Detectare Deepfake
Arhitectura își propune să detecteze imagini sintetice, voci clonate și deepfake. Cu toate acestea, detectarea nu este o dovadă automată.

### 17. Fără „mașină de adevăr” automată (moderare ≠ verificarea faptelor)
Un sistem verifică: „Conținutul încalcă regulile?” (Moderarea conținutului), un altul prevede: „Ce informații și surse sunt disponibile?” (Asistență pentru informații). Opiniile nu sunt șterse pur și simplu pentru că sunt „greșite”.

### 18. Protecție împotriva interpretării greșite culturale
AI necesită **Modele de context cultural** pentru a preveni ca normele de comunicare ale unei țări să fie asumate ca standard global.

### 19. Ironie, satira și umor
AI folosește contextul, emoji-urile, istoricul conversațiilor și structurile de ironie cunoscute, dar trebuie să permită incertitudinea atunci când semnificațiile sunt ambigue.

### 20. Nicio pedeapsă bazată pe un singur scor AI
Nicio intervenție severă de moderare nu se poate baza doar pe un singur rezultat de clasificare automatizată (Text + Context + Comportament + Limbă + Media + Rule Engine = Evaluarea riscurilor).

### 21. Semnale de comportament al utilizatorilor și sistem fără credit social
Aceasta se referă la semnalele tehnice de abuz (de exemplu, postarea de spam în masă), nu un sistem general de evaluare socială. Nexus Gaja nu menține un sistem de credit social – moderarea servește la securitate, nu la evaluarea valorii unei persoane.

### 22. Moderația AI trebuie să fie auditabilă
Toate deciziile automate relevante sunt înregistrate (ID-ul evenimentului, ID-ul regulii, Încrederea, Revizuirea umană etc.) pentru a asigura trasabilitatea.

### 23. False pozitive, false negative și valori de calitate
Tipurile de erori sunt monitorizate. Un tablou de bord măsoară precizia, rechemarea și, în special, **Rata de anulare a contestațiilor** (numărul de contestații reușite).

### 24. Echitatea lingvistică și părtinirea traducerii
Calitatea moderației trebuie să fie comparabilă în toate limbile acceptate (Multilingual Moderation Benchmark). Dacă rezultatele moderarii diferă între original și traducere (Conflict de traducere), aceasta trebuie revizuită în mod specific.

### 25. Motor de propuneri de arhitectură și politici
Regulile (Policy Engine) nu sunt codificate hard în modelele AI. AI furnizează constatări; Motorul de politici decide pe baza regulilor actuale. Acest lucru permite **modificări de model fără modificări de reguli**.

### 26. Omul rămâne autoritatea finală
- **NG-AI-MOD-001**: AI ajută la detectarea și clasificarea, dar nu înlocuiește evaluarea umană în deciziile severe.
- **NG-AI-MOD-002**: deciziile automate de moderare trebuie să fie urmăribile, înregistrate și verificabile.

**Rezumat**: construim un sistem în patru etape: Detectarea AI, Analiza contextului și a riscurilor, Motorul de politici și Guvernarea umană. Acest lucru permite o automatizare puternică fără a crea o arhitectură periculoasă „AI ca judecător”.

## Starea proiectului
Proiectul se află în prezent în faza activă de arhitectură și planificare.
Deciziile arhitecturale în curs sunt documentate în folderul `/docs`.