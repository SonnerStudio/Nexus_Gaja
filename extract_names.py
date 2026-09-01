import glob
import re
import codecs

# We want to replace all occurrences of "Jan Sonner" and its translations
# with "Jan Friske" (and appropriate translations if possible, or just "Jan Friske")
# AND replace "© 2024–2026 Jan Sonner / SonnerStudio" with "© 2024–2026 SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio"

with codecs.open('replacements.log', 'w', encoding='utf-8') as out:
    for filepath in glob.glob('README*.md'):
        with codecs.open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find the copyright line
        m = re.search(r'2024.2026 (.*?) / SonnerStudio', content)
        if m:
            name = m.group(1)
            out.write(f"{filepath}: {name}\n")
