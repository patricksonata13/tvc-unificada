"""
TVC - TV CARIOCA
Estrutura Organizacional Completa com Hierarquia e Funções
"""

from flask import Flask, render_template, jsonify
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# ============================================
# HIERARQUIA ORGANIZACIONAL TVC
# ============================================

ORGANOGRAMA = {
    "holding": {
        "nome": "TVC - TV CARIOCA",
        "ceo": "Ana Paula Silveira",
        "fundacao": "2024",
        "missao": "Produzir conteúdo autêntico sobre o Rio de Janeiro",
        "visao": "Ser a maior plataforma de conteúdo carioca do Brasil",
        "valores": ["Autenticidade", "Diversidade", "Qualidade", "Inovação"]
    },
    "diretorias": [
        {
            "id": "escaleta",
            "nome": "Diretoria de Conteúdo",
            "diretor": "Carlos Alberto",
            "email": "carlos.alberto@tvc.com",
            "ramal": "101",
            "equipe": 12,
            "projetos_ativos": 23
        },
        {
            "id": "estudios",
            "nome": "Diretoria de Produção",
            "diretor": "Mariana Santos",
            "email": "mariana.santos@tvc.com",
            "ramal": "102",
            "equipe": 45,
            "projetos_ativos": 8
        },
        {
            "id": "jornalismo",
            "nome": "Diretoria de Jornalismo",
            "diretor": "Marcos Uchôa",
            "email": "marcos.uchoa@tvc.com",
            "ramal": "103",
            "equipe": 28,
            "projetos_ativos": 15
        },
        {
            "id": "esportes",
            "nome": "Diretoria de Esportes",
            "diretor": "Renato Maurício Prado",
            "email": "renato.prado@tvc.com",
            "ramal": "104",
            "equipe": 18,
            "projetos_ativos": 12
        },
        {
            "id": "master",
            "nome": "Diretoria Financeira",
            "diretor": "Roberto Carlos",
            "email": "roberto.carlos@tvc.com",
            "ramal": "105",
            "equipe": 8,
            "projetos_ativos": 6
        }
    ]
}

# ============================================
# EQUIPE COMPLETA POR DIRETORIA
# ============================================

