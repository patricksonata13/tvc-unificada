import os, sqlite3

def briefing_tvc():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    num_p = conn.execute('SELECT count(*) FROM pipeline').fetchone()[0]
    
    texto = f"Relatório de prontidão TVC Studios. Diretor, temos {num_p} projetos em base. Todos os protocolos de criptografia estão ativos e a infraestrutura está operando com eficiência máxima. O software TVC OS está pronto para o lançamento."
    
    os.system(f'say -v Luciana "{texto}"')

if __name__ == "__main__":
    briefing_tvc()
