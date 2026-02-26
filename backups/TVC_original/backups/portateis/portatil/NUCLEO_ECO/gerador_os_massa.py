import sqlite3, os

def gerar_os_talentos():
    db_path = os.path.expanduser('~/TVC4/tvc_admin.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute('SELECT nome, funcao FROM talentos')
    talentos = cursor.fetchall()
    
    os_dir = os.path.expanduser("~/TVC4/NUCLEO_ECO/ORDENS_SERVICO")
    os.makedirs(os_dir, exist_ok=True)
    
    for t in talentos:
        nome, funcao = t
        conteudo = f"""
        ==================================================
        TVC STUDIOS - ORDEM DE SERVIÇO DIGITAL
        ==================================================
        CONTRATADO: {nome}
        FUNÇÃO: {funcao}
        PROJETO: ESTELIONATO CARIOCA
        DATA: 2026-02-18
        --------------------------------------------------
        DETERMINAÇÃO: Comparecer ao set portando ID funcional.
        PAGAMENTO: Liberado pós-diária via TVC_PAY.
        ==================================================
        """
        with open(f"{os_dir}/OS_{nome.replace(' ', '_')}.txt", "w") as f:
            f.write(conteudo)
            
    print(f"📦 {len(talentos)} Ordens de Serviço geradas em: {os_dir}")
    conn.close()

if __name__ == "__main__":
    gerar_os_talentos()
