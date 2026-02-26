import os

def criar_template_roteiro(projeto, episodio):
    template = f"""
    PROJETO: {projeto}
    EPISÓDIO: {episodio}
    --------------------------------------------------
    CENA 01 - [LOCAL] - [DIA/NOITE]
    PERSONAGENS: 
    
    AÇÃO: 
    
    DIÁLOGO:
    --------------------------------------------------
    """
    path = os.path.expanduser(f"~/TVC4/NUCLEO_PRO/{projeto}_EP{episodio}.txt")
    with open(path, "w") as f:
        f.write(template)
    print(f"✍️ Template de Roteiro criado: {path}")

if __name__ == "__main__":
    p = input("Nome do Projeto: ")
    e = input("Número do Episódio: ")
    criar_template_roteiro(p, e)
