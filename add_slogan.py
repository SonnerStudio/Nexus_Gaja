import os
import glob
import time
from deep_translator import GoogleTranslator

# The slogans in the main languages
SLOGANS = {
    "de": "> *Für Völkerfrieden und Völkerverständigung*",
    "en": "> *For global peace and mutual understanding*",
    "es": "> *Por la paz global y el entendimiento mutuo*",
    "zh": "> *致力于全球和平与相互理解*",
    "tr": "> *Küresel barış ve karşılıklı anlayış için*"
}

def translate_slogan(target_lang):
    if target_lang in SLOGANS:
        return SLOGANS[target_lang]
    
    try:
        translator = GoogleTranslator(source='en', target=target_lang)
        translated = translator.translate("For global peace and mutual understanding")
        time.sleep(0.5)
        return f"> *{translated}*"
    except Exception as e:
        print(f"Error translating for {target_lang}: {e}")
        return None

def inject_slogan(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already injected
    if "> *" in content.split('\n')[2:5]: # Checking the first few lines
        print(f"[SKIP] {filepath} already has a slogan")
        return

    slogan = translate_slogan(lang)
    if not slogan:
        return

    # Find the title line
    lines = content.split('\n')
    if lines[0].startswith("# Nexus Gaja"):
        # Insert slogan after the title
        lines.insert(1, "")
        lines.insert(2, slogan)
        lines.insert(3, "")
        
        # Also let's place it nicely before the Logo if we want, or after.
        # Above logo looks better:
        # # Nexus Gaja
        #
        # > *Slogan*
        #
        # ![Logo]...
        
        new_content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] {filepath} updated with slogan: {slogan}")

files = glob.glob("README*.md")
print(f"Processing {len(files)} README files...")

for filepath in files:
    name = os.path.basename(filepath)
    if name == "README.md":
        lang = "en"
    else:
        lang = name.replace("README.", "").replace(".md", "")
        
    inject_slogan(filepath, lang)

print("Done!")
