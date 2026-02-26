from PIL import Image, ImageDraw, ImageFont

def criar_background_tvc():
    # Definições de cores (Clean: Cinza e Branco)
    cor_fundo = (240, 240, 240) # Cinza muito claro
    cor_detalhe = (200, 200, 200) # Cinza médio
    largura, altura = 1280, 720

    # Criar imagem base
    img = Image.new('RGB', (largura, altura), color=cor_fundo)
    draw = ImageDraw.Draw(img)

    # Desenhar formas geométricas minimalistas (Estilo TV Moderna)
    draw.rectangle([0, 600, 1280, 720], fill=(255, 255, 255)) # Barra 
branca inferior
    draw.line([0, 600, 1280, 600], fill=cor_detalhe, width=2) # Linha 
divisória

    # Simular silhueta do Rio (Pão de Açúcar simplificado)
    draw.polygon([(100, 600), (300, 300), (500, 600)], fill=(230, 230, 
230))
    draw.polygon([(400, 600), (600, 400), (800, 600)], fill=(235, 235, 
235))

    # Adicionar o selo da TVC 4.0
    try:
        # Tenta desenhar um texto se não houver logo em PNG
        draw.text((1100, 50), "TVC 4.0", fill=(100, 100, 100))
        draw.text((50, 630), "FONTE: DIZ QUE | NEWS RIO", fill=(150, 150, 
150))
    except:
        pass

    img.save(os.path.expanduser("~/TVC4/Assets/cenario_clean.png"))
    print("✅ Cenário 'Rio Clean' gerado com sucesso em Assets!")

import os
if __name__ == "__main__":
    criar_background_tvc()
