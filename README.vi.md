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

## Kiến trúc kỹ thuật (Khái niệm cốt lõi)

Cốt lõi kỹ thuật của Nexus Gaja là mô hình giao tiếp được xây dựng tùy chỉnh được chia thành ba lớp:

1. **Bản gốc**: Đối tượng giao tiếp (tin nhắn) do người gửi tạo ra luôn không thay đổi.
2. **Giải thích ngữ nghĩa**: Hệ thống không chỉ phân tích từ ngữ mà còn phân tích ý nghĩa thực tế.
3. **Trình bày ngôn ngữ đích**: AI chỉ tạo bản trình bày tạm thời hoặc được lưu trong bộ nhớ đệm của bản gốc cho người nhận tương ứng dựa trên ngôn ngữ ưa thích của họ. Bản dịch không bao giờ ghi đè lên tin nhắn gốc.

### Phụ thuộc vào bối cảnh
Các bản dịch trong Nexus Gaja không bao giờ xem tin nhắn một cách riêng biệt. Công cụ xem xét toàn bộ hệ thống phân cấp:
`Tin nhắn` → `Tin nhắn trước` → `Bối cảnh chủ đề` → `Bối cảnh cộng đồng` → `Ngôn ngữ / Khu vực` → `Tùy chọn người dùng`

### Hiệu quả thông qua dịch thuật theo yêu cầu
Quá trình dịch chỉ diễn ra một cách hiệu quả về tài nguyên **theo yêu cầu** (Theo yêu cầu). Khi người dùng yêu cầu nội dung, nội dung đó sẽ được dịch sang ngôn ngữ cài sẵn của họ. Sau khi tạo bản dịch cho một ngôn ngữ cụ thể, bản dịch đó sẽ được lưu trữ vĩnh viễn (bộ nhớ đệm) để tăng tốc đáng kể các yêu cầu trong tương lai.

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

### 2. AI điều tiết như một hệ thống con
Thay vì một AI duy nhất, một hệ thống con mạnh mẽ được thiết lập:
```văn bản
                 ĐIỀU CHỈNH AI của NEXUS GAJA
                          │
       ┌──────────────────┼──────────────────┐
       │ │ │
  Ngôn ngữ AI An toàn AI Lừa đảo AI
       │ │ │
       ├──────────────┬───┴──────────────┬───┤
       │ │ │
 Bản sắc hành vi dịch thuật
 Phân tích Phân tích Tín hiệu
       │ │ │
       └──────────────┼──────────────────┘
                      ▼
               Đánh giá rủi ro
                      │
                      ▼
               Đánh giá con người
```

### 3. Các mô-đun AI quan trọng nhất
Nexus Gaja sử dụng chín lĩnh vực phân tích chuyên biệt:
- **M1 – Hiểu ngôn ngữ**: Phát hiện ngôn ngữ, phương ngữ, tiếng lóng, dấu hiệu mỉa mai, vấn đề dịch thuật.
- **M2 – Phát hiện độc tính/ Lạm dụng**: Phát hiện những lời lăng mạ, công kích cá nhân, quấy rối.
- **M3 – Phát hiện mối đe dọa**: Phát hiện các mối đe dọa tiềm ẩn, tống tiền, thông báo bạo lực.
- **M4 – Phát hiện sự căm ghét / mất nhân tính**: Phát hiện các cuộc tấn công có chủ đích nhằm vào mọi người dựa trên các liên kết cụ thể.
- **M5 – Phát hiện thư rác/ thao túng**: Phát hiện thư rác, hành vi bot, phối hợp thao túng.
- **M6 – Phát hiện gian lận**: Phát hiện các nỗ lực lừa đảo đáng ngờ, lừa đảo, kỹ thuật xã hội.
- **M7 – Tính toàn vẹn danh tính**: Kiểm tra các tín hiệu liên quan đến việc chiếm đoạt tài khoản, nhiều tài khoản, trốn lệnh cấm.
- **M8 – An toàn phương tiện**: Phân tích hình ảnh, âm thanh, video, tài liệu.
- **M9 – Context Engine**: Mô-đun quan trọng nhất. Nó hợp nhất những phát hiện riêng lẻ.

