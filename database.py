import sqlite3
import os
from modulos.escaleta.escaleta import ESCALETA_PROJETOS
from modulos.jornalismo.jornalismo import JORNALISMO_NOTICIAS
from modulos.esportes.esportes import ESPORTES_CLUBES, BRASILEIRAO, CARIOCA
from modulos.estudios.estudios import EQUIPE, EQUIPAMENTOS, MATERIAIS, FLUXO, AGENDA, ESCALAS
from modulos.financeiro.financeiro import MASTER_FINANCEIRO

DB_PATH = 'tvc.db'

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    """Cria as tabelas se não existirem."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escaleta (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            tipo TEXT,
            status TEXT,
            progresso INTEGER,
            visao TEXT,
            responsavel TEXT,
            orcamento INTEGER,
            descricao TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jornalismo (
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            categoria TEXT,
            data TEXT,
            autor TEXT,
            conteudo TEXT,
            views INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clubes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            estadio TEXT,
            tecnico TEXT,
            titulos INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS brasileirao (
            pos INTEGER PRIMARY KEY,
            time TEXT,
            pontos INTEGER,
            jogos INTEGER,
            vitorias INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carioca (
            pos INTEGER PRIMARY KEY,
            time TEXT,
            pontos INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipe (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            funcao TEXT,
            area TEXT,
            contato TEXT,
            disponibilidade TEXT,
            projetos TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipamentos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            tipo TEXT,
            quantidade INTEGER,
            disponiveis INTEGER,
            status TEXT,
            localizacao TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS materiais (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            tipo TEXT,
            quantidade INTEGER,
            disponiveis INTEGER,
            unidade TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fluxo (
            id INTEGER PRIMARY KEY,
            projeto TEXT,
            tarefa TEXT,
            responsavel TEXT,
            prazo TEXT,
            status TEXT,
            prioridade TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agenda (
            id INTEGER PRIMARY KEY,
            data TEXT,
            evento TEXT,
            local TEXT,
            responsavel TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escalas (
            id INTEGER PRIMARY KEY,
            data TEXT,
            funcao TEXT,
            membro TEXT,
            local TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS financeiro (
            chave TEXT PRIMARY KEY,
            valor TEXT
        )
    ''')

    conn.commit()
    conn.close()

def populate_db():
    """Insere dados iniciais se as tabelas estiverem vazias, com tratamento de erros."""
    conn = get_connection()
    cursor = conn.cursor()

    # Escaleta
    cursor.execute("SELECT COUNT(*) FROM escaleta")
    if cursor.fetchone()[0] == 0 and ESCALETA_PROJETOS:
        for p in ESCALETA_PROJETOS:
            cursor.execute('''
                INSERT INTO escaleta (id, nome, tipo, status, progresso, visao, responsavel, orcamento, descricao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (p['id'], p['nome'], p['tipo'], p['status'], p['progresso'], p['visao'], p['responsavel'], p['orcamento'], p['descricao']))

    # Jornalismo
    cursor.execute("SELECT COUNT(*) FROM jornalismo")
    if cursor.fetchone()[0] == 0 and JORNALISMO_NOTICIAS:
        for n in JORNALISMO_NOTICIAS:
            cursor.execute('''
                INSERT INTO jornalismo (id, titulo, categoria, data, autor, conteudo, views)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (n['id'], n['titulo'], n['categoria'], n['data'], n['autor'], n['conteudo'], n['views']))

    # Clubes
    cursor.execute("SELECT COUNT(*) FROM clubes")
    if cursor.fetchone()[0] == 0 and ESPORTES_CLUBES:
        for c in ESPORTES_CLUBES:
            cursor.execute('''
                INSERT INTO clubes (id, nome, estadio, tecnico, titulos)
                VALUES (?, ?, ?, ?, ?)
            ''', (c['id'], c['nome'], c['estadio'], c['tecnico'], c['titulos']))

    # Brasileirão
    cursor.execute("SELECT COUNT(*) FROM brasileirao")
    if cursor.fetchone()[0] == 0 and BRASILEIRAO:
        for b in BRASILEIRAO:
            cursor.execute('''
                INSERT INTO brasileirao (pos, time, pontos, jogos, vitorias)
                VALUES (?, ?, ?, ?, ?)
            ''', (b['pos'], b['time'], b['pontos'], b['jogos'], b['vitorias']))

    # Carioca
    cursor.execute("SELECT COUNT(*) FROM carioca")
    if cursor.fetchone()[0] == 0 and CARIOCA:
        for c in CARIOCA:
            cursor.execute('''
                INSERT INTO carioca (pos, time, pontos)
                VALUES (?, ?, ?)
            ''', (c['pos'], c['time'], c['pontos']))

    # Equipe
    cursor.execute("SELECT COUNT(*) FROM equipe")
    if cursor.fetchone()[0] == 0 and EQUIPE:
        for e in EQUIPE:
            projetos_str = ','.join(e.get('projetos', [])) if e.get('projetos') else ''
            cursor.execute('''
                INSERT INTO equipe (id, nome, funcao, area, contato, disponibilidade, projetos)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (e['id'], e['nome'], e['funcao'], e['area'], e['contato'], e['disponibilidade'], projetos_str))

    # Equipamentos
    cursor.execute("SELECT COUNT(*) FROM equipamentos")
    if cursor.fetchone()[0] == 0 and EQUIPAMENTOS:
        for eq in EQUIPAMENTOS:
            cursor.execute('''
                INSERT INTO equipamentos (id, nome, tipo, quantidade, disponiveis, status, localizacao)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (eq['id'], eq['nome'], eq['tipo'], eq['quantidade'], eq['disponiveis'], eq['status'], eq['localizacao']))

    # Materiais
    cursor.execute("SELECT COUNT(*) FROM materiais")
    if cursor.fetchone()[0] == 0 and MATERIAIS:
        for m in MATERIAIS:
            cursor.execute('''
                INSERT INTO materiais (id, nome, tipo, quantidade, disponiveis, unidade)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (m['id'], m['nome'], m['tipo'], m['quantidade'], m['disponiveis'], m['unidade']))

    # Fluxo
    cursor.execute("SELECT COUNT(*) FROM fluxo")
    if cursor.fetchone()[0] == 0 and FLUXO:
        for f in FLUXO:
            cursor.execute('''
                INSERT INTO fluxo (id, projeto, tarefa, responsavel, prazo, status, prioridade)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (f['id'], f['projeto'], f['tarefa'], f['responsavel'], f['prazo'], f['status'], f['prioridade']))

    # Agenda (com proteção contra chaves faltantes)
    cursor.execute("SELECT COUNT(*) FROM agenda")
    if cursor.fetchone()[0] == 0 and AGENDA:
        for a in AGENDA:
            try:
                cursor.execute('''
                    INSERT INTO agenda (id, data, evento, local, responsavel)
                    VALUES (?, ?, ?, ?, ?)
                ''', (a['id'], a['data'], a['evento'], a['local'], a['responsavel']))
            except KeyError as e:
                print(f"Aviso: item de agenda com chave faltando: {e} - pulando")
                continue

    # Escalas (com proteção)
    cursor.execute("SELECT COUNT(*) FROM escalas")
    if cursor.fetchone()[0] == 0 and ESCALAS:
        for e in ESCALAS:
            try:
                cursor.execute('''
                    INSERT INTO escalas (id, data, funcao, membro, local)
                    VALUES (?, ?, ?, ?, ?)
                ''', (e['id'], e['data'], e['funcao'], e['membro'], e['local']))
            except KeyError as e:
                print(f"Aviso: item de escala com chave faltando: {e} - pulando")
                continue

    # Financeiro (chave-valor)
    cursor.execute("SELECT COUNT(*) FROM financeiro")
    if cursor.fetchone()[0] == 0 and MASTER_FINANCEIRO:
        for chave, valor in MASTER_FINANCEIRO.items():
            cursor.execute('''
                INSERT INTO financeiro (chave, valor)
                VALUES (?, ?)
            ''', (chave, str(valor)))

    conn.commit()
    conn.close()

def get_all_data():
    """Retorna um dicionário com todos os dados do banco."""
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    data = {}

    cursor.execute("SELECT * FROM escaleta")
    data['escaleta'] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM jornalismo")
    data['jornalismo'] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM clubes")
    data['esportes'] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM brasileirao ORDER BY pos")
    data['brasileirao'] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM carioca ORDER BY pos")
    data['carioca'] = [dict(row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM equipe")
    equipe = [dict(row) for row in cursor.fetchall()]
    for e in equipe:
        if 'projetos' in e and e['projetos']:
            e['projetos'] = e['projetos'].split(',') if e['projetos'] else []
    cursor.execute("SELECT * FROM equipamentos")
    equipamentos = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT * FROM materiais")
    materiais = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT * FROM fluxo")
    fluxo = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT * FROM agenda")
    agenda = [dict(row) for row in cursor.fetchall()]
    cursor.execute("SELECT * FROM escalas")
    escalas = [dict(row) for row in cursor.fetchall()]

    data['estudios'] = {
        'equipe': equipe,
        'equipamentos': equipamentos,
        'materiais': materiais,
        'fluxo': fluxo,
        'agenda': agenda,
        'escalas': escalas
    }

    cursor.execute("SELECT * FROM financeiro")
    financeiro = {}
    for row in cursor.fetchall():
        val = row['valor']
        try:
            if val.isdigit():
                val = int(val)
            else:
                val = float(val)
        except:
            pass
        financeiro[row['chave']] = val
    data['financeiro'] = financeiro

    data['stats'] = {
        'projetos': len(data['escaleta']),
        'noticias': len(data['jornalismo']),
        'clubes': len(data['esportes']),
        'equipe': len(equipe),
        'equipamentos': len(equipamentos),
        'materiais': len(materiais)
    }

    conn.close()
    return data

def init_logs_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT,
            acao TEXT,
            tabela TEXT,
            item_id TEXT,
            dados TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def registrar_log(usuario, acao, tabela, item_id=None, dados=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (usuario, acao, tabela, item_id, dados)
        VALUES (?, ?, ?, ?, ?)
    ''', (usuario, acao, tabela, str(item_id) if item_id else None, str(dados) if dados else None))
    conn.commit()
    conn.close()

# Inicialização do banco e criação da tabela de logs
if not os.path.exists(DB_PATH):
    init_db()
    populate_db()
else:
    # Apenas cria a tabela de logs se não existir
    init_logs_table()
