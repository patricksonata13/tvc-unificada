#!/usr/bin/env python3
# Integração com Whisper Notes para transcrição

import os
import subprocess
from pathlib import Path

class TVCWhisper:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        
    def enviar_para_whisper(self, video_path):
        """Abre o vídeo no Whisper Notes para transcrição"""
        
        # Whisper Notes usa o Finder para abrir arquivos
        subprocess.run(['open', video_path])
        
        print("📤 Vídeo aberto no Whisper Notes")
        print("   Transcreva manualmente e salve a legenda em:")
        print(f"   {self.base}/TVC_STUDIOS/LEGENDAS/PT/")
        
    def processar_pasta(self):
        """Abre todos os vídeos novos no Whisper"""
        finalizados = f"{self.base}/TVC_STUDIOS/Finalizados"
        legendas = f"{self.base}/TVC_STUDIOS/LEGENDAS/PT"
        
        for video in os.listdir(finalizados):
            if not video.endswith('.mp4'):
                continue
                
            nome = Path(video).stem
            legenda = f"{legendas}/{nome}.pt.srt"
            
            # Se não tem legenda, abre no Whisper
            if not os.path.exists(legenda):
                print(f"\n🎬 Novo vídeo: {video}")
                self.enviar_para_whisper(os.path.join(finalizados, video))
                input("Pressione Enter após transcrever para continuar...")

if __name__ == "__main__":
    wh = TVCWhisper()
    wh.processar_pasta()