EQUIPE = {
    "escaleta": [
        {"id": 1, "nome": "Carlos Alberto", "cargo": "Diretor de Conteúdo", "email": "carlos@tvc.com", "ramal": "101", "foto": "👨‍💼", "projetos": ["CATIÇO", "THE PUNCH"]},
        {"id": 2, "nome": "Ana Paula", "cargo": "Roteirista Chefe", "email": "ana@tvc.com", "ramal": "111", "foto": "👩‍💼", "projetos": ["TEU SAMBA", "TRÊM"]},
        {"id": 3, "nome": "Mariana Santos", "cargo": "Editora", "email": "mariana@tvc.com", "ramal": "112", "foto": "👩‍💻", "projetos": ["TRÊM", "CATIÇO"]},
        {"id": 4, "nome": "Paulo Roberto", "cargo": "Roteirista", "email": "paulo@tvc.com", "ramal": "113", "foto": "👨‍💻", "projetos": ["THE PUNCH"]},
        {"id": 5, "nome": "Fernanda Lima", "cargo": "Roteirista", "email": "fernanda@tvc.com", "ramal": "114", "foto": "👩‍🎨", "projetos": ["FESTA DA LAURA"]},
    ],
    "estudios": [
        {"id": 6, "nome": "Mariana Santos", "cargo": "Diretora de Produção", "email": "mariana.producao@tvc.com", "ramal": "102", "foto": "👩‍🎬", "projetos": ["CATIÇO", "TRÊM"]},
        {"id": 7, "nome": "Joel Zito Araújo", "cargo": "Diretor de Set", "email": "joel@tvc.com", "ramal": "121", "foto": "🎬", "projetos": ["CATIÇO"]},
        {"id": 8, "nome": "Walter Salles", "cargo": "Diretor de Fotografia", "email": "walter@tvc.com", "ramal": "122", "foto": "🎥", "projetos": ["TRÊM"]},
        {"id": 9, "nome": "Cacá Diegues", "cargo": "Diretor de Set", "email": "caca@tvc.com", "ramal": "123", "foto": "🎬", "projetos": ["TEU SAMBA"]},
        {"id": 10, "nome": "Lula Carvalho", "cargo": "Fotógrafo", "email": "lula@tvc.com", "ramal": "124", "foto": "📷", "projetos": ["TRÊM"]},
        {"id": 11, "nome": "Aline Marta", "cargo": "Atriz", "email": "aline@tvc.com", "ramal": "125", "foto": "🎭", "projetos": ["CATIÇO", "TRÊM"]},
        {"id": 12, "nome": "Lucas Penteado", "cargo": "Ator", "email": "lucas@tvc.com", "ramal": "126", "foto": "🎭", "projetos": ["CATIÇO", "TRÊM"]},
    ],
    "jornalismo": [
        {"id": 13, "nome": "Marcos Uchôa", "cargo": "Editor-Chefe", "email": "marcos.uchoa@tvc.com", "ramal": "103", "foto": "📰", "projetos": ["Jornal Rio", "Bom Dia Rio"]},
        {"id": 14, "nome": "Flávia Jannuzzi", "cargo": "Âncora", "email": "flavia@tvc.com", "ramal": "131", "foto": "🎙️", "projetos": ["Bom Dia Rio"]},
        {"id": 15, "nome": "Renata Capucci", "cargo": "Repórter", "email": "renata@tvc.com", "ramal": "132", "foto": "🎤", "projetos": ["RJ no Ar"]},
        {"id": 16, "nome": "Mariana Gross", "cargo": "Âncora", "email": "mariana.gross@tvc.com", "ramal": "133", "foto": "🎙️", "projetos": ["Edição de Sábado"]},
    ],
    "esportes": [
        {"id": 17, "nome": "Renato Maurício Prado", "cargo": "Diretor de Esportes", "email": "renato.prado@tvc.com", "ramal": "104", "foto": "⚽", "projetos": ["Mesa Redonda", "Radar Esportivo"]},
        {"id": 18, "nome": "Janio de Freitas", "cargo": "Comentarista", "email": "janio@tvc.com", "ramal": "141", "foto": "🎙️", "projetos": ["Resenha Flamengo"]},
        {"id": 19, "nome": "Alex Escobar", "cargo": "Comentarista", "email": "alex@tvc.com", "ramal": "142", "foto": "🎙️", "projetos": ["Mesa Redonda"]},
        {"id": 20, "nome": "Carol Barcellos", "cargo": "Repórter", "email": "carol@tvc.com", "ramal": "143", "foto": "🎤", "projetos": ["Vôlei Rio Show"]},
    ],
    "master": [
        {"id": 21, "nome": "Roberto Carlos", "cargo": "CFO", "email": "roberto.carlos@tvc.com", "ramal": "105", "foto": "💰", "projetos": ["Financeiro"]},
        {"id": 22, "nome": "Cristina Lemos", "cargo": "Contadora", "email": "cristina@tvc.com", "ramal": "151", "foto": "📊", "projetos": ["Contabilidade"]},
        {"id": 23, "nome": "Ricardo Silva", "cargo": "Analista Financeiro", "email": "ricardo@tvc.com", "ramal": "152", "foto": "📈", "projetos": ["Orçamentos"]},
    ]
}

# ============================================
# FERRAMENTAS POR DIRETORIA
# ============================================

