#!/bin/bash
# Cores para output
VERDE='\033[0;32m'
AMARELO='\033[1;33m'
AZUL='\033[0;34m'
SEM_COR='\033[0m'

echo -e "${AZUL}========================================${SEM_COR}"
echo -e "${VERDE}🚀 TVC - Iniciando todos os módulos${SEM_COR}"
echo -e "${AZUL}========================================${SEM_COR}"

# Matar processos antigos
echo -e "${AMARELO}🔪 Matando processos antigos nas portas 5001-5004...${SEM_COR}"
for porta in 5001 5002 5003 5004; do
    lsof -ti :$porta | xargs kill -9 2>/dev/null
done

# Função para iniciar um módulo
iniciar_modulo() {
    local nome=$1
    local pasta=$2
    local porta=$3
    local cor=$4
    local nome_seguro=$(echo "$nome" | tr ' /' '_')

    if [ -d "$pasta" ]; then
        echo -e "${cor}📦 Iniciando $nome na porta $porta...${SEM_COR}"
        (cd "$pasta" && python3 app.py > /dev/null 2>&1) &
        local pid=$!
        echo $pid > "/tmp/tvc_${nome_seguro}.pid"
        echo -e "${VERDE}   ✅ $nome rodando em http://localhost:$porta (PID: $pid)${SEM_COR}"
    else
        echo -e "${AMARELO}⚠️  Pasta $nome não encontrada: $pasta${SEM_COR}"
    fi
}

# Iniciar módulos
iniciar_modulo "Escaleta Hub" "$HOME/TVC/modulos/escaleta-hub" 5001 "\033[0;36m"
iniciar_modulo "Software" "$HOME/TVC/modulos/software" 5002 "\033[0;35m"
iniciar_modulo "Jornalismo_Esportes" "$HOME/TVC/modulos/jornalismo-esportes" 5003 "\033[0;32m"
iniciar_modulo "Estudios" "$HOME/TVC/modulos/estudios" 5004 "\033[0;33m"

echo -e "${AZUL}========================================${SEM_COR}"
echo -e "${VERDE}✅ Todos os módulos iniciados!${SEM_COR}"
echo -e "${AZUL}========================================${SEM_COR}"
echo -e "📌 Acesse:"
echo -e "   Escaleta Hub:       ${VERDE}http://localhost:5001${SEM_COR}"
echo -e "   Software:           ${VERDE}http://localhost:5002${SEM_COR}"
echo -e "   Jornalismo/Esportes:${VERDE}http://localhost:5003${SEM_COR}"
echo -e "   Estúdios:           ${VERDE}http://localhost:5004${SEM_COR}"
echo -e "${AZUL}========================================${SEM_COR}"
