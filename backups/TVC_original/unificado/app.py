import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import Flask, jsonify, render_template
from flask_cors import CORS

# Configuração de logging
log_file = 'logs/tvc.log'
os.makedirs('logs', exist_ok=True)

handler = RotatingFileHandler(log_file, maxBytes=10_000_000, backupCount=5)
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
))
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.INFO)

# Importar dados (com tratamento de erro)
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
    from escaleta import ESCALETA_PROJETOS
    from jornalismo import JORNALISMO_NOTICIAS
    from esportes import (
        ESPORTES_CLUBES, BRASILEIRAO, CARIOCA,
        PROXIMOS_JOGOS, ARTILHEIROS
    )
    from estudios import (
        EQUIPE, EQUIPAMENTOS, MATERIAIS,
        FLUXO, AGENDA, ESCALAS
    )
    from master import MASTER_FINANCEIRO, get_status
    logging.info("✅ Dados importados com sucesso")
except Exception as e:
    logging.error(f"❌ Erro na importação: {e}")
    # Inicializa vazio para evitar crash
    ESCALETA_PROJETOS = []
    JORNALISMO_NOTICIAS = []
    ESPORTES_CLUBES = []
    BRASILEIRAO = []
    CARIOCA = []
    PROXIMOS_JOGOS = []
    ARTILHEIROS = []
    EQUIPE = []
    EQUIPAMENTOS = []
    MATERIAIS = []
    FLUXO = []
    AGENDA = []
    ESCALAS = []
    MASTER_FINANCEIRO = {}
    get_status = lambda: {}

app = Flask(__name__)
CORS(app)

# ==================== ROTAS ====================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'modules': {
            'escaleta': len(ESCALETA_PROJETOS) > 0,
            'jornalismo': len(JORNALISMO_NOTICIAS) > 0,
            'esportes': len(ESPORTES_CLUBES) > 0,
            'estudios': len(EQUIPE) > 0
        }
    })

@app.route('/api/tudo')
def api_tudo():
    return jsonify({
        'escaleta': ESCALETA_PROJETOS,
        'jornalismo': JORNALISMO_NOTICIAS,
        'esportes': {
            'clubes': ESPORTES_CLUBES,
            'brasileirao': BRASILEIRAO,
            'carioca': CARIOCA,
            'jogos': PROXIMOS_JOGOS,
            'artilheiros': ARTILHEIROS
        },
        'estudios': {
            'equipe': EQUIPE,
            'equipamentos': EQUIPAMENTOS,
            'materiais': MATERIAIS,
            'fluxo': FLUXO,
            'agenda': AGENDA,
            'escalas': ESCALAS
        },
        'master': {
            'financeiro': MASTER_FINANCEIRO,
            'status': get_status()
        },
        'stats': {
            'projetos': len(ESCALETA_PROJETOS),
            'noticias': len(JORNALISMO_NOTICIAS),
            'clubes': len(ESPORTES_CLUBES),
            'equipe': len(EQUIPE),
            'equipamentos': len(EQUIPAMENTOS),
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M')
        }
    })

# Rotas específicas (opcional, mas podem ser úteis)
@app.route('/api/escaleta/projetos')
def api_escaleta():
    return jsonify(ESCALETA_PROJETOS)

@app.route('/api/jornalismo/noticias')
def api_jornalismo():
    return jsonify(JORNALISMO_NOTICIAS)

@app.route('/api/esportes/clubes')
def api_clubes():
    return jsonify(ESPORTES_CLUBES)

@app.route('/api/esportes/brasileirao')
def api_brasileirao():
    return jsonify(BRASILEIRAO)

@app.route('/api/esportes/proximos_jogos')
def api_jogos():
    return jsonify(PROXIMOS_JOGOS)

@app.route('/api/estudios/equipe')
def api_equipe():
    return jsonify(EQUIPE)

@app.route('/api/estudios/equipamentos')
def api_equipamentos():
    return jsonify(EQUIPAMENTOS)

@app.route('/api/estudios/materiais')
def api_materiais():
    return jsonify(MATERIAIS)

@app.route('/api/estudios/fluxo')
def api_fluxo():
    return jsonify(FLUXO)

@app.route('/api/estudios/agenda')
def api_agenda():
    return jsonify(AGENDA)

@app.route('/api/estudios/escalas')
def api_escalas():
    return jsonify(ESCALAS)

@app.route('/api/master/financeiro')
def api_financeiro():
    return jsonify(MASTER_FINANCEIRO)

@app.route('/api/master/status')
def api_status():
    return jsonify(get_status())

if __name__ == '__main__':
    from config import Config
    logging.info(f"🚀 Iniciando TVC Unificado na porta {Config.PORT}")
    print(f"\n🚀 TVC Unificado rodando em http://localhost:{Config.PORT}")
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
