#!/bin/bash
# Inicia o sistema TVC Unificado

cd "$(dirname "$0")"
source venv/bin/activate 2>/dev/null || python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt

# Mata processo na porta 5000 se existir
lsof -ti :5000 | xargs kill -9 2>/dev/null

echo "🚀 Iniciando TVC Unificado..."
python app.py &

sleep 3
open http://localhost:5000
