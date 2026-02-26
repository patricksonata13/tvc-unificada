import os, sqlite3, json, datetime

def sincronizar_fluxo(projeto, cena_id, acao):
    db_path = os.path.expanduser('~/TVC4/tvc_admin.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 1. ROTEIRO (Gera a intenção)
    if acao == "ROTEIRO":
        print(f"✍️ [ROTEIRO] Cena {cena_id} de '{projeto}' liberada para produção.")
        cursor.execute("UPDATE pipeline SET fase = 'PRODUÇÃO' WHERE nome = ?", (projeto,))
        
    # 2. PRODUÇÃO (Registra a captura)
    elif acao == "PRODUCAO":
        print(f"🎥 [PRODUÇÃO] Cena {cena_id} rodada. Enviando metadados para Pós.")
        # Simula o log de câmera
        log_camera = {"projeto": projeto, "cena": cena_id, "data": data_atual, "status": "OK"}
        with open(os.path.expanduser(f"~/TVC4/TVC_STUDIOS/Brutos/LOG_{cena_id}.json"), "w") as f:
            json.dump(log_camera, f)
            
    # 3. PÓS-PRODUÇÃO (Finaliza com base no log)
    elif acao == "POS":
        print(f"✂️ [PÓS] Finalizando Cena {cena_id}. Aplicando look 'Estelionato'.")
        cursor.execute("UPDATE pipeline SET fase = 'FINALIZAÇÃO' WHERE nome = ?", (projeto,))
        os.system(f'say -v Luciana "Diretor, a cena {cena_id} percorreu o fluxo perfeito e está pronta."')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Teste de integração total
    print("--- INICIANDO CICLO DE PRODUÇÃO TVC ---")
    sincronizar_fluxo("ESTELIONATO CARIOCA", "CENA_01", "ROTEIRO")
    sincronizar_fluxo("ESTELIONATO CARIOCA", "CENA_01", "PRODUCAO")
    sincronizar_fluxo("ESTELIONATO CARIOCA", "CENA_01", "POS")
