#!/bin/bash
echo "🎬 TVC Studios - Plataforma Completa"
echo "===================================="

# Matar processos antigos
lsof -ti :5001 | xargs kill -9 2>/dev/null

# Iniciar backend
cd ~/TVC4/PLATAFORMA_WEB/backend
python3 app.py &

sleep 3

# Abrir no navegador
open http://localhost:5001

echo ""
echo "✅ Plataforma rodando!"
echo "📱 Acesse: http://localhost:5001"
echo ""
echo "📋 Projetos disponíveis:"
echo "   - CATIÇO (90%)"
echo "   - TEU SAMBA (30%)"
echo "   - TRÊM (45%)"
echo "   - COSTA VERDE (40%)"
echo "   - Ô POSTINHO (25%)"
echo ""
echo "🛠️  Módulos disponíveis:"
echo "   - HUD em Tempo Real"
echo "   - Dashboard Financeiro"
echo "   - Processador de Vídeos"
echo "   - Sistema de Legendas"
echo "   - Backup Automático"