### 4. Tại sao Context Engine lại quan trọng
Một tìm kiếm từ khóa thuần túy sẽ không đủ. "Tôi có thể giết anh ta vì cười" về mặt ngữ nghĩa chứa đựng bạo lực nhưng là một cách nói tu từ. “8 giờ tối mai tôi sẽ bắn hắn trước cửa nhà” lại là một tình huống hoàn toàn khác. AI phải hiểu ý nghĩa của tuyên bố đó trong bối cảnh cụ thể của nó.

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

### 10. Không có "Hình phạt AI"
**AI không áp đặt biện pháp trừng phạt cuối cùng.** Nó có thể kích hoạt các biện pháp kỹ thuật tức thời (ví dụ: tạm thời giữ lại tin nhắn) đối với những lo ngại nghiêm trọng về bảo mật, nhưng quyết định cuối cùng vẫn có thể kiểm chứng được.

### 11. Các biện pháp bảo vệ có thể tự động diễn ra
Trong trường hợp có mối đe dọa cụ thể (Đã phát hiện mối đe dọa → Độ tin cậy cao → Hạn chế tạm thời → Đánh giá của con người → Quyết định), chúng tôi bảo vệ người dùng bị đe dọa mà không biến AI thành người phán xét.

### 12. AI phải có khả năng biện minh cho các quyết định của mình
DSA yêu cầu lý do rõ ràng và cụ thể. AI cung cấp lý luận có cấu trúc: Quy tắc (NG-CONDUCT-004), Đã phát hiện (Mối đe dọa cụ thể tiềm ẩn), Độ tin cậy (0,94), Ngữ cảnh liên quan (4 thông báo trước đó), Hành động được đề xuất (Đánh giá của con người).

### 13. AI không được bí mật thay đổi nội dung
**AI kiểm duyệt không bao giờ được thay đổi nội dung gốc mà không được chú ý.** Trong quá trình tự động sửa, dịch hoặc tóm tắt, bản gốc luôn được giữ nguyên.

### 14. Nội dung do AI tạo ra
Chúng tôi phân biệt giữa: Do con người tạo ra, do AI hỗ trợ, do AI tạo ra và do AI điều khiển. Điều này sẽ trở thành một phần của siêu dữ liệu nội dung.

### 15. Dán nhãn Nội dung AI & Lớp xuất xứ AI
Theo các quy tắc minh bạch của Đạo luật AI của Liên minh Châu Âu (có hiệu lực từ tháng 8 năm 2026), nội dung do AI tạo ra phải có thể nhận dạng được. Chúng tôi cung cấp Lớp chứng minh AI để lưu trữ siêu dữ liệu (AI-Origin, Model, Timestamp, Human Review).

### 16. Phát hiện Deepfake
Kiến trúc này nhằm mục đích phát hiện các hình ảnh tổng hợp, giọng nói nhân bản và các tác phẩm sâu. Tuy nhiên, việc phát hiện không phải là bằng chứng tự động.

### 17. Không có "Máy xác thực" tự động (Kiểm duyệt ≠ Kiểm tra sự thật)
Một hệ thống kiểm tra: "Nội dung có vi phạm quy tắc không?" (Kiểm duyệt nội dung), một người khác cung cấp: "Có những thông tin và nguồn nào?" (Hỗ trợ thông tin). Các ý kiến ​​không chỉ bị xóa vì "sai".

### 18. Bảo vệ chống lại sự hiểu sai về văn hóa
AI yêu cầu **Mô hình bối cảnh văn hóa** để ngăn chặn việc coi các chuẩn mực giao tiếp của một quốc gia là tiêu chuẩn toàn cầu.

### 19. Trớ trêu, châm biếm và hài hước
AI sử dụng ngữ cảnh, biểu tượng cảm xúc, lịch sử hội thoại và các cấu trúc mỉa mai đã biết nhưng phải cho phép có sự không chắc chắn khi ý nghĩa không rõ ràng.

