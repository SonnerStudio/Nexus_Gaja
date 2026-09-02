import os
import glob
import time
from deep_translator import GoogleTranslator

# 40 Existing languages + 30 New languages
EXISTING_LANGS = {
    'en': 'English', 'de': 'Deutsch', 'tr': 'Türkçe', 'es': 'Español', 'zh': '中文', 
    'fr': 'Français', 'it': 'Italiano', 'pt': 'Português', 'nl': 'Nederlands', 'ru': 'Русский', 
    'ja': '日本語', 'ko': '한국어', 'ar': 'العربية', 'hi': 'हिन्दी', 'bn': 'বাংলা', 
    'pl': 'Polski', 'id': 'Bahasa Indonesia', 'vi': 'Tiếng Việt', 'th': 'ไทย', 'fa': 'فارسی', 
    'uk': 'Українська', 'cs': 'Čeština', 'el': 'Ελληνικά', 'hu': 'Magyar', 'sv': 'Svenska', 
    'ro': 'Română', 'da': 'Dansk', 'fi': 'Suomi', 'no': 'Norsk', 'sk': 'Slovenčina', 
    'hr': 'Hrvatski', 'bg': 'Български', 'sr': 'Српски', 'lt': 'Lietuvių', 'lv': 'Latviešu', 
    'et': 'Eesti', 'sl': 'Slovenščina', 'he': 'עברית', 'sw': 'Kiswahili', 'am': 'አማርኛ'
}

NEW_LANGS = {
    'ur': 'اردو', 'mr': 'मराठी', 'te': 'తెలుగు', 'ta': 'தமிழ்', 'gu': 'ગુજરાતી',
    'kn': 'ಕನ್ನಡ', 'ml': 'മലയാളം', 'pa': 'ਪੰਜਾਬੀ', 'jv': 'Basa Jawa', 'ms': 'Bahasa Melayu',
    'tl': 'Tagalog', 'uz': 'Oʻzbekcha', 'kk': 'Қазақша', 'az': 'Azərbaycanca', 'ka': 'ქართული',
    'hy': 'Հայերեն', 'km': 'ភាសាខ្មែរ', 'si': 'සිංහල', 'ne': 'नेपाली', 'zu': 'isiZulu',
    'af': 'Afrikaans', 'sq': 'Shqip', 'mk': 'Македонски', 'is': 'Íslenska', 'cy': 'Cymraeg',
    'eu': 'Euskara', 'gl': 'Galego', 'mt': 'Malti', 'be': 'Беларуская', 'mn': 'Монгол'
}

ALL_LANGS = {**EXISTING_LANGS, **NEW_LANGS}

# Generate the new Nav Block
nav_links = []
for code, name in ALL_LANGS.items():
    filename = "README.md" if code == "en" else f"README.{code}.md"
    nav_links.append(f"[{name}]({filename})")

NAV_BLOCK = "<details>\n<summary>🌍 Available in 70 Languages (Click to expand)</summary>\n\n"
NAV_BLOCK += " | ".join(nav_links) + "\n\n</details>"

def translate_content(text, target_lang):
    # Google Translate expects 'jw' for Javanese instead of 'jv'
    translator_target = 'jw' if target_lang == 'jv' else target_lang
    translator = GoogleTranslator(source='de', target=translator_target)
    
    # Split text into manageable chunks (split by double newline to keep markdown blocks intact)
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
            
            time.sleep(1) # Rate limiting
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
    # Find the existing <details>...</details> block and replace it
    new_content = re.sub(r'<details>.*?<\/details>', NAV_BLOCK, content, flags=re.DOTALL)
    if new_content == content:
        # If not found, insert after Hero Image
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
    # Remove the existing Nav Block from base_content before translating
    base_content_no_nav = re.sub(r'<details>.*?<\/details>', '{{NAV_BLOCK}}', base_content, flags=re.DOTALL)

    # 1. Translate and create new READMEs
    for code, name in NEW_LANGS.items():
        filepath = f"README.{code}.md"
        if os.path.exists(filepath):
            print(f"[SKIP] {filepath} already exists.")
            continue
            
        print(f"Translating to language code: {code}...")
        translated_text = translate_content(base_content_no_nav, code)
        if translated_text:
            # Replace placeholder with the new Nav Block
            final_content = translated_text.replace('{{NAV_BLOCK}}', NAV_BLOCK)
            
            # Post-translation name fixes just in case
            final_content = final_content.replace('Jan Sonner', 'Jan Friske')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(final_content)
            print(f"[OK] Created {filepath}")
        time.sleep(2)

    # 2. Update Nav Block in all existing files
    for filepath in glob.glob('README*.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        update_nav_block(filepath, content)
        print(f"[UPDATED NAV] {filepath}")

if __name__ == "__main__":
    main()
