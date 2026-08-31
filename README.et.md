# Nexus Gaja

![Nexus Gaja logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** on intelligentne kontekstitundlik sidevõrk, mis on loodud globaalse suhtluse revolutsiooni muutmiseks.

## Eesmärk ja visioon
Globaliseeruvas maailmas on keel sageli suurim takistus. Nexus Gaja põhieesmärk on võimaldada inimeste vahel sujuvat, takistusteta ja kontekstuaalselt täpset suhtlust olenemata sellest, kas nad räägivad ühist keelt.

Asi pole ainult sõnade jäigas tõlkimises, vaid **tähenduse ülekandmises**. Nexus Gaja ühendab inimesi sügavamal tasandil, mõistes kultuurilisi, piirkondlikke ja kontekstuaalseid nüansse, võimaldades seeläbi ehedaid ja autentseid vestlusi.

## Võimalused ja funktsioonid
- **Multimeediumisuhtlus**: süsteem töötleb mitte ainult teksti, vaid ka pilti, heli ja videot. See võimaldab reaalajas täielikult kaasahaaravaid vestlusi (nt videokõnesid või häälsõnumeid) üle keelebarjääride.
- **Kontekstitundlikkus**: iroonia, idioomide, žargooni ja piirkondlike dialektide äratundmine, millest tavalised tõlkijad sageli valesti aru saavad.
- **Platvormideülene võrk**: toimib privaatvestluste, foorumite lõimede (kommentaaridega postituste) ja ülemaailmse kogukonna suhtluse alusena.

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

## AI-abiga modereerimine (WP 1.8.4)

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. Põhiprintsiip
Arhitektuuri jaoks on kõige olulisem lause: **Modereerimise AI on ülevaatesüsteem, mitte autonoomne valitsemissüsteem.**
See on loodud inimeste abistamiseks mõõdukalt, mitte ise määrama, millised arvamused on Nexus Gajas lubatud.
Me eristame kolme taset:
- **Tuvastamine:** "Siin võib olla reeglite rikkumine."
- **Hindamine:** "Reegli rikkumise tõenäosus on näiteks 94%.
- **Otsus:** "Mis toimingut tegelikult tehakse?"
Kolmandat taset peab rasketel juhtudel juhtima inimene.

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

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI ei tohi sisu salaja muuta
**Mõõdukas tehisintellekt ei tohi kunagi algset sisu märkamatult muuta.** Automaatse parandamise, tõlkimise või kokkuvõtte tegemise ajal säilitatakse alati originaal.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

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

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Kokkuvõte**: ehitame neljaetapilise süsteemi: tehisintellekti tuvastamine, konteksti- ja riskianalüüs, poliitikamootor ja inimjuhtimine. See võimaldab tugevat automatiseerimist ilma ohtlikku "AI kui kohtuniku" arhitektuuri looma.

## Projekti olek
Projekt on hetkel aktiivses arhitektuuri- ja planeerimisfaasis.
Käimasolevad arhitektuuriotsused dokumenteeritakse kaustas "/docs".