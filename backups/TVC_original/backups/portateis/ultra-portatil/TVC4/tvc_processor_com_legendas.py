#!/usr/bin/env python3
# Processador de vídeo COM LEGENDAS INTEGRADAS

import os
import subprocess
from pathlib import Path

class TVCProcessorComLegendas:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.assets = f"{self.base}/Assets"
        self.logo = f"{self.assets}/logo_oficial.png"
        
    def processar(self):
        """Processa vídeos com logo E legendas"""
        
        # Pastas
        brutos = f"{self.base}/TVC_STUDIOS/Brutos"
        final = f"{self.base}/TVC_STUDIOS/Finalizados"
        legendas_pt = f"{self.base}/TVC_STUDIOS/LEGENDAS/PT"
        
        print(f"\n🎬 TVC PROCESSADOR COM LEGENDAS")
        print("="*50)
        
        for arquivo in os.listdir(brutos):
            if arquivo.endswith('.mp4'):
                nome = Path(arquivo).stem
                video_in = os.path.join(brutos, arquivo)
                video_out = os.path.join(final, f"TVC_{arquivo}")
                
                # Procurar legenda correspondente
                legenda_pt = os.path.join(legendas_pt, f"{nome}.pt.srt")
                
                print(f"\n📹 Processando: {arquivo}")
                
                if os.path.exists(legenda_pt):
                    print(f"   ✅ Legenda encontrada: {legenda_pt}")
                    
                    # Comando com logo + legenda
                    cmd = [
                        'ffmpeg', '-i', video_in,
                        '-i', self.logo,
                        '-vf', f"movie={self.logo}[logo];[in][logo]overlay=10:10,subtitles={legenda_pt}",
                        '-c:a', 'copy',
                        video_out, '-y'
                    ]
                else:
                    print(f"   ⚠️ Sem legenda, apenas logo")
                    # Comando só com logo
                    cmd = [
                        'ffmpeg', '-i', video_in,
                        '-i', self.logo,
                        '-filter_complex', 'overlay=10:10',
                        '-c:a', 'copy',
                        video_out, '-y'
                    ]
                
                # Executar
                subprocess.run(cmd, capture_output=True)
                print(f"   ✅ Finalizado: {video_out}")
                
        print("\n✅ Processamento concluído!")

if __name__ == "__main__":
    proc = TVCProcessorComLegendas()
    proc.processar()
