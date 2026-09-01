# Nexus Gaja

![Nembo ya Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** ni mtandao wa mawasiliano wenye akili, unaozingatia muktadha ulioundwa kuleta mageuzi katika mawasiliano ya kimataifa.

## Kusudi na Maono
Katika ulimwengu wa utandawazi, lugha ndio kikwazo kikubwa zaidi. Lengo kuu la Nexus Gaja ni kuwezesha mawasiliano ya watu bila vikwazo, bila vikwazo, na kimuktadha—bila kujali kama wanazungumza lugha ya kawaida.

Siyo tu kuhusu kutafsiri maneno kwa ukali, lakini kuhusu **kuhamisha maana**. Nexus Gaja huunganisha watu kwa undani zaidi kwa kuelewa nuances za kitamaduni, kimaeneo, na kimuktadha, hivyo basi kuwezesha mazungumzo ya kweli na ya kweli.

## Uwezekano na Vipengele
- **Mawasiliano ya Multimedia**: Mfumo huchakata sio maandishi tu, bali pia picha, sauti na video. Hii inaruhusu mazungumzo ya kina kabisa (k.m., simu za video au ujumbe wa sauti) katika muda halisi katika vizuizi vya lugha.
- **Usikivu wa Muktadha**: Utambuzi wa kejeli, nahau, jargon, na lahaja za kieneo ambazo mara nyingi hazieleweki vibaya na watafsiri wa kawaida.
- **Mtandao wa Mfumo Mtambuka**: Hutumika kama msingi wa mazungumzo ya faragha, mazungumzo ya mijadala (machapisho yenye maoni), na mwingiliano wa jumuiya duniani kote.

---

## Usanifu wa Kiufundi (Dhana ya Msingi)

Msingi wa kiufundi wa Nexus Gaja ni modeli ya mawasiliano iliyoundwa maalum ambayo imegawanywa kikamilifu katika tabaka tatu:

1. **Asili**: Kitu cha mawasiliano (ujumbe) kilichoundwa na mtumaji daima hubaki kuwa kisichobadilika.
2. **Tafsiri ya Semantiki**: Mfumo hauchanganui maneno tu, bali maana halisi.
3. **Uwakilishi wa Lugha Lengwa**: AI huunda tu uwakilishi wa muda au uliohifadhiwa wa asili kwa mpokeaji husika kulingana na lugha anayopendelea. Tafsiri haziwahi kubatilisha ujumbe asili.

### Utegemezi wa Muktadha
Tafsiri katika Nexus Gaja kamwe hazioni ujumbe kwa kutengwa. Injini inazingatia uongozi mzima:
`Ujumbe` → `Ujumbe Uliotangulia` → `Muktadha wa Mazungumzo` → `Muktadha wa Jumuiya` → `Lugha / Eneo` → `Mapendeleo ya Mtumiaji`

### Ufanisi kupitia Tafsiri Unapohitaji
Tafsiri hutokea kwa ufanisi wa rasilimali tu **kwa ombi** (Inapohitajika). Mtumiaji anapoomba maudhui, hutafsiriwa katika lugha yao iliyowekwa awali. Mara tafsiri ya lugha mahususi inapotolewa, huhifadhiwa kabisa (caching) ili kuharakisha maombi ya siku zijazo.

## Usaidizi wa Kudhibiti AI (WP 1.8.4)

Kwa Kudhibiti Usaidizi wa AI, tunachukua hatua muhimu kutoka kwa wazo la bidhaa hadi usanifu wa kiufundi, kwa kuzingatia kanuni za sasa za Umoja wa Ulaya (mahitaji ya uwazi ya Sheria ya EU AI chini ya Sanaa. 50; Sheria ya Huduma za Dijitali yenye uhalali unaoeleweka na chaguo za kukata rufaa).

### 1. Kanuni ya Msingi
Sentensi muhimu zaidi kwa usanifu ni: **Ukadiriaji AI ni mfumo wa mapitio, sio mfumo wa kutawala unaojitegemea.**
Imeundwa kusaidia wanadamu kwa kiasi, sio kujiamua ni maoni gani yanaruhusiwa kuwepo kwenye Nexus Gaja.
Tunatofautisha kati ya viwango vitatu:
- **Ugunduzi:** "Kunaweza kuwa na ukiukaji wa sheria hapa."
- **Tathmini:** "Uwezekano wa ukiukaji wa sheria ni, kwa mfano, 94%.
- **Uamuzi:** "Ni hatua gani hasa inachukuliwa?"
Ngazi ya tatu lazima kudhibitiwa na binadamu katika kesi kali.

### 2. The Moderation AI as a Subsystem
Instead of a single AI, a robust subsystem is established:
```text
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──────────────────┐
       │                  │                  │
  Language AI        Safety AI          Fraud AI
       │                  │                  │
       ├──────────────┬───┴──────────────┬───┤
       │              │                  │
 Translation      Behaviour          Identity
 Analysis         Analysis            Signals
       │              │                  │
       └──────────────┼──────────────────┘
                      ▼
               Risk Assessment
                      │
                      ▼
               Human Review
```

### 3. The Most Important AI Modules
Nexus Gaja utilizes nine specialized analysis areas:
- **M1 – Language Understanding**: Detects language, dialect, slang, irony indicators, translation issues.
- **M2 – Toxicity / Abuse Detection**: Detects insults, personal attacks, harassment.
- **M3 – Threat Detection**: Detects potential threats, blackmail, violence announcements.
- **M4 – Hate / Dehumanization Detection**: Detects targeted attacks on people based on specific affiliations.
- **M5 – Spam / Manipulation Detection**: Detects spam, bot behavior, coordinated manipulation.
- **M6 – Fraud Detection**: Detects suspicious fraud attempts, phishing, social engineering.
- **M7 – Identity Integrity**: Checks signals regarding account takeovers, multiple accounts, ban evasion.
- **M8 – Media Safety**: Analyzes images, audio, video, documents.
- **M9 – Context Engine**: The most important module. It merges the individual findings.

### 4. Why the Context Engine is Crucial
A pure keyword search would be insufficient. "I could kill him from laughing" semantically contains violence but is a figure of speech. "Tomorrow at 8 PM I will shoot him in front of his house" is a completely different situation. The AI must understand what the statement means in its specific context.

### 5. Udhibiti wa Lugha nyingi
Kiasi haiwezi tu kulinganisha maneno. Ni lazima ichanganue kiwango cha kisemantiki (k.m., nahau za Kijerumani dhidi ya nahau za Kijapani dhidi ya misemo ya kieneo).

### 6. Original Language + Translation
Original and translation are analyzed separately. Only then does the "Combined Moderation Assessment" take place. This allows Nexus Gaja to determine whether the translation itself may have escalated or altered the facts.

### 7. Confidence Score
Every AI evaluation receives a confidence score (e.g., Threat probability: 0.96). However: **Confidence Score ≠ Truth.** A score of 96% only means the model is highly certain of its classification, not necessarily that the user is guilty.

### 8. Kutokuwa na uhakika Kunakuwa Ishara Yenyewe
Ikiwa AI haina uhakika (k.m., Tishio: 0.62, Satire: 0.54), lazima isitekeleze tu sheria kali. Badala yake, kutokuwa na uhakika kunajengwa moja kwa moja kwenye usanifu: **Uhakiki wa Kibinadamu Unahitajika**.

### 9. Kanda Nne za Maamuzi
- 🟢 **KIJANI**: Kuna uwezekano mkubwa wa kutii. → hakuna hatua.
- 🟡 **MANJANO**: Ukiukaji unaowezekana. → kufuatilia / kutoa onyo ikiwa ni lazima.
- 🟠 **CHUNGWA**: Ukiukaji unaowezekana. → ukaguzi wa wastani.
- 🔴 **RED**: Ukiukaji mkubwa unaowezekana. → kipimo cha kinga cha haraka + mapitio ya binadamu.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Hatua za Kinga Inaweza Kutokea Kiotomatiki
Katika tukio la tishio halisi (Tishio limegunduliwa → Kujiamini kwa juu → Kizuizi cha muda → Mapitio ya kibinadamu → Uamuzi), tunalinda mtumiaji aliyetishiwa bila kugeuza AI kuwa hakimu.

### 12. AI Lazima Iweze Kuhalalisha Maamuzi Yake
DSA inahitaji sababu zilizo wazi na mahususi. AI hutoa hoja zilizopangwa: Kanuni (NG-CONDUCT-004), Imegunduliwa (Tishio halisi linalowezekana), Kujiamini (0.94), Muktadha husika (Ujumbe 4 Zilizotangulia), Hatua inayopendekezwa (Uhakiki wa kibinadamu).

### 13. AI Sipaswi Kubadilisha Maudhui kwa Siri
**AI ya Kudhibiti haipaswi kamwe kubadilisha maudhui asili bila kutambuliwa.** Wakati wa kusahihisha kiotomatiki, tafsiri, au muhtasari, asili huhifadhiwa kila mara.

### 14. Maudhui Yanayozalishwa na AI
Tunatofautisha kati ya: Iliyoundwa na binadamu, inayosaidiwa na AI, inayozalishwa na AI, na inayotumiwa na AI. Hii itakuwa sehemu ya metadata ya maudhui.

### 15. Uwekaji Lebo ya Maudhui ya AI na Tabaka la Maonyesho la AI
Kulingana na sheria za uwazi za Sheria ya EU AI (kuanzia Agosti 2026), maudhui yanayotokana na AI lazima yatambulike. Tunatoa Safu ya Mazoezi ya AI ambayo huhifadhi metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Utambuzi wa kina
Usanifu unalenga kugundua picha za sintetiki, sauti zilizoundwa na za kina. Walakini, kugundua sio uthibitisho wa kiotomatiki.

### 17. Hakuna "Mashine ya Ukweli" ya Kiotomatiki (Moderation ≠ Kukagua Ukweli)
Mfumo mmoja hukagua: "Je, maudhui yanakiuka sheria?" (Ukadiriaji wa Maudhui), mwingine hutoa: "Ni taarifa na vyanzo gani vinavyopatikana?" (Msaada wa Taarifa). Maoni hayafutwi tu kwa kuwa "makosa."

### 18. Kinga Dhidi ya Tafsiri Potofu ya Kitamaduni
AI inahitaji **Miundo ya Muktadha wa Kitamaduni** ili kuzuia kanuni za mawasiliano za nchi moja kuchukuliwa kama kiwango cha kimataifa.

### 19. Kejeli, Kejeli, na Ucheshi
AI hutumia muktadha, emoji, historia ya mazungumzo, na miundo ya kejeli inayojulikana, lakini lazima iruhusu kutokuwa na uhakika wakati maana ni ngumu.

### 20. Hakuna Adhabu Kulingana na Alama Moja ya AI
Hakuna uingiliaji kati mkali wa ukadiriaji unaoweza kutegemea tu matokeo ya uainishaji ya kiotomatiki (Maandishi + Muktadha + Tabia + Lugha + Media + Injini ya Kanuni = Tathmini ya Hatari).

### 21. Ishara za Tabia ya Mtumiaji & Hakuna Mfumo wa Mikopo ya Kijamii
Hii inahusiana na ishara za matumizi mabaya ya kiufundi (k.m., uchapishaji wa barua taka nyingi), si mfumo wa jumla wa ukadiriaji wa kijamii. Nexus Gaja haidumii Mfumo wa Mikopo ya Kijamii - usimamizi hulinda usalama, si tathmini ya thamani ya mtu.

### 22. AI ya Kiasi Lazima Ikaguliwe
Maamuzi yote muhimu ya kiotomatiki yamewekwa (Kitambulisho-Tukio, Kitambulisho-Kanuni, Kujiamini, Ukaguzi wa Binadamu, n.k.) ili kuhakikisha ufuatiliaji.

### 23. Chanya Isiyo sahihi, Hasi za Uongo & Vipimo vya Ubora
Aina za makosa hufuatiliwa. Dashibodi hupima Usahihi, Kukumbuka, na hasa **Kiwango cha Kurejesha Rufaa** (idadi ya rufaa zilizofanikiwa).

### 24. Usawa wa Lugha na Upendeleo wa Tafsiri
Ubora wa kukadiri lazima ulinganishwe katika lugha zote zinazotumika (Kigezo cha Udhibiti wa Lugha nyingi). Ikiwa matokeo ya ukadiriaji yatatofautiana kati ya asilia na tafsiri (Mgogoro wa Tafsiri), lazima hili likaguliwe mahususi.

### 25. Pendekezo la Usanifu & Injini ya Sera
Sheria (Injini ya Sera) hazijawekwa ngumu katika miundo ya AI. AI hutoa matokeo; Injini ya Sera huamua kulingana na sheria za sasa. Hii inaruhusu **mabadiliko ya modeli bila mabadiliko ya sheria**.

### 26. Mwanadamu Anabaki kuwa Mamlaka ya Mwisho
- **NG-AI-MOD-001**: AI husaidia katika kutambua na kuainisha, lakini haichukui nafasi ya ukaguzi wa kibinadamu katika maamuzi magumu.
- **NG-AI-MOD-002**: Maamuzi ya udhibiti wa kiotomatiki lazima yafuatiliwe, yaweze kuandikika na yaweze kuthibitishwa.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Kanuni za Ufadhili na Muundo wa Mapato (WP 1.10.1)

Kwa Nexus Gaja, kanuni muhimu sana ya kiuchumi inatumika: **Hakuna utangazaji wa kitamaduni ndani ya jukwaa.**
Hii kimsingi inatofautisha Nexus Gaja kutoka kwa mitandao mingi ya kijamii ya leo. Walakini, hii haimaanishi kuwa Nexus Gaja haiwezi kuwa na tabia ya kibiashara. Kinyume chake, jukwaa lazima liwe na uwezo wa kiuchumi ili kusudi lake la kijamii liweze kudumu. Shughuli za kiuchumi ni njia ya kufikia malengo, si madhumuni ya msingi ya jukwaa.

### 1. Kanuni ya NG-FIN-001
Nexus Gaja hufadhili shughuli zake kupitia njia za uwazi za mapato zinazotenganishwa na maslahi ya watumiaji, na si kupitia uchumaji wa usikivu wa watumiaji wake au data ya kibinafsi.

### 2. Hakuna Utangazaji wa Jadi
Hasa marufuku ni:
- Matangazo ya mabango
- Matangazo ya pop-up
- Matangazo ya video ya kucheza kiotomatiki
- Machapisho yanayofadhiliwa katika mipasho ya kawaida
- Profaili za utangazaji za kibinafsi
- Uuzaji wa wasifu wa mtumiaji au data ya kibinafsi
- Utangazaji unaotokana na mazungumzo ya faragha.

Nexus Gaja inasalia kuwa **nafasi ya mawasiliano badala ya nafasi ya matangazo**.

### 3. Ufadhili Bila Matangazo (The 6 Pillars)
Ufadhili umejengwa juu ya nguzo sita:
``` maandishi
                 NEXUS GAJA
                     │
       ┌────────────┼────────────┐
       ▼ ▼ ▼
   MICHANGO YA PREMIUM ORGANIZATION
       │ │ │
       ├──────────────────────────┤
       ▼ ▼ ▼
    HUDUMA ZA USHIRIKI WA RUZUKU
```

#### Nguzo ya 1 - Uanachama wa Msingi Bila Malipo
**Nexus Gaja Isiyolipishwa** huwezesha uelewa wa kimsingi wa kimataifa kwa kila mtu (wasifu, mawasiliano ya kimataifa, machapisho, jumuiya, gumzo, tafsiri msingi) bila gharama.

#### Nguzo ya 2 – Matoleo ya Kulipiwa
Matoleo yanayolipishwa ya hiari (**Nexus Gaja Plus**) yanayotoa viwango vikubwa zaidi vya hifadhi, ubora wa juu wa maudhui, viwango vilivyopanuliwa vya AI na vipengele vya shirika.
**Muhimu (Freemium badala ya Dark Freemium):** Mawasiliano ya kimsingi lazima yawahi kuharibiwa kwa njia bandia.

#### Nguzo ya 3 – Mashirika
Akaunti maalum za shule, vyuo vikuu, mashirika yasiyo ya kiserikali, biashara na manispaa (**Shirika la Nexus Gaja**). Shule zinaweza kusaidiwa kupitia viwango vya kitaasisi kama vizidishi vya uelewa wa kimataifa.

#### Nguzo ya 4 – Michango
**Njia ya Ufadhili ya Nexus Gaja** inakubali michango ya jumla na iliyotengwa (k.m., "kwa mawasiliano ya kimataifa ya vijana"). **Leja ya Ugawaji wa Fedha** inahakikisha ugawaji wa fedha kwa uwazi.
**Mfuko wa Kusudi na Tombola:** Sehemu ya michango hulisha bwawa kwa matumizi bila malipo/punguzo. Utaratibu wa bahati nasibu/tombola unaweza kutenga fedha hizi kwa uwazi na ukaguzi.

#### Nguzo ya 5 – Ufadhili wa Taasisi
Misingi, programu za ufadhili wa kitamaduni, au programu za serikali.
**NG-FIN-002:** Usaidizi wa kifedha haununui udhibiti wa uhariri au kiufundi (Uhuru).

#### Nguzo ya 6 - Huduma za Biashara
Huduma za B2B kama vile **Translation-as-a-Service** (API), mawasiliano ya shirika, au vyumba vya mikutano vya kimataifa, bila kulemea mipasho ya kawaida ya mtumiaji.

### 4. Hakuna Uchumaji wa Data na Uchumi wa Ufuatiliaji
**NG-FIN-003:** Data ya kibinafsi ya mtumiaji si bidhaa. Hakuna uuzaji wa orodha, wasifu, au historia. Nexus Gaja hainufaiki kutokana na ufuatiliaji wa kisaikolojia (Uchumi wa Ufuatiliaji).

### 5. Uwazi wa Fedha & Leja ya Mfuko
**Uwazi wa Kifedha wa Nexus Gaja:** Uchapishaji wa miundo ya kifedha iliyojumlishwa. Michango iliyotengwa hupokea uhasibu wa kiufundi (Kitambulisho cha Mfuko → Madhumuni → Salio → Mgao). Hakuna ruzuku mtambuka ya madhumuni ya kijamii katika uuzaji wa kampuni.

### 6. Mshikamano-Based Financing Model
Uwekaji bei unatokana na mwelekeo wa gharama, usawa na mshikamano.
**Solidarity Premium:** Chaguo la hiari kwa watumiaji wa Premium kufadhili sehemu ya ufikiaji wa mtumiaji mwingine. Mshikamano wa kulazimishwa au jamii ya daraja la juu (heshima ndogo/usawaji kwa watumiaji wasiolipishwa) hairuhusiwi kabisa.

### 7. KPIs za Kiuchumi Badala ya Uchumi wa Uchumi
Hakuna utegemezi wa kuweka watumiaji "mtandaoni kwa muda mrefu iwezekanavyo" (hakuna ragebait, milisho isiyo na kikomo).
Badala yake, tunatumia vipimo kama vile:
- **Kielezo cha Mawasiliano Ulimwenguni (GCI):** Uhusiano wenye mafanikio wa mawasiliano kati ya watu kutoka maeneo mbalimbali ya lugha/utamaduni.
- **Uwiano Endelevu wa Mfumo (PSR):** Mapato ya mara kwa mara / gharama za uendeshaji zinazorudiwa (Lengo ≥ 1).

### 8. Kile Tusichokitaka kwa Dhahiri (Orodha Hasi)
Nexus Gaja **haifadhiliwi na:
❌ Uuzaji wa data ya kibinafsi
❌ Utangazaji wa kitamaduni uliobinafsishwa
❌ Kufuatilia tabia ya mtumiaji kwa madhumuni ya utangazaji
❌ Uuzaji wa data ya mawasiliano ya kibinafsi
❌ Utumiaji wa data wa AI uliofichwa
❌ Ukuta wa malipo wa Ujanja wa Premium
❌ Masharti ya ufikiaji Bandia wa uchumaji wa mapato
❌ Ushawishi wa kisiasa unaolipwa
❌ Ununuzi wa maamuzi ya upendeleo ya udhibiti.

### 9. Usanifu wa Awali wa Fedha
``` maandishi
                         NEXUS GAJA
                              │
             ┌───────────────┼─────────────────────
             │ │ │
             ▼ ▼ ▼
          USERS ORGANIZATIONS ENTERPRISE
             │ │ │
             └───────────────┼──────────────────
                              │
                       HUDUMA ZA JUKWAA
                              │
          ┌────────────────── ┼──────────────────┐
          ▼ ▼ ▼
       API YA PREMIUM DONATIONS
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               FEDHA ZINAZOZUIA MFUKO MKUU
                                        │
                                        ▼
                                  KUSUDI LA KIJAMII
```

### Muhtasari wa Kanuni za Ufadhili (NG-FIN)
- **NG-FIN-001:** Hakuna ufadhili kupitia utangazaji wa kitamaduni.
- **NG-FIN-002:** Hakuna udhibiti wa uhariri/kiufundi kupitia usaidizi wa kifedha.
- **NG-FIN-003:** Data ya kibinafsi si bidhaa.
- **NG-FIN-004:** Mawasiliano ya kimsingi yanaendelea kufikiwa bila malipo.
- **NG-FIN-005:** Matoleo ya kulipiwa hayapaswi kudhalilisha watumiaji bila malipo.
- **NG-FIN-006:** Fedha zilizotengwa zinasimamiwa kulingana na madhumuni yao.
- **NG-FIN-007:** Usimamizi wa uwazi wa michango na ruzuku.
- **NG-FIN-008:** Huduma za kibiashara za B2B hazihatarishi uhuru.
- **NG-FIN-009:** Zingatia uendelevu badala ya upeo wa juu wa uchumaji wa mapato.
- **NG-FIN-010:** Muundo hulinda kabisa madhumuni ya kijamii.

## API, Violesura, na Usanifu wa Mawasiliano (WP 1.11.3)

Ili kuhakikisha uthabiti wa mfumo, usalama na uimara, Nexus Gaja inafuata usanifu kamili wa API-kwanza na unaoendeshwa na tukio.

### Core Principles
- **No Direct Database Access:** Components communicate exclusively via defined interfaces (APIs or Events), never through direct database queries of other services.
- **API Gateway:** All external client requests route through an API Gateway handling authentication, routing, and rate limiting.
- **Provider Abstraction:** External services (AI models, payment providers, translation engines) are integrated via abstraction layers, avoiding hardcoded dependencies and enabling flexible provider swapping.

### Mifumo ya Mawasiliano
- **API za Usawazishaji (REST/HTTPS):** Hutumika kwa maombi ya mara moja kama vile kuingia, mipangilio ya wasifu, au tafsiri za moja kwa moja.
- **Matukio Yasiyolandanishwa (Basi la Tukio):** Mfumo mkuu wa neva wa Nexus Gaja kwa uchakataji uliocheleweshwa, uliotenganishwa (k.m., `Ujumbe.Umeundwa` unaoanzisha Ukadiriaji, Tafsiri, na Arifa bila kulandanisha).
- **Muda Halisi (WebSocket):** Vituo maalum vya viashiria vya mazungumzo ya moja kwa moja na chapa.

### Usalama na Kuegemea
- **Muundo wa Sifuri wa Kuaminiana:** Trafiki ya ndani ya mtandao haiaminiki kiotomatiki; mawasiliano nyeti ya huduma kwa huduma yanahitaji uthibitishaji.
- **Mchoro wa Kutokuwa na uwezo na Kikasha toezi:** Shughuli muhimu (kama vile michango au kutuma ujumbe) zimeundwa ili zisiwe na uwezo ili kuzuia uchakataji unaorudiwa, kwa kutumia mchoro wa Kikasha toezi ili kuhakikisha kuwa matukio hayapotei kamwe hata wakati wa shughuli za hifadhidata.

## Muundo wa Kikoa cha MVP (WP 1.12)

Nexus Gaja inaajiri Usanifu wa MVP Unaoendeshwa na Kikoa (ADR-025), iliyoundwa kama moduli ya monolith iliyo na mipaka iliyo wazi ya kikoa. Muundo huu huzuia uchangamano wa huduma ndogo kabla ya wakati huku ukibakiza unyumbufu wa kugawanya vikoa mahususi baadaye.

### Huluki Muhimu za Kikoa
Usanifu hutenganisha kwa uwazi dhana tofauti ili kuhakikisha uadilifu wa data na kuepuka mitego ya kimuundo kama "Jina la mtumiaji = Binadamu":
- **Kitambulisho na Akaunti:** `Mtu` ≠ `Akaunti ya Mtumiaji` ≠ `Uthibitishaji wa Kitambulisho`. Mtu aliyeidhinishwa anashiriki kupitia akaunti, lakini huluki hubaki tofauti.
- **Mawasiliano:** `Ujumbe` ≠ `Tafsiri`. Ujumbe asilia haubadiliki; tafsiri ni vyombo vilivyounganishwa.
- **Ukadiriaji:** `Ripoti` ≠ `Uamuzi wa Kudhibiti`. Ripoti ni madai tu; kesi ya wastani hufanya uchunguzi.
- **Fedha:** `Mchango` ≠ `Salio la Mfuko`. Malipo yamewekwa kupitia leja isiyobadilika kwa hazina, kuhakikisha uwazi wa kifedha.

### Vikoa Vilivyounganishwa
Mfumo umegawanywa katika vikoa vya kimantiki vilivyo wazi (Miktadha Iliyounganishwa): Utambulisho, Akaunti, Shirika, Mawasiliano, Jumuiya, Lugha, Usaidizi, Arifa, Fedha, na Utawala. Vikoa hivi hupanga safari nzima kutoka kwa vyombo vya ulimwengu halisi (Watumiaji, Shule, Mashirika Yasiyo ya Kiserikali) hadi mwingiliano wao wa kidijitali na utawala unaohusiana.

##Hali ya Mradi
Mradi kwa sasa uko katika hatua ya usanifu na upangaji hai.
Maamuzi yanayoendelea ya usanifu yameandikwa kwenye folda ya `/hati`.