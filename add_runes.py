import os
import glob
import re

# Rune mapping for basic Latin characters (27 Runes context)
# Includes Elder Futhark + a few extras for ä, ö, ü and punctuation.
RUNE_MAP = {
    'a': 'ᚨ', 'b': 'ᛒ', 'c': 'ᚳ', 'd': 'ᛞ', 'e': 'ᛖ', 'f': 'ᚠ', 'g': 'ᚷ',
    'h': 'ᚻ', 'i': 'ᛁ', 'j': 'ᛃ', 'k': 'ᚲ', 'l': 'ᛚ', 'm': 'ᛗ', 'n': 'ᚾ',
    'o': 'ᛟ', 'p': 'ᛈ', 'q': 'ᛢ', 'r': 'ᚱ', 's': 'ᛊ', 't': 'ᛏ', 'u': 'ᚢ',
    'v': 'ᚡ', 'w': 'ᚹ', 'x': 'ᛉ', 'y': 'ᛦ', 'z': 'ᛉ',
    'ä': 'ᛅ', 'ö': 'ᚯ', 'ü': 'ᚣ', 'ß': 'ᛊᛊ'
}

def transliterate_to_runes(text):
    # We want to transliterate text, but NOT markdown formatting or links.
    # We can do this roughly by transliterating everything that's not inside brackets or backticks,
    # or just transliterate only alphabetic characters.
    
    # Simpler approach: Transliterate word by word, skipping HTML tags and markdown
    # A robust way is to split by parts that shouldn't be touched.
    # We will ignore <...>, [...](...), `...`, and image links.
    
    pattern = r'(<[^>]+>|\[[^\]]+\]\([^\)]+\)|`[^`]+`|\!\[[^\]]+\]\([^\)]+\))'
    parts = re.split(pattern, text)
    
    result = []
    for part in parts:
        if re.match(pattern, part):
            result.append(part)
        else:
            # Transliterate this part
            transliterated = ""
            for char in part:
                lower_char = char.lower()
                if lower_char in RUNE_MAP:
                    transliterated += RUNE_MAP[lower_char]
                else:
                    transliterated += char
            result.append(transliterated)
    
    return "".join(result)

def main():
    with open('README.de.md', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract NAV_BLOCK roughly
    nav_match = re.search(r'<details>.*?<\/details>', content, flags=re.DOTALL)
    if nav_match:
        nav_block = nav_match.group(0)
        content_no_nav = content.replace(nav_block, '{{NAV_BLOCK}}')
    else:
        content_no_nav = content
        
    runes_content = transliterate_to_runes(content_no_nav)
    
    # Write to README.runes.md
    with open('README.runes.md', 'w', encoding='utf-8') as f:
        # We don't restore nav block here yet, because the main script updates all readmes anyway.
        # Just write the placeholder or keep it out. The update_nav_block in the main script will fix it.
        # But wait, add_remaining_langs.py handles the update_nav_block.
        # Let's put {{NAV_BLOCK}} in and let the other script replace it, or replace it here if we know it.
        f.write(runes_content)
        
    print("[OK] Created README.runes.md")

if __name__ == "__main__":
    main()
