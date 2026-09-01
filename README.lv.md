# Nexus Gaja

![Nexus Gaja logotips](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** ir vieds, kontekstjutīgs saziņas tīkls, kas izstrādāts, lai mainītu globālo saziņu.

## Mērķis un vīzija

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

Globalizētajā pasaulē valoda bieži vien ir lielākā barjera. Nexus Gaja galvenais mērķis ir nodrošināt netraucētu, bezšķēršļu un kontekstuāli precīzu saziņu starp cilvēkiem neatkarīgi no tā, vai viņi runā kopīgā valodā.

Runa nav tikai par stingru vārdu tulkošanu, bet par **nozīmes pārnešanu**. Nexus Gaja saista cilvēkus dziļākā līmenī, izprotot kultūras, reģionālās un kontekstuālās nianses, tādējādi nodrošinot patiesas, autentiskas sarunas.

## Iespējas un funkcijas
- **Multivides sakari**: sistēma apstrādā ne tikai tekstu, bet arī attēlu, audio un video. Tas ļauj reāllaikā veidot visaptverošas sarunas (piemēram, videozvanus vai balss ziņas) pāri valodas barjerām.
- **Kontekstu jutīgums**: ironijas, idiomu, žargona un reģionālo dialektu atpazīšana, ko parastie tulki bieži pārprot.
- **Starpplatformu tīkls**: kalpo kā pamats privātām tērzēšanas sarunām, foruma pavedieniem (ziņas ar komentāriem) un globālās kopienas mijiedarbībām.

---

## Tehniskā arhitektūra (pamatkoncepcija)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

Nexus Gaja tehniskais kodols ir īpaši izveidots sakaru modelis, kas ir stingri sadalīts trīs slāņos:

1. **Oriģināls**: sūtītāja izveidotais komunikācijas objekts (ziņojums) vienmēr paliek nemainīgs.
2. **Semantiskā interpretācija**: sistēma analizē ne tikai vārdus, bet arī faktisko nozīmi.
3. **Mērķa valodas attēlojums**: AI tikai izveido oriģināla pagaidu vai kešatmiņas attēlojumu attiecīgajam adresātam, pamatojoties uz viņa vēlamo valodu. Tulkojumi nekad nepārraksta sākotnējo ziņojumu.

### Konteksta atkarība
Tulkojumos Nexus Gaja ziņojumi nekad netiek skatīti atsevišķi. Dzinējs ņem vērā visu hierarhiju:
"Ziņojums" → "Iepriekšējie ziņojumi" → "Pavediena konteksts" → "Kopienas konteksts" → "Valoda/reģions" → "Lietotāja preferences"

### Efektivitāte, izmantojot tulkošanu pēc pieprasījuma
Tulkošana notiek resursu ziņā efektīvi tikai **pēc pieprasījuma** (pēc pieprasījuma). Kad lietotājs pieprasa saturu, tas tiek tulkots viņa iepriekš iestatītajā valodā. Kad tulkojums noteiktai valodai ir ģenerēts, tas tiek pastāvīgi saglabāts (kešatmiņā), lai ievērojami paātrinātu turpmākos pieprasījumus.

## AI atbalstīta regulēšana (WP 1.8.4)

![Nexus Gaja AI moderācija](assets/img/nexus_moderation.jpg)

Izmantojot AI atbalstītu moderāciju, mēs speram nozīmīgu soli no produkta idejas līdz tehniskajai arhitektūrai, ņemot vērā pašreizējos ES noteikumus (ES AI likuma pārredzamības prasības saskaņā ar 50. pantu; Digitālo pakalpojumu likums ar saprotamiem pamatojumiem un apelācijas iespējām).

### 1. Pamatprincips
Vissvarīgākais teikums arhitektūrai ir: **Moderācijas AI ir pārskatīšanas sistēma, nevis autonoma regulēšanas sistēma.**
Tas ir izstrādāts, lai palīdzētu cilvēkiem ar mēru, nevis lai pati noteiktu, kādi viedokļi ir atļauti Nexus Gaja.
Mēs izšķiram trīs līmeņus:
- **Atklāšana:** "Šeit varētu būt noteikumu pārkāpums."
- **Novērtējums:** "Noteikumu pārkāpuma varbūtība ir, piemēram, 94%.
- **Lēmums:** "Kāda darbība faktiski tiek veikta?"
Trešais līmenis smagos gadījumos ir jākontrolē cilvēkam.

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

### 11. Aizsardzības pasākumi var notikt automātiski
Konkrētu draudu gadījumā (Draudi atklāti → Augsta uzticamība → Pagaidu ierobežojums → Cilvēka pārbaude → Lēmums), mēs aizsargājam apdraudēto lietotāju, nepārvēršot AI par tiesnesi.

### 12. AI jāspēj pamatot savus lēmumus
DSA pieprasa skaidrus un konkrētus iemeslus. AI nodrošina strukturētu pamatojumu: Noteikums (NG-CONDUCT-004), Atklāts (iespējami konkrēti draudi), Pārliecība (0,94), Attiecīgais konteksts (Iepriekšējie 4 ziņojumi), Ieteicamā darbība (Cilvēka pārskats).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

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

### 25. Arhitektūras priekšlikums un politikas dzinējs
Noteikumi (politikas programma) AI modeļos nav iekodēti. AI nodrošina konstatējumus; politikas programma pieņem lēmumu, pamatojoties uz pašreizējiem noteikumiem. Tas ļauj veikt **modeļa izmaiņas bez noteikumu izmaiņām**.

### 26. Cilvēks paliek galīgā autoritāte
- **NG-AI-MOD-001**: mākslīgais intelekts palīdz noteikt un klasificēt, bet neaizstāj cilvēka veikto pārbaudi smagu lēmumu pieņemšanā.
- **NG-AI-MOD-002**: automatizētajiem regulēšanas lēmumiem ir jābūt izsekojamiem, reģistrējamiem un pārbaudāmiem.

**Kopsavilkums**: mēs veidojam četru posmu sistēmu: AI noteikšana, konteksta un riska analīze, politikas dzinējs un cilvēku pārvaldība. Tas nodrošina spēcīgu automatizāciju, neradot bīstamu "AI kā tiesneša" arhitektūru.

## Finansēšanas principi un ieņēmumu modelis (WP 1.10.1)

![Nexus Gaja finanšu modelis](assets/img/nexus_finance.jpg)

Uz Nexus Gaja attiecas ļoti svarīgs ekonomisks princips: **Platformā nav tradicionālu reklāmu.**
Tas būtiski atšķir Nexus Gaja no daudziem mūsdienu sociālajiem tīkliem. Tomēr tas nenozīmē, ka Nexus Gaja nevar būt komerciāls raksturs. Gluži pretēji, platformai ir jābūt ekonomiski dzīvotspējīgai, lai tās sociālais mērķis varētu pastāvēt. Ekonomiskā darbība ir līdzeklis mērķa sasniegšanai, nevis platformas galvenais mērķis.

### 1. Princips NG-FIN-001
Nexus Gaja finansē savu darbību, izmantojot caurspīdīgas ieņēmumu plūsmas, kas ir nošķirtas no lietotāju interesēm, nevis monetizē lietotāju uzmanību vai personas datus.

### 2. Nav tradicionālās reklāmas
Īpaši aizliegti ir:
- Reklāmkarogu reklāmas
- Uznirstošās reklāmas
- Automātiski atskaņotas videoreklāmas
- Sponsorētās ziņas standarta plūsmā
- Personalizēti reklāmas profili
- Lietotāju profilu vai personas datu pārdošana
- Reklāma, kas iegūta no privātām sarunām.

Nexus Gaja remains a **communication space rather than an advertising space**.

### 3. Finansējums bez reklāmas (6 pīlāri)
Finansējums balstās uz sešiem pīlāriem:
``` teksts
                 NEXUS GAJA
                     │
       ┌─────────────┼──────────────
       ▼ ▼ ▼
   PREMIUM ORGANIZĀCIJAS ZIEDOUMI
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    SNIEDZ PARTNERĪBAS PAKALPOJUMUS
```

#### 1. pīlārs — bezmaksas pamata dalība
**Nexus Gaja Free** nodrošina pamata starptautisko izpratni ikvienam (profils, starptautiskā saziņa, ziņas, kopienas, tērzēšana, pamata tulkošana) bez maksas.

#### 2. pīlārs — Premium piedāvājumi
Brīvprātīgi maksas piedāvājumi (**Nexus Gaja Plus**), kas nodrošina lielākus krātuves ierobežojumus, augstāku multivides kvalitāti, paplašinātas AI kvotas un organizatoriskas funkcijas.
**Svarīgi (Freemium, nevis Dark Freemium):** pamata saziņu nekad nedrīkst mākslīgi pasliktināt.

#### Pillar 3 – Organizations
Special accounts for schools, universities, NGOs, businesses, and municipalities (**Nexus Gaja Organization**). Schools can be supported via institutional rates as multipliers of international understanding.

#### 4. pīlārs – ziedojumi
**Nexus Gaja finansējuma fonds** pieņem vispārīgus un mērķtiecīgus ziedojumus (piemēram, “starptautiskai jaunatnes komunikācijai”). **Līdzekļu piešķiršanas virsgrāmata** nodrošina pārskatāmu līdzekļu piešķiršanu.
**Mērķa fonds un tombola:** daļa no ziedojumiem tiek nodrošināta bezmaksas/atlaides izmantošanai. Loterijas/tombola mehānisms var piešķirt šos līdzekļus pārredzami un auditējami.

#### 5. pīlārs – iestāžu finansējums
Fondi, kultūras finansēšanas programmas vai valsts programmas.
**NG-FIN-002:** Finansiālais atbalsts nenodrošina redakcionālo vai tehnisko kontroli (neatkarība).

#### 6. pīlārs — komerciālie pakalpojumi
B2B pakalpojumi, piemēram, **Translation-as-a-Service** (API), organizācijas komunikācija vai starptautiskas konferenču telpas, neapgrūtinot standarta lietotāju plūsmu.

### 4. Bez datu monetizācijas un uzraudzības ekonomikas
**NG-FIN-003:** Personas lietotāja dati nav prece. Netiek pārdoti saraksti, profili vai vēstures. Nexus Gaja negūst peļņu no psiholoģiskās uzraudzības (novērošanas ekonomika).

### 5. Finanšu pārredzamība un fondu virsgrāmata
**Nexus Gaja finanšu pārredzamība:** apkopoto finanšu struktūru publicēšana. Mērķziedojumi saņem tehnisko uzskaiti (Fonda ID → Mērķis → Atlikums → Piešķīrums). Nekādas sociālo mērķu šķērssubsidēšanas korporatīvajā mārketingā.

### 6. Uz solidaritāti balstīts finansēšanas modelis
Cenu noteikšanas pamatā ir orientācija uz izmaksām, godīgums un solidaritāte.
**Solidaritātes Premium:** brīvprātīga iespēja Premium lietotājiem finansēt daļu no cita lietotāja piekļuves. Piespiedu solidaritāte vai augstākās klases sabiedrība (mazāka cieņa/mērenība pret bezmaksas lietotājiem) ir stingri aizliegta.

### 7. Economic KPIs Instead of Engagement Economy
No dependence on keeping users "online as long as possible" (no ragebait, infinite feeds).
Instead, we use metrics like:
- **Global Communication Index (GCI):** Successful communication relationships between people from different linguistic/cultural regions.
- **Platform Sustainability Ratio (PSR):** Recurring revenue / recurring operating costs (Target ≥ 1).

### 8. Ko mēs nepārprotami nevēlamies (negatīvais saraksts)
Nexus Gaja **nav** finansē:
❌ Personas datu pārdošana
❌ Personalizēta tradicionālā reklāma
❌ Lietotāju uzvedības uzraudzība reklāmas nolūkos
❌ Privāto sakaru datu pārdošana
❌ Slēpts AI datu lietojums
❌ Manipulatīvas Premium maksas sienas
❌ Mākslīgais sasniedzamības ierobežojums monetizācijai
❌ Apmaksāta politiskā ietekme
❌ Priviliģētu moderācijas lēmumu iegāde.

### 9. Sākotnējā finanšu arhitektūra
``` teksts
                         NEXUS GAJA
                              │
             ┌────────────────┼───────────────
             │ │ │
             ▼ ▼ ▼
          LIETOTĀJU ORGANIZĀCIJAS UZŅĒMUMS
             │ │ │
             └────────────────┼──────────────────
                              │
                       PLATFORMAS PAKALPOJUMI
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       PREMIUM DONATIONS API
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               VISPĀRĒJAIS FONDS IEROBEŽOTS FONDS
                                        │
                                        ▼
                                  SOCIĀLAIS MĒRĶIS
```

### Finansēšanas principu kopsavilkums (NG-FIN)
- **NG-FIN-001:** Nav finansējuma, izmantojot tradicionālo reklamēšanu.
- **NG-FIN-002:** Nav redakcionālas/tehniskas kontroles ar finansiālu atbalstu.
- **NG-FIN-003:** Personas dati nav prece.
- **NG-FIN-004:** Pamata saziņa joprojām ir pieejama bez maksas.
- **NG-FIN-005:** Premium piedāvājumi nedrīkst pazemināt bezmaksas lietotāju statusu.
- **NG-FIN-006:** Mērķtiecīgie līdzekļi tiek pārvaldīti atbilstoši to mērķim.
- **NG-FIN-007:** Ziedojumu un dotāciju pārredzama pārvaldība.
- **NG-FIN-008:** Komerciālie B2B pakalpojumi neapdraud neatkarību.
- **NG-FIN-009:** Koncentrējieties uz ilgtspējību, nevis uz maksimālu monetizāciju.
- **NG-FIN-010:** Struktūra pastāvīgi nodrošina sociālo mērķi.

## API, saskarnes un komunikācijas arhitektūra (WP 1.11.3)

Lai nodrošinātu sistēmas stabilitāti, drošību un mērogojamību, Nexus Gaja stingri ievēro API pirmā un uz notikumu balstītu arhitektūru.

### Pamatprincipi
- **Nav tiešas piekļuves datu bāzei:** komponenti sazinās tikai, izmantojot noteiktas saskarnes (API vai notikumus), nekad neizmantojot tiešus citu pakalpojumu datu bāzes vaicājumus.
- **API vārteja:** visi ārējo klientu pieprasījumi tiek maršrutēti caur API vārteju, kas apstrādā autentifikāciju, maršrutēšanu un ātruma ierobežošanu.
- **Pakalpojumu sniedzēja abstrakcija:** ārējie pakalpojumi (AI modeļi, maksājumu nodrošinātāji, tulkošanas programmas) ir integrēti, izmantojot abstrakcijas slāņus, izvairoties no cietā kodētām atkarībām un ļaujot elastīgi apmainīties ar pakalpojumu sniedzējiem.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Drošība un uzticamība
- **Zero-Trust Model:** iekšējā tīkla trafika netiek automātiski uzticama; sensitīvai pakalpojumu savstarpējai saziņai nepieciešama autentifikācija.
- **Idempotency & Outbox Pattern:** kritiskās darbības (piemēram, ziedojumi vai ziņojumapmaiņa) ir izstrādātas tā, lai tās būtu idempotiskas, lai novērstu dublikātu apstrādi, izmantojot izsūtnes modeli, lai nodrošinātu, ka notikumi nekad netiek zaudēti pat datu bāzes transakciju laikā.

## MVP domēna modelis (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja izmanto stingri uz domēnu balstītu MVP arhitektūru (ADR-025), kas veidota kā modulārs monolīts ar skaidrām domēna robežām. Šī struktūra novērš priekšlaicīgu mikropakalpojumu sarežģītību, vienlaikus saglabājot elastību, lai vēlāk sadalītu konkrētus domēnus.

### Galvenās domēna entītijas
Arhitektūra skaidri nodala atšķirīgus jēdzienus, lai nodrošinātu datu integritāti un izvairītos no strukturālām kļūmēm, piemēram, "Lietotājvārds = cilvēks":
- **Identitāte un konti:** "Persona" ≠ "Lietotāja konts" ≠ "Identitātes verifikācija". Verificēta persona piedalās, izmantojot kontu, taču entītijas paliek atsevišķas.
- **Saziņa:** "Ziņojums" ≠ "Tulkojums". Sākotnējais vēstījums paliek nemainīgs; tulkojumi ir saistītas entītijas.
- **Moderācija:** "Ziņojums" ≠ "Moderācijas lēmums". Ziņojums ir tikai prasība; moderācijas lieta veic izmeklēšanu.
- **Finanses:** "Ziedojums" ≠ "Līdzekļu atlikums". Maksājumi tiek iegrāmatoti, izmantojot nemainīgu virsgrāmatu fondā, nodrošinot finanšu caurskatāmību.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Projekta statuss
Šobrīd projekts atrodas aktīvā arhitektūras un plānošanas fāzē.
Pašreizējie arhitektūras lēmumi tiek dokumentēti mapē /docs.

---

---

## Licence un intelektuālais īpašums

> **© 2024–2026 Jan Sonner / SonnerStudio — visas tiesības aizsargātas.**

**Nexus Gaja** ir ekskluzīvais **Jan Sonner** intelektuālais īpašums, kas darbojas **SonnerStudio** ietvaros.

Jans Sonners ir vienīgais Nexus Gaja radītājs, arhitekts un īpašnieks, tostarp visas koncepcijas, arhitektūra, domēna modeļi, zīmola identitāte un saistītā dokumentācija.

**Nekādas tiesības, licences vai īpašumtiesības nepieder nevienai trešajai pusei** neatkarīgi no to lieluma, tirgus stāvokļa vai ietekmes tehnoloģiju nozarē.

### Kas NAV atļauts bez nepārprotamas rakstiskas piekrišanas:
- šīs programmatūras vai tās dokumentācijas kopēšana, reproducēšana vai izplatīšana
- Pārveidot, adaptējot vai veidojot atvasinātus darbus
- Jebkuras Nexus Gaja daļas komerciāla izmantošana
- Izmantojot šīs krātuves saturu kā apmācību datus AI vai LLM sistēmām
- jebkādu tiesību apakšlicencēšana vai nodošana trešajām personām

### Aizsargāts intelektuālais īpašums
Šādi oriģinālie jēdzieni tiek aizsargāti kā Jana Sonnera komercnoslēpumi un patentēti darbi:
- Slāņu komunikācijas modelis (oriģināls, semantiskā interpretācija, tulkotā izvade)
- Identitātes atdalīšanas princips (persona nav konts, nav identitātes pārbaude)
- Ziņojuma-tulkošanas atsaistes modelis (Ziņojums nav tulkojums)
- AI mērenības pārvaldības sistēma

### Sazinieties
Licencēšanas jautājumiem: https://github.com/SonnerStudio

Nexus Gaja un Nexus Gaja logotips ir Jana Sonnera preču zīmes. Nosaukuma vai zīmola neatļauta izmantošana ir aizliegta.

Pilnus licences noteikumus skatiet LICENCES failā.
