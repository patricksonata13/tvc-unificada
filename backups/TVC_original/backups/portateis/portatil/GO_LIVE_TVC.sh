#!/bin/bash
echo "🚀 INICIANDO SEQUÊNCIA DE LANÇAMENTO TVC..."

# 1. Validação de Robustez
python3 ~/TVC4/HOLDING/COMPLIANCE/validador_producao.py

# 2. Desencriptação Temporária para Render (Segurança)
# (O script de Pós agora lida com os ficheiros .tvc)

# 3. Processamento e Upload
./~/TVC4/FECHAR_DIARIA_TVC.sh

# 4. Atualização de Valor de Mercado
python3 ~/TVC4/CORPORATIVO/ESTRATEGIA_EXPANSAO/relatorio_investidor.py

echo "✅ OPERAÇÃO CONCLUÍDA. A TVC ESTÁ NO TOPO."
