import random, os

def analisar_roteiro_ai(projeto):
    # Simula análise de densidade de cenas e elenco
    complexidade = random.uniform(0.5, 1.0)
    custo_est = complexidade * 50000
    otimizacao = custo_est * 0.15
    
    print(f"🤖 [TVC AI] Analisando Roteiro: {projeto}")
    print(f"📍 Complexidade de Produção: {int(complexidade*100)}%")
    print(f"💰 Custo Estimado: R$ {custo_est:,.2f}")
    print(f"💡 Sugestão AI: Agrupar locações no Porto Maravilha para economizar R$ {otimizacao:,.2f}.")
    
    os.system(f'say -v Luciana "Diretor, a inteligência artificial sugere uma economia de {int(otimizacao)} reais neste projeto."')

if __name__ == "__main__":
    analisar_roteiro_ai("ESTELIONATO CARIOCA")
