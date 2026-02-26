#!/bin/bash
while true
do
  python3 ~/TVC4/clima_rio.py
  echo "🌡️ Clima do Rio atualizado na grade."
  sleep 900 # Espera 15 minutos
done
