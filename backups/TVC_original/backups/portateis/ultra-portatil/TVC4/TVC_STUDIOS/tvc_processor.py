import os, subprocess

def processamento_inteligente():
    input_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    output_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    
    for f in os.listdir(input_dir):
        if f.endswith(".mp4") and not f.startswith("TVC_"):
            print(f"🚀 Renderizando com workflow de Roteiro: {f}")
            out = os.path.join(output_dir, f"TVC_FINAL_{f}")
            
            # Filtro Cinematic TVC + Audio Boost
            cmd = [
                'ffmpeg', '-i', os.path.join(input_dir, f),
                '-vf', 'eq=contrast=1.1:saturation=1.2,unsharp=5:5:1.0:5:5:0.0',
                '-c:v', 'libx264', '-crf', '20', '-c:a', 'aac', '-b:a', '192k', out, '-y'
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            # Notificação Final
            os.system(f'say -v Luciana "Entrega finalizada."')

if __name__ == "__main__":
    processamento_inteligente()
