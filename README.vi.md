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

In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Technical Architecture (Core Concept)

![Nexus Gaja Translation Concept](assets/img/nexus_translation.jpg)

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

![Nexus Gaja AI Moderation](assets/img/nexus_moderation.jpg)

With AI-Assisted Moderation, we are taking a significant step from product idea to technical architecture, taking into account current EU regulations (transparency requirements of the EU AI Act under Art. 50; Digital Services Act with comprehensible justifications and appeal options).

### 1. Basic Principle
The most important sentence for the architecture is: **The moderation AI is a review system, not an autonomous ruling system.**
It is designed to assist humans in moderation, not to determine itself which opinions are allowed to exist on Nexus Gaja.
We differentiate between three levels:
- **Detection:** "There could be a rule violation here."
- **Evaluation:** "The probability of a rule violation is, for example, 94%."
- **Decision:** "What action is actually taken?"
The third level must be controlled by a human in severe cases.

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

### 5. Multilingual Moderation
Moderation cannot simply compare words. It must analyze the semantic level (e.g., German idioms vs. Japanese idioms vs. regional expressions).

### 6. Original Language + Translation
Original and translation are analyzed separately. Only then does the "Combined Moderation Assessment" take place. This allows Nexus Gaja to determine whether the translation itself may have escalated or altered the facts.

### 7. Confidence Score
Every AI evaluation receives a confidence score (e.g., Threat probability: 0.96). However: **Confidence Score ≠ Truth.** A score of 96% only means the model is highly certain of its classification, not necessarily that the user is guilty.

### 8. Uncertainty Becomes a Signal Itself
If the AI is uncertain (e.g., Threat: 0.62, Satire: 0.54), it must not simply enforce harsh rules. Instead, uncertainty is built directly into the architecture: **Human Review Required**.

### 9. Four Decision Zones
- 🟢 **GREEN**: Highly likely compliant. → no action.
- 🟡 **YELLOW**: Possible violation. → monitor / provide a warning if necessary.
- 🟠 **ORANGE**: Probable violation. → moderation review.
- 🔴 **RED**: Severe possible violation. → immediate protective measure + human review.

### 10. No "AI Punishment"
**The AI imposes no final sanctions.** It can trigger technical immediate measures (e.g., temporarily holding back a message) for severe security concerns, but the final decision remains verifiable.

### 11. Protective Measures Can Occur Automatically
In the event of a concrete threat (Threat detected → High confidence → Temporary restriction → Human review → Decision), we protect the threatened user without turning the AI into a judge.

### 12. The AI Must Be Able to Justify Its Decisions
The DSA requires clear and specific reasons. The AI provides structured reasoning: Rule (NG-CONDUCT-004), Detected (Potential concrete threat), Confidence (0.94), Relevant context (Previous 4 messages), Recommended action (Human review).

### 13. AI Must Not Secretly Alter Content
**Moderation AI must never alter the original content unnoticed.** During automatic correction, translation, or summarization, the original is always preserved.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. No Automatic "Truth Machine" (Moderation ≠ Fact Checking)
One system checks: "Does the content violate rules?" (Content Moderation), another provides: "What information and sources are available?" (Information Assistance). Opinions are not simply deleted for being "wrong."

### 18. Protection Against Cultural Misinterpretation
The AI requires **Cultural Context Models** to prevent the communication norms of one country from being assumed as a global standard.

### 19. Irony, Satire, and Humor
The AI uses context, emojis, conversation history, and known irony structures, but must allow for uncertainty when meanings are ambiguous.

### 20. No Punishment Based on a Single AI Score
No severe moderation intervention may be based solely on a single automated classification result (Text + Context + Behaviour + Language + Media + Rule Engine = Risk Assessment).

### 21. User Behaviour Signals & No Social Credit System
This relates to technical abuse signals (e.g., mass spam posting), not a general social rating system. Nexus Gaja does not maintain a Social Credit System – moderation serves security, not the assessment of a person's worth.

### 22. Moderation AI Must Be Auditable
All relevant automated decisions are logged (Event-ID, Rule-ID, Confidence, Human-Review, etc.) to ensure traceability.

### 23. Kết quả dương tính giả, âm tính giả & thước đo chất lượng
Các loại lỗi được theo dõi. Trang tổng quan đo lường Độ chính xác, Thu hồi và đặc biệt là **Tỷ lệ đảo ngược khiếu nại** (số lượng khiếu nại thành công).

### 24. Language Equity & Translation Bias
Moderation quality must be comparable across all supported languages (Multilingual Moderation Benchmark). If moderation results differ between the original and the translation (Translation Conflict), this must be specifically reviewed.

