# Nexus Gaja

![Nexus Gaja -logo](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** on älykäs, kontekstiherkkä viestintäverkko, joka on suunniteltu mullistamaan globaali viestintä.

## Tarkoitus ja visio
Globalisoituneessa maailmassa kieli on usein suurin este. Nexus Gajan päätavoite on mahdollistaa saumaton, esteetön ja kontekstitarkka kommunikointi ihmisten välillä riippumatta siitä, puhuvatko he yhteistä kieltä.

Kyse ei ole vain sanojen tiukasta kääntämisestä, vaan **merkityksen siirtämisestä**. Nexus Gaja yhdistää ihmiset syvemmällä tasolla ymmärtämällä kulttuurisia, alueellisia ja kontekstuaalisia vivahteita, mikä mahdollistaa aidon, autenttisen keskustelun.

## Mahdollisuudet ja ominaisuudet
- **Multimediaviestintä**: Järjestelmä käsittelee tekstin lisäksi myös kuvaa, ääntä ja videota. Tämä mahdollistaa täysin mukaansatempaavien keskustelujen (esim. videopuhelut tai ääniviestit) reaaliajassa yli kielimuurien.
- **Kontekstiherkkyys**: Ironian, idiomien, ammattislangin ja alueellisten murteiden tunnistaminen, jotka perinteiset kääntäjät usein ymmärtävät väärin.
- **Cross-Platform Network**: toimii perustana yksityisille chateille, foorumisäikeille (kommentteja sisältävät viestit) ja maailmanlaajuiselle yhteisön vuorovaikutukselle.

---

## Tekninen arkkitehtuuri (ydinkonsepti)

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
 Analysis         Analysis            Signals
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

### 11. Suojatoimenpiteet voivat tapahtua automaattisesti
Konkreettisen uhan sattuessa (Uhka havaittu → Korkea luottamus → Väliaikainen rajoitus → Ihmisten arviointi → Päätös) suojaamme uhattua käyttäjää muuttamatta tekoälyä tuomariksi.

### 12. Tekoälyn täytyy pystyä perustelemaan päätöksensä
DSA vaatii selkeitä ja erityisiä syitä. Tekoäly tarjoaa jäsennellyt perustelut: Sääntö (NG-CONDUCT-004), Havaittu (mahdollinen konkreettinen uhka), Luottamus (0,94), Asiaankuuluva konteksti (4 edellistä viestiä), Suositeltu toiminta (Human Review).

### 13. AI ei saa muuttaa sisältöä salaa
**Moderation AI ei saa koskaan muuttaa alkuperäistä sisältöä huomaamatta.** Automaattisen korjauksen, käännöksen tai yhteenvedon aikana alkuperäinen säilytetään aina.

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

## Projektin tila
Projekti on tällä hetkellä aktiivisessa arkkitehtuuri- ja suunnitteluvaiheessa.
Käynnissä olevat arkkitehtoniset päätökset dokumentoidaan "/docs"-kansioon.