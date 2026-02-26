#!/usr/bin/env python3
import os
import time
import psutil
import datetime

class TVCHUDColorido:
    def __init__(self):
        self.RED = '\033[91m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.BLUE = '\033[94m'
        self.CYAN = '\033[96m'
        self.BOLD = '\033[1m'
        self.END = '\033[0m'
        
    def barra(self, percent, size=20):
        filled = int(size * percent / 100)
        bar = '█' * filled + '░' * (size - filled)
        color = self.GREEN if percent < 50 else self.YELLOW if percent < 80 else self.RED
        return f"{color}{bar}{self.END}"
        
    def run(self):
        try:
            while True:
                os.system('clear')
                cpu = psutil.cpu_percent()
                mem = psutil.virtual_memory().percent
                disk = psutil.disk_usage('/').percent
                agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                
                print(f"{self.BOLD}{self.CYAN}╔{'═'*50}╗{self.END}")
                print(f"{self.BOLD}{self.CYAN}║{self.END}{' TVC STUDIOS - HUD MONITOR':^50}{self.BOLD}{self.CYAN}║{self.END}")
                print(f"{self.BOLD}{self.CYAN}╠{'═'*50}╣{self.END}")
                print(f"{self.BOLD}{self.CYAN}║{self.END}   📅 {agora}{' ':<29}{self.BOLD}{self.CYAN}║{self.END}")
                print(f"{self.BOLD}{self.CYAN}╠{'═'*50}╣{self.END}")
                print(f"{self.BOLD}{self.CYAN}║{self.END}   CPU:  {self.barra(cpu)} {cpu:5.1f}%{' ':<11}{self.BOLD}{self.CYAN}║{self.END}")
                print(f"{self.BOLD}{self.CYAN}║{self.END}   RAM:  {self.barra(mem)} {mem:5.1f}%{' ':<11}{self.BOLD}{self.CYAN}║{self.END}")
                print(f"{self.BOLD}{self.CYAN}║{self.END}   DISCO: {self.barra(disk)} {disk:5.1f}%{' ':<10}{self.BOLD}{self.CYAN}║{self.END}")
                print(f"{self.BOLD}{self.CYAN}╚{'═'*50}╝{self.END}")
                time.sleep(2)
        except KeyboardInterrupt:
            print(f"\n{self.GREEN}HUD encerrado.{self.END}")

if __name__ == "__main__":
    TVCHUDColorido().run()
