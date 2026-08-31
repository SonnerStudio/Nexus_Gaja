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

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

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

### 10. Brez "kazni AI"
**Umetna inteligenca ne nalaga dokončnih sankcij.** Lahko sproži takojšnje tehnične ukrepe (npr. začasno zadržanje sporočila) zaradi resnih varnostnih pomislekov, vendar je končna odločitev še vedno preverljiva.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. AI mora biti sposoben utemeljiti svoje odločitve
DSA zahteva jasne in posebne razloge. AI zagotavlja strukturirano razmišljanje: pravilo (NG-CONDUCT-004), zaznano (potencialna konkretna grožnja), zaupanje (0,94), ustrezen kontekst (prejšnja 4 sporočila), priporočeni ukrep (človeški pregled).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

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

### 25. Motor za predloge in politike arhitekture
Pravila (policy engine) niso trdo kodirana v modele AI. AI zagotavlja ugotovitve; Policy Engine odloča na podlagi trenutnih pravil. To omogoča **spremembe modela brez sprememb pravil**.

### 26. Človek ostaja zadnja avtoriteta
- **NG-AI-MOD-001**: AI pomaga pri odkrivanju in razvrščanju, vendar ne nadomesti človeškega pregleda pri resnih odločitvah.
- **NG-AI-MOD-002**: Samodejne moderacijske odločitve morajo biti sledljive, beležene in preverljive.

**Povzetek**: Gradimo štiristopenjski sistem: odkrivanje umetne inteligence, analiza konteksta in tveganja, mehanizem politike in človeško upravljanje. To omogoča močno avtomatizacijo brez ustvarjanja nevarne arhitekture "AI kot sodnik".

## Status projekta
Projekt je trenutno v fazi aktivne arhitekture in načrtovanja.
Tekoče arhitekturne odločitve so dokumentirane v mapi `/docs`.