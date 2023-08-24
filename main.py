from PIL import Image, ImageDraw, ImageFont
import os

# Fungsi untuk menambahkan watermark ke gambar
def add_watermark(input_image_path, output_image_path, watermark_text, opacity):
    base = Image.open(input_image_path).convert("RGBA")
    width, height = base.size

    # Membuat gambar untuk watermark
    watermark = Image.new("RGBA", base.size)
    draw = ImageDraw.Draw(watermark)

    # Menggunakan font dan ukuran yang sesuai
    font = ImageFont.truetype("arial.ttf", 36)  # Ganti dengan path font yang sesuai
    text_width, text_height = draw.textsize(watermark_text, font)
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # Menggambar teks watermark dengan opacitas yang ditentukan
    draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, int(255 * opacity)))

    # Menambahkan watermark ke gambar utama
    watermarked = Image.alpha_composite(base, watermark)

    # Simpan gambar yang telah ditambahkan watermark
    watermarked.save(output_image_path, "PNG")

if __name__ == "__main__":
    input_image_path = "images/test.png"  # Ganti dengan path gambar input
    output_image_path = "images/testnew.png"  # Ganti dengan path tempat menyimpan hasil gambar
    watermark_text = "GanggaArtShop.com"
    opacity = 0.5  # Opacity berkisar antara 0 (transparan) hingga 1 (solid)

    add_watermark(input_image_path, output_image_path, watermark_text, opacity)
