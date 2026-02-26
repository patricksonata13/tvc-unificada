#!/usr/bin/env python3
# Sistema de legendas usando SpeechRecognition (mais leve)

import os
import subprocess
import speech_recognition as sr
from pydub import AudioSegment
from pathlib import Path

class TVCLegendasSR:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.legendas_dir = f"{self.base}/TVC_STUDIOS/LEGENDAS"
        os.makedirs(f"{self.legendas_dir}/PT", exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/EN", exist_ok=True)
        
    def extrair_audio(self, video_path):
        """Extrai áudio do vídeo"""
        audio_path = video_path.replace('.mp4', '.wav').replace('Brutos', 'Temp')
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        
        cmd = ['ffmpeg', '-i', video_path, '-ar', '16000', '-ac', '1', audio_path, '-y', '-loglevel', 'quiet']
        subprocess.run(cmd)
        return audio_path
        
    def transcrever_audio(self, audio_path):
        """Transcreve áudio usando Google Speech Recognition"""
        recognizer = sr.Recognizer()
        
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            
        try:
            # Tenta português
            texto = recognizer.recognize_google(audio, language='pt-BR')
            return texto
        except:
            try:
                # Tenta inglês
                texto = recognizer.recognize_google(audio, language='en-US')
                return texto
            except:
                return "[Áudio não pôde ser transcrito]"
                
    def criar_legenda(self, video_path):
        """Cria legenda para um vídeo"""
        nome = Path(video_path).stem
        print(f"\n🎬 Processando: {nome}")
        
        # Extrair áudio
        audio = self.extrair_audio(video_path)
        
        # Transcrever
        print("   🤖 Transcrevendo áudio...")
        texto = self.transcrever_audio(audio)
        
        # Criar legenda PT
        srt_pt = f"{self.legendas_dir}/PT/{nome}.pt.srt"
        with open(srt_pt, 'w', encoding='utf-8') as f:
            f.write(f"""1
00:00:01,000 --> 00:00:10,000
{texto}

2
00:00:11,000 --> 00:00:15,000
Fim da transcrição automática.
""")
        
        # Criar versão em inglês (simplificada)
        srt_en = f"{self.legendas_dir}/EN/{nome}.en.srt"
        with open(srt_en, 'w', encoding='utf-8') as f:
            f.write(f"""1
00:00:01,000 --> 00:00:10,000
{texto}

2
00:00:11,000 --> 00:00:15,000
End of automatic transcription.
""")
        
        print(f"   ✅ Legendas criadas em: {srt_pt}")
        
        # Limpar
        if os.path.exists(audio):
            os.remove(audio)
            
    def processar_todos(self):
        """Processa todos os vídeos da pasta Brutos"""
        brutos = f"{self.base}/TVC_STUDIOS/Brutos"
        
        for arquivo in os.listdir(brutos):
            if arquivo.endswith('.mp4'):
                video = os.path.join(brutos, arquivo)
                self.criar_legenda(video)

if __name__ == "__main__":
    leg = TVCLegendasSR()
    leg.processar_todos()
