import sqlite3, os

def exibir_status():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome, fase FROM pipeline')
    projetos = cursor.fetchall()
    
    print("\n" + "="*40)
    print("      TVC ECO - STATUS DO PIPELINE")
    print("="*40)
    
    for nome, fase in projetos:
        status_icon = "🎬" if fase == "GRAVAÇÃO" else "✍️" if fase == "ROTEIRO" else "📂"
        print(f"{status_icon} {nome.ljust(20)} | FASE: {fase}")
        
    print("="*40 + "\n")
    conn.close()

if __name__ == "__main__":
    exibir_status()
