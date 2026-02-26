#!/usr/bin/env python3
# Dashboard completo da TVC

import os
import json
import psutil
from datetime import datetime

def mostrar():
    os.system('clear')
    
    # Cores
    verde = '\033[92m'
    amarelo = '\033[93m'
    azul = '\033[94m'
    roxo = '\033[95m'
    ciano = '\033[96m'
    reset = '\033[0m'
    negrito = '\033[1m'
    
    print(f"{negrito}{ciano}╔{'═'*60}╗{reset}")
    print(f"{negrito}{ciano}║{reset}{' TVC STUDIOS - DASHBOARD COMPLETO ':^60}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}╠{'═'*60}╣{reset}")
    
    # Hardware
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    print(f"{negrito}{ciano}║{reset} {negrito}💻 HARDWARE{reset}{' ':<49}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}║{reset}   CPU:  {cpu:5.1f}%{' ':<47}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}║{reset}   RAM:  {mem:5.1f}%{' ':<47}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}║{reset}   DISCO: {disk:5.1f}%{' ':<46}{negrito}{ciano}║{reset}")
    
    # Financeiro
    try:
        with open(os.path.expanduser("~/TVC4/GESTAO/dados_financeiros.json")) as f:
            fin = json.load(f)
        print(f"{negrito}{ciano}╠{'═'*60}╣{reset}")
        print(f"{negrito}{ciano}║{reset} {negrito}💰 FINANCEIRO{reset}{' ':<47}{negrito}{ciano}║{reset}")
        print(f"{negrito}{ciano}║{reset}   Equity: R$ {fin['equity_brl']:>13,.2f}{' ':<29}{negrito}{ciano}║{reset}")
    except:
        pass
    
    # Projetos
    try:
        with open(os.path.expanduser("~/TVC4/GESTAO/projetos.json")) as f:
            proj = json.load(f)
        print(f"{negrito}{ciano}╠{'═'*60}╣{reset}")
        print(f"{negrito}{ciano}║{reset} {negrito}🎬 PROJETOS ATIVOS{reset}{' ':<42}{negrito}{ciano}║{reset}")
        for p in proj['projetos']:
            nome = p['nome'][:20]
            status = p['status'][:15]
            prog = p['progresso']
            print(f"{negrito}{ciano}║{reset}   {nome:20} {status:15} {prog:3}%{' ':<9}{negrito}{ciano}║{reset}")
    except:
        pass
    
    # Vídeos
    brutos = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    final = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    
    qtd_brutos = len([f for f in os.listdir(brutos) if f.endswith('.mp4')]) if os.path.exists(brutos) else 0
    qtd_final = len([f for f in os.listdir(final) if f.endswith('.mp4')]) if os.path.exists(final) else 0
    
    print(f"{negrito}{ciano}╠{'═'*60}╣{reset}")
    print(f"{negrito}{ciano}║{reset} {negrito}📹 VÍDEOS{reset}{' ':<50}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}║{reset}   Brutos: {qtd_brutos} | Finalizados: {qtd_final}{' ':<31}{negrito}{ciano}║{reset}")
    
    # Status geral
    print(f"{negrito}{ciano}╠{'═'*60}╣{reset}")
    status = "🟢 OPERACIONAL"
    if qtd_brutos > 0:
        status += f" | {qtd_brutos} vídeo(s) aguardando"
    print(f"{negrito}{ciano}║{reset}   {status}{' ':<42}{negrito}{ciano}║{reset}")
    print(f"{negrito}{ciano}╚{'═'*60}╝{reset}")

if __name__ == "__main__":
    mostrar()
