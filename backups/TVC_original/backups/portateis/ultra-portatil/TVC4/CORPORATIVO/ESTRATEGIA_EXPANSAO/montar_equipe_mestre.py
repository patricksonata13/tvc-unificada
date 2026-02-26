import sqlite3, os

def estruturar_lideranca():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    
    # Criando a tabela de Liderança se não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS lideranca 
                   (id INTEGER PRIMARY KEY, nome TEXT, nucleo TEXT, cargo TEXT, projeto_foco TEXT)''')
    
    equipe_chave = [
        ('PATRICK SONATA', 'CRIATIVO', 'Showrunner / Roteirista-Chefe', 'Estelionato Carioca'),
        ('CATIÇO SILVA', 'OPERAÇÕES', 'Diretor de Produção / Logística', 'Geral'),
        ('TAMIRES GOMES', 'PÓS-PRODUÇÃO', 'Diretora de Tecnologia e VFX', 'TVC Play'),
        ('BEATRIZ REIS', 'DIREÇÃO', 'Diretora de Cena (Núcleo Drama)', 'O Matuto'),
        ('SQUAD RAIZES', 'ELENCO', 'Coordenação de Talentos', 'Banco Raízes')
    ]
    
    cursor.executemany('INSERT OR REPLACE INTO lideranca (nome, nucleo, cargo, projeto_foco) VALUES (?, ?, ?, ?)', equipe_chave)
    conn.commit()
    print("🏢 Hierarquia de Liderança TVC Studios consolidada no Banco de Dados.")
    conn.close()

if __name__ == "__main__":
    estruturar_lideranca()
