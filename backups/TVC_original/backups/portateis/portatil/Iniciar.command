#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 Iniciando TVC Studios Portátil..."
python3 PLATAFORMA_WEB/backend/app.py &
sleep 2
open http://localhost:5001
wait
