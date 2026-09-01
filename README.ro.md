# Nexus Gaja

> *Pentru pace globală și înțelegere reciprocă*


![Nexus Gaja Logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** este o rețea de comunicare inteligentă, sensibilă la context, concepută pentru a revoluționa comunicarea globală.

## Scop și viziune

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

Într-o lume globalizată, limba este adesea cea mai mare barieră. Scopul principal al Nexus Gaja este de a permite comunicarea fără probleme, fără bariere și precisă din punct de vedere contextual între oameni, indiferent dacă vorbesc o limbă comună.

Nu este vorba doar despre traducerea rigidă a cuvintelor, ci despre **transferarea sensului**. Nexus Gaja conectează oamenii la un nivel mai profund prin înțelegerea nuanțelor culturale, regionale și contextuale, permițând astfel conversații autentice și autentice.

## Posibilități și caracteristici
- **Comunicare multimedia**: sistemul procesează nu doar text, ci și imagini, audio și video. Acest lucru permite conversații complet captivante (de exemplu, apeluri video sau mesaje vocale) în timp real, peste barierele lingvistice.
- **Sensibilitatea contextului**: recunoașterea ironiei, a idiomurilor, a jargonului și a dialectelor regionale care sunt adesea înțelese greșit de traducătorii convenționali.
- **Rețea multiplatformă**: servește drept bază pentru chat-urile private, firele de discuții pe forum (postări cu comentarii) și interacțiunile comunității globale.

---

## Technical Architecture (Core Concept)

![Conceptul de traducere Nexus Gaja](assets/img/nexus_translation.jpg)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Original**: Obiectul de comunicare (mesajul) creat de expeditor rămâne întotdeauna imuabil.
2. **Interpretare semantică**: Sistemul analizează nu doar cuvintele, ci și sensul real.
3. **Reprezentare în limba țintă**: AI creează doar o reprezentare temporară sau în cache a originalului pentru destinatarul respectiv, pe baza limbii preferate. Traducerile nu suprascriu niciodată mesajul original.

### Dependența de context
Traducerile din Nexus Gaja nu vizualizează niciodată mesajele izolat. Motorul ia în considerare întreaga ierarhie:
`Mesaj` → `Mesaje anterioare` → `Contextul firului` → `Contextul comunității` → `Limbă/Regiune` → `Preferințe utilizator`

### Eficiență prin traducere la cerere
Traducerea are loc eficient din punct de vedere al resurselor doar **la cerere** (la cerere). Când un utilizator solicită conținut, acesta este tradus în limba lor prestabilită. Odată ce o traducere pentru o anumită limbă este generată, aceasta este stocată permanent (caching) pentru a accelera drastic solicitările viitoare.

## Moderare asistată de IA (WP 1.8.4)

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

Cu AI-Assisted Moderation, facem un pas semnificativ de la ideea de produs la arhitectura tehnică, ținând cont de reglementările UE actuale (cerințele de transparență ale Legii UE AI în conformitate cu art. 50; Legea privind serviciile digitale cu justificări și opțiuni de recurs inteligibile).

### 1. Principiul de bază
Cea mai importantă propoziție pentru arhitectură este: ** AI de moderare este un sistem de revizuire, nu un sistem de guvernare autonom.**
Este conceput pentru a ajuta oamenii cu moderație, nu pentru a determina singur ce opinii au permisiunea de a exista pe Nexus Gaja.
Facem diferența între trei niveluri:
- **Detecție:** „Ar putea exista o încălcare a regulilor aici.”
- **Evaluare:** „Probabilitatea unei încălcări a regulilor este, de exemplu, de 94%.
- **Decizie:** "Ce măsuri se întreprind de fapt?"
Al treilea nivel trebuie controlat de un om în cazuri severe.

### 2. AI de moderare ca subsistem
În loc de un singur AI, este stabilit un subsistem robust:
```text
                 MODERARE NEXUS GAJA AI
                          │
       ┌──────────────────┼─────────────────────
       │ │ │
  Language AI Safety AI Fraud AI
       │ │ │
       ├──────────────┬───┴──────────────────────
       │ │ │
 Identitatea comportamentului de traducere
 Analiză Semnale de analiză
       │ │ │
       └──────────────┼───────────────────
                      ▼
               Evaluarea riscurilor
                      │
                      ▼
               Revista umană
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

### 9. Patru zone de decizie
- 🟢 **VERDE**: foarte probabil conform. → nicio acțiune.
- 🟡 **GALBEN**: Posibilă încălcare. → monitorizați / furnizați un avertisment dacă este necesar.
- 🟠 **ORANGE**: Încălcare probabilă. → revizuire moderare.
- 🔴 **ROȘU**: posibilă încălcare gravă. → măsură de protecție imediată + revizuire umană.

### 10. Fără „Pedeapsă AI”
**AI nu impune sancțiuni finale.** Poate declanșa măsuri tehnice imediate (de exemplu, reținerea temporară a unui mesaj) pentru probleme grave de securitate, dar decizia finală rămâne verificabilă.

### 11. Măsurile de protecție pot apărea automat
În cazul unei amenințări concrete (Amenințare detectată → Încredere ridicată → Restricție temporară → Revizuire umană → Decizie), protejăm utilizatorul amenințat fără a transforma IA într-un judecător.

### 12. AI trebuie să fie capabilă să-și justifice deciziile
DSA necesită motive clare și specifice. AI oferă raționament structurat: Regulă (NG-CONDUCT-004), Detectat (Potențial amenințare concretă), Încredere (0,94), Context relevant (Mesaje anterioare 4), Acțiune recomandată (Evaluare umană).

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

## Principii de finanțare și model de venituri (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

Pentru Nexus Gaja, se aplică un principiu economic extrem de important: **Fără publicitate tradițională în cadrul platformei.**
Acest lucru distinge fundamental Nexus Gaja de multe dintre rețelele sociale de astăzi. Cu toate acestea, acest lucru nu înseamnă că Nexus Gaja nu poate avea un caracter comercial. Dimpotrivă, platforma trebuie să fie viabilă din punct de vedere economic, astfel încât scopul ei social să poată rezista. Activitatea economică este un mijloc pentru un scop, nu scopul principal al platformei.

### 1. Principiul NG-FIN-001
Nexus Gaja își finanțează operațiunile prin fluxuri transparente de venituri separate de interesele utilizatorilor, și nu prin monetizarea atenției utilizatorilor sau a datelor personale.

### 2. Fără publicitate tradițională
Sunt interzise în mod special:
- reclame bannere
- Reclame pop-up
- Redare automată a anunțurilor video
- Postări sponsorizate în feedul standard
- Profiluri de publicitate personalizate
- Vânzarea profilurilor de utilizator sau a datelor personale
- Publicitate derivată din conversații private.

Nexus Gaja rămâne mai degrabă un **spațiu de comunicare decât un spațiu publicitar**.

### 3. Finanțare fără publicitate (Cei 6 piloni)
Finanțarea este construită pe șase piloni:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   DONATII ORGANIZATII PREMIUM
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    ACORDĂ SERVICII DE PARTENERIAT
```

#### Pilonul 1 – Abonament de bază gratuit
**Nexus Gaja Free** permite înțelegerea internațională de bază pentru toată lumea (profil, comunicare internațională, postări, comunități, chat-uri, traducere de bază) fără costuri.

#### Pilonul 2 – Oferte premium
Oferte plătite voluntare (**Nexus Gaja Plus**) care oferă limite mai mari de stocare, calitate media mai mare, cote extinse de AI și funcții organizaționale.
**Important (Freemium în loc de Dark Freemium):** Comunicarea de bază nu trebuie să fie niciodată degradată artificial.

#### Pilonul 3 – Organizații
Conturi speciale pentru școli, universități, ONG-uri, întreprinderi și municipalități (**Nexus Gaja Organization**). Școlile pot fi susținute prin rate instituționale ca multiplicatori ai înțelegerii internaționale.

#### Pilonul 4 – Donații
**Fondul de finanțare Nexus Gaja** acceptă donații generale și alocate (de exemplu, „pentru comunicarea internațională a tinerilor”). Un **Registrul de alocare a fondurilor** asigură o alocare transparentă a fondurilor.
**Purpose Fund & Tombola:** O parte din donații alimentează un fond pentru utilizare gratuită/reducere. Un mecanism de loterie/tombola poate aloca aceste fonduri în mod transparent și auditabil.

#### Pilonul 5 – Finanțarea instituțională
Fundații, programe de finanțare culturală sau programe de stat.
**NG-FIN-002:** Sprijinul financiar nu cumpără control editorial sau tehnic (Independență).

#### Pilonul 6 – Servicii comerciale
Servicii B2B, cum ar fi **Translation-as-a-Service** (API), comunicarea organizațională sau sălile de conferințe internaționale, fără a încărca fluxul standard al utilizatorilor.

### 4. Fără monetizare de date și economie de supraveghere
**NG-FIN-003:** Datele personale ale utilizatorilor nu sunt o marfă. Nicio vânzare de liste, profiluri sau istorii. Nexus Gaja nu profită de supravegherea psihologică (Economia de Supraveghere).

### 5. Transparența financiară și Registrul fondurilor
**Nexus Gaja Financial Transparency:** Publicarea structurilor financiare agregate. Donațiile alocate primesc contabilitate tehnică (ID fond → Scop → Sold → Alocare). Fără subvenționare încrucișată a scopurilor sociale în marketingul corporativ.

### 6. Modelul de finanțare pe bază de solidaritate
Prețurile se bazează pe orientarea către costuri, corectitudine și solidaritate.
**Solidarity Premium:** O opțiune voluntară pentru utilizatorii Premium de a finanța o parte din accesul altui utilizator. Solidaritatea forțată sau o societate de clasă premium (mai puțin respect/moderare pentru utilizatorii gratuiti) este strict interzisă.

### 7. KPI-uri economice în loc de economia de implicare
Fără dependență de menținerea utilizatorilor „online cât mai mult posibil” (fără ragebait, fluxuri infinite).
În schimb, folosim valori precum:
- **Indexul de comunicare globală (GCI):** Relații de comunicare de succes între oameni din diferite regiuni lingvistice/culturale.
- **Platform Sustainability Ratio (PSR):** Venituri recurente / costuri operaționale recurente (țintă ≥ 1).

### 8. Ce nu dorim în mod explicit (Lista negativă)
Nexus Gaja **nu** este finanțat de:
❌ Vânzarea datelor cu caracter personal
❌ Publicitate tradițională personalizată
❌ Monitorizarea comportamentului utilizatorilor în scopuri publicitare
❌ Vânzarea datelor de comunicații private
❌ Utilizarea ascunsă a datelor AI
❌ Paywall-uri Premium manipulative
❌ Restricție de acoperire artificială pentru monetizare
❌ Influență politică plătită
❌ Achiziționarea deciziilor de moderare privilegiate.

### 9. Arhitectura financiară preliminară
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼─────────────────
             │ │ │
             ▼ ▼ ▼
          ORGANIZAȚII DE UTILIZATORI ÎNTREPRINDEREA
             │ │ │
             └────────────────┼─────────────────
                              │
                       SERVICII DE PLATFORMĂ
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API DONAȚII PREMIUM
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               FOND GENERAL FONDURI RESTRICȚIONATE
                                        │
                                        ▼
                                  SCOP SOCIAL
```

### Rezumatul principiilor de finanțare (NG-FIN)
- **NG-FIN-001:** Fără finanțare prin publicitate tradițională.
- **NG-FIN-002:** Fără control editorial/tehnic prin sprijin financiar.
- **NG-FIN-003:** Datele personale nu sunt o marfă.
- **NG-FIN-004:** Comunicarea de bază rămâne accesibilă fără plată.
- **NG-FIN-005:** Ofertele premium nu trebuie să degradeze utilizatorii gratuiti.
- **NG-FIN-006:** Fondurile alocate sunt gestionate în funcție de scopul lor.
- **NG-FIN-007:** Gestionarea transparentă a donațiilor și granturilor.
- **NG-FIN-008:** Serviciile comerciale B2B nu compromit independența.
- **NG-FIN-009:** Concentrați-vă pe durabilitate mai degrabă decât pe monetizarea maximă.
- **NG-FIN-010:** Structura asigură permanent scopul social.

## API, interfețe și arhitectură de comunicare (WP 1.11.3)

Pentru a asigura stabilitatea, securitatea și scalabilitatea sistemului, Nexus Gaja urmează o arhitectură strict bazată pe API și bazată pe evenimente.

### Principii de bază
- **Fără acces direct la baza de date:** Componentele comunică exclusiv prin interfețe definite (API-uri sau evenimente), niciodată prin interogări directe de baze de date ale altor servicii.
- **API Gateway:** Toate solicitările clientului extern sunt direcționate printr-un API Gateway care gestionează autentificarea, rutarea și limitarea ratei.
- **Abstracția furnizorului:** Serviciile externe (modele AI, furnizorii de plată, motoare de traducere) sunt integrate prin straturi de abstracție, evitând dependențele codificate și permițând schimbarea flexibilă a furnizorilor.

### Modele de comunicare
- **API-uri sincrone (REST/HTTPS):** utilizate pentru solicitări imediate, cum ar fi autentificare, setări de profil sau traduceri directe.
- **Evenimente asincrone (Event Bus):** Sistemul nervos central al Nexus Gaja pentru procesare întârziată, decuplată (de exemplu, „Message.Created” care declanșează Moderarea, Traducerea și Notificarea în mod asincron).
- **În timp real (WebSocket):** Canale dedicate pentru chat live și indicatori de tastare.

### Securitate și fiabilitate
- **Model Zero-Trust:** Traficul intern al rețelei nu este automat de încredere; comunicarea sensibilă de la serviciu la serviciu necesită autentificare.
- **Idempotity & Outbox Pattern:** Operațiunile critice (cum ar fi donațiile sau mesajele) sunt concepute pentru a fi idempotente pentru a preveni duplicarea procesării, utilizând modelul Outbox pentru a se asigura că evenimentele nu se pierd niciodată, chiar și în timpul tranzacțiilor cu baza de date.

## Model de domeniu MVP (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja folosește o arhitectură MVP strict bazată pe domenii (ADR-025), concepută ca un monolit modular cu limite clare de domeniu. Această structură previne complexitatea prematură a microserviciilor, păstrând în același timp flexibilitatea de a împărți mai târziu anumite domenii.

### Entități de domeniu de bază
Arhitectura separă în mod explicit concepte distincte pentru a asigura integritatea datelor și pentru a evita capcanele structurale precum „Nume utilizator = Om”:
- **Identitate și conturi:** `Persoană` ≠ `Cont de utilizator` ≠ `Verificarea identității`. O persoană verificată participă printr-un cont, dar entitățile rămân separate.
- **Comunicare:** `Mesaj` ≠ `Traducere`. Mesajul original rămâne imuabil; traducerile sunt entități legate.
- **Moderare:** `Raport` ≠ `Decizie de moderare`. Un raport este doar o revendicare; un caz de moderare conduce ancheta.
- **Finanțe:** `Donație` ≠ `Soldul fondului`. Plățile sunt înregistrate printr-un registru imuabil la un fond, asigurând transparența financiară.

### Domenii interconectate
Sistemul este împărțit în domenii logice clare (Contexte delimitate): Identitate, Cont, Organizație, Comunicare, Comunitate, Limbă, Moderare, Notificare, Finanțe și Guvernare. Aceste domenii cartografiază întreaga călătorie de la entitățile din lumea reală (Utilizatori, școli, ONG-uri) la interacțiunile lor digitale și guvernanța aferentă.

## Starea proiectului
Proiectul se află în prezent în faza activă de arhitectură și planificare.
Deciziile arhitecturale în curs sunt documentate în folderul `/docs`.

---

---

## Licență și proprietate intelectuală

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Toate drepturile rezervate.**

**Nexus Gaja** este proprietatea intelectuală exclusivă a **Jan Friske**, care operează sub **SonnerStudio**.

Jan Friske este singurul creator, arhitect și proprietar al Nexus Gaja, inclusiv toate conceptele, arhitectura, modelele de domenii, identitatea mărcii și documentația asociată.

**Nu sunt deținute drepturi, licențe sau interese de proprietate de către niciun terț**, indiferent de dimensiunea, poziția pe piață sau influența acestora în industria tehnologiei.

### Ce NU este permis fără acordul explicit scris:
- Copierea, reproducerea sau distribuirea acestui software sau a documentației sale
- Modificarea, adaptarea sau crearea de lucrări derivate
- Utilizarea comercială a oricărei părți a Nexus Gaja
- Utilizarea conținutului acestui depozit ca date de instruire pentru sisteme AI sau LLM
- Sublicențierea sau transferul oricăror drepturi către terți

### Proprietate intelectuală protejată
Următoarele concepte originale sunt protejate ca secrete comerciale și creații proprietare ale lui Jan Friske:
- Modelul de comunicare stratificat (original, interpretare semantică, rezultat tradus)
- Principiul separării identității (Persoana nu este un cont nu este verificarea identității)
- Modelul de decuplare mesaj-traducere (Mesajul nu este traducere)
- Cadrul de guvernare a moderarii AI

### Contact
Pentru întrebări privind licențele: https://github.com/SonnerStudio

Nexus Gaja și sigla Nexus Gaja sunt mărci comerciale ale lui Jan Friske. Utilizarea neautorizată a numelui sau mărcii este interzisă.

Vedeți termenii completi de licență în fișierul LICENȚĂ.
