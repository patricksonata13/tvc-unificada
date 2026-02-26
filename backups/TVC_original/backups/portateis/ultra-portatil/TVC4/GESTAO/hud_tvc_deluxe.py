#!/usr/bin/env python3
import os
import time
import psutil
import datetime

class TVCHUDDeluxe:
    def __init__(self):
        self.CORES = {
            'reset': '\033[0m',
            'verde': '\033[92m',
            'amarelo': '\033[93m',
            'vermelho': '\033[91m',
            'azul': '\033[94m',
            'roxo': '\033[95m',
            'ciano': '\033[96m',
            'branco': '\033[97m',
            'negrito': '\033[1m',
            'fundo_preto': '\033[40m'
        }
        
    def get_barra(self, percent, tamanho=30):
        cheio = int(tamanho * percent / 100)
        vazio = tamanho - cheio
        if percent < 50:
            cor = self.CORES['verde']
        elif percent < 80:
            cor = self.CORES['amarelo']
        else:
            cor = self.CORES['vermelho']
        return f"{cor}{'█' * cheio}{self.CORES['reset']}{'░' * vazio}"
        
    def run(self):
        try:
            while True:
                os.system('clear')
                
                # Coletar dados
                cpu = psutil.cpu_percent()
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                # Cabecalho
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}╔{'═'*60}╗{self.CORES['reset']}")
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}{self.CORES['negrito']}{' TVC STUDIOS - HUD DELUXE ':^60}{self.CORES['reset']}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}╠{'═'*60}╣{self.CORES['reset']}")
                
                # Data/Hora
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}   📅 {agora}{' ':<39}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}╠{'═'*60}╣{self.CORES['reset']}")
                
                # CPU
                barra_cpu = self.get_barra(cpu)
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}   🖥️  CPU:  {barra_cpu} {cpu:5.1f}%{' ':<21}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                
                # RAM
                barra_mem = self.get_barra(mem)
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}   🧠 RAM:  {barra_mem} {mem:5.1f}%{' ':<21}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                
                # DISCO
                barra_disk = self.get_barra(disk)
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}   💾 DISCO: {barra_disk} {disk:5.1f}%{' ':<20}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                
                # Rodapé
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}╠{'═'*60}╣{self.CORES['reset']}")
                status = "🟢 SAUDÁVEL" if cpu < 70 and mem < 80 else "🟡 ATENÇÃO" if cpu < 90 else "🔴 CRÍTICO"
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}   STATUS: {status}{' ':<47}{self.CORES['negrito']}{self.CORES['roxo']}║{self.CORES['reset']}")
                print(f"{self.CORES['negrito']}{self.CORES['roxo']}╚{'═'*60}╝{self.CORES['reset']}")
                
                time.sleep(2)
                
        except KeyboardInterrupt:
            print(f"\n{self.CORES['verde']}HUD encerrado. Até mais!{self.CORES['reset']}")

if __name__ == "__main__":
    TVCHUDDeluxe().run()
