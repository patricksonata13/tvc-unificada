#!/bin/bash
# Atualiza o arquivo de dados da escaleta com os novos projetos
cat > modulos/escaleta/escaleta.py << 'INNEREOF'
# data/escaleta.py - 19 projetos

ESCALETA_PROJETOS = [
    {"id": 1, "nome": "CATIÇO", "tipo": "Filme", "status": "Pós-produção", "progresso": 90,
     "visao": "Comunidades", "responsavel": "Carlos Alberto", "orcamento": 800000,
     "descricao": "Cidade de Deus, anos 90. Jovem negro se torna bandido famoso."},
    {"id": 2, "nome": "TEU SAMBA", "tipo": "Novela", "status": "Pré-produção", "progresso": 30,
     "visao": "Cultural", "responsavel": "Ana Paula", "orcamento": 410000,
     "descricao": "Jovem sambista busca sucesso enfrentando tradição."},
    {"id": 3, "nome": "TRÊM", "tipo": "Série", "status": "Desenvolvimento", "progresso": 45,
     "visao": "Comunidades", "responsavel": "Mariana Santos", "orcamento": 1200000,
     "descricao": "Jovens formam grupo de dança no trem."},
    {"id": 4, "nome": "THE PUNCH", "tipo": "Filme", "status": "Roteiro", "progresso": 15,
     "visao": "Zona Oeste", "responsavel": "Paulo Roberto", "orcamento": 600000,
     "descricao": "Após um soco viral, homem tenta reconstruir sua vida."},
    {"id": 5, "nome": "A PRINCESA PERDIDA", "tipo": "Filme", "status": "Pré-produção", "progresso": 25,
     "visao": "Zona Sul", "responsavel": "Carla Dias", "orcamento": 750000,
     "descricao": "Angolana rica foge de casamento arranjado."},
    {"id": 6, "nome": "FESTA DA LAURA", "tipo": "Filme", "status": "Roteiro", "progresso": 20,
     "visao": "Comunidades", "responsavel": "Fernanda Lima", "orcamento": 550000,
     "descricao": "Mãe prepara festa extravagante na Cidade de Deus."},
    {"id": 7, "nome": "CORINHO DE FOGO", "tipo": "Filme", "status": "Desenvolvimento", "progresso": 10,
     "visao": "Cultural", "responsavel": "Marcelo Santos", "orcamento": 450000,
     "descricao": "Cantor gospel sem unção tenta voltar ao estrelato."},
    {"id": 8, "nome": "DIFERENTE MAS NEM TANTO", "tipo": "Série", "status": "Roteiro", "progresso": 35,
     "visao": "Zona Oeste", "responsavel": "Luciana Mello", "orcamento": 1500000,
     "descricao": "Família negra de Madureira enfrenta preconceitos."},
    {"id": 9, "nome": "O MATUTO", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 25,
     "visao": "Comunidades", "responsavel": "Ricardo Silva", "orcamento": 300000,
     "descricao": "Homem comum esconde identidade secreta no crime."},
    {"id": 10, "nome": "COSTA VERDE", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 40,
     "visao": "Litoral", "responsavel": "Patricia Costa", "orcamento": 350000,
     "descricao": "Conflito entre praias e florestas."},
    {"id": 11, "nome": "VIADUTO", "tipo": "Mini Novela", "status": "Desenvolvimento", "progresso": 15,
     "visao": "Cultural", "responsavel": "André Luiz", "orcamento": 280000,
     "descricao": "Forças ancestrais e tecnologia sob o viaduto."},
    {"id": 12, "nome": "VARRE SAI", "tipo": "Mini Novela", "status": "Pré-produção", "progresso": 50,
     "visao": "Comunidades", "responsavel": "Cristina Lemos", "orcamento": 320000,
     "descricao": "Comunidade enfrenta desafios com solidariedade."},
    {"id": 13, "nome": "UM VERÃO EM ARRAIAL", "tipo": "Mini Novela", "status": "Roteiro", "progresso": 30,
     "visao": "Litoral", "responsavel": "João Paulo", "orcamento": 380000,
     "descricao": "Paixões intensas em Arraial do Cabo."},
    {"id": 14, "nome": "ESTELIONATÁRIOS DIGITAIS", "tipo": "Série", "status": "Desenvolvimento", "progresso": 20,
     "visao": "Zona Sul", "responsavel": "Roberta Campos", "orcamento": 900000,
     "descricao": "Estelionatários digitais veem império ruir."},
    {"id": 15, "nome": "MÃOS QUE CURAM", "tipo": "Filme", "status": "Roteiro", "progresso": 15,
     "visao": "Comunidades", "responsavel": "Lázaro Ramos", "orcamento": 1100000,
     "descricao": "Benzedeira do subúrbio enfrenta desafios da fé."},
    {"id": 16, "nome": "FUNK-SE", "tipo": "Série", "status": "Desenvolvimento", "progresso": 25,
     "visao": "Comunidades", "responsavel": "Tatiana Issa", "orcamento": 1300000,
     "descricao": "Série documental sobre a história do funk carioca."},
    {"id": 17, "nome": "CIDADE PARTIDA", "tipo": "Documentário", "status": "Pesquisa", "progresso": 10,
     "visao": "Zona Oeste", "responsavel": "Eduardo Coutinho", "orcamento": 500000,
     "descricao": "Retrato das múltiplas realidades da Zona Oeste carioca."},
    {"id": 18, "nome": "LATA DE TINTA", "tipo": "Filme Longa", "status": "Desenvolvimento", "progresso": 10,
     "visao": "Zona Norte", "responsavel": "Fernanda Montenegro", "orcamento": 1200000,
     "descricao": "Um casal recém-separado precisa voltar à casa onde moraram para pintá-la e entregá-la, revivendo todos os momentos de 10 anos juntos."},
    {"id": 19, "nome": "TERRENO DE FAMÍLIA", "tipo": "Documentário", "status": "Pesquisa", "progresso": 5,
     "visao": "Memória", "responsavel": "Eduardo Coutinho Jr.", "orcamento": 450000,
     "descricao": "Documentário sobre as brigas de uma família por herança de um terreno, explorando conflitos e memórias."}
]
INNEREOF

# Atualiza o banco de dados (insere ou atualiza os projetos)
python3 << 'PYEOF'
import sqlite3
from modulos.escaleta.escaleta import ESCALETA_PROJETOS
conn = sqlite3.connect('tvc.db')
c = conn.cursor()
for p in ESCALETA_PROJETOS:
    c.execute('''
        INSERT OR REPLACE INTO escaleta 
        (id, nome, tipo, status, progresso, visao, responsavel, orcamento, descricao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (p['id'], p['nome'], p['tipo'], p['status'], p['progresso'], p['visao'], p['responsavel'], p['orcamento'], p['descricao']))
conn.commit()
conn.close()
print("Banco de dados atualizado com sucesso.")
PYEOF

echo "Projetos adicionados/atualizados. Reinicie o servidor se necessário."