### 20. Không trừng phạt dựa trên một điểm AI duy nhất
Không có sự can thiệp kiểm duyệt nghiêm trọng nào có thể chỉ dựa trên một kết quả phân loại tự động duy nhất (Văn bản + Ngữ cảnh + Hành vi + Ngôn ngữ + Phương tiện + Công cụ quy tắc = Đánh giá rủi ro).

### 21. Tín hiệu hành vi người dùng & Không có hệ thống tín dụng xã hội
Điều này liên quan đến các dấu hiệu lạm dụng kỹ thuật (ví dụ: đăng spam hàng loạt), không phải hệ thống xếp hạng xã hội chung. Nexus Gaja không duy trì Hệ thống tín dụng xã hội – việc kiểm duyệt nhằm mục đích bảo mật chứ không phải để đánh giá giá trị của một người.

### 22. AI kiểm duyệt phải được kiểm duyệt
Tất cả các quyết định tự động có liên quan đều được ghi lại (ID sự kiện, ID quy tắc, Độ tin cậy, Đánh giá con người, v.v.) để đảm bảo khả năng truy nguyên.

### 23. Kết quả dương tính giả, âm tính giả & thước đo chất lượng
Các loại lỗi được theo dõi. Trang tổng quan đo lường Độ chính xác, Thu hồi và đặc biệt là **Tỷ lệ đảo ngược khiếu nại** (số lượng khiếu nại thành công).

### 24. Công bằng ngôn ngữ & Xu hướng dịch thuật
Chất lượng kiểm duyệt phải tương đương nhau trên tất cả các ngôn ngữ được hỗ trợ (Điểm chuẩn kiểm duyệt đa ngôn ngữ). Nếu kết quả kiểm duyệt khác nhau giữa bản gốc và bản dịch (Xung đột bản dịch) thì điều này phải được xem xét cụ thể.

### 25. Đề xuất kiến trúc & Công cụ chính sách
Các quy tắc (Công cụ chính sách) không được mã hóa cứng vào các mô hình AI. AI cung cấp những phát hiện; Công cụ chính sách quyết định dựa trên các quy tắc hiện hành. Điều này cho phép **thay đổi mô hình mà không thay đổi quy tắc**.

### 26. Con Người Vẫn Là Quyền Quyết Định Cuối Cùng
- **NG-AI-MOD-001**: AI hỗ trợ phát hiện và phân loại nhưng không thay thế sự xem xét của con người trong các quyết định quan trọng.
- **NG-AI-MOD-002**: Các quyết định kiểm duyệt tự động phải có thể theo dõi, ghi lại và kiểm chứng được.

**Summary**: We are building a four-stage system: AI Detection, Context and Risk Analysis, Policy Engine, and Human Governance. This enables strong automation without creating a dangerous "AI as Judge" architecture.

## Nguyên tắc tài chính và mô hình doanh thu (WP 1.10.1)

For Nexus Gaja, a highly important economic principle applies: **No traditional advertising within the platform.**
This fundamentally distinguishes Nexus Gaja from many of today's social networks. However, this does not mean that Nexus Gaja cannot have a commercial character. On the contrary, the platform must be economically viable so that its social purpose can endure. Economic activity is a means to an end, not the primary purpose of the platform.

### 1. Nguyên lý NG-FIN-001
Nexus Gaja tài trợ cho hoạt động của mình thông qua các luồng doanh thu minh bạch tách biệt với lợi ích của người dùng chứ không phải thông qua việc kiếm tiền từ sự chú ý hoặc dữ liệu cá nhân của người dùng.

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

#### Trụ cột 1 – Tư cách thành viên cơ bản miễn phí
**Nexus Gaja Free** mang lại sự hiểu biết quốc tế cơ bản cho mọi người (hồ sơ, giao tiếp quốc tế, bài đăng, cộng đồng, cuộc trò chuyện, bản dịch cơ bản) miễn phí.

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

Để đảm bảo tính ổn định, bảo mật và khả năng mở rộng của hệ thống, Nexus Gaja tuân theo kiến ​​trúc nghiêm ngặt dựa trên API và hướng sự kiện.

