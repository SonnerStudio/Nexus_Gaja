# Nexus Gaja

![Nexus Gaja logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** on intelligentne kontekstitundlik sidevõrk, mis on loodud globaalse suhtluse revolutsiooni muutmiseks.

## Eesmärk ja visioon
Globaliseeruvas maailmas on keel sageli suurim takistus. Nexus Gaja põhieesmärk on võimaldada inimeste vahel sujuvat, takistusteta ja kontekstuaalselt täpset suhtlust olenemata sellest, kas nad räägivad ühist keelt.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

Nexus Gaja tehniline tuum on eritellimusel valmistatud sidemudel, mis on rangelt jagatud kolme kihti:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## AI-Assisted Moderation (WP 1.8.4)

Tehisintellekti abiga modereerimisega astume olulise sammu tooteideest tehnilise arhitektuurini, võttes arvesse kehtivaid EL-i regulatsioone (ELi tehisintellekti seaduse läbipaistvusnõuded art. 50 alusel; digitaalteenuste seadus koos arusaadavate põhjenduste ja edasikaebamisvõimalustega).

### 1. Basic Principle
The most important sentence for the architecture is: **The moderation AI is a review system, not an autonomous ruling system.**
It is designed to assist humans in moderation, not to determine itself which opinions are allowed to exist on Nexus Gaja.
We differentiate between three levels:
- **Detection:** "There could be a rule violation here."
- **Evaluation:** "The probability of a rule violation is, for example, 94%."
- **Decision:** "What action is actually taken?"
The third level must be controlled by a human in severe cases.

### 2. Moderatsiooni AI kui alamsüsteem
Ühe AI asemel luuakse tugev alamsüsteem:
``` tekst
                 NEXUS GAJA AI MODERATSIOON
                          │
       ┌─────────────────┼─────────────-──
       │ │ │
  Keel AI Ohutus AI Pettus AI
       │ │ │
       ├-
       │ │ │
 Tõlkekäitumise identiteet
 Analüüs Analüüsi signaalid
       │ │ │
       └──────────────┼───────────────────
                      ▼
               Riski hindamine
                      │
                      ▼
               Human Review
```

### 3. Kõige olulisemad AI moodulid
Nexus Gaja kasutab üheksat spetsiaalset analüüsivaldkonda:
- **M1 – keele mõistmine**: tuvastab keele, dialekti, slängi, iroonianäitajad ja tõlkeprobleemid.
- **M2 – mürgisuse/kuritarvitamise tuvastamine**: tuvastab solvangud, isiklikud rünnakud ja ahistamise.
- **M3 – ohu tuvastamine**: tuvastab võimalikud ähvardused, väljapressimised ja vägivallateated.
- **M4 – vihkamise/dehumaniseerimise tuvastamine**: tuvastab sihipärased rünnakud inimeste vastu, lähtudes konkreetsetest sidemetest.
- **M5 – rämpsposti/manipulatsiooni tuvastamine**: tuvastab rämpsposti, robotite käitumise ja koordineeritud manipuleerimise.
- **M6 – pettuse tuvastamine**: tuvastab kahtlased pettusekatsed, andmepüügi ja sotsiaalse manipuleerimise.
- **M7 – identiteedi terviklikkus**: kontrollib signaale konto ülevõtmise, mitme konto ja keelust kõrvalehoidmise kohta.
- **M8 – meedia ohutus**: analüüsib pilte, heli, videot, dokumente.
- **M9 – kontekstimootor**: kõige olulisem moodul. See ühendab üksikud leiud.

### 4. Miks on kontekstimootor ülioluline?
Puhast märksõnaotsingust ei piisa. "Ma võiksin ta naermisest tappa" sisaldab semantiliselt vägivalda, kuid on kõnekujund. "Homme kell 20 lasen ma ta maja ees maha" on hoopis teine ​​olukord. Tehisintellekt peab mõistma, mida avaldus selle konkreetses kontekstis tähendab.

### 5. Mitmekeelne modereerimine
Mõõdukus ei saa lihtsalt sõnu võrrelda. See peab analüüsima semantilist taset (nt saksa idioomid vs jaapani idioomid vs piirkondlikud väljendid).

### 6. Algkeel + tõlge
Eraldi analüüsitakse originaali ja tõlget. Alles seejärel toimub "kombineeritud modereerimise hindamine". See võimaldab Nexus Gajal kindlaks teha, kas tõlge ise võis fakte eskaleerida või muuta.

### 7. Usalduse skoor
Iga tehisintellekti hindamine saab usaldusskoori (nt ohu tõenäosus: 0,96). Siiski: **Usaldusskoor ≠ Tõde.** 96% skoor tähendab ainult seda, et mudel on oma klassifikatsioonis väga kindel, mitte aga tingimata seda, et kasutaja on süüdi.

### 8. Ebakindlusest saab signaal ise
Kui tehisintellekt on ebakindel (nt oht: 0,62, satiir: 0,54), ei tohi see lihtsalt karme reegleid jõustada. Selle asemel on ebakindlus otse arhitektuuri sisse ehitatud: **Vajalik on inimlik ülevaade**.

### 9. Neli otsusetsooni
- 🟢 **ROHELINE**: suure tõenäosusega vastavuses. → ei mingit tegevust.
- 🟡 **KOLLANE**: võimalik rikkumine. → jälgige / vajadusel hoiatage.
- 🠠 **ORANŽ**: tõenäoline rikkumine. → modereerimise ülevaade.
- 🔴 **PUNANE**: võimalik tõsine rikkumine. → kohene kaitsemeede + inimese ülevaatus.

### 10. AI karistust pole
** Tehisintellekt ei kehtesta lõplikke sanktsioone.** See võib tõsiste turvaprobleemide korral käivitada kohesed tehnilised meetmed (nt sõnumi saatmise ajutine tagasilükkamine), kuid lõplikku otsust saab kontrollida.

### 11. Kaitsemeetmed võivad rakenduda automaatselt
Konkreetse ohu korral (Tuvastati oht → Suur usaldus → Ajutine piirang → Inimese ülevaatus → Otsus) kaitseme ohustatud kasutajat ilma tehisintellektist kohtunikku muutmata.

### 12. AI peab suutma oma otsuseid põhjendada
DSA nõuab selgeid ja konkreetseid põhjuseid. Tehisintellekt pakub struktureeritud põhjendusi: reegel (NG-CONDUCT-004), tuvastatud (potentsiaalne konkreetne oht), usaldus (0,94), asjakohane kontekst (eelmised 4 sõnumit), soovituslik tegevus (inimeste ülevaade).

### 13. AI ei tohi sisu salaja muuta
**Mõõdukas tehisintellekt ei tohi kunagi algset sisu märkamatult muuta.** Automaatse parandamise, tõlkimise või kokkuvõtte tegemise ajal säilitatakse alati originaal.

### 14. AI-ga loodud sisu
Teeme vahet: inimese loodud, tehisintellekti abil loodud, tehisintellekti loodud ja tehisintellektiga manipuleeritud vahel. Sellest saab osa sisu metaandmetest.

### 15. AI sisu ja AI päritolukihi märgistamine
EL-i tehisintellekti seaduse (jõustub augustist 2026) läbipaistvusreeglite kohaselt peab tehisintellekti loodud sisu olema tuvastatav. Pakume tehisintellekti päritolukihti, mis salvestab metaandmeid (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. Automaatne "tõemasin" puudub (mõõdukus ≠ faktikontroll)
Üks süsteem kontrollib: "Kas sisu rikub reegleid?" (Sisu modereerimine), teine ​​pakub järgmist: "Milline teave ja allikad on saadaval?" (Teabeabi). Arvamusi ei kustutata lihtsalt sellepärast, et need on "valed".

### 18. Kaitse kultuurilise väärtõlgenduse eest
Tehisintellekt nõuab **kultuurikonteksti mudeleid**, et vältida ühe riigi suhtlusnormide võtmist globaalse standardina.

### 19. Iroonia, satiir ja huumor
AI kasutab konteksti, emotikone, vestluste ajalugu ja teadaolevaid irooniastruktuure, kuid peab võimaldama ebakindlust, kui tähendused on mitmetähenduslikud.

### 20. Ühel tehisintellekti skoori alusel karistus puudub
Ükski tõsine modereerimissekkumine ei tohi põhineda ainult ühel automatiseeritud klassifitseerimise tulemusel (tekst + kontekst + käitumine + keel + meedia + reeglimootor = riskianalüüs).

### 21. Kasutaja käitumise signaalid ja sotsiaalse krediidisüsteemi puudumine
See on seotud tehniliste kuritarvitamise signaalidega (nt massiline rämpspostitus), mitte üldise sotsiaalse reitingusüsteemiga. Nexus Gaja ei halda sotsiaalset krediidisüsteemi – mõõdukus teenib turvalisust, mitte inimese väärtuse hindamist.

### 22. Mõõdukas AI peab olema auditeeritav
Jälgitavuse tagamiseks logitakse kõik asjakohased automatiseeritud otsused (sündmuse ID, reegli ID, usaldus, inimülevaatus jne).

### 23. Valepositiivsed, valenegatiivid ja kvaliteedimõõdikud
Veatüüpe jälgitakse. Armatuurlaud mõõdab täpsust, tagasikutsumist ja eriti **apellatsiooni tagasivõtmise määra** (edukate apellatsioonide arv).

### 24. Language Equity & Translation Bias
Modereerimise kvaliteet peab olema kõigis toetatud keeltes võrreldav (mitmekeelne modereerimise võrdlusalus). Kui modereerimistulemused erinevad originaali ja tõlke vahel (tõlkekonflikt), tuleb see eraldi üle vaadata.

### 25. Arhitektuuriettepaneku ja poliitika mootor
Reeglid (Policy Engine) ei ole AI mudelitesse sisse kodeeritud. Tehisintellekt pakub leide; poliitikamootor otsustab kehtivate reeglite alusel. See võimaldab **mudeleid muuta ilma reeglite muutmiseta**.

### 26. Inimene jääb lõplikuks autoriteediks
- **NG-AI-MOD-001**: tehisintellekt aitab tuvastada ja klassifitseerida, kuid ei asenda tõsiste otsuste tegemisel inimese kontrolli.
- **NG-AI-MOD-002**: automaatsed modereerimisotsused peavad olema jälgitavad, logitavad ja kontrollitavad.

**Kokkuvõte**: ehitame neljaetapilise süsteemi: tehisintellekti tuvastamine, konteksti- ja riskianalüüs, poliitikamootor ja inimjuhtimine. See võimaldab tugevat automatiseerimist ilma ohtlikku "AI kui kohtuniku" arhitektuuri looma.

## Finantseerimispõhimõtted ja tulumudel (WP 1.10.1)

Nexus Gaja puhul kehtib väga oluline majanduslik põhimõte: **platvormil ei ole traditsioonilist reklaami.**
See eristab Nexus Gajat paljudest tänapäeva sotsiaalvõrgustikest. See aga ei tähenda, et Nexus Gaja ei saaks olla kommertsliku iseloomuga. Vastupidi, platvorm peab olema majanduslikult elujõuline, et selle sotsiaalne eesmärk püsiks. Majandustegevus on vahend eesmärgi saavutamiseks, mitte platvormi esmane eesmärk.

### 1. Põhimõte NG-FIN-001
Nexus Gaja rahastab oma tegevust läbipaistvate tuluvoogude kaudu, mis on eraldatud kasutajate huvidest, mitte aga kasutajate tähelepanu või isikuandmete monetiseerimise kaudu.

### 2. Traditsiooniline reklaam puudub
Eriti keelatud on:
- bännerreklaamid
- Hüpikreklaamid
- Automaatselt esitatavad videoreklaamid
- Sponsoreeritud postitused standardvoos
- Isikupärastatud reklaamiprofiilid
- Kasutajaprofiilide või isikuandmete müük
- Privaatsetest vestlustest tuletatud reklaam.

Nexus Gaja jääb pigem **kommunikatsioonipinnaks kui reklaamipinnaks**.

### 3. Financing Without Advertising (The 6 Pillars)
Financing is built on six pillars:
```text
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
   PREMIUM       ORGANIZATION    DONATIONS
       │             │             │
       ├─────────────┼─────────────┤
       ▼             ▼             ▼
    GRANTS       PARTNERSHIPS    SERVICES
```

#### Pillar 1 – Free Basic Membership
**Nexus Gaja Free** enables basic international understanding for everyone (profile, international communication, posts, communities, chats, basic translation) at no cost.

#### Pillar 2 – Premium Offerings
Voluntary paid offerings (**Nexus Gaja Plus**) providing greater storage limits, higher media quality, expanded AI quotas, and organizational features.
**Important (Freemium instead of Dark Freemium):** Basic communication must never be artificially degraded.

#### Pillar 3 – Organizations
Special accounts for schools, universities, NGOs, businesses, and municipalities (**Nexus Gaja Organization**). Schools can be supported via institutional rates as multipliers of international understanding.

#### 4. sammas – annetused
**Nexus Gaja rahastamiskogu** võtab vastu üldisi ja sihtotstarbelisi annetusi (nt „rahvusvaheliseks noortesuhtluseks”). **Fondide jaotamise pearaamat** tagab vahendite läbipaistva jaotamise.
**Eesmärgifond ja tombola:** osa annetustest toidab basseini tasuta/soodushinnaga kasutamiseks. Loterii/tombola mehhanism võib neid vahendeid eraldada läbipaistvalt ja auditeeritavalt.

#### 5. sammas – institutsioonide rahastamine
Sihtasutused, kultuuri rahastamisprogrammid või riiklikud programmid.
**NG-FIN-002:** Rahaline toetus ei tähenda toimetuslikku ega tehnilist kontrolli (Independence).

#### 6. sammas – kommertsteenused
B2B-teenused, nagu **Tõlke teenusena** (API), organisatsiooniline suhtlus või rahvusvahelised konverentsiruumid, ilma standardset kasutajavoogu koormamata.

### 4. Andmete monetiseerimine ja järelevalve majandus
**NG-FIN-003:** Isiklikud kasutajaandmed ei ole kaup. Ei müüda loendeid, profiile ega ajalugu. Nexus Gaja ei saa kasu psühholoogilisest jälgimisest (seiremajandus).

### 5. Finantsläbipaistvus ja fondide pearaamat
**Nexus Gaja finantsläbipaistvus:** koondatud finantsstruktuuride avaldamine. Sihtotstarbelised annetused saavad tehnilise arvestuse (fondi ID → Eesmärk → Saldo → Eraldamine). Ei mingit sotsiaalsete eesmärkide ristsubsideerimist ettevõtte turundusse.

### 6. Solidarity-Based Financing Model
Pricing is based on cost-orientation, fairness, and solidarity.
**Solidarity Premium:** A voluntary option for Premium users to finance a portion of another user's access. Forced solidarity or a premium class society (less respect/moderation for free users) is strictly prohibited.

### 7. Economic KPIs Instead of Engagement Economy
No dependence on keeping users "online as long as possible" (no ragebait, infinite feeds).
Instead, we use metrics like:
- **Global Communication Index (GCI):** Successful communication relationships between people from different linguistic/cultural regions.
- **Platform Sustainability Ratio (PSR):** Recurring revenue / recurring operating costs (Target ≥ 1).

### 8. What We Explicitly Do Not Want (Negative List)
Nexus Gaja is **not** financed by:
❌ Sale of personal data
❌ Personalized traditional advertising
❌ Monitoring user behavior for advertising purposes
❌ Sale of private communication data
❌ Hidden AI data usage
❌ Manipulative Premium paywalls
❌ Artificial reach restriction for monetization
❌ Paid political influence
❌ Purchase of privileged moderation decisions.

### 9. Preliminary Financial Architecture
```text
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
          USERS          ORGANIZATIONS      ENTERPRISE
             │                │                │
             └────────────────┼────────────────┘
                              │
                       PLATFORM SERVICES
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
       PREMIUM             DONATIONS            API
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
               GENERAL FUND       RESTRICTED FUNDS
                                        │
                                        ▼
                                  SOCIAL PURPOSE
```

### Summary of Financing Principles (NG-FIN)
- **NG-FIN-001:** No financing through traditional advertising.
- **NG-FIN-002:** No editorial/technical control through financial support.
- **NG-FIN-003:** Personal data is not a commodity.
- **NG-FIN-004:** Basic communication remains accessible without payment.
- **NG-FIN-005:** Premium offerings must not degrade free users.
- **NG-FIN-006:** Earmarked funds are managed according to their purpose.
- **NG-FIN-007:** Transparent management of donations and grants.
- **NG-FIN-008:** Commercial B2B services do not compromise independence.
- **NG-FIN-009:** Focus on sustainability rather than maximum monetization.
- **NG-FIN-010:** The structure permanently secures the social purpose.

## API, liidesed ja suhtlusarhitektuur (WP 1.11.3)

Süsteemi stabiilsuse, turvalisuse ja skaleeritavuse tagamiseks järgib Nexus Gaja rangelt API-põhist ja sündmustepõhist arhitektuuri.

### Põhiprintsiibid
- **Otsene juurdepääs andmebaasile puudub:** komponendid suhtlevad ainult määratletud liideste (API-de või sündmuste) kaudu, mitte kunagi muude teenuste otseste andmebaasipäringute kaudu.
- **API lüüs:** kõik välised kliendipäringud suunatakse läbi API lüüsi, mis käsitleb autentimist, marsruutimist ja kiiruse piiramist.
- **Pakkuja abstraktsioon:** välisteenused (AI mudelid, makseteenuse pakkujad, tõlkemootorid) on integreeritud abstraktsioonikihtide kaudu, vältides kodeeritud sõltuvusi ja võimaldades pakkujate paindlikku vahetamist.

### Suhtlusmustrid
- **Sünkroonsed API-d (REST/HTTPS):** kasutatakse koheste päringute jaoks, nagu sisselogimine, profiiliseaded või otsetõlked.
- **Asünkroonsed sündmused (sündmussiin):** Nexus Gaja kesknärvisüsteem viivitatud ja lahtiühendatud töötlemiseks (nt sõnum.Loodud, mis käivitab asünkroonselt modereerimise, tõlkimise ja teavituse).
- **Reaalajas (WebSocket):** spetsiaalsed kanalid otsevestluse ja tippimise indikaatorite jaoks.

### Turvalisus ja töökindlus
- **Null-usaldusmudel:** sisevõrgu liiklust ei usaldata automaatselt; tundlik teenustevaheline suhtlus nõuab autentimist.
- **Idempotency & Outbox Pattern:** kriitilised toimingud (nt annetused või sõnumid) on kavandatud olema idempotentsed, et vältida topelttöötlust, kasutades Väljundkausta mustrit, et sündmused ei läheks kunagi kaduma isegi andmebaasi tehingute ajal.

## MVP domeenimudel (WP 1.12)

Nexus Gaja kasutab rangelt domeenipõhist MVP-arhitektuuri (ADR-025), mis on kujundatud selgete domeenipiiridega modulaarse monoliidina. See struktuur hoiab ära mikroteenuse enneaegse keerukuse, säilitades samas paindlikkuse konkreetsete domeenide hilisemaks eraldamiseks.

### Põhidomeeni üksused
Arhitektuur eraldab selgesõnaliselt erinevad mõisted, et tagada andmete terviklikkus ja vältida struktuurseid lõkse, nagu "Kasutajanimi = inimene":
- **Isik ja kontod:** „Isik” ≠ „Kasutajakonto” ≠ „Identiteedi kinnitamine”. Kinnitatud isik osaleb konto kaudu, kuid olemid jäävad eraldiseisvaks.
- **Suhtlus:** "Sõnum" ≠ "Tõlge". Algne sõnum jääb muutumatuks; tõlked on lingitud üksused.
- **Modereerimine:** "Teavita" ≠ "Modereerimisotsus". Aruanne on lihtsalt nõue; uurimist viib läbi modereerimisjuhtum.
- **Finantsid:** "Annetus" ≠ "Fondide saldo". Maksed broneeritakse muutumatu pearaamatu kaudu fondi, tagades finantsläbipaistvuse.

### Ühendatud domeenid
Süsteem on jagatud selgeteks loogilisteks valdkondadeks (piiratud kontekstid): identiteet, konto, organisatsioon, suhtlus, kogukond, keel, modereerimine, teavitamine, rahandus ja juhtimine. Need domeenid kaardistavad kogu teekonna pärismaailma üksustest (kasutajad, koolid, valitsusvälised organisatsioonid) nende digitaalse suhtluse ja sellega seotud valitsemiseni.

## Projekti olek
Projekt on hetkel aktiivses arhitektuuri- ja planeerimisfaasis.
Käimasolevad arhitektuuriotsused dokumenteeritakse kaustas "/docs".