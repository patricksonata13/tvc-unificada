"""
TVC - TV Carioca | Plataforma de Gestão
"""
from flask import Flask, render_template, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# ==================== ESCALETA HUB — 17 PROJETOS ====================
ESCALETA_PROJETOS = [
    {"id": 1, "nome": "CATIÇO", "tipo": "Filme", "status": "Pós-produção", "progresso": 90,
     "visao": "Comunidades", "responsavel": "Carlos Alberto", "orcamento": 800000,
     "descricao": "Cidade de Deus, anos 90. Jovem negro se torna bandido famoso."},
    {"id": 2, "nome": "TEU SAMBA", "tipo": "Novela", "status": "Pré-produção", "progresso": 30,
     "visao": "Cultural", "responsavel": "Ana Paula", "orcamento": 410000,
     "descricao": "Jovem sambista busca sucesso enfrentando tradição."},
    {"id": 3, "nome": "TRÊM", "tipo": "Série", "status": "Desenvolvimento", "progresso": 45,
     "visao": "Comunidades", "responsavel": "Mariana Santos", "orcamento": 1200000,
     "descricao": "Jovens formam grupo de dança no trem."},
    {"id": 4, "nome": "THE PUNCH", "tipo": "Filme", "status": "Roteiro", "progresso": 15,
     "visao": "Zona Oeste", "responsavel": "Paulo Roberto", "orcamento": 600000,
     "descricao": "Após um soco viral, homem tenta reconstruir sua vida."},
    {"id": 5, "nome": "A PRINCESA PERDIDA", "tipo": "Filme", "status": "Pré-produção", "progresso": 25,
     "visao": "Zona Sul", "responsavel": "Carla Dias", "orcamento": 750000,
     "descricao": "Angolana rica foge de casamento arranjado."},
    {"id": 6, "nome": "FESTA DA LAURA", "tipo": "Filme", "status": "Roteiro", "progresso": 20,
     "visao": "Comunidades", "responsavel": "Fernanda Lima", "orcamento": 550000,
     "descricao": "Mãe prepara festa extravagante na Cidade de Deus."},
    {"id": 7, "nome": "CORINHO DE FOGO", "tipo": "Filme", "status": "Desenvolvimento", "progresso": 10,
     "visao": "Cultural", "responsavel": "Marcelo Santos", "orcamento": 450000,
     "descricao": "Cantor gospel sem unção tenta voltar ao estrelato."},
    {"id": 8, "nome": "DIFERENTE MAS NEM TANTO", "tipo": "Série", "status": "Roteiro", "progresso": 35,
     "visao": "Zona Oeste", "responsavel": "Luciana Mello", "orcamento": 1500000,
     "descricao": "Família negra de Madureira enfrenta preconceitos."},
    {"id": 9, "nome": "O MATUTO", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 25,
     "visao": "Comunidades", "responsavel": "Ricardo Silva", "orcamento": 300000,
     "descricao": "Homem comum esconde identidade secreta no crime."},
    {"id": 10, "nome": "COSTA VERDE", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 40,
     "visao": "Litoral", "responsavel": "Patricia Costa", "orcamento": 350000,
     "descricao": "Conflito entre praias e florestas."},
    {"id": 11, "nome": "VIADUTO", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 15,
     "visao": "Cultural", "responsavel": "André Luiz", "orcamento": 280000,
     "descricao": "Forças ancestrais e tecnologia sob o viaduto."},
    {"id": 12, "nome": "VARRE SAI", "tipo": "Mini Novela", "status": "Pré-produção", "progresso": 50,
     "visao": "Comunidades", "responsavel": "Cristina Lemos", "orcamento": 320000,
     "descricao": "Comunidade enfrenta desafios com solidariedade."},
    {"id": 13, "nome": "UM VERÃO EM ARRAIAL", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 30,
     "visao": "Litoral", "responsavel": "João Paulo", "orcamento": 380000,
     "descricao": "Paixões intensas em Arraial do Cabo."},
    {"id": 14, "nome": "LETRA 7", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 20,
     "visao": "Centro", "responsavel": "Marcos Vinicius", "orcamento": 290000,
     "descricao": "Estelionatários digitais veem império ruir."},
    {"id": 15, "nome": "Ô POSTINHO", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 15,
     "visao": "Cotidiano", "responsavel": "Amanda Souza", "orcamento": 260000,
     "descricao": "Posto de saúde caótico da favela."},
    {"id": 16, "nome": "IMPÉRIO DE PEDRA", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 25,
     "visao": "Zona Sul", "responsavel": "Roberto Carlos", "orcamento": 400000,
     "descricao": "Família do Vidigal tenta se adaptar ao Leblon."},
    {"id": 17, "nome": "MEIA TROCADA", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 10,
     "visao": "Comunidades", "responsavel": "Thiago Mendes", "orcamento": 270000,
     "descricao": "Homem divorciado vira síndico no Vidigal."},
]

