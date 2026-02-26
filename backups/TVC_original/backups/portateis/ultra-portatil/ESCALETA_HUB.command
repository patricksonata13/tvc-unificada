#!/bin/bash
echo "📋 Iniciando ESCALETA HUB - Sistema de Gestão"
pkill -f python
cd ~/ESCALETA_HUB/PLATAFORMA_WEB/backend
python3 app.py &
sleep 3
open http://localhost:5001
echo "✅ Escaleta Hub rodando em http://localhost:5001"
