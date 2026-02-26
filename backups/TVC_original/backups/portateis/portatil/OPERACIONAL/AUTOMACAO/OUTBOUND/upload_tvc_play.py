import os, time, shutil

def simulador_upload():
    finalizados = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    servidor_tvc_play = os.path.expanduser("~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/TVC_PLAY")
    
    fila = [f for f in os.listdir(finalizados) if f.startswith("TVC_FINAL_")]
    
    if not fila:
        print("☁️ [UPLOAD] Servidor em standby. Nenhuma mídia nova.")
        return

    for video in fila:
        print(f"☁️ [UPLOAD] Transferindo {video} para o CDN do TVC Play...")
        # Simula o tempo de upload
        time.sleep(1) 
        shutil.copy(os.path.join(finalizados, video), os.path.join(servidor_tvc_play, video))
        print(f"✅ [PUBLISHED] {video} está online em www.tvcplay.com.br/assistir")

    os.system('say -v Luciana "Diretor, o conteúdo está oficialmente online para os assinantes."')

if __name__ == "__main__":
    simulador_upload()
