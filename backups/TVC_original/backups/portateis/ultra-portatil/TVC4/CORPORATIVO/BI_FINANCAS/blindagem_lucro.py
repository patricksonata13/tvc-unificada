import json, os

def calcular_resultado_real(receita_bruta):
    impostos = receita_bruta * 0.165  # Simulação de Lucro Presumido
    custos_fixos = receita_bruta * 0.20
    reserva_expansao = receita_bruta * 0.10
    lucro_liquido = receita_bruta - impostos - custos_fixos - reserva_expansao
    
    balanco = {
        "receita_bruta": receita_bruta,
        "impostos_provisionados": impostos,
        "reserva_tecnica": reserva_expansao,
        "lucro_real_distribuivel": lucro_liquido
    }
    
    path = os.path.expanduser("~/TVC4/CORPORATIVO/BI_FINANCAS/BALANCO_REAL_TVC.json")
    with open(path, "w") as f:
        json.dump(balanco, f, indent=4)
    print(f"📊 Blindagem Fiscal Concluída. Lucro Real: R$ {lucro_liquido:,.2f}")

if __name__ == "__main__":
    calcular_resultado_real(286350.00) # Exemplo baseado nos 23 projetos
