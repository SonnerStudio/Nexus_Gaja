# Nexus Gaja

![Nexus Gaja embléma](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

A **Nexus Gaja** egy intelligens, környezetérzékeny kommunikációs hálózat, amelyet a globális kommunikáció forradalmasítására terveztek.

## Cél és jövőkép
A globalizált világban gyakran a nyelv jelenti a legnagyobb akadályt. A Nexus Gaja fő célja, hogy zökkenőmentes, akadálymentes és kontextus szerint pontos kommunikációt tegyen lehetővé az emberek között – függetlenül attól, hogy egy közös nyelvet beszélnek-e.

Nem csak a szavak merev fordításáról van szó, hanem a **jelentés átadásáról**. A Nexus Gaja mélyebb szinten köti össze az embereket azáltal, hogy megérti a kulturális, regionális és kontextuális árnyalatokat, és ezáltal valódi, hiteles beszélgetéseket tesz lehetővé.

## Lehetőségek és funkciók
- **Multimédia kommunikáció**: A rendszer nemcsak szöveget, hanem képeket, hangot és videót is feldolgoz. Ez lehetővé teszi a teljes mértékben magával ragadó beszélgetéseket (például videohívásokat vagy hangüzeneteket) valós időben, a nyelvi korlátok között.
- **Kontextusérzékenység**: Az irónia, az idiómák, a zsargon és a regionális nyelvjárások felismerése, amelyeket a hagyományos fordítók gyakran félreértenek.
- **Platformos hálózat**: Privát csevegések, fórumszálak (megjegyzéseket tartalmazó bejegyzések) és globális közösségi interakciók alapjául szolgál.

---

## Műszaki architektúra (alapkoncepció)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Eredeti**: A feladó által létrehozott kommunikációs objektum (üzenet) mindig változtathatatlan marad.
2. **Szemantikai értelmezés**: A rendszer nem csak a szavakat elemzi, hanem a tényleges jelentést is.
3. **Célnyelvi megjelenítés**: Az AI csupán ideiglenes vagy gyorsítótárazott reprezentációt hoz létre az eredetiről az adott címzett számára a preferált nyelv alapján. A fordítások soha nem írják felül az eredeti üzenetet.

### Kontextusfüggőség
A Nexus Gaja fordításai soha nem tekintik az üzeneteket elszigetelten. A motor figyelembe veszi a teljes hierarchiát:
"Üzenet" → "Korábbi üzenetek" → "Szálkörnyezet" → "Közösségi kontextus" → "Nyelv/régió" → "Felhasználói beállítások"

### Hatékonyság igény szerinti fordítással
A fordítás csak **kérésre** (igény szerint) történik erőforrás-hatékonyan. Amikor egy felhasználó tartalmat kér, azt lefordítják az előre beállított nyelvére. Amint egy adott nyelvre egy fordítást generált, azt véglegesen tárolja (gyorsítótárban), hogy drasztikusan felgyorsítsa a jövőbeni kéréseket.

## AI-asszisztált moderálás (WP 1.8.4)

Az AI-asszisztált moderációval jelentős lépést teszünk a termékötlettől a műszaki architektúráig, figyelembe véve a jelenlegi EU-szabályozást (az EU AI törvény 50. cikk szerinti átláthatósági követelményei; digitális szolgáltatásokról szóló törvény érthető indoklással és fellebbezési lehetőségekkel).

### 1. Alapelv
Az architektúra legfontosabb mondata: **A moderációs AI egy felülvizsgálati rendszer, nem pedig egy autonóm uralkodó rendszer.**
Úgy tervezték, hogy mértékkel segítse az embereket, nem pedig saját maga határozza meg, mely vélemények létezhetnek a Nexus Gaján.
Három szintet különböztetünk meg:
- ** Észlelés:** "Itt szabálysértés történt."
- **Kiértékelés:** "A szabálysértés valószínűsége például 94%.
- **Döntés:** "Mi a tényleges intézkedés?"
A harmadik szintet súlyos esetekben embernek kell irányítania.

### 2. A moderációs AI mint alrendszer
Egyetlen mesterséges intelligencia helyett egy robusztus alrendszer jön létre:
``` szöveg
                 NEXUS GAJA AI MODERÁCIÓ
                          │
       ┌─────────────────┼──────────────-
       │ │ │
  Nyelv AI biztonság AI csalás AI
       │ │ │
       ├-
       │ │ │
 Fordítási Viselkedés Identitás
 Elemzés Elemzési jelek
       │ │ │
       └──────────────┼───────────────────
                      ▼
               Kockázatértékelés
                      │
                      ▼
               Human Review
```

### 3. A legfontosabb AI-modulok
A Nexus Gaja kilenc speciális elemzési területet használ:
- **M1 – Nyelvértés**: Felismeri a nyelvet, a dialektust, a szlenget, az iróniát, a fordítási problémákat.
- **M2 – Toxicitás/visszaélés észlelése**: Érzékeli a sértéseket, személyes támadásokat, zaklatást.
- **M3 – Fenyegetés észlelése**: észleli a potenciális fenyegetéseket, zsarolásokat, erőszakos bejelentéseket.
- **M4 – Gyűlölet/dehumanizáció észlelése**: Érzékeli az emberek elleni célzott támadásokat meghatározott hovatartozás alapján.
- **M5 – Spam/Manipulation Detection**: Érzékeli a spamet, a bot viselkedését és az összehangolt manipulációt.
- **M6 – Csalásészlelés**: Felderíti a gyanús csalási kísérleteket, adathalászatot, közösségi manipulációt.
- **M7 – Identity Integrity**: Ellenőrzi a fiókok átvételére, több fiókra és a kitiltásra vonatkozó jelzéseket.
- **M8 – Médiabiztonság**: Képek, hang, videó, dokumentumok elemzése.
- **M9 – Context Engine**: A legfontosabb modul. Összevonja az egyes leleteket.

### 4. Miért fontos a Context Engine?
A puszta kulcsszavas keresés nem lenne elegendő. „Megölhetném őt a nevetéstől” szemantikailag erőszakot tartalmaz, de csak beszéd. "Holnap este 8-kor lelövöm a háza előtt" teljesen más helyzet. Az AI-nak meg kell értenie, mit jelent az állítás a sajátos kontextusában.

### 5. Többnyelvű moderálás
A mértékkel nem lehet egyszerűen összehasonlítani a szavakat. Elemeznie kell a szemantikai szintet (pl. német idiómák kontra japán kifejezések vs. regionális kifejezések).

### 6. Eredeti nyelv + fordítás
Az eredetit és a fordítást külön elemezzük. Csak ezután kerül sor a „Kombinált moderációs értékelésre”. Ez lehetővé teszi a Nexus Gaja számára, hogy megállapítsa, hogy maga a fordítás fokozhatta-e vagy megváltoztatta-e a tényeket.

### 7. Magabiztossági pontszám
Minden mesterséges intelligencia értékelés megbízhatósági pontszámot kap (pl. fenyegetés valószínűsége: 0,96). Azonban: **Magabiztossági pontszám ≠ Igazság.** A 96%-os pontszám csak azt jelenti, hogy a modell nagyon biztos a besorolásában, nem feltétlenül azt, hogy a felhasználó bűnös.

### 8. A bizonytalanság önmagában is jelzé válik
Ha a mesterséges intelligencia bizonytalan (pl. fenyegetés: 0,62, szatíra: 0,54), nem szabad egyszerűen szigorú szabályokat érvényesíteni. Ehelyett a bizonytalanság közvetlenül beépül az architektúrába: **Emberi felülvizsgálat szükséges**.

### 9. Négy döntési zóna
- 🟢 **ZÖLD**: Nagy valószínűséggel kompatibilis. → nincs művelet.
- 🟡 **SÁRGA**: Lehetséges jogsértés. → figyelje / szükség esetén adjon figyelmeztetést.
- 🟠 **NARANCS**: Valószínű jogsértés. → moderálási áttekintés.
- 🔴 **PIROS**: Súlyos lehetséges szabálysértés. → azonnali védőintézkedés + emberi felülvizsgálat.

### 10. Nincs "AI-büntetés"
**Az AI nem szab ki végső szankciókat.** Súlyos biztonsági aggályok esetén azonnali technikai intézkedéseket indíthat el (például ideiglenesen visszatarthatja az üzenetet), de a végső döntés ellenőrizhető marad.

### 11. A védőintézkedések automatikusan megtörténhetnek
Konkrét fenyegetés esetén (Fenyegetés észlelve → Magas bizalom → Ideiglenes korlátozás → Emberi felülvizsgálat → Döntés) megvédjük a fenyegetett felhasználót anélkül, hogy az AI-t bíróvá alakítanánk.

### 12. Az AI-nak képesnek kell lennie arra, hogy igazolja döntéseit
A DSA világos és konkrét indokokat igényel. Az AI strukturált érvelést biztosít: Szabály (NG-CONDUCT-004), Észlelt (Potenciális konkrét fenyegetés), Magabiztosság (0,94), Releváns kontextus (Előző 4 üzenet), Javasolt intézkedés (Emberi felülvizsgálat).

### 13. Az AI nem változtathatja meg titokban a tartalmat
**A moderációs AI soha nem változtathatja meg észrevétlenül az eredeti tartalmat.** Az automatikus javítás, fordítás vagy összegzés során az eredetit mindig megőrzi.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Mélyhamisítás észlelése
Az architektúra célja szintetikus képek, klónozott hangok és mélyhamisítások észlelése. Az észlelés azonban nem automatikusan bizonyítja.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irónia, szatíra és humor
Az AI kontextust, hangulatjeleket, beszélgetési előzményeket és ismert iróniastruktúrákat használ, de lehetővé kell tennie a bizonytalanságot, ha a jelentések nem egyértelműek.

### 20. Nincs büntetés egyetlen AI-pontszám alapján
Semmilyen súlyos moderálási beavatkozás nem alapulhat kizárólag egyetlen automatizált besorolási eredményen (Szöveg + Kontextus + Viselkedés + Nyelv + Média + Szabálymotor = Kockázatértékelés).

### 21. Felhasználói viselkedési jelzések és nincs szociális kreditrendszer
Ez a technikai visszaélésekre utaló jelekre (pl. tömeges spamküldésre) vonatkozik, nem pedig egy általános közösségi minősítési rendszerre. A Nexus Gaja nem tart fenn társadalmi kreditrendszert – a mértékletesség a biztonságot szolgálja, nem pedig az ember értékének felmérését.

### 22. A moderált mesterséges intelligencia auditálhatónak kell lennie
A nyomon követhetőség biztosítása érdekében minden releváns automatizált döntés naplózásra kerül (Eseményazonosító, Szabályazonosító, Bizalom, Human-Review stb.).

### 23. Hamis pozitívumok, hamis negatívumok és minőségi mutatók
A hibatípusokat figyelik. Az irányítópult a pontosságot, a visszahívást és különösen a **fellebbezés visszavonási arányát** (a sikeres fellebbezések számát) méri.

### 24. Language Equity & Translation Bias
A moderálás minőségének összehasonlíthatónak kell lennie az összes támogatott nyelven (Multilingual Moderation Benchmark). Ha a moderálás eredménye eltér az eredeti és a fordítás között (fordítási konfliktus), akkor ezt külön felül kell vizsgálni.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. Az Ember marad a végső hatóság
- **NG-AI-MOD-001**: A mesterséges intelligencia segít az észlelésben és az osztályozásban, de nem helyettesíti a súlyos döntések emberi felülvizsgálatát.
- **NG-AI-MOD-002**: Az automatizált moderálási döntéseknek nyomon követhetőnek, naplózhatónak és ellenőrizhetőnek kell lenniük.

**Összefoglaló**: Négy szakaszból álló rendszert építünk: AI-észlelés, kontextus- és kockázatelemzés, irányelvmotor és emberi kormányzás. Ez erős automatizálást tesz lehetővé veszélyes „AI mint bíró” architektúra létrehozása nélkül.

## Projekt állapota
A projekt jelenleg az aktív építészeti és tervezési fázisban van.
A folyamatban lévő építészeti döntések a „/docs” mappában vannak dokumentálva.