# ==================== JORNALISMO ====================
JORNALISMO_NOTICIAS = [
    {"id": 1, "titulo": "Prefeitura anuncia edital de cultura de R$ 1 milhão",
     "categoria": "Cidade", "data": "21/02/2026", "autor": "Redação",
     "conteudo": "RioFilme lança edital para produção de curtas e webséries.", "views": 1234},
    {"id": 2, "titulo": "Madureira recebe festival de samba com 20 escolas",
     "categoria": "Cultura", "data": "20/02/2026", "autor": "Redação",
     "conteudo": "Evento reúne as principais escolas de samba do Rio.", "views": 892},
    {"id": 3, "titulo": "Flamengo vence clássico por 3x1 no Maracanã",
     "categoria": "Esportes", "data": "19/02/2026", "autor": "Redação Esportes",
     "conteudo": "Rubro-negro assume liderança do campeonato.", "views": 2156},
]

# ==================== ESPORTES ====================
ESPORTES_CLUBES = [
    {"id": 1, "nome": "Flamengo", "estadio": "Maracanã", "tecnico": "Tite", "titulos": 38},
    {"id": 2, "nome": "Fluminense", "estadio": "Maracanã", "tecnico": "Diniz", "titulos": 33},
    {"id": 3, "nome": "Vasco", "estadio": "São Januário", "tecnico": "Carille", "titulos": 26},
    {"id": 4, "nome": "Botafogo", "estadio": "Nilton Santos", "tecnico": "Artur Jorge", "titulos": 21},
]

BRASILEIRAO = [
    {"pos": 1, "time": "Flamengo", "pontos": 38},
    {"pos": 2, "time": "Botafogo", "pontos": 36},
    {"pos": 3, "time": "Palmeiras", "pontos": 34},
    {"pos": 4, "time": "Fluminense", "pontos": 32},
]

PROXIMOS_JOGOS = [
    {"id": 1, "data": "22/02", "time_casa": "Flamengo", "time_fora": "Fluminense", "local": "Maracanã"},
    {"id": 2, "data": "23/02", "time_casa": "Vasco", "time_fora": "Botafogo", "local": "São Januário"},
]

# ==================== ESTÚDIOS ====================
EQUIPAMENTOS = [
    {"id": 1, "nome": "Câmera RED", "tipo": "Câmera", "quantidade": 3, "disponiveis": 2},
    {"id": 2, "nome": "Kit Iluminação", "tipo": "Iluminação", "quantidade": 5, "disponiveis": 3},
]

FUNCIONARIOS = [
    {"id": 1, "nome": "Carlos Alberto", "funcao": "Diretor", "disponibilidade": "Ocupado"},
    {"id": 2, "nome": "Ana Paula", "funcao": "Produtora", "disponibilidade": "Ocupada"},
]

# ==================== MASTER ====================
MASTER_FINANCEIRO = {
    "equity_brl": 8240000,
    "equity_usd": 1650000,
    "receitas_2026": 12400000,
    "despesas_2026": 8900000,
    "lucro_2026": 3500000,
}

def get_status():
    return {
        "cpu": random.randint(30, 70),
        "memoria": random.randint(40, 80),
        "disco": 78,
    }

# ==================== ROTAS ====================
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/tudo')
def api_tudo():
    return jsonify({
        'escaleta': ESCALETA_PROJETOS,
        'jornalismo': JORNALISMO_NOTICIAS,
        'esportes': ESPORTES_CLUBES,
        'brasileirao': BRASILEIRAO,
        'jogos': PROXIMOS_JOGOS,
        'equipamentos': EQUIPAMENTOS,
        'funcionarios': FUNCIONARIOS,
        'financeiro': MASTER_FINANCEIRO,
        'status': get_status(),
        'stats': {
            'projetos': len(ESCALETA_PROJETOS),
            'noticias': len(JORNALISMO_NOTICIAS),
            'clubes': len(ESPORTES_CLUBES),
        }
    })

if __name__ == '__main__':
    print('\n' + '='*60)
    print(' TVC - TV Carioca (ORIGINAL) '.center(60, '='))
    print('='*60)
    print(f'  Projetos: {len(ESCALETA_PROJETOS)}')
    print(f'  Notícias: {len(JORNALISMO_NOTICIAS)}')
    print(f'  Clubes: {len(ESPORTES_CLUBES)}')
    print('='*60)
    print('  Acesse: http://localhost:5000')
    print('='*60 + '\n')
    app.run(debug=True, port=5000)
