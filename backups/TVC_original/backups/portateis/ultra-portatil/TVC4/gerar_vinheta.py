import os
import subprocess

def criar_vinheta():
    saida = 
os.path.expanduser("~/TVC4/Assets/vinheta_tvc.mp4")
    # Gera um flash branco com o nome da TVC 
centralizado
    comando = [
        "ffmpeg", "-y", "-f", "lavfi", "-i", 
"color=c=white:s=1280x720:d=3",
        "-vf", "drawtext=text='TVC 
4.0':x=(w-tw)/2:y=(h-th)/2:fontsize=70:fontcolor=black:alpha='if(lt(t,1.5),t/1.5,1-(t-1.5)/1.5)'",
        "-c:v", "libx264", "-pix_fmt", "yuv420p", saida
    ]
    subprocess.run(comando)
    print(f"🎬 Vinheta de transição criada: {saida}")

if __name__ == "__main__":
    criar_vinheta()
