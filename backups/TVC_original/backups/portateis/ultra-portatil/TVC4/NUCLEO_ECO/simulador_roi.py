import os

def calcular_roi(investimento_total, assinantes_meta, preco_assinatura):
    faturamento_mensal = assinantes_meta * preco_assinatura
    faturamento_anual = faturamento_mensal * 12
    roi = ((faturamento_anual - investimento_total) / investimento_total) * 100
    ponto_equilibrio = investimento_total / preco_assinatura

    report = f"""
    =============================================
          TVC ECONOMY: PROJEÇÃO DE RETORNO
    =============================================
    Investimento Total: R$ {investimento_total:,.2f}
    Meta de Assinantes: {assinantes_meta}
    Mensalidade: R$ {preco_assinatura:,.2f}
    ---------------------------------------------
    Faturamento Anual Est.: R$ {faturamento_anual:,.2f}
    ROI Estimado (12 meses): {roi:.1f}%
    Ponto de Equilíbrio: {ponto_equilibrio:.0f} assinaturas
    =============================================
    """
    print(report)
    
    path = os.path.expanduser("~/TVC4/NUCLEO_ECO/ULTIMA_PROJECAO_ROI.txt")
    with open(path, "w") as f:
        f.write(report)

if __name__ == "__main__":
    print("--- SIMULADOR DE NEGÓCIOS TVC ---")
    try:
        inv = float(input("Investimento total estimado (R$): "))
        meta = int(input("Meta de assinantes ativos: "))
        preco = float(input("Preço da assinatura mensal (R$): "))
        calcular_roi(inv, meta, preco)
    except ValueError:
        print("❌ Erro: Digite apenas números.")
