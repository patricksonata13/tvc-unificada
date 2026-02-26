from flask import Flask, jsonify, render_template
import sys
sys.path.append('data')
try:
    from jornalismo import JORNALISMO_NOTICIAS
except ImportError:
    JORNALISMO_NOTICIAS = []
try:
    from esportes import ESPORTES_CLUBES, BRASILEIRAO, PROXIMOS_JOGOS, ARTILHEIROS
except ImportError:
    ESPORTES_CLUBES = []
    BRASILEIRAO = []
    PROXIMOS_JOGOS = []
    ARTILHEIROS = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/noticias')
def noticias():
    return jsonify(JORNALISMO_NOTICIAS)

@app.route('/api/clubes')
def clubes():
    return jsonify(ESPORTES_CLUBES)

@app.route('/api/brasileirao')
def brasileirao():
    return jsonify(BRASILEIRAO)

@app.route('/api/jogos')
def jogos():
    return jsonify(PROXIMOS_JOGOS)

@app.route('/api/artilheiros')
def artilheiros():
    return jsonify(ARTILHEIROS)

if __name__ == '__main__':
    print("\n🚀 Módulo Jornalismo/Esportes rodando em http://localhost:5001")
    app.run(debug=True, port=5003)
