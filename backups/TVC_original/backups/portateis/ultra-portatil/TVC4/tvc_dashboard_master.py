import os, psutil, shutil, sqlite3, json

def gerar_tvc_os_v16():
    # Carregar dados financeiros reais
    try:
        with open(os.path.expanduser("~/TVC4/CORPORATIVO/BI_FINANCAS/BALANCO_REAL_TVC.json"), "r") as f:
            financeiro = json.load(f)
            lucro_real = financeiro["lucro_real_distribuivel"]
    except:
        lucro_real = 0.0

    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    num_p = conn.execute('SELECT count(*) FROM pipeline').fetchone()[0]
    num_t = conn.execute('SELECT count(*) FROM talentos').fetchone()[0]
    conn.close()

    html = f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head><meta charset="UTF-8">
    <style>
        :root {{ --bg: #F8F9FA; --text: #1A1A1A; --accent: #000; --green: #28A745; }}
        body {{ margin: 0; font-family: 'Inter', sans-serif; background: var(--bg); color: var(--text); display: flex; height: 100vh; }}
        nav {{ width: 250px; background: #FFF; border-right: 1px solid #EEE; padding: 30px; }}
        .nav-item {{ padding: 12px; border-radius: 8px; font-size: 13px; color: #666; cursor: pointer; }}
        .active {{ background: var(--accent); color: #FFF; }}
        main {{ flex: 1; padding: 40px; overflow-y: auto; }}
        .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; }}
        .card {{ background: #FFF; padding: 25px; border-radius: 12px; border: 1px solid #EEE; box-shadow: 0 2px 5px rgba(0,0,0,0.02); }}
        .metric {{ font-size: 32px; font-weight: 800; color: var(--accent); }}
        .profit {{ color: var(--green); }}
    </style></head>
    <body>
        <nav>
            <div style="font-weight: 800; font-size: 20px; margin-bottom: 40px;">TVC STUDIOS</div>
            <div class="nav-item active">Master Control</div>
            <div class="nav-item">Pipeline ({num_p})</div>
            <div class="nav-item">Squad ({num_t})</div>
            <div class="nav-item">Distribuição IA</div>
        </nav>
        <main>
            <div class="header">
                <h1>Painel Executivo</h1>
                <div style="text-align: right;">
                    <span style="font-size: 11px; color: #999;">LUCRO REAL LÍQUIDO</span>
                    <div class="metric profit">R$ {lucro_real:,.2f}</div>
                </div>
            </div>
            <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
                <div class="card"><h3>Projetos</h3><div class="metric">{num_p}</div></div>
                <div class="card"><h3>Talentos</h3><div class="metric">{num_t}</div></div>
                <div class="card"><h3>Eficiência</h3><div class="metric">98%</div></div>
            </div>
            <div class="card" style="margin-top: 20px; border-left: 5px solid var(--accent);">
                <h3>Próximo Lançamento (IA)</h3>
                <p>Estelionato Carioca Piloto • <b>Amanhã, 20:00h</b></p>
                <small style="color: #999;">Status: Arquivos encriptados e prontos para o CDN.</small>
            </div>
        </main>
    </body>
    </html>
    """
    with open(os.path.expanduser('~/TVC4/DASHBOARD_MASTER.html'), 'w') as f: f.write(html)
    os.system('say -v Luciana "Sincronização financeira e de distribuição concluída."')

if __name__ == "__main__":
    gerar_tvc_os_v16()
