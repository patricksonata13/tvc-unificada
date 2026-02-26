import os

def gerar_ordem_dia(projeto, local, talentos):
    call_sheet = f"""
    --------------------------------------------------
    TVC STUDIOS - ORDEM DO DIA (AUTOMÁTICA)
    PROJETO: {projeto} | LOCAL: {local}
    --------------------------------------------------
    TALENTOS ESCALADOS: {', '.join(talentos)}
    FLUXO: Roteiro Verificado -> Câmeras Prontas
    --------------------------------------------------
    """
    path = os.path.expanduser(f"~/TVC4/OPERACIONAL/LOGISTICA/CALL_{projeto.replace(' ', '_')}.txt")
    with open(path, "w") as f:
        f.write(call_sheet)
    print(f"📅 Call Sheet gerada via Roteiro: {path}")

if __name__ == "__main__":
    gerar_ordem_dia("ESTELIONATO CARIOCA", "PORTO MARAVILHA", ["SONATA", "CATIÇO"])