### 25. Architecture Proposal & Policy Engine
Rules (Policy Engine) are not hardcoded into the AI models. The AI provides findings; the Policy Engine decides based on current rules. This allows for **model changes without rule changes**.

### 26. The Human Remains the Final Authority
- **NG-AI-MOD-001**: The AI assists in detection and classification, but does not replace human review in severe decisions.
- **NG-AI-MOD-002**: Automated moderation decisions must be traceable, loggable, and verifiable.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Nguyên tắc tài chính và mô hình doanh thu (WP 1.10.1)

![Nexus Gaja Finance Model](assets/img/nexus_finance.jpg)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Nguyên lý NG-FIN-001
Nexus Gaja tài trợ cho hoạt động của mình thông qua các luồng doanh thu minh bạch tách biệt với lợi ích của người dùng chứ không phải thông qua việc kiếm tiền từ sự chú ý hoặc dữ liệu cá nhân của người dùng.

### 2. Không có quảng cáo truyền thống
Cụ thể bị cấm là:
- Quảng cáo biểu ngữ
- Quảng cáo bật lên
- Quảng cáo video tự động phát
- Các bài đăng được tài trợ trong nguồn cấp dữ liệu tiêu chuẩn
- Hồ sơ quảng cáo được cá nhân hóa
- Bán hồ sơ người dùng hoặc dữ liệu cá nhân
- Quảng cáo bắt nguồn từ các cuộc trò chuyện riêng tư.

Nexus Gaja vẫn là một **không gian giao tiếp chứ không phải là không gian quảng cáo**.

### 3. Tài trợ không cần quảng cáo (6 trụ cột)
Nguồn tài chính được xây dựng trên sáu trụ cột:
```văn bản
                 NEXUS GAJA
                     │
       ┌─────────────┼─────────────┐
       ▼ ▼ ▼
   ĐÓNG GÓP TỔ CHỨC CAO CẤP
       │ │ │
       ├─────────────┼─────────────┤
       ▼ ▼ ▼
    DỊCH VỤ HỢP TÁC TÀI TRỢ
```

#### Pillar 1 – Free Basic Membership
**Nexus Gaja Free** enables basic international understanding for everyone (profile, international communication, posts, communities, chats, basic translation) at no cost.

#### Trụ cột 2 – Ưu đãi cao cấp
Các dịch vụ trả phí tự nguyện (**Nexus Gaja Plus**) cung cấp giới hạn lưu trữ lớn hơn, chất lượng phương tiện cao hơn, hạn ngạch AI mở rộng và các tính năng tổ chức.
**Quan trọng (Freemium thay vì Dark Freemium):** Giao tiếp cơ bản không bao giờ được làm suy giảm một cách giả tạo.

#### Trụ cột 3 – Tổ chức
Tài khoản đặc biệt dành cho các trường học, trường đại học, tổ chức phi chính phủ, doanh nghiệp và thành phố (**Tổ chức Nexus Gaja**). Các trường học có thể được hỗ trợ thông qua tỷ lệ thể chế như là hệ số nhân của sự hiểu biết quốc tế.

#### Trụ cột 4 – Đóng góp
**Quỹ tài trợ của Nexus Gaja** chấp nhận các khoản quyên góp chung và được dành riêng (ví dụ: "cho hoạt động giao tiếp của giới trẻ quốc tế"). **Sổ cái phân bổ quỹ** đảm bảo việc phân bổ vốn minh bạch.
**Quỹ mục đích & Tombola:** Một phần tiền quyên góp sẽ cung cấp cho một nhóm để sử dụng miễn phí/giảm giá. Cơ chế xổ số/tombola có thể phân bổ các khoản tiền này một cách minh bạch và có thể kiểm toán được.

#### Trụ cột 5 – Tài trợ thể chế
Các tổ chức, chương trình tài trợ văn hóa hoặc chương trình của tiểu bang.
**NG-FIN-002:** Hỗ trợ tài chính không mua quyền kiểm soát biên tập hoặc kỹ thuật (Độc lập).

#### Trụ cột 6 – Dịch vụ thương mại
Các dịch vụ B2B như **Dịch dưới dạng dịch vụ** (API), giao tiếp tổ chức hoặc phòng hội thảo quốc tế mà không tạo gánh nặng cho nguồn cấp dữ liệu người dùng tiêu chuẩn.

### 4. Nền kinh tế không giám sát và kiếm tiền từ dữ liệu
**NG-FIN-003:** Dữ liệu cá nhân của người dùng không phải là hàng hóa. Không bán danh sách, hồ sơ hoặc lịch sử. Nexus Gaja không thu lợi từ việc giám sát tâm lý (Kinh tế giám sát).

