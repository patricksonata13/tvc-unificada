#!/usr/bin/env python3
# Versão standalone do TVC Studios
import os
import sys
import webbrowser
import threading
import time
from pathlib import Path

# Adicionar caminho para encontrar os módulos
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def iniciar_servidor():
    from PLATAFORMA_WEB.backend.app import app
    app.run(host='0.0.0.0', port=5001, debug=False)

def abrir_navegador():
    time.sleep(2)
    webbrowser.open('http://localhost:5001')

if __name__ == '__main__':
    print("🚀 Iniciando TVC Studios...")
    threading.Thread(target=iniciar_servidor, daemon=True).start()
    threading.Thread(target=abrir_navegador, daemon=True).start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n👋 Encerrando...")
        sys.exit(0)
