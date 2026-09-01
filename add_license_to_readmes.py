import os
import glob

LICENSE_EN = """
---

## License & Intellectual Property

> **© 2024–2026 Jan Sonner / SonnerStudio — All rights reserved.**

**Nexus Gaja** is the exclusive intellectual property of **Jan Sonner**, operating under **SonnerStudio**.

Jan Sonner is the sole creator, architect, and owner of Nexus Gaja — including all concepts, architecture, domain models, brand identity, and associated documentation.

**No rights, licenses, or ownership interests are held by any third party**, regardless of their size, market position, or influence in the technology industry.

### What is NOT permitted without explicit written consent:
- ❌ Copying, reproducing, or distributing this software or its documentation
- ❌ Modifying, adapting, or creating derivative works
- ❌ Commercial use of any part of Nexus Gaja
- ❌ Using the contents of this repository as **training data for AI/LLM systems**
- ❌ Sublicensing or transferring any rights to third parties

### Protected Intellectual Property
The following original concepts are protected as trade secrets and proprietary creations of Jan Sonner:
- The layered communication model *(Original / Semantic Interpretation / Translated Output)*
- The identity separation principle *(Person ≠ Account ≠ Identity Verification)*
- The Message-Translation decoupling model *(Message ≠ Translation)*
- The AI moderation governance framework

### Contact
For licensing inquiries: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*"Nexus Gaja" and the Nexus Gaja logo are trademarks of Jan Sonner. Unauthorized use of the name or brand is prohibited.*

➡️ See full license terms in [LICENSE](LICENSE)
"""

