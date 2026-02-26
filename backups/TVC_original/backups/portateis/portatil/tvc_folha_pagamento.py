import sqlite3
import os

def gerar_folha():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome, funcao, cache_base FROM talentos')
    equipe = cursor.fetchall()
    
    print("\n" + "="*40)
    print("      FOLHA DE PAGAMENTO TVC - MENSAL")
    print("="*40)
    
    total_geral = 0
    for nome, funcao, salario in equipe:
        print(f"👤 {nome.ljust(18)} | {funcao.ljust(15)} | R$ {salario:>8.2f}")
        total_geral += salario
        
    print("-"*40)
    print(f"💰 CUSTO TOTAL DE TALENTOS: R$ {total_geral:>10.2f}")
    print("="*40 + "\n")
    conn.close()

if __name__ == "__main__":
    gerar_folha()
