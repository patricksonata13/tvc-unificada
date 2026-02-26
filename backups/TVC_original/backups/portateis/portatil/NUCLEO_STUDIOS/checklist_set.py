import sqlite3, os

def gerar_checklist_diaria(projeto):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT item FROM inventario WHERE status = "Disponível"')
    itens = cursor.fetchall()
    
    path = os.path.expanduser(f"~/TVC4/NUCLEO_STUDIOS/CHECKLIST_{projeto}.txt")
    with open(path, "w") as f:
        f.write(f"📋 CHECKLIST DE SAÍDA - PROJETO: {projeto}\n")
        f.write("==========================================\n")
        for item in itens:
            f.write(f"[ ] {item[0]}\n")
        f.write("\n⚠️ Verificar baterias e cartões antes de sair.")
    
    print(f"📦 Checklist gerado para o núcleo Studios: {path}")
    conn.close()

if __name__ == "__main__":
    p = input("Qual projeto vai para o set amanhã? ").upper()
    gerar_checklist_diaria(p)
