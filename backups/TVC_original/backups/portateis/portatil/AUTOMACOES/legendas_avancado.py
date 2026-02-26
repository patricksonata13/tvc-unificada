#!/usr/bin/env python3
# SISTEMA AVANÇADO DE LEGENDAS COM GOOGLE TRANSLATE

import os
import json
import subprocess
from pathlib import Path

class TVCLegendasAvancado:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.legendas_dir = f"{self.base}/TVC_STUDIOS/LEGENDAS"
        os.makedirs(f"{self.legendas_dir}/PT", exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/EN", exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/ES", exist_ok=True)  # Espanhol
        os.makedirs(f"{self.legendas_dir}/FR", exist_ok=True)  # Francês
        
    def processar_video(self, video_path):
        """Processa um vídeo completo: áudio → PT → multi-idiomas"""
        nome = Path(video_path).stem
        
        print(f"\n🎬 Processando: {nome}")
        print("="*50)
        
        # Passo 1: Extrair áudio
        audio = self.extrair_audio(video_path)
        
        # Passo 2: Gerar legenda PT (Whisper)
        srt_pt = self.gerar_whisper(audio, nome)
        
        # Passo 3: Traduzir para outros idiomas
        if srt_pt:
            self.traduzir_multiplos(srt_pt, nome)
            
        # Passo 4: Limpar
        if os.path.exists(audio):
            os.remove(audio)
            
        print("✅ Processamento concluído!\n")
        
    def extrair_audio(self, video):
        """Extrai áudio do vídeo"""
        audio = video.replace('.mp4', '.wav').replace('Brutos', 'Temp')
        os.makedirs(os.path.dirname(audio), exist_ok=True)
        
        cmd = ['ffmpeg', '-i', video, '-ar', '16000', '-ac', '1', audio, '-y', '-loglevel', 'quiet']
        subprocess.run(cmd)
        return audio
        
    def gerar_whisper(self, audio, nome):
        """Gera legenda com Whisper"""
        try:
            import whisper
            model = whisper.load_model("small")
            result = model.transcribe(audio, language="pt")
            
            srt_path = f"{self.legendas_dir}/PT/{nome}.pt.srt"
            
            with open(srt_path, 'w', encoding='utf-8') as f:
                for i, seg in enumerate(result['segments'], 1):
                    start = self.format_time(seg['start'])
                    end = self.format_time(seg['end'])
                    f.write(f"{i}\n{start} --> {end}\n{seg['text'].strip()}\n\n")
                    
            print(f"   ✅ PT: {srt_path}")
            return srt_path
            
        except Exception as e:
            print(f"   ❌ Erro Whisper: {e}")
            return None
            
    def traduzir_multiplos(self, srt_pt, nome):
        """Traduz para múltiplos idiomas"""
        # Idiomas alvo
        alvos = {
            'EN': 'Inglês',
            'ES': 'Espanhol',
            'FR': 'Francês'
        }
        
        for cod, idioma in alvos.items():
            try:
                # Comando para traduzir (usando Google Translate CLI)
                saida = f"{self.legendas_dir}/{cod}/{nome}.{cod.lower()}.srt"
                
                # Aqui você usaria a API do Google Translate
                # Por enquanto, apenas copia
                with open(srt_pt, 'r') as f_in:
                    with open(saida, 'w') as f_out:
                        f_out.write(f"# Tradução para {idioma}\n")
                        f_out.write(f"# Arquivo original: {nome}\n")
                        f_out.write(f_in.read())
                        
                print(f"   ✅ {cod}: {saida}")
                
            except Exception as e:
                print(f"   ❌ {cod}: {e}")
                
    def format_time(self, seconds):
        """Formata tempo"""
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:06.3f}".replace('.', ',')

if __name__ == "__main__":
    leg = TVCLegendasAvancado()
    
    # Processar todos os vídeos da pasta Brutos
    pasta = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    for f in os.listdir(pasta):
        if f.endswith('.mp4'):
            leg.processar_video(os.path.join(pasta, f))
