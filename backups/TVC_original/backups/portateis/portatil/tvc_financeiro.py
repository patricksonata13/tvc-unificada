def gerar_estimativa_projeto(nome_projeto, dias_set, equipe_num):
    custo_equipe_dia = 150.00  # Média TVC
    alimentacao_dia = equipe_num * 30.00
    total = (custo_equipe_dia * equipe_num + alimentacao_dia) * dias_set
    
    print(f"--- ORÇAMENTO ESTIMADO: {nome_projeto} ---")
    print(f"Dias de Set: {dias_set}")
    print(f"Tamanho da Equipe: {equipe_num}")
    print(f"Custo Total Estimado: R$ {total:.2f}")
    print("------------------------------------------")

if __name__ == "__main__":
    projeto = input("Nome do Projeto: ")
    gerar_estimativa_projeto(projeto, 3, 5) # Exemplo: 3 dias, 5 pessoas
