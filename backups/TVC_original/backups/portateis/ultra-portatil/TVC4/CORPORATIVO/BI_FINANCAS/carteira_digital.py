import json, os

def atualizar_financeiro(projeto, receita, custo):
    margem = receita - custo
    dados = {
        "projeto": projeto,
        "receita_bruta": receita,
        "custo_operacional": custo,
        "margem_liquida": margem
    }
    path = os.path.expanduser(f"~/TVC4/CORPORATIVO/BI_FINANCAS/BALANCO_{projeto}.json")
    with open(path, "w") as f:
        json.dump(dados, f, indent=4)
    print(f"💰 Balanço de {projeto} atualizado.")

if __name__ == "__main__":
    atualizar_financeiro("ESTELIONATO_CARIOCA", 50000, 15000)
