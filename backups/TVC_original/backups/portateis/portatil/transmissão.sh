#!/bin/bash

# Substitua pela sua chave de transmissão do YouTube/Twitch
STREAM_KEY="SUA-CHAVE-AQUI"
RTMP_URL="rtmp://a.rtmp.youtube.com/live2"

echo "📡 TVC 4.0 - INICIANDO TRANSMISSÃO AO VIVO..."

ffmpeg -re -f concat -safe 0 -i ~/TVC4/grade.txt \
-c:v libx264 -preset veryfast -maxrate 3000k -bufsize 6000k \
-pix_fmt yuv420p -g 50 -c:a aac -b:a 128k \
-f flv "$RTMP_URL/$STREAM_KEY"
