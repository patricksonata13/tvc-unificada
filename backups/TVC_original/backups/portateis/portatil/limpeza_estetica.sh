#!/bin/bash
echo "🧼 Organizando estética do diretório TVC4..."
mkdir -p ~/TVC4/.system_logs
mv ~/TVC4/*.log ~/TVC4/.system_logs/ 2>/dev/null
echo "✅ Ambiente clean."
