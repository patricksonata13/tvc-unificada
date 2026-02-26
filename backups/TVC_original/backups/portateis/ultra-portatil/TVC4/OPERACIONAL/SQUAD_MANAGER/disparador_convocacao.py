import sqlite3, os

def disparar_mensagens():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    
    # Busca talentos escalados para o projeto ativo
    cursor.execute('SELECT nome, funcao FROM talentos LIMIT 5') # Exemplo com os 5 primeiros
    convocados = cursor.fetchall()
    
    projeto = "ESTELIONATO CARIOCA"
    set_local = "Porto Maravilha, Rio de Janeiro"
    horario = "07:00 AM"

    print(f"\n📡 [GATEWAY SMS] Iniciando disparos para o projeto: {projeto}")
    
    for nome, funcao in convocados:
        msg = f"Olá {nome} ({funcao}), a TVC Studios convoca você para o set de '{projeto}'. Local: {set_local} às {horario}. Confirme seu QR Code no App."
        print(f"📲 ENVIANDO PARA {nome}: {msg}")
    
    os.system(f'say -v Luciana "Diretor, a convocação do Squad Raízes foi enviada via satélite."')
    conn.close()

if __name__ == "__main__":
    disparar_mensagens()
