import os
from PIL import Image, ImageDraw, ImageFont

for i in range(384, 434):
    namaFile = f'IMG_3{i}'
    file_path = f'images-landscape/{namaFile}.JPG'
    
    if os.path.exists(file_path):
        image = Image.open(file_path).convert("RGBA")
        
        width, height = image.size
        
        txt = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        
        font = ImageFont.truetype("poppins.ttf", 200)
        d = ImageDraw.Draw(txt)    
        text = "ganggaartshop.com"
        
        textwidth, textheight = d.textsize(text, font=font)
        
        x = (width - textwidth) // 2
        y = (height - textheight) // 2
        
        d.text((x, y), "ganggaartshop.com", fill=(0, 0, 0, 95), font=font)
        
        combined = Image.alpha_composite(image, txt)
        combined.save(f'output-landscape/{namaFile}.png')
    else:
        print(f"File '{file_path}' tidak ditemukan.")
