#!/usr/bin/env python3
# SISTEMA DE LEGENDAS AUTOMÁTICAS DA TVC
# Gera legendas em português e traduz para inglês

import os
import sys
import json
import subprocess
from pathlib import Path

class TVCLegendas:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.assets = f"{self.base}/Assets"
        self.legendas_dir = f"{self.base}/TVC_STUDIOS/LEGENDAS"
        self.cores = {
            'verde': '\033[92m',
            'amarelo': '\033[93m',
            'azul': '\033[94m',
            'reset': '\033[0m',
            'negrito': '\033[1m'
        }
        
        # Criar pastas
        os.makedirs(self.legendas_dir, exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/PT", exist_ok=True)
        os.makedirs(f"{self.legendas_dir}/EN", exist_ok=True)
        
    def log(self, msg, cor='verde'):
        print(f"{self.cores[cor]}{msg}{self.cores['reset']}")
        
    def extrair_audio(self, video_path):
        """Extrai áudio do vídeo para processamento"""
        audio_path = video_path.replace('.mp4', '.wav').replace('Brutos', 'Temp')
        os.makedirs(os.path.dirname(audio_path), exist_ok=True)
        
        self.log(f"🎵 Extraindo áudio: {os.path.basename(video_path)}", 'azul')
        cmd = [
            'ffmpeg', '-i', video_path,
            '-ar', '16000', '-ac', '1', '-c:a', 'pcm_s16le',
            audio_path, '-y', '-loglevel', 'quiet'
        ]
        subprocess.run(cmd)
        return audio_path
        
    def gerar_legenda_pt(self, audio_path, video_nome):
        """Gera legenda em português usando Whisper"""
        try:
            from faster_whisper import WhisperModel
            
            self.log("🤖 Processando áudio com IA (português)...", 'amarelo')
            
            # Carregar modelo (pequeno para velocidade)
            model = WhisperModel("small", device="cpu", compute_type="int8")
            
            # Transcrever
            segments, info = model.transcribe(audio_path, language="pt", beam_size=5)
            
            # Criar arquivo SRT
            srt_path = f"{self.legendas_dir}/PT/{video_nome}.pt.srt"
            
            with open(srt_path, 'w', encoding='utf-8') as f:
                for i, segment in enumerate(segments, start=1):
                    start = self.format_tempo(segment.start)
                    end = self.format_tempo(segment.end)
                    text = segment.text.strip()
                    
                    f.write(f"{i}\n")
                    f.write(f"{start} --> {end}\n")
                    f.write(f"{text}\n\n")
                    
            self.log(f"✅ Legenda PT gerada: {srt_path}")
            return srt_path
            
        except Exception as e:
            self.log(f"❌ Erro na geração PT: {e}", 'amarelo')
            return None
            
    def traduzir_para_ingles(self, srt_pt_path, video_nome):
        """Traduz legenda do português para inglês"""
        try:
            import openai
            
            self.log("🌎 Traduzindo para inglês...", 'azul')
            
            # Ler legenda PT
            with open(srt_pt_path, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                
            # Dividir em blocos para não exceder limite
            blocos = conteudo.split('\n\n')
            blocos_traduzidos = []
            
            # Traduzir cada bloco
            for bloco in blocos:
                if not bloco.strip():
                    continue
                    
                linhas = bloco.split('\n')
                if len(linhas) >= 3:
                    numero = linhas[0]
                    tempo = linhas[1]
                    texto = ' '.join(linhas[2:])
                    
                    # Aqui você usaria uma API de tradução
                    # Por simplicidade, vamos usar um dicionário simples
                    traducao = self.traduzir_texto(texto)
                    
                    blocos_traduzidos.append(f"{numero}\n{tempo}\n{traducao}")
                    
            # Salvar legenda EN
            srt_en_path = f"{self.legendas_dir}/EN/{video_nome}.en.srt"
            with open(srt_en_path, 'w', encoding='utf-8') as f:
                f.write('\n\n'.join(blocos_traduzidos))
                
            self.log(f"✅ Legenda EN gerada: {srt_en_path}")
            return srt_en_path
            
        except Exception as e:
            self.log(f"❌ Erro na tradução: {e}", 'amarelo')
            return None
            
    def traduzir_texto(self, texto):
        """Tradução simples (versão inicial)"""
        # Dicionário simples para demonstração
        # Em produção, use API do Google Translate ou OpenAI
        traducoes = {
            'Olá': 'Hello',
            'Mundo': 'World',
            'Bem-vindo': 'Welcome',
            'TVC Studios': 'TVC Studios',
            'Rio de Janeiro': 'Rio de Janeiro',
        }
        
        # Se não encontrar, mantém o original
        return traducoes.get(texto, texto)
        
    def gerar_legenda_completa(self, video_path):
        """Gera legendas PT e EN para um vídeo"""
        video_nome = Path(video_path).stem
        
        self.log(f"\n🎬 Processando: {video_nome}", 'negrito')
        
        # Extrair áudio
        audio_path = self.extrair_audio(video_path)
        
        # Gerar legenda PT
        srt_pt = self.gerar_legenda_pt(audio_path, video_nome)
        
        if srt_pt:
            # Traduzir para EN
            self.traduzir_para_ingles(srt_pt, video_nome)
            
        # Limpar arquivo temporário
        if os.path.exists(audio_path):
            os.remove(audio_path)
            
    def format_tempo(self, segundos):
        """Formata tempo para formato SRT (00:00:00,000)"""
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        segs = segundos % 60
        return f"{horas:02d}:{minutos:02d}:{segs:06.3f}".replace('.', ',')

if __name__ == "__main__":
    leg = TVCLegendas()
    
    # Processar vídeos da pasta Brutos
    brutos = os.path.expanduser("~/TVC4/TVC_STUDIOS/Brutos")
    
    for arquivo in os.listdir(brutos):
        if arquivo.lower().endswith('.mp4'):
            video_path = os.path.join(brutos, arquivo)
            leg.gerar_legenda_completa(video_path)
