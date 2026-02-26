#!/bin/bash
clear
echo "⚔️ ATIVANDO PROTOCOLO OVERLORD v2.0 - TVC STUDIOS"
echo "-----------------------------------------------"

# 1. Lançar o Sentinel em Segundo Plano (Vigilância Invisível)
python3 ~/TVC4/OPERACIONAL/tvc_sentinel.py & 

# 2. Auto-Reparo e Backups
python3 ~/TVC4/CORPORATIVO/COMPLIANCE/tvc_self_heal.py
cp ~/TVC4/tvc_admin.db ~/TVC4/.system_logs/backup_$(date +%Y%m%d).db

# 3. Auditoria de Criptografia de Roteiros
python3 ~/TVC4/CORPORATIVO/COMPLIANCE/auditoria_seguranca.py

# 4. Voz Siri-Style High-End
say -v Luciana "Diretor, sentinelas ativos. O ecossistema TVC está agora em modo de defesa autónoma."

# 5. Lançar o HUD Central
python3 ~/TVC4/OPERACIONAL/HUD_TVC.py
