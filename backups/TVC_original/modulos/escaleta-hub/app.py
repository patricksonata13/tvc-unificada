from flask import Flask, jsonify, render_template
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

try:
    from escaleta import ESCALETA_PROJETOS
except ImportError:
    ESCALETA_PROJETOS = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/projetos')
def projetos():
    return jsonify(ESCALETA_PROJETOS)

if __name__ == '__main__':
    print("\n🎬 Escaleta Hub rodando em http://localhost:5001")
    app.run(debug=True, port=5001)
