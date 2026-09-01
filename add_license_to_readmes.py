"""
Replaces the English license section in all README files (except DE, ES, TR, ZH, EN)
with a properly translated version in the respective language.
"""

import os
import glob
import time
from deep_translator import GoogleTranslator

# Languages with already-correct native translations - skip these
SKIP_LANGS = {"en", "de", "es", "tr", "zh"}

# The English license template to translate
LICENSE_EN_TEMPLATE = """---

## License & Intellectual Property

> **© 2024–2026 Jan Sonner / SonnerStudio — All rights reserved.**

**Nexus Gaja** is the exclusive intellectual property of **Jan Sonner**, operating under **SonnerStudio**.

Jan Sonner is the sole creator, architect, and owner of Nexus Gaja — including all concepts, architecture, domain models, brand identity, and associated documentation.

**No rights, licenses, or ownership interests are held by any third party**, regardless of their size, market position, or influence in the technology industry.

### What is NOT permitted without explicit written consent:
- Copying, reproducing, or distributing this software or its documentation
- Modifying, adapting, or creating derivative works
- Commercial use of any part of Nexus Gaja
- Using the contents of this repository as training data for AI or LLM systems
- Sublicensing or transferring any rights to third parties

### Protected Intellectual Property
The following original concepts are protected as trade secrets and proprietary creations of Jan Sonner:
- The layered communication model (Original, Semantic Interpretation, Translated Output)
- The identity separation principle (Person is not Account is not Identity Verification)
- The Message-Translation decoupling model (Message is not Translation)
- The AI moderation governance framework

### Contact
For licensing inquiries: https://github.com/SonnerStudio

Nexus Gaja and the Nexus Gaja logo are trademarks of Jan Sonner. Unauthorized use of the name or brand is prohibited.

See full license terms in the LICENSE file."""

# The marker that identifies the start of the English license section
LICENSE_MARKER = "\n---\n\n## License"

def translate_text(text, target_lang):
    """Translate text using Google Translate via deep-translator."""
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        # Split into chunks of max 4000 chars to avoid API limits
        chunks = []
        lines = text.split('\n')
        current_chunk = []
        current_len = 0
        
        for line in lines:
            if current_len + len(line) > 3500:
                chunks.append('\n'.join(current_chunk))
                current_chunk = [line]
                current_len = len(line)
            else:
                current_chunk.append(line)
                current_len += len(line) + 1
        
        if current_chunk:
            chunks.append('\n'.join(current_chunk))
        
        translated_chunks = []
        for chunk in chunks:
            if chunk.strip():
                t = translator.translate(chunk)
                translated_chunks.append(t)
                time.sleep(0.5)  # Rate limiting
            else:
                translated_chunks.append(chunk)
        
        return '\n'.join(translated_chunks)
    except Exception as e:
        print(f"    [ERROR] Translation failed: {e}")
        return None

def remove_english_license(content):
    """Remove the English license section from README content."""
    idx = content.find(LICENSE_MARKER)
    if idx == -1:
        # Try alternate marker
        idx = content.find("\n---\n\n## License & Intellectual Property")
    if idx == -1:
        return content, False
    return content[:idx], True

def process_readme(filepath, lang_code):
    """Translate and replace the license section for a given README."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Remove existing English license section
    new_content, found = remove_english_license(content)
    if not found:
        print(f"  [WARN] No license section found in {os.path.basename(filepath)}")
        new_content = content

    print(f"  [TRANSLATING] {os.path.basename(filepath)} ({lang_code})...")
    translated = translate_text(LICENSE_EN_TEMPLATE, lang_code)
    
    if translated is None:
        print(f"  [SKIP] Could not translate for {lang_code}, keeping English")
        return False
    
    # Append translated license
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        f.write("\n\n---\n\n")
        f.write(translated)
        f.write("\n")
    
    print(f"  [OK] {os.path.basename(filepath)} updated with {lang_code} license")
    return True

# Process all README files
files = sorted(glob.glob("README*.md"))
to_process = []

for filepath in files:
    name = os.path.basename(filepath)
    if name == "README.md":
        lang = "en"
    else:
        lang = name.replace("README.", "").replace(".md", "")
    
    if lang not in SKIP_LANGS:
        to_process.append((filepath, lang))

print(f"Processing {len(to_process)} README files (skipping EN, DE, ES, TR, ZH)...\n")

success = 0
for filepath, lang in to_process:
    ok = process_readme(filepath, lang)
    if ok:
        success += 1
    time.sleep(1)  # Rate limiting between files

print(f"\nDone! Successfully translated {success}/{len(to_process)} files.")
