# Nexus Gaja

![Logotip Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** je inteligentno, na kontekst občutljivo komunikacijsko omrežje, zasnovano za revolucijo globalne komunikacije.

## Namen in vizija
V globaliziranem svetu je jezik pogosto največja ovira. Glavni cilj Nexus Gaja je omogočiti brezhibno, brez ovir in kontekstualno natančno komunikacijo med ljudmi – ne glede na to, ali govorijo skupen jezik.

Ne gre le za togo prevajanje besed, ampak za **prenos pomena**. Nexus Gaja povezuje ljudi na globlji ravni z razumevanjem kulturnih, regionalnih in kontekstualnih odtenkov ter tako omogoča pristne, verodostojne pogovore.

## Možnosti in funkcije
- **Večpredstavnostna komunikacija**: sistem ne obdeluje samo besedila, ampak tudi sliko, zvok in video. To omogoča popolnoma poglobljene pogovore (npr. video klice ali glasovna sporočila) v realnem času prek jezikovnih ovir.
- **Občutljivost na kontekst**: prepoznavanje ironije, idiomov, žargona in regionalnih narečij, ki jih običajni prevajalci pogosto napačno razumejo.
- **Mreža med platformami**: Služi kot osnova za zasebne klepete, teme foruma (objave s komentarji) in interakcije globalne skupnosti.

---

## Tehnična arhitektura (temeljni koncept)

Tehnično jedro Nexus Gaja je komunikacijski model, izdelan po meri, ki je strogo razdeljen na tri plasti:

1. **Original**: Komunikacijski objekt (sporočilo), ki ga ustvari pošiljatelj, vedno ostane nespremenljiv.
2. **Semantična razlaga**: sistem ne analizira le besed, ampak dejanski pomen.
3. **Predstavitev ciljnega jezika**: AI samo ustvari začasno ali predpomnjeno predstavitev izvirnika za posameznega prejemnika na podlagi njihovega želenega jezika. Prevodi nikoli ne prepišejo izvirnega sporočila.

### Odvisnost od konteksta
Prevodi v Nexus Gaji si nikoli ne ogledajo ločenih sporočil. Motor upošteva celotno hierarhijo:
`Sporočilo` → `Prejšnja sporočila` → `Kontekst niti` → `Kontekst skupnosti` → `Jezik/regija` → `Uporabniške nastavitve`

### Učinkovitost s prevodom na zahtevo
Prevajanje poteka z učinkovito uporabo virov samo **na zahtevo** (na zahtevo). Ko uporabnik zahteva vsebino, se ta prevede v njegov prednastavljeni jezik. Ko je enkrat ustvarjen prevod za določen jezik, se trajno shrani (predpomnilnik), da se drastično pospešijo prihodnje zahteve.

## Moderiranje s pomočjo umetne inteligence (WP 1.8.4)

Z AI-Assisted Moderation naredimo pomemben korak od ideje izdelka do tehnične arhitekture, pri čemer upoštevamo veljavne predpise EU (zahteve glede preglednosti EU AI Act po 50. členu; Digital Services Act z razumljivimi utemeljitvami in možnostmi pritožbe).

### 1. Osnovno načelo
Najpomembnejši stavek za arhitekturo je: **Umetna inteligenca za moderiranje je pregledovalni sistem, ne avtonomen vladajoči sistem.**
Zasnovan je tako, da zmerno pomaga ljudem, ne pa zato, da sam določa, katera mnenja lahko obstajajo na Nexus Gaji.
Ločimo med tremi stopnjami:
- **Zaznavanje:** "Tu lahko pride do kršitve pravila."
- **Ocena:** "Verjetnost kršitve pravila je na primer 94 %."
- **Odločitev:** "Kateri ukrep je dejansko sprejet?"
Tretjo raven mora v hujših primerih nadzorovati človek.

### 2. Umetna inteligenca za moderiranje kot podsistem
Namesto ene same AI je vzpostavljen robusten podsistem:
```besedilo
                 NEXUS GAJA AI MODERACIJA
                          │
       ┌───────────────────┼────────────────────┐
       │ │ │
  Jezik AI Varnost AI Goljufije AI
       │ │ │
       ├───────────────┬───┴───────────────┬───┤
       │ │ │
 Identiteta prevodnega vedenja
 Analiza Analiza signalov
       │ │ │
       └───────────────┼───────────────────┘
                      ▼
               Ocena tveganja
                      │
                      ▼
               Človeški pregled
```

### 3. Najpomembnejši moduli AI
Nexus Gaja uporablja devet specializiranih področij analize:
- **M1 – Razumevanje jezika**: zazna jezik, narečje, sleng, indikatorje ironije, težave s prevodom.
- **M2 – zaznavanje strupenosti/zlorabe**: zazna žalitve, osebne napade, nadlegovanje.
- **M3 – zaznavanje groženj**: zazna potencialne grožnje, izsiljevanje, napovedi nasilja.
- **M4 – Zaznavanje sovraštva/dehumanizacije**: zazna ciljane napade na ljudi na podlagi določenih pripadnosti.
- **M5 – zaznavanje neželene pošte/manipulacije**: zazna neželeno pošto, vedenje botov, usklajeno manipulacijo.
- **M6 – Fraud Detection**: zazna sumljive poskuse goljufij, lažno predstavljanje, socialni inženiring.
- **M7 – Celovitost identitete**: Preverja signale glede prevzemov računov, več računov, izogibanje prepovedi.
- **M8 – Media Safety**: Analizira slike, zvok, video, dokumente.
- **M9 – Context Engine**: Najpomembnejši modul. Združuje posamezne ugotovitve.

### 4. Zakaj je Context Engine ključen
Samo iskanje po ključnih besedah ne bi zadostovalo. "Lahko bi ga ubil od smeha" pomensko vsebuje nasilje, vendar je figura govora. "Jutri ob 20. uri ga bom streljal pred njegovo hišo" je povsem druga situacija. AI mora razumeti, kaj izjava pomeni v svojem posebnem kontekstu.

### 5. Večjezično moderiranje
Zmernost ne more preprosto primerjati besed. Analizirati mora pomensko raven (npr. nemški idiomi v primerjavi z japonskimi idiomi v primerjavi z regionalnimi izrazi).

### 6. Izvirni jezik + prevod
Izvirnik in prevod sta analizirana ločeno. Šele nato se izvede "kombinirano ocenjevanje moderiranja". To omogoča Nexus Gaja, da ugotovi, ali je sam prevod morda stopnjeval ali spremenil dejstva.

### 7. Ocena zaupanja
Vsako vrednotenje umetne inteligence prejme oceno zaupanja (npr. verjetnost grožnje: 0,96). Vendar: **Rezultat zaupanja ≠ Resnica.** Rezultat 96 % samo pomeni, da je model zelo prepričan o svoji klasifikaciji, ne pa nujno, da je uporabnik kriv.

### 8. Negotovost sama postane signal
Če je umetna inteligenca negotova (npr. Grožnja: 0,62, Satira: 0,54), ne sme preprosto uveljavljati strogih pravil. Namesto tega je negotovost vgrajena neposredno v arhitekturo: **Potreben je človeški pregled**.

### 9. Štiri območja odločitve
- 🟢 **ZELENO**: zelo verjetno skladno. → brez ukrepanja.
- 🟡 **RUMENO**: Možna kršitev. → spremljajte / po potrebi opozorite.
- 🟠 **ORANŽNA**: Verjetna kršitev. → moderacijski pregled.
- 🔴 **RDEČA**: možna huda kršitev. → takojšen zaščitni ukrep + človeški pregled.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Zaščitni ukrepi se lahko izvedejo samodejno
V primeru konkretne grožnje (Zaznana grožnja → Visoko zaupanje → Začasna omejitev → Človeški pregled → Odločitev) zaščitimo ogroženega uporabnika, ne da bi AI spremenili v sodnika.

### 12. AI mora biti sposoben utemeljiti svoje odločitve
DSA zahteva jasne in posebne razloge. AI zagotavlja strukturirano razmišljanje: pravilo (NG-CONDUCT-004), zaznano (potencialna konkretna grožnja), zaupanje (0,94), ustrezen kontekst (prejšnja 4 sporočila), priporočeni ukrep (človeški pregled).

### 13. AI ne sme na skrivaj spreminjati vsebine
**Umetna inteligenca moderiranja ne sme nikoli neopazno spremeniti izvirne vsebine.** Med samodejnim popravkom, prevodom ali povzemanjem se izvirnik vedno ohrani.

### 14. Vsebina, ustvarjena z umetno inteligenco
Razlikujemo med: človeško ustvarjenim, s pomočjo umetne inteligence, ustvarjenim z umetno inteligenco in manipuliranim z umetno inteligenco. To bo postalo del metapodatkov vsebine.

### 15. Označevanje vsebine AI in sloj izvora AI
V skladu s pravili o preglednosti zakona EU o umetni inteligenci (velja od avgusta 2026) mora biti vsebina, ustvarjena z umetno inteligenco, prepoznavna. Ponujamo plast porekla AI, ki shranjuje metapodatke (izvor AI, model, časovni žig, človeški pregled).

### 16. Deepfake Detection
Cilj arhitekture je zaznati sintetične slike, klonirane glasove in globoke ponaredke. Vendar odkrivanje ni samodejni dokaz.

### 17. Brez samodejnega "stroja resnice" (moderacija ≠ preverjanje dejstev)
En sistem preveri: "Ali vsebina krši pravila?" (Moderiranje vsebine), drugi podaja: "Katere informacije in viri so na voljo?" (Informacijska pomoč). Mnenja niso preprosto izbrisana, ker so "napačna".

### 18. Zaščita pred napačno kulturno interpretacijo
Umetna inteligenca zahteva **Modele kulturnega konteksta**, da prepreči, da bi se komunikacijske norme ene države prevzele kot globalni standard.

### 19. Ironija, satira in humor
Umetna inteligenca uporablja kontekst, emojije, zgodovino pogovorov in znane ironične strukture, vendar mora dopuščati negotovost, ko so pomeni dvoumni.

### 20. Brez kazni na podlagi ene same ocene AI
Noben resen poseg moderiranja ne sme temeljiti samo na enem samem rezultatu avtomatizirane klasifikacije (besedilo + kontekst + vedenje + jezik + mediji + mehanizem pravil = ocena tveganja).

### 21. Signali vedenja uporabnikov in brez socialnega kreditnega sistema
To se nanaša na znake tehnične zlorabe (npr. množično objavljanje neželene e-pošte), ne pa na splošni družbeni sistem ocenjevanja. Nexus Gaja ne vzdržuje socialnega kreditnega sistema – zmernost služi varnosti in ne oceni vrednosti osebe.

### 22. Umetna inteligenca moderiranja mora biti revizijska
Vse pomembne samodejne odločitve se beležijo (ID dogodka, ID pravila, zaupanje, človeški pregled itd.), da se zagotovi sledljivost.

### 23. Lažno pozitivni rezultati, lažno negativi in merila kakovosti
Vrste napak se spremljajo. Nadzorna plošča meri natančnost, odpoklic in zlasti **stopnjo razveljavitve pritožbe** (število uspešnih pritožb).

### 24. Jezikovna pravičnost in pristranskost pri prevajanju
Kakovost moderiranja mora biti primerljiva v vseh podprtih jezikih (Multilingual Moderation Benchmark). Če se rezultati moderiranja med izvirnikom in prevodom razlikujejo (konflikt prevoda), je treba to posebej pregledati.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. Človek ostaja zadnja avtoriteta
- **NG-AI-MOD-001**: AI pomaga pri odkrivanju in razvrščanju, vendar ne nadomesti človeškega pregleda pri resnih odločitvah.
- **NG-AI-MOD-002**: Samodejne moderacijske odločitve morajo biti sledljive, beležene in preverljive.

**Povzetek**: Gradimo štiristopenjski sistem: odkrivanje umetne inteligence, analiza konteksta in tveganja, mehanizem politike in človeško upravljanje. To omogoča močno avtomatizacijo brez ustvarjanja nevarne arhitekture "AI kot sodnik".

## Načela financiranja in model prihodkov (WP 1.10.1)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Principle NG-FIN-001
Nexus Gaja finances its operations through transparent revenue streams separated from user interests, and not through the monetization of its users' attention or personal data.

### 2. No Traditional Advertising
Specifically prohibited are:
- Banner ads
- Pop-up ads
- Auto-playing video ads
- Sponsored posts in the standard feed
- Personalized advertising profiles
- Sale of user profiles or personal data
- Advertising derived from private conversations.

Nexus Gaja remains a **communication space rather than an advertising space**.

### 3. Financiranje brez oglaševanja (6 stebrov)
Financiranje je zgrajeno na šestih stebrih:
```besedilo
                 NEXUS GAJA
                     │
       ┌─────────────┼──────────────┐
       ▼ ▼ ▼
   DONACIJE PREMIUM ORGANIZACIJ
       │ │ │
       ├─────────────┼──────────────┤
       ▼ ▼ ▼
    DONACIJE PARTNERSTVA STORITVE
```

#### 1. steber – brezplačno osnovno članstvo
**Nexus Gaja Free** omogoča osnovno mednarodno razumevanje za vsakogar (profil, mednarodna komunikacija, objave, skupnosti, klepeti, osnovni prevod) brez stroškov.

#### 2. steber – vrhunske ponudbe
Prostovoljne plačljive ponudbe (**Nexus Gaja Plus**), ki zagotavljajo večje omejitve prostora za shranjevanje, višjo kakovost medijev, razširjene kvote AI in organizacijske funkcije.
**Pomembno (Freemium namesto Dark Freemium):** Osnovna komunikacija ne sme biti nikoli umetno poslabšana.

#### 3. steber – Organizacije
Posebni računi za šole, univerze, nevladne organizacije, podjetja in občine (**Organizacija Nexus Gaja**). Šole je mogoče podpreti z institucionalnimi stopnjami kot multiplikatorji mednarodnega razumevanja.

#### 4. steber – Donacije
**Nexus Gaja Funding Pool** sprejema splošne in namenske donacije (npr. "za mednarodno komunikacijo mladih"). **Knjiga dodeljevanja sredstev** zagotavlja pregledno dodeljevanje sredstev.
**Namenski sklad in tombola:** Del donacij napaja sklad za brezplačno/s popustom uporabo. Mehanizem loterije/tombole lahko ta sredstva dodeli pregledno in revizijsko.

#### 5. steber – Institucionalno financiranje
Fundacije, programi financiranja kulture ali državni programi.
**NG-FIN-002:** Finančna podpora ne zahteva uredniškega ali tehničnega nadzora (neodvisnost).

#### Steber 6 – Komercialne storitve
Storitve B2B, kot je **Prevajanje kot storitev** (API), organizacijska komunikacija ali mednarodne konferenčne sobe, ne da bi obremenjevali standardni vir uporabnikov.

### 4. Brez monetizacije podatkov in nadzorne ekonomije
**NG-FIN-003:** Osebni podatki uporabnika niso blago. Brez prodaje seznamov, profilov ali zgodovin. Nexus Gaja nima koristi od psihološkega nadzora (Surveillance Economy).

### 5. Finančna preglednost in knjiga sklada
**Nexus Gaja Finančna preglednost:** Objava agregiranih finančnih struktur. Za namenske donacije se izvede tehnično računovodstvo (ID sklada → Namen → Stanje → Dodelitev). Brez navzkrižnega subvencioniranja socialnih namenov v korporativni marketing.

### 6. Solidarnostni model financiranja
Cene temeljijo na stroškovni naravnanosti, pravičnosti in solidarnosti.
**Solidarity Premium:** Prostovoljna možnost za Premium uporabnike, da financirajo del dostopa drugega uporabnika. Prisilna solidarnost ali družba višjega razreda (manj spoštovanja/moderacije za brezplačne uporabnike) je strogo prepovedana.

### 7. Ekonomski KPI-ji namesto gospodarstva angažiranosti
Brez odvisnosti od ohranjanja uporabnikov "na spletu čim dlje" (brez ragebaita, neskončnih virov).
Namesto tega uporabljamo meritve, kot so:
- **Globalni komunikacijski indeks (GCI):** Uspešni komunikacijski odnosi med ljudmi iz različnih jezikovnih/kulturnih regij.
- **Platform Sustainability Ratio (PSR):** Ponavljajoči se prihodki/ponavljajoči se operativni stroški (Cilj ≥ 1).

### 8. Česa izrecno ne želimo (negativni seznam)
Nexus Gaja **ne** financira:
❌ Prodaja osebnih podatkov
❌ Personalizirano tradicionalno oglaševanje
❌ Spremljanje vedenja uporabnikov za namene oglaševanja
❌ Prodaja zasebnih komunikacijskih podatkov
❌ Skrita uporaba podatkov AI
❌ Manipulativni plačljivi zidovi Premium
❌ Omejitev umetnega dosega za monetizacijo
❌ Plačan politični vpliv
❌ Nakup privilegiranih moderacijskih odločitev.

### 9. Predhodna finančna arhitektura
```besedilo
                         NEXUS GAJA
                              │
             ┌─────────────────┼──────────────────┐
             │ │ │
             ▼ ▼ ▼
          ORGANIZACIJE UPORABNIKOV PODJETJE
             │ │ │
             └─────────────────┼─────────────────┘
                              │
                       STORITVE PLATFORME
                              │
          ┌────────────────────┼──────────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS
                              │
                    ┌──────────┴──────────┐
                    ▼ ▼
               OMEJENI SKLAD SPLOŠNEGA SKLADA
                                        │
                                        ▼
                                  SOCIALNI NAMEN
```

### Povzetek načel financiranja (NG-FIN)
- **NG-FIN-001:** Brez financiranja prek tradicionalnega oglaševanja.
- **NG-FIN-002:** Brez uredniškega/tehničnega nadzora s finančno podporo.
- **NG-FIN-003:** Osebni podatki niso blago.
- **NG-FIN-004:** Osnovna komunikacija ostaja dostopna brez plačila.
- **NG-FIN-005:** Premium ponudbe ne smejo poslabšati brezplačnih uporabnikov.
- **NG-FIN-006:** Namenska sredstva se upravljajo po namenu.
- **NG-FIN-007:** Pregledno upravljanje donacij in nepovratnih sredstev.
- **NG-FIN-008:** Komercialne storitve B2B ne ogrožajo neodvisnosti.
- **NG-FIN-009:** Osredotočite se na trajnost in ne na maksimalno monetizacijo.
- **NG-FIN-010:** Objekt trajno zavaruje družbeni namen.

## API, vmesniki in komunikacijska arhitektura (WP 1.11.3)

Za zagotovitev stabilnosti, varnosti in razširljivosti sistema Nexus Gaja sledi arhitekturi, ki temelji izključno na API-ju in temelji na dogodkih.

### Temeljna načela
- **Brez neposrednega dostopa do baze podatkov:** Komponente komunicirajo izključno prek definiranih vmesnikov (API-jev ali dogodkov), nikoli prek neposrednih poizvedb v bazi podatkov drugih storitev.
- **API Gateway:** Vse zunanje zahteve odjemalcev potekajo skozi API Gateway, ki obravnava preverjanje pristnosti, usmerjanje in omejevanje hitrosti.
- **Abstrakcija ponudnika:** Zunanje storitve (modeli umetne inteligence, ponudniki plačil, prevajalski mehanizmi) so integrirane prek abstraktnih plasti, s čimer se izognemo trdo kodiranim odvisnostim in omogočimo prilagodljivo zamenjavo ponudnika.

### Komunikacijski vzorci
- **Sinhroni API-ji (REST/HTTPS):** Uporablja se za takojšnje zahteve, kot so prijava, nastavitve profila ali neposredni prevodi.
- **Asinhroni dogodki (vodilo dogodkov):** Centralni živčni sistem Nexus Gaja za zakasnjeno, ločeno obdelavo (npr. `Message.Created`, ki sproži moderiranje, prevajanje in obveščanje asinhrono).
- **Realni čas (WebSocket):** Namenski kanali za klepet v živo in indikatorje tipkanja.

### Varnost in zanesljivost
- **Model ničelnega zaupanja:** notranjemu omrežnemu prometu se ne zaupa samodejno; občutljiva komunikacija storitev-storitev zahteva avtentikacijo.
- **Vzorec idempotence & Outbox:** Kritične operacije (kot so donacije ali pošiljanje sporočil) so zasnovane tako, da so idempotentne, da se prepreči podvojena obdelava, z uporabo vzorca Outbox, da se zagotovi, da se dogodki nikoli ne izgubijo niti med transakcijami baze podatkov.

## Model domene MVP (WP 1.12)

Nexus Gaja uporablja izključno domensko usmerjeno MVP arhitekturo (ADR-025), zasnovano kot modularni monolit z jasnimi domenskimi mejami. Ta struktura preprečuje prezgodnjo kompleksnost mikrostoritev, hkrati pa ohranja prilagodljivost za kasnejšo razdelitev določenih domen.

### Entitete osnovne domene
Arhitektura eksplicitno ločuje različne koncepte, da zagotovi celovitost podatkov in se izogne strukturnim pastem, kot je "uporabniško ime = človek":
- **Identiteta in računi:** `Oseba` ≠ `Uporabniški račun` ≠ `Preverjanje identitete`. Preverjena oseba sodeluje prek računa, vendar subjekti ostanejo ločeni.
- **Komunikacija:** `Sporočilo` ≠ `Prevod`. Prvotno sporočilo ostane nespremenljivo; prevodi so povezane entitete.
- **Moderacija:** `Poročilo` ≠ `Odločitev o moderiranju`. Poročilo je le zahtevek; moderatorski primer vodi preiskavo.
- **Finance:** `Donacija` ≠ `Stanje sredstev`. Plačila se knjižijo prek nespremenljive knjige v sklad, kar zagotavlja finančno preglednost.

### Medsebojno povezane domene
Sistem je razdeljen na jasne logične domene (omejene kontekste): identiteta, račun, organizacija, komunikacija, skupnost, jezik, moderiranje, obveščanje, finance in upravljanje. Te domene preslikajo celotno pot od entitet v resničnem svetu (uporabnikov, šol, nevladnih organizacij) do njihovih digitalnih interakcij in povezanega upravljanja.

## Status projekta
Projekt je trenutno v fazi aktivne arhitekture in načrtovanja.
Tekoče arhitekturne odločitve so dokumentirane v mapi `/docs`.