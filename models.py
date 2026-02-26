from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Escaleta(db.Model):
    __tablename__ = 'escaleta'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    status = db.Column(db.String(50))
    progresso = db.Column(db.Integer)
    visao = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))
    orcamento = db.Column(db.Integer)
    descricao = db.Column(db.Text)

class Jornalismo(db.Model):
    __tablename__ = 'jornalismo'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    categoria = db.Column(db.String(50))
    data = db.Column(db.String(20))
    autor = db.Column(db.String(100))
    conteudo = db.Column(db.Text)
    views = db.Column(db.Integer)

class Clube(db.Model):
    __tablename__ = 'clubes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    estadio = db.Column(db.String(100))
    tecnico = db.Column(db.String(100))
    titulos = db.Column(db.Integer)

class OutroTime(db.Model):
    __tablename__ = 'outros_times'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    estadio = db.Column(db.String(100))
    tecnico = db.Column(db.String(100))
    titulos = db.Column(db.Integer)

class Volei(db.Model):
    __tablename__ = 'volei'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    ginasio = db.Column(db.String(100))
    titulos = db.Column(db.Integer)

class Handebol(db.Model):
    __tablename__ = 'handebol'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(100))
    ginasio = db.Column(db.String(100))
    titulos = db.Column(db.Integer)

class Brasileirao(db.Model):
    __tablename__ = 'brasileirao'
    pos = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100))
    pontos = db.Column(db.Integer)
    jogos = db.Column(db.Integer)
    vitorias = db.Column(db.Integer)

class Carioca(db.Model):
    __tablename__ = 'carioca'
    pos = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(100))
    pontos = db.Column(db.Integer)

class Equipe(db.Model):
    __tablename__ = 'equipe'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    funcao = db.Column(db.String(100))
    area = db.Column(db.String(100))
    contato = db.Column(db.String(100))
    disponibilidade = db.Column(db.String(50))
    projetos = db.Column(db.String(200))

class Equipamento(db.Model):
    __tablename__ = 'equipamentos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    disponiveis = db.Column(db.Integer)
    status = db.Column(db.String(50))
    localizacao = db.Column(db.String(100))

class Material(db.Model):
    __tablename__ = 'materiais'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    quantidade = db.Column(db.Integer)
    disponiveis = db.Column(db.Integer)
    unidade = db.Column(db.String(20))

class Fluxo(db.Model):
    __tablename__ = 'fluxo'
    id = db.Column(db.Integer, primary_key=True)
    projeto = db.Column(db.String(100))
    tarefa = db.Column(db.String(200))
    responsavel = db.Column(db.String(100))
    prazo = db.Column(db.String(20))
    status = db.Column(db.String(50))
    prioridade = db.Column(db.String(20))

class Agenda(db.Model):
    __tablename__ = 'agenda'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20))
    evento = db.Column(db.String(200))
    local = db.Column(db.String(100))
    responsavel = db.Column(db.String(100))

class Escala(db.Model):
    __tablename__ = 'escalas'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20))
    funcao = db.Column(db.String(100))
    membro = db.Column(db.String(100))
    local = db.Column(db.String(100))

class Financeiro(db.Model):
    __tablename__ = 'financeiro'
    chave = db.Column(db.String(100), primary_key=True)
    valor = db.Column(db.String(200))
