#Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** adalah jaringan komunikasi cerdas dan peka konteks yang dirancang untuk merevolusi komunikasi global.

## Tujuan dan Visi
Di dunia yang terglobalisasi, bahasa sering kali menjadi hambatan terbesar. Tujuan utama Nexus Gaja adalah untuk memungkinkan komunikasi yang lancar, bebas hambatan, dan akurat secara kontekstual antara orang-orang—terlepas dari apakah mereka berbicara dalam bahasa yang sama.

Ini bukan hanya tentang menerjemahkan kata-kata secara kaku, tetapi tentang **mentransfer makna**. Nexus Gaja menghubungkan orang-orang pada tingkat yang lebih dalam dengan memahami nuansa budaya, regional, dan kontekstual, sehingga memungkinkan percakapan yang tulus dan autentik.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

---

## Arsitektur Teknis (Konsep Inti)

Inti teknis Nexus Gaja adalah model komunikasi yang dibuat khusus dan dibagi menjadi tiga lapisan:

1. **Asli**: Objek komunikasi (pesan) yang dibuat oleh pengirim selalu tidak dapat diubah.
2. **Interpretasi Semantik**: Sistem menganalisis tidak hanya kata-kata, tetapi makna sebenarnya.
3. **Representasi Bahasa Target**: AI hanya membuat representasi sementara atau cache dari dokumen asli untuk masing-masing penerima berdasarkan bahasa pilihan mereka. Terjemahan tidak pernah menimpa pesan aslinya.

### Ketergantungan Konteks
Terjemahan di Nexus Gaja tidak pernah melihat pesan secara terpisah. Mesin mempertimbangkan seluruh hierarki:
`Pesan` → `Pesan Sebelumnya` → `Konteks Utas` → `Konteks Komunitas` → `Bahasa/Wilayah` → `Preferensi Pengguna`

### Efisiensi melalui Terjemahan Sesuai Permintaan
Penerjemahan hanya dilakukan dengan hemat sumber daya **atas permintaan** (Sesuai Permintaan). Saat pengguna meminta konten, konten tersebut diterjemahkan ke dalam bahasa yang telah ditetapkan sebelumnya. Setelah terjemahan untuk bahasa tertentu dibuat, terjemahan tersebut disimpan secara permanen (cache) untuk mempercepat permintaan di masa mendatang secara drastis.

## Moderasi Berbantuan AI (WP 1.8.4)

Dengan Moderasi Berbantuan AI, kami mengambil langkah signifikan mulai dari ide produk hingga arsitektur teknis, dengan mempertimbangkan peraturan UE saat ini (persyaratan transparansi UU AI UE berdasarkan Pasal 50; Undang-Undang Layanan Digital dengan justifikasi yang dapat dipahami dan opsi banding).

### 1. Prinsip Dasar
Kalimat paling penting untuk arsitektur ini adalah: **Moderasi AI adalah sistem peninjauan, bukan sistem pemerintahan yang otonom.**
Hal ini dirancang untuk membantu manusia dalam jumlah sedang, bukan untuk menentukan sendiri opini mana yang boleh ada di Nexus Gaja.
Kami membedakan antara tiga tingkatan:
- **Deteksi:** "Mungkin ada pelanggaran aturan di sini."
- **Evaluasi:** "Kemungkinan pelanggaran aturan, misalnya, adalah 94%."
- **Keputusan:** "Tindakan apa yang sebenarnya diambil?"
Tingkat ketiga harus dikendalikan oleh manusia dalam kasus yang parah.

### 2. Moderasi AI sebagai Subsistem
Alih-alih menggunakan AI tunggal, subsistem yang kuat akan dibuat:
```teks
                 MODERASI NEXUS GAJA AI
                          │
       ┌───────────────────┼───────────────────┐
       │ │ │
  Bahasa AI Keamanan AI Penipuan AI
       │ │ │
       ├───────────────┬───┴───────────────┬───┤
       │ │ │
 Identitas Perilaku Penerjemahan
 Analisis Sinyal Analisis
       │ │ │
       └───────────────┼───────────────────┘
                      ▼
               Penilaian Risiko
                      │
                      ▼
               Tinjauan Manusia
```

