from PIL import Image, ImageDraw
import os
def gerar():
    path = os.path.expanduser("~/TVC4/Assets/logo_tvc_transparente.png")
    img = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([50, 50, 450, 450], fill=(100, 100, 100, 255))
    draw.text((150, 220), "TVC 4.0", fill=(255, 255, 255))
    img.save(path)
    print("🎨 Logo gerada em Assets!")
if __name__ == "__main__":
    gerar()
