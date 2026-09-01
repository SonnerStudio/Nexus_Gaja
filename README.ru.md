# Нексус Гайя

![Логотип Nexus Gaja](assets/logo.jpg)

![Nexus Gaja Hero](assets/img/nexus_hero.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** — это интеллектуальная, контекстно-зависимая коммуникационная сеть, призванная совершить революцию в глобальной коммуникации.

## Purpose and Vision

![Nexus Gaja Vision](assets/img/nexus_vision.jpg)

В глобализированном мире язык зачастую является самым большим барьером. Основная цель Nexus Gaja — обеспечить беспрепятственное, безбарьерное и контекстуально точное общение между людьми, независимо от того, говорят ли они на одном языке.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

![Концепция перевода Nexus Gaja](assets/img/nexus_translation.jpg)

Техническое ядро ​​Nexus Gaja — это специально разработанная модель связи, строго разделенная на три уровня:

1. **Оригинал**: объект связи (сообщение), созданный отправителем, всегда остается неизменным.
2. **Семантическая интерпретация**: система анализирует не только слова, но и их фактическое значение.
3. **Представление на целевом языке**: ИИ просто создает временное или кэшированное представление оригинала для соответствующего получателя на основе предпочитаемого им языка. Переводы никогда не перезаписывают исходное сообщение.

### Зависимость от контекста
Переводчики в Nexus Gaja никогда не рассматривают сообщения изолированно. Движок учитывает всю иерархию:
`Сообщение` → `Предыдущие сообщения` → `Контекст темы` → `Контекст сообщества` → `Язык/регион` → `Пользовательские настройки`

### Эффективность благодаря переводу по требованию
Перевод осуществляется с минимальным использованием ресурсов только **по запросу** (по требованию). Когда пользователь запрашивает контент, он переводится на заданный им язык. После создания перевода для определенного языка он постоянно сохраняется (кэшируется), что значительно ускоряет будущие запросы.

## Модерация с помощью искусственного интеллекта (WP 1.8.4)

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. Основной принцип
Самое важное предложение для архитектуры: **Модерирующий ИИ — это система обзора, а не автономная управляющая система.**
Он создан для того, чтобы помогать людям в умеренности, а не для того, чтобы самостоятельно определять, какие мнения могут существовать на Нексусе Гайя.
Мы различаем три уровня:
- **Обнаружение:** «Здесь может быть нарушение правил».
- **Оценка:** «Вероятность нарушения правил, например, 94%».
- **Решение:** «Какие действия фактически предприняты?»
Третий уровень в тяжелых случаях должен контролироваться человеком.

### 2. ИИ модерации как подсистема
Вместо единого ИИ создается надежная подсистема:
```текст
                 NEXUS GAJA AI МОДЕРАЦИЯ
                          │
       ┌───────────────────┼───────────────────┐
       │ │ │
  Языковой ИИ ИИ безопасности ИИ мошенничества
       │ │ │
       ├───────────────┬───┴──────────────┬───┤
       │ │ │
 Идентичность поведения при переводе
 Анализ сигналов анализа
       │ │ │
       +
                      ▼
               Оценка риска
                      │
                      ▼
               Человеческий обзор
```

### 3. Наиболее важные модули ИИ
Nexus Gaja использует девять специализированных областей анализа:
- **M1 – Понимание языка**: определяет язык, диалект, сленг, индикаторы иронии, проблемы перевода.
- **M2 – Обнаружение токсичности/злоупотреблений**: Обнаруживает оскорбления, личные нападения, преследования.
- **M3 – Обнаружение угроз**: Обнаруживает потенциальные угрозы, шантаж, объявления о насилии.
- **M4 – Обнаружение ненависти/дегуманизации**: обнаруживает целевые нападения на людей на основе их определенной принадлежности.
- **M5 – Обнаружение спама/манипуляций**: обнаруживает спам, поведение ботов, скоординированные манипуляции.
- **M6 – Обнаружение мошенничества**: обнаруживает подозрительные попытки мошенничества, фишинга, социальной инженерии.
- **M7 – целостность личности**: проверяет сигналы, касающиеся захвата учетных записей, нескольких учетных записей, уклонения от бана.
- **M8 – Безопасность СМИ**: анализирует изображения, аудио, видео и документы.
- **M9 – Механизм контекста**: самый важный модуль. Он объединяет отдельные результаты.

### 4. Почему механизм контекста имеет решающее значение
Чистого поиска по ключевым словам будет недостаточно. «Я мог бы убить его от смеха» семантически содержит насилие, но является фигурой речи. «Завтра в 8 вечера я его застрелю перед домом» — это совсем другая ситуация. ИИ должен понимать, что означает это утверждение в конкретном контексте.

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

### 6. Язык оригинала + перевод
Оригинал и перевод анализируются отдельно. Только после этого проводится «Комбинированная модерационная оценка». Это позволяет Nexus Gaja определить, мог ли сам перевод обострить или изменить факты.

### 7. Оценка уверенности
Каждая оценка ИИ получает оценку достоверности (например, вероятность угрозы: 0,96). Однако: **Оценка уверенности ≠ Истина.** Оценка 96 % означает лишь то, что модель полностью уверена в своей классификации, но не обязательно, что пользователь виновен.

### 8. Неопределенность сама становится сигналом
Если ИИ неуверен (например, Угроза: 0,62, Сатира: 0,54), он не должен просто навязывать жесткие правила. Вместо этого неопределенность встроена непосредственно в архитектуру: **Требуется человеческий контроль**.

### 9. Четыре зоны принятия решений
- 🟢 **ЗЕЛЕНЫЙ**: высокая вероятность соответствия. → никаких действий.
- 🟡 **ЖЕЛТЫЙ**: возможное нарушение. → контролировать/предупреждать при необходимости.
- 🟠 **ОРАНЖЕВЫЙ**: Вероятное нарушение. → проверка модерации.
- 🔴 **КРАСНЫЙ**: возможно серьёзное нарушение. → немедленная защитная мера + проверка человеком.

### 10. Никаких «наказаний ИИ»
**ИИ не налагает окончательных санкций.** Он может инициировать немедленные технические меры (например, временное закрытие сообщения) в случае серьезных проблем с безопасностью, но окончательное решение остается проверяемым.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. Контент, созданный искусственным интеллектом
Мы различаем: созданные человеком, созданные с помощью ИИ, созданные ИИ и управляемые ИИ. Это станет частью метаданных контента.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Обнаружение дипфейков
Целью этой архитектуры является обнаружение синтетических изображений, клонированных голосов и дипфейков. Однако обнаружение не является автоматическим доказательством.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Ирония, сатира и юмор
ИИ использует контекст, смайлы, историю разговоров и известные структуры иронии, но должен учитывать неопределенность, когда значения двусмысленны.

### 20. Отсутствие наказаний на основе одного показателя ИИ
Никакое серьезное вмешательство в модерацию не может быть основано исключительно на одном результате автоматической классификации (Текст + Контекст + Поведение + Язык + Медиа + Механизм правил = Оценка риска).

### 21. Сигналы поведения пользователей и отсутствие системы социального кредитования
Это относится к техническим сигналам злоупотреблений (например, массовой рассылке спама), а не к общей системе социального рейтинга. Nexus Gaja не поддерживает систему социального кредита – модерация служит безопасности, а не оценке достоинства человека.

### 22. Модерация ИИ должна быть проверяемой
Все соответствующие автоматизированные решения протоколируются (идентификатор события, идентификатор правила, уверенность, проверка человеком и т. д.) для обеспечения возможности отслеживания.

### 23. Ложные срабатывания, ложные негативы и показатели качества
Типы ошибок отслеживаются. Панель мониторинга измеряет точность, отзыв и особенно **коэффициент отмены апелляций** (количество успешных апелляций).

### 24. Языковое равенство и предвзятость перевода
Качество модерации должно быть сопоставимым на всех поддерживаемых языках (тест многоязычной модерации). Если результаты модерации оригинала и перевода различаются (конфликт перевода), это необходимо специально проверить.

### 25. Архитектурное предложение и механизм политики
Правила (Policy Engine) не запрограммированы жестко в моделях ИИ. ИИ предоставляет результаты; Policy Engine принимает решение на основе текущих правил. Это позволяет вносить **изменения модели без изменения правил**.

### 26. Человек остается последней инстанцией
- **NG-AI-MOD-001**: ИИ помогает в обнаружении и классификации, но не заменяет человеческий контроль при принятии серьезных решений.
- **NG-AI-MOD-002**: решения автоматической модерации должны быть отслеживаемыми, регистрируемыми и проверяемыми.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Financing Principles and Revenue Model (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

Для Nexus Gaja действует очень важный экономический принцип: **Никакой традиционной рекламы на платформе.**
Это принципиально отличает Nexus Gaja от многих современных социальных сетей. Однако это не означает, что Nexus Gaja не может носить коммерческий характер. Напротив, платформа должна быть экономически жизнеспособной, чтобы ее социальная цель могла сохраниться. Экономическая деятельность — это средство для достижения цели, а не основная цель платформы.

### 1. Принцип NG-FIN-001
Nexus Gaja финансирует свою деятельность за счет прозрачных потоков доходов, отделенных от интересов пользователей, а не за счет монетизации внимания своих пользователей или личных данных.

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

#### Компонент 2 – Премиум-предложения
Добровольные платные предложения (**Nexus Gaja Plus**), обеспечивающие больший объем хранилища, более высокое качество мультимедиа, расширенные квоты искусственного интеллекта и организационные функции.
**Важно (Freemium вместо Dark Freemium):** Базовое общение никогда не должно искусственно ухудшаться.

#### Компонент 3 – Организации
Специальные счета для школ, университетов, НПО, предприятий и муниципалитетов (**Организация Nexus Gaja**). Школы могут поддерживаться через институциональные ставки как мультипликаторы международного взаимопонимания.

#### Компонент 4 – Пожертвования
**Финансовый пул Nexus Gaja** принимает общие и целевые пожертвования (например, «на международную молодежную связь»). **Книга распределения средств** обеспечивает прозрачное распределение средств.
**Целевой фонд и Томбола:** Часть пожертвований пополняет пул для бесплатного/скидочного использования. Механизм лотереи/томболы может распределять эти средства прозрачно и поддающимся проверке.

#### Компонент 5 – Институциональное финансирование
Фонды, программы финансирования культуры или государственные программы.
**NG-FIN-002:** Финансовая поддержка не подразумевает редакционный или технический контроль (Независимость).

#### Компонент 6 – Коммерческие услуги
Услуги B2B, такие как **Перевод как услуга** (API), организационная коммуникация или международные конференц-залы, не обременяя стандартную ленту пользователей.

### 4. Отсутствие монетизации данных и экономики наблюдения
**NG-FIN-003:** Персональные данные пользователя не являются товаром. Никакой продажи списков, профилей или историй. Nexus Gaja не получает прибыли от психологического наблюдения (экономики наблюдения).

### 5. Financial Transparency & Fund Ledger
**Nexus Gaja Financial Transparency:** Publication of aggregated financial structures. Earmarked donations receive technical accounting (Fund ID → Purpose → Balance → Allocation). No cross-subsidization of social purposes into corporate marketing.

### 6. Модель финансирования на основе солидарности
Ценообразование основано на ориентации на затраты, справедливости и солидарности.
**Премиум солидарности.** Премиум-пользователи могут добровольно финансировать часть доступа другого пользователя. Принудительная солидарность или общество премиум-класса (меньше уважения/модерации к бесплатным пользователям) строго запрещены.

### 7. Economic KPIs Instead of Engagement Economy
No dependence on keeping users "online as long as possible" (no ragebait, infinite feeds).
Instead, we use metrics like:
- **Global Communication Index (GCI):** Successful communication relationships between people from different linguistic/cultural regions.
- **Platform Sustainability Ratio (PSR):** Recurring revenue / recurring operating costs (Target ≥ 1).

### 8. Чего мы явно не хотим (негативный список)
Nexus Gaja **не** финансируется:
❌ Продажа персональных данных
❌ Персонализированная традиционная реклама
❌ Мониторинг поведения пользователей в рекламных целях
❌ Продажа данных частного общения
❌ Скрытое использование данных ИИ
❌ Манипулятивные платные доступы премиум-класса
❌ Искусственное ограничение охвата для монетизации.
❌ Платное политическое влияние
❌Покупка привилегированных решений модерации.

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

## API, интерфейсы и коммуникационная архитектура (WP 1.11.3)

Чтобы обеспечить стабильность, безопасность и масштабируемость системы, Nexus Gaja придерживается строго API-ориентированной и управляемой событиями архитектуры.

### Основные принципы
- **Нет прямого доступа к базе данных.** Компоненты взаимодействуют исключительно через определенные интерфейсы (API или события), а не через прямые запросы к базе данных других служб.
- **Шлюз API:** все запросы внешних клиентов направляются через шлюз API, который обрабатывает аутентификацию, маршрутизацию и ограничение скорости.
– **Абстракция поставщика.** Внешние сервисы (модели искусственного интеллекта, поставщики платежей, системы перевода) интегрируются через уровни абстракции, что позволяет избежать жестко запрограммированных зависимостей и обеспечить гибкую смену поставщиков.

### Шаблоны общения
– **Синхронные API (REST/HTTPS):** используются для немедленных запросов, таких как вход в систему, настройки профиля или прямой перевод.
- **Асинхронные события (шина событий):** центральная нервная система Nexus Gaja для отложенной, разделенной обработки (например, «Message.Created» асинхронно запускает модерацию, перевод и уведомление).
- **В реальном времени (WebSocket):** выделенные каналы для живого чата и индикаторов набора текста.

### Безопасность и надежность
- **Модель нулевого доверия:** Внутренний сетевой трафик не считается автоматически доверенным; конфиденциальная связь между службами требует аутентификации.
- **Идемпотентность и шаблон исходящих сообщений.** Критические операции (например, пожертвования или обмен сообщениями) разработаны так, чтобы быть идемпотентными, чтобы предотвратить дублирующую обработку, используя шаблон исходящих сообщений, чтобы гарантировать, что события никогда не будут потеряны даже во время транзакций базы данных.

## Модель домена MVP (WP 1.12)

![Модульный монолит Nexus Gaja](assets/img/nexus_architecture.jpg)

Nexus Gaja employs a strictly Domain-Driven MVP Architecture (ADR-025), designed as a modular monolith with clear domain boundaries. This structure prevents premature microservice complexity while retaining the flexibility to split out specific domains later.

### Сущности основного домена
В архитектуре четко разделены отдельные концепции, чтобы обеспечить целостность данных и избежать структурных ошибок, таких как «Имя пользователя = Человек»:
- **Идентификация и учетные записи:** «Лицо» ≠ «Учетная запись пользователя» ≠ «Проверка личности». Подтвержденное лицо участвует через учетную запись, но сущности остаются отдельными.
- **Общение:** `Сообщение` ≠ `Перевод`. Исходное сообщение остается неизменным; переводы являются связанными сущностями.
- **Модерация:** `Сообщить` ≠ `Решение о модерации`. Отчет — это просто заявление; модерация дела проводит расследование.
- **Финансы:** «Пожертвование» ≠ «Баланс средств». Платежи регистрируются в фонде через неизменяемую книгу, что обеспечивает финансовую прозрачность.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Статус проекта
В настоящее время проект находится на активной стадии архитектуры и планирования.
Текущие архитектурные решения документируются в папке `/docs`.