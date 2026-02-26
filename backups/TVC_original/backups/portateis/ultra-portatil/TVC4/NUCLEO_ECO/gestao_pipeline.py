import sqlite3, os

def iniciar_pipeline():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pipeline (id INTEGER PRIMARY KEY, nome TEXT, fase TEXT)')
    # Inserindo alguns projetos do catálogo
    projetos = [('CATIÇO', 'PRODUÇÃO'), ('O MATUTO', 'GRAVAÇÃO'), ('TRÊM', 'ROTEIRO')]
    cursor.executemany('INSERT OR IGNORE INTO pipeline (nome, fase) VALUES (?, ?)', projetos)
    conn.commit()
    conn.close()
    print("📋 Pipeline de Projetos Atualizado no Núcleo ECO.")

if __name__ == "__main__":
    iniciar_pipeline()
