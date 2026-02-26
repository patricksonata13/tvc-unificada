#!/usr/bin/env python3
# Menu de Legendas da TVC

import os
import subprocess
from pathlib import Path

def menu_legendas():
    while True:
        os.system('clear')
        
        print(f"""
╔══════════════════════════════════════════════════╗
║         TVC STUDIOS - SISTEMA DE LEGENDAS        ║
╚══════════════════════════════════════════════════╝

 1. 📝 Gerar legendas PT (Whisper IA)
 2. 🌎 Traduzir para Inglês
 3. 🇪🇸 Traduzir para Espanhol
 4. 🇫🇷 Traduzir para Francês
 5. 🎬 Processar vídeos com legendas
 6. 📂 Ver legendas geradas
 7. 🔧 Instalar dependências
 0. 🔙 Voltar

 Escolha uma opção: """)
        
        opcao = input().strip()
        
        if opcao == '1':
            os.system('python3 ~/TVC4/AUTOMACOES/legendas.py')
            input("\nPressione Enter para continuar...")
            
        elif opcao == '2':
            os.system('python3 ~/TVC4/AUTOMACOES/legendas_avancado.py')
            input("\nPressione Enter para continuar...")
            
        elif opcao == '3':
            print("\n🇪🇸 Tradução para Espanhol...")
            # Implementar
            input("\nPressione Enter para continuar...")
            
        elif opcao == '4':
            print("\n🇫🇷 Tradução para Francês...")
            # Implementar
            input("\nPressione Enter para continuar...")
            
        elif opcao == '5':
            os.system('python3 ~/TVC4/tvc_processor_com_legendas.py')
            input("\nPressione Enter para continuar...")
            
        elif opcao == '6':
            print("\n📂 Legendas disponíveis:")
            os.system('ls -la ~/TVC4/TVC_STUDIOS/LEGENDAS/*/*.srt 2>/dev/null')
            input("\nPressione Enter para continuar...")
            
        elif opcao == '7':
            print("\n🔧 Instalando dependências...")
            os.system('pip3 install faster-whisper openai-whisper pysrt')
            os.system('brew install ffmpeg')
            input("\nPressione Enter para continuar...")
            
        elif opcao == '0':
            break

if __name__ == "__main__":
    menu_legendas()
