import os
import subprocess
import time

def processar_tvc():
    logo = os.path.expanduser("~/TVC4/Assets/logo_oficial.png")
    input_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    output_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")

    if not os.path.exists(input_dir):
        print("❌ Pasta 'Brutos' não encontrada.")
        return

    arquivos = [f for f in os.listdir(input_dir) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]

    if not arquivos:
        print("📭 Nenhum vídeo novo para processar.")
        return

    for arquivo in arquivos:
        input_path = os.path.join(input_dir, arquivo)
        output_path = os.path.join(output_dir, f"TVC_{arquivo}")

        print(f"🎬 [PROCESSO] Renderizando: {arquivo}...")

        # Comando FFmpeg otimizado (Corte 9:16 + Overlay Logo)
        cmd = [
            'ffmpeg', '-i', input_path, '-i', logo,
            '-filter_complex',
            '[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920[v];'
            '[v][1:v]overlay=W-w-50:50', 
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '22', '-c:a', 'aac', '-b:a', '192k',
            output_path, '-y'
        ]

        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # --- ALERTA DE VOZ TVC ---
        mensagem = f"Diretor, o vídeo {arquivo} foi finalizado com sucesso."
        os.system(f'say -v Luciana "{mensagem}"')
        
        print(f"✅ [SUCESSO] TVC_{arquivo} exportado para Finalizados.")
        
        # Atualiza o Dashboard automaticamente após cada vídeo
        os.system("python3 ~/TVC4/tvc_dashboard_master.py")

if __name__ == "__main__":
    processar_tvc()