FERRAMENTAS = {
    "escaleta": [
        {"id": 1, "nome": "Roteiro Digital", "descricao": "Editor de roteiros colaborativo", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Ana Paula"},
        {"id": 2, "nome": "Storyboard Pro", "descricao": "Criação de storyboards", "status": "Ativo", "ultimo_acesso": "20/02/2026", "responsavel": "Carlos Alberto"},
        {"id": 3, "nome": "Aprovação de Roteiros", "descricao": "Fluxo de aprovação", "status": "Ativo", "ultimo_acesso": "19/02/2026", "responsavel": "Mariana Santos"},
        {"id": 4, "nome": "Biblioteca de Roteiros", "descricao": "Acervo de roteiros finalizados", "status": "Ativo", "ultimo_acesso": "18/02/2026", "responsavel": "Paulo Roberto"},
    ],
    "estudios": [
        {"id": 5, "nome": "Agenda de Gravações", "descricao": "Calendário de sets", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Mariana Santos"},
        {"id": 6, "nome": "Controle de Equipamentos", "descricao": "Gestão de estoque", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Joel Zito"},
        {"id": 7, "nome": "Escala de Elenco", "descricao": "Disponibilidade de atores", "status": "Ativo", "ultimo_acesso": "20/02/2026", "responsavel": "Walter Salles"},
        {"id": 8, "nome": "Orçamento de Produção", "descricao": "Controle de gastos por set", "status": "Ativo", "ultimo_acesso": "19/02/2026", "responsavel": "Cacá Diegues"},
        {"id": 9, "nome": "Checklist de Set", "descricao": "Lista de verificação pré-gravação", "status": "Ativo", "ultimo_acesso": "18/02/2026", "responsavel": "Lula Carvalho"},
    ],
    "jornalismo": [
        {"id": 10, "nome": "Pautas Diárias", "descricao": "Sugestões de pautas", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Marcos Uchôa"},
        {"id": 11, "nome": "Editor de Texto", "descricao": "Edição colaborativa", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Flávia Jannuzzi"},
        {"id": 12, "nome": "Linha do Tempo", "descricao": "Cronologia de notícias", "status": "Ativo", "ultimo_acesso": "20/02/2026", "responsavel": "Renata Capucci"},
        {"id": 13, "nome": "Apuração", "descricao": "Ferramenta de checagem", "status": "Ativo", "ultimo_acesso": "19/02/2026", "responsavel": "Mariana Gross"},
    ],
    "esportes": [
        {"id": 14, "nome": "Escala de Jogos", "descricao": "Calendário esportivo", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Renato Maurício Prado"},
        {"id": 15, "nome": "Estatísticas ao Vivo", "descricao": "Dados em tempo real", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Janio de Freitas"},
        {"id": 16, "nome": "Escala de Comentaristas", "descricao": "Agenda da equipe", "status": "Ativo", "ultimo_acesso": "20/02/2026", "responsavel": "Alex Escobar"},
        {"id": 17, "nome": "Banco de Imagens", "descricao": "Acervo de jogos", "status": "Ativo", "ultimo_acesso": "19/02/2026", "responsavel": "Carol Barcellos"},
    ],
    "master": [
        {"id": 18, "nome": "Fluxo de Caixa", "descricao": "Controle financeiro", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Roberto Carlos"},
        {"id": 19, "nome": "Orçamento por Projeto", "descricao": "Acompanhamento", "status": "Ativo", "ultimo_acesso": "21/02/2026", "responsavel": "Cristina Lemos"},
        {"id": 20, "nome": "Relatórios Gerenciais", "descricao": "Dashboards financeiros", "status": "Ativo", "ultimo_acesso": "20/02/2026", "responsavel": "Ricardo Silva"},
        {"id": 21, "nome": "Previsão Orçamentária", "descricao": "Projeções", "status": "Ativo", "ultimo_acesso": "19/02/2026", "responsavel": "Roberto Carlos"},
    ]
}

# ============================================
# PRAZOS E ENTREGAS POR PROJETO
# ============================================

PRAZOS = [
    {"id": 1, "projeto": "CATIÇO", "fase": "Pós-produção", "entrega": "30/06/2026", "status": "Em dia", "progresso": 90, "responsavel": "Carlos Alberto", "prioridade": "Alta"},
    {"id": 2, "projeto": "TEU SAMBA", "fase": "Pré-produção", "entrega": "05/06/2026", "status": "Em dia", "progresso": 30, "responsavel": "Ana Paula", "prioridade": "Média"},
    {"id": 3, "projeto": "TRÊM", "fase": "Desenvolvimento", "entrega": "15/08/2026", "status": "Atenção", "progresso": 45, "responsavel": "Mariana Santos", "prioridade": "Alta"},
    {"id": 4, "projeto": "THE PUNCH", "fase": "Roteiro", "entrega": "30/09/2026", "status": "Em dia", "progresso": 15, "responsavel": "Paulo Roberto", "prioridade": "Baixa"},
    {"id": 5, "projeto": "Jornal Rio", "fase": "Diário", "entrega": "22/02/2026", "status": "Entregue", "progresso": 100, "responsavel": "Marcos Uchôa", "prioridade": "Alta"},
    {"id": 6, "projeto": "Bom Dia Rio", "fase": "Diário", "entrega": "22/02/2026", "status": "Entregue", "progresso": 100, "responsavel": "Flávia Jannuzzi", "prioridade": "Alta"},
]

# ============================================
# PROJETOS POR DIRETORIA
# ============================================

PROJETOS_POR_DIRETORIA = {
    "escaleta": [
        {"id": 1, "nome": "CATIÇO", "tipo": "Filme", "status": "Em produção", "prazo": "30/06/2026", "equipe": ["Carlos Alberto", "Aline Marta", "Lucas Penteado"]},
        {"id": 2, "nome": "TEU SAMBA", "tipo": "Novela", "status": "Pré-produção", "prazo": "05/06/2026", "equipe": ["Ana Paula", "Diogo Nogueira"]},
        {"id": 3, "nome": "TRÊM", "tipo": "Série", "status": "Desenvolvimento", "prazo": "15/08/2026", "equipe": ["Mariana Santos", "Aline Marta"]},
        {"id": 4, "nome": "THE PUNCH", "tipo": "Filme", "status": "Roteiro", "prazo": "30/09/2026", "equipe": ["Paulo Roberto"]},
    ],
    "estudios": [
        {"id": 5, "nome": "Gravação CATIÇO", "tipo": "Set", "status": "Agendado", "prazo": "25/02/2026", "equipe": ["Joel Zito", "Aline Marta"]},
        {"id": 6, "nome": "Gravação TRÊM", "tipo": "Set", "status": "Agendado", "prazo": "27/02/2026", "equipe": ["Walter Salles", "Lucas Penteado"]},
    ],
    "jornalismo": [
        {"id": 7, "nome": "Jornal Rio", "tipo": "Telejornal", "status": "Diário", "prazo": "22/02/2026", "equipe": ["Marcos Uchôa"]},
        {"id": 8, "nome": "Bom Dia Rio", "tipo": "Telejornal", "status": "Diário", "prazo": "22/02/2026", "equipe": ["Flávia Jannuzzi"]},
    ],
    "esportes": [
        {"id": 9, "nome": "Resenha Flamengo", "tipo": "Programa", "status": "Semanal", "prazo": "23/02/2026", "equipe": ["Janio de Freitas"]},
        {"id": 10, "nome": "Mesa Redonda", "tipo": "Programa", "status": "Semanal", "prazo": "24/02/2026", "equipe": ["Renato Maurício Prado", "Alex Escobar"]},
    ]
}

# ============================================
# ROTAS DA API
# ============================================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/organograma')
def api_organograma():
    return jsonify(ORGANOGRAMA)

@app.route('/api/equipe/<diretoria>')
def api_equipe(diretoria):
    return jsonify(EQUIPE.get(diretoria, []))

@app.route('/api/ferramentas/<diretoria>')
def api_ferramentas(diretoria):
    return jsonify(FERRAMENTAS.get(diretoria, []))

@app.route('/api/prazos')
def api_prazos():
    return jsonify(PRAZOS)

@app.route('/api/prazos/diretoria/<diretoria>')
def api_prazos_diretoria(diretoria):
    projetos = PROJETOS_POR_DIRETORIA.get(diretoria, [])
    return jsonify(projetos)

@app.route('/api/tudo')
def api_tudo():
    return jsonify({
        'organograma': ORGANOGRAMA,
        'equipe': EQUIPE,
        'ferramentas': FERRAMENTAS,
        'prazos': PRAZOS,
        'projetos_por_diretoria': PROJETOS_POR_DIRETORIA,
        'stats': {
            'total_funcionarios': sum(len(e) for e in EQUIPE.values()),
            'total_projetos': len(PRAZOS),
            'total_ferramentas': sum(len(f) for f in FERRAMENTAS.values()),
            'ultima_atualizacao': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    })

if __name__ == '__main__':
    print('\n' + '='*70)
    print(' 🏢 TVC - TV CARIOCA (ESTRUTURA ORGANIZACIONAL) '.center(70, '•'))
    print('='*70)
    print('\n📊 ESTATÍSTICAS:')
    print(f'   👥 Total de Funcionários: {sum(len(e) for e in EQUIPE.values())}')
    print(f'   📋 Total de Projetos: {len(PRAZOS)}')
    print(f'   🛠️ Total de Ferramentas: {sum(len(f) for f in FERRAMENTAS.values())}')
    print(f'   🏢 Diretorias: 5')
    print('\n' + '='*70)
    print('🚀 Servidor: http://localhost:5000')
    print('🎨 Cores: Areia • Cinza • Amarelo')
    print('='*70 + '\n')
    app.run(debug=True, port=5000)