LICENSE_TRANSLATIONS = {
    "de": """
---

## Lizenz & Geistiges Eigentum

> **© 2024–2026 Jan Sonner / SonnerStudio — Alle Rechte vorbehalten.**

**Nexus Gaja** ist das ausschließliche geistige Eigentum von **Jan Sonner**, tätig unter **SonnerStudio**.

Jan Sonner ist der alleinige Schöpfer, Architekt und Inhaber von Nexus Gaja — einschließlich aller Konzepte, Architekturen, Domänenmodelle, Markenidentität und zugehörigen Dokumentationen.

**Keinerlei Rechte, Lizenzen oder Eigentumsinteressen werden Dritten gewährt**, unabhängig von deren Größe, Marktstellung oder Einfluss in der Technologiebranche.

### Was NICHT ohne ausdrückliche schriftliche Zustimmung gestattet ist:
- ❌ Kopieren, Vervielfältigen oder Verbreiten dieser Software oder ihrer Dokumentation
- ❌ Modifizieren, Anpassen oder Erstellen abgeleiteter Werke
- ❌ Kommerzielle Nutzung jeglicher Teile von Nexus Gaja
- ❌ Verwendung des Repository-Inhalts als **Trainingsdaten für KI/LLM-Systeme**
- ❌ Unterlizenzierung oder Übertragung von Rechten an Dritte

### Geschütztes geistiges Eigentum
Folgende Originalkonzepte sind als Geschäftsgeheimnisse und proprietäre Schöpfungen von Jan Sonner geschützt:
- Das mehrschichtige Kommunikationsmodell *(Original / Semantische Interpretation / Übersetzte Ausgabe)*
- Das Identitätstrennungsprinzip *(Person ≠ Benutzerkonto ≠ Identitätsverifikation)*
- Das Nachricht-Übersetzungs-Entkopplungsmodell *(Nachricht ≠ Übersetzung)*
- Das KI-Moderations-Governance-Framework

### Kontakt
Für Lizenzanfragen: [github.com/SonnerStudio](https://github.com/SonnerStudio)

*„Nexus Gaja" und das Nexus-Gaja-Logo sind Marken von Jan Sonner. Die unbefugte Verwendung des Namens oder der Marke ist untersagt.*

➡️ Vollständige Lizenzbedingungen in [LICENSE](LICENSE)
""",
    "es": """
---

## Licencia y Propiedad Intelectual

> **© 2024–2026 Jan Sonner / SonnerStudio — Todos los derechos reservados.**

**Nexus Gaja** es propiedad intelectual exclusiva de **Jan Sonner**, que opera bajo **SonnerStudio**.

Jan Sonner es el único creador, arquitecto y propietario de Nexus Gaja, incluyendo todos los conceptos, arquitecturas, modelos de dominio, identidad de marca y documentación asociada.

**Ningún derecho, licencia o interés de propiedad es otorgado a terceros**, independientemente de su tamaño, posición en el mercado o influencia en la industria tecnológica.

### Lo que NO está permitido sin consentimiento escrito explícito:
- ❌ Copiar, reproducir o distribuir este software o su documentación
- ❌ Modificar, adaptar o crear obras derivadas
- ❌ Uso comercial de cualquier parte de Nexus Gaja
- ❌ Usar el contenido de este repositorio como **datos de entrenamiento para sistemas de IA/LLM**
- ❌ Sublicenciar o transferir derechos a terceros

### Contacto
Para consultas de licencias: [github.com/SonnerStudio](https://github.com/SonnerStudio)

➡️ Ver términos completos de licencia en [LICENSE](LICENSE)
""",
    "tr": """
---

## Lisans ve Fikri Mülkiyet

> **© 2024–2026 Jan Sonner / SonnerStudio — Tüm hakları saklıdır.**

**Nexus Gaja**, **SonnerStudio** bünyesinde faaliyet gösteren **Jan Sonner**'ın münhasır fikri mülkiyetidir.

Jan Sonner, tüm kavramlar, mimariler, alan modelleri, marka kimliği ve ilgili belgeler dahil olmak üzere Nexus Gaja'nın tek yaratıcısı, mimarı ve sahibidir.

**Teknoloji sektöründeki büyüklükleri, piyasa konumları veya etkileri ne olursa olsun, hiçbir üçüncü tarafa herhangi bir hak, lisans veya mülkiyet çıkarı tanınmamaktadır.**

### Açık yazılı izin olmaksızın YAPILAMAYACAKLAR:
- ❌ Bu yazılımın veya belgelerinin kopyalanması, çoğaltılması veya dağıtılması
- ❌ Değiştirme, uyarlama veya türev eserler oluşturma
- ❌ Nexus Gaja'nın herhangi bir bölümünün ticari kullanımı
- ❌ Bu deponun içeriğinin **yapay zeka/LLM sistemleri için eğitim verisi** olarak kullanılması
- ❌ Hakların üçüncü taraflara alt lisanslama veya devredilmesi

### İletişim
Lisans sorguları için: [github.com/SonnerStudio](https://github.com/SonnerStudio)

➡️ Tam lisans koşulları için [LICENSE](LICENSE) dosyasına bakın
""",
    "zh": """
---

## 许可证与知识产权

> **© 2024–2026 Jan Sonner / SonnerStudio — 保留所有权利。**

**Nexus Gaja** 是 **Jan Sonner**（以 **SonnerStudio** 名义运营）的专有知识产权。

Jan Sonner 是 Nexus Gaja 的唯一创造者、架构师和所有者，包括所有概念、架构、领域模型、品牌标识及相关文档。

**无论任何第三方在技术行业的规模、市场地位或影响力如何，均不授予任何权利、许可或所有权权益。**

### 未经明确书面同意，不得进行以下操作：
- ❌ 复制、再现或分发本软件或其文档
- ❌ 修改、改编或创建衍生作品
- ❌ 将 Nexus Gaja 的任何部分用于商业目的
- ❌ 将本存储库内容用作**人工智能/大语言模型系统的训练数据**
- ❌ 向第三方转授许可或转让权利

### 联系方式
许可查询：[github.com/SonnerStudio](https://github.com/SonnerStudio)

➡️ 完整许可条款请参见 [LICENSE](LICENSE)
"""
}

def append_license(filepath, lang_code):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Skip if already has license section
    if "## License" in content or "## Lizenz" in content or "## Licencia" in content or "## Lisans" in content or "许可证" in content:
        print(f"  [SKIP] {filepath} already has license section")
        return

    if lang_code in LICENSE_TRANSLATIONS:
        license_text = LICENSE_TRANSLATIONS[lang_code]
    else:
        license_text = LICENSE_EN

    with open(filepath, "a", encoding="utf-8") as f:
        f.write(license_text)

    print(f"  [OK] Added license to {os.path.basename(filepath)}")

# Process all README files
files = sorted(glob.glob("README*.md"))
print(f"Processing {len(files)} README files...")

for filepath in files:
    name = os.path.basename(filepath)
    # Extract language code
    if name == "README.md":
        lang = "en"
    else:
        lang = name.replace("README.", "").replace(".md", "")
    
    append_license(filepath, lang)

print(f"\nDone! Processed {len(files)} files.")
