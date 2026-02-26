#!/usr/bin/env python3
# Gera projetos para DaVinci Resolve automaticamente

import os
import json
import datetime
from pathlib import Path

class TVCDaVinci:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.davinci_dir = os.path.expanduser("~/Movies/DaVinci Resolve/Projects")
        os.makedirs(self.davinci_dir, exist_ok=True)
        
    def gerar_projeto(self, projeto_nome, arquivos):
        """Gera um arquivo de projeto para DaVinci Resolve"""
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Criar estrutura básica do projeto
        projeto = {
            "nome": projeto_nome,
            "criado": timestamp,
            "modificado": timestamp,
            "arquivos": [],
            "timeline": {
                "nome": "Timeline Principal",
                "duracao": 0,
                "clipes": []
            }
        }
        
        # Adicionar arquivos
        tempo = 0
        for i, arq in enumerate(arquivos):
            clip = {
                "id": i+1,
                "arquivo": arq,
                "inicio": tempo,
                "duracao": 10  # segundos (ideal seria ler do vídeo)
            }
            projeto["timeline"]["clipes"].append(clip)
            tempo += 10
            
        projeto["timeline"]["duracao"] = tempo
        
        # Salvar projeto
        projeto_path = f"{self.davinci_dir}/{projeto_nome}.drp"
        with open(projeto_path, 'w') as f:
            json.dump(projeto, f, indent=2)
            
        print(f"✅ Projeto DaVinci criado: {projeto_path}")
        return projeto_path
        
    def criar_projeto_do_dia(self):
        """Cria um projeto com os vídeos do dia"""
        data = datetime.datetime.now().strftime("%Y-%m-%d")
        finalizados = f"{self.base}/TVC_STUDIOS/Finalizados"
        
        videos = [f for f in os.listdir(finalizados) if f.endswith('.mp4')]
        
        if videos:
            self.gerar_projeto(f"TVC_Projeto_{data}", videos)
        else:
            print("📭 Nenhum vídeo encontrado")

if __name__ == "__main__":
    dv = TVCDaVinci()
    dv.criar_projeto_do_dia()
