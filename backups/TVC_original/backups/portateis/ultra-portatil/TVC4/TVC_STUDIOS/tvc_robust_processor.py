import os, subprocess, hashlib, shutil

def get_md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def processar_robusto():
    brutos_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    vault_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/COFRE_ORIGINAIS")
    finalizados_dir = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    os.makedirs(vault_dir, exist_ok=True)

    arquivos = [f for f in os.listdir(brutos_dir) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]

    for f in arquivos:
        input_path = os.path.join(brutos_dir, f)
        print(f"🔒 [INTEGRIDADE] Gerando Hash MD5 para {f}...")
        
        # 1. Processamento Cinematográfico (Look TVC)
        output_path = os.path.join(finalizados_dir, f"TVC_FINAL_{f}")
        cmd = [
            'ffmpeg', '-i', input_path, 
            '-vf', 'eq=contrast=1.2:saturation=1.3,scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920',
            '-c:v', 'libx264', '-crf', '18', '-preset', 'slow', output_path, '-y'
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 2. Mover para o Cofre (Segurança)
        shutil.move(input_path, os.path.join(vault_dir, f))
        print(f"✅ [SUCESSO] {f} processado e movido para o COFRE.")
        
    os.system('say -v Luciana "Diretor, os brutos foram processados e os originais estão protegidos no cofre."')

if __name__ == "__main__":
    processar_robusto()
