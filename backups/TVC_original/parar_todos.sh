#!/bin/bash
echo "🛑 Parando todos os módulos TVC..."
for pidfile in /tmp/tvc_*.pid; do
    if [ -f "$pidfile" ]; then
        pid=$(cat "$pidfile")
        kill $pid 2>/dev/null && echo "   ✅ Parou processo $pid"
        rm "$pidfile"
    fi
done
echo "✅ Todos os módulos parados."
