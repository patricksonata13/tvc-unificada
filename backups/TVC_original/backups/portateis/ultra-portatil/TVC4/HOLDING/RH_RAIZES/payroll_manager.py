import sqlite3, os

def processar_folha():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome, funcao FROM talentos')
    talentos = cursor.fetchall()
    
    print("📋 FOLHA DE PAGAMENTO GERADA - MÊS VIGENTE")
    for t in talentos:
        # Simulação de diária padrão R$ 250,00
        print(f"TALENTO: {t[0]:<20} | STATUS: LIBERADO | VALOR: R$ 250,00")
    
    os.system('say -v Luciana "Diretor, a folha de pagamento do Banco Raízes foi processada com sucesso."')
    conn.close()

if __name__ == "__main__":
    processar_folha()
