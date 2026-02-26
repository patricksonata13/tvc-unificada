import sqlite3, os

def buscar_disponibilidade(funcao):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM talentos WHERE funcao = ?', (funcao,))
    resultados = cursor.fetchall()
    
    print(f"\n🔍 Buscando {funcao} no Banco Raízes...")
    for r in resultados:
        print(f"   [DISPONÍVEL] {r[0]}")
    conn.close()

if __name__ == "__main__":
    funcao = input("Qual profissional você precisa agora? (Ex: Ator, Cinegrafista): ")
    buscar_disponibilidade(funcao)
