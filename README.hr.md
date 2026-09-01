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

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

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
Čisto pretraživanje ključnih riječi ne bi bilo dovoljno. "Mogla bih ga ubiti od smijeha" semantički sadrži nasilje, ali je figura govora. “Sutra u 20 sati pucat ću na njega ispred njegove kuće” sasvim je druga situacija. AI mora razumjeti što izjava znači u svom specifičnom kontekstu.

### 5. Višejezična moderacija
Umjerenost ne može jednostavno uspoređivati riječi. Mora analizirati semantičku razinu (npr. njemački idiomi naspram japanskih idioma naspram regionalnih izraza).

### 6. Izvorni jezik + prijevod
Izvornik i prijevod analiziraju se zasebno. Tek tada se provodi "Kombinirano ocjenjivanje moderiranja". To omogućuje Nexus Gaji da utvrdi je li sam prijevod možda eskalirao ili izmijenio činjenice.

### 7. Ocjena povjerenja
Svaka procjena umjetne inteligencije dobiva ocjenu pouzdanosti (npr. vjerojatnost prijetnje: 0,96). Međutim: **Ocjena povjerenja ≠ Istina.** Rezultat od 96% samo znači da je model vrlo siguran u svoju klasifikaciju, a ne nužno da je korisnik kriv.

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. Četiri zone odluke
- 🟢 **ZELENO**: Vrlo vjerojatno usklađeno. → nema akcije.
- 🟡 **ŽUTO**: Moguć prekršaj. → nadzirati / dati upozorenje ako je potrebno.
- 🟠 **NARANČASTA**: Vjerojatno kršenje. → moderacijski pregled.
- 🔴 **CRVENO**: Ozbiljan mogući prekršaj. → trenutna zaštitna mjera + ljudski pregled.

### 10. Nema "AI kazne"
**AI ne nameće konačne sankcije.** Može pokrenuti hitne tehničke mjere (npr. privremeno zadržavanje poruke) zbog ozbiljnih sigurnosnih problema, ali konačna odluka ostaje provjerljiva.

### 11. Zaštitne mjere mogu se dogoditi automatski
U slučaju konkretne prijetnje (otkrivena prijetnja → Visoka pouzdanost → Privremeno ograničenje → Ljudski pregled → Odluka), štitimo ugroženog korisnika bez pretvaranja umjetne inteligencije u suca.

### 12. AI mora biti u stanju opravdati svoje odluke
DSA zahtijeva jasne i specifične razloge. AI pruža strukturirano razmišljanje: pravilo (NG-CONDUCT-004), otkriveno (potencijalna konkretna prijetnja), povjerenje (0,94), relevantan kontekst (prethodne 4 poruke), preporučena radnja (ljudski pregled).

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

### 18. Zaštita od kulturnog pogrešnog tumačenja
AI zahtijeva **Modele kulturnog konteksta** kako bi se spriječilo da se komunikacijske norme jedne zemlje preuzmu kao globalni standard.

### 19. Ironija, satira i humor
AI koristi kontekst, emojije, povijest razgovora i poznate strukture ironije, ali mora dopustiti nesigurnost kada su značenja dvosmislena.

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

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

## Financing Principles and Revenue Model (WP 1.10.1)

Za Nexus Gaju primjenjuje se vrlo važan ekonomski princip: **Bez tradicionalnog oglašavanja unutar platforme.**
To bitno razlikuje Nexus Gaja od mnogih današnjih društvenih mreža. No, to ne znači da Nexus Gaja ne može imati komercijalni karakter. Naprotiv, platforma mora biti ekonomski održiva kako bi njena društvena svrha mogla trajati. Ekonomska aktivnost je sredstvo za postizanje cilja, a ne primarna svrha platforme.

### 1. Načelo NG-FIN-001
Nexus Gaja svoje poslovanje financira kroz transparentne tokove prihoda odvojene od interesa korisnika, a ne kroz monetizaciju pažnje ili osobnih podataka svojih korisnika.

### 2. Nema tradicionalnog oglašavanja
Posebno su zabranjeni:
- Banner oglasi
- Skočni oglasi
- Automatska reprodukcija video oglasa
- Sponzorirane objave u standardnom feedu
- Personalizirani profili za oglašavanje
- Prodaja korisničkih profila ili osobnih podataka
- Oglašavanje proizašlo iz privatnih razgovora.

Nexus Gaja ostaje **komunikacijski, a ne oglasni prostor**.

