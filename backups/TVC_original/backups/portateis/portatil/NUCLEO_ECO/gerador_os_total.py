import sqlite3, os

def gerar_os_expansao():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    
    # Busca todos os projetos e talentos
    cursor.execute('SELECT nome FROM pipeline')
    projetos = [p[0] for p in cursor.fetchall()]
    cursor.execute('SELECT nome, funcao FROM talentos')
    talentos = cursor.fetchall()
    
    os_dir = os.path.expanduser("~/TVC4/NUCLEO_ECO/ORDENS_SERVICO_TOTAL")
    os.makedirs(os_dir, exist_ok=True)
    
    for i, projeto in enumerate(projetos):
        # Distribui talentos de forma cíclica para os projetos
        t_nome, t_funcao = talentos[i % len(talentos)]
        
        with open(f"{os_dir}/OS_{projeto.replace(' ', '_')}.txt", "w") as f:
            f.write(f"TVC STUDIOS - ORDEM DE SERVIÇO\nPROJETO: {projeto}\nRESPONSÁVEL: {t_nome}\nFUNÇÃO: {t_funcao}\nSTATUS: AUTORIZADO")
            
    print(f"✅ {len(projetos)} Ordens de Serviço geradas para o Pipeline Total.")
    os.system('say -v Luciana "Diretor, o cronograma de ordens de serviço para todos os vinte e três projetos foi atualizado."')
    conn.close()

if __name__ == "__main__":
    gerar_os_expansao()
