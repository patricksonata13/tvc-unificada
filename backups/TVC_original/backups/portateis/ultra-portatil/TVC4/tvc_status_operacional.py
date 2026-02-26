import sqlite3
import os

def check_status():
    print("======= RELATÓRIO OPERACIONAL TVC =======")
    # Check de RH
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM talentos')
    total_talentos = cursor.fetchone()[0]
    print(f"👥 RH: {total_talentos} talentos no Banco Raízes.")
    
    # Check de Arquivos
    brutos = len(os.listdir(os.path.expanduser('~/TVC4/TVC_STUDIOS/Brutos')))
    finalizados = len(os.listdir(os.path.expanduser('~/TVC4/TVC_STUDIOS/Finalizados')))
    print(f"🎬 STUDIOS: {brutos} brutos aguardando | {finalizados} finalizados.")
    
    # Check de Financeiro (Simulado)
    print("💰 FINANCEIRO: 3 editais em fase de prestação de contas.")
    print("==========================================")
    conn.close()

if __name__ == "__main__":
    check_status()
