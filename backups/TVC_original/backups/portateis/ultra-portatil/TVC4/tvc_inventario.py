import sqlite3
import os

def iniciar_inventario():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            status TEXT DEFAULT 'Disponível',
            responsavel TEXT
        )
    ''')
    conn.commit()
    conn.close()

def movimentar_item(item_id, novo_status, responsavel):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('UPDATE inventario SET status = ?, responsavel = ? WHERE id = ?', 
                   (novo_status, responsavel, item_id))
    conn.commit()
    print(f"📦 Item {item_id} atualizado: {novo_status} com {responsavel}")
    conn.close()

if __name__ == "__main__":
    iniciar_inventario()
    print("SISTEMA DE INVENTÁRIO TVC INICIADO.")
