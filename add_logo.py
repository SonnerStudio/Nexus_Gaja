import os
import shutil
import glob

# 1. Create assets dir and copy logo
assets_dir = 'c:/Dev/Repos/SonnerStudio/Nexus_Gaja/assets'
os.makedirs(assets_dir, exist_ok=True)
src_logo = r'C:\Users\hbcom\.gemini\antigravity-ide\brain\6a1af385-263c-41af-b957-e97b52c4f087\nexus_gaja_logo_1788189296097.jpg'
dst_logo = os.path.join(assets_dir, 'logo.jpg')
shutil.copy2(src_logo, dst_logo)

# 2. Update all READMEs
repo_dir = 'c:/Dev/Repos/SonnerStudio/Nexus_Gaja'
readmes = glob.glob(os.path.join(repo_dir, 'README*.md'))

img_markdown = '![Nexus Gaja Logo](assets/logo.jpg)\n'

for readme in readmes:
    with open(readme, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '![Nexus Gaja Logo]' not in content:
        content = content.replace('# Nexus Gaja\n', '# Nexus Gaja\n\n' + img_markdown, 1)
        with open(readme, 'w', encoding='utf-8') as f:
            f.write(content)

print("Added logo to all readmes")
