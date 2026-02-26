#!/bin/bash
# Instalador completo - Ferramentas + Integrações

echo "🚀 INSTALADOR COMPLETO TVC STUDIOS"
echo "=================================="

# 1. Homebrew
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
brew install ffmpeg

# 3. Criar aliases
echo "🔧 Configurando aliases..."
echo 'alias tvchand="python3 ~/TVC4/AUTOMACOES/otimizar_handbrake.py"' >> ~/.zshrc
echo 'alias tvcdavinci="python3 ~/TVC4/AUTOMACOES/davinci_projects.py"' >> ~/.zshrc
echo 'alias tvcwhisper="python3 ~/TVC4/AUTOMACOES/whisper_integration.py"' >> ~/.zshrc
echo 'alias tvcoff="python3 ~/TVC4/AUTOMACOES/obs_recorder.py"' >> ~/.zshrc
echo 'alias tvcaud="python3 ~/TVC4/AUTOMACOES/audacity_processor.py"' >> ~/.zshrc
echo 'alias tvcmenu="python3 ~/TVC4/tvc_manager.py"' >> ~/.zshrc

source ~/.zshrc

# 4. Dar permissões
chmod +x ~/TVC4/AUTOMACOES/*.py
chmod +x ~/TVC4/GESTAO/*.py
chmod +x ~/TVC4/*.py

echo ""
echo "✅ INSTALAÇÃO COMPLETA!"
echo ""
echo "Comandos disponíveis:"
echo "  tvcmenu     - Menu principal"
echo "  tvchand     - Otimizar vídeos"
echo "  tvcdavinci  - Criar projeto DaVinci"
echo "  tvcwhisper  - Transcrição"
echo "  tvcoff      - Gravar com OBS"
echo "  tvcaud      - Editar áudio"
echo ""
echo "Para abrir ferramentas individuais:"
echo "  open -a DaVinci\\ Resolve"
echo "  open -a OBS"
echo "  open -a Audacity"
echo "  open -a GIMP"