### 5. Minh bạch tài chính & Sổ cái quỹ
**Minh bạch tài chính của Nexus Gaja:** Công bố cấu trúc tài chính tổng hợp. Các khoản quyên góp dành riêng sẽ được tính toán kỹ thuật (ID quỹ → Mục đích → Số dư → Phân bổ). Không trợ cấp chéo cho các mục đích xã hội vào hoạt động tiếp thị của công ty.

### 6. Mô hình tài trợ dựa trên tinh thần đoàn kết
Việc định giá dựa trên định hướng chi phí, công bằng và đoàn kết.
**Solidarity Premium:** Một tùy chọn tự nguyện dành cho người dùng Premium để tài trợ một phần quyền truy cập của người dùng khác. Sự đoàn kết cưỡng bức hoặc một xã hội có đẳng cấp cao (ít tôn trọng/điều độ hơn đối với người dùng miễn phí) đều bị nghiêm cấm.

### 7. KPI kinh tế thay vì nền kinh tế gắn kết
Không phụ thuộc vào việc giữ người dùng "trực tuyến càng lâu càng tốt" (không có trò đùa, nguồn cấp dữ liệu vô hạn).
Thay vào đó, chúng tôi sử dụng các số liệu như:
- **Chỉ số Giao tiếp Toàn cầu (GCI):** Mối quan hệ giao tiếp thành công giữa những người đến từ các vùng ngôn ngữ/văn hóa khác nhau.
- **Tỷ lệ bền vững nền tảng (PSR):** Doanh thu định kỳ / chi phí vận hành định kỳ (Mục tiêu ≥ 1).

### 8. Điều chúng ta rõ ràng không muốn (Danh sách tiêu cực)
Nexus Gaja **không** được tài trợ bởi:
❌ Bán dữ liệu cá nhân
❌ Quảng cáo truyền thống được cá nhân hóa
❌ Giám sát hành vi người dùng nhằm mục đích quảng cáo
❌ Bán dữ liệu liên lạc riêng tư
❌ Sử dụng dữ liệu AI ẩn
❌ Tường phí trả phí có tính thao túng
❌ Hạn chế phạm vi tiếp cận nhân tạo để kiếm tiền
❌ Ảnh hưởng chính trị được trả tiền
❌ Mua các quyết định kiểm duyệt đặc quyền.

### 9. Kiến trúc tài chính sơ bộ
```văn bản
                         NEXUS GAJA
                              │
             ┌────────────────┼────────────────┐
             │ │ │
             ▼ ▼ ▼
          NGƯỜI SỬ DỤNG TỔ CHỨC DOANH NGHIỆP
             │ │ │
             └────────────────┼────────────────┘
                              │
                       DỊCH VỤ NỀN TẢNG
                              │
          ┌─────────────────── ┼───────────────────┐
          ▼ ▼ ▼
       API QUYÊN GÓP CAO CẤP
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               QUỸ TỔNG HỢP QUỸ HẠN CHẾ
                                        │
                                        ▼
                                  MỤC ĐÍCH XÃ HỘI
```

### Tóm tắt Nguyên tắc Tài chính (NG-FIN)
- **NG-FIN-001:** Không tài trợ thông qua quảng cáo truyền thống.
- **NG-FIN-002:** Không kiểm soát biên tập/kỹ thuật thông qua hỗ trợ tài chính.
- **NG-FIN-003:** Dữ liệu cá nhân không phải là hàng hóa.
- **NG-FIN-004:** Vẫn có thể truy cập liên lạc cơ bản mà không cần thanh toán.
- **NG-FIN-005:** Các dịch vụ cao cấp không được làm suy giảm người dùng miễn phí.
- **NG-FIN-006:** Quỹ dành riêng được quản lý theo mục đích của chúng.
- **NG-FIN-007:** Quản lý minh bạch các khoản quyên góp và tài trợ.
- **NG-FIN-008:** Các dịch vụ B2B thương mại không ảnh hưởng đến tính độc lập.
- **NG-FIN-009:** Tập trung vào tính bền vững hơn là kiếm tiền tối đa.
- **NG-FIN-010:** Cấu trúc đảm bảo vĩnh viễn mục đích xã hội.

