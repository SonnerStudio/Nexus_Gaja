import os
import glob
import shutil
import re

# Base 133 Languages + Runes
BASE_LANGS = {
    'en': 'English', 'de': 'Deutsch', 'tr': 'Türkçe', 'es': 'Español', 'zh': '中文', 
    'fr': 'Français', 'it': 'Italiano', 'pt': 'Português', 'nl': 'Nederlands', 'ru': 'Русский', 
    'ja': '日本語', 'ko': '한국어', 'ar': 'العربية', 'hi': 'हिन्दी', 'bn': 'বাংলা', 
    'pl': 'Polski', 'id': 'Bahasa Indonesia', 'vi': 'Tiếng Việt', 'th': 'ไทย', 'fa': 'فارسی', 
    'uk': 'Українська', 'cs': 'Čeština', 'el': 'Ελληνικά', 'hu': 'Magyar', 'sv': 'Svenska', 
    'ro': 'Română', 'da': 'Dansk', 'fi': 'Suomi', 'no': 'Norsk', 'sk': 'Slovenčina', 
    'hr': 'Hrvatski', 'bg': 'Български', 'sr': 'Српски', 'lt': 'Lietuvių', 'lv': 'Latviešu', 
    'et': 'Eesti', 'sl': 'Slovenščina', 'he': 'עברית', 'sw': 'Kiswahili', 'am': 'አማርኛ',
    'ur': 'اردو', 'mr': 'मराठी', 'te': 'తెలుగు', 'ta': 'தமிழ்', 'gu': 'ગુજરાતી',
    'kn': 'ಕನ್ನಡ', 'ml': 'മലയാളം', 'pa': 'ਪੰਜਾਬੀ', 'jv': 'Basa Jawa', 'ms': 'Bahasa Melayu',
    'tl': 'Tagalog', 'uz': 'Oʻzbekcha', 'kk': 'Қазақша', 'az': 'Azərbaycanca', 'ka': 'ქართული',
    'hy': 'Հայերեն', 'km': 'ភាសាខ្មែរ', 'si': 'සිංහල', 'ne': 'नेपाली', 'zu': 'isiZulu',
    'af': 'Afrikaans', 'sq': 'Shqip', 'mk': 'Македонски', 'is': 'Íslenska', 'cy': 'Cymraeg',
    'eu': 'Euskara', 'gl': 'Galego', 'mt': 'Malti', 'be': 'Беларуская', 'mn': 'Монгол',
    'so': 'Soomaali', 'ha': 'Hausa', 'yo': 'Yorùbá', 'ig': 'Igbo', 'xh': 'isiXhosa',
    'su': 'Basa Sunda', 'mg': 'Malagasy', 'rw': 'Ikinyarwanda', 'ny': 'Chichewa', 'sn': 'chiShona',
    'ku': 'Kurdî', 'ps': 'پښتو', 'sd': 'سنڌي', 'or': 'ଓଡ଼ିଆ', 'as': 'অসমীয়া',
    'bs': 'Bosanski', 'lo': 'ລາວ', 'my': 'မြန်မာ', 'tg': 'Тоҷикӣ', 'tk': 'Türkmençe',
    'zh-tw': '繁體中文', 'ca': 'Català', 'ceb': 'Bisaya', 'ky': 'Кыргызча', 'ug': 'ئۇيغۇرچە',
    'om': 'Afaan Oromoo', 'ln': 'Lingála', 'lg': 'Luganda', 'ak': 'Twi', 'st': 'Sesotho',
    'nso': 'Sesotho sa Leboa', 'ti': 'ትግርኛ', 'bm': 'Bamanankan', 'bho': 'भोजपुरी', 'mai': 'मैथिली',
    'doi': 'डोगरी', 'sa': 'संस्कृतम्', 'gom': 'कोंकणी', 'mni': 'মৈতৈলোন্', 'qu': 'Runa Simi',
    'gn': 'Avañe\'ẽ', 'ay': 'Aymar aru', 'ht': 'Kreyòl Ayisyen', 'eo': 'Esperanto', 'la': 'Latina',
    'yi': 'ייִדיש', 'ga': 'Gaeilge', 'ckb': 'کوردی (Sorani)', 'sm': 'Gagana fa\'a Sāmoa', 'tt': 'Татарча',
    'co': 'Corsu', 'dv': 'ދިވެހި', 'ee': 'Eʋegbe', 'fy': 'Frysk', 'haw': 'ʻŌlelo Hawaiʻi',
    'hmn': 'Hmoob', 'ilo': 'Ilokano', 'kri': 'Krio', 'lb': 'Lëtzebuergesch', 
    'mi': 'Māori', 'lus': 'Mizo', 'gd': 'Gàidhlig', 'ts': 'Xitsonga',
    'runes': 'ᚱᚢᚾᛖᛋ (Futhark)'
}

