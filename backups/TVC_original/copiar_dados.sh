#!/bin/bash
echo "📦 Copiando dados da versão final para os módulos..."

# Estudios
cp ~/TVC/versoes/final/data/estudios.py ~/TVC/modulos/estudios/data/ 2>/dev/null
cp ~/TVC/versoes/final/data/master.py ~/TVC/modulos/estudios/data/ 2>/dev/null

# Jornalismo/Esportes
cp ~/TVC/versoes/final/data/jornalismo.py ~/TVC/modulos/jornalismo-esportes/data/ 2>/dev/null
cp ~/TVC/versoes/final/data/esportes.py ~/TVC/modulos/jornalismo-esportes/data/ 2>/dev/null

# Escaleta Hub (se existir)
cp ~/TVC/versoes/final/data/escaleta.py ~/TVC/modulos/escaleta-hub/data/ 2>/dev/null

echo "✅ Dados copiados. Reinicie os módulos com ~/TVC/parar_todos.sh && ~/TVC/iniciar_todos.sh"
