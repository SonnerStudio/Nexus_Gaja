# ኔክሰስ ጋጃ

![Nexus Gaja Logo](ንብረቶች/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** ዓለም አቀፍ ግንኙነትን ለመለወጥ የተነደፈ አስተዋይ፣ አውድ-ስሱ የመገናኛ አውታር ነው።

## አላማ እና ራዕይ
በግሎባላይዜሽን ዓለም ውስጥ ቋንቋ ብዙውን ጊዜ ትልቁ እንቅፋት ነው። የNexus Gaja ዋና ግብ በሰዎች መካከል ምንም እንከን የለሽ፣ እንቅፋት-ነጻ እና ትክክለኛ ግንኙነትን ማስቻል ነው— የጋራ ቋንቋ ይናገሩ።

ቃላትን በግትርነት መተርጎም ብቻ ሳይሆን ስለ ** ትርጉም ስለማስተላለፍ** ነው። ኔክሰስ ጋጃ ባህላዊ፣ ክልላዊ እና ዐውደ-ጽሑፋዊ ጉዳዮችን በመረዳት ሰዎችን በጥልቅ ያገናኛል፣ በዚህም እውነተኛ፣ ትክክለኛ ውይይቶችን ያስችላል።

## እድሎች እና ባህሪዎች
- ** መልቲሚዲያ ኮሙኒኬሽን ***፡ ስርዓቱ ጽሑፍን ብቻ ሳይሆን ምስልን፣ ኦዲዮን እና ቪዲዮን ጭምር ያካሂዳል። ይህ ሙሉ ለሙሉ መሳጭ ንግግሮች (ለምሳሌ፡ የቪዲዮ ጥሪዎች ወይም የድምጽ መልዕክቶች) በቋንቋ መሰናክሎች ውስጥ በቅጽበት ይፈቅዳል።
- **የአውድ ትብነት**፡ ብዙውን ጊዜ በተለመደው ተርጓሚዎች የተሳሳቱ ምጸታዊ፣ ፈሊጦች፣ ጃርጎን እና ክልላዊ ቀበሌኛዎችን ማወቅ።
- **የመስቀል-ፕላትፎርም ኔትወርክ ***፡ ለግል ውይይቶች፣ የመድረክ ክሮች (ከአስተያየቶች ጋር የተለጠፈ ልጥፎች) እና ለአለም አቀፍ የማህበረሰብ መስተጋብር እንደ መሰረት ሆኖ ያገለግላል።

---

## Technical Architecture (Core Concept)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## AI-Assisted Moderation (WP 1.8.4)

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. መሰረታዊ መርህ
ለሥነ ሕንፃው በጣም አስፈላጊው ዓረፍተ ነገር፡ ** ልከኝነት AI የግምገማ ሥርዓት እንጂ ራሱን የቻለ ገዥ ሥርዓት አይደለም።**
በNexus Gaja ላይ የትኞቹ አስተያየቶች ሊኖሩ እንደሚችሉ እራሱን ለመወሰን ሳይሆን ሰዎችን በመጠኑ ለመርዳት ታስቦ የተሰራ ነው።
በሦስት ደረጃዎች መካከል እንለያለን-
- ** ማወቂያ: ** "እዚህ የሕግ ጥሰት ሊኖር ይችላል."
- ** ግምገማ: ** "የደንብ ጥሰት ዕድል ለምሳሌ 94% ነው."
- ** ውሳኔ: ** "በእርግጥ ምን እርምጃ ተወሰደ?"
ሦስተኛው ደረጃ ከባድ በሆኑ ጉዳዮች በሰው ቁጥጥር ሊደረግበት ይገባል.

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

### 4. ለምን የአውድ ሞተር ወሳኝ ነው።
ንጹህ ቁልፍ ቃል ፍለጋ በቂ አይሆንም። "በሳቅ ልገድለው እችል ነበር" በትርጉም አመፅን ይዟል ግን የአነጋገር ዘይቤ ነው። "ነገ ከቀኑ 8 ሰአት ላይ በቤቱ ፊት ለፊት እተኩስበታለሁ" ፍፁም የተለየ ሁኔታ ነው። AI መግለጫው በተወሰነ አውድ ውስጥ ምን ማለት እንደሆነ መረዳት አለበት።

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

### 6. ኦሪጅናል ቋንቋ + ትርጉም
ኦሪጅናል እና ትርጉም ለየብቻ ይተነተናል። ከዚያ በኋላ ብቻ "የተጣመረ የአወያይ ግምገማ" ይከናወናል. ይህ ኔክሰስ ጋጃ ትርጉሙ ራሱ ተባብሶ ወይም እውነታውን ለውጦ እንደሆነ ለማወቅ ያስችላል።

### 7. የመተማመን ነጥብ
እያንዳንዱ የ AI ግምገማ በራስ የመተማመን ነጥብ ይቀበላል (ለምሳሌ፣ የማስፈራሪያ ዕድል፡ 0.96)። ነገር ግን፡ **የመተማመን ነጥብ ≠ እውነት።** ነጥብ 96% ብቻ ማለት ሞዴሉ ስለ ምደባው በጣም እርግጠኛ ነው ማለት ነው እንጂ ተጠቃሚው ጥፋተኛ ነው ማለት አይደለም።

### 8. እርግጠኛ አለመሆን ራሱ ምልክት ይሆናል።
AI እርግጠኛ ካልሆነ (ለምሳሌ፡ ዛቻ፡ 0.62፣ ሳቲር፡ 0.54)፣ ጨካኝ ህጎችን በቀላሉ ማስከበር የለበትም። በምትኩ፣ እርግጠኛ አለመሆን በቀጥታ በህንፃው ውስጥ ተገንብቷል፡ ** የሰው ግምገማ ያስፈልጋል ***።

### 9. አራት የውሳኔ ዞኖች
- 🟢 **አረንጓዴ**: በጣም ታዛዥ ሊሆን ይችላል። → ምንም እርምጃ የለም።
- 🟡 **ቢጫ**፡ የሚቻለውን መጣስ። → አስፈላጊ ከሆነ ይቆጣጠሩ / ማስጠንቀቂያ ይስጡ.
- 🟠 **ብርቱካናማ**፡ ምናልባት ጥሰት ሊሆን ይችላል። → የአወያይ ግምገማ።
- 🔴 **ቀይ**: ከባድ ሊሆን የሚችል ጥሰት። → ወዲያውኑ የመከላከያ እርምጃ + የሰዎች ግምገማ.

### 10. የለም "AI ቅጣት"
** AI ምንም የመጨረሻ ማዕቀብ አይጥልም።** ለከባድ የደህንነት ስጋቶች ቴክኒካል አፋጣኝ እርምጃዎችን (ለምሳሌ፣ ለጊዜው መልእክትን መቆጠብ) ሊያነሳሳ ይችላል፣ነገር ግን የመጨረሻው ውሳኔ የተረጋገጠ ነው።

### 11. የመከላከያ እርምጃዎች በራስ-ሰር ሊከሰቱ ይችላሉ
ተጨባጭ ስጋት (ስጋት ተገኝቷል → ከፍተኛ በራስ መተማመን → ጊዜያዊ ገደብ → የሰዎች ግምገማ → ውሳኔ) ፣ AI ወደ ዳኛ ሳንለውጥ የተፈራረቀውን ተጠቃሚ እንጠብቃለን።

### 12. AI ውሳኔውን ማረጋገጥ መቻል አለበት።
DSA ግልጽ እና የተወሰኑ ምክንያቶችን ይፈልጋል። AI የተዋቀረ ምክንያትን ያቀርባል፡ ደንብ (NG-CONDUCT-004)፣ የተገኘ (የተጨባጭ ስጋት)፣ መተማመን (0.94)፣ ተዛማጅ አውድ (የቀደሙት 4 መልዕክቶች)፣ የሚመከር እርምጃ (የሰው ልጅ ግምገማ)።

### 13. AI ይዘትን በሚስጥር መቀየር የለበትም
** ልከኝነት AI በፍፁም ሳይታወቅ ዋናውን ይዘት መቀየር የለበትም።** በራስ-ሰር እርማት፣ ትርጉም ወይም ማጠቃለያ ወቅት ዋናው ሁልጊዜ ተጠብቆ ይቆያል።

### 14. AI-የመነጨ ይዘት
በሚከተሉት መካከል እንለያለን፡- በሰው የተፈጠረ፣ በ AI የታገዘ፣ በ AI የተፈጠረ እና በ AI-manipulated። ይህ የይዘት ሜታዳታ አካል ይሆናል።

### 15. የ AI ይዘት እና AI Provenance ንብርብር መሰየሚያ
በአውሮፓ ህብረት AI ህግ ግልጽነት ህግ (ከኦገስት 2026 ጀምሮ) በ AI የመነጨ ይዘት ተለይቶ የሚታወቅ መሆን አለበት። ሜታዳታ (AI-Origin፣ Model፣ Timestamp፣ Human Review) የሚያከማች AI Provenance ንብርብር እናቀርባለን።

### 16. Deepfake Detection
አርክቴክቸር ሰው ሰራሽ ምስሎችን፣ የተዘበራረቁ ድምጾችን እና ጥልቅ ሀሰቶችን ለመለየት ያለመ ነው። ሆኖም፣ ማግኘቱ በራስ ሰር ማረጋገጫ አይሆንም።

### 17. ምንም አውቶማቲክ "የእውነት ማሽን" የለም (ልከኝነት ≠ እውነታን ማረጋገጥ)
አንድ ስርዓት ይፈትሻል፡ "ይዘቱ ደንቦችን ይጥሳል?" (የይዘት አወያይ)፣ ሌላው ደግሞ “ምን መረጃ እና ምንጮች ይገኛሉ?” የሚል ይሰጣል። (የመረጃ እገዛ)። አስተያየቶች "ስህተት" ስለሆኑ በቀላሉ አይሰረዙም።

### 18. ከባህላዊ የተሳሳተ ትርጓሜ ጥበቃ
የአንድ ሀገር የግንኙነት ደንቦች እንደ አለምአቀፍ ደረጃ እንዳይወሰዱ ለመከላከል AI **የባህላዊ አውድ ሞዴሎች** ይፈልጋል።

### 19. አስቂኝ፣ ሳቲር እና ቀልድ
AI አውድ፣ ስሜት ገላጭ ምስሎች፣ የውይይት ታሪክ እና የታወቁ አስቂኝ አወቃቀሮችን ይጠቀማል፣ ነገር ግን ትርጉሞች አሻሚ ሲሆኑ እርግጠኛ አለመሆንን መፍቀድ አለበት።

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. የተጠቃሚ ባህሪ ምልክቶች እና ምንም ማህበራዊ ብድር ስርዓት የለም
ይህ ከቴክኒካዊ አላግባብ መጠቀም ምልክቶች ጋር ይዛመዳል (ለምሳሌ፡ የጅምላ አይፈለጌ መልዕክት መለጠፍ)፣ አጠቃላይ የማህበራዊ ደረጃ አሰጣጥ ስርዓት አይደለም። ኔክሰስ ጋጃ የማህበራዊ ክሬዲት ስርዓትን አይጠብቅም - ልከኝነት ደህንነትን ያገለግላል እንጂ የአንድን ሰው ዋጋ መገምገም አይደለም።

### 22. ልከኝነት AI ተሰሚነት ያለው መሆን አለበት።
ሁሉም ተዛማጅነት ያላቸው አውቶማቲክ ውሳኔዎች መፈለጊያውን ለማረጋገጥ (የክስተት-መታወቂያ፣ ደንብ-መታወቂያ፣ መተማመን፣ የሰው ግምገማ፣ ወዘተ) ገብተዋል።

### 23. የውሸት አዎንታዊ, የውሸት አሉታዊ እና የጥራት መለኪያዎች
የስህተት ዓይነቶች ቁጥጥር ይደረግባቸዋል። ዳሽቦርድ ትክክለኛነትን፣ አስታዋሽ እና በተለይም **የይግባኝ መቀልበሻ መጠን** (የተሳካላቸው ይግባኞች ብዛት) ይለካል።

### 24. የቋንቋ እኩልነት እና የትርጉም አድልዎ
የልከኝነት ጥራት በሁሉም የሚደገፉ ቋንቋዎች (ባለብዙ ቋንቋ አወያይ ቤንችማርክ) መወዳደር አለበት። የሽምግልና ውጤቶች በዋናው እና በትርጉሙ (የትርጉም ግጭት) መካከል የሚለያዩ ከሆነ ይህ በተለይ መከለስ አለበት።

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Financing Principles and Revenue Model (WP 1.10.1)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Principle NG-FIN-001
Nexus Gaja finances its operations through transparent revenue streams separated from user interests, and not through the monetization of its users' attention or personal data.

### 2. ባህላዊ ማስታወቂያ የለም።
በተለይ የተከለከሉ ናቸው፡-
- የባነር ማስታወቂያዎች
- ብቅ-ባይ ማስታወቂያዎች
- የቪዲዮ ማስታወቂያዎችን በራስ-ሰር በማጫወት ላይ
- በመደበኛ ምግብ ውስጥ የተደገፉ ልጥፎች
- ለግል የተበጁ የማስታወቂያ መገለጫዎች
- የተጠቃሚ መገለጫዎች ወይም የግል ውሂብ ሽያጭ
- ከግል ንግግሮች የተገኘ ማስታወቂያ።

Nexus Gaja ከማስታወቂያ ቦታ** ይልቅ **የመገናኛ ቦታ ሆኖ ይቆያል።

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

#### ምሰሶ 1 - ነፃ መሰረታዊ አባልነት
**Nexus Gaja Free** ለሁሉም ሰው (መገለጫ፣ ዓለም አቀፍ ግንኙነት፣ ልጥፎች፣ ማህበረሰቦች፣ ቻቶች፣ መሠረታዊ ትርጉም) መሠረታዊ ዓለም አቀፍ ግንዛቤን ያለምንም ወጪ ያስችላል።

#### ምሰሶ 2 - ፕሪሚየም አቅርቦቶች
በፈቃደኝነት የሚከፈልባቸው አቅርቦቶች (**Nexus Gaja Plus**) ከፍተኛ የማከማቻ ገደቦችን፣ ከፍተኛ የሚዲያ ጥራትን፣ የተስፋፋ AI ኮታዎችን እና ድርጅታዊ ባህሪያትን ያቀርባል።
** ጠቃሚ (ከጨለማ ፍሪሚየም ይልቅ ፍሪሚየም):** መሰረታዊ ግንኙነት በሰው ሰራሽ መንገድ መበላሸት የለበትም።

#### ምሰሶ 3 - ድርጅቶች
ለትምህርት ቤቶች፣ ዩኒቨርሲቲዎች፣ መንግሥታዊ ያልሆኑ ድርጅቶች፣ ንግዶች እና ማዘጋጃ ቤቶች ልዩ መለያዎች (**Nexus Gaja Organization**). ትምህርት ቤቶች እንደ ዓለም አቀፍ ግንዛቤ ማባዛት በተቋማዊ ተመኖች ሊደገፉ ይችላሉ።

#### ምሰሶ 4 - ልገሳዎች
**Nexus Gaja Funding Pool** አጠቃላይ እና የተመደቡ ልገሳዎችን ይቀበላል (ለምሳሌ፣ "ለአለም አቀፍ የወጣቶች ግንኙነት")። **የፈንድ ድልድል ደብተር** ግልጽ የገንዘብ ድልድል ያረጋግጣል።
**የዓላማ ፈንድ እና ቶምቦላ፡** የተወሰነው የልገሳ ክፍል በነጻ/ቅናሽ አገልግሎት ገንዳውን ይመገባል። የሎተሪ/ቶምቦላ ዘዴ እነዚህን ገንዘቦች በግልፅ እና ኦዲት በሆነ መልኩ መመደብ ይችላል።

#### ምሰሶ 5 - ተቋማዊ የገንዘብ ድጋፍ
መሠረቶች፣ የባህል የገንዘብ ድጋፍ ፕሮግራሞች ወይም የግዛት ፕሮግራሞች።
** NG-FIN-002: ** የገንዘብ ድጋፍ የኤዲቶሪያል ወይም የቴክኒክ ቁጥጥር (ነጻነት) አይገዛም.

#### ምሰሶ 6 - የንግድ አገልግሎቶች
የB2B አገልግሎቶች እንደ ** ትርጉም-እንደ-አገልግሎት** (ኤፒአይ)፣ ድርጅታዊ ግንኙነት ወይም ዓለም አቀፍ የስብሰባ ክፍሎች፣ መደበኛውን የተጠቃሚ ምግብ ሳይጫኑ።

### 4. ምንም የውሂብ ገቢ መፍጠር እና ክትትል ኢኮኖሚ የለም
**NG-FIN-003:** የግል ተጠቃሚ ውሂብ ሸቀጥ አይደለም። የዝርዝሮች፣ መገለጫዎች ወይም ታሪኮች ሽያጭ የለም። ኔክሰስ ጋጃ ከሥነ ልቦና ክትትል (Surveillance Economy) አያተርፍም።

### 5. የፋይናንሺያል ግልጽነት እና ፈንድ መዝገብ
**Nexus Gaja የፋይናንሺያል ግልጽነት:** የተዋሃዱ የፋይናንስ መዋቅሮች ህትመት. የታቀዱ ልገሳዎች ቴክኒካዊ የሂሳብ አያያዝ (የፈንድ መታወቂያ → ዓላማ → ሚዛን → ምደባ) ይቀበላሉ። ወደ ኮርፖሬት ግብይት የማህበራዊ ዓላማ ድጎማ የለም።

### 6. በአንድነት ላይ የተመሰረተ የፋይናንስ ሞዴል
የዋጋ አወጣጥ በዋጋ-ተኮርነት፣ ፍትሃዊነት እና አብሮነት ላይ የተመሰረተ ነው።
**የአንድነት ፕሪሚየም፡** ለPremium ተጠቃሚዎች የሌላ ተጠቃሚን መዳረሻ የተወሰነ ክፍል የገንዘብ ድጋፍ ለማድረግ በፈቃደኝነት የሚደረግ አማራጭ። የግዳጅ አብሮነት ወይም ፕሪሚየም መደብ ማህበረሰብ (ለነፃ ተጠቃሚዎች ያነሰ አክብሮት/መቆጣጠር) በጥብቅ የተከለከለ ነው።

### 7. ከተሳትፎ ኢኮኖሚ ይልቅ ኢኮኖሚያዊ KPIs
ተጠቃሚዎችን "በተቻለ መጠን በመስመር ላይ" በማቆየት ላይ ጥገኝነት የለም (ራጋባይት የለም፣ ማለቂያ የሌላቸው ምግቦች)።
በምትኩ፣ እንደዚህ ያሉ መለኪያዎችን እንጠቀማለን፡-
- **ግሎባል ኮሙኒኬሽን ኢንዴክስ (GCI):** ከተለያዩ የቋንቋ/ባህላዊ ክልሎች በመጡ ሰዎች መካከል የተሳካ የግንኙነት ግንኙነት።
- **የፕላትፎርም ዘላቂነት ሬሾ (PSR):** ተደጋጋሚ ገቢ / ተደጋጋሚ የስራ ማስኬጃ ወጪዎች (ዒላማ ≥ 1)።

### 8. በግልፅ የማንፈልገው (አሉታዊ ዝርዝር)
Nexus Gaja ** የገንዘብ ድጋፍ የተደረገው በ፡
❌ የግል መረጃ ሽያጭ
❌ ለግል የተበጀ ባህላዊ ማስታወቂያ
❌ የተጠቃሚ ባህሪን ለማስታወቂያ አላማ መከታተል
❌ የግል የግንኙነት መረጃ ሽያጭ
❌ የተደበቀ AI ውሂብ አጠቃቀም
❌ Manipulative Premium paywalls
❌ ለገቢ መፍጠር ሰው ሰራሽ ተደራሽነት ገደብ
❌ የተከፈለ የፖለቲካ ተጽዕኖ
❌ ልዩ መብት ያላቸው የአወያይ ውሳኔዎች ግዢ።

### 9. የመጀመሪያ ደረጃ የፋይናንስ አርክቴክቸር
`` ጽሑፍ
                         NEXUS GAJA
                              │
             ───────────────
             │ │
             ▼ ▼ ▼
          የተጠቃሚ ድርጅቶች ኢንተርፕራይዝ
             │ │
             └─────────────
                              │
                       የፕላትፎርም አገልግሎቶች
                              │
          ──────────── ┼───────
          ▼ ▼ ▼
       ፕሪሚየም ልገሳዎች ኤፒአይ
                              │
                    ────────
                    ▼ ▼
               አጠቃላይ ፈንድ የተገደበ ፈንዶች
                                        │
                                        ▼
                                  ማህበራዊ ዓላማ
```

### የፋይናንስ መርሆዎች ማጠቃለያ (NG-FIN)
- ** NG-FIN-001: ** በባህላዊ ማስታወቂያ በኩል ፋይናንስ የለም.
- ** NG-FIN-002: ** በገንዘብ ድጋፍ በኩል የአርትዖት / ቴክኒካዊ ቁጥጥር የለም.
- ** NG-FIN-003: ** የግል መረጃ ሸቀጥ አይደለም.
- **NG-FIN-004:** መሰረታዊ ግንኙነት ያለክፍያ ተደራሽ ሆኖ ይቆያል።
- **NG-FIN-005:** የፕሪሚየም አቅርቦቶች ነፃ ተጠቃሚዎችን ዝቅ ማድረግ የለባቸውም።
- ** NG-FIN-006: ** የተመደቡ ገንዘቦች እንደ ዓላማቸው ይተዳደራሉ።
- ** NG-FIN-007: *** የልገሳ እና የእርዳታዎች ግልጽ አስተዳደር.
- **NG-FIN-008:** የንግድ B2B አገልግሎቶች ነፃነትን አይጎዱም።
- ** NG-FIN-009: *** ከከፍተኛ ገቢ መፍጠር ይልቅ ዘላቂነት ላይ ያተኩሩ።
- ** NG-FIN-010: ** መዋቅሩ የማህበራዊ ዓላማን በቋሚነት ያረጋግጣል.

## ኤፒአይ፣ በይነገጾች እና የግንኙነት አርክቴክቸር (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### ዋና መርሆዎች
- ** ምንም ቀጥተኛ የውሂብ ጎታ መዳረሻ የለም: *** አካላት የሚገናኙት በተገለጹ በይነገጾች (ኤፒአይኤስ ወይም ዝግጅቶች) ብቻ ነው እንጂ በሌሎች አገልግሎቶች ቀጥተኛ የውሂብ ጎታ መጠይቆች በፍጹም አይገናኙም።
- **ኤፒአይ ጌትዌይ፡** ሁሉም የውጭ ደንበኛ ጥያቄዎች በኤፒአይ ጌትዌይ ማረጋገጫ፣ ማዘዋወር እና ተመን መገደብ በኩል ይሄዳሉ።
- **የአቅራቢ ማጠቃለያ፡** ውጫዊ አገልግሎቶች (AI ሞዴሎች፣ የክፍያ አቅራቢዎች፣ የትርጉም ሞተሮች) በ abstraction layers የተዋሃዱ፣ ሃርድ ኮድ የተደረጉ ጥገኝነቶችን በማስወገድ እና ተለዋዋጭ አቅራቢዎችን መለዋወጥ ያስችላል።

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Security and Reliability
- **Zero-Trust Model:** Internal network traffic is not automatically trusted; sensitive service-to-service communication requires authentication.
- **Idempotency & Outbox Pattern:** Critical operations (like donations or messaging) are designed to be idempotent to prevent duplicate processing, utilizing the Outbox pattern to ensure events are never lost even during database transactions.

## MVP ዶሜይን ሞዴል (WP 1.12)

Nexus Gaja እንደ ሞዱል ሞኖሊት ከግልጽ የጎራ ድንበሮች ጋር በጥብቅ የተነደፈ በDomain-Driven MVP Architecture (ADR-025) ይጠቀማል። ይህ መዋቅር ከጊዜ በኋላ የተወሰኑ ጎራዎችን ለመከፋፈል ተለዋዋጭነትን በማቆየት ያለጊዜው የማይክሮ አገልግሎት ውስብስብነትን ይከላከላል።

### የኮር ዶሜይን አካላት
አርክቴክቸር የውሂብን ታማኝነት ለማረጋገጥ እና እንደ "የተጠቃሚ ስም = ሰው" ያሉ መዋቅራዊ ወጥመዶችን ለማስወገድ የተለያዩ ፅንሰ ሀሳቦችን በግልፅ ይለያል።
- **ማንነት እና መለያዎች፡** `ሰው` ≠ `የተጠቃሚ መለያ` ≠ `ማንነት ማረጋገጫ`። የተረጋገጠ ሰው በመለያ ይሳተፋል፣ ነገር ግን ህጋዊ አካላት የተለዩ እንደሆኑ ይቆያሉ።
- **መገናኛ፡** `መልዕክት` ≠ `ትርጉም`። ዋናው መልእክት የማይለወጥ ሆኖ ይቆያል; ትርጉሞች የተገናኙ አካላት ናቸው።
- ** ልከኝነት፡** `ሪፖርት` ≠ `የመጠነኛ ውሳኔ`። ዘገባ የይገባኛል ጥያቄ ብቻ ነው; በመጠኑ ጉዳይ ላይ ምርመራውን ያካሂዳል.
- ** ፋይናንስ፡** `ልገሳ` ≠ `የፈንድ ሒሳብ`። ክፍያዎች የፋይናንስ ግልጽነትን በማረጋገጥ በማይለወጥ ደብተር ወደ ፈንድ ይያዛሉ።

### እርስ በርስ የተያያዙ ጎራዎች
ስርዓቱ ግልጽ በሆኑ ምክንያታዊ ጎራዎች (የተጠረዙ አውዶች) የተከፋፈለ ነው፡ ማንነት፣ መለያ፣ ድርጅት፣ ግንኙነት፣ ማህበረሰብ፣ ቋንቋ፣ ልከኝነት፣ ማስታወቂያ፣ ፋይናንስ እና አስተዳደር። እነዚህ ጎራዎች ከገሃዱ ዓለም አካላት (ተጠቃሚዎች፣ ትምህርት ቤቶች፣ መንግሥታዊ ያልሆኑ ድርጅቶች) ወደ ዲጂታል ግንኙነቶቻቸው እና ተዛማጅ አስተዳደራቸው የሚያደርጉትን ጉዞ በሙሉ ይሳሉ።

## የፕሮጀክት ሁኔታ
ፕሮጀክቱ በአሁኑ ጊዜ በሥነ ሕንፃ እና በዕቅድ ደረጃ ላይ ነው።
በመካሄድ ላይ ያሉ የስነ-ህንፃ ውሳኔዎች በ`/ሰነዶች` አቃፊ ውስጥ ተመዝግበው ይገኛሉ።