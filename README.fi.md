# Nexus Gaja

![Nexus Gaja -logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** on älykäs, kontekstiherkkä viestintäverkko, joka on suunniteltu mullistamaan globaali viestintä.

## Tarkoitus ja visio

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

Globalisoituneessa maailmassa kieli on usein suurin este. Nexus Gajan päätavoite on mahdollistaa saumaton, esteetön ja kontekstitarkka kommunikointi ihmisten välillä riippumatta siitä, puhuvatko he yhteistä kieltä.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Mahdollisuudet ja ominaisuudet
- **Multimediaviestintä**: Järjestelmä käsittelee tekstin lisäksi myös kuvaa, ääntä ja videota. Tämä mahdollistaa täysin mukaansatempaavien keskustelujen (esim. videopuhelut tai ääniviestit) reaaliajassa yli kielimuurien.
- **Kontekstiherkkyys**: Ironian, idiomien, ammattislangin ja alueellisten murteiden tunnistaminen, jotka perinteiset kääntäjät usein ymmärtävät väärin.
- **Cross-Platform Network**: toimii perustana yksityisille chateille, foorumisäikeille (kommentteja sisältävät viestit) ja maailmanlaajuiselle yhteisön vuorovaikutukselle.

---

## Tekninen arkkitehtuuri (ydinkonsepti)

![Nexus Gaja -käännöskonsepti](assets/img/nexus_translation.jpg)

Nexus Gajan tekninen ydin on räätälöity viestintämalli, joka on jaettu tiukasti kolmeen kerrokseen:

1. **Alkuperäinen**: Lähettäjän luoma viestintäobjekti (viesti) pysyy aina muuttumattomana.
2. **Semanttinen tulkinta**: Järjestelmä analysoi sanojen lisäksi niiden todellisen merkityksen.
3. **Kohdekielen esitys**: Tekoäly luo vain väliaikaisen tai välimuistissa olevan esityksen alkuperäisestä vastaavalle vastaanottajalle tämän ensisijaisen kielen perusteella. Käännökset eivät koskaan korvaa alkuperäistä viestiä.

### Kontekstiriippuvuus
Nexus Gajan käännökset eivät koskaan katso viestejä erillään. Moottori ottaa huomioon koko hierarkian:
"Viesti" → "Edelliset viestit" → "Käiekonteksti" → "Yhteisön konteksti" → "Kieli/alue" → "Käyttäjäasetukset"

### Tehokkuus on-demand-käännöksen avulla
Käännös tapahtuu resurssitehokkaasti vain **pyynnöstä** (On-Demand). Kun käyttäjä pyytää sisältöä, se käännetään hänen ennalta määritetylle kielelle. Kun käännös tietylle kielelle on luotu, se tallennetaan pysyvästi (välimuistiin), jotta tulevia pyyntöjä voidaan nopeuttaa huomattavasti.

## AI-avusteinen moderointi (WP 1.8.4)

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

Tekoälyavusteisella moderaatiolla otamme merkittävän askeleen tuoteideasta tekniseen arkkitehtuuriin ottaen huomioon nykyiset EU-säädökset (EU AI-lain avoimuusvaatimukset 50 artiklan nojalla; digitaalipalvelulaki ymmärrettävin perusteluin ja valitusmahdollisuuksin).

### 1. Perusperiaate
Tärkein lause arkkitehtuurille on: **Moderointi-AI on tarkistusjärjestelmä, ei autonominen päätösjärjestelmä.**
Se on suunniteltu auttamaan ihmisiä kohtuudella, ei määrittämään itse, mitkä mielipiteet Nexus Gajasta saavat olla.
Erotamme kolme tasoa:
- **Havainto:** "Tässä saattaa olla sääntörikkomus."
- **Arviointi:** "Sääntörikkomuksen todennäköisyys on esimerkiksi 94 %."
- **Päätös:** "Mihin toimiin todellisuudessa ryhdytään?"
Kolmannen tason on oltava ihmisen hallinnassa vaikeissa tapauksissa.

### 2. Moderation AI alijärjestelmänä
Yhden tekoälyn sijaan perustetaan vankka alijärjestelmä:
``` tekstiä
                 NEXUS GAJA AI MODERATION
                          │
       ┌─────────────────┼─────────────────-
       │ │ │
  Kieli AI Turvallisuus AI-petos AI
       │ │ │
       ├──────────────┬───┴─────────────────-
       │ │ │
 Käännöskäyttäytymisidentiteetti
 Analyysi Analyysisignaalit
       │ │ │
       └──────────────┼────────────────────
                      ▼
               Riskinarviointi
                      │
                      ▼
               Human Review
```

### 3. Tärkeimmät AI-moduulit
Nexus Gaja hyödyntää yhdeksää erikoistunutta analyysialuetta:
- **M1 – Kielen ymmärtäminen**: Havaitsee kielen, murteen, slangin, ironian ilmaisimet ja käännösongelmat.
- **M2 – Myrkyllisyyden / väärinkäytön havaitseminen**: Havaitsee loukkaukset, henkilökohtaiset hyökkäykset ja häirinnän.
- **M3 – Uhkien havaitseminen**: Havaitsee mahdolliset uhkaukset, kiristyksen ja väkivaltailmoitukset.
- **M4 – Vihan / epäinhimillisyyden tunnistus**: Havaitsee kohdistettuja hyökkäyksiä ihmisiin tiettyjen sidosryhmien perusteella.
- **M5 – Roskapostin/manipuloinnin tunnistus**: Havaitsee roskapostin, botin toiminnan ja koordinoidun manipuloinnin.
- **M6 – Petoksen havaitseminen**: Havaitsee epäilyttävät petosyritykset, tietojenkalastelut ja manipuloinnin.
- **M7 – Identity Integrity**: Tarkistaa signaalit tilin haltuunotosta, useista tileistä ja kiellon kiertämisestä.
- **M8 – Media Safety**: Analysoi kuvia, ääntä, videota, asiakirjoja.
- **M9 – Context Engine**: Tärkein moduuli. Se yhdistää yksittäiset havainnot.

### 4. Miksi kontekstimoottori on ratkaisevan tärkeä
Pelkkä avainsanahaku ei riitä. "Voisin tappaa hänet nauramasta" sisältää semanttisesti väkivaltaa, mutta on puhetta. "Huomenna klo 20 ammun hänet hänen talonsa edessä" on täysin erilainen tilanne. Tekoälyn on ymmärrettävä, mitä lausunto tarkoittaa erityisessä kontekstissaan.

### 5. Monikielinen moderointi
Kohtuullisuus ei voi vain verrata sanoja. Sen on analysoitava semanttinen taso (esim. saksalaiset idiomit vs. japanilaiset idiomit vs. alueelliset ilmaisut).

### 6. Alkuperäinen kieli + käännös
Alkuperäinen ja käännös analysoidaan erikseen. Vasta sitten suoritetaan "Yhdistetty moderoinnin arviointi". Näin Nexus Gaja voi määrittää, onko itse käännös saattanut eskaloida tai muuttaa tosiasioita.

### 7. Luottamuspisteet
Jokainen tekoälyarviointi saa luottamuspisteen (esim. Uhan todennäköisyys: 0,96). Kuitenkin: **Luottamuspisteet ≠ Totuus.** 96 %:n pistemäärä tarkoittaa vain, että malli on erittäin varma luokittelustaan, ei välttämättä sitä, että käyttäjä on syyllinen.

### 8. Epävarmuus muuttuu signaaliksi itsekseen
Jos tekoäly on epävarma (esim. uhka: 0,62, satiiri: 0,54), se ei saa vain pakottaa voimaan ankaria sääntöjä. Sen sijaan epävarmuus on rakennettu suoraan arkkitehtuuriin: **Human Review Required**.

### 9. Neljä päätösaluetta
- 🟢 **VIHREÄ**: Hyvin todennäköisesti yhteensopiva. → ei toimintaa.
- 🟡 **KELTAINEN**: Mahdollinen rikkomus. → tarkkaile / anna tarvittaessa varoitus.
- 🟠 **ORANSI**: Todennäköinen rikkomus. → moderointiarvostelu.
- 🔴 **PUNAINEN**: Mahdollinen vakava rikkomus. → välitön suojatoimenpide + ihmisen tarkastelu.

### 10. Ei "AI-rangaistusta"
**Tekoäly ei määrää lopullisia sanktioita.** Se voi käynnistää teknisiä välittömiä toimenpiteitä (esim. tilapäisesti lykätä viestiä) vakavien turvallisuusongelmien vuoksi, mutta lopullinen päätös on edelleen tarkistettavissa.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. Tekoälyn luoma sisältö
Erotamme: ihmisen luoma, tekoälyn avustama, tekoälyn luoma ja tekoälyn manipuloima. Tästä tulee osa sisällön metadataa.

### 15. Tekoälysisällön ja tekoälyn alkuperäkerroksen merkitseminen
EU:n tekoälylain (voimassa elokuussa 2026) läpinäkyvyyssääntöjen mukaan tekoälyn luoman sisällön on oltava tunnistettavissa. Tarjoamme tekoälyn alkuperäkerroksen, joka tallentaa metatiedot (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
Arkkitehtuuri pyrkii havaitsemaan synteettiset kuvat, kloonatut äänet ja syväväärennökset. Havaitseminen ei kuitenkaan ole automaattisesti todiste.

### 17. Ei automaattista "Truth Machine" (Moderaatio ≠ Faktantarkistus)
Yksi järjestelmä tarkistaa: "Rikkooko sisältö sääntöjä?" (Sisällön moderointi), toinen tarjoaa: "Mitä tietoja ja lähteitä on saatavilla?" (Tietoapu). Mielipiteitä ei vain poisteta "väärien" vuoksi.

### 18. Suojaus kulttuurisilta väärintulkinnoilta
Tekoäly edellyttää **Cultural Context Models** -mallia, jotta yhden maan viestintänormeja ei pidettäisi globaalina standardina.

### 19. Ironiaa, satiiria ja huumoria
Tekoäly käyttää kontekstia, hymiöitä, keskusteluhistoriaa ja tunnettuja ironiarakenteita, mutta sen on sallittava epävarmuus, kun merkitykset ovat moniselitteisiä.

### 20. Ei rangaistusta yksittäisen tekoälypisteen perusteella
Mikään vakava moderointi ei saa perustua vain yhteen automatisoituun luokitustulokseen (teksti + konteksti + käyttäytyminen + kieli + media + sääntömoottori = riskinarviointi).

### 21. Käyttäjäkäyttäytymissignaalit ja ei sosiaalista luottojärjestelmää
Tämä liittyy teknisiin väärinkäyttösignaaleihin (esim. joukkoroskapostiviestiin), ei yleiseen sosiaaliseen luokitusjärjestelmään. Nexus Gaja ei ylläpidä sosiaalista luottojärjestelmää – maltillisuus palvelee turvallisuutta, ei ihmisen arvon arviointia.

### 22. Kohtuullisen tekoälyn on oltava auditoitavissa
Kaikki asiaankuuluvat automaattiset päätökset kirjataan lokiin (tapahtumatunnus, sääntötunnus, luottamus, ihmisen tarkistus jne.) jäljitettävyyden varmistamiseksi.

### 23. Väärät positiiviset, väärät negatiivit ja laatumittarit
Virhetyyppejä valvotaan. Kojelauta mittaa tarkkuutta, palautusta ja erityisesti **valituksen peruutusprosenttia** (onnistuneiden valitusten määrä).

### 24. Language Equity & Translation Bias
Valvonnan laadun on oltava vertailukelpoinen kaikilla tuetuilla kielillä (Multilingual Moderation Benchmark). Jos moderoinnin tulokset eroavat alkuperäisen ja käännöksen välillä (käännösristiriita), tämä on tarkastettava erikseen.

### 25. Architecture Proposal & Policy Engine
Sääntöjä (Policy Engine) ei ole koodattu tekoälymalleihin. Tekoäly tarjoaa havaintoja; Policy Engine päättää nykyisten sääntöjen perusteella. Tämä mahdollistaa **mallimuutokset ilman sääntömuutoksia**.

### 26. Ihminen on lopullinen auktoriteetti
- **NG-AI-MOD-001**: Tekoäly auttaa havaitsemisessa ja luokittelussa, mutta ei korvaa ihmisen suorittamaa tarkastelua vakavissa päätöksissä.
- **NG-AI-MOD-002**: Automaattisten valvontapäätösten on oltava jäljitettävissä, kirjattavissa ja todennettavissa.

**Yhteenveto**: Rakennamme nelivaiheista järjestelmää: tekoälyn havaitseminen, konteksti- ja riskianalyysi, politiikkamoottori ja inhimillinen hallinto. Tämä mahdollistaa vahvan automaation luomatta vaarallista "AI tuomarina" -arkkitehtuuria.

## Rahoitusperiaatteet ja tulomalli (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

Nexus Gajaan sovelletaan erittäin tärkeää taloudellista periaatetta: **Ei perinteistä mainontaa alustassa.**
Tämä erottaa Nexus Gajan pohjimmiltaan monista tämän päivän sosiaalisista verkostoista. Tämä ei kuitenkaan tarkoita, että Nexus Gaja ei voisi olla kaupallinen luonne. Päinvastoin alustan on oltava taloudellisesti kannattava, jotta sen sosiaalinen tarkoitus kestää. Taloudellinen toiminta on keino saavuttaa päämäärä, ei alustan ensisijainen tarkoitus.

### 1. Principle NG-FIN-001
Nexus Gaja finances its operations through transparent revenue streams separated from user interests, and not through the monetization of its users' attention or personal data.

### 2. Ei perinteistä mainontaa
Erityisesti kiellettyjä ovat:
- Bannerimainokset
- Ponnahdusikkunamainokset
- Automaattisesti toistuvat videomainokset
- Sponsoroidut viestit vakiosyötteessä
- Henkilökohtaiset mainosprofiilit
- Käyttäjäprofiilien tai henkilötietojen myynti
- Yksityisistä keskusteluista johdettu mainonta.

Nexus Gaja on edelleen **viestintätila mainostilan sijaan**.

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

#### Pillar 4 – Donations
The **Nexus Gaja Funding Pool** accepts general and earmarked donations (e.g., "for international youth communication"). A **Fund Allocation Ledger** ensures transparent allocation of funds.
**Purpose Fund & Tombola:** A portion of donations feeds a pool for free/discounted usage. A lottery/tombola mechanism can allocate these funds transparently and auditably.

#### Pillar 5 – Institutional Funding
Foundations, cultural funding programs, or state programs.
**NG-FIN-002:** Financial support does not buy editorial or technical control (Independence).

#### Pillar 6 – Commercial Services
B2B services like **Translation-as-a-Service** (API), organizational communication, or international conference rooms, without burdening the standard user feed.

### 4. Ei tietojen kaupallistamista ja valvontataloutta
**NG-FIN-003:** Henkilökohtaiset käyttäjätiedot eivät ole hyödyke. Ei luetteloiden, profiilien tai historian myyntiä. Nexus Gaja ei hyödy psykologisesta valvonnasta (Surveillance Economy).

### 5. Taloudellinen läpinäkyvyys ja rahastorekisteri
**Nexus Gaja Financial Transparency:** Koottujen rahoitusrakenteiden julkaiseminen. Korvamerkityille lahjoituksille tehdään tekninen kirjanpito (rahastotunnus → tarkoitus → saldo → kohdentaminen). Ei ristiinsubventointia sosiaalisiin tarkoituksiin yritysmarkkinointiin.

### 6. Solidaarisuuteen perustuva rahoitusmalli
Hinnoittelu perustuu kustannuslähtöisyyteen, oikeudenmukaisuuteen ja solidaarisuuteen.
**Solidarity Premium:** Premium-käyttäjien vapaaehtoinen vaihtoehto rahoittaa osan toisen käyttäjän käyttöoikeuksista. Pakkosolidaarisuus tai premium-luokan yhteiskunta (vähemmän kunnioitusta/malttia ilmaisia ​​käyttäjiä kohtaan) on ehdottomasti kielletty.

### 7. Taloudelliset KPI:t sitoutumistalouden sijaan
Ei riippuvuutta käyttäjien pitämisestä "online-tilassa niin kauan kuin mahdollista" (ei raivosyöttiä, loputtomat syötteet).
Sen sijaan käytämme mittareita, kuten:
- **Global Communication Index (GCI):** Onnistuneet kommunikaatiosuhteet eri kieli-/kulttuurialueilta tulevien ihmisten välillä.
- **Alustan kestävyyssuhde (PSR):** Toistuvat tulot / toistuvat käyttökustannukset (tavoite ≥ 1).

### 8. Mitä emme nimenomaisesti halua (negatiivinen luettelo)
Nexus Gajaa **ei** rahoita:
❌ Henkilötietojen myynti
❌ Henkilökohtaista perinteistä mainontaa
❌ Käyttäjien käyttäytymisen seuranta mainontatarkoituksiin
❌ Yksityisten viestintätietojen myynti
❌ Piilotettu AI-datan käyttö
❌ Manipulatiiviset Premium-maksumuuret
❌ Kaupallistamisen keinotekoinen kattavuusrajoitus
❌ Maksettu poliittinen vaikutusvalta
❌ Etuoikeutettujen moderointipäätösten ostaminen.

### 9. Alustava rahoitusarkkitehtuuri
``` tekstiä
                         NEXUS GAJA
                              │
             ┌────────────────┼───────────────
             │ │ │
             ▼ ▼ ▼
          KÄYTTÄJIEN ORGANISAATIOT YRITYS
             │ │ │
             └────────────────┼──────────────────
                              │
                       ALUSTAPALVELUT
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       PREMIUM DONATIONS -sovellusliittymä
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               YLEISRAHASTON RAJOITETTU VARAS
                                        │
                                        ▼
                                  SOSIAALINEN TARKOITUS
```

### Yhteenveto rahoitusperiaatteista (NG-FIN)
- **NG-FIN-001:** Ei rahoitusta perinteisen mainonnan kautta.
- **NG-FIN-002:** Ei toimituksellista/teknistä valvontaa taloudellisen tuen kautta.
- **NG-FIN-003:** Henkilötiedot eivät ole hyödyke.
- **NG-FIN-004:** Perusviestintä on käytettävissä ilman maksua.
- **NG-FIN-005:** Premium-tarjoukset eivät saa heikentää ilmaisia ​​käyttäjiä.
- **NG-FIN-006:** Korvattuja varoja hallinnoidaan niiden käyttötarkoituksen mukaisesti.
- **NG-FIN-007:** Lahjoitusten ja apurahojen läpinäkyvä hallinta.
- **NG-FIN-008:** Kaupalliset B2B-palvelut eivät vaaranna riippumattomuutta.
- **NG-FIN-009:** Keskity kestävyyteen maksimaalisen kaupallistamisen sijaan.
- **NG-FIN-010:** Rakenne turvaa pysyvästi yhteiskunnallisen tarkoituksen.

## API, rajapinnat ja viestintäarkkitehtuuri (WP 1.11.3)

Järjestelmän vakauden, turvallisuuden ja skaalautuvuuden varmistamiseksi Nexus Gaja noudattaa tiukasti API-ensimmäistä ja tapahtumalähtöistä arkkitehtuuria.

### Perusperiaatteet
- **Ei suoraa tietokantakäyttöä:** Komponentit kommunikoivat yksinomaan määritettyjen liitäntöjen (API tai tapahtumat) kautta, eivät koskaan muiden palveluiden suorien tietokantakyselyjen kautta.
- **API-yhdyskäytävä:** Kaikki ulkoiset asiakaspyynnöt reititetään API-yhdyskäytävän kautta, joka käsittelee todennusta, reititystä ja nopeusrajoitusta.
- **Provider Abstraction:** Ulkoiset palvelut (AI-mallit, maksupalveluntarjoajat, käännöskoneet) on integroitu abstraktiokerrosten kautta, mikä välttää kovakoodatut riippuvuudet ja mahdollistaa joustavan palveluntarjoajan vaihdon.

### Viestintämallit
- **Synkroniset sovellusliittymät (REST/HTTPS):** Käytetään välittömiin pyyntöihin, kuten kirjautumiseen, profiiliasetuksiin tai suoriin käännöksiin.
- **Asynkroniset tapahtumat (tapahtumaväylä):** Nexus Gajan keskushermosto viivästettyyn ja irrotettuun käsittelyyn (esim. "Message.Created", joka laukaisee moderoinnin, kääntämisen ja ilmoituksen asynkronisesti).
- **Reaaliaikainen (WebSocket):** Omat kanavat live-chatille ja kirjoitusilmaisimille.

### Turvallisuus ja luotettavuus
- **Zero-Trust Model:** Sisäiseen verkkoliikenteeseen ei luoteta automaattisesti; herkkä palveluiden välinen viestintä vaatii todennusta.
- **Idempotency & Outbox Pattern:** Kriittiset toiminnot (kuten lahjoitukset tai viestit) on suunniteltu idempotenteiksi päällekkäisten käsittelyjen estämiseksi. Lähtevät-kuviota käytetään varmistamaan, että tapahtumat eivät koskaan katoa edes tietokantatapahtumien aikana.

## MVP-verkkotunnusmalli (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja käyttää tiukasti Domain-Driven MVP-arkkitehtuuria (ADR-025), joka on suunniteltu modulaariseksi monoliitiksi, jolla on selkeät toimialueen rajat. Tämä rakenne estää ennenaikaisen mikropalvelun monimutkaisuuden säilyttäen samalla joustavuuden jakaa tiettyjä alueita myöhemmin.

### Verkkoalueen ydinkokonaisuudet
Arkkitehtuuri erottaa selkeästi erilliset käsitteet varmistaakseen tietojen eheyden ja välttääkseen rakenteelliset sudenkuopat, kuten "Käyttäjänimi = ihminen":
- **Identiteetti ja tilit:** "Henkilö" ≠ "Käyttäjätili" ≠ "Identiteettivahvistus". Vahvistettu henkilö osallistuu tilin kautta, mutta entiteetit pysyvät erillisinä.
- **Viestintä:** "Viesti" ≠ "Käännös". Alkuperäinen viesti pysyy muuttumattomana; käännökset ovat linkitettyjä kokonaisuuksia.
- **Moderointi:** Raportti ≠ Valvontapäätös. Raportti on vain väite; maltillinen tapaus suorittaa tutkinnan.
- **Talous:** "Lahjoitus" ≠ "Rahasaldo". Maksut kirjataan muuttumattoman kirjanpidon kautta rahastoon, mikä varmistaa talouden läpinäkyvyyden.

### Yhdistetyt verkkotunnukset
Järjestelmä on jaettu selkeisiin loogisiin alueisiin (rajoitetut kontekstit): Identiteetti, tili, organisaatio, viestintä, yhteisö, kieli, moderointi, ilmoitus, talous ja hallinto. Nämä verkkotunnukset kartoittavat koko matkan reaalimaailman kokonaisuuksista (käyttäjät, koulut, kansalaisjärjestöt) heidän digitaaliseen vuorovaikutukseensa ja siihen liittyvään hallintoon.

## Projektin tila
Projekti on tällä hetkellä aktiivisessa arkkitehtuuri- ja suunnitteluvaiheessa.
Käynnissä olevat arkkitehtoniset päätökset dokumentoidaan "/docs"-kansioon.

---

---

## Lisenssi ja immateriaalioikeudet

> **© 2024–2026 Jan Sonner / SonnerStudio — Kaikki oikeudet pidätetään.**

**Nexus Gaja** on **SonnerStudion** alaisuudessa toimivan **Jan Sonnerin** yksinoikeudellinen immateriaalioikeus.

Jan Sonner on Nexus Gajan ainoa luoja, arkkitehti ja omistaja – mukaan lukien kaikki konseptit, arkkitehtuuri, verkkotunnusmallit, brändi-identiteetti ja siihen liittyvä dokumentaatio.

**Millään kolmannella osapuolella ei ole oikeuksia, lisenssejä tai omistusosuuksia** riippumatta niiden koosta, markkina-asemasta tai vaikutuksesta teknologiateollisuudessa.

### Mikä EI ole sallittua ilman nimenomaista kirjallista lupaa:
- Tämän ohjelmiston tai sen dokumentaation kopioiminen, jäljentäminen tai jakelu
- Muokkaa, mukauttaa tai luo johdannaisteoksia
- Nexus Gajan minkä tahansa osan kaupallinen käyttö
- Tämän arkiston sisällön käyttäminen AI- tai LLM-järjestelmien koulutustietona
- Alilisensointi tai oikeuksien siirtäminen kolmansille osapuolille

### Suojattu henkinen omaisuus
Seuraavat alkuperäiset konseptit on suojattu liikesalaisuuksina ja Jan Sonnerin omistusoikeudellisina luomina:
- Kerrosviestintämalli (alkuperäinen, semanttinen tulkinta, käännetty tulos)
- Henkilöllisyyden erotteluperiaate (henkilö ei ole tili ei ole henkilöllisyyden vahvistus)
- Viestin ja käännöksen irrotusmalli (viesti ei ole käännöstä)
- Tekoälyn moderoinnin hallintokehys

### Ota yhteyttä
Lisenssitiedustelut: https://github.com/SonnerStudio

Nexus Gaja ja Nexus Gaja -logo ovat Jan Sonnerin tavaramerkkejä. Nimen tai tuotemerkin luvaton käyttö on kielletty.

Katso täydelliset lisenssiehdot LICENSE-tiedostosta.
