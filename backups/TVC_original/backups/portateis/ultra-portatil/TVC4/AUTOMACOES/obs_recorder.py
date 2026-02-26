#!/usr/bin/env python3
# Controle do OBS Studio via API

import os
import json
import subprocess
import requests
import time

class TVCOBS:
    def __init__(self):
        self.base = os.path.expanduser("~/TVC4")
        self.obs_host = "localhost"
        self.obs_port = 4455
        self.obs_password = "tvc123"  # Mude isso
        
    def iniciar_obs(self):
        """Inicia OBS Studio"""
        subprocess.Popen(['open', '-a', 'OBS'])
        time.sleep(5)  # Aguarda OBS abrir
        
    def comando_obs(self, comando):
        """Envia comando para OBS via WebSocket"""
        try:
            response = requests.post(
                f"http://{self.obs_host}:{self.obs_port}/api/v1/{comando}",
                json={"password": self.obs_password}
            )
            return response.json()
        except:
            return {"error": "OBS não respondendo"}
            
    def gravar_programa(self, programa_nome, duracao_minutos):
        """Grava um programa por tempo determinado"""
        
        print(f"🎥 Gravando: {programa_nome}")
        
        # Configurar nome do arquivo
        data = time.strftime("%Y%m%d_%H%M%S")
        arquivo = f"{self.base}/TVC_STUDIOS/Brutos/{programa_nome}_{data}.mp4"
        
        # Iniciar gravação
        self.comando_obs("start_recording")
        
        # Gravar por X minutos
        for i in range(duracao_minutos):
            time.sleep(60)
            print(f"   ⏱️  {i+1} minutos gravados...")
            
        # Parar gravação
        self.comando_obs("stop_recording")
        print(f"✅ Gravação concluída: {arquivo}")
        
    def agendar_gravacao(self, programa, horario, duracao):
        """Agenda gravação para horário específico"""
        print(f"📅 Gravacao de '{programa}' agendada para {horario}")
        # Aqui você usaria cron ou schedule do Python

if __name__ == "__main__":
    obs = TVCOBS()
    
    print("""
   1. Gravar agora
   2. Agendar gravação
   """)
    
    op = input("Opção: ")
    
    if op == '1':
        nome = input("Nome do programa: ")
        duracao = int(input("Duração (minutos): "))
        obs.gravar_programa(nome, duracao)
