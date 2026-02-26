from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

# Cria o blueprint
auth_bp = Blueprint('auth', __name__)

# Cria o LoginManager e EXPORTA ele
login_manager = LoginManager()

# Configura a rota de login (para redirecionar quando necessário)
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Por favor, faça login para acessar esta página.'

# Simulação de usuários (em produção, use banco de dados)
USERS = {
    'admin': generate_password_hash('admin123'),  # senha: admin123
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in USERS and check_password_hash(USERS[username], password):
            user = User(username)
            login_user(user)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('admin.index'))
        else:
            flash('Usuário ou senha inválidos', 'error')

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('auth.login'))
