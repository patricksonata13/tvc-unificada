import os

def gerar_contrato(nome_talento, projeto):
    contrato = f"""
    ============================================================
    CONTRATO DE CESSÃO DE IMAGEM E VOZ - TVC STUDIOS 2026
    ============================================================
    CEDENTE: {nome_talento}
    CESSIONÁRIA: TVC STUDIOS & HOLDING
    PROJETO: {projeto}
    
    Pelo presente instrumento, o CEDENTE autoriza o uso de sua 
    imagem e voz para fins de exibição na plataforma TVC PLAY 
    e redes sociais afiliadas por tempo indeterminado.
    
    FORO: Comarca do Rio de Janeiro, RJ.
    ============================================================
    """
    path = os.path.expanduser(f"~/TVC4/HOLDING/JURIDICO/CONTRATO_{nome_talento.replace(' ', '_')}.txt")
    with open(path, "w") as f:
        f.write(contrato)
    print(f"⚖️ Contrato gerado para: {nome_talento}")

if __name__ == "__main__":
    gerar_contrato("PATRICK SONATA", "ESTELIONATO CARIOCA")
