#!/bin/bash
PROJETO=$1
DATA=$(date +%Y%m%d_%H%M)
DIR_VERSOES=~/TVC4/NUCLEO_PRO/VERSOES_HISTORICO/

mkdir -p $DIR_VERSOES
cp ~/TVC4/NUCLEO_PRO/TEASER_$PROJETO.txt $DIR_VERSOES/TEASER_${PROJETO}_V_${DATA}.txt

echo "📜 Snapshot de roteiro criado para $PROJETO em $DATA"
