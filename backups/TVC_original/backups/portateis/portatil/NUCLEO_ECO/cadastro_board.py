import sqlite3, os

def cadastrar_diretoria():
    db_path = os.path.expanduser('~/TVC4/tvc_admin.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT, nucleo TEXT, cargo TEXT)')
    
    board = [
        ('Patrick Sonata', 'PRO', 'Showrunner'),
        ('Tamires Gomes', 'PLAY', 'Diretora de Distribuição'),
        ('Catiço Silva', 'STUDIOS', 'Coordenador de Dublês')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO usuarios (nome, nucleo, cargo) VALUES (?, ?, ?)', board)
    conn.commit()
    conn.close()
    print("✅ Board de Diretores da TVC registrado com sucesso!")

if __name__ == "__main__":
    cadastrar_diretoria()
