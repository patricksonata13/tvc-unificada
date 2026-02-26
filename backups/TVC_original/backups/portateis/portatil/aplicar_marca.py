import os
import subprocess

def carimbar():
    ffmpeg_path = "/opt/homebrew/bin/ffmpeg" # Ajustaremos se necessario
    video_input = os.path.expanduser("~/TVC4/Assets/Novelas/cap05.mp4")
    logo = os.path.expanduser("~/TVC4/Assets/logo_tvc_transparente.png")
    output = os.path.expanduser("~/TVC4/TVC4_FINAL_COM_LOGO.mp4")
    
    # Comando para colocar a logo no canto (overlay)
    comando = [
        "ffmpeg", "-y", "-i", video_input, "-i", logo,
        "-filter_complex", "overlay=W-w-10:10",
        "-c:a", "copy", output
    ]
    
    print("📺 Carimbando a marca da TVC 4.0 no video...")
    subprocess.run(comando)
    print(f"✅ Video pronto para o ar: {output}")

if __name__ == "__main__":
    carimbar()
