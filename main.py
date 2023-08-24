from PIL import Image, ImageDraw, ImageFont

img = Image.open('images/test.png')
width, height = img.size

draw = ImageDraw.Draw(img)
text = "PySeek"

font = ImageFont.truetype('poppins.ttf', 80)

textwidth, textheight = draw.textsize(text, font=font)

x = (width - textwidth) // 2
y = (height - textheight) // 2

draw.text((x, y), text, font=font, fill=(0, 0, 0, 50))  

img.save('images/watermarked.png') 

img = Image.open('images/watermarked.png')
img.show()
