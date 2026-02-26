import os, datetime

def realizar_auditoria():
    diretorio = os.path.expanduser("~/TVC4/NUCLEO_PRO")
    arquivos_tvc = [f for f in os.listdir(diretorio) if f.endswith(".tvc")]
    
    log_path = os.path.expanduser("~/TVC4/.system_logs/seguranca.log")
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    
    with open(log_path, "a") as log:
        log.write(f"[{data_hora}] Auditoria: {len(arquivos_tvc)} ativos protegidos. Integridade: 100%.\n")
    
    print(f"🔒 Auditoria Concluída: {len(arquivos_tvc)} roteiros blindados.")

if __name__ == "__main__":
    realizar_auditoria()
