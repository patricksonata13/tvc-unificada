from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_login import LoginManager, current_user
import database
from auth import auth_bp, login_manager
from admin import admin_bp
import crud
from flask_swagger import swagger
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'chave-super-secreta-tvc')
CORS(app)

# Inicializa o Flask-Login
login_manager.init_app(app)

# Registra os blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def home():
    return render_template('index.html', logged_in=current_user.is_authenticated)

@app.route('/api/tudo')
def api_tudo():
    dados = database.get_all_data()
    return jsonify(dados)

MODULOS = {
    'escaleta': {'table': 'escaleta', 'id_field': 'id'},
    'jornalismo': {'table': 'jornalismo', 'id_field': 'id'},
    'esportes': {'table': 'clubes', 'id_field': 'id'},
    'brasileirao': {'table': 'brasileirao', 'id_field': 'pos'},
    'carioca': {'table': 'carioca', 'id_field': 'pos'},
    'equipe': {'table': 'equipe', 'id_field': 'id'},
    'equipamentos': {'table': 'equipamentos', 'id_field': 'id'},
    'materiais': {'table': 'materiais', 'id_field': 'id'},
    'fluxo': {'table': 'fluxo', 'id_field': 'id'},
    'agenda': {'table': 'agenda', 'id_field': 'id'},
    'escalas': {'table': 'escalas', 'id_field': 'id'},
    'financeiro': {'table': 'financeiro', 'id_field': 'chave'},
}

@app.route('/api/<modulo>', methods=['GET'])
def listar(modulo):
    """
    Lista todos os itens de um módulo
    ---
    tags:
      - Módulos
    parameters:
      - name: modulo
        in: path
        type: string
        required: true
        description: "Nome do módulo (ex: jornalismo, escaleta)"
    responses:
      200:
        description: Lista de itens
        schema:
          type: array
          items:
            type: object
    """
    if modulo not in MODULOS:
        return jsonify({'erro': 'Módulo não encontrado'}), 404
    info = MODULOS[modulo]
    itens = crud.get_all(info['table'])
    return jsonify(itens)

@app.route('/api/<modulo>/<id>', methods=['GET'])
def buscar(modulo, id):
    """
    Busca um item específico por ID
    ---
    tags:
      - Módulos
    parameters:
      - name: modulo
        in: path
        type: string
        required: true
        description: "Nome do módulo"
      - name: id
        in: path
        type: string
        required: true
        description: "ID do item (ou chave primária)"
    responses:
      200:
        description: Item encontrado
        schema:
          type: object
      404:
        description: Item não encontrado
    """
    if modulo not in MODULOS:
        return jsonify({'erro': 'Módulo não encontrado'}), 404
    info = MODULOS[modulo]
    item = crud.get_by_id(info['table'], info['id_field'], id)
    if item is None:
        return jsonify({'erro': 'Item não encontrado'}), 404
    return jsonify(item)

@app.route('/api/<modulo>', methods=['POST'])
def criar(modulo):
    """
    Cria um novo item no módulo
    ---
    tags:
      - Módulos
    parameters:
      - name: modulo
        in: path
        type: string
        required: true
        description: "Nome do módulo"
      - name: body
        in: body
        required: true
        schema:
          type: object
          description: "Dados do item a ser criado"
    responses:
      201:
        description: Item criado
        schema:
          type: object
          properties:
            id:
              type: integer
            mensagem:
              type: string
      400:
        description: Dados inválidos
      404:
        description: Módulo não encontrado
    """
    if modulo not in MODULOS:
        return jsonify({'erro': 'Módulo não encontrado'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'erro': 'Dados inválidos'}), 400
    info = MODULOS[modulo]
    try:
        novo_id = crud.create_item(info['table'], data, info['id_field'])
        return jsonify({'id': novo_id, 'mensagem': 'Criado com sucesso'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/<modulo>/<id>', methods=['PUT'])
def atualizar(modulo, id):
    """
    Atualiza um item existente
    ---
    tags:
      - Módulos
    parameters:
      - name: modulo
        in: path
        type: string
        required: true
        description: "Nome do módulo"
      - name: id
        in: path
        type: string
        required: true
        description: "ID do item"
      - name: body
        in: body
        required: true
        schema:
          type: object
          description: "Dados a serem atualizados"
    responses:
      200:
        description: Item atualizado
        schema:
          type: object
          properties:
            mensagem:
              type: string
      400:
        description: Dados inválidos
      404:
        description: Item não encontrado
    """
    if modulo not in MODULOS:
        return jsonify({'erro': 'Módulo não encontrado'}), 404
    data = request.get_json()
    if not data:
        return jsonify({'erro': 'Dados inválidos'}), 400
    info = MODULOS[modulo]
    try:
        afetados = crud.update_item(info['table'], info['id_field'], id, data)
        if afetados == 0:
            return jsonify({'erro': 'Item não encontrado'}), 404
        return jsonify({'mensagem': 'Atualizado com sucesso'})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@app.route('/api/<modulo>/<id>', methods=['DELETE'])
def deletar(modulo, id):
    """
    Deleta um item
    ---
    tags:
      - Módulos
    parameters:
      - name: modulo
        in: path
        type: string
        required: true
        description: "Nome do módulo"
      - name: id
        in: path
        type: string
        required: true
        description: "ID do item"
    responses:
      200:
        description: Item deletado
        schema:
          type: object
          properties:
            mensagem:
              type: string
      404:
        description: Item não encontrado
    """
    if modulo not in MODULOS:
        return jsonify({'erro': 'Módulo não encontrado'}), 404
    info = MODULOS[modulo]
    try:
        afetados = crud.delete_item(info['table'], info['id_field'], id)
        if afetados == 0:
            return jsonify({'erro': 'Item não encontrado'}), 404
        return jsonify({'mensagem': 'Deletado com sucesso'})
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

# ==================== SWAGGER ====================
@app.route('/swagger/spec')
def swagger_spec():
    try:
        return jsonify(swagger(app))
    except Exception as e:
        print("\n*** ERRO no Swagger:", e, "\n")
        return jsonify({'erro': str(e)}), 500

@app.route('/swagger/docs')
def swagger_docs():
    return render_template('swagger.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("="*60)
    print("TVC UNIFICADO - Com autenticação e admin")
    print("="*60)
    app.run(debug=True, port=port)
