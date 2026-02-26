#!/bin/bash
# Inicia todos os serviços da TVC

echo "🚀 Iniciando TVC Studios - Todos os serviços"
echo "============================================="

# Iniciar watchdog em background
echo "📡 Iniciando Watchdog..."
python3 ~/TVC4/tvc_watchdog.py &
WATCHDOG_PID=$!
echo "   PID: $WATCHDOG_PID"

# Iniciar HUD em nova janela (se tiver Terminal)
if command -v open &> /dev/null; then
    # macOS
    osascript -e 'tell app "Terminal" to do script "python3 ~/TVC4/GESTAO/hud_tvc.py"'
else
    # Linux
    gnome-terminal -- python3 ~/TVC4/GESTAO/hud_tvc.py 2>/dev/null || \
    xterm -e python3 ~/TVC4/GESTAO/hud_tvc.py 2>/dev/null &
fi

echo ""
echo "✅ Serviços iniciados!"
echo ""
echo "Comandos úteis:"
echo "  - Ver processos: ps aux | grep python"
echo "  - Parar watchdog: kill $WATCHDOG_PID"
echo "  - Menu principal: python3 ~/TVC4/tvc_manager.py"
