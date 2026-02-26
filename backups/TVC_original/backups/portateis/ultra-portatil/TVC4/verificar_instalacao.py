#!/usr/bin/env python3
# Verifica o que foi instalado

import os
import subprocess

def verificar():
    print("\n🔍 VERIFICANDO FERRAMENTAS INSTALADAS")
    print("="*50)
    
    ferramentas = {
        "HandBrake": ["handbrake", "HandBrakeCLI"],
        "OBS Studio": ["obs", "OBS"],
        "Audacity": ["audacity", "Audacity"],
        "GIMP": ["gimp", "GIMP"],
        "yt-dlp": ["yt-dlp"],
        "ffmpeg": ["ffmpeg"]
    }
    
    for nome, cmds in ferramentas.items():
        encontrou = False
        for cmd in cmds:
            try:
                subprocess.run(['which', cmd], capture_output=True, check=True)
                encontrou = True
                break
            except:
                pass
                
        if encontrou:
            print(f"✅ {nome}: INSTALADO")
        else:
            print(f"❌ {nome}: NÃO INSTALADO")
            
    print("\n📁 Pastas do TVC Studios:")
    pastas = [
        "~/TVC4",
        "~/TVC4/AUTOMACOES",
        "~/TVC4/GESTAO",
        "~/TVC4/TVC_STUDIOS/Brutos",
        "~/TVC4/TVC_STUDIOS/Finalizados",
        "~/TVC4/TVC_STUDIOS/LEGENDAS"
    ]
    
    for pasta in pastas:
        if os.path.exists(os.path.expanduser(pasta)):
            print(f"✅ {pasta}")
        else:
            print(f"❌ {pasta}")

if __name__ == "__main__":
    verificar()
