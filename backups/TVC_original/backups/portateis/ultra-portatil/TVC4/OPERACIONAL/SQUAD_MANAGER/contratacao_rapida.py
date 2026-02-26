import sqlite3, os

def contratar_talento(nome, funcao):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO talentos (nome, funcao) VALUES (?, ?)", (nome, funcao))
    conn.commit()
    conn.close()
    print(f"👤 {nome} foi integrado ao Squad como {funcao}.")

if __name__ == "__main__":
    # Simula a entrada de novos talentos de elite
    contratar_talento("ALICE MARINS", "DIRETORA DE FOTOGRAFIA")
    contratar_talento("BRUNO COSTA", "OPERADOR DE DRONE")