### 3. Modul AI Paling Penting
Nexus Gaja menggunakan sembilan area analisis khusus:
- **M1 – Pemahaman Bahasa**: Mendeteksi bahasa, dialek, bahasa gaul, indikator ironi, masalah terjemahan.
- **M2 – Deteksi Toksisitas / Penyalahgunaan**: Mendeteksi penghinaan, serangan pribadi, pelecehan.
- **M3 – Deteksi Ancaman**: Mendeteksi potensi ancaman, pemerasan, pengumuman kekerasan.
- **M4 – Deteksi Kebencian / Dehumanisasi**: Mendeteksi serangan yang ditargetkan pada orang berdasarkan afiliasi tertentu.
- **M5 – Deteksi Spam / Manipulasi**: Mendeteksi spam, perilaku bot, manipulasi terkoordinasi.
- **M6 – Deteksi Penipuan**: Mendeteksi upaya penipuan yang mencurigakan, phishing, rekayasa sosial.
- **M7 – Integritas Identitas**: Memeriksa sinyal terkait pengambilalihan akun, banyak akun, penghindaran larangan.
- **M8 – Keamanan Media**: Menganalisis gambar, audio, video, dokumen.
- **M9 – Mesin Konteks**: Modul paling penting. Ini menggabungkan temuan individu.

### 4. Mengapa Mesin Konteks Penting
Pencarian kata kunci murni tidak akan cukup. "Aku bisa membunuhnya karena tertawa" secara semantik mengandung kekerasan tetapi merupakan kiasan. "Besok jam 8 malam saya akan menembaknya di depan rumahnya" adalah situasi yang sangat berbeda. AI harus memahami arti pernyataan tersebut dalam konteks spesifiknya.

### 5. Moderasi Multibahasa
Moderasi tidak bisa sekadar membandingkan kata-kata. Itu harus menganalisis tingkat semantik (misalnya, idiom Jerman vs. idiom Jepang vs. ekspresi regional).

### 6. Original Language + Translation
Original and translation are analyzed separately. Only then does the "Combined Moderation Assessment" take place. This allows Nexus Gaja to determine whether the translation itself may have escalated or altered the facts.

### 7. Confidence Score
Every AI evaluation receives a confidence score (e.g., Threat probability: 0.96). However: **Confidence Score ≠ Truth.** A score of 96% only means the model is highly certain of its classification, not necessarily that the user is guilty.

### 8. Ketidakpastian Menjadi Sinyal Itu Sendiri
Jika AI tidak yakin (misalnya, Ancaman: 0,62, Satire: 0,54), AI tidak boleh sekadar menerapkan aturan yang keras. Sebaliknya, ketidakpastian dibangun langsung ke dalam arsitektur: **Diperlukan Tinjauan Manusia**.

### 9. Empat Zona Keputusan
- 🟢 **HIJAU**: Kemungkinan besar sesuai. → tidak ada tindakan.
- 🟡 **KUNING** : Kemungkinan pelanggaran. → pantau / berikan peringatan bila perlu.
- 🟠 **ORANGE**: Kemungkinan pelanggaran. → tinjauan moderasi.
- 🔴 **MERAH**: Kemungkinan pelanggaran berat. → tindakan perlindungan segera + tinjauan manusia.

### 10. Tidak Ada "Hukuman AI"
**AI tidak memberikan sanksi akhir.** AI dapat memicu tindakan teknis segera (misalnya, menahan pesan untuk sementara) karena masalah keamanan yang parah, namun keputusan akhir tetap dapat diverifikasi.

### 11. Tindakan Perlindungan Dapat Terjadi Secara Otomatis
Jika terjadi ancaman nyata (Ancaman terdeteksi → Keyakinan tinggi → Pembatasan sementara → Peninjauan manusia → Keputusan), kami melindungi pengguna yang terancam tanpa menjadikan AI sebagai hakim.

