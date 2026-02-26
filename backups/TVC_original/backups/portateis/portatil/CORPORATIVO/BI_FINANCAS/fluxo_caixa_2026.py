import datetime

def projetar_gastos():
    custo_fixo_talentos = 147 * 12500.00 # Baseado no Banco Raízes
    custo_producao_projeto = 45000.00
    num_projetos = 23
    
    total_investimento = (custo_fixo_talentos * 3) + (custo_producao_projeto * num_projetos)
    
    print("="*50)
    print(f"       TVC HOLDING - PROJEÇÃO FINANCEIRA Q1")
    print("="*50)
    print(f"Data de Emissão: {datetime.date.today()}")
    print(f"Custo Fixo Trimestral (RH): R$ {custo_fixo_talentos * 3:,.2f}")
    print(f"Custo Total Produção (23 Proj): R$ {custo_producao_projeto * num_projetos:,.2f}")
    print("-" * 50)
    print(f"EXPOSIÇÃO TOTAL DE CAPITAL: R$ {total_investimento:,.2f}")
    print("="*50)

if __name__ == "__main__":
    projetar_gastos()
