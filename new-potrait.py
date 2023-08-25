import os
from PIL import Image, ImageDraw, ImageFont

for i in range(416, 452):
    namaFile = f'IMG_3{i}'
    file_path = f'new-images-potrait/{namaFile}.JPG'
    
    if os.path.exists(file_path):
        image = Image.open(file_path).convert("RGBA")
        imagerotate = image.rotate(-90, expand=True)
        
        width, height = image.size
        
        txt = Image.new('RGBA', (height, width), (255, 255, 255, 0))
        
        font = ImageFont.truetype("poppins.ttf", 200)
        d = ImageDraw.Draw(txt)    
        text = "ganggaartshop.com"
        
        textwidth, textheight = d.textsize(text, font=font)
        
        x = (height - textwidth) // 2
        y = (width - textheight) // 2
        
        d.text((x, y), "ganggaartshop.com", fill=(0, 0, 0, 95), font=font)
        
        combined = Image.alpha_composite(imagerotate, txt)
        combined.save(f'new-potrait/{namaFile}.png')
    else:
        print(f"File '{file_path}' tidak ditemukan.")
