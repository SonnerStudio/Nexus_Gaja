import os
import re
import time
import sys

try:
    from deep_translator import GoogleTranslator
except ImportError:
    os.system(f'{sys.executable} -m pip install deep-translator')
    from deep_translator import GoogleTranslator

langs = {
    'en': 'English', 'de': 'Deutsch', 'tr': 'Türkçe', 'es': 'Español', 'zh-CN': '中文',
    'fr': 'Français', 'it': 'Italiano', 'pt': 'Português', 'nl': 'Nederlands', 'ru': 'Русский',
    'ja': '日本語', 'ko': '한국어', 'ar': 'العربية', 'hi': 'हिन्दी', 'bn': 'বাংলা',
    'pl': 'Polski', 'id': 'Bahasa Indonesia', 'vi': 'Tiếng Việt', 'th': 'ไทย', 'fa': 'فارسی',
    'uk': 'Українська', 'cs': 'Čeština', 'el': 'Ελληνικά', 'hu': 'Magyar', 'sv': 'Svenska',
    'ro': 'Română', 'da': 'Dansk', 'fi': 'Suomi', 'no': 'Norsk', 'sk': 'Slovenčina',
    'hr': 'Hrvatski', 'bg': 'Български', 'sr': 'Српски', 'lt': 'Lietuvių', 'lv': 'Latviešu',
    'et': 'Eesti', 'sl': 'Slovenščina', 'he': 'עברית', 'sw': 'Kiswahili', 'am': 'አማርኛ'
}

# Generate the language bar
lang_links = []
for code, name in langs.items():
    filename = 'README.md' if code == 'en' else (f'README.zh.md' if code == 'zh-CN' else f'README.{code}.md')
    lang_links.append(f"[{name}]({filename})")

lang_bar = "<details>\n<summary>🌍 Available in 40 Languages (Click to expand)</summary>\n\n" + " | ".join(lang_links) + "\n\n</details>"

english_content = """# Nexus Gaja

{LANG_BAR}

**Nexus Gaja** is an intelligent, context-sensitive communication network designed to revolutionize global communication.

## Purpose and Vision
In a globalized world, language is often the biggest barrier. The main goal of Nexus Gaja is to enable seamless, barrier-free, and contextually accurate communication between people—regardless of whether they speak a common language.

It's not just about rigidly translating words, but about **transferring meaning**. Nexus Gaja connects people on a deeper level by understanding cultural, regional, and contextual nuances, thereby enabling genuine, authentic conversations.

## Possibilities and Features
- **Multimedia Communication**: The system processes not just text, but also image, audio, and video. This allows for fully immersive conversations (e.g., video calls or voice messages) in real-time across language barriers.
- **Context Sensitivity**: Recognition of irony, idioms, jargon, and regional dialects that are often misunderstood by conventional translators.
- **Cross-Platform Network**: Serves as a foundation for private chats, forum threads (posts with comments), and global community interactions.

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

## Project Status
The project is currently in the active architecture and planning phase.
Ongoing architectural decisions are documented in the `/docs` folder.
"""

def split_and_translate(text, target_lang):
    if target_lang == 'en':
        return text
    
    chunks = text.split('\n\n')
    translated_chunks = []
    
    t_lang = 'iw' if target_lang == 'he' else target_lang
    translator = GoogleTranslator(source='en', target=t_lang)
    for chunk in chunks:
        if chunk.strip() == '':
            translated_chunks.append('')
            continue
        if chunk.startswith('{LANG_BAR}') or chunk.startswith('`Message`'):
            translated_chunks.append(chunk)
            continue
            
        try:
            res = translator.translate(chunk)
            if res is None:
                translated_chunks.append(chunk)
            else:
                translated_chunks.append(res)
        except Exception as e:
            # Silently fallback to english chunk on error
            translated_chunks.append(chunk)
        
        time.sleep(2) # Increased delay to prevent rate limits and bans
            
    return '\n\n'.join(translated_chunks)

base_dir = 'c:/Dev/Repos/SonnerStudio/Nexus_Gaja'
readme_path = os.path.join(base_dir, 'README.md')

with open(readme_path, 'r', encoding='utf-8') as f:
    english_content = f.read()

# Replace the actual lang bar with {LANG_BAR} so it can be injected correctly
english_content = re.sub(r'<details>.*?<\/details>', '{LANG_BAR}', english_content, count=1, flags=re.DOTALL)

print("Starting translations...")
for code, name in langs.items():
    actual_code = 'zh' if code == 'zh-CN' else code
    filename = 'README.md' if code == 'en' else f'README.{actual_code}.md'
    filepath = os.path.join(base_dir, filename)
    
    # We already have high-quality manual translations for DE, TR, ES, ZH which we update manually
    if code in ['en', 'de', 'tr', 'es', 'zh-CN']:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            # Replace the old language bar line (which starts with 🌍 or 🌐)
            content = re.sub(r'<details>.*?<\/details>', lang_bar, content, count=1, flags=re.DOTALL)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        continue
    
    if os.path.exists(filepath):
        print(f"Skipping {code}, already exists.")
        continue
    
    print(f"Translating to {code}...")
    translated = split_and_translate(english_content, code)
    # Inject the lang bar
    translated = translated.replace('{LANG_BAR}', lang_bar)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(translated)
        
    time.sleep(1)

print("Done translating.")
