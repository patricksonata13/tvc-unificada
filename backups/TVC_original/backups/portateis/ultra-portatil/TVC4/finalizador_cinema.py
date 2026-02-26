import os
import subprocess

def aplicar_filtro_tvc(arquivo_entrada):
    nome, ext = os.path.splitext(arquivo_entrada)
    arquivo_saida = f"{nome}_FINAL{ext}"
    
    print(f"🎬 Aplicando Filtro Cinema TVC 4.0 em: 
{arquivo_entrada}")
    
    # Filtro: Contraste alto, dessaturação leve e 
vinheta nas bordas
    filtro = "eq=contrast=1.1:saturation=0.85, 
vignette=pi/4"
    
    comando = [
        "ffmpeg", "-y", "-i", arquivo_entrada,
        "-vf", filtro, "-c:v", "libx264", "-crf", "18", 
"-c:a", "copy",
        arquivo_saida
    ]
    
    subprocess.run(comando)
    print(f"✅ Vídeo finalizado com look de cinema: 
{arquivo_saida}")

if __name__ == "__main__":
    # Testando com o capítulo da novela
    video = 
os.path.expanduser("~/TVC4/Assets/Novelas/cap05.mp4")
    if os.path.exists(video):
        aplicar_filtro_tvc(video)
