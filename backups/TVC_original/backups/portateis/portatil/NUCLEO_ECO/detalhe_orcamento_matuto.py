def calcular_episodio():
    total_temporada = 45000.00
    episodios = 10
    custo_ep = total_temporada / episodios
    
    print(f"--- ANÁLISE FINANCEIRA: O MATUTO ---")
    print(f"Custo por Episódio: R$ {custo_ep:.2f}")
    print(f"Distribuição sugerida por EP:")
    print(f"- Cachets: R$ {custo_ep * 0.4:.2f}")
    print(f"- Logística/Set: R$ {custo_ep * 0.3:.2f}")
    print(f"- Pós-Produção: R$ {custo_ep * 0.2:.2f}")
    print(f"- Fundo de Emergência: R$ {custo_ep * 0.1:.2f}")
    print("-------------------------------------")

if __name__ == "__main__":
    calcular_episodio()
