import os, time, psutil

def monitor_incidencias():
    while True:
        cpu = psutil.cpu_percent()
        if cpu > 95:
            os.system('say -v Luciana "Alerta Crítico: Sobrecarga de processamento na Holding."')
            with open(os.path.expanduser("~/TVC4/.system_logs/incidencias.log"), "a") as f:
                f.write(f"{time.ctime()}: Alerta de CPU em {cpu}%\n")
        
        # Verifica se o HUD ainda está a correr
        processos = [p.name() for p in psutil.process_iter()]
        if "python3" not in str(processos):
             print("⚠️ Processos vitais em queda. Reiniciando monitor...")
        
        time.sleep(30) # Monitorização silenciosa a cada 30 seg

if __name__ == "__main__":
    monitor_incidencias()
