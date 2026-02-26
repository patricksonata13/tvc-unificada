import os
import subprocess

def montar_plantao(texto_noticia):
    # Caminhos dos arquivos
    base = os.path.expanduser("~/TVC4/Assets")
    cenario = os.path.join(base, "cenario_clean.png")
    audio = "audio_plantao.mp3"
    video_final = "ESTREIA_TVC4.mp4"

    print(f"🎬 Iniciando renderização da TVC 4.0...")
    
    # Comando Mestre do FFmpeg:
    # 1. Pega a imagem estática e transforma em vídeo de 5 segundos
    # 2. Adiciona o áudio da locução
    # 3. Desenha a tarja dinâmica (Ticker) com a notícia do Diz Que
    
    comando = [
        "ffmpeg", "-y", "-loop", "1", "-i", cenario, "-i", audio,
        "-vf", 
f"drawtext=text='{texto_noticia}':x=w-t*200:y=h-80:fontsize=40:fontcolor=red:box=1:boxcolor=white@0.8",
        "-c:v", "libx264", "-t", "10", "-pix_fmt", "yuv420p", "-c:a", 
"aac", "-shortest", video_final
    ]

    try:
        subprocess.run(comando, check=True)
        print(f"✅ SUCESSO! O vídeo '{video_final}' está pronto para o 
ar.")
        subprocess.run(["open", video_final])
    except Exception as e:
        print(f"❌ Erro no FFmpeg: {e}. Verifique se a instalação 
terminou.")

if __name__ == "__main__":
    # Simulando uma entrada do seu app DIZ QUE
    noticia_real = "ALERTA DIZ QUE: Transito lento na subida da Ponte 
Rio-Niterói. Evite a região!"
    montar_plantao(noticia_real)
