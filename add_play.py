from PIL import Image, ImageDraw
import sys

def add_play_button(image_path, output_path):
    img = Image.open(image_path)
    
    # Resize image to width 360
    wpercent = (360 / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((360, hsize), Image.Resampling.LANCZOS)
    
    # Create an overlay for the play button
    overlay = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Center coordinates
    x, y = 360 // 2, hsize // 2
    r = 40
    
    # Draw semi-transparent dark circle
    draw.ellipse((x - r, y - r, x + r, y + r), fill=(0, 0, 0, 150))
    
    # Draw white triangle
    # Points of the triangle
    p1 = (x - 12, y - 20)
    p2 = (x - 12, y + 20)
    p3 = (x + 20, y)
    draw.polygon([p1, p2, p3], fill=(255, 255, 255, 255))
    
    # Composite the overlay onto the original image
    img = img.convert("RGBA")
    out = Image.alpha_composite(img, overlay)
    
    out.convert("RGB").save(output_path, quality=90)
    print(f"Processed {output_path}")

add_play_button('C:\\Dev\\Repos\\SonnerStudio\\Nexus_Gaja\\assets\\video\\Nexus_Gaja_TikTok_thumb.jpg', 'C:\\Dev\\Repos\\SonnerStudio\\Nexus_Gaja\\assets\\video\\Nexus_Gaja_TikTok_thumb.jpg')
add_play_button('C:\\Dev\\Repos\\SonnerStudio\\Nexus_Gaja\\assets\\video\\Nexus_Gaja_TikTok_EN_thumb.jpg', 'C:\\Dev\\Repos\\SonnerStudio\\Nexus_Gaja\\assets\\video\\Nexus_Gaja_TikTok_EN_thumb.jpg')
