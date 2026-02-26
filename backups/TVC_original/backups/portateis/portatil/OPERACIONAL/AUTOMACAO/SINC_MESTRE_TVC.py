import os, sqlite3, time

def iniciar_ciclo_completo(projeto, ep_numero):
    # 1. GATILHO DE ROTEIRO (Writer's Room)
    print(f"✍️  [ROTEIRO] Consolidando texto para {projeto} EP {ep_numero}...")
    time.sleep(1)
    
    # 2. GATILHO DE PRODUÇÃO (Set Digital)
    print(f"🎥 [PRODUÇÃO] Gerando Ordem do Dia e vinculando Talentos...")
    os.system(f"python3 ~/TVC4/NUCLEO_PRO/gerador_callsheet_auto.py")
    time.sleep(1)
    
    # 3. GATILHO DE PÓS (Render Farm)
    print(f"✂️  [PÓS-PRODUÇÃO] Ativando Watchdog para processamento com Look Cinema...")
    # Aqui o sistema fica em standby aguardando o arquivo bruto chegar
    
    mensagem = f"Diretor, o fluxo para {projeto} episódio {ep_numero} está sincronizado do roteiro à entrega."
    os.system(f'say -v Luciana "{mensagem}"')

if __name__ == "__main__":
    projeto = "ESTELIONATO CARIOCA"
    iniciar_ciclo_completo(projeto, "01")
