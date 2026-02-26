import shutil, os, datetime

def realizar_backup():
    origem = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    data = datetime.datetime.now().strftime("%Y-%m-%d")
    destino = os.path.expanduser(f"~/TVC4/BACKUP_DIARIO/BRUTOS_{data}")
    
    os.makedirs(destino, exist_ok=True)
    arquivos = os.listdir(origem)
    
    if not arquivos:
        print("📭 Nada para fazer backup hoje.")
        return

    for arq in arquivos:
        shutil.copy2(os.path.join(origem, arq), os.path.join(destino, arq))
        print(f"🛡️ Backup concluído: {arq}")

if __name__ == "__main__":
    realizar_backup()