### 12. AI Harus Mampu Membenarkan Keputusannya
DSA memerlukan alasan yang jelas dan spesifik. AI memberikan alasan terstruktur: Aturan (NG-CONDUCT-004), Terdeteksi (Potensi ancaman nyata), Keyakinan (0,94), Konteks yang relevan (4 pesan sebelumnya), Tindakan yang disarankan (Tinjauan manusia).

### 13. AI Tidak Boleh Mengubah Konten Secara Diam-diam
**Moderasi AI tidak boleh mengubah konten asli tanpa diketahui.** Selama koreksi otomatis, terjemahan, atau ringkasan, konten asli selalu dipertahankan.

### 14. AI-Generated Content
We distinguish between: Human-created, AI-assisted, AI-generated, and AI-manipulated. This will become part of the content metadata.

### 15. Labeling of AI Content & AI Provenance Layer
According to the transparency rules of the EU AI Act (effective August 2026), AI-generated content must be identifiable. We provide an AI Provenance Layer that stores metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deepfake Detection
The architecture aims to detect synthetic images, cloned voices, and deepfakes. However, detection is not automatically proof.

### 17. Tidak Ada "Mesin Kebenaran" Otomatis (Moderasi ≠ Pengecekan Fakta)
Satu sistem memeriksa: "Apakah konten tersebut melanggar aturan?" (Moderasi Konten), yang lain memberikan: "Informasi dan sumber apa yang tersedia?" (Bantuan Informasi). Pendapat tidak dihapus begitu saja karena dianggap "salah".

### 18. Perlindungan Terhadap Salah Tafsir Budaya
AI memerlukan **Model Konteks Budaya** untuk mencegah norma komunikasi suatu negara dianggap sebagai standar global.

### 19. Ironi, Sindiran, dan Humor
AI menggunakan konteks, emoji, riwayat percakapan, dan struktur ironi yang diketahui, namun harus memperhitungkan ketidakpastian ketika maknanya ambigu.

### 20. Tidak Ada Hukuman Berdasarkan Skor AI Tunggal
Intervensi moderasi berat tidak boleh hanya didasarkan pada satu hasil klasifikasi otomatis (Teks + Konteks + Perilaku + Bahasa + Media + Mesin Aturan = Penilaian Risiko).

### 21. Sinyal Perilaku Pengguna & Tidak Ada Sistem Kredit Sosial
Hal ini berkaitan dengan sinyal penyalahgunaan teknis (misalnya, postingan spam massal), bukan sistem rating sosial secara umum. Nexus Gaja tidak menerapkan Sistem Kredit Sosial – moderasi bertujuan untuk keamanan, bukan penilaian terhadap nilai seseorang.

### 22. AI Moderasi Harus Dapat Diaudit
Semua keputusan otomatis yang relevan dicatat (ID Peristiwa, ID Aturan, Keyakinan, Tinjauan Manusia, dll.) untuk memastikan ketertelusuran.

### 23. Positif Palsu, Negatif Palsu & Metrik Kualitas
Jenis kesalahan dipantau. Dasbor mengukur Presisi, Perolehan Kembali, dan khususnya **Tingkat Pembalikan Banding** (jumlah banding yang berhasil).

### 24. Kesetaraan Bahasa & Bias Terjemahan
Kualitas moderasi harus sebanding di semua bahasa yang didukung (Tolok Ukur Moderasi Multibahasa). Jika hasil moderasi berbeda antara asli dan terjemahan (Konflik Terjemahan), maka hal ini harus ditinjau secara khusus.

### 25. Proposal Arsitektur & Mesin Kebijakan
Aturan (Mesin Kebijakan) tidak dikodekan secara hardcode ke dalam model AI. AI memberikan temuan; Mesin Kebijakan memutuskan berdasarkan aturan saat ini. Hal ini memungkinkan **perubahan model tanpa perubahan aturan**.

