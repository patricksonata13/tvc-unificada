import sqlite3, os

def gerar_relatorio_diretoria():
    db_path = os.path.expanduser('~/TVC4/tvc_admin.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Total em Folha
    cursor.execute('SELECT SUM(cache_base) FROM talentos')
    total_folha = cursor.fetchone()[0] or 0
    
    # 2. Projetos por Fase
    cursor.execute('SELECT fase, COUNT(*) FROM pipeline GROUP BY fase')
    fases = cursor.fetchall()
    
    # 3. Status do Inventário
    cursor.execute('SELECT status, COUNT(*) FROM inventario GROUP BY status')
    estoque = cursor.fetchall()
    
    print("\n" + "█"*50)
    print("      TVC BUSINESS INTELLIGENCE - RELATÓRIO CEO")
    print("█"*50)
    print(f"💰 CUSTO MENSAL FIXO (TALENTOS): R$ {total_folha:,.2f}")
    print("-" * 50)
    print("📈 PIPELINE DE PRODUÇÃO:")
    for fase, qtd in fases:
        print(f"   - {fase.ljust(18)} : {qtd} Projeto(s)")
    print("-" * 50)
    print("📦 STATUS DE SUPRIMENTOS:")
    for status, qtd in estoque:
        print(f"   - {status.ljust(18)} : {qtd} Item(ns)")
    print("█"*50 + "\n")
    conn.close()

if __name__ == "__main__":
    gerar_relatorio_diretoria()