# 64 National Variants mapped to their Base Language Code
# Format: 'alias_code': ('base_code', 'Alias Display Name')
NATIONAL_VARIANTS = {
    # Spanish Variants
    'es-AR': ('es', 'Español (Argentina)'), 'es-BO': ('es', 'Español (Bolivia)'),
    'es-CL': ('es', 'Español (Chile)'), 'es-CO': ('es', 'Español (Colombia)'),
    'es-CR': ('es', 'Español (Costa Rica)'), 'es-CU': ('es', 'Español (Cuba)'),
    'es-DO': ('es', 'Español (República Dominicana)'), 'es-EC': ('es', 'Español (Ecuador)'),
    'es-SV': ('es', 'Español (El Salvador)'), 'es-GT': ('es', 'Español (Guatemala)'),
    'es-HN': ('es', 'Español (Honduras)'), 'es-MX': ('es', 'Español (México)'),
    'es-NI': ('es', 'Español (Nicaragua)'), 'es-PA': ('es', 'Español (Panamá)'),
    'es-PY': ('es', 'Español (Paraguay)'), 'es-PE': ('es', 'Español (Perú)'),
    'es-PR': ('es', 'Español (Puerto Rico)'), 'es-UY': ('es', 'Español (Uruguay)'),
    'es-VE': ('es', 'Español (Venezuela)'), 'es-GQ': ('es', 'Español (Guinea Ecuatorial)'),
    
    # English Variants
    'en-AU': ('en', 'English (Australia)'), 'en-CA': ('en', 'English (Canada)'),
    'en-IN': ('en', 'English (India)'), 'en-IE': ('en', 'English (Ireland)'),
    'en-JM': ('en', 'English (Jamaica)'), 'en-NZ': ('en', 'English (New Zealand)'),
    'en-ZA': ('en', 'English (South Africa)'), 'en-GB': ('en', 'English (UK)'),
    'en-US': ('en', 'English (USA)'), 'en-BZ': ('en', 'English (Belize)'),
    'en-NG': ('en', 'English (Nigeria)'), 'en-KE': ('en', 'English (Kenya)'),
    'en-SG': ('en', 'English (Singapore)'), 'en-PH': ('en', 'English (Philippines)'),
    
    # French Variants
    'fr-CA': ('fr', 'Français (Canada)'), 'fr-BE': ('fr', 'Français (Belgique)'),
    'fr-CH': ('fr', 'Français (Suisse)'), 'fr-SN': ('fr', 'Français (Sénégal)'),
    'fr-CI': ('fr', 'Français (Côte d\'Ivoire)'), 'fr-CM': ('fr', 'Français (Cameroun)'),
    'fr-ML': ('fr', 'Français (Mali)'), 'fr-CD': ('fr', 'Français (RDC)'),
    'fr-MG': ('fr', 'Français (Madagascar)'), 'fr-HT': ('fr', 'Français (Haïti)'),
    
    # Portuguese Variants
    'pt-BR': ('pt', 'Português (Brasil)'), 'pt-AO': ('pt', 'Português (Angola)'),
    'pt-MZ': ('pt', 'Português (Moçambique)'), 'pt-CV': ('pt', 'Português (Cabo Verde)'),
    
    # German Variants
    'de-AT': ('de', 'Deutsch (Österreich)'), 'de-CH': ('de', 'Deutsch (Schweiz)'),
    'de-LI': ('de', 'Deutsch (Liechtenstein)'), 'de-LU': ('de', 'Deutsch (Luxemburg)'),
    
    # Dutch Variants
    'nl-BE': ('nl', 'Nederlands (België)'), 'nl-SR': ('nl', 'Nederlands (Suriname)'),
    
    # Arabic Variants
    'ar-EG': ('ar', 'العربية (مصر)'), 'ar-SA': ('ar', 'العربية (السعودية)'),
    'ar-AE': ('ar', 'العربية (الإمارات)'), 'ar-MA': ('ar', 'العربية (المغرب)'),
    'ar-DZ': ('ar', 'العربية (الجزائر)'), 'ar-IQ': ('ar', 'العربية (العراق)'),
    'ar-SY': ('ar', 'العربية (سوريا)'), 'ar-LB': ('ar', 'العربية (لبنان)'),
    'ar-JO': ('ar', 'العربية (الأردن)'), 'ar-YE': ('ar', 'العربية (اليمن)'),
    
    # Chinese Variants
    'zh-SG': ('zh', '中文 (新加坡)'), 'zh-HK': ('zh-tw', '繁體中文 (香港)'),
    'zh-MO': ('zh-tw', '繁體中文 (澳門)')
}

# Create a combined dict of ALL languages and aliases
ALL_LANGS_DISPLAY = {**BASE_LANGS}
for alias, (base, display) in NATIONAL_VARIANTS.items():
    ALL_LANGS_DISPLAY[alias] = display

# Generate the massive Nav Block (approx. 198 total languages/regions)
nav_links = []
# Sort the dictionary so it looks organized (optional, but let's keep original order)
for code, name in ALL_LANGS_DISPLAY.items():
    filename = "README.md" if code == "en" else f"README.{code}.md"
    nav_links.append(f"[{name}]({filename})")

NAV_BLOCK = f"<details>\n<summary>🌍 Available in {len(ALL_LANGS_DISPLAY)} Languages & Regions (Click to expand)</summary>\n\n"
NAV_BLOCK += " | ".join(nav_links) + "\n\n</details>"


def update_nav_block(filepath, content):
    new_content = content.replace('{{NAV_BLOCK}}', NAV_BLOCK)
    new_content = re.sub(r'<details>.*?<\/details>', NAV_BLOCK, new_content, flags=re.DOTALL)
    if new_content == content:
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'nexus_hero.jpg' in line:
                lines.insert(i + 2, NAV_BLOCK)
                new_content = '\n'.join(lines)
                break
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)


def main():
    # 1. Create all alias files
    for alias_code, (base_code, _) in NATIONAL_VARIANTS.items():
        base_file = "README.md" if base_code == "en" else f"README.{base_code}.md"
        alias_file = f"README.{alias_code}.md"
        
        if not os.path.exists(base_file):
            print(f"[ERROR] Base file {base_file} missing for {alias_code}.")
            continue
            
        shutil.copyfile(base_file, alias_file)
        print(f"[OK] Created Alias: {alias_file} (from {base_file})")

    # 2. Update NAV_BLOCK in all README files
    print("\nUpdating Navigation Blocks in all files...")
    all_readmes = glob.glob('README*.md')
    for filepath in all_readmes:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        update_nav_block(filepath, content)
        print(f"[UPDATED NAV] {filepath}")

if __name__ == "__main__":
    main()
