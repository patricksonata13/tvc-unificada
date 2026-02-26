"""
TVC - TV Carioca | Plataforma de Gestão Modular
"""
from flask import Flask, render_template, jsonify
from datetime import datetime

# Importar dados
from data.escaleta import ESCALETA_PROJETOS
from data.jornalismo import JORNALISMO_NOTICIAS
from data.esportes import ESPORTES_CLUBES, BRASILEIRAO, CARIOCA, PROXIMOS_JOGOS, ARTILHEIROS
from data.estudios import ROTEIROS, EQUIPAMENTOS, FUNCIONARIOS
from data.master import MASTER_FINANCEIRO, get_status

app = Flask(__name__)

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
        'carioca': CARIOCA,
        'jogos': PROXIMOS_JOGOS,
        'artilheiros': ARTILHEIROS,
        'roteiros': ROTEIROS,
        'equipamentos': EQUIPAMENTOS,
        'funcionarios': FUNCIONARIOS,
        'financeiro': MASTER_FINANCEIRO,
        'status': get_status(),
        'stats': {
            'projetos': len(ESCALETA_PROJETOS),
            'noticias': len(JORNALISMO_NOTICIAS),
            'clubes': len(ESPORTES_CLUBES),
            'equipamentos': len(EQUIPAMENTOS),
            'funcionarios': len(FUNCIONARIOS),
            'ultima_atualizacao': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    })

if __name__ == '__main__':
    print('\n' + '='*60)
    print(' TVC - TV Carioca (MODULAR) '.center(60, '='))
    print('='*60)
    print(f'  Projetos: {len(ESCALETA_PROJETOS)}')
    print(f'  Notícias: {len(JORNALISMO_NOTICIAS)}')
    print(f'  Clubes: {len(ESPORTES_CLUBES)}')
    print(f'  Equipamentos: {len(EQUIPAMENTOS)}')
    print(f'  Funcionários: {len(FUNCIONARIOS)}')
    print('='*60)
    print('  Acesse: http://localhost:5000')
    print('='*60 + '\n')
    app.run(debug=True, port=5001)
