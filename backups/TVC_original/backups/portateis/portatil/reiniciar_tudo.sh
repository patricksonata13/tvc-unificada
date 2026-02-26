#!/bin/bash
# Reinicia toda a plataforma TVC

echo "🔄 Reiniciando TVC Studios - Plataforma Completa"
echo "================================================"

# Matar todos os processos Python na porta 5001
echo "📡 Liberando porta 5001..."
lsof -ti :5001 | xargs kill -9 2>/dev/null

# Matar qualquer outro processo Python relacionado
pkill -f "python.*app.py" 2>/dev/null

# Aguardar liberação
sleep 2

# Iniciar backend
echo "🚀 Iniciando backend Flask..."
cd ~/TVC4/PLATAFORMA_WEB/backend
python3 app.py > ~/TVC4/PLATAFORMA_WEB/backend.log 2>&1 &

# Aguardar inicialização
sleep 3

# Abrir no navegador
echo "🌐 Abrindo plataforma no navegador..."
open http://localhost:5001

# Mostrar status
echo ""
echo "✅ Plataforma reiniciada!"
echo "📱 Acesse: http://localhost:5001"
echo "📋 Logs: ~/TVC4/PLATAFORMA_WEB/backend.log"
echo ""
echo "📊 Status da API:"
curl -s http://localhost:5001/api/stats | python3 -m json.tool 2>/dev/null || echo "   Aguardando API responder..."
