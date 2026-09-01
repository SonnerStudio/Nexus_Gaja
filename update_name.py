import glob

replacements = {
    "Jan Sonner / SonnerStudio": "SonnerStudio - Jan Friske Gründer, Inhaber, Direktor und Chefdesigner von SonnerStudio",
    "Jan Sonner": "Jan Friske",
    "ጃን ሶነር": "ጃን ፍሪስኬ",
    "جان سونر": "جان فريسكي",
    "Ян Сонер": "Ян Фриске",
    "ג'אן זונר": "ג'אן פריסקה",
    "Ян Соннер": "Ян Фріске"
}

files = glob.glob('README*.md') + ['LICENSE']

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