### Nguyên tắc cốt lõi
- **Không có quyền truy cập cơ sở dữ liệu trực tiếp:** Các thành phần giao tiếp độc quyền thông qua các giao diện được xác định (API hoặc Sự kiện), không bao giờ thông qua các truy vấn cơ sở dữ liệu trực tiếp của các dịch vụ khác.
- **Cổng API:** Tất cả các yêu cầu của máy khách bên ngoài đều định tuyến thông qua việc xác thực, định tuyến và giới hạn tốc độ xử lý Cổng API.
- **Tóm tắt nhà cung cấp:** Các dịch vụ bên ngoài (mô hình AI, nhà cung cấp thanh toán, công cụ dịch thuật) được tích hợp thông qua các lớp trừu tượng, tránh sự phụ thuộc được mã hóa cứng và cho phép chuyển đổi nhà cung cấp linh hoạt.

### Các kiểu giao tiếp
- **API đồng bộ (REST/HTTPS):** Được sử dụng cho các yêu cầu ngay lập tức như đăng nhập, cài đặt hồ sơ hoặc dịch trực tiếp.
- **Sự kiện không đồng bộ (Bus sự kiện):** Hệ thống thần kinh trung ương của Nexus Gaja dành cho quá trình xử lý bị trì hoãn, tách rời (ví dụ: `Message.Created` kích hoạt Kiểm duyệt, Dịch và Thông báo không đồng bộ).
- **Thời gian thực (WebSocket):** Các kênh dành riêng cho chỉ báo nhập và trò chuyện trực tiếp.

### Bảo mật và độ tin cậy
- **Mô hình Zero-Trust:** Lưu lượng truy cập mạng nội bộ không được tự động tin cậy; giao tiếp dịch vụ với dịch vụ nhạy cảm yêu cầu xác thực.
- **Mẫu bình thường & hộp thư đi:** Các hoạt động quan trọng (như quyên góp hoặc nhắn tin) được thiết kế bình thường để ngăn chặn việc xử lý trùng lặp, sử dụng mẫu Hộp thư đi để đảm bảo các sự kiện không bao giờ bị mất ngay cả trong các giao dịch cơ sở dữ liệu.

## Mô hình miền MVP (WP 1.12)

Nexus Gaja sử dụng Kiến trúc MVP hướng miền (ADR-025) nghiêm ngặt, được thiết kế dưới dạng khối nguyên khối mô-đun với ranh giới miền rõ ràng. Cấu trúc này ngăn chặn sự phức tạp ban đầu của vi dịch vụ trong khi vẫn duy trì tính linh hoạt để phân chia các miền cụ thể sau này.

### Thực thể miền cốt lõi
Kiến trúc phân tách rõ ràng các khái niệm riêng biệt để đảm bảo tính toàn vẹn dữ liệu và tránh các cạm bẫy về cấu trúc như "Tên người dùng = Con người":
- **Danh tính & Tài khoản:** `Người` ≠ `Tài khoản người dùng` ≠ `Xác minh danh tính`. Một người đã được xác minh tham gia thông qua một tài khoản, nhưng các thực thể vẫn tách biệt.
- **Giao tiếp:** `Tin nhắn` ≠ `Dịch`. Thông điệp ban đầu vẫn không thay đổi; bản dịch là các thực thể được liên kết.
- **Kiểm duyệt:** `Báo cáo` ≠ `Quyết định kiểm duyệt`. Một báo cáo chỉ đơn thuần là một yêu cầu bồi thường; một trường hợp ôn hòa tiến hành điều tra.
- **Tài chính:** `Quyên góp` ≠ `Số dư quỹ`. Các khoản thanh toán được ghi nhận thông qua sổ cái bất biến của quỹ, đảm bảo tính minh bạch tài chính.

### Interconnected Domains
The system is divided into clear logical domains (Bounded Contexts): Identity, Account, Organization, Communication, Community, Language, Moderation, Notification, Finance, and Governance. These domains map the entire journey from real-world entities (Users, Schools, NGOs) to their digital interactions and related governance.

## Tình trạng dự án
Dự án hiện đang trong giai đoạn kiến trúc và quy hoạch tích cực.
Các quyết định về kiến ​​trúc đang diễn ra được ghi lại trong thư mục `/docs`.