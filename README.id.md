#Nexus Gaja

![Logo Nexus Gaja](assets/logo.jpg)

<details>
<summary>🌍 Available in 40 Languages (Click to expand)</summary>

[English](README.md) | [Deutsch](README.de.md) | [Türkçe](README.tr.md) | [Español](README.es.md) | [中文](README.zh.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Português](README.pt.md) | [Nederlands](README.nl.md) | [Русский](README.ru.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [العربية](README.ar.md) | [हिन्दी](README.hi.md) | [বাংলা](README.bn.md) | [Polski](README.pl.md) | [Bahasa Indonesia](README.id.md) | [Tiếng Việt](README.vi.md) | [ไทย](README.th.md) | [فارسی](README.fa.md) | [Українська](README.uk.md) | [Čeština](README.cs.md) | [Ελληνικά](README.el.md) | [Magyar](README.hu.md) | [Svenska](README.sv.md) | [Română](README.ro.md) | [Dansk](README.da.md) | [Suomi](README.fi.md) | [Norsk](README.no.md) | [Slovenčina](README.sk.md) | [Hrvatski](README.hr.md) | [Български](README.bg.md) | [Српски](README.sr.md) | [Lietuvių](README.lt.md) | [Latviešu](README.lv.md) | [Eesti](README.et.md) | [Slovenščina](README.sl.md) | [עברית](README.he.md) | [Kiswahili](README.sw.md) | [አማርኛ](README.am.md)

</details>

**Nexus Gaja** adalah jaringan komunikasi cerdas dan peka konteks yang dirancang untuk merevolusi komunikasi global.

## Tujuan dan Visi
Di dunia yang terglobalisasi, bahasa seringkali menjadi hambatan terbesar. Tujuan utama Nexus Gaja adalah untuk memungkinkan komunikasi yang lancar, bebas hambatan, dan akurat secara kontekstual antara orang-orang—terlepas dari apakah mereka berbicara dalam bahasa yang sama.

Ini bukan hanya tentang menerjemahkan kata-kata secara kaku, tetapi tentang **mentransfer makna**. Nexus Gaja menghubungkan orang-orang pada tingkat yang lebih dalam dengan memahami nuansa budaya, regional, dan kontekstual, sehingga memungkinkan percakapan yang tulus dan autentik.

## Kemungkinan dan Fitur
- **Komunikasi Multimedia**: Sistem tidak hanya memproses teks, tetapi juga gambar, audio, dan video. Hal ini memungkinkan percakapan yang benar-benar mendalam (misalnya, panggilan video atau pesan suara) secara real-time melintasi batasan bahasa.
- **Sensitivitas Konteks**: Pengenalan ironi, idiom, jargon, dan dialek daerah yang sering disalahpahami oleh penerjemah konvensional.
- **Jaringan Lintas Platform**: Berfungsi sebagai fondasi untuk obrolan pribadi, rangkaian pesan forum (postingan dengan komentar), dan interaksi komunitas global.

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

### 6. Bahasa Asli + Terjemahan
Asli dan terjemahan dianalisis secara terpisah. Baru setelah itu dilakukan “Penilaian Moderasi Gabungan”. Hal ini memungkinkan Nexus Gaja untuk menentukan apakah terjemahan itu sendiri mungkin telah meningkatkan atau mengubah fakta.

### 7. Skor Keyakinan
Setiap evaluasi AI menerima skor keyakinan (misalnya, probabilitas Ancaman: 0,96). Namun: **Skor Keyakinan ≠ Kebenaran.** Skor 96% hanya berarti model sangat yakin dengan klasifikasinya, belum tentu pengguna bersalah.

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

### 14. Konten Buatan AI
Kami membedakan antara: Buatan manusia, dibantu AI, dihasilkan AI, dan dimanipulasi AI. Ini akan menjadi bagian dari metadata konten.

### 15. Pelabelan Konten AI & Lapisan Asal AI
Menurut aturan transparansi UU AI UE (berlaku Agustus 2026), konten yang dihasilkan AI harus dapat diidentifikasi. Kami menyediakan AI Provenance Layer yang menyimpan metadata (AI-Origin, Model, Timestamp, Human Review).

### 16. Deteksi Deepfake
Arsitekturnya bertujuan untuk mendeteksi gambar sintetis, suara kloning, dan deepfake. Namun, deteksi tidak serta merta menjadi bukti.

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

## Status Proyek
Proyek ini saat ini sedang dalam tahap arsitektur dan perencanaan aktif.
Keputusan arsitektur yang sedang berlangsung didokumentasikan dalam folder `/docs`.