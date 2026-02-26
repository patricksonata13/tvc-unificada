from flask import Blueprint, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

docs_bp = Blueprint('docs', __name__)

# Rota para o arquivo swagger.json (especificação OpenAPI)
@docs_bp.route('/swagger.json')
def swagger_spec():
    spec = {
        "openapi": "3.0.0",
        "info": {
            "title": "TVC API",
            "description": "API unificada da TV Carioca",
            "version": "1.0.0"
        },
        "paths": {
            "/api/tudo": {
                "get": {
                    "summary": "Retorna todos os dados",
                    "responses": {
                        "200": {
                            "description": "Sucesso"
                        }
                    }
                }
            },
            "/api/{modulo}": {
                "get": {
                    "summary": "Lista itens de um módulo",
                    "parameters": [
                        {
                            "name": "modulo",
                            "in": "path",
                            "required": True,
                            "schema": {"type": "string"}
                        }
                    ],
                    "responses": {
                        "200": {"description": "Lista de itens"}
                    }
                },
                "post": {
                    "summary": "Cria um novo item",
                    "parameters": [...],
                    "responses": {
                        "201": {"description": "Criado com sucesso"}
                    }
                }
            }
            # ... (pode expandir depois)
        }
    }
    return jsonify(spec)

# Configurar Swagger UI
SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "TVC API"}
)
