import os
import shutil

def limpar_set():
    brutos = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    arquivo_morto = os.path.expanduser("~/TVC4/TVC_STUDIOS/Arquivo_Morto")
    os.makedirs(arquivo_morto, exist_ok=True)
    
    arquivos = [f for f in os.listdir(brutos) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]
    
    for f in arquivos:
        shutil.move(os.path.join(brutos, f), os.path.join(arquivo_morto, f))
        print(f"📦 {f} movido para Arquivo Morto.")

if __name__ == "__main__":
    limpar_set()