### 3. Financiranje bez oglašavanja (6 stupova)
Financiranje se temelji na šest stupova:
```tekst
                 NEXUS GAJA
                     │
       ┌──────────────┼───────────────┐
       ▼ ▼ ▼
   DONACIJE PREMIUM ORGANIZACIJE
       │ │ │
       ├──────────────┼──────────────┤
       ▼ ▼ ▼
    GRANOVI PARTNERSTVA USLUGE
```

#### Stup 1 – besplatno osnovno članstvo
**Nexus Gaja Free** omogućuje osnovno međunarodno razumijevanje za sve (profil, međunarodna komunikacija, postovi, zajednice, chatovi, osnovni prijevod) bez ikakvih troškova.

#### Stup 2 – Premium ponude
Dobrovoljne plaćene ponude (**Nexus Gaja Plus**) koje pružaju veća ograničenja pohrane, veću kvalitetu medija, proširene kvote umjetne inteligencije i organizacijske značajke.
**Važno (Freemium umjesto Dark Freemium):** Osnovna komunikacija nikada se ne smije umjetno degradirati.

#### Pillar 3 – Organizations
Special accounts for schools, universities, NGOs, businesses, and municipalities (**Nexus Gaja Organization**). Schools can be supported via institutional rates as multipliers of international understanding.

#### Stup 4 – Donacije
**Nexus Gaja Funding Pool** prihvaća opće i namjenske donacije (npr. "za međunarodnu komunikaciju mladih"). **Knjiga raspodjele sredstava** osigurava transparentnu raspodjelu sredstava.
**Namjenski fond i tombola:** Dio donacija hrani skup za besplatno/s popustom korištenje. Mehanizam lutrije/tombole može dodijeliti ta sredstva transparentno i revizijski.

#### Stup 5 – Institucionalno financiranje
Zaklade, programi financiranja kulture ili državni programi.
**NG-FIN-002:** Financijska potpora ne kupuje uređivačku ili tehničku kontrolu (Neovisnost).

#### Stup 6 – Komercijalne usluge
B2B usluge poput **Translation-as-a-Service** (API), organizacijska komunikacija ili međunarodne konferencijske sobe, bez opterećenja standardnog korisničkog feeda.

### 4. Nema monetizacije podataka i ekonomije nadzora
**NG-FIN-003:** Osobni podaci korisnika nisu roba. Nema prodaje popisa, profila ili povijesti. Nexus Gaja ne profitira od psihološkog nadzora (Surveillance Economy).

### 5. Financijska transparentnost i knjiga fondova
**Nexus Gaja Financijska transparentnost:** Objava agregiranih financijskih struktura. Namjenske donacije dobivaju tehničko knjigovodstvo (ID fonda → Svrha → Stanje → Raspodjela). Nema unakrsnog subvencioniranja društvenih namjena u korporativni marketing.

### 6. Model financiranja temeljen na solidarnosti
Cijene se temelje na troškovno usmjerenosti, pravednosti i solidarnosti.
**Solidarity Premium:** dobrovoljna opcija za Premium korisnike da financiraju dio pristupa drugog korisnika. Prisilna solidarnost ili društvo vrhunske klase (manje poštovanja/umjerenosti za besplatne korisnike) strogo je zabranjeno.

### 7. Ekonomski KPI umjesto ekonomije angažmana
Nema ovisnosti o održavanju korisnika "online što je duže moguće" (bez ragebaita, beskonačnih feedova).
Umjesto toga koristimo mjerne podatke kao što su:
- **Globalni komunikacijski indeks (GCI):** Uspješni komunikacijski odnosi između ljudi iz različitih jezičnih/kulturnih regija.
- **Omjer održivosti platforme (PSR):** Ponavljajući prihod / ponavljajući operativni troškovi (Cilj ≥ 1).

### 8. Ono što izričito ne želimo (negativna lista)
Nexus Gaja **ne** financira:
❌ Prodaja osobnih podataka
❌ Personalizirano tradicionalno oglašavanje
❌ Praćenje ponašanja korisnika u svrhu oglašavanja
❌ Prodaja osobnih komunikacijskih podataka
❌ Skrivena upotreba AI podataka
❌ Manipulativni Premium sustavi plaćanja
❌ Umjetno ograničenje dosega za unovčavanje
❌ Plaćeni politički utjecaj
❌ Kupnja privilegiranih moderacijskih odluka.

