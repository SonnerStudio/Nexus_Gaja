# Nexus Gaja

![Biểu tượng Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** là mạng truyền thông thông minh, nhạy cảm với ngữ cảnh được thiết kế để cách mạng hóa truyền thông toàn cầu.

## Mục đích và Tầm nhìn
Trong một thế giới toàn cầu hóa, ngôn ngữ thường là rào cản lớn nhất. Mục tiêu chính của Nexus Gaja là cho phép giao tiếp liền mạch, không rào cản và chính xác theo ngữ cảnh giữa mọi người—bất kể họ có nói một ngôn ngữ chung hay không.

Nó không chỉ là dịch từ một cách cứng nhắc mà còn là **chuyển nghĩa**. Nexus Gaja kết nối mọi người ở mức độ sâu hơn bằng cách hiểu rõ các sắc thái văn hóa, khu vực và ngữ cảnh, từ đó tạo điều kiện cho các cuộc trò chuyện chân thực, xác thực.

## Khả năng và tính năng
- **Giao tiếp đa phương tiện**: Hệ thống không chỉ xử lý văn bản mà còn cả hình ảnh, âm thanh và video. Điều này cho phép các cuộc trò chuyện hoàn toàn hấp dẫn (ví dụ: cuộc gọi điện video hoặc tin nhắn thoại) trong thời gian thực, vượt qua các rào cản ngôn ngữ.
- **Độ nhạy ngữ cảnh**: Nhận biết sự mỉa mai, thành ngữ, biệt ngữ và phương ngữ vùng miền thường bị các dịch giả thông thường hiểu nhầm.
- **Mạng đa nền tảng**: Đóng vai trò là nền tảng cho các cuộc trò chuyện riêng tư, chủ đề diễn đàn (bài đăng có nhận xét) và tương tác cộng đồng toàn cầu.

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

## Kiểm duyệt được hỗ trợ bởi AI (WP 1.8.4)

Với Kiểm duyệt được hỗ trợ bởi AI, chúng tôi đang thực hiện một bước quan trọng từ ý tưởng sản phẩm đến kiến ​​trúc kỹ thuật, có tính đến các quy định hiện hành của EU (các yêu cầu về tính minh bạch của Đạo luật AI của EU theo Điều 50; Đạo luật dịch vụ kỹ thuật số với các giải thích dễ hiểu và các tùy chọn khiếu nại).

### 1. Nguyên tắc cơ bản
Câu quan trọng nhất đối với kiến trúc là: **AI kiểm duyệt là một hệ thống đánh giá, không phải hệ thống cai trị tự trị.**
Nó được thiết kế để hỗ trợ con người một cách có chừng mực chứ không phải để tự xác định những ý kiến nào được phép tồn tại trên Nexus Gaja.
Chúng ta phân biệt ba cấp độ:
- **Phát hiện:** "Có thể có vi phạm quy tắc ở đây."
- **Đánh giá:** "Ví dụ: Xác suất vi phạm quy tắc là 94%."
- **Quyết định:** "Hành động thực sự được thực hiện là gì?"
Cấp độ thứ ba phải được kiểm soát bởi con người trong những trường hợp nghiêm trọng.

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

### 8. Sự không chắc chắn tự nó trở thành một tín hiệu
Nếu AI không chắc chắn (ví dụ: Đe dọa: 0,62, Châm biếm: 0,54), thì nó không chỉ đơn giản là thực thi các quy tắc khắc nghiệt. Thay vào đó, sự không chắc chắn được tích hợp trực tiếp vào kiến ​​trúc: **Yêu cầu đánh giá của con người**.

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

### 13. AI không được bí mật thay đổi nội dung
**AI kiểm duyệt không bao giờ được thay đổi nội dung gốc mà không được chú ý.** Trong quá trình tự động sửa, dịch hoặc tóm tắt, bản gốc luôn được giữ nguyên.

### 14. Nội dung do AI tạo ra
Chúng tôi phân biệt giữa: Do con người tạo ra, do AI hỗ trợ, do AI tạo ra và do AI điều khiển. Điều này sẽ trở thành một phần của siêu dữ liệu nội dung.

### 15. Dán nhãn Nội dung AI & Lớp xuất xứ AI
Theo các quy tắc minh bạch của Đạo luật AI của Liên minh Châu Âu (có hiệu lực từ tháng 8 năm 2026), nội dung do AI tạo ra phải có thể nhận dạng được. Chúng tôi cung cấp Lớp chứng minh AI để lưu trữ siêu dữ liệu (AI-Origin, Model, Timestamp, Human Review).

### 16. Phát hiện Deepfake
Kiến trúc này nhằm mục đích phát hiện các hình ảnh tổng hợp, giọng nói nhân bản và các tác phẩm giả mạo. Tuy nhiên, việc phát hiện không phải là bằng chứng tự động.

### 17. Không có "Máy xác thực" tự động (Kiểm duyệt ≠ Kiểm tra sự thật)
Một hệ thống kiểm tra: "Nội dung có vi phạm quy tắc không?" (Kiểm duyệt nội dung), một người khác cung cấp: "Có những thông tin và nguồn nào?" (Hỗ trợ thông tin). Các ý kiến ​​không chỉ bị xóa vì "sai".

### 18. Bảo vệ chống lại sự hiểu sai về văn hóa
AI yêu cầu **Mô hình bối cảnh văn hóa** để ngăn chặn việc coi các chuẩn mực giao tiếp của một quốc gia là tiêu chuẩn toàn cầu.

### 19. Trớ trêu, châm biếm và hài hước
AI sử dụng ngữ cảnh, biểu tượng cảm xúc, lịch sử hội thoại và các cấu trúc mỉa mai đã biết nhưng phải cho phép có sự không chắc chắn khi ý nghĩa không rõ ràng.

### 20. Không trừng phạt dựa trên một điểm AI duy nhất
Không có sự can thiệp kiểm duyệt nghiêm trọng nào có thể chỉ dựa trên một kết quả phân loại tự động duy nhất (Văn bản + Ngữ cảnh + Hành vi + Ngôn ngữ + Phương tiện + Công cụ quy tắc = Đánh giá rủi ro).

### 21. Tín hiệu hành vi người dùng & Không có hệ thống tín dụng xã hội
Điều này liên quan đến các tín hiệu lạm dụng kỹ thuật (ví dụ: đăng spam hàng loạt), không phải hệ thống xếp hạng xã hội chung. Nexus Gaja không duy trì Hệ thống tín dụng xã hội – việc kiểm duyệt nhằm mục đích bảo mật chứ không phải để đánh giá giá trị của một người.

### 22. AI kiểm duyệt phải được kiểm duyệt
Tất cả các quyết định tự động có liên quan đều được ghi lại (ID sự kiện, ID quy tắc, Độ tin cậy, Đánh giá con người, v.v.) để đảm bảo khả năng truy nguyên.

### 23. False Positives, False Negatives & Quality Metrics
Error types are monitored. A dashboard measures Precision, Recall, and especially the **Appeal Reversal Rate** (number of successful appeals).

### 24. Công bằng ngôn ngữ & Xu hướng dịch thuật
Chất lượng kiểm duyệt phải tương đương nhau trên tất cả các ngôn ngữ được hỗ trợ (Điểm chuẩn kiểm duyệt đa ngôn ngữ). Nếu kết quả kiểm duyệt khác nhau giữa bản gốc và bản dịch (Xung đột bản dịch) thì điều này phải được xem xét cụ thể.

### 25. Đề xuất kiến trúc & Công cụ chính sách
Các quy tắc (Công cụ chính sách) không được mã hóa cứng vào các mô hình AI. AI cung cấp những phát hiện; Công cụ chính sách quyết định dựa trên các quy tắc hiện hành. Điều này cho phép **thay đổi mô hình mà không thay đổi quy tắc**.

### 26. Con Người Vẫn Là Quyền Quyết Định Cuối Cùng
- **NG-AI-MOD-001**: AI hỗ trợ phát hiện và phân loại nhưng không thay thế sự xem xét của con người trong các quyết định quan trọng.
- **NG-AI-MOD-002**: Các quyết định kiểm duyệt tự động phải có thể theo dõi, ghi lại và kiểm chứng được.

**Tóm tắt**: Chúng tôi đang xây dựng một hệ thống gồm bốn giai đoạn: Phát hiện AI, Phân tích bối cảnh và rủi ro, Công cụ chính sách và Quản trị con người. Điều này cho phép tự động hóa mạnh mẽ mà không tạo ra kiến ​​trúc "AI làm Thẩm phán" nguy hiểm.

## Tình trạng dự án
Dự án hiện đang trong giai đoạn kiến trúc và quy hoạch tích cực.
Các quyết định về kiến ​​trúc đang diễn ra được ghi lại trong thư mục `/docs`.