### 26. Manusia Tetap Menjadi Otoritas Terakhir
- **NG-AI-MOD-001**: AI membantu dalam deteksi dan klasifikasi, namun tidak menggantikan tinjauan manusia dalam pengambilan keputusan yang berat.
- **NG-AI-MOD-002**: Keputusan moderasi otomatis harus dapat dilacak, dapat dicatat, dan dapat diverifikasi.

**Ringkasan**: Kami sedang membangun sistem empat tahap: Deteksi AI, Analisis Konteks dan Risiko, Mesin Kebijakan, dan Tata Kelola Manusia. Hal ini memungkinkan otomatisasi yang kuat tanpa menciptakan arsitektur "AI sebagai Hakim" yang berbahaya.

## Prinsip Pembiayaan dan Model Pendapatan (WP 1.10.1)

Bagi Nexus Gaja, prinsip ekonomi yang sangat penting berlaku: **Tidak ada iklan tradisional dalam platform.**
Hal ini secara mendasar membedakan Nexus Gaja dari banyak jejaring sosial saat ini. Meski demikian, bukan berarti Nexus Gaja tidak bisa bersifat komersil. Sebaliknya, platform tersebut harus layak secara ekonomi agar tujuan sosialnya dapat bertahan. Aktivitas ekonomi adalah alat untuk mencapai tujuan, bukan tujuan utama platform ini.

### 1. Prinsip NG-FIN-001
Nexus Gaja membiayai operasinya melalui aliran pendapatan transparan yang dipisahkan dari kepentingan pengguna, dan bukan melalui monetisasi perhatian atau data pribadi penggunanya.

### 2. Tidak Ada Iklan Tradisional
Yang secara khusus dilarang adalah:
- Iklan spanduk
- Iklan munculan
- Iklan video yang diputar otomatis
- Postingan bersponsor di feed standar
- Profil iklan yang dipersonalisasi
- Penjualan profil pengguna atau data pribadi
- Iklan berasal dari percakapan pribadi.

Nexus Gaja tetap menjadi **ruang komunikasi, bukan ruang iklan**.

### 3. Pembiayaan Tanpa Iklan (6 Pilar)
Pembiayaan dibangun berdasarkan enam pilar:
```teks
                 NEXUS GAJA
                     │
       ┌──────────────┼──────────────┐
       ▼ ▼ ▼
   DONASI ORGANISASI PREMIUM
       │ │ │
       ├──────────────┼──────────────┤
       ▼ ▼ ▼
    JASA KEMITRAAN HIBAH
```

#### Pilar 1 – Keanggotaan Dasar Gratis
**Nexus Gaja Free** memungkinkan pemahaman internasional dasar untuk semua orang (profil, komunikasi internasional, postingan, komunitas, obrolan, terjemahan dasar) tanpa biaya.

#### Pilar 2 – Penawaran Premium
Penawaran berbayar sukarela (**Nexus Gaja Plus**) memberikan batas penyimpanan yang lebih besar, kualitas media yang lebih tinggi, kuota AI yang diperluas, dan fitur organisasi.
**Penting (Freemium, bukan Dark Freemium):** Komunikasi dasar tidak boleh didegradasi secara artifisial.

#### Pilar 3 – Organisasi
Rekening khusus untuk sekolah, universitas, LSM, bisnis, dan kota (**Nexus Gaja Organization**). Sekolah dapat didukung melalui tingkat kelembagaan sebagai pengganda pemahaman internasional.

#### Pilar 4 – Donasi
**Kolam Pendanaan Nexus Gaja** menerima donasi umum dan khusus (misalnya, "untuk komunikasi pemuda internasional"). **Buku Besar Alokasi Dana** memastikan alokasi dana yang transparan.
**Dana Tujuan & Tombola:** Sebagian donasi diberikan ke kumpulan untuk penggunaan gratis/diskon. Mekanisme lotere/tombola dapat mengalokasikan dana tersebut secara transparan dan auditable.

