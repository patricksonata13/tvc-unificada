import sqlite3
import os

def iniciar_banco():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS talentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            bairro TEXT,
            funcao TEXT,
            cache_base REAL
        )
    ''')
    conn.commit()
    conn.close()

def cadastrar_talento(nome, bairro, funcao, cache):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('INSERT INTO talentos (nome, bairro, funcao, cache_base) VALUES (?, ?, ?, ?)', 
                   (nome, bairro, funcao, cache))
    conn.commit()
    print(f"✅ {nome} cadastrado com sucesso no Banco Raízes!")
    conn.close()

if __name__ == "__main__":
    iniciar_banco()
    # Exemplo de uso:
    # cadastrar_talento("Catiço Silva", "Cidade de Deus", "Ator/Ação", 500.00)
