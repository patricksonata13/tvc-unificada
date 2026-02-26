import random, os

def simular_audiencia():
    hits = random.randint(5000, 15000)
    conversao = hits * 0.05  # 5% viram assinantes
    receita = conversao * 29.90
    
    print("\n" + "📈" * 15)
    print("   RELATÓRIO DE PERFORMANCE TVC PLAY")
    print("   PROJETO: ESTELIONATO CARIOCA")
    print("📈" * 15)
    print(f"Visualizações Únicas: {hits}")
    print(f"Novos Assinantes: {int(conversao)}")
    print(f"Receita Gerada: R$ {receita:,.2f}")
    print("📈" * 15 + "\n")
    
    os.system(f'say -v Luciana "Diretor, tivemos {hits} visualizações e a receita cresceu."')

if __name__ == "__main__":
    simular_audiencia()
