#नेक्सस गाजा

![नेक्सस गाजा लोगो](संपत्ति/लोगो.jpg)

![नेक्सस गाजा हीरो](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**नेक्सस गाजा** एक बुद्धिमान, संदर्भ-संवेदनशील संचार नेटवर्क है जिसे वैश्विक संचार में क्रांति लाने के लिए डिज़ाइन किया गया है।

## उद्देश्य और दृष्टि

![नेक्सस गाजा विज़न](assets/img/nexus_vision.jpg)

वैश्वीकृत दुनिया में, भाषा अक्सर सबसे बड़ी बाधा होती है। नेक्सस गाजा का मुख्य लक्ष्य लोगों के बीच निर्बाध, बाधा मुक्त और प्रासंगिक रूप से सटीक संचार सक्षम करना है - भले ही वे एक आम भाषा बोलते हों।

यह केवल शब्दों का सख्ती से अनुवाद करने के बारे में नहीं है, बल्कि **अर्थ स्थानांतरित करने** के बारे में है। नेक्सस गाजा सांस्कृतिक, क्षेत्रीय और प्रासंगिक बारीकियों को समझकर लोगों को गहरे स्तर पर जोड़ता है, जिससे वास्तविक, प्रामाणिक बातचीत संभव हो पाती है।

## संभावनाएँ और विशेषताएँ
- **मल्टीमीडिया संचार**: सिस्टम न केवल पाठ, बल्कि छवि, ऑडियो और वीडियो को भी संसाधित करता है। यह भाषा बाधाओं के पार वास्तविक समय में पूरी तरह से गहन बातचीत (उदाहरण के लिए, वीडियो कॉल या वॉयस संदेश) की अनुमति देता है।
- **संदर्भ संवेदनशीलता**: विडंबनाओं, मुहावरों, शब्दजाल और क्षेत्रीय बोलियों की पहचान जिन्हें अक्सर पारंपरिक अनुवादकों द्वारा गलत समझा जाता है।
- **क्रॉस-प्लेटफ़ॉर्म नेटवर्क**: निजी चैट, फ़ोरम थ्रेड (टिप्पणियों के साथ पोस्ट), और वैश्विक सामुदायिक इंटरैक्शन के लिए एक आधार के रूप में कार्य करता है।

---

## तकनीकी वास्तुकला (मुख्य अवधारणा)

![नेक्सस गाजा ट्रांसलेशन कॉन्सेप्ट](assets/img/nexus_translation.jpg)

The technical core of Nexus Gaja is a custom-built communication model that is strictly divided into three layers:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### प्रसंग निर्भरता
नेक्सस गाजा में अनुवाद संदेशों को कभी भी अलग करके नहीं देखता। इंजन संपूर्ण पदानुक्रम पर विचार करता है:
`संदेश` → `पिछला संदेश` → `थ्रेड संदर्भ` → `सामुदायिक संदर्भ` → `भाषा / क्षेत्र` → `उपयोगकर्ता प्राथमिकताएं`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## एआई-असिस्टेड मॉडरेशन (WP 1.8.4)

![नेक्सस गाजा एआई मॉडरेशन](एसेट्स/आईएमजी/नेक्सस_मॉडरेशन.जेपीजी)

एआई-असिस्टेड मॉडरेशन के साथ, हम वर्तमान ईयू नियमों (अनुच्छेद 50 के तहत ईयू एआई अधिनियम की पारदर्शिता आवश्यकताओं; समझने योग्य औचित्य और अपील विकल्पों के साथ डिजिटल सेवा अधिनियम) को ध्यान में रखते हुए, उत्पाद विचार से तकनीकी वास्तुकला तक एक महत्वपूर्ण कदम उठा रहे हैं।

### 1. मूल सिद्धांत
आर्किटेक्चर के लिए सबसे महत्वपूर्ण वाक्य है: **मॉडरेशन एआई एक समीक्षा प्रणाली है, न कि एक स्वायत्त शासन प्रणाली।**
इसे मनुष्यों की संयमित सहायता करने के लिए डिज़ाइन किया गया है, न कि स्वयं यह निर्धारित करने के लिए कि नेक्सस गाजा पर किन विचारों को मौजूद रहने की अनुमति है।
हम तीन स्तरों के बीच अंतर करते हैं:
- **पता लगाना:** "यहां नियम का उल्लंघन हो सकता है।"
- **मूल्यांकन:** "उदाहरण के लिए, नियम के उल्लंघन की संभावना 94% है।"
- **निर्णय:** "वास्तव में क्या कार्रवाई की गई है?"
गंभीर मामलों में तीसरे स्तर को मानव द्वारा नियंत्रित किया जाना चाहिए।

### 2. एक सबसिस्टम के रूप में मॉडरेशन एआई
एकल AI के बजाय, एक मजबूत सबसिस्टम स्थापित किया गया है:
```पाठ
                 नेक्सस गाजा एआई मॉडरेशन
                          │
       ┌──────────────────┼──────────────┐
       │ │ │
  भाषा एआई सुरक्षा एआई धोखाधड़ी एआई
       │ │ │
       ├──────────────┬───┴──────────────┬──┤
       │ │ │
 अनुवाद व्यवहार पहचान
 विश्लेषण विश्लेषण संकेत
       │ │ │
       └──────────────┼─────────────────┘
                      ▼
               जोखिम मूल्यांकन
                      │
                      ▼
               मानव समीक्षा
```

### 3. सबसे महत्वपूर्ण एआई मॉड्यूल
नेक्सस गाजा नौ विशेष विश्लेषण क्षेत्रों का उपयोग करता है:
- **एम1 - भाषा समझ**: भाषा, बोली, कठबोली भाषा, व्यंग्य संकेतक, अनुवाद संबंधी मुद्दों का पता लगाता है।
- **एम2 - विषाक्तता/दुरुपयोग का पता लगाना**: अपमान, व्यक्तिगत हमलों, उत्पीड़न का पता लगाता है।
- **एम3 - खतरे का पता लगाना**: संभावित खतरों, ब्लैकमेल, हिंसा की घोषणाओं का पता लगाता है।
- **एम4 - नफरत/अमानवीयकरण का पता लगाना**: विशिष्ट संबद्धता के आधार पर लोगों पर लक्षित हमलों का पता लगाता है।
- **एम5 - स्पैम/हेरफेर का पता लगाना**: स्पैम, बॉट व्यवहार, समन्वित हेरफेर का पता लगाता है।
- **एम6 - धोखाधड़ी का पता लगाना**: संदिग्ध धोखाधड़ी प्रयासों, फ़िशिंग, सोशल इंजीनियरिंग का पता लगाता है।
- **एम7 - पहचान की अखंडता**: खाता अधिग्रहण, एकाधिक खातों, प्रतिबंध चोरी के संबंध में संकेतों की जांच करता है।
- **एम8 - मीडिया सुरक्षा**: छवियों, ऑडियो, वीडियो, दस्तावेज़ों का विश्लेषण करता है।
- **एम9 - संदर्भ इंजन**: सबसे महत्वपूर्ण मॉड्यूल। यह व्यक्तिगत निष्कर्षों को मिला देता है।

### 4. कॉन्टेक्स्ट इंजन महत्वपूर्ण क्यों है
शुद्ध कीवर्ड खोज अपर्याप्त होगी. "मैं उसे हंसने से मार सकता था" में शब्दार्थ की दृष्टि से हिंसा शामिल है लेकिन यह अलंकार है। "कल रात 8 बजे मैं उसे उसके घर के सामने गोली मार दूंगा" यह बिल्कुल अलग स्थिति है। एआई को यह समझना चाहिए कि कथन का उसके विशिष्ट संदर्भ में क्या अर्थ है।

### 5. बहुभाषी संयम
मॉडरेशन केवल शब्दों की तुलना नहीं कर सकता. इसे शब्दार्थ स्तर का विश्लेषण करना चाहिए (उदाहरण के लिए, जर्मन मुहावरे बनाम जापानी मुहावरे बनाम क्षेत्रीय अभिव्यक्तियाँ)।

### 6. मूल भाषा+अनुवाद
मूल और अनुवाद का अलग-अलग विश्लेषण किया गया है। तभी "संयुक्त मॉडरेशन मूल्यांकन" होता है। यह नेक्सस गाजा को यह निर्धारित करने की अनुमति देता है कि क्या अनुवाद ने स्वयं तथ्यों को बढ़ाया या बदल दिया है।

### 7. कॉन्फिडेंस स्कोर
प्रत्येक एआई मूल्यांकन को एक आत्मविश्वास स्कोर प्राप्त होता है (उदाहरण के लिए, खतरे की संभावना: 0.96)। हालाँकि: **आत्मविश्वास स्कोर ≠ सत्य।** 96% का स्कोर केवल इसका मतलब है कि मॉडल अपने वर्गीकरण के बारे में अत्यधिक निश्चित है, जरूरी नहीं कि उपयोगकर्ता दोषी है।

### 8. अनिश्चितता स्वयं एक संकेत बन जाती है
यदि एआई अनिश्चित है (उदाहरण के लिए, खतरा: 0.62, व्यंग्य: 0.54), तो इसे केवल कठोर नियम लागू नहीं करने चाहिए। इसके बजाय, अनिश्चितता सीधे वास्तुकला में निर्मित होती है: **मानव समीक्षा आवश्यक**।

### 9. चार निर्णय क्षेत्र
- 🟢 **हरा**: अत्यधिक संभावित अनुपालन। → कोई कार्रवाई नहीं.
- 🟡 **पीला**: संभावित उल्लंघन। → यदि आवश्यक हो तो निगरानी करें/चेतावनी दें।
- 🟠 **नारंगी**: संभावित उल्लंघन। → मॉडरेशन समीक्षा.
- 🔴 **लाल**: गंभीर संभावित उल्लंघन। → तत्काल सुरक्षात्मक उपाय + मानवीय समीक्षा।

### 10. कोई "एआई सज़ा" नहीं
**एआई कोई अंतिम प्रतिबंध नहीं लगाता है।** यह गंभीर सुरक्षा चिंताओं के लिए तकनीकी तत्काल उपायों (उदाहरण के लिए, किसी संदेश को अस्थायी रूप से रोकना) को ट्रिगर कर सकता है, लेकिन अंतिम निर्णय सत्यापन योग्य रहता है।

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. एआई को अपने निर्णयों को सही ठहराने में सक्षम होना चाहिए
डीएसए को स्पष्ट और विशिष्ट कारणों की आवश्यकता है। एआई संरचित तर्क प्रदान करता है: नियम (एनजी-आचरण-004), पता लगाया गया (संभावित ठोस खतरा), आत्मविश्वास (0.94), प्रासंगिक संदर्भ (पिछले 4 संदेश), अनुशंसित कार्रवाई (मानव समीक्षा)।

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. एआई-जनित सामग्री
हम इनमें अंतर करते हैं: मानव-निर्मित, एआई-सहायता प्राप्त, एआई-जनित, और एआई-हेरफेर। यह सामग्री मेटाडेटा का हिस्सा बन जाएगा.

### 15. एआई सामग्री और एआई उद्गम परत की लेबलिंग
EU AI अधिनियम (अगस्त 2026 से प्रभावी) के पारदर्शिता नियमों के अनुसार, AI-जनित सामग्री पहचान योग्य होनी चाहिए। हम एक एआई प्रोवेंस लेयर प्रदान करते हैं जो मेटाडेटा (एआई-उत्पत्ति, मॉडल, टाइमस्टैम्प, मानव समीक्षा) संग्रहीत करता है।

### 16. डीपफेक डिटेक्शन
आर्किटेक्चर का लक्ष्य सिंथेटिक छवियों, क्लोन की गई आवाज़ों और डीपफेक का पता लगाना है। हालाँकि, पता लगाना स्वचालित रूप से प्रमाण नहीं है।

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. व्यंग्य, व्यंग्य और हास्य
एआई संदर्भ, इमोजी, वार्तालाप इतिहास और ज्ञात विडंबनापूर्ण संरचनाओं का उपयोग करता है, लेकिन जब अर्थ अस्पष्ट हों तो उसे अनिश्चितता की अनुमति देनी चाहिए।

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. झूठी सकारात्मकता, झूठी नकारात्मकता और गुणवत्ता मेट्रिक्स
त्रुटि प्रकारों की निगरानी की जाती है. एक डैशबोर्ड परिशुद्धता, रिकॉल और विशेष रूप से **अपील रिवर्सल दर** (सफल अपीलों की संख्या) को मापता है।

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. मानव ही अंतिम प्राधिकारी है
- **एनजी-एआई-एमओडी-001**: एआई पता लगाने और वर्गीकरण में सहायता करता है, लेकिन गंभीर निर्णयों में मानव समीक्षा को प्रतिस्थापित नहीं करता है।
- **एनजी-एआई-एमओडी-002**: स्वचालित मॉडरेशन निर्णय ट्रेस करने योग्य, लॉग करने योग्य और सत्यापन योग्य होने चाहिए।

**सारांश**: हम चार चरणों वाली प्रणाली बना रहे हैं: एआई डिटेक्शन, संदर्भ और जोखिम विश्लेषण, नीति इंजन और मानव प्रशासन। यह एक खतरनाक "एआई एज़ जज" आर्किटेक्चर बनाए बिना मजबूत स्वचालन को सक्षम बनाता है।

## Financing Principles and Revenue Model (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

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

### 3. विज्ञापन के बिना वित्तपोषण (6 स्तंभ)
वित्त पोषण छह स्तंभों पर बनाया गया है:
```पाठ
                 नेक्सस गाजा
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   प्रीमियम संगठन दान
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    अनुदान साझेदारी सेवाएँ
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

#### स्तंभ 6 - वाणिज्यिक सेवाएँ
B2B सेवाएँ जैसे **अनुवाद-ए-सेवा** (एपीआई), संगठनात्मक संचार, या अंतर्राष्ट्रीय सम्मेलन कक्ष, मानक उपयोगकर्ता फ़ीड पर बोझ डाले बिना।

### 4. कोई डेटा मुद्रीकरण और निगरानी अर्थव्यवस्था नहीं
**एनजी-फिन-003:** व्यक्तिगत उपयोगकर्ता डेटा कोई वस्तु नहीं है। सूचियों, प्रोफाइलों या इतिहासों की कोई बिक्री नहीं। नेक्सस गाजा को मनोवैज्ञानिक निगरानी (निगरानी अर्थव्यवस्था) से लाभ नहीं होता है।

### 5. वित्तीय पारदर्शिता एवं फंड लेजर
**नेक्सस गाजा वित्तीय पारदर्शिता:** समग्र वित्तीय संरचनाओं का प्रकाशन। निर्धारित दान को तकनीकी लेखांकन प्राप्त होता है (फंड आईडी → उद्देश्य → शेष → आवंटन)। कॉरपोरेट मार्केटिंग में सामाजिक उद्देश्यों के लिए कोई क्रॉस-सब्सिडी नहीं।

### 6. एकजुटता-आधारित वित्तपोषण मॉडल
मूल्य-निर्धारण लागत-अभिविन्यास, निष्पक्षता और एकजुटता पर आधारित है।
**सॉलिडैरिटी प्रीमियम:** प्रीमियम उपयोगकर्ताओं के लिए किसी अन्य उपयोगकर्ता की पहुंच के एक हिस्से को वित्तपोषित करने का एक स्वैच्छिक विकल्प। जबरन एकजुटता या प्रीमियम वर्ग का समाज (मुक्त उपयोगकर्ताओं के लिए कम सम्मान/संयम) सख्त वर्जित है।

### 7. सगाई अर्थव्यवस्था के बजाय आर्थिक KPIs
उपयोगकर्ताओं को "जब तक संभव हो सके ऑनलाइन" रखने पर कोई निर्भरता नहीं (कोई रेजबेट नहीं, अनंत फ़ीड)।
इसके बजाय, हम मेट्रिक्स का उपयोग करते हैं जैसे:
- **वैश्विक संचार सूचकांक (जीसीआई):** विभिन्न भाषाई/सांस्कृतिक क्षेत्रों के लोगों के बीच सफल संचार संबंध।
- **प्लेटफ़ॉर्म स्थिरता अनुपात (पीएसआर):** आवर्ती राजस्व / आवर्ती परिचालन लागत (लक्ष्य ≥ 1)।

### 8. हम स्पष्ट रूप से क्या नहीं चाहते (नकारात्मक सूची)
नेक्सस गाजा को **नहीं** वित्तपोषित किया जाता है:
❌ व्यक्तिगत डेटा की बिक्री
❌ वैयक्तिकृत पारंपरिक विज्ञापन
❌ विज्ञापन उद्देश्यों के लिए उपयोगकर्ता के व्यवहार की निगरानी करना
❌ निजी संचार डेटा की बिक्री
❌ छिपा हुआ AI डेटा उपयोग
❌ मैनिपुलेटिव प्रीमियम पेवॉल्स
मुद्रीकरण के लिए कृत्रिम पहुंच प्रतिबंध
❌ भुगतान किया गया राजनीतिक प्रभाव
❌ विशेषाधिकार प्राप्त मॉडरेशन निर्णयों की खरीद।

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

## API, Interfaces, and Communication Architecture (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### मूल सिद्धांत
- **कोई प्रत्यक्ष डेटाबेस एक्सेस नहीं:** घटक विशेष रूप से परिभाषित इंटरफेस (एपीआई या इवेंट) के माध्यम से संचार करते हैं, कभी भी अन्य सेवाओं के प्रत्यक्ष डेटाबेस प्रश्नों के माध्यम से नहीं।
- **एपीआई गेटवे:** सभी बाहरी क्लाइंट अनुरोध प्रमाणीकरण, रूटिंग और दर सीमित करने वाले एपीआई गेटवे के माध्यम से रूट करते हैं।
- **प्रदाता अमूर्त:** बाहरी सेवाओं (एआई मॉडल, भुगतान प्रदाता, अनुवाद इंजन) को अमूर्त परतों के माध्यम से एकीकृत किया जाता है, हार्डकोडेड निर्भरता से बचा जाता है और लचीले प्रदाता स्वैपिंग को सक्षम किया जाता है।

### संचार पैटर्न
- **सिंक्रोनस एपीआई (REST/HTTPS):** लॉगिन, प्रोफ़ाइल सेटिंग्स या सीधे अनुवाद जैसे तत्काल अनुरोधों के लिए उपयोग किया जाता है।
- **एसिंक्रोनस इवेंट्स (इवेंट बस):** विलंबित, डिकौपल्ड प्रोसेसिंग के लिए नेक्सस गाजा का केंद्रीय तंत्रिका तंत्र (उदाहरण के लिए, `मैसेज.क्रिएटेड` मॉडरेशन, ट्रांसलेशन और नोटिफिकेशन को एसिंक्रोनस रूप से ट्रिगर करता है)।
- **रीयलटाइम (वेबसॉकेट):** लाइव चैट और टाइपिंग संकेतकों के लिए समर्पित चैनल।

### सुरक्षा और विश्वसनीयता
- **जीरो-ट्रस्ट मॉडल:** आंतरिक नेटवर्क ट्रैफ़िक पर स्वचालित रूप से भरोसा नहीं किया जाता है; संवेदनशील सेवा-से-सेवा संचार के लिए प्रमाणीकरण की आवश्यकता होती है।
- **निष्क्रियता और आउटबॉक्स पैटर्न:** महत्वपूर्ण संचालन (जैसे दान या संदेश) को डुप्लिकेट प्रसंस्करण को रोकने के लिए निष्क्रिय बनाया गया है, आउटबॉक्स पैटर्न का उपयोग यह सुनिश्चित करने के लिए किया जाता है कि डेटाबेस लेनदेन के दौरान भी घटनाएं कभी न खोएं।

## एमवीपी डोमेन मॉडल (डब्ल्यूपी 1.12)

![नेक्सस गाजा मॉड्यूलर मोनोलिथ](assets/img/nexus_architecture.jpg)

नेक्सस गाजा एक सख्ती से डोमेन-संचालित एमवीपी आर्किटेक्चर (एडीआर-025) को नियोजित करता है, जिसे स्पष्ट डोमेन सीमाओं के साथ एक मॉड्यूलर मोनोलिथ के रूप में डिज़ाइन किया गया है। यह संरचना बाद में विशिष्ट डोमेन को विभाजित करने के लचीलेपन को बनाए रखते हुए समय से पहले माइक्रोसर्विस जटिलता को रोकती है।

### कोर डोमेन इकाइयाँ
आर्किटेक्चर डेटा अखंडता सुनिश्चित करने और "उपयोगकर्ता नाम = मानव" जैसे संरचनात्मक नुकसान से बचने के लिए स्पष्ट रूप से अलग-अलग अवधारणाओं को अलग करता है:
- **पहचान और खाते:** `व्यक्ति` ≠ `उपयोगकर्ता खाता` ≠ `पहचान सत्यापन`। एक सत्यापित व्यक्ति एक खाते के माध्यम से भाग लेता है, लेकिन इकाइयाँ अलग रहती हैं।
- **संचार:** `संदेश` ≠ `अनुवाद`। मूल संदेश अपरिवर्तनीय रहता है; अनुवाद जुड़े हुए निकाय हैं।
- **संयम:** `रिपोर्ट` ≠ `संयम निर्णय`। एक रिपोर्ट महज़ एक दावा है; एक मॉडरेशन मामले की जांच की जाती है।
- **वित्त:** `दान` ≠ `फंड बैलेंस`। वित्तीय पारदर्शिता सुनिश्चित करते हुए, भुगतान को एक अपरिवर्तनीय बहीखाता के माध्यम से फंड में बुक किया जाता है।

### इंटरकनेक्टेड डोमेन
सिस्टम को स्पष्ट तार्किक डोमेन (बद्ध संदर्भ) में विभाजित किया गया है: पहचान, खाता, संगठन, संचार, समुदाय, भाषा, मॉडरेशन, अधिसूचना, वित्त और शासन। ये डोमेन वास्तविक दुनिया की संस्थाओं (उपयोगकर्ताओं, स्कूलों, एनजीओ) से लेकर उनके डिजिटल इंटरैक्शन और संबंधित प्रशासन तक की पूरी यात्रा को मैप करते हैं।

## परियोजना की स्थिति
परियोजना वर्तमान में सक्रिय वास्तुकला और योजना चरण में है।
चल रहे वास्तुशिल्प निर्णयों को `/docs` फ़ोल्डर में प्रलेखित किया जाता है।

---

---

## लाइसेंस एवं बौद्धिक संपदा

> **© 2024–2026 जनवरी सोनर / सोनरस्टूडियो - सर्वाधिकार सुरक्षित।**

**नेक्सस गाजा** **जन सोनर** की विशिष्ट बौद्धिक संपदा है, जो **सोनरस्टूडियो** के अंतर्गत संचालित होती है।

जान सोननर नेक्सस गाजा के एकमात्र निर्माता, वास्तुकार और मालिक हैं - जिसमें सभी अवधारणाएं, वास्तुकला, डोमेन मॉडल, ब्रांड पहचान और संबंधित दस्तावेज़ शामिल हैं।

**कोई भी अधिकार, लाइसेंस या स्वामित्व हित किसी तीसरे पक्ष के पास नहीं है**, चाहे उनका आकार, बाजार स्थिति, या प्रौद्योगिकी उद्योग में प्रभाव कुछ भी हो।

### स्पष्ट लिखित सहमति के बिना क्या अनुमति नहीं है:
- इस सॉफ़्टवेयर या इसके दस्तावेज़ की प्रतिलिपि बनाना, पुन: प्रस्तुत करना या वितरित करना
- व्युत्पन्न कार्यों को संशोधित करना, अनुकूलित करना या बनाना
- नेक्सस गाजा के किसी भी हिस्से का व्यावसायिक उपयोग
- एआई या एलएलएम सिस्टम के लिए प्रशिक्षण डेटा के रूप में इस भंडार की सामग्री का उपयोग करना
- उपलाइसेंस देना या किसी अधिकार को तीसरे पक्ष को हस्तांतरित करना

### संरक्षित बौद्धिक संपदा
निम्नलिखित मूल अवधारणाएँ जन सोनर के व्यापार रहस्यों और मालिकाना कृतियों के रूप में संरक्षित हैं:
- स्तरित संचार मॉडल (मूल, शब्दार्थ व्याख्या, अनुवादित आउटपुट)
- पहचान पृथक्करण सिद्धांत (व्यक्ति खाता नहीं है पहचान सत्यापन नहीं है)
- संदेश-अनुवाद डिकॉउलिंग मॉडल (संदेश अनुवाद नहीं है)
- एआई मॉडरेशन गवर्नेंस फ्रेमवर्क

### संपर्क करें
लाइसेंस संबंधी पूछताछ के लिए: https://github.com/SonnerStudio

नेक्सस गाजा और नेक्सस गाजा लोगो जान सोनर के ट्रेडमार्क हैं। नाम या ब्रांड का अनधिकृत उपयोग निषिद्ध है।

LICENSE फ़ाइल में पूर्ण लाइसेंस शर्तें देखें।
