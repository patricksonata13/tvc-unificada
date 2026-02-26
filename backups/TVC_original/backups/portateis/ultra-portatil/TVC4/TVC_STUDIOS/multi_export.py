import os
import subprocess

def exportar_formatos(video_nome):
    input_path = os.path.expanduser(f"~/TVC4/TVC_STUDIOS/Finalizados/{video_nome}")
    export_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/EXPORT_REDES")
    os.makedirs(export_dir, exist_ok=True)

    formatos = {
        "TIKTOK": "1080:1920",
        "INSTAGRAM_FEED": "1080:1350",
        "YOUTUBE_SHORTS": "1080:1920"
    }

    print(f"🚀 Iniciando exportação multi-plataforma para: {video_nome}")

    for rede, res in formatos.items():
        output = os.path.join(export_dir, f"{rede}_{video_nome}")
        cmd = [
            'ffmpeg', '-i', input_path,
            '-vf', f'scale={res}:force_original_aspect_ratio=increase,crop={res}',
            '-c:v', 'libx264', '-crf', '23', '-preset', 'veryfast', output, '-y'
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ {rede} pronto.")

    os.system(f'say -v Luciana "Diretor, as versões para redes sociais de {video_nome} estão prontas."')

if __name__ == "__main__":
    # Pega o último vídeo finalizado para testar
    finalizados = os.listdir(os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados"))
    videos = [f for f in finalizados if f.startswith("TVC_")]
    if videos:
        exportar_formatos(videos[-1])
    else:
        print("📭 Nenhum vídeo finalizado encontrado.")
