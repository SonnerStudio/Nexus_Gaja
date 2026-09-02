import os
import glob
import time
from deep_translator import GoogleTranslator

# 120 previous languages
OLD_LANGS = {
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
    'yi': 'ייִדיש', 'ga': 'Gaeilge', 'ckb': 'کوردی (Sorani)', 'sm': 'Gagana fa\'a Sāmoa', 'tt': 'Татарча'
}

# The remaining 13 languages to reach 133
NEW_13_LANGS = {
    'co': 'Corsu', 'dv': 'ދިވެހި', 'ee': 'Eʋegbe', 'fy': 'Frysk', 'haw': 'ʻŌlelo Hawaiʻi',
    'hmn': 'Hmoob', 'ilo': 'Ilokano', 'kri': 'Krio', 'lb': 'Lëtzebuergesch', 
    'mi': 'Māori', 'lus': 'Mizo', 'gd': 'Gàidhlig', 'ts': 'Xitsonga'
}

# Plus Runes
RUNES = {
    'runes': 'ᚱᚢᚾᛖᛋ (Futhark)'
}

ALL_LANGS = {**OLD_LANGS, **NEW_13_LANGS, **RUNES}

# Generate the new Nav Block
nav_links = []
for code, name in ALL_LANGS.items():
    filename = "README.md" if code == "en" else f"README.{code}.md"
    nav_links.append(f"[{name}]({filename})")

NAV_BLOCK = f"<details>\n<summary>🌍 Available in {len(ALL_LANGS)} Languages (Click to expand)</summary>\n\n"
NAV_BLOCK += " | ".join(nav_links) + "\n\n</details>"

def translate_content(text, target_lang):
    mapping = {'jv': 'jw', 'zh-tw': 'zh-TW', 'mni': 'mni-Mtei'}
    translator_target = mapping.get(target_lang, target_lang)
    translator = GoogleTranslator(source='de', target=translator_target)
    
    paragraphs = text.split('\n\n')
    translated_paragraphs = []
    
    current_chunk = ""
    for p in paragraphs:
        if len(current_chunk) + len(p) > 4000:
            try:
                translated = translator.translate(current_chunk)
                if translated:
                    translated_paragraphs.append(translated)
                else:
                    translated_paragraphs.append(current_chunk)
            except Exception as e:
                err_msg = str(e).encode('ascii', 'replace').decode('ascii')
                print(f"Warning: translation failed for a chunk to {target_lang}, using original text. Error: {err_msg[:100]}")
                translated_paragraphs.append(current_chunk)
            
            time.sleep(1)
            current_chunk = p + "\n\n"
        else:
            current_chunk += p + "\n\n"
            
    if current_chunk.strip():
        try:
            translated = translator.translate(current_chunk)
            if translated:
                translated_paragraphs.append(translated)
            else:
                translated_paragraphs.append(current_chunk)
        except Exception as e:
            err_msg = str(e).encode('ascii', 'replace').decode('ascii')
            print(f"Warning: translation failed for a chunk to {target_lang}, using original text. Error: {err_msg[:100]}")
            translated_paragraphs.append(current_chunk)
        
    return '\n\n'.join(translated_paragraphs)

def update_nav_block(filepath, content):
    import re
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
    with open('README.de.md', 'r', encoding='utf-8') as f:
        base_content = f.read()

    import re
    base_content_no_nav = re.sub(r'<details>.*?<\/details>', '{{NAV_BLOCK}}', base_content, flags=re.DOTALL)

    for code, name in NEW_13_LANGS.items():
        filepath = f"README.{code}.md"
        if os.path.exists(filepath):
            print(f"[SKIP] {filepath} already exists.")
            continue
            
        print(f"Translating to language code: {code}...")
        translated_text = translate_content(base_content_no_nav, code)
        if translated_text:
            final_content = translated_text.replace('{{NAV_BLOCK}}', NAV_BLOCK)
            final_content = final_content.replace('Jan Sonner', 'Jan Friske')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"[OK] Created {filepath}")
        time.sleep(2)

    for filepath in glob.glob('README*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        update_nav_block(filepath, content)
        print(f"[UPDATED NAV] {filepath}")

if __name__ == "__main__":
    main()
