#!/bin/bash
# Instalador completo da TVC Studios

echo "🚀 Instalando TVC Studios - Sistema Completo"
echo "============================================="

# Criar estrutura de pastas
echo "📁 Criando estrutura de diretórios..."
mkdir -p ~/TVC4/{Assets,TVC_STUDIOS/{Brutos,Finalizados},GESTAO/{RELATORIOS},AUTOMACOES,BACKUPS}

# Instalar dependências Python
echo "🐍 Instalando dependências Python..."
pip3 install psutil watchdog 2>/dev/null || pip install psutil watchdog

# Verificar ffmpeg
echo "🎬 Verificando ffmpeg..."
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg não encontrado. Instale com: brew install ffmpeg"
else
    echo "✅ ffmpeg OK"
fi

# Dar permissão de execução
echo "🔧 Configurando permissões..."
chmod +x ~/TVC4/*.py 2>/dev/null
chmod +x ~/TVC4/GESTAO/*.py 2>/dev/null
chmod +x ~/TVC4/AUTOMACOES/*.py 2>/dev/null

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "Para iniciar o sistema:"
echo "  python3 ~/TVC4/tvc_manager.py"
echo ""
echo "Ou execute cada módulo separadamente:"
echo "  - HUD: python3 ~/TVC4/GESTAO/hud_tvc.py"
echo "  - Financeiro: python3 ~/TVC4/GESTAO/dashboard_financeiro.py"
echo "  - Projetos: python3 ~/TVC4/GESTAO/projetos.py"
echo "  - Backup: python3 ~/TVC4/AUTOMACOES/backup_automatico.py"
echo "  - Relatórios: python3 ~/TVC4/AUTOMACOES/relatorios_automaticos.py"
