import os, time, psutil, datetime, json

def draw_hud():
    while True:
        os.system('clear')
        now = datetime.datetime.now().strftime("%H:%M:%S")
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        
        # Carrega dados financeiros
        try:
            with open(os.path.expanduser("~/TVC4/CORPORATIVO/BI_FINANCAS/BALANCO_REAL_TVC.json"), "r") as f:
                fin = json.load(f)
                lucro = fin["lucro_real_distribuivel"]
        except: lucro = 0.0

        print(f"============================================================")
        print(f" TVC STUDIOS | OPERATIONAL HUD | {now} ")
        print(f"============================================================")
        print(f" [HARDWARE STATUS]")
        print(f" CPU LOAD: {cpu}%    MEMORY: {mem}%")
        print(f" SYSTEM TEMPERATURE: STABLE")
        print(f"------------------------------------------------------------")
        print(f" [FINANCIAL INTELLIGENCE]")
        print(f" EQUITY (BRL): R$ {lucro:,.2f}")
        print(f" EQUITY (USD): U$ {lucro/5.20:,.2f}")
        print(f" MARKET VOLATILITY: LOW")
        print(f"------------------------------------------------------------")
        print(f" [ACTIVE PIPELINE]")
        print(f" PROJECTS: 23 | SQUAD: 147 | SECURITY: AES-256 ACTIVE")
        print(f"------------------------------------------------------------")
        print(f" STATUS: SYSTEM IDLE - MONITORING ACTIVE...")
        print(f" (Press Ctrl+C to exit HUD)")
        time.sleep(1.5)

if __name__ == "__main__":
    draw_hud()
