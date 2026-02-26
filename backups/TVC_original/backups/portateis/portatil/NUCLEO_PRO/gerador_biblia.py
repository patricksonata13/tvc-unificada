import os

def gerar_biblia(projeto, tema, publico):
    conteudo = f"""
    ==================================================
    TVC PRO - BÍBLIA DE PRODUÇÃO: {projeto}
    ==================================================
    TEMA CENTRAL: {tema}
    PÚBLICO-ALVO: {publico}
    
    1. CONCEITO VISUAL: Estética urbana, cores saturadas.
    2. ARCO NARRATIVO: Do conflito territorial à superação.
    3. ESTRATÉGIA DE LANÇAMENTO: TVC PLAY (Exclusivo).
    
    --------------------------------------------------
    DOCUMENTO GERADO PARA DIRETORIA TVC - 2026
    ==================================================
    """
    path = os.path.expanduser(f"~/TVC4/NUCLEO_PRO/BIBLIA_{projeto}.txt")
    with open(path, "w") as f:
        f.write(conteudo)
    print(f"📖 Bíblia de Produção criada: {path}")

if __name__ == "__main__":
    p = input("Nome do Projeto: ")
    t = input("Tema Central: ")
    pub = input("Público-alvo: ")
    gerar_biblia(p, t, pub)