### 9. Preliminarna financijska arhitektura
```tekst
                         NEXUS GAJA
                              │
             ┌─────────────────┼──────────────────┐
             │ │ │
             ▼ ▼ ▼
          ORGANIZACIJE KORISNIKA PODUZEĆE
             │ │ │
             └─────────────────┼──────────────────┘
                              │
                       USLUGE PLATFORME
                              │
          ┌────────────────────┼──────────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS
                              │
                    ┌──────────┴──────────┐
                    ▼ ▼
               OPĆI FOND OGRANIČENI FONDOVI
                                        │
                                        ▼
                                  DRUŠTVENA NAMJENA
```

### Sažetak načela financiranja (NG-FIN)
- **NG-FIN-001:** Nema financiranja putem tradicionalnog oglašavanja.
- **NG-FIN-002:** Nema uredničke/tehničke kontrole kroz financijsku potporu.
- **NG-FIN-003:** Osobni podaci nisu roba.
- **NG-FIN-004:** Osnovna komunikacija ostaje dostupna bez plaćanja.
- **NG-FIN-005:** Premium ponude ne smiju degradirati besplatne korisnike.
- **NG-FIN-006:** Namjenskim sredstvima upravlja se prema namjeni.
- **NG-FIN-007:** Transparentno upravljanje donacijama i potporama.
- **NG-FIN-008:** Komercijalne B2B usluge ne ugrožavaju neovisnost.
- **NG-FIN-009:** Usredotočite se na održivost, a ne na maksimalno unovčavanje.
- **NG-FIN-010:** Objekt trajno osigurava društvenu namjenu.

## API, sučelja i komunikacijska arhitektura (WP 1.11.3)

Kako bi se osigurala stabilnost, sigurnost i skalabilnost sustava, Nexus Gaja slijedi striktno API-prvu i arhitekturu vođenu događajima.

### Core Principles
- **No Direct Database Access:** Components communicate exclusively via defined interfaces (APIs or Events), never through direct database queries of other services.
- **API Gateway:** All external client requests route through an API Gateway handling authentication, routing, and rate limiting.
- **Provider Abstraction:** External services (AI models, payment providers, translation engines) are integrated via abstraction layers, avoiding hardcoded dependencies and enabling flexible provider swapping.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Sigurnost i pouzdanost
- **Zero-Trust Model:** interni mrežni promet se ne smatra automatski pouzdanim; osjetljiva komunikacija usluga-usluga zahtijeva autentifikaciju.
- **Idempotencija & Outbox Pattern:** Kritične operacije (kao što su donacije ili slanje poruka) dizajnirane su da budu idempotentne kako bi se spriječila duplicirana obrada, koristeći Outbox uzorak kako bi se osiguralo da se događaji nikada ne izgube čak ni tijekom transakcija baze podataka.

## MVP model domene (WP 1.12)

Nexus Gaja koristi striktno domenski upravljanu MVP arhitekturu (ADR-025), dizajniranu kao modularni monolit s jasnim granicama domene. Ova struktura sprječava preuranjenu složenost mikroservisa, a istovremeno zadržava fleksibilnost za kasnije odvajanje određenih domena.

### Entiteti osnovne domene
Arhitektura eksplicitno odvaja različite koncepte kako bi se osigurao integritet podataka i izbjegle strukturne zamke poput "Korisničko ime = Čovjek":
- **Identitet i računi:** `Osoba` ≠ `Korisnički račun` ≠ `Provjera identiteta`. Verificirana osoba sudjeluje putem računa, ali entiteti ostaju odvojeni.
- **Komunikacija:** `Poruka` ≠ `Prijevod`. Izvorna poruka ostaje nepromjenjiva; prijevodi su povezani entiteti.
- **Moderacija:** `Izvješće` ≠ `Odluka o moderaciji`. Izvješće je samo zahtjev; a moderation case provodi istragu.
- **Financije:** `Donacija` ≠ `Stanje sredstava`. Uplate se knjiže putem nepromjenjive knjige u fond, čime se osigurava financijska transparentnost.

### Međusobno povezane domene
Sustav je podijeljen u jasne logičke domene (ograničene kontekste): identitet, račun, organizacija, komunikacija, zajednica, jezik, moderacija, obavijesti, financije i upravljanje. Ove domene mapiraju cijelo putovanje od entiteta u stvarnom svijetu (korisnici, škole, nevladine organizacije) do njihovih digitalnih interakcija i povezanog upravljanja.

## Status projekta
Projekt je trenutno u fazi aktivne arhitekture i planiranja.
Tekuće arhitektonske odluke dokumentirane su u mapi `/docs`.