#!/usr/bin/env python3
# Gera relatório completo do sistema

import os
import json
import datetime
import psutil

def gerar_status():
    data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    status = {
        'data': data,
        'hardware': {
            'cpu': psutil.cpu_percent(),
            'memoria': psutil.virtual_memory().percent,
            'disco': psutil.disk_usage('/').percent
        },
        'financeiro': {},
        'projetos': {},
        'videos': {}
    }
    
    # Dados financeiros
    try:
        with open(os.path.expanduser("~/TVC4/GESTAO/dados_financeiros.json")) as f:
            status['financeiro'] = json.load(f)
    except:
        status['financeiro'] = {'erro': 'não encontrado'}
    
    # Projetos
    try:
        with open(os.path.expanduser("~/TVC4/GESTAO/projetos.json")) as f:
            status['projetos'] = json.load(f)
    except:
        status['projetos'] = {'erro': 'não encontrado'}
    
    # Contar vídeos
    brutos = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    finalizados = os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")
    
    if os.path.exists(brutos):
        status['videos']['brutos'] = len([f for f in os.listdir(brutos) if f.endswith('.mp4')])
    if os.path.exists(finalizados):
        status['videos']['finalizados'] = len([f for f in os.listdir(finalizados) if f.endswith('.mp4')])
    
    # Salvar
    arquivo = os.path.expanduser(f"~/TVC4/GESTAO/RELATORIOS/status_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    with open(arquivo, 'w') as f:
        json.dump(status, f, indent=2)
    
    print(f"✅ Status salvo em: {arquivo}")
    return status

if __name__ == "__main__":
    gerar_status()
