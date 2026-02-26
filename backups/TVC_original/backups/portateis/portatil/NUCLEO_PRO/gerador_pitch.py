import os

def gerar_pitch(projeto, logline, diferencial):
    pitch = f"""
    ==================================================
    TVC STUDIOS - PITCH DE MERCADO 2026
    ==================================================
    PROJETO: {projeto}
    CONCEITO (LOGLINE): {logline}
    
    DIFERENCIAL COMPETITIVO DA TVC: 
    {diferencial}
    
    CAPACIDADE OPERACIONAL INSTALADA: 
    - Pipeline Digital (ECO)
    - Processamento FFmpeg 8.0 (STUDIOS)
    - Distribuição Própria (TVC PLAY)
    
    Este projeto faz parte do catálogo de 23 obras originais.
    ==================================================
    """
    path = os.path.expanduser(f"~/TVC4/NUCLEO_PRO/PITCH_{projeto.replace(' ', '_')}.txt")
    with open(path, "w") as f:
        f.write(pitch)
    print(f"💎 Documento de Pitch gerado: {path}")

if __name__ == "__main__":
    p = input("Nome do Projeto: ")
    l = input("Logline (Resumo em 1 frase): ")
    d = input("Por que é único? ")
    gerar_pitch(p, l, d)
