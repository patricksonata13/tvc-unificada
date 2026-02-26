#!/bin/bash
# Script para rodar Whisper em Docker

echo "🐳 Iniciando Whisper em Docker..."

# Criar pasta para legendas
mkdir -p ~/TVC4/TVC_STUDIOS/LEGENDAS/{PT,EN}

# Processar cada vídeo da pasta Brutos
for video in ~/TVC4/TVC_STUDIOS/Brutos/*.mp4; do
    if [ -f "$video" ]; then
        nome=$(basename "$video" .mp4)
        echo "🎬 Processando: $nome"
        
        # Rodar Whisper em Docker
        docker run --rm -v ~/TVC4/TVC_STUDIOS/Brutos:/data:ro \
            -v ~/TVC4/TVC_STUDIOS/LEGENDAS/PT:/output \
            onerahmet/openai-whisper-asr-webservice:latest \
            whisper /data/$(basename "$video") --model tiny --language pt --output_dir /output --output_format srt
            
        echo "✅ Legenda criada para $nome"
    fi
done

echo "✅ Processamento concluído!"
