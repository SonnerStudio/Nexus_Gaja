# Nexus Gaja

![Nexus Gaja logotips](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** ir vieds, kontekstjutīgs saziņas tīkls, kas izstrādāts, lai mainītu globālo saziņu.

## Mērķis un vīzija
Globalizētajā pasaulē valoda bieži vien ir lielākā barjera. Nexus Gaja galvenais mērķis ir nodrošināt netraucētu, bezšķēršļu un kontekstuāli precīzu saziņu starp cilvēkiem neatkarīgi no tā, vai viņi runā kopīgā valodā.

Runa nav tikai par stingru vārdu tulkošanu, bet par **nozīmes pārnešanu**. Nexus Gaja saista cilvēkus dziļākā līmenī, izprotot kultūras, reģionālās un kontekstuālās nianses, tādējādi nodrošinot patiesas, autentiskas sarunas.

## Iespējas un funkcijas
- **Multivides sakari**: sistēma apstrādā ne tikai tekstu, bet arī attēlu, audio un video. Tas ļauj reāllaikā veidot visaptverošas sarunas (piemēram, videozvanus vai balss ziņas) pāri valodas barjerām.
- **Kontekstu jutīgums**: ironijas, idiomu, žargona un reģionālo dialektu atpazīšana, ko parastie tulki bieži pārprot.
- **Starpplatformu tīkls**: kalpo kā pamats privātām tērzēšanas sarunām, foruma pavedieniem (ziņas ar komentāriem) un globālās kopienas mijiedarbībām.

---

## Tehniskā arhitektūra (pamatkoncepcija)

Nexus Gaja tehniskais kodols ir īpaši izveidots sakaru modelis, kas ir stingri sadalīts trīs slāņos:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## AI atbalstīta regulēšana (WP 1.8.4)

Izmantojot AI atbalstītu moderāciju, mēs speram nozīmīgu soli no produkta idejas līdz tehniskajai arhitektūrai, ņemot vērā pašreizējos ES noteikumus (ES AI likuma pārredzamības prasības saskaņā ar 50. pantu; Digitālo pakalpojumu likums ar saprotamiem pamatojumiem un apelācijas iespējām).

### 1. Basic Principle
The most important sentence for the architecture is: **The moderation AI is a review system, not an autonomous ruling system.**
It is designed to assist humans in moderation, not to determine itself which opinions are allowed to exist on Nexus Gaja.
We differentiate between three levels:
- **Detection:** "There could be a rule violation here."
- **Evaluation:** "The probability of a rule violation is, for example, 94%."
- **Decision:** "What action is actually taken?"
The third level must be controlled by a human in severe cases.

### 2. Moderācijas AI kā apakšsistēma
Viena AI vietā tiek izveidota spēcīga apakšsistēma:
``` teksts
                 NEXUS GAJA AI MODERĀCIJA
                          │
       ┌─────────────────┼───────────────────
       │ │ │
  Valoda AI Drošība AI Krāpšana AI
       │ │ │
       -
       │ │ │
 Tulkošanas uzvedības identitāte
 Analīze Analīzes signāli
       │ │ │
       └──────────────┼────────────────────
                      ▼
               Riska novērtējums
                      │
                      ▼
               Cilvēka apskats
```

### 3. Vissvarīgākie AI moduļi
Nexus Gaja izmanto deviņas specializētas analīzes jomas:
- **M1 — valodas izpratne**: nosaka valodu, dialektu, slengu, ironijas rādītājus, tulkošanas problēmas.
- **M2 — toksicitātes / ļaunprātīgas izmantošanas noteikšana**: nosaka apvainojumus, personiskus uzbrukumus, uzmākšanos.
- **M3 — draudu noteikšana**: atklāj iespējamos draudus, šantāžu, paziņojumus par vardarbību.
- **M4 — naida/dehumanizācijas noteikšana**: nosaka mērķtiecīgus uzbrukumus cilvēkiem, pamatojoties uz konkrētu piederību.
- **M5 — surogātpasta/manipulāciju noteikšana**: nosaka surogātpastu, robotu uzvedību, koordinētas manipulācijas.
- **M6 — krāpšanas noteikšana**: atklāj aizdomīgus krāpšanas mēģinājumus, pikšķerēšanu, sociālo inženieriju.
- **M7 — identitātes integritāte**: pārbauda signālus par kontu pārņemšanu, vairākiem kontiem, izvairīšanos no aizlieguma.
- **M8 — multivides drošība**: analizē attēlus, audio, video, dokumentus.
- **M9 — konteksta dzinējs**: vissvarīgākais modulis. Tas apvieno atsevišķus atklājumus.

### 4. Kāpēc konteksta programmai ir izšķiroša nozīme
Ar tīru atslēgvārdu meklēšanu nepietiktu. "Es varētu viņu nogalināt no smiekliem" semantiski satur vardarbību, bet ir runas figūra. "Rīt pulksten 20 es viņu nošaušu viņa mājas priekšā" ir pavisam cita situācija. AI ir jāsaprot, ko paziņojums nozīmē tā konkrētajā kontekstā.

### 5. Daudzvalodu moderēšana
Mērenība nevar vienkārši salīdzināt vārdus. Tai ir jāanalizē semantiskais līmenis (piemēram, vācu idiomas pret japāņu idiomas pret reģionālajām izteiksmēm).

### 6. Oriģinālvaloda + tulkojums
Oriģināls un tulkojums tiek analizēti atsevišķi. Tikai pēc tam notiek "Kombinētais moderācijas novērtējums". Tas ļauj Nexus Gaja noteikt, vai pats tulkojums, iespējams, ir saasinājis vai mainījis faktus.

### 7. Pārliecības rādītājs
Katrs AI novērtējums saņem ticamības punktu (piemēram, draudu iespējamība: 0,96). Tomēr: **Uzticības rādītājs ≠ Patiesība.** 96% rādītājs tikai nozīmē, ka modelis ir ļoti pārliecināts par savu klasifikāciju, bet ne vienmēr to, ka vainīgs ir lietotājs.

### 8. Nenoteiktība pati par sevi kļūst par signālu
Ja mākslīgais intelekts ir neskaidrs (piemēram, draudi: 0,62, satīra: 0,54), tas nedrīkst vienkārši īstenot bargus noteikumus. Tā vietā nenoteiktība ir tieši iebūvēta arhitektūrā: **Nepieciešams cilvēka pārskats**.

### 9. Četras lēmumu zonas
- 🟢 **ZAĻA**: ļoti iespējams, ka atbilst. → nekādas darbības.
- 🟡 **DZELTENS**: iespējams pārkāpums. → uzraudzīt / vajadzības gadījumā nodrošināt brīdinājumu.
- 🟠 **ORANŽA**: iespējams pārkāpums. → moderācijas apskats.
- 🔴 **SARKANS**: iespējams smags pārkāpums. → tūlītējs aizsardzības pasākums + cilvēka apskate.

### 10. Nav "AI soda"
**AI nepiemēro galīgas sankcijas.** Tas var izraisīt tūlītējus tehniskus pasākumus (piemēram, īslaicīgi aizturēt ziņojumu) nopietnu drošības apsvērumu dēļ, taču galīgais lēmums joprojām ir pārbaudāms.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. AI jāspēj pamatot savus lēmumus
DSA pieprasa skaidrus un konkrētus iemeslus. AI nodrošina strukturētu pamatojumu: Noteikums (NG-CONDUCT-004), Atklāts (iespējami konkrēti draudi), Pārliecība (0,94), Attiecīgais konteksts (Iepriekšējie 4 ziņojumi), Ieteicamā darbība (Cilvēka pārskats).

### 13. AI nedrīkst slepeni mainīt saturu
**Moderācijas AI nekad nedrīkst nepamanīti mainīt sākotnējo saturu.** Automātiskās labošanas, tulkošanas vai kopsavilkuma laikā oriģināls vienmēr tiek saglabāts.

### 14. AI radīts saturs
Mēs izšķiram: cilvēka radītu, mākslīgā intelekta palīdzību, mākslīgā intelekta radītu un ar AI manipulētu. Tas kļūs par satura metadatu daļu.

### 15. AI satura un AI izcelsmes slāņa marķēšana
Saskaņā ar ES MI likuma (spēkā 2026. gada augustā) pārredzamības noteikumiem mākslīgā intelekta radītajam saturam ir jābūt identificējamam. Mēs nodrošinām AI izcelsmes slāni, kurā tiek glabāti metadati (AI izcelsme, modelis, laikspiedols, cilvēka pārskats).

### 16. Dziļa viltojumu noteikšana
Arhitektūras mērķis ir atklāt sintētiskos attēlus, klonētas balsis un dziļus viltojumus. Tomēr atklāšana nav automātisks pierādījums.

### 17. Nav automātiskas "patiesības mašīnas" (mērenība ≠ faktu pārbaude)
Viena sistēma pārbauda: "Vai saturs pārkāpj noteikumus?" (Satura regulēšana), cits sniedz: "Kāda informācija un avoti ir pieejami?" (Informācijas palīdzība). Viedokļi netiek vienkārši dzēsti tāpēc, ka tie ir "nepareizi".

### 18. Aizsardzība pret kultūras nepareizu interpretāciju
AI pieprasa **Kultūras konteksta modeļus**, lai novērstu, ka vienas valsts komunikācijas normas tiek uzskatītas par globālu standartu.

### 19. Ironija, satīra un humors
AI izmanto kontekstu, emocijzīmes, sarunu vēsturi un zināmas ironijas struktūras, taču tai ir jāpieļauj nenoteiktība, ja nozīmes ir neskaidras.

### 20. Bez soda, pamatojoties uz vienu AI rezultātu
Neviena nopietna regulēšanas iejaukšanās nedrīkst būt balstīta tikai uz vienu automatizētu klasifikācijas rezultātu (teksts + konteksts + uzvedība + valoda + mediji + noteikumu dzinējs = riska novērtējums).

### 21. Lietotāju uzvedības signāli un bez sociālo kredītu sistēmas
Tas attiecas uz tehniskas ļaunprātīgas izmantošanas signāliem (piemēram, masveida surogātpasta izlikšanu), nevis uz vispārēju sociālo vērtēšanas sistēmu. Nexus Gaja neuztur Sociālo kredītu sistēmu – mērenība kalpo drošībai, nevis cilvēka vērtības novērtējumam.

### 22. Mērenībai AI jābūt auditējamai
Lai nodrošinātu izsekojamību, tiek reģistrēti visi attiecīgie automatizētie lēmumi (notikuma ID, kārtula ID, pārliecība, cilvēka pārskats utt.).

### 23. Viltus pozitīvi, viltus negatīvi un kvalitātes rādītāji
Kļūdu veidi tiek uzraudzīti. Informācijas panelis mēra precizitāti, atsaukšanu un jo īpaši **apelācijas atsaukšanas biežumu** (veiksmīgo apelāciju skaitu).

### 24. Language Equity & Translation Bias
Regulēšanas kvalitātei ir jābūt salīdzināmai visās atbalstītajās valodās (Multilingual moderation etalons). Ja regulēšanas rezultāti atšķiras oriģinālā un tulkojumā (tulkošanas konflikts), tas ir īpaši jāpārskata.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Project Status
The project is currently in the active architecture and planning phase.
Ongoing architectural decisions are documented in the `/docs` folder.
