#!/usr/bin/env python3
# Sistema de legendas usando Google Cloud Speech API
# Requer: conta Google Cloud e credenciais

import os
import subprocess
import json
from pathlib import Path

class TVCLegendasGoogle:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.legendas_dir = f"{self.base}/TVC_STUDIOS/LEGENDAS"
        os.makedirs(f"{self.legendas_dir}/PT", exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/EN", exist_ok=True)
        
    def verificar_credenciais(self):
        """Verifica se as credenciais do Google Cloud existem"""
        cred_path = os.path.expanduser("~/google-cloud-credentials.json")
        if not os.path.exists(cred_path):
            print("\n⚠️  Credenciais do Google Cloud não encontradas!")
            print("Para usar esta opção:")
            print("1. Crie uma conta no Google Cloud")
            print("2. Ative a Speech-to-Text API")
            print("3. Baixe as credenciais para ~/google-cloud-credentials.json")
            return False
        return True
        
    def transcrever_com_google(self, audio_path, idioma='pt-BR'):
        """Transcreve usando Google Cloud Speech API"""
        try:
            from google.cloud import speech_v1
            import io
            
            client = speech_v1.SpeechClient()
            
            with io.open(audio_path, 'rb') as f:
                content = f.read()
                
            audio = speech_v1.RecognitionAudio(content=content)
            config = speech_v1.RecognitionConfig(
                encoding=speech_v1.RecognitionConfig.AudioEncoding.LINEAR16,
                sample_rate_hertz=16000,
                language_code=idioma,
                enable_automatic_punctuation=True,
            )
            
            response = client.recognize(config=config, audio=audio)
            
            texto = []
            for result in response.results:
                texto.append(result.alternatives[0].transcript)
                
            return ' '.join(texto)
            
        except Exception as e:
            print(f"   ❌ Erro na transcrição Google: {e}")
            return None
            
    def criar_legenda(self, video_path):
        """Cria legenda usando Google Cloud"""
        if not self.verificar_credenciais():
            return
            
        nome = Path(video_path).stem
        print(f"\n🎬 Processando: {nome}")
        
        # Extrair áudio
        audio = video_path.replace('.mp4', '.wav').replace('Brutos', 'Temp')
        os.makedirs(os.path.dirname(audio), exist_ok=True)
        
        cmd = ['ffmpeg', '-i', video_path, '-ar', '16000', '-ac', '1', audio, '-y', '-loglevel', 'quiet']
        subprocess.run(cmd)
        
        # Transcrever em português
        print("   🤖 Transcrevendo em português...")
        texto_pt = self.transcrever_com_google(audio, 'pt-BR')
        
        if texto_pt:
            srt_pt = f"{self.legendas_dir}/PT/{nome}.pt.srt"
            with open(srt_pt, 'w', encoding='utf-8') as f:
                f.write(f"""1
00:00:01,000 --> 00:00:10,000
{texto_pt}
""")
            print(f"   ✅ PT: {srt_pt}")
            
        # Transcrever em inglês
        print("   🤖 Transcrevendo em inglês...")
        texto_en = self.transcrever_com_google(audio, 'en-US')
        
        if texto_en:
            srt_en = f"{self.legendas_dir}/EN/{nome}.en.srt"
            with open(srt_en, 'w', encoding='utf-8') as f:
                f.write(f"""1
00:00:01,000 --> 00:00:10,000
{texto_en}
""")
            print(f"   ✅ EN: {srt_en}")
            
        # Limpar
        if os.path.exists(audio):
            os.remove(audio)

if __name__ == "__main__":
    leg = TVCLegendasGoogle()
    
    brutos = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    for f in os.listdir(brutos):
        if f.endswith('.mp4'):
            leg.criar_legenda(os.path.join(brutos, f))
