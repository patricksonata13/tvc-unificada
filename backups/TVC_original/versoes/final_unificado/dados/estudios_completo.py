# data/estudios.py - Gestão completa de estúdio

# ==================== EQUIPE ====================
EQUIPE = [
    {"id": 1, "nome": "Joel Zito Araújo", "funcao": "Diretor", "area": "Direção", "contato": "joel@tvc.com", "disponibilidade": "Ocupado", "projetos": ["CATIÇO"]},
    {"id": 2, "nome": "Walter Salles", "funcao": "Diretor", "area": "Direção", "contato": "walter@tvc.com", "disponibilidade": "Ocupado", "projetos": ["TRÊM"]},
    {"id": 3, "nome": "Cacá Diegues", "funcao": "Diretor", "area": "Direção", "contato": "caca@tvc.com", "disponibilidade": "Disponível", "projetos": ["TEU SAMBA"]},
    {"id": 4, "nome": "Aline Marta", "funcao": "Atriz", "area": "Elenco", "contato": "aline@tvc.com", "disponibilidade": "Ocupada", "projetos": ["CATIÇO", "TRÊM"]},
    {"id": 5, "nome": "Lucas Penteado", "funcao": "Ator", "area": "Elenco", "contato": "lucas@tvc.com", "disponibilidade": "Ocupado", "projetos": ["CATIÇO", "TRÊM"]},
]

# ==================== EQUIPAMENTOS ====================
EQUIPAMENTOS = [
    {"id": 1, "nome": "Câmera RED Komodo", "tipo": "Câmera", "quantidade": 3, "disponiveis": 2, "status": "Operacional", "localizacao": "Estúdio A"},
    {"id": 2, "nome": "Câmera Sony FX9", "tipo": "Câmera", "quantidade": 4, "disponiveis": 3, "status": "Operacional", "localizacao": "Estúdio B"},
    {"id": 3, "nome": "Lente Zeiss CP.3", "tipo": "Lente", "quantidade": 8, "disponiveis": 5, "status": "Operacional", "localizacao": "Prateleira 2"},
    {"id": 4, "nome": "Kit Iluminação ARRI", "tipo": "Iluminação", "quantidade": 5, "disponiveis": 3, "status": "Operacional", "localizacao": "Depósito"},
]

# ==================== MATERIAIS ====================
MATERIAIS = [
    {"id": 1, "nome": "Cartão SD 128GB", "tipo": "Mídia", "quantidade": 20, "disponiveis": 15, "unidade": "un"},
    {"id": 2, "nome": "Bateria V-Mount", "tipo": "Energia", "quantidade": 12, "disponiveis": 8, "unidade": "un"},
]

# ==================== FLUXO DE TRABALHO ====================
FLUXO = [
    {"id": 1, "projeto": "CATIÇO", "tarefa": "Finalizar edição", "responsavel": "Joel Zito", "prazo": "22/02/2026", "status": "Em andamento", "prioridade": "Alta"},
    {"id": 2, "projeto": "CATIÇO", "tarefa": "Correção de cor", "responsavel": "Lula Carvalho", "prazo": "25/02/2026", "status": "Aguardando", "prioridade": "Média"},
]

# ==================== AGENDA ====================
AGENDA = [
    {"id": 1, "titulo": "Gravação CATIÇO", "data": "25/02/2026", "hora_inicio": "08:00", "hora_fim": "18:00", "local": "Cidade de Deus", "tipo": "Gravação", "participantes": ["Joel Zito", "Aline Marta"]},
]

# ==================== ESCALAS ====================
ESCALAS = [
    {"id": 1, "projeto": "CATIÇO", "data": "25/02/2026", "local": "Cidade de Deus", "horario": "08:00-18:00",
     "equipe": ["Joel Zito (Dir)", "Pedro Costa (Fot)"],
     "elenco": ["Aline Marta"], "status": "Confirmado"},
]
