#!/bin/bash
echo "--- FINALIZANDO OPERAÇÃO DIÁRIA TVC ---"
python3 ~/TVC4/OPERACIONAL/SQUAD_MANAGER/disparador_convocacao.py # Convoca para amanhã
python3 ~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/upload_tvc_play.py # Lança o de hoje
python3 ~/TVC4/tvc_dashboard_master.py                          # Atualiza Dashboard
echo "--- TUDO PRONTO, DIRETOR. DESCANCE. ---"
