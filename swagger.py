from flask import Blueprint, jsonify
from flask_swagger import swagger

swagger_bp = Blueprint('swagger', __name__)

@swagger_bp.route('/spec')
def spec():
    return jsonify(swagger(app))

@swagger_bp.route('/docs')
def docs():
    return render_template('swagger.html')
