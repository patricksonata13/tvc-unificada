import os, shutil

def publicar_video():
    origem = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    destino = os.path.expanduser("~/TVC4/NUCLEO_PLAY/CONTEUDO_PUBLICADO")
    os.makedirs(destino, exist_ok=True)
    
    arquivos = os.listdir(origem)
    if not arquivos:
        print("📭 Nada em 'Finalizados' para publicar.")
        return

    for arq in arquivos:
        shutil.move(os.path.join(origem, arq), os.path.join(destino, arq))
        print(f"🚀 {arq} agora está AO VIVO no TVC PLAY!")

if __name__ == "__main__":
    publicar_video()
