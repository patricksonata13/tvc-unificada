#!/usr/bin/env python3
# Menu integrado de ferramentas externas

import os
import subprocess

def menu():
    while True:
        os.system('clear')
        
        print(f"""
╔══════════════════════════════════════════════════╗
║         TVC STUDIOS - FERRAMENTAS EXTERNAS       ║
╚══════════════════════════════════════════════════╝

 1. 🎬 HandBrake - Otimizar vídeos
 2. 🎨 DaVinci Resolve - Criar projeto
 3. 🎤 Whisper Notes - Transcrever áudio
 4. 📹 OBS Studio - Gravar programa
 5. 🔊 Audacity - Editar áudio
 6. 🖼️  GIMP - Editar thumbnails
 7. 📥 yt-dlp - Baixar vídeos
 8. 🔧 Instalar todas as ferramentas
 0. 🔙 Voltar

 Escolha: """)
        
        op = input().strip()
        
        if op == '1':
            os.system('python3 ~/TVC4/AUTOMACOES/otimizar_handbrake.py')
            input("\nPressione Enter...")
            
        elif op == '2':
            os.system('python3 ~/TVC4/AUTOMACOES/davinci_projects.py')
            input("\nPressione Enter...")
            
        elif op == '3':
            os.system('python3 ~/TVC4/AUTOMACOES/whisper_integration.py')
            input("\nPressione Enter...")
            
        elif op == '4':
            os.system('python3 ~/TVC4/AUTOMACOES/obs_recorder.py')
            input("\nPressione Enter...")
            
        elif op == '5':
            os.system('python3 ~/TVC4/AUTOMACOES/audacity_processor.py')
            input("\nPressione Enter...")
            
        elif op == '6':
            subprocess.run(['open', '-a', 'GIMP'])
            input("\n✅ GIMP aberto. Pressione Enter...")
            
        elif op == '7':
            url = input("URL do vídeo: ")
            os.system(f'yt-dlp -o "~/TVC4/TVC_STUDIOS/Brutos/%(title)s.%(ext)s" {url}')
            input("\n✅ Download concluído!")
            
        elif op == '8':
            os.system('bash ~/TVC4/instalar_ferramentas.sh')
            input("\nPressione Enter...")
            
        elif op == '0':
            break

if __name__ == "__main__":
    menu()
