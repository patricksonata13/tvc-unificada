import sqlite3
from flask import Blueprint, render_template, abort, redirect, url_for, request, flash
from flask_login import login_required, current_user
import crud
import database

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

MODULOS = {
    'escaleta': {'table': 'escaleta', 'id_field': 'id', 'nome': 'Escaleta'},
    'jornalismo': {'table': 'jornalismo', 'id_field': 'id', 'nome': 'Jornalismo'},
    'esportes': {'table': 'clubes', 'id_field': 'id', 'nome': 'Clubes (Esportes)'},
    'brasileirao': {'table': 'brasileirao', 'id_field': 'pos', 'nome': 'Brasileirão'},
    'carioca': {'table': 'carioca', 'id_field': 'pos', 'nome': 'Carioca'},
    'equipe': {'table': 'equipe', 'id_field': 'id', 'nome': 'Equipe (Estúdios)'},
    'equipamentos': {'table': 'equipamentos', 'id_field': 'id', 'nome': 'Equipamentos'},
    'materiais': {'table': 'materiais', 'id_field': 'id', 'nome': 'Materiais'},
    'fluxo': {'table': 'fluxo', 'id_field': 'id', 'nome': 'Fluxo'},
    'agenda': {'table': 'agenda', 'id_field': 'id', 'nome': 'Agenda'},
    'escalas': {'table': 'escalas', 'id_field': 'id', 'nome': 'Escalas'},
    'financeiro': {'table': 'financeiro', 'id_field': 'chave', 'nome': 'Financeiro (chave-valor)'},
}

@admin_bp.route('/')
@login_required
def index():
    return render_template('admin/index.html', modulos=MODULOS)

@admin_bp.route('/<modulo>')
@login_required
def list_items(modulo):
    if modulo not in MODULOS:
        abort(404)
    info = MODULOS[modulo]
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    offset = (page - 1) * per_page
    conn = database.get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {info['table']} LIMIT ? OFFSET ?", (per_page, offset))
    itens = [dict(row) for row in cursor.fetchall()]
    cursor.execute(f"SELECT COUNT(*) FROM {info['table']}")
    total = cursor.fetchone()[0]
    conn.close()
    total_pages = (total + per_page - 1) // per_page
    return render_template('admin/list.html', modulo=modulo, info=info, itens=itens, page=page, per_page=per_page, total_pages=total_pages, total=total)

@admin_bp.route('/<modulo>/novo', methods=['GET', 'POST'])
@login_required
def new_item(modulo):
    if modulo not in MODULOS:
        abort(404)
    info = MODULOS[modulo]
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            novo_id = crud.create_item(info['table'], data, info['id_field'])
            database.registrar_log(current_user.id, 'CREATE', info['table'], novo_id, str(data))
            flash('Item criado com sucesso!', 'success')
            return redirect(url_for('admin.list_items', modulo=modulo))
        except Exception as e:
            flash(f'Erro ao criar: {e}', 'error')
    # GET: exibe formulário vazio
    conn = database.get_connection()
    cursor = conn.execute(f"PRAGMA table_info({info['table']})")
    colunas = [row[1] for row in cursor.fetchall() if row[1] != info['id_field']]
    conn.close()
    return render_template('admin/edit.html', modulo=modulo, info=info, colunas=colunas, item=None)

@admin_bp.route('/<modulo>/<id>/editar', methods=['GET', 'POST'])
@login_required
def edit_item(modulo, id):
    if modulo not in MODULOS:
        abort(404)
    info = MODULOS[modulo]
    if request.method == 'POST':
        data = request.form.to_dict()
        try:
            crud.update_item(info['table'], info['id_field'], id, data)
            database.registrar_log(current_user.id, 'UPDATE', info['table'], id, str(data))
            flash('Item atualizado com sucesso!', 'success')
            return redirect(url_for('admin.list_items', modulo=modulo))
        except Exception as e:
            flash(f'Erro ao atualizar: {e}', 'error')
    item = crud.get_by_id(info['table'], info['id_field'], id)
    if not item:
        abort(404)
    conn = database.get_connection()
    cursor = conn.execute(f"PRAGMA table_info({info['table']})")
    colunas = [row[1] for row in cursor.fetchall() if row[1] != info['id_field']]
    conn.close()
    return render_template('admin/edit.html', modulo=modulo, info=info, colunas=colunas, item=item)

@admin_bp.route('/<modulo>/<id>/deletar', methods=['POST'])
@login_required
def delete_item(modulo, id):
    if modulo not in MODULOS:
        abort(404)
    info = MODULOS[modulo]
    try:
        item = crud.get_by_id(info['table'], info['id_field'], id)
        crud.delete_item(info['table'], info['id_field'], id)
        database.registrar_log(current_user.id, 'DELETE', info['table'], id, str(item) if item else None)
        flash('Item deletado com sucesso!', 'success')
    except Exception as e:
        flash(f'Erro ao deletar: {e}', 'error')
    return redirect(url_for('admin.list_items', modulo=modulo))
