# Nexus Gaja

![Nexus Gaja Logo](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** is an intelligent, context-sensitive communication network designed to revolutionize global communication.

## Purpose and Vision

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

در دنیای جهانی شده، زبان اغلب بزرگترین مانع است. هدف اصلی Nexus Gaja برقراری ارتباط یکپارچه، بدون مانع و با زمینه دقیق بین افراد است - صرف نظر از اینکه آنها به یک زبان مشترک صحبت می کنند یا خیر.

این فقط در مورد ترجمه دقیق کلمات نیست، بلکه در مورد **انتقال معنا ** است. Nexus Gaja با درک تفاوت‌های فرهنگی، منطقه‌ای و زمینه‌ای، افراد را در سطح عمیق‌تری به هم متصل می‌کند و در نتیجه امکان گفتگوهای واقعی و معتبر را فراهم می‌کند.

## امکانات و ویژگی ها
- **ارتباطات چند رسانه ای**: سیستم نه تنها متن، بلکه تصویر، صدا و ویدئو را نیز پردازش می کند. این اجازه می دهد تا مکالمات کاملاً همه جانبه (مانند تماس های ویدیویی یا پیام های صوتی) را در زمان واقعی از طریق موانع زبانی انجام دهید.
- **حساسیت زمینه**: شناخت کنایه، اصطلاحات، اصطلاحات و گویش های منطقه ای که اغلب توسط مترجمان مرسوم به اشتباه درک می شوند.
- **شبکه متقابل پلتفرم**: به عنوان پایه ای برای چت های خصوصی، موضوعات انجمن (پست ها با نظر) و تعاملات بین جامعه جهانی عمل می کند.

---

## معماری فنی (مفهوم اصلی)

![مفهوم ترجمه Nexus Gaja](assets/img/nexus_translation.jpg)

هسته فنی Nexus Gaja یک مدل ارتباطی سفارشی است که به طور دقیق به سه لایه تقسیم می شود:

1. **Original**: The communication object (message) created by the sender always remains immutable.
2. **Semantic Interpretation**: The system analyzes not just the words, but the actual meaning.
3. **Target Language Representation**: The AI merely creates a temporary or cached representation of the original for the respective recipient based on their preferred language. Translations never overwrite the original message.

### Context Dependency
Translations in Nexus Gaja never view messages in isolation. The engine considers the entire hierarchy:
`Message` → `Previous Messages` → `Thread Context` → `Community Context` → `Language / Region` → `User Preferences`

### Efficiency through On-Demand Translation
Translation occurs resource-efficiently only **upon request** (On-Demand). When a user requests content, it is translated into their preset language. Once a translation for a specific language is generated, it is permanently stored (caching) to drastically accelerate future requests.

## تعدیل به کمک هوش مصنوعی (WP 1.8.4)

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

با تعدیل به کمک هوش مصنوعی، با در نظر گرفتن مقررات جاری اتحادیه اروپا (الزامات شفافیت قانون هوش مصنوعی اتحادیه اروپا بر اساس ماده 50؛ قانون خدمات دیجیتال با توجیهات قابل فهم و گزینه های تجدیدنظر) گام مهمی از ایده محصول به معماری فنی برمی داریم.

### 1. اصل اساسی
مهمترین جمله برای معماری این است: ** هوش مصنوعی تعدیل یک سیستم بررسی است، نه یک سیستم حاکم مستقل.**
این برای کمک به انسان در حد اعتدال طراحی شده است، نه اینکه خودش تعیین کند که کدام عقاید مجاز به وجود در Nexus Gaja هستند.
ما بین سه سطح تفاوت قائل می شویم:
- **تشخیص:** "در اینجا ممکن است یک قانون نقض شود."
- **ارزیابی:** "احتمال نقض قانون مثلاً 94 درصد است."
- **تصمیم:** "در واقع چه اقدامی انجام شده است؟"
سطح سوم در موارد شدید باید توسط انسان کنترل شود.

### 2. هوش مصنوعی Moderation به عنوان یک زیرسیستم
به جای یک هوش مصنوعی واحد، یک زیر سیستم قوی ایجاد می شود:
``متن
                 NEXUS GAJA AI MODERATION
                          │
       ┌──────────────────┼──
       │ │ │
  زبان AI Safety AI Fraud AI
       │ │ │
       ├──────────────┬───┴───
       │ │ │
 هویت رفتار ترجمه
 سیگنال های تحلیل آنالیز
       │ │ │
       └──────────────┼────-
                      ▼
               ارزیابی ریسک
                      │
                      ▼
               بررسی انسانی
```

### 3. مهم ترین ماژول های هوش مصنوعی
Nexus Gaja از نه حوزه تجزیه و تحلیل تخصصی استفاده می کند:
- **M1 - درک زبان **: زبان، گویش، عامیانه، شاخص های کنایه، مسائل ترجمه را تشخیص می دهد.
- **M2 - سمیت / تشخیص سوء استفاده **: توهین، حملات شخصی، آزار و اذیت را تشخیص می دهد.
- **M3 - شناسایی تهدید**: تهدیدهای بالقوه، باج خواهی، اعلامیه های خشونت را تشخیص می دهد.
- **M4 - تشخیص نفرت / غیرانسانی سازی **: حملات هدفمند به افراد را بر اساس وابستگی های خاص تشخیص می دهد.
- **M5 - Spam / Manipulation Detection **: هرزنامه، رفتار ربات، دستکاری هماهنگ را تشخیص می دهد.
- **M6 - کشف تقلب**: تلاش های مشکوک به کلاهبرداری، فیشینگ، مهندسی اجتماعی را شناسایی می کند.
- **M7 - یکپارچگی هویت **: سیگنال های مربوط به تصاحب حساب، چندین حساب، ممنوعیت فرار را بررسی می کند.
- **M8 - ایمنی رسانه**: تصاویر، صدا، ویدئو، اسناد را تجزیه و تحلیل می کند.
- **M9 – Context Engine**: مهمترین ماژول. یافته های فردی را ادغام می کند.

### 4. چرا Context Engine بسیار مهم است
جستجوی کلمه کلیدی خالص کافی نخواهد بود. "من می توانستم او را از خنده بکشم" از نظر معنایی حاوی خشونت است اما یک شکل گفتاری است. «فردا ساعت 20 جلوی در خانه اش تیراندازی می کنم» وضعیتی کاملا متفاوت است. هوش مصنوعی باید بفهمد که این بیانیه در زمینه خاص خود به چه معناست.

### 5. تعدیل چند زبانه
اعتدال نمی تواند به سادگی کلمات را با هم مقایسه کند. باید سطح معنایی را تجزیه و تحلیل کند (به عنوان مثال، اصطلاحات آلمانی در مقابل اصطلاحات ژاپنی در مقابل عبارات منطقه ای).

### 6. زبان اصلی + ترجمه
اصل و ترجمه به طور جداگانه تجزیه و تحلیل می شوند. تنها پس از آن "ارزیابی اعتدال ترکیبی" انجام می شود. این به Nexus Gaja اجازه می‌دهد تا تعیین کند که آیا خود ترجمه ممکن است واقعیت‌ها را افزایش داده یا تغییر داده باشد.

### 7. امتیاز اعتماد به نفس
هر ارزیابی هوش مصنوعی یک امتیاز اطمینان دریافت می کند (به عنوان مثال، احتمال تهدید: 0.96). با این حال: **امتیاز اطمینان ≠ حقیقت.** امتیاز 96٪ فقط به این معنی است که مدل از طبقه بندی خود کاملاً مطمئن است، نه لزوماً اینکه کاربر مقصر است.

### 8. عدم قطعیت خود به یک سیگنال تبدیل می شود
اگر هوش مصنوعی نامشخص باشد (به عنوان مثال، تهدید: 0.62، طنز: 0.54)، نباید صرفاً قوانین خشن را اجرا کند. در عوض، عدم قطعیت مستقیماً در معماری ایجاد می‌شود: **بازبینی انسانی الزامی است**.

### 9. چهار منطقه تصمیم گیری
- **سبز **: به احتمال زیاد سازگار است. → بدون اقدام
- **زرد**: تخلف احتمالی. → نظارت کنید / در صورت لزوم یک هشدار ارائه دهید.
- **نارنجی**: تخلف احتمالی. → بررسی اعتدال.
- 🔴 **قرمز**: تخلف شدید احتمالی. ← اقدام حفاظتی فوری + بررسی انسانی.

### 10. بدون "مجازات هوش مصنوعی"
**هوش مصنوعی هیچ تحریم نهایی را اعمال نمی‌کند.** می‌تواند اقدامات فنی فوری (مثلاً توقف موقت پیام) را برای نگرانی‌های شدید امنیتی ایجاد کند، اما تصمیم نهایی همچنان قابل تأیید است.

### 11. اقدامات حفاظتی می تواند به طور خودکار رخ دهد
در صورت تهدید ملموس (تهدید شناسایی شده ← اطمینان بالا ← محدودیت موقت ← بازبینی انسانی ← تصمیم)، ما از کاربر تهدید شده بدون تبدیل هوش مصنوعی به قاضی محافظت می کنیم.

### 12. هوش مصنوعی باید بتواند تصمیمات خود را توجیه کند
DSA به دلایل روشن و مشخصی نیاز دارد. هوش مصنوعی استدلال ساختاری را ارائه می دهد: قانون (NG-CONDUCT-004)، شناسایی شده (تهدید بتن بالقوه)، اطمینان (0.94)، زمینه مرتبط (4 پیام قبلی)، اقدام توصیه شده (بازبینی انسانی).

### 13. هوش مصنوعی نباید مخفیانه محتوا را تغییر دهد
**هوش مصنوعی اعتدال هرگز نباید محتوای اصلی را بدون توجه تغییر دهد.** در طول تصحیح، ترجمه یا خلاصه سازی خودکار، متن اصلی همیشه حفظ می شود.

### 14. محتوای تولید شده توسط هوش مصنوعی
ما بین: ایجاد شده توسط انسان، با کمک هوش مصنوعی، تولید شده توسط هوش مصنوعی و دستکاری شده توسط هوش مصنوعی تمایز قائل می شویم. این بخشی از ابرداده محتوا خواهد شد.

### 15. برچسب گذاری محتوای هوش مصنوعی و لایه منشأ هوش مصنوعی
بر اساس قوانین شفافیت قانون هوش مصنوعی اتحادیه اروپا (قابل اجرا در اوت 2026)، محتوای تولید شده توسط هوش مصنوعی باید قابل شناسایی باشد. ما یک لایه منشأ هوش مصنوعی ارائه می دهیم که ابرداده ها (AI-Origin، Model، Timestamp، Human Review) را ذخیره می کند.

### 16. تشخیص Deepfake
هدف این معماری تشخیص تصاویر مصنوعی، صداهای شبیه سازی شده و دیپ فیک است. با این حال، تشخیص به طور خودکار اثبات نیست.

### 17. بدون "ماشین حقیقت" خودکار (اعتدال ≠ بررسی واقعیت)
یک سیستم چک می کند: "آیا محتوا قوانین را نقض می کند؟" (Content Moderation)، دیگری ارائه می دهد: "چه اطلاعات و منابعی در دسترس است؟" (کمک اطلاعاتی). نظرات صرفاً به دلیل "اشتباه" بودن حذف نمی شوند.

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. بدون مجازات بر اساس یک امتیاز هوش مصنوعی
هیچ مداخله تعدیل شدید ممکن است تنها بر اساس یک نتیجه طبقه بندی خودکار منفرد باشد (متن + زمینه + رفتار + زبان + رسانه + موتور قانون = ارزیابی ریسک).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. هوش مصنوعی اعتدالی باید قابل کنترل باشد
همه تصمیمات خودکار مربوطه ثبت می شوند (شناسه رویداد، شناسه قانون، اطمینان، بازبینی انسانی، و غیره) تا از قابلیت ردیابی اطمینان حاصل شود.

### 23. معیارهای مثبت کاذب، منفی کاذب و معیارهای کیفیت
انواع خطا نظارت می شود. داشبورد دقت، یادآوری، و به ویژه **نرخ بازگشت تجدیدنظر** (تعداد درخواست های تجدیدنظر موفق) را اندازه گیری می کند.

### 24. برابری زبان و تعصب ترجمه
کیفیت تعدیل باید در همه زبان های پشتیبانی شده قابل مقایسه باشد (معیار تعدیل چند زبانه). اگر نتایج تعدیل بین نسخه اصلی و ترجمه متفاوت باشد (تضاد ترجمه)، این باید به طور خاص بررسی شود.

### 25. موتور پیشنهاد و سیاست معماری
قوانین (موتور سیاست) در مدل‌های هوش مصنوعی کدگذاری نشده است. هوش مصنوعی یافته هایی را ارائه می دهد. موتور سیاست بر اساس قوانین جاری تصمیم می گیرد. این امکان را برای **تغییر مدل بدون تغییر قانون** فراهم می کند.

### 26. انسان اقتدار نهایی باقی می ماند
- **NG-AI-MOD-001**: هوش مصنوعی به شناسایی و طبقه بندی کمک می کند، اما در تصمیم گیری های شدید جایگزین بررسی انسانی نمی شود.
- **NG-AI-MOD-002**: تصمیمات تعدیل خودکار باید قابل ردیابی، ثبت و تأیید باشند.

**خلاصه**: ما در حال ساختن یک سیستم چهار مرحله ای هستیم: تشخیص هوش مصنوعی، تحلیل زمینه و ریسک، موتور سیاست گذاری، و مدیریت انسانی. این امر اتوماسیون قوی را بدون ایجاد معماری خطرناک «AI as Judge» امکان پذیر می کند.

## اصول تامین مالی و مدل درآمد (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

برای Nexus Gaja، یک اصل اقتصادی بسیار مهم اعمال می‌شود: **بدون تبلیغات سنتی در پلتفرم.**
این موضوع اساساً Nexus Gaja را از بسیاری از شبکه های اجتماعی امروزی متمایز می کند. با این حال، این بدان معنا نیست که Nexus Gaja نمی تواند یک شخصیت تجاری داشته باشد. برعکس، این پلتفرم باید از نظر اقتصادی مقرون به صرفه باشد تا هدف اجتماعی آن پایدار بماند. فعالیت اقتصادی وسیله ای برای رسیدن به هدف است، نه هدف اصلی پلت فرم.

### 1. Principle NG-FIN-001
Nexus Gaja finances its operations through transparent revenue streams separated from user interests, and not through the monetization of its users' attention or personal data.

### 2. بدون تبلیغات سنتی
به طور خاص ممنوع هستند:
- تبلیغات بنری
- تبلیغات پاپ آپ
- پخش خودکار تبلیغات ویدیویی
- پست های حمایت شده در فید استاندارد
- پروفایل های تبلیغاتی شخصی
- فروش پروفایل های کاربر یا اطلاعات شخصی
- تبلیغات ناشی از گفتگوهای خصوصی.

Nexus Gaja remains a **communication space rather than an advertising space**.

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

#### ستون 2 - پیشنهادات برتر
پیشنهادات پولی داوطلبانه (**Nexus Gaja Plus**) محدودیت‌های ذخیره‌سازی بیشتر، کیفیت رسانه بالاتر، سهمیه‌های هوش مصنوعی گسترده و ویژگی‌های سازمانی را ارائه می‌کنند.
**مهم (Freemium به جای Dark Freemium):** ارتباطات پایه هرگز نباید به طور مصنوعی تخریب شود.

#### Pillar 3 – Organizations
Special accounts for schools, universities, NGOs, businesses, and municipalities (**Nexus Gaja Organization**). Schools can be supported via institutional rates as multipliers of international understanding.

#### Pillar 4 – Donations
The **Nexus Gaja Funding Pool** accepts general and earmarked donations (e.g., "for international youth communication"). A **Fund Allocation Ledger** ensures transparent allocation of funds.
**Purpose Fund & Tombola:** A portion of donations feeds a pool for free/discounted usage. A lottery/tombola mechanism can allocate these funds transparently and auditably.

#### رکن 5 – تامین مالی نهادی
بنیادها، برنامه های تأمین مالی فرهنگی یا برنامه های دولتی.
**NG-FIN-002:** پشتیبانی مالی کنترل تحریریه یا فنی (استقلال) را خریداری نمی کند.

#### رکن 6 – خدمات بازرگانی
خدمات B2B مانند **Translation-as-a-Service** (API)، ارتباطات سازمانی، یا اتاق های کنفرانس بین المللی، بدون بارگذاری بر فید استاندارد کاربر.

### 4. No Data Monetization & Surveillance Economy
**NG-FIN-003:** Personal user data is not a commodity. No sale of lists, profiles, or histories. Nexus Gaja does not profit from psychological surveillance (Surveillance Economy).

### 5. شفافیت مالی و دفتر صندوق
**شفافیت مالی Nexus Gaja:** انتشار ساختارهای مالی انبوه. کمک های اختصاصی حسابداری فنی دریافت می کنند (شناسه صندوق → هدف → مانده → تخصیص). عدم یارانه متقابل اهداف اجتماعی در بازاریابی شرکتی.

### 6. مدل تامین مالی مبتنی بر همبستگی
قیمت گذاری بر اساس هزینه گرایی، انصاف و همبستگی است.
**Solidarity Premium:** گزینه ای داوطلبانه برای کاربران Premium برای تامین مالی بخشی از دسترسی کاربر دیگر. همبستگی اجباری یا جامعه طبقه ممتاز (احترام/اعتدال کمتر برای کاربران رایگان) اکیداً ممنوع است.

### 7. شاخص های کلیدی عملکرد اقتصادی به جای اقتصاد تعاملی
بدون وابستگی به نگه داشتن کاربران "تا زمانی که ممکن است آنلاین" (بدون راگبایت، فیدهای بی نهایت).
در عوض، ما از معیارهایی مانند:
- **شاخص ارتباطات جهانی (GCI):** روابط ارتباطی موفق بین افراد از مناطق مختلف زبانی/فرهنگی.
- **نسبت پایداری پلتفرم (PSR): ** درآمد مکرر / هزینه های عملیاتی مکرر (هدف ≥ 1).

### 8. آنچه ما آشکارا نمی خواهیم (فهرست منفی)
Nexus Gaja **نه** توسط:
❌ فروش اطلاعات شخصی
❌ تبلیغات سنتی شخصی
❌ نظارت بر رفتار کاربران برای اهداف تبلیغاتی
❌ فروش داده های ارتباطی خصوصی
❌ استفاده از داده های هوش مصنوعی پنهان
❌ دیوارهای پرداخت حق بیمه دستکاری
❌ محدودیت دسترسی مصنوعی برای کسب درآمد
❌ نفوذ سیاسی پولی
❌ خرید تصمیمات اعتدال ممتاز.

### 9. معماری مالی مقدماتی
``متن
                         NEXUS GAJA
                              │
             ┌────────────────┼────
             │ │ │
             ▼ ▼ ▼
          كاربران سازمان ENTERPRISE
             │ │ │
             └────────────────┼────
                              │
                       خدمات پلت فرم
                              │
          ┌──────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API PREMIUM DONATIONS
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               GENERAL FUND RESTRICTED FUNDS
                                        │
                                        ▼
                                  هدف اجتماعی
```

### خلاصه اصول تامین مالی (NG-FIN)
- **NG-FIN-001:** بدون تامین مالی از طریق تبلیغات سنتی.
- **NG-FIN-002:** بدون کنترل ویرایشی/فنی از طریق حمایت مالی.
- **NG-FIN-003:** داده های شخصی یک کالا نیست.
- **NG-FIN-004:** ارتباطات اولیه بدون پرداخت قابل دسترسی است.
- **NG-FIN-005:** پیشنهادهای ممتاز نباید باعث تنزل کاربران رایگان شود.
- **NG-FIN-006:** وجوه اختصاصی بر اساس هدفشان مدیریت می شوند.
- **NG-FIN-007:** مدیریت شفاف کمک های مالی و کمک های مالی.
- **NG-FIN-008: ** خدمات تجاری B2B استقلال را به خطر نمی اندازد.
- **NG-FIN-009: ** تمرکز بر پایداری به جای حداکثر درآمدزایی.
- **NG-FIN-010:** ساختار به طور دائم هدف اجتماعی را تضمین می کند.

## API، رابط‌ها و معماری ارتباطات (WP 1.11.3)

برای اطمینان از ثبات، امنیت و مقیاس‌پذیری سیستم، Nexus Gaja از معماری کاملاً مبتنی بر API و رویداد محور پیروی می‌کند.

### اصول اصلی
- **دسترسی مستقیم به پایگاه داده:** مؤلفه ها منحصراً از طریق رابط های تعریف شده (API یا رویدادها) ارتباط برقرار می کنند، هرگز از طریق جستجوهای مستقیم پایگاه داده سایر سرویس ها.
- **درگاه API:** تمام درخواست های مشتری خارجی از طریق یک API Gateway که احراز هویت، مسیریابی و محدود کردن نرخ را مدیریت می کند، می گذرد.
- **انتزاع ارائه دهنده:** خدمات خارجی (مدل های هوش مصنوعی، ارائه دهندگان پرداخت، موتورهای ترجمه) از طریق لایه های انتزاعی ادغام می شوند، از وابستگی های کدگذاری شده اجتناب می کنند و امکان تعویض ارائه دهنده انعطاف پذیر را فراهم می کنند.

### الگوهای ارتباطی
- ** APIهای همزمان (REST/HTTPS):** برای درخواست‌های فوری مانند ورود به سیستم، تنظیمات نمایه یا ترجمه مستقیم استفاده می‌شود.
- **رویدادهای ناهمزمان (اتوبوس رویداد):** سیستم عصبی مرکزی Nexus Gaja برای پردازش تأخیری و جداشده (مثلاً «پیام. ایجاد شده» که باعث تعدیل، ترجمه و اعلان به صورت ناهمزمان می‌شود).
- ** بیدرنگ (WebSocket): ** کانال های اختصاصی برای چت زنده و نشانگرهای تایپ.

### امنیت و قابلیت اطمینان
- ** مدل صفر اعتماد: ** ترافیک شبکه داخلی به طور خودکار قابل اعتماد نیست. ارتباطات حساس سرویس به سرویس نیاز به احراز هویت دارد.
- **ناتوانی و الگوی صندوق خروجی:** عملیات حیاتی (مانند کمک های مالی یا پیام رسانی) به گونه ای طراحی شده اند که از پردازش تکراری جلوگیری کنند و از الگوی صندوق خروجی استفاده می کنند تا اطمینان حاصل شود که رویدادها هرگز حتی در طول تراکنش های پایگاه داده از بین نمی روند.

## مدل دامنه MVP (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja employs a strictly Domain-Driven MVP Architecture (ADR-025), designed as a modular monolith with clear domain boundaries. This structure prevents premature microservice complexity while retaining the flexibility to split out specific domains later.

### Core Domain Entities
The architecture explicitly separates distinct concepts to ensure data integrity and avoid structural pitfalls like "Username = Human":
- **Identity & Accounts:** `Person` ≠ `User Account` ≠ `Identity Verification`. A verified person participates via an account, but the entities remain separate.
- **Communication:** `Message` ≠ `Translation`. The original message remains immutable; translations are linked entities.
- **Moderation:** `Report` ≠ `Moderation Decision`. A report is merely a claim; a moderation case conducts the investigation.
- **Finances:** `Donation` ≠ `Fund Balance`. Payments are booked via an immutable ledger to a fund, ensuring financial transparency.

### دامنه های به هم پیوسته
این سیستم به حوزه‌های منطقی واضح (زمینه‌های محدود) تقسیم می‌شود: هویت، حساب، سازمان، ارتباطات، جامعه، زبان، تعدیل، اطلاع‌رسانی، امور مالی و حکومت. این دامنه‌ها کل سفر را از موجودیت‌های دنیای واقعی (کاربران، مدارس، سازمان‌های غیردولتی) تا تعاملات دیجیتالی و حاکمیت مرتبط ترسیم می‌کنند.

## Project Status
The project is currently in the active architecture and planning phase.
Ongoing architectural decisions are documented in the `/docs` folder.


---

---

## مجوز و مالکیت معنوی

> **© 2024–2026 Jan Sonner / SonnerStudio — کلیه حقوق محفوظ است.**

**Nexus Gaja** مالکیت معنوی انحصاری **Jan Sonner** است که تحت **SonnerStudio** کار می کند.

Jan Sonner تنها خالق، معمار و مالک Nexus Gaja است - از جمله تمام مفاهیم، ​​معماری، مدل‌های دامنه، هویت برند، و اسناد مرتبط.

**هیچ حقوق، مجوز، یا منافع مالکیتی در اختیار هیچ شخص ثالثی نیست**، صرف نظر از اندازه، موقعیت بازار، یا نفوذ آنها در صنعت فناوری.

### چه چیزی بدون رضایت کتبی صریح مجاز نیست:
- کپی، تکثیر یا توزیع این نرم افزار یا مستندات آن
- اصلاح، اقتباس، یا ایجاد آثار مشتق شده
- استفاده تجاری از هر قسمت از Nexus Gaja
- استفاده از محتویات این مخزن به عنوان داده های آموزشی برای سیستم های AI یا LLM
- صدور مجوز فرعی یا انتقال هر گونه حقوق به اشخاص ثالث

### مالکیت معنوی حفاظت شده
مفاهیم اصلی زیر به عنوان اسرار تجاری و خلاقیت های اختصاصی Jan Sonner محافظت می شوند:
- مدل ارتباط لایه ای (اصلی، تفسیر معنایی، خروجی ترجمه شده)
- اصل جداسازی هویت (شخص حساب نیست تایید هویت نیست)
- مدل جداسازی پیام-ترجمه (پیام ترجمه نیست)
- چارچوب حاکمیت تعدیل هوش مصنوعی

### تماس بگیرید
برای درخواست مجوز: https://github.com/SonnerStudio

Nexus Gaja و آرم Nexus Gaja علائم تجاری Jan Sonner هستند. استفاده غیرمجاز از نام یا برند ممنوع است.

شرایط کامل مجوز را در فایل LICENSE مشاهده کنید.
