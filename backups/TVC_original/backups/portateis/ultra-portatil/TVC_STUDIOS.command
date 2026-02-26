#!/bin/bash
echo "🎬 Iniciando TVC STUDIOS - Sistema de Produção"
pkill -f python
cd ~/TVC_STUDIOS/PLATAFORMA_WEB/backend
python3 app_tvc.py &
sleep 3
open http://localhost:5002
echo "✅ TVC Studios rodando em http://localhost:5002"
