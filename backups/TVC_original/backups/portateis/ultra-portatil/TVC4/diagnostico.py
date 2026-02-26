#!/usr/bin/env python3
# Diagnóstico do sistema TVC

import os
from pathlib import Path

base = os.path.expanduser("~/TVC4")

print("\n🔍 DIAGNÓSTICO TVC STUDIOS")
print("="*50)

# Verificar arquivos necessários
arquivos = {
    "tvc_watchdog.py": "AUTOMACOES",
    "tvc_processor.py": "",
    "GESTAO/hud_tvc.py": "GESTAO",
    "GESTAO/dashboard_financeiro.py": "GESTAO",
    "GESTAO/projetos.py": "GESTAO",
    "AUTOMACOES/backup_automatico.py": "AUTOMACOES",
    "AUTOMACOES/relatorios_automaticos.py": "AUTOMACOES",
}

for arquivo, pasta in arquivos.items():
    if pasta:
        path = f"{base}/{pasta}/{arquivo.split('/')[-1]}"
    else:
        path = f"{base}/{arquivo}"
    
    if os.path.exists(path):
        print(f"✅ {arquivo}: OK")
    else:
        print(f"❌ {arquivo}: NÃO ENCONTRADO")

# Verificar pastas
pastas = [
    "Assets",
    "TVC_STUDIOS/Brutos",
    "TVC_STUDIOS/Finalizados",
    "GESTAO",
    "GESTAO/RELATORIOS",
    "AUTOMACOES",
    "BACKUPS"
]

print("\n📁 PASTAS:")
for pasta in pastas:
    path = f"{base}/{pasta}"
    if os.path.exists(path):
        print(f"✅ {pasta}: OK")
    else:
        print(f"❌ {pasta}: NÃO ENCONTRADA")

# Verificar arquivos de dados
dados = [
    "GESTAO/dados_financeiros.json",
    "GESTAO/projetos.json",
    "AUTOMACOES/backup_log.json"
]

print("\n📊 ARQUIVOS DE DADOS:")
for dado in dados:
    path = f"{base}/{dado}"
    if os.path.exists(path):
        tamanho = os.path.getsize(path)
        print(f"✅ {dado}: OK ({tamanho} bytes)")
    else:
        print(f"❌ {dado}: NÃO ENCONTRADO")

print("\n" + "="*50)
