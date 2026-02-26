import requests
from PIL import Image, ImageDraw, ImageFont
import os

def buscar_clima():
    # Coordenadas do Rio de Janeiro
    url = 
"https://api.open-meteo.com/v1/forecast?latitude=-22.9064&longitude=-43.1822&current_weather=true"
    response = requests.get(url).json()
    temp = response['current_weather']['temperature']
    vel_vento = response['current_weather']['windspeed']
    return f"{temp}°C", f"{vel_vento} km/h"

def gerar_card_clima():
    temp, vento = buscar_clima()
    
    # Criar fundo transparente/clean
    img = Image.new('RGBA', (400, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Desenhar retângulo cinza elegante (transparência 80%)
    draw.rounded_rectangle([10, 10, 390, 190], radius=20, fill=(240, 240, 
240, 220))
    
    # Texto (Em tons de cinza escuro)
    draw.text((30, 30), "RIO DE JANEIRO", fill=(100, 100, 100))
    draw.text((30, 60), temp, fill=(50, 50, 50), font_size=60)
    draw.text((30, 140), f"Ventos: {vento}", fill=(120, 120, 120))
    
    img.save(os.path.expanduser("~/TVC4/Assets/clima_hoje.png"))
    print(f"🌡️ Clima atualizado: {temp}")

if __name__ == "__main__":
    gerar_card_clima()