#### Pilar 5 – Pendanaan Kelembagaan
Yayasan, program pendanaan budaya, atau program negara.
**NG-FIN-002:** Dukungan finansial tidak membeli kendali editorial atau teknis (Kemerdekaan).

#### Pilar 6 – Pelayanan Komersial
Layanan B2B seperti **Translation-as-a-Service** (API), komunikasi organisasi, atau ruang konferensi internasional, tanpa membebani feed pengguna standar.

### 4. Tidak Ada Monetisasi Data & Pengawasan Ekonomi
**NG-FIN-003:** Data pengguna pribadi bukan merupakan komoditas. Tidak ada penjualan daftar, profil, atau riwayat. Nexus Gaja tidak mengambil keuntungan dari pengawasan psikologis (Surveillance Economy).

### 5. Transparansi Keuangan & Buku Besar Dana
**Transparansi Keuangan Nexus Gaja:** Publikasi struktur keuangan agregat. Sumbangan yang dialokasikan menerima akuntansi teknis (ID Dana → Tujuan → Saldo → Alokasi). Tidak ada subsidi silang untuk tujuan sosial ke dalam pemasaran korporat.

### 6. Model Pembiayaan Berbasis Solidaritas
Penetapan harga didasarkan pada orientasi biaya, keadilan, dan solidaritas.
**Solidaritas Premium:** Opsi sukarela bagi pengguna Premium untuk membiayai sebagian dari akses pengguna lain. Solidaritas yang dipaksakan atau masyarakat kelas premium (kurang menghormati/moderasi bagi pengguna gratis) sangat dilarang.

### 7. KPI Ekonomi Daripada Ekonomi Keterlibatan
Tidak ada ketergantungan pada menjaga pengguna "online selama mungkin" (tidak ada ragebait, feed tanpa batas).
Sebagai gantinya, kami menggunakan metrik seperti:
- **Indeks Komunikasi Global (GCI):** Hubungan komunikasi yang sukses antara orang-orang dari wilayah bahasa/budaya yang berbeda.
- **Rasio Keberlanjutan Platform (PSR):** Pendapatan berulang / biaya operasional berulang (Target ≥ 1).

### 8. Apa yang Secara Jelas Tidak Kita Inginkan (Daftar Negatif)
Nexus Gaja **tidak** dibiayai oleh:
❌ Penjualan data pribadi
❌ Iklan tradisional yang dipersonalisasi
❌ Memantau perilaku pengguna untuk tujuan periklanan
❌ Penjualan data komunikasi pribadi
❌ Penggunaan data AI tersembunyi
❌ Paywall Premium yang manipulatif
❌ Pembatasan jangkauan buatan untuk monetisasi
❌ Pengaruh politik berbayar
❌ Pembelian keputusan moderasi yang memiliki hak istimewa.

### 9. Arsitektur Keuangan Awal
```teks
                         NEXUS GAJA
                              │
             ┌─────────────────┼─────────────────┐
             │ │ │
             ▼ ▼ ▼
          PERUSAHAAN ORGANISASI PENGGUNA
             │ │ │
             └──────────────────┼─────────────────┘
                              │
                       LAYANAN PLATFORM
                              │
          ┌─────────────────────┼────────────────────┐
          ▼ ▼ ▼
       API DONASI PREMIUM
                              │
                    ┌─────────┴─────────┐
                    ▼ ▼
               DANA UMUM DANA TERBATAS
                                        │
                                        ▼
                                  TUJUAN SOSIAL
```

