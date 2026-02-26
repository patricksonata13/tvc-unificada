import time
import subprocess
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MasterHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.mp4', '.mov', '.mkv')):
            nome_arquivo = os.path.basename(event.src_path)
            print(f"✨ [DETECÇÃO] Novo bruto na área: {nome_arquivo}")
            
            # 1. Aguarda estabilidade do arquivo
            time.sleep(2)
            
            # 2. Processamento Principal (Logo + Vertical)
            print("🎬 [PASSO 1/3] Iniciando Processamento Principal...")
            subprocess.run(["python3", os.path.expanduser("~/TVC4/tvc_processor.py")])
            
            # 3. Exportação Multi-Plataforma
            print("🚀 [PASSO 2/3] Gerando versões para Redes Sociais...")
            subprocess.run(["python3", os.path.expanduser("~/TVC4/TVC_STUDIOS/multi_export.py")])
            
            # 4. Auditoria de Custos Atualizada
            print("💰 [PASSO 3/3] Atualizando Auditoria Financeira...")
            subprocess.run(["python3", os.path.expanduser("~/TVC4/NUCLEO_ECO/auditoria_financeira.py")])
            
            print(f"🏁 [CONCLUÍDO] Fluxo completo para {nome_arquivo}")

if __name__ == "__main__":
    path = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    event_handler = MasterHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    print(f"📡 TVC STUDIOS: Sistema de Automação Total Ativo...")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
