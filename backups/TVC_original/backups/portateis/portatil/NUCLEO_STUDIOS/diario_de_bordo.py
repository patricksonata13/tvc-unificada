import datetime, os

def registrar_diaria(projeto, cenas, cartoes, observacao):
    data = datetime.datetime.now().strftime("%d/%m/%Y")
    conteudo = f"""
    ==================================================
    TVC STUDIOS - RELATÓRIO DIÁRIO DE PRODUÇÃO (RDP)
    ==================================================
    PROJETO: {projeto}
    DATA: {data}
    CENAS RODADAS: {cenas}
    CARTÕES UTILIZADOS: {cartoes}
    
    OBSERVAÇÕES DO SET:
    {observacao}
    
    STATUS DO BACKUP: [ ] PENDENTE  [ ] CONCLUÍDO
    --------------------------------------------------
    ASSINATURA: COORDENAÇÃO DE SET
    ==================================================
    """
    nome_arq = f"RDP_{projeto}_{datetime.datetime.now().strftime('%Y%m%d')}.txt"
    path = os.path.expanduser(f"~/TVC4/NUCLEO_STUDIOS/{nome_arq}")
    
    with open(path, "w") as f:
        f.write(conteudo)
    print(f"✅ Diário de Bordo (RDP) registrado em: {path}")

if __name__ == "__main__":
    print("--- TVC STUDIOS: REGISTRO DE DIÁRIA ---")
    p = input("Nome do Projeto (ex: O MATUTO): ").upper()
    c = input("Cenas filmadas hoje: ")
    car = input("Quantidade de cartões de memória preenchidos: ")
    obs = input("Ocorrências ou notas do Diretor: ")
    registrar_diaria(p, c, car, obs)
