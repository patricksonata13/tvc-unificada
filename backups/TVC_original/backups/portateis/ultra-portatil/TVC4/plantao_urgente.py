import os
import subprocess

def disparar_emergencia():
    base = os.path.expanduser("~/TVC4")
    vinheta = os.path.join(base, 
"Assets/vinheta_tvc.mp4")
    noticia_txt = os.path.join(base, 
"Assets/status_transito.txt")
    saida_emergencia = os.path.join(base, 
"PLANTAO_AO_VIVO.mp4")

    # 1. Gerar um bip de alerta de 2 segundos
    print("🔔 Gerando sinal sonoro de alerta...")
    subprocess.run([
        "ffmpeg", "-y", "-f", "lavfi", "-i", 
"sine=frequency=1000:duration=2", 
        os.path.join(base, "Assets/alerta.wav")
    ])

    # 2. Criar o vídeo do plantão com a notícia do 'Diz 
Que'
    print("🚨 Montando vídeo de emergência...")
    # Lendo a notícia
    with open(noticia_txt, 'r') as f:
        texto = f.read()

    comando = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", 
"color=c=gray:s=1280x720:d=5",
        "-vf", 
f"drawtext=text='{texto}':x=(w-tw)/2:y=(h-th)/2:fontsize=40:fontcolor=white:box=1:boxcolor=red@0.8",
        "-c:v", "libx264", os.path.join(base, 
"Assets/corpo_plantao.mp4")
    ]
    subprocess.run(comando)

    # 3. Concatenar Vinheta + Corpo do Plantão
    # (Criando lista para o FFmpeg)
    with open("join.txt", "w") as f:
        f.write(f"file 'Assets/vinheta_tvc.mp4'\nfile 
'Assets/corpo_plantao.mp4'")

    subprocess.run(["ffmpeg", "-y", "-f", "concat", 
"-safe", "0", "-i", "join.txt", "-c", "copy", 
saida_emergencia])
    
    print(f"🔥 PLANTÃO GERADO! Abrindo 
{saida_emergencia}")
    subprocess.run(["open", saida_emergencia])

if __name__ == "__main__":
    disparar_emergencia()
