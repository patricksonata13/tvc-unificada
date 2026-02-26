import sqlite3
import os

def check_out(item_id, responsavel):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('UPDATE inventario SET status = "Em Uso", responsavel = ? WHERE id = ?', (responsavel, item_id))
    conn.commit()
    conn.close()
    print(f"📦 Equipamento {item_id} saiu com {responsavel}!")

if __name__ == "__main__":
    print("--- TVC LOGÍSTICA: SAÍDA DE MATERIAL ---")
    id_item = input("ID do Equipamento: ")
    nome = input("Nome do Responsável (Talento/Técnico): ")
    check_out(id_item, nome)
