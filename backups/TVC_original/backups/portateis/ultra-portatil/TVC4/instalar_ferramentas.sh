#!/bin/bash
# Instalador de ferramentas essenciais para TVC Studios

echo "🚀 Instalando ferramentas essenciais..."

# 1. Homebrew (se não tiver)
if ! command -v brew &> /dev/null; then
    echo "📦 Instalando Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# 2. Ferramentas via Homebrew
echo "📦 Instalando ferramentas via Homebrew..."
brew install handbrake
brew install obs
brew install audacity
brew install gimp
brew install yt-dlp
brew install ffmpeg  # Reforçar instalação

# 3. Abrir páginas de download para as outras
echo "🌐 Abrindo páginas de download..."
open "https://www.blackmagicdesign.com/products/davinciresolve"
open "https://apps.apple.com/br/app/final-cut-pro/id424389933"
open "https://shotcut.org/"
open "https://handbrake.fr/"
open "https://whispernotes.app/pt"

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "Ferramentas instaladas via Homebrew:"
echo "  - HandBrake (conversor de vídeo)"
echo "  - OBS Studio (gravação de tela)"
echo "  - Audacity (edição de áudio)"
echo "  - GIMP (edição de imagem)"
echo "  - yt-dlp (download de vídeos)"
echo "  - ffmpeg (processamento de vídeo)"
echo ""
echo "Ferramentas com página aberta para download manual:"
echo "  - DaVinci Resolve (edição profissional)"
echo "  - Final Cut Pro (edição Mac)"
echo "  - Shotcut (editor leve)"
echo "  - Whisper Notes (transcrição)"