### Ringkasan Prinsip Pembiayaan (NG-FIN)
- **NG-FIN-001:** Tidak ada pembiayaan melalui iklan tradisional.
- **NG-FIN-002:** Tidak ada kontrol editorial/teknis melalui dukungan keuangan.
- **NG-FIN-003:** Data pribadi bukan merupakan komoditas.
- **NG-FIN-004:** Komunikasi dasar tetap dapat diakses tanpa pembayaran.
- **NG-FIN-005:** Penawaran premium tidak boleh merendahkan pengguna gratis.
- **NG-FIN-006:** Dana yang dialokasikan dikelola sesuai peruntukannya.
- **NG-FIN-007:** Pengelolaan donasi dan hibah yang transparan.
- **NG-FIN-008:** Layanan B2B komersial tidak mengurangi independensi.
- **NG-FIN-009:** Fokus pada keberlanjutan daripada monetisasi maksimal.
- **NG-FIN-010:** Struktur ini secara permanen menjamin tujuan sosial.

## API, Antarmuka, dan Arsitektur Komunikasi (WP 1.11.3)

To ensure system stability, security, and scalability, Nexus Gaja follows a strictly API-first and event-driven architecture. 

### Core Principles
- **No Direct Database Access:** Components communicate exclusively via defined interfaces (APIs or Events), never through direct database queries of other services.
- **API Gateway:** All external client requests route through an API Gateway handling authentication, routing, and rate limiting.
- **Provider Abstraction:** External services (AI models, payment providers, translation engines) are integrated via abstraction layers, avoiding hardcoded dependencies and enabling flexible provider swapping.

### Communication Patterns
- **Synchronous APIs (REST/HTTPS):** Used for immediate requests like login, profile settings, or direct translations.
- **Asynchronous Events (Event Bus):** The central nervous system of Nexus Gaja for delayed, decoupled processing (e.g., `Message.Created` triggering Moderation, Translation, and Notification asynchronously).
- **Realtime (WebSocket):** Dedicated channels for live chat and typing indicators.

### Security and Reliability
- **Zero-Trust Model:** Internal network traffic is not automatically trusted; sensitive service-to-service communication requires authentication.
- **Idempotency & Outbox Pattern:** Critical operations (like donations or messaging) are designed to be idempotent to prevent duplicate processing, utilizing the Outbox pattern to ensure events are never lost even during database transactions.

## MVP Domain Model (WP 1.12)

Nexus Gaja menggunakan Arsitektur MVP Berbasis Domain (ADR-025) yang dirancang sebagai monolit modular dengan batas domain yang jelas. Struktur ini mencegah kompleksitas layanan mikro yang prematur sekaligus mempertahankan fleksibilitas untuk memisahkan domain tertentu di kemudian hari.

### Entitas Domain Inti
Arsitekturnya secara eksplisit memisahkan konsep-konsep berbeda untuk memastikan integritas data dan menghindari kesalahan struktural seperti "Nama Pengguna = Manusia":
- **Identitas & Akun:** `Orang` ≠ `Akun Pengguna` ≠ `Verifikasi Identitas`. Orang yang terverifikasi berpartisipasi melalui akun, namun entitasnya tetap terpisah.
- **Komunikasi:** `Pesan` ≠ `Terjemahan`. Pesan aslinya tetap tidak berubah; terjemahan adalah entitas yang terhubung.
- **Moderasi:** `Laporan` ≠ `Keputusan Moderasi`. Laporan hanyalah sebuah klaim; kasus moderasi melakukan penyelidikan.
- **Keuangan:** `Sumbangan` ≠ `Saldo Dana`. Pembayaran dibukukan melalui buku besar yang tidak dapat diubah ke suatu dana, sehingga memastikan transparansi keuangan.

### Domain yang Saling Berhubungan
Sistem ini dibagi ke dalam domain logis yang jelas (Konteks Terikat): Identitas, Akun, Organisasi, Komunikasi, Komunitas, Bahasa, Moderasi, Pemberitahuan, Keuangan, dan Tata Kelola. Domain-domain ini memetakan keseluruhan perjalanan dari entitas dunia nyata (Pengguna, Sekolah, LSM) hingga interaksi digital dan tata kelola terkait.

## Status Proyek
Proyek ini saat ini sedang dalam tahap arsitektur dan perencanaan aktif.
Keputusan arsitektur yang sedang berlangsung didokumentasikan dalam folder `/docs`.