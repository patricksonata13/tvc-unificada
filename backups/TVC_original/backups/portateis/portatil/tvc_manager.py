#!/usr/bin/env python3
# TVC_MANAGER.py - Versão Corrigida

import os
import sys
import time
import subprocess
from pathlib import Path

class TVCManager:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        
    def menu(self):
        while True:
            os.system('clear')
            print(f"""
╔══════════════════════════════════════════════════╗
║         TVC STUDIOS - MANAGER                     ║
╚══════════════════════════════════════════════════╝

 1. 📡 Watchdog (processamento automático)
 2. 📊 HUD em tempo real
 3. 💰 Dashboard Financeiro
 4. 📋 Gerenciar Projetos
 5. 📦 Backup Automático
 6. 📈 Relatórios
 7. 🎬 Processar Vídeos Manualmente
 8. 🔧 Configurações
 9. 🛠️  Ferramentas Externas
 0. 🌐 Plataforma Web
    Sair

 Escolha: """)
            
            opcao = input().strip()
            
            if opcao == '1':
                self.iniciar_watchdog()
            elif opcao == '2':
                self.iniciar_hud()
            elif opcao == '3':
                self.financeiro()
            elif opcao == '4':
                self.projetos()
            elif opcao == '5':
                self.backup()
            elif opcao == '6':
                self.relatorios()
            elif opcao == '7':
                self.processar_agora()
            elif opcao == '8':
                self.configuracoes()
            elif opcao == '9':
                self.ferramentas_externas()
            elif opcao == '0':
                self.plataforma_web()
                break
                
    def iniciar_watchdog(self):
        print("📡 Iniciando watchdog...")
        subprocess.Popen(['python3', f'{self.base}/tvc_watchdog.py'], 
                        stdout=subprocess.DEVNULL, 
                        stderr=subprocess.DEVNULL)
        print("✅ Watchdog iniciado!")
        input("\nPressione Enter...")
        
    def iniciar_hud(self):
        os.system(f'python3 {self.base}/GESTAO/hud_tvc_deluxe.py')
        
    def financeiro(self):
        os.system(f'python3 {self.base}/GESTAO/dashboard_financeiro.py')
        input("\nPressione Enter...")
        
    def projetos(self):
        os.system(f'python3 {self.base}/GESTAO/projetos.py')
        input("\nPressione Enter...")
        
    def backup(self):
        os.system(f'python3 {self.base}/AUTOMACOES/backup_automatico.py listar')
        input("\nPressione Enter...")
        
    def relatorios(self):
        os.system(f'python3 {self.base}/AUTOMACOES/relatorios_automaticos.py agora')
        input("\nPressione Enter...")
        
    def processar_agora(self):
        os.system(f'python3 {self.base}/tvc_processor.py')
        input("\nPressione Enter...")
        
    def configuracoes(self):
        print("""
 CONFIGURAÇÕES:
   1. Verificar dependências
   2. Criar estrutura de pastas
   """)
        op = input("Opção: ")
        if op == '1':
            self.verificar_dependencias()
        elif op == '2':
            self.criar_estrutura()
        input("\nPressione Enter...")
        
    def ferramentas_externas(self):
        os.system(f'python3 {self.base}/GESTAO/menu_ferramentas.py')
        
    def plataforma_web(self):
        os.system(f'bash {self.base}/PLATAFORMA_WEB/iniciar_plataforma.sh')
        
    def verificar_dependencias(self):
        print("\n🔍 Verificando dependências...")
        deps = {'ffmpeg': 'ffmpeg -version', 'python3': 'python3 --version'}
        for nome, cmd in deps.items():
            try:
                subprocess.run(cmd.split(), capture_output=True, check=True)
                print(f"   ✅ {nome}")
            except:
                print(f"   ❌ {nome}")
                
    def criar_estrutura(self):
        pastas = ['Assets', 'TVC_STUDIOS/Brutos', 'TVC_STUDIOS/Finalizados', 
                 'GESTAO', 'GESTAO/RELATORIOS', 'AUTOMACOES', 'BACKUPS']
        for pasta in pastas:
            path = f"{self.base}/{pasta}"
            os.makedirs(path, exist_ok=True)
            print(f"   ✅ {pasta}")

if __name__ == "__main__":
    manager = TVCManager()
    manager.menu()
