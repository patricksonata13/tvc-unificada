#!/usr/bin/env python3
import os, time, psutil, datetime, platform
class TVCHUD:
    def __init__(self):
        self.cores = {'reset': '\033[0m', 'verde': '\033[92m', 'ciano': '\033[96m', 'negrito': '\033[1m'}
    def run(self):
        try:
            while True:
                os.system('clear')
                stats = {'cpu': psutil.cpu_percent(), 'memoria': psutil.virtual_memory().percent, 'data': datetime.datetime.now().strftime("%d/%m/%Y %H:%M")}
                print(f"{self.cores['ciano']}{self.cores['negrito']}╔═ TVC HUD ═╗{self.cores['reset']}")
                print(f"   {stats['data']}")
                print(f"   CPU: {stats['cpu']}%")
                print(f"   RAM: {stats['memoria']}%")
                print(f"{self.cores['ciano']}{self.cores['negrito']}╚═══════════╝{self.cores['reset']}")
                time.sleep(2)
        except: pass
if __name__ == "__main__": TVCHUD().run()
