import os
import shutil
import datetime

def processar_entrega():
    origem = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    destino_play = os.path.expanduser("~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/TVC_PLAY")
    log_entrega = os.path.expanduser("~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/protocolos_entrega.txt")
    
    videos = [f for f in os.listdir(origem) if f.startswith("TVC_FINAL_")]
    
    if not videos:
        print("📭 Nada para entregar no momento.")
        return

    for video in videos:
        # Simulação de verificação de Compliance
        print(f"📦 Despachando: {video} para TVC PLAY...")
        
        # Move para a pasta de exibição final
        shutil.copy(os.path.join(origem, video), os.path.join(destino_play, video))
        
        # Gera Protocolo
        with open(log_entrega, "a") as log:
            data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log.write(f"[{data}] ENTREGUE: {video} | DESTINO: TVC_PLAY | STATUS: DISPONÍVEL\n")
            
    os.system('say -v Luciana "Diretor, os episódios foram entregues ao servidor da TVC PLAY e os protocolos de segurança foram gerados."')

if __name__ == "__main__":
    processar_entrega()
