#!/bin/bash
# Inicia a plataforma web da TVC

echo "🚀 Iniciando Plataforma TVC Studios"
echo "==================================="

# Matar processos antigos na porta 5001
echo "📡 Limpando porta 5001..."
lsof -ti :5001 | xargs kill -9 2>/dev/null

# Verificar se Flask está instalado
if ! python3 -c "import flask" 2>/dev/null; then
    echo "📦 Instalando Flask..."
    pip3 install flask flask-cors psutil
fi

# Ir para pasta do backend
cd ~/TVC4/PLATAFORMA_WEB/backend

# Iniciar backend em background
echo "🖥️  Iniciando backend (porta 5001)..."
python3 app.py > ~/TVC4/PLATAFORMA_WEB/backend.log 2>&1 &
BACKEND_PID=$!

# Aguardar backend iniciar
sleep 3

# Verificar se subiu
if curl -s http://127.0.0.1:5001/api/stats > /dev/null; then
    echo "✅ Backend OK!"
else
    echo "❌ ERRO: Backend não respondeu"
    cat ~/TVC4/PLATAFORMA_WEB/backend.log
    exit 1
fi

# Abrir frontend no navegador
echo "🌐 Abrindo frontend no navegador..."
open "http://localhost:5001"

echo ""
echo "✅ Plataforma iniciada!"
echo "   Backend PID: $BACKEND_PID"
echo "   Log: ~/TVC4/PLATAFORMA_WEB/backend.log"
echo "   Para parar: kill $BACKEND_PID"
echo ""
echo "Acesse: http://localhost:5001"
