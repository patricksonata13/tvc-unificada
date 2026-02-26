import sqlite3, os, datetime

def agendar_mes():
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome FROM pipeline WHERE fase != "FINALIZAÇÃO"')
    projetos = cursor.fetchall()
    
    data_inicio = datetime.date.today()
    agenda_path = os.path.expanduser("~/TVC4/NUCLEO_ECO/AGENDA_MESTRE_2026.txt")
    
    with open(agenda_path, "w") as f:
        f.write("====================================================\n")
        f.write("      AGENDA MESTRE DE PRODUÇÃO - TVC STUDIOS\n")
        f.write("====================================================\n")
        for i, proj in enumerate(projetos):
            data_proj = data_inicio + datetime.timedelta(days=i*2)
            f.write(f"DATA: {data_proj} | PROJETO: {proj[0].upper()} | STATUS: SET ATIVO\n")
            
    print(f"📅 Agenda Mestre gerada: {agenda_path}")
    os.system('say -v Luciana "Diretor, a agenda mestre para os vinte e três projetos foi consolidada."')
    conn.close()

if __name__ == "__main__":
    agendar_mes()
