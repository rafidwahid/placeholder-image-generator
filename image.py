from PIL import Image, ImageDraw, ImageFont

font_path = "arial.ttf"
font_size = 100

for i in range(1, 11):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    text = str(i)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (img.width - text_width) / 2
    text_y = (img.height - text_height) / 2
    draw.text((text_x, text_y), text, fill='black', font=font)
    img.save(f'image_{i}.webp', format='WEBP')

print("Images created successfully.")
