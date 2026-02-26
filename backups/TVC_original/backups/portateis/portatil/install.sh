#!/bin/bash
# Instalador do TVC Studios

echo "╔══════════════════════════════════════════════╗"
echo "║     TVC Studios - Instalação Automática     ║"
echo "╚══════════════════════════════════════════════╝"
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado!"
    echo "Instale em: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"

# Instalar dependências
echo "📦 Instalando dependências..."
pip3 install flask flask-cors psutil > /dev/null 2>&1

# Criar estrutura
echo "📁 Criando estrutura de pastas..."
mkdir -p ~/TVC_STUDIOS/{Brutos,Finalizados,LEGENDAS}
mkdir -p ~/TVC_STUDIOS/LEGENDAS/{PT,EN}

# Copiar arquivos (assumindo que estão no mesmo diretório)
echo "📋 Copiando arquivos..."
cp -r ./* ~/TVC_STUDIOS/ 2>/dev/null || true

# Criar atalho
echo "🔧 Criando atalho..."
cat > ~/Desktop/"TVC Studios.command" << 'INNEREOF'
#!/bin/bash
cd ~/TVC_STUDIOS
python3 PLATAFORMA_WEB/backend/app.py &
sleep 2
open http://localhost:5001
wait
INNEREOF
chmod +x ~/Desktop/"TVC Studios.command"

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "Para iniciar:"
echo "  1. Clique no ícone 'TVC Studios' na área de trabalho"
echo "  2. Ou execute: cd ~/TVC_STUDIOS && python3 PLATAFORMA_WEB/backend/app.py"
echo "  3. Acesse: http://localhost:5001"
echo ""