## API, Giao diện và Kiến trúc Truyền thông (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### Nguyên tắc cốt lõi
- **Không có quyền truy cập cơ sở dữ liệu trực tiếp:** Các thành phần giao tiếp độc quyền thông qua các giao diện được xác định (API hoặc Sự kiện), không bao giờ thông qua các truy vấn cơ sở dữ liệu trực tiếp của các dịch vụ khác.
- **Cổng API:** Tất cả các yêu cầu của máy khách bên ngoài đều định tuyến thông qua việc xác thực, định tuyến và giới hạn tốc độ xử lý Cổng API.
- **Tóm tắt nhà cung cấp:** Các dịch vụ bên ngoài (mô hình AI, nhà cung cấp thanh toán, công cụ dịch thuật) được tích hợp thông qua các lớp trừu tượng, tránh sự phụ thuộc được mã hóa cứng và cho phép chuyển đổi nhà cung cấp linh hoạt.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Bảo mật và độ tin cậy
- **Mô hình Zero-Trust:** Lưu lượng truy cập mạng nội bộ không được tự động tin cậy; giao tiếp dịch vụ với dịch vụ nhạy cảm yêu cầu xác thực.
- **Mẫu bình thường & hộp thư đi:** Các hoạt động quan trọng (như quyên góp hoặc nhắn tin) được thiết kế bình thường để ngăn chặn việc xử lý trùng lặp, sử dụng mẫu Hộp thư đi để đảm bảo các sự kiện không bao giờ bị mất ngay cả trong các giao dịch cơ sở dữ liệu.

## Mô hình miền MVP (WP 1.12)

![Nexus Gaja Modular Monolith](assets/img/nexus_architecture.jpg)

Nexus Gaja sử dụng Kiến trúc MVP hướng miền (ADR-025) nghiêm ngặt, được thiết kế dưới dạng khối nguyên khối mô-đun với ranh giới miền rõ ràng. Cấu trúc này ngăn chặn sự phức tạp ban đầu của vi dịch vụ trong khi vẫn duy trì tính linh hoạt để phân chia các miền cụ thể sau này.

### Core Domain Entities
The architecture explicitly separates distinct concepts to ensure data integrity and avoid structural pitfalls like "Username = Human":
- **Identity & Accounts:** `Person` ≠ `User Account` ≠ `Identity Verification`. A verified person participates via an account, but the entities remain separate.
- **Communication:** `Message` ≠ `Translation`. The original message remains immutable; translations are linked entities.
- **Moderation:** `Report` ≠ `Moderation Decision`. A report is merely a claim; a moderation case conducts the investigation.
- **Finances:** `Donation` ≠ `Fund Balance`. Payments are booked via an immutable ledger to a fund, ensuring financial transparency.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Tình trạng dự án
Dự án hiện đang trong giai đoạn kiến trúc và quy hoạch tích cực.
Các quyết định về kiến ​​trúc đang diễn ra được ghi lại trong thư mục `/docs`.

---

---

## Giấy phép & Sở hữu trí tuệ

> **© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio — Bảo lưu mọi quyền.**

**Nexus Gaja** là tài sản trí tuệ độc quyền của **Jan Friske**, hoạt động dưới **SonnerStudio**.

Jan Friske là người sáng tạo, kiến ​​trúc sư và chủ sở hữu duy nhất của Nexus Gaja — bao gồm tất cả các khái niệm, kiến ​​trúc, mô hình miền, nhận diện thương hiệu và tài liệu liên quan.

**Không có quyền, giấy phép hoặc lợi ích sở hữu nào thuộc về bất kỳ bên thứ ba nào**, bất kể quy mô, vị trí thị trường hoặc tầm ảnh hưởng của họ trong ngành công nghệ.

### Những điều KHÔNG được phép nếu không có sự đồng ý rõ ràng bằng văn bản:
- Sao chép, sao chép hoặc phân phối phần mềm này hoặc tài liệu của nó
- Sửa đổi, phỏng theo hoặc tạo tác phẩm phái sinh
- Sử dụng thương mại bất kỳ phần nào của Nexus Gaja
- Sử dụng nội dung của kho này làm dữ liệu đào tạo cho hệ thống AI hoặc LLM
- Cấp phép lại hoặc chuyển giao bất kỳ quyền nào cho bên thứ ba

### Sở hữu trí tuệ được bảo vệ
Các khái niệm ban đầu sau đây được bảo vệ dưới dạng bí mật thương mại và sáng tạo độc quyền của Jan Friske:
- Mô hình truyền thông phân lớp (Bản gốc, Phiên dịch ngữ nghĩa, Đầu ra được dịch)
- Nguyên tắc tách biệt danh tính (Người không phải là Tài khoản không phải là Xác minh danh tính)
- Mô hình tách tin nhắn-dịch (Tin nhắn không phải là dịch thuật)
- Khung quản trị kiểm duyệt AI

### Liên hệ
Để được giải đáp thắc mắc về giấy phép: https://github.com/SonnerStudio

Nexus Gaja và logo Nexus Gaja là thương hiệu của Jan Friske. Việc sử dụng trái phép tên hoặc nhãn hiệu đều bị cấm.

Xem các điều khoản cấp phép đầy đủ trong tệp LICENSE.
