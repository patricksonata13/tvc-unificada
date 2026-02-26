#!/bin/bash
# Camada 1: Local (Trabalho)
# Camada 2: Arquivo Morto (Local de Segurança)
# Camada 3: Nuvem/Cloud (Simulado no diretório OUTBOUND)

SOURCE=~/TVC4/TVC_STUDIOS/Finalizados/
DEST_LOCAL=~/TVC4/TVC_STUDIOS/COFRE_ORIGINAIS/
DEST_CLOUD=~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/TVC_PLAY/

echo "🔐 Iniciando Backup de Alta Disponibilidade..."
rsync -av --progress $SOURCE $DEST_LOCAL
echo "☁️ Sincronizando com Servidor de Distribuição..."
rsync -av --progress $SOURCE $DEST_CLOUD

say -v Luciana "Diretor, backup redundante concluído. Dados blindados."
