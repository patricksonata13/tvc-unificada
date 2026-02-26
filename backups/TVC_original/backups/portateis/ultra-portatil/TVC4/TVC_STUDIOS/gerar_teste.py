import subprocess
import os

def criar_video_teste():
    output = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos/teste_sinal.mp4")
    # Gera um padrão de teste (colorbars) em 1080x1920
    cmd = [
        'ffmpeg', '-f', 'lavfi', '-i', 'testsrc=size=1080x1920:rate=30', 
        '-t', '5', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', output, '-y'
    ]
    subprocess.run(cmd)
    print(f"🎬 Vídeo de teste gerado em 'Brutos': {output}")

if __name__ == "__main__":
    criar_video_teste()
