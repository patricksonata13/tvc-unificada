import random

def analisar_clima_social():
    temas = ["Crime Real", "Comédia de Costumes", "Acção Rio", "Documentário"]
    top_tema = random.choice(temas)
    
    print(f"📊 [INSIGHT] A audiência está a pedir mais: {top_tema}")
    print(f"💡 Sugestão para o Núcleo Pro: Ajustar Episódio 02 de 'Estelionato Carioca'.")

if __name__ == "__main__":
    analisar_clima_social()
