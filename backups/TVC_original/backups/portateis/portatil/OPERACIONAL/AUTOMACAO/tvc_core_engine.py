import os, subprocess, sqlite3, logging, datetime

# Configuração de Logs Profissionais
logging.basicConfig(filename=os.path.expanduser('~/TVC4/tvc_system.log'), level=logging.INFO)

def registrar_evento(etapa, status, detalhes):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS logs_auditoria 
                   (timestamp TEXT, etapa TEXT, status TEXT, detalhes TEXT)''')
    cursor.execute("INSERT INTO logs_auditoria VALUES (?, ?, ?, ?)", 
                   (datetime.datetime.now(), etapa, status, detalhes))
    conn.commit()
    conn.close()

def processar_com_seguranca(cmd, etapa_nome):
    try:
        logging.info(f"Iniciando {etapa_nome}")
        subprocess.run(cmd, check=True, capture_output=True)
        registrar_evento(etapa_nome, "SUCESSO", "Operação concluída sem erros")
        return True
    except subprocess.CalledProcessError as e:
        erro_msg = f"Falha na etapa {etapa_nome}: {e.stderr.decode()}"
        logging.error(erro_msg)
        registrar_evento(etapa_nome, "ERRO", erro_msg)
        os.system(f'say -v Luciana "Alerta Diretor! Falha crítica na etapa de {etapa_nome}"')
        return False

if __name__ == "__main__":
    print("🛡️ Motor Central TVC em modo Standby (Robustez Ativada)")
