import sqlite3
import os

def gerar_dash():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    
    # Busca Talentos
    cursor.execute('SELECT nome, funcao, cache_base FROM talentos')
    talentos = cursor.fetchall()
    
    # Busca Inventário
    cursor.execute('SELECT item, status, responsavel FROM inventario')
    itens = cursor.fetchall()
    
    total_folha = sum(t[2] for t in talentos)
    
    html = f"""
    <html>
    <head>
        <title>TVC COMMAND CENTER</title>
        <style>
            body {{ font-family: sans-serif; background: #0f172a; color: white; padding: 40px; }}
            .card {{ background: #1e293b; padding: 20px; border-radius: 10px; margin-bottom: 20px; border: 1px solid #334155; }}
            h1 {{ color: #38bdf8; border-bottom: 2px solid #38bdf8; padding-bottom: 10px; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ text-align: left; padding: 12px; border-bottom: 1px solid #334155; }}
            .status {{ padding: 4px 8px; border-radius: 4px; font-size: 12px; }}
            .green {{ background: #166534; }}
            .blue {{ background: #1e40af; }}
        </style>
    </head>
    <body>
        <h1>📺 TVC CENTRAL OPERACIONAL</h1>
        <div class="card">
            <h2>💰 Financeiro: R$ {total_folha:,.2f} / mês</h2>
        </div>
        <div class="card">
            <h2>👥 Talentos Cadastrados</h2>
            <table>
                <tr><th>Nome</th><th>Função</th><th>Cachê</th></tr>
                {"".join([f"<tr><td>{t[0]}</td><td>{t[1]}</td><td>R$ {t[2]:,.2f}</td></tr>" for t in talentos])}
            </table>
        </div>
        <div class="card">
            <h2>📦 Almoxarifado</h2>
            <table>
                <tr><th>Item</th><th>Status</th><th>Responsável</th></tr>
                {"".join([f"<tr><td>{i[0]}</td><td><span class='status {'green' if i[1]=='Disponível' else 'blue'}'>{i[1]}</span></td><td>{i[2] if i[2] else '-'}</td></tr>" for i in itens])}
            </table>
        </div>
    </body>
    </html>
    """
    
    with open(os.path.expanduser('~/TVC4/dashboard_tvc.html'), 'w') as f:
        f.write(html)
    print("🚀 Dashboard atualizado! Abra o arquivo ~/TVC4/dashboard_tvc.html no seu navegador.")
    conn.close()

if __name__ == "__main__":
    gerar_dash()
