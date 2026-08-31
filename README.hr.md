# Nexus Gaja

![Logotip Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** je inteligentna komunikacijska mreža osjetljiva na kontekst dizajnirana za revoluciju globalne komunikacije.

## Svrha i vizija
U globaliziranom svijetu jezik je često najveća prepreka. Glavni cilj Nexus Gaja je omogućiti besprijekornu, besprijekornu i kontekstualno točnu komunikaciju među ljudima—bez obzira na to govore li zajedničkim jezikom.

Ne radi se samo o krutom prevođenju riječi, već o **prijenosu značenja**. Nexus Gaja povezuje ljude na dubljoj razini razumijevanjem kulturnih, regionalnih i kontekstualnih nijansi, čime omogućuje istinske, autentične razgovore.

## Mogućnosti i značajke
- **Multimedijska komunikacija**: Sustav ne obrađuje samo tekst, već i sliku, zvuk i video. To omogućuje potpuno imerzivne razgovore (npr. videopozive ili glasovne poruke) u stvarnom vremenu bez obzira na jezične barijere.
- **Osjetljivost na kontekst**: prepoznavanje ironije, idioma, žargona i regionalnih dijalekata koje konvencionalni prevoditelji često pogrešno razumiju.
- **Mreža na više platformi**: služi kao temelj za privatne razgovore, teme foruma (postovi s komentarima) i interakcije globalne zajednice.

---

## Tehnička arhitektura (temeljni koncept)

Tehnička jezgra Nexus Gaja je komunikacijski model izrađen po narudžbi koji je strogo podijeljen u tri sloja:

1. **Original**: Komunikacijski objekt (poruka) koji je stvorio pošiljatelj uvijek ostaje nepromjenjiv.
2. **Semantička interpretacija**: Sustav ne analizira samo riječi, već i stvarno značenje.
3. **Prikaz ciljanog jezika**: AI samo stvara privremeni ili predmemorirani prikaz izvornika za dotičnog primatelja na temelju njihovog željenog jezika. Prijevodi nikada ne prebrišu izvornu poruku.

### Ovisnost o kontekstu
Prijevodi u Nexus Gaji nikada ne gledaju izolirane poruke. Motor uzima u obzir cijelu hijerarhiju:
`Poruka` → `Prethodne poruke` → `Kontekst teme` → `Kontekst zajednice` → `Jezik/regija` → `Korisničke postavke`

### Učinkovitost putem prijevoda na zahtjev
Prijevod se vrši uz učinkovitu potrošnju resursa samo **na zahtjev** (On-Demand). Kada korisnik zatraži sadržaj, on se prevodi na njegov unaprijed postavljeni jezik. Nakon što se generira prijevod za određeni jezik, on se trajno pohranjuje (sprema u predmemoriju) kako bi se drastično ubrzali budući zahtjevi.

## Moderacija potpomognuta umjetnom inteligencijom (WP 1.8.4)

S moderiranjem potpomognutim umjetnom inteligencijom poduzimamo značajan korak od ideje proizvoda do tehničke arhitekture, uzimajući u obzir trenutne propise EU (zahtjeve transparentnosti EU AI Acta prema čl. 50; Zakon o digitalnim uslugama s razumljivim obrazloženjima i mogućnostima žalbe).

### 1. Osnovno načelo
Najvažnija rečenica za arhitekturu je: **Umjerena umjetna inteligencija je sustav za pregled, a ne autonomni upravljački sustav.**
Osmišljen je da umjereno pomaže ljudima, a ne da sam određuje koja mišljenja smiju postojati na Nexus Gaji.
Razlikujemo tri razine:
- **Otkrivanje:** "Ovdje bi moglo doći do kršenja pravila."
- **Procjena:** "Vjerojatnost kršenja pravila je, na primjer, 94%."
- **Odluka:** "Koja je radnja zapravo poduzeta?"
Treću razinu u teškim slučajevima mora kontrolirati čovjek.

### 2. AI za moderiranje kao podsustav
Umjesto jedne umjetne inteligencije, uspostavljen je robustan podsustav:
```tekst
                 NEXUS GAJA AI UMJERENOST
                          │
       ┌───────────────────┼────────────────────┐
       │ │ │
  Jezik AI Sigurnost AI Prijevara AI
       │ │ │
       ├───────────────┬───┴───────────────┬───┤
       │ │ │
 Identitet ponašanja pri prevođenju
 Analiza Analiza signala
       │ │ │
       └───────────────┼────────────────────┘
                      ▼
               Procjena rizika
                      │
                      ▼
               Ljudski pregled
```

### 3. Najvažniji AI moduli
Nexus Gaja koristi devet specijaliziranih područja analize:
- **M1 – Razumijevanje jezika**: otkriva jezik, dijalekt, sleng, indikatore ironije, probleme s prijevodom.
- **M2 – Otkrivanje toksičnosti/zlouporabe**: otkriva uvrede, osobne napade, uznemiravanje.
- **M3 – Otkrivanje prijetnji**: Otkriva potencijalne prijetnje, ucjene, najave nasilja.
- **M4 – Detekcija mržnje/dehumanizacije**: otkriva ciljane napade na ljude na temelju određene pripadnosti.
- **M5 – Otkrivanje neželjene pošte/manipulacije**: otkriva neželjenu poštu, ponašanje robota, koordiniranu manipulaciju.
- **M6 – otkrivanje prijevara**: otkriva sumnjive pokušaje prijevare, krađu identiteta, društveni inženjering.
- **M7 – Integritet identiteta**: Provjerava signale u vezi s preuzimanjem računa, višestrukim računima, izbjegavanjem zabrane.
- **M8 – Media Safety**: Analizira slike, audio, video, dokumente.
- **M9 – Context Engine**: Najvažniji modul. Spaja pojedinačne nalaze.

### 4. Zašto je Context Engine ključan
Čisto pretraživanje ključnih riječi ne bi bilo dovoljno. "Mogao bih ga ubiti od smijeha" semantički sadrži nasilje, ali je riječna figura. “Sutra u 20 sati pucat ću na njega ispred njegove kuće” sasvim je druga situacija. AI mora razumjeti što izjava znači u svom specifičnom kontekstu.

### 5. Višejezična moderacija
Umjerenost ne može jednostavno uspoređivati riječi. Mora analizirati semantičku razinu (npr. njemački idiomi naspram japanskih idioma naspram regionalnih izraza).

### 6. Izvorni jezik + prijevod
Izvornik i prijevod analiziraju se zasebno. Tek tada se provodi "Kombinirano ocjenjivanje moderiranja". To omogućuje Nexus Gaji da utvrdi je li sam prijevod možda eskalirao ili izmijenio činjenice.

### 7. Ocjena povjerenja
Svaka procjena umjetne inteligencije dobiva ocjenu pouzdanosti (npr. vjerojatnost prijetnje: 0,96). Međutim: **Ocjena povjerenja ≠ Istina.** Rezultat od 96% samo znači da je model vrlo siguran u svoju klasifikaciju, a ne nužno da je korisnik kriv.

### 8. Nesigurnost sama postaje signal
Ako je umjetna inteligencija nesigurna (npr. Prijetnja: 0,62, Satira: 0,54), ne smije jednostavno provoditi stroga pravila. Umjesto toga, neizvjesnost je ugrađena izravno u arhitekturu: **Potreban je ljudski pregled**.

### 9. Četiri zone odluke
- 🟢 **ZELENO**: Vrlo vjerojatno usklađeno. → nema akcije.
- 🟡 **ŽUTO**: Moguć prekršaj. → nadzirati / dati upozorenje ako je potrebno.
- 🟠 **NARANČASTA**: Vjerojatno kršenje. → moderacijski pregled.
- 🔴 **CRVENO**: Ozbiljan mogući prekršaj. → trenutna zaštitna mjera + ljudski pregled.

### 10. Nema "AI kazne"
**AI ne nameće konačne sankcije.** Može pokrenuti hitne tehničke mjere (npr. privremeno zadržavanje poruke) zbog ozbiljnih sigurnosnih problema, ali konačna odluka ostaje provjerljiva.

### 11. Zaštitne mjere mogu se dogoditi automatski
U slučaju konkretne prijetnje (otkrivena prijetnja → Visoka pouzdanost → Privremeno ograničenje → Ljudski pregled → Odluka), štitimo ugroženog korisnika bez pretvaranja umjetne inteligencije u suca.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI ne smije tajno mijenjati sadržaj
**Moderacija AI nikada ne smije neprimjetno mijenjati izvorni sadržaj.** Tijekom automatskog ispravljanja, prijevoda ili sažimanja, izvornik se uvijek čuva.

### 14. Sadržaj generiran umjetnom inteligencijom
Razlikujemo: stvorene od strane ljudi, potpomognute umjetnom inteligencijom, generirane umjetnom inteligencijom i manipulirane umjetnom inteligencijom. To će postati dio metapodataka sadržaja.

### 15. Označavanje AI sadržaja i sloj AI porijekla
U skladu s pravilima o transparentnosti Zakona o umjetnoj inteligenciji EU (na snazi od kolovoza 2026.), sadržaj generiran umjetnom inteligencijom mora biti prepoznatljiv. Nudimo AI Provenance Layer koji pohranjuje metapodatke (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake detekcija
Arhitektura ima za cilj otkriti sintetičke slike, klonirane glasove i deepfake. Međutim, otkrivanje nije automatski dokaz.

### 17. Nema automatskog "stroja za istinu" (Moderacija ≠ Provjera činjenica)
Jedan sustav provjerava: "Krši li sadržaj pravila?" (Moderiranje sadržaja), drugi daje: "Koje informacije i izvori su dostupni?" (Informacijska pomoć). Mišljenja se ne brišu samo zato što su "pogrešna".

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Ironija, satira i humor
AI koristi kontekst, emojije, povijest razgovora i poznate strukture ironije, ali mora dopustiti nesigurnost kada su značenja dvosmislena.

### 20. Nema kazne na temelju jednog AI rezultata
Nikakva ozbiljna intervencija moderiranja ne smije se temeljiti samo na jednom rezultatu automatizirane klasifikacije (Tekst + Kontekst + Ponašanje + Jezik + Mediji + Mehanizam pravila = Procjena rizika).

### 21. Signali ponašanja korisnika & Nema sustava društvenog kreditiranja
Ovo se odnosi na signale tehničke zlouporabe (npr. masovno slanje neželjene pošte), a ne na opći sustav društvenog ocjenjivanja. Nexus Gaja ne održava sustav društvenog kreditiranja – umjerenost služi sigurnosti, a ne procjeni vrijednosti osobe.

### 22. Umjerenost AI mora biti provjerljiva
Sve relevantne automatizirane odluke se bilježe (ID događaja, ID pravila, Povjerljivost, ljudski pregled, itd.) kako bi se osigurala sljedivost.

### 23. Lažno pozitivni, lažno negativni i metrike kvalitete
Prate se vrste grešaka. Nadzorna ploča mjeri preciznost, opoziv, a posebno **Stopu poništenja žalbe** (broj uspješnih žalbi).

### 24. Jezična jednakost i pristranost prijevoda
Kvaliteta moderiranja mora biti usporediva na svim podržanim jezicima (Multilingual Moderation Benchmark). Ako se rezultati moderiranja razlikuju između izvornika i prijevoda (sukob prijevoda), to se mora posebno pregledati.

### 25. Motor za prijedloge i politiku arhitekture
Pravila (Policy Engine) nisu tvrdo kodirana u AI modele. AI daje nalaze; Policy Engine odlučuje na temelju trenutnih pravila. To omogućuje **promjene modela bez promjena pravila**.

### 26. Čovjek ostaje konačni autoritet
- **NG-AI-MOD-001**: AI pomaže u otkrivanju i klasifikaciji, ali ne zamjenjuje ljudski pregled u teškim odlukama.
- **NG-AI-MOD-002**: Odluke o automatskom moderiranju moraju se moći pratiti, bilježiti i provjeriti.

**Sažetak**: Gradimo sustav od četiri faze: otkrivanje umjetne inteligencije, analiza konteksta i rizika, mehanizam za politiku i ljudsko upravljanje. To omogućuje snažnu automatizaciju bez stvaranja opasne arhitekture "AI kao suca".

## Status projekta
Projekt je trenutno u fazi aktivne arhitekture i planiranja.
Tekuće arhitektonske odluke dokumentirane su u mapi `/docs`.