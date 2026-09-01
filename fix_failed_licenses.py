"""
Manually injects hardcoded native license translations for languages
where the Google Translate API failed.
"""

import os

FAILED_LANGS = {
    "am": ("README.am.md", """---

## ፍቃድ እና የአዕምሮ ንብረት

> **© 2024–2026 ጃን ሶነር / SonnerStudio — ሁሉም መብቶች የተጠበቁ ናቸው።**

**Nexus Gaja** የ**ጃን ሶነር** ብቸኛ የአዕምሮ ንብረት ነው፣ በ**SonnerStudio** ስር ይሠራል።

ጃን ሶነር ሁሉንም ፅንሰ-ሀሳቦች፣ አርክቴክቸር፣ ዶሜይን ሞዴሎች፣ የምርት ማንነት እና ተዛማጅ ሰነዶችን ጨምሮ የ Nexus Gaja ብቸኛ ፈጣሪ፣ አርክቴክት እና ባለቤት ነው።

**ምንም ዓይነት መብቶች፣ ፍቃዶች ወይም የባለቤትነት ጥቅሞች ለሶስተኛ ወገኖች አይሰጡም**፣ የቴክኖሎጂ ኢንዱስትሪ ውስጥ ያላቸው መጠን፣ የገበያ ቦታ ወይም ተጽዕኖ ምንም ይሁን።

### ያለ ግልጽ የጽሑፍ ፈቃድ የማይፈቀዱ ነገሮች:
- ❌ ይህንን ሶፍትዌር ወይም ሰነዶቹን መቅዳት፣ ማባዛት ወይም ማሰራጨት
- ❌ ማሻሻያ፣ ማላበሻ ወይም ተዋጽኦ ሥራዎች መፍጠር
- ❌ ከ Nexus Gaja ማንኛውም ክፍል የሚገኝ ንግዳዊ አጠቃቀም
- ❌ የዚህ ማከማቻ ይዘቶችን ለ AI ወይም LLM ስርዓቶች የሥልጠና ውሂብ አድርጎ መጠቀም
- ❌ ለሶስተኛ ወገኖች ፍቃዶችን ንዑስ-ፍቃድ ወይም ማስተላለፍ

### ያቀፈ የአዕምሮ ንብረት
የሚከተሉት ዋና ፅንሰ-ሀሳቦች በጃን ሶነር ባለቤትነት ምስጢሮች እና ብቸኛ ፈጠራዎች ተጠብቀዋል:
- ስፋት ያለው የግንኙነት ሞዴል *(ዋና / የትርጉም ትርጓሜ / የተተረጎመ ውጤት)*
- የማንነት ልዩነት መርህ *(ሰው ≠ መለያ ≠ የማንነት ማረጋገጫ)*
- የመልዕክት-ትርጉም መነጠፊያ ሞዴል *(መልዕክት ≠ ትርጉም)*
- AI ሞዴሬሽን አስተዳደር ማዕቀፍ

### ያግኙን
ለፍቃድ ጥያቄዎች: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" እና የ Nexus Gaja አርማ የጃን ሶነር ምልክቶች ናቸው። ስሙን ወይም ምርቱን ሳይፈቀድ መጠቀም የተከለከለ ነው።*

➡️ ሙሉ የፍቃድ ውሎችን በ [LICENSE](LICENSE) ፋይል ውስጥ ይመልከቱ
"""),

    "bg": ("README.bg.md", """---

## Лиценз и интелектуална собственост

> **© 2024–2026 Ян Сонер / SonnerStudio — Всички права запазени.**

**Nexus Gaja** е изключителна интелектуална собственост на **Ян Сонер**, работещ под **SonnerStudio**.

Ян Сонер е единственият създател, архитект и собственик на Nexus Gaja — включително всички концепции, архитектура, домейн модели, идентичност на марката и свързана документация.

**Никакви права, лицензи или права на собственост не се предоставят на трети страни**, независимо от техния размер, пазарна позиция или влияние в технологичната индустрия.

### Какво НЕ е разрешено без изрично писмено съгласие:
- ❌ Копиране, възпроизвеждане или разпространение на този софтуер или неговата документация
- ❌ Модифициране, адаптиране или създаване на производни произведения
- ❌ Търговско използване на каквато и да е част от Nexus Gaja
- ❌ Използване на съдържанието на това хранилище като данни за обучение на AI или LLM системи
- ❌ Сублицензиране или прехвърляне на права на трети страни

### Контакт
За запитвания относно лицензи: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*„Nexus Gaja" и логото на Nexus Gaja са търговски марки на Ян Сонер. Неупълномощеното използване на името или марката е забранено.*

➡️ Вижте пълните условия на лиценза в [LICENSE](LICENSE)
"""),

    "he": ("README.he.md", """---

## רישיון וקניין רוחני

> **© 2024–2026 ג'אן זונר / SonnerStudio — כל הזכויות שמורות.**

**Nexus Gaja** הוא הקניין הרוחני הבלעדי של **ג'אן זונר**, הפועל תחת **SonnerStudio**.

ג'אן זונר הוא היוצר, האדריכל והבעלים הבלעדי של Nexus Gaja — כולל כל המושגים, הארכיטקטורה, מודלי הדומיין, זהות המותג והתיעוד הנלווה.

**לא מוקנות זכויות, רישיונות או אינטרסי בעלות לצדדים שלישיים**, ללא קשר לגודלם, מעמדם בשוק או השפעתם בתעשיית הטכנולוגיה.

### מה אסור ללא הסכמה מפורשת בכתב:
- ❌ העתקה, שכפול או הפצה של תוכנה זו או תיעודה
- ❌ שינוי, התאמה או יצירת יצירות נגזרות
- ❌ שימוש מסחרי בכל חלק של Nexus Gaja
- ❌ שימוש בתכולת מאגר זה כנתוני אימון למערכות AI או LLM
- ❌ רישוי משנה או העברת זכויות לצדדים שלישיים

### יצירת קשר
לבירורי רישיון: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" ולוגו Nexus Gaja הם סימני מסחר של ג'אן זונר. שימוש בלתי מורשה בשם או במותג אסור.*

➡️ ראה תנאי רישיון מלאים ב-[LICENSE](LICENSE)
"""),

    "hr": ("README.hr.md", """---

## Licenca i intelektualno vlasništvo

> **© 2024–2026 Jan Sonner / SonnerStudio — Sva prava pridržana.**

**Nexus Gaja** je isključivo intelektualno vlasništvo **Jana Sonnera**, koji djeluje pod **SonnerStudio**.

Jan Sonner je jedini kreator, arhitekt i vlasnik Nexus Gaje — uključujući sve koncepte, arhitekturu, domenalne modele, identitet marke i povezanu dokumentaciju.

**Nikakva prava, licence ili vlasnički interesi nisu dodijeljeni trećim stranama**, bez obzira na njihovu veličinu, tržišnu poziciju ili utjecaj u tehnološkoj industriji.

### Što NIJE dopušteno bez izričitog pisanog pristanka:
- ❌ Kopiranje, reproduciranje ili distribucija ovog softvera ili njegove dokumentacije
- ❌ Modificiranje, prilagodba ili stvaranje izvedenih djela
- ❌ Komercijalna upotreba bilo kojeg dijela Nexus Gaje
- ❌ Korištenje sadržaja ovog repozitorija kao podataka za obuku AI ili LLM sustava
- ❌ Podlicenciranje ili prijenos prava trećim stranama

### Kontakt
Za upite o licenciranju: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*„Nexus Gaja" i logotip Nexus Gaja zaštitni su znakovi Jana Sonnera. Neovlaštena upotreba imena ili marke je zabranjena.*

➡️ Pogledajte pune uvjete licence u [LICENSE](LICENSE)
"""),

    "hu": ("README.hu.md", """---

## Licenc és szellemi tulajdon

> **© 2024–2026 Jan Sonner / SonnerStudio — Minden jog fenntartva.**

**A Nexus Gaja** a **SonnerStudio** keretében működő **Jan Sonner** kizárólagos szellemi tulajdona.

Jan Sonner a Nexus Gaja egyedüli alkotója, tervezője és tulajdonosa — beleértve az összes koncepciót, architektúrát, domain modellt, márkaazonosságot és a kapcsolódó dokumentációt.

**Semmilyen jog, licenc vagy tulajdoni érdek nem illeti meg harmadik feleket**, tekintet nélkül méretükre, piaci pozíciójukra vagy technológiai iparban betöltött befolyásukra.

### Mi NEM megengedett kifejezett írásbeli hozzájárulás nélkül:
- ❌ A szoftver vagy dokumentációjának másolása, sokszorosítása vagy terjesztése
- ❌ Módosítás, adaptálás vagy származékos művek létrehozása
- ❌ A Nexus Gaja bármely részének kereskedelmi felhasználása
- ❌ A repozitórium tartalmának AI vagy LLM rendszerek betanítási adatként való felhasználása
- ❌ Jogok allicencelése vagy átruházása harmadik felekre

### Kapcsolat
Licenc-kérdések esetén: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*A „Nexus Gaja" és a Nexus Gaja logó Jan Sonner védjegyei. A név vagy márka jogosulatlan használata tilos.*

➡️ A teljes licencfeltételeket a [LICENSE](LICENSE) fájlban találja
"""),

    "id": ("README.id.md", """---

## Lisensi & Kekayaan Intelektual

> **© 2024–2026 Jan Sonner / SonnerStudio — Semua hak dilindungi.**

**Nexus Gaja** adalah kekayaan intelektual eksklusif milik **Jan Sonner**, yang beroperasi di bawah **SonnerStudio**.

Jan Sonner adalah satu-satunya pencipta, arsitek, dan pemilik Nexus Gaja — termasuk semua konsep, arsitektur, model domain, identitas merek, dan dokumentasi terkait.

**Tidak ada hak, lisensi, atau kepentingan kepemilikan yang diberikan kepada pihak ketiga**, terlepas dari ukuran, posisi pasar, atau pengaruh mereka di industri teknologi.

### Yang TIDAK diizinkan tanpa persetujuan tertulis eksplisit:
- ❌ Menyalin, mereproduksi, atau mendistribusikan perangkat lunak ini atau dokumentasinya
- ❌ Memodifikasi, mengadaptasi, atau membuat karya turunan
- ❌ Penggunaan komersial dari bagian mana pun dari Nexus Gaja
- ❌ Menggunakan konten repositori ini sebagai data pelatihan untuk sistem AI atau LLM
- ❌ Mensublisensikan atau mentransfer hak kepada pihak ketiga

### Kontak
Untuk pertanyaan lisensi: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" dan logo Nexus Gaja adalah merek dagang Jan Sonner. Penggunaan nama atau merek yang tidak sah dilarang.*

➡️ Lihat ketentuan lisensi lengkap di [LICENSE](LICENSE)
"""),

    "it": ("README.it.md", """---

## Licenza e Proprietà Intellettuale

> **© 2024–2026 Jan Sonner / SonnerStudio — Tutti i diritti riservati.**

**Nexus Gaja** è proprietà intellettuale esclusiva di **Jan Sonner**, che opera sotto **SonnerStudio**.

Jan Sonner è il solo creatore, architetto e proprietario di Nexus Gaja — inclusi tutti i concetti, l'architettura, i modelli di dominio, l'identità del marchio e la documentazione associata.

**Nessun diritto, licenza o interesse di proprietà è concesso a terzi**, indipendentemente dalle loro dimensioni, posizione di mercato o influenza nel settore tecnologico.

### Cosa NON è consentito senza esplicito consenso scritto:
- ❌ Copiare, riprodurre o distribuire questo software o la sua documentazione
- ❌ Modificare, adattare o creare opere derivate
- ❌ Uso commerciale di qualsiasi parte di Nexus Gaja
- ❌ Utilizzo dei contenuti di questo repository come dati di addestramento per sistemi AI o LLM
- ❌ Sublicenziare o trasferire diritti a terzi

### Contatto
Per richieste di licenza: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" e il logo Nexus Gaja sono marchi di Jan Sonner. L'uso non autorizzato del nome o del marchio è vietato.*

➡️ Consulta i termini completi della licenza in [LICENSE](LICENSE)
"""),

    "ja": ("README.ja.md", """---

## ライセンスと知的財産権

> **© 2024–2026 Jan Sonner / SonnerStudio — 全ての権利を保有。**

**Nexus Gaja** は、**SonnerStudio** として活動する **Jan Sonner** の独占的な知的財産です。

Jan Sonner は、すべての概念、アーキテクチャ、ドメインモデル、ブランドアイデンティティ、および関連ドキュメントを含む Nexus Gaja の唯一の創造者、設計者、および所有者です。

**いかなる第三者にも権利、ライセンス、または所有権は付与されません**（テクノロジー業界での規模、市場での地位、または影響力にかかわらず）。

### 明示的な書面による同意なしに許可されていないこと:
- ❌ このソフトウェアまたはそのドキュメントのコピー、複製、または配布
- ❌ 修正、改変、または派生物の作成
- ❌ Nexus Gaja のいかなる部分の商業的使用
- ❌ このリポジトリのコンテンツを AI または LLM システムのトレーニングデータとして使用
- ❌ 第三者へのサブライセンスまたは権利の譲渡

### 連絡先
ライセンスに関するお問い合わせ: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*「Nexus Gaja」および Nexus Gaja ロゴは Jan Sonner の商標です。名前またはブランドの無断使用は禁止されています。*

➡️ 完全なライセンス条項は [LICENSE](LICENSE) ファイルをご覧ください
"""),

    "ko": ("README.ko.md", """---

## 라이선스 및 지적 재산권

> **© 2024–2026 Jan Sonner / SonnerStudio — 모든 권리 보유.**

**Nexus Gaja**는 **SonnerStudio** 산하에서 운영하는 **Jan Sonner**의 독점적 지적 재산입니다.

Jan Sonner는 모든 개념, 아키텍처, 도메인 모델, 브랜드 아이덴티티 및 관련 문서를 포함한 Nexus Gaja의 유일한 창작자, 설계자 및 소유자입니다.

**기술 업계에서의 규모, 시장 지위 또는 영향력에 관계없이 어떠한 제3자에게도 권리, 라이선스 또는 소유권이 부여되지 않습니다.**

### 명시적인 서면 동의 없이 허용되지 않는 사항:
- ❌ 이 소프트웨어 또는 문서의 복사, 재현 또는 배포
- ❌ 수정, 개조 또는 파생 작업 생성
- ❌ Nexus Gaja의 어떤 부분이든 상업적 사용
- ❌ 이 저장소의 내용을 AI 또는 LLM 시스템의 학습 데이터로 사용
- ❌ 제3자에게 권리 재라이선스 또는 양도

### 연락처
라이선스 문의: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" 및 Nexus Gaja 로고는 Jan Sonner의 상표입니다. 이름이나 브랜드의 무단 사용은 금지되어 있습니다.*

➡️ 전체 라이선스 조건은 [LICENSE](LICENSE) 파일을 참조하세요
"""),

    "lt": ("README.lt.md", """---

## Licencija ir intelektinė nuosavybė

> **© 2024–2026 Jan Sonner / SonnerStudio — Visos teisės saugomos.**

**Nexus Gaja** yra išskirtinė **Jan Sonner**, veikiančio **SonnerStudio** vardu, intelektinė nuosavybė.

Jan Sonner yra vienintelis Nexus Gaja kūrėjas, architektas ir savininkas — įskaitant visas sąvokas, architektūrą, domeno modelius, prekės ženklo tapatybę ir susijusius dokumentus.

**Jokios teisės, licencijos ar nuosavybės interesai nėra suteikiami trečiosioms šalims**, neatsižvelgiant į jų dydį, rinkos poziciją ar įtaką technologijų pramonėje.

### Kas NELEIDŽIAMA be aiškaus raštiško sutikimo:
- ❌ Šios programinės įrangos ar jos dokumentacijos kopijavimas, dauginimas ar platinimas
- ❌ Modifikavimas, adaptavimas ar išvestinių kūrinių kūrimas
- ❌ Bet kurios Nexus Gaja dalies komercinis naudojimas
- ❌ Šios saugyklos turinio naudojimas kaip AI ar LLM sistemų mokymo duomenys
- ❌ Teisių sublicencijavimas ar perdavimas trečiosioms šalims

### Kontaktai
Licencijos klausimais: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*„Nexus Gaja" ir Nexus Gaja logotipas yra Jan Sonner prekių ženklai. Neteisėtas vardo ar prekės ženklo naudojimas yra draudžiamas.*

➡️ Visas licencijos sąlygas žr. [LICENSE](LICENSE) faile
"""),
}

# Marker to find and replace
ENGLISH_MARKER = "\n\n---\n\n## License & Intellectual Property"

for lang, (filename, native_license) in FAILED_LANGS.items():
    if not os.path.exists(filename):
        print(f"[SKIP] {filename} not found")
        continue

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove existing English license block
    idx = content.find(ENGLISH_MARKER)
    if idx == -1:
        # Try alternate
        idx = content.rfind("\n---\n")
        if idx == -1:
            print(f"[WARN] No license marker found in {filename}")
            base_content = content
        else:
            base_content = content[:idx]
    else:
        base_content = content[:idx]

    with open(filename, "w", encoding="utf-8") as f:
        f.write(base_content)
        f.write(native_license)

    print(f"[OK] {filename} — native {lang} license injected")

print("\nAll failed languages fixed!")
