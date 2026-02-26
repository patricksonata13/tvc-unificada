#!/usr/bin/env python3
# Versão alternativa usando ffmpeg (já instalado)

import os
import subprocess
from pathlib import Path

class TVCOtimizadorFFmpeg:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        
    def otimizar(self, video_path):
        """Otimiza vídeo usando ffmpeg (mais leve que HandBrake)"""
        nome = Path(video_path).stem
        saida = os.path.join(self.base, "TVC_STUDIOS/Otimizados", f"{nome}_otimizado.mp4")
        
        os.makedirs(os.path.dirname(saida), exist_ok=True)
        
        print(f"🎬 Otimizando: {nome}")
        
        # ffmpeg com parâmetros de qualidade
        cmd = [
            'ffmpeg', '-i', video_path,
            '-c:v', 'libx264',
            '-crf', '23',  # Qualidade (18-28, menor = melhor)
            '-preset', 'medium',
            '-c:a', 'aac',
            '-b:a', '128k',
            '-movflags', '+faststart',
            '-vf', 'scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2',
            saida, '-y'
        ]
        
        subprocess.run(cmd)
        print(f"✅ Otimizado: {saida}")
        return saida
        
    def otimizar_pasta(self):
        """Otimiza todos os vídeos da pasta Finalizados"""
        finalizados = f"{self.base}/TVC_STUDIOS/Finalizados"
        
        for arquivo in os.listdir(finalizados):
            if arquivo.endswith('.mp4'):
                video = os.path.join(finalizados, arquivo)
                self.otimizar(video)

if __name__ == "__main__":
    opt = TVCOtimizadorFFmpeg()
    opt.otimizar_pasta()
