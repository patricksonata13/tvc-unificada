from flask import Flask, jsonify, render_template
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

try:
    from estudios import (
        EQUIPE, EQUIPAMENTOS, MATERIAIS, FLUXO, AGENDA, ESCALAS
    )
    print("✅ Importação bem-sucedida!")
    print(f"   EQUIPE: {len(EQUIPE)} itens")
    print(f"   EQUIPAMENTOS: {len(EQUIPAMENTOS)} itens")
    print(f"   MATERIAIS: {len(MATERIAIS)} itens")
    print(f"   FLUXO: {len(FLUXO)} itens")
    print(f"   AGENDA: {len(AGENDA)} itens")
    print(f"   ESCALAS: {len(ESCALAS)} itens")
except ImportError as e:
    print(f"❌ Erro na importação: {e}")
    EQUIPE = []
    EQUIPAMENTOS = []
    MATERIAIS = []
    FLUXO = []
    AGENDA = []
    ESCALAS = []

try:
    from master import MASTER_FINANCEIRO
except:
    MASTER_FINANCEIRO = {}

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# ===== Rotas da API =====
@app.route('/api/equipe')
def api_equipe():
    return jsonify(EQUIPE)

@app.route('/api/equipamentos')
def api_equipamentos():
    return jsonify(EQUIPAMENTOS)

@app.route('/api/materiais')
def api_materiais():
    return jsonify(MATERIAIS)

@app.route('/api/fluxo')
def api_fluxo():
    return jsonify(FLUXO)

@app.route('/api/agenda')
def api_agenda():
    return jsonify(AGENDA)

@app.route('/api/escalas')
def api_escalas():
    return jsonify(ESCALAS)

# Opcional: rota para roteiros (se existir)
try:
    from estudios import ROTEIROS
    @app.route('/api/roteiros')
    def api_roteiros():
        return jsonify(ROTEIROS)
except:
    pass

# Rota que retorna todos os dados de uma vez (útil para o frontend)
@app.route('/api/tudo')
def api_tudo():
    return jsonify({
        'equipe': EQUIPE,
        'equipamentos': EQUIPAMENTOS,
        'materiais': MATERIAIS,
        'fluxo': FLUXO,
        'agenda': AGENDA,
        'escalas': ESCALAS
    })

if __name__ == '__main__':
    print("\n🎥 Módulo Estúdios rodando em http://localhost:5004")
    app.run(debug=True, port=5004)
