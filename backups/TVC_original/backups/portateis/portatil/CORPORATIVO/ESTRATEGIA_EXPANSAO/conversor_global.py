import json, os

def converter_para_global():
    path_financeiro = os.path.expanduser("~/TVC4/CORPORATIVO/BI_FINANCAS/BALANCO_REAL_TVC.json")
    with open(path_financeiro, "r") as f:
        dados = json.load(f)
    
    taxa_usd = 5.20 # Câmbio projetado
    equity_usd = dados["lucro_real_distribuivel"] / taxa_usd
    
    print(f"🌍 Global Mode: Equity Estimado em U$ {equity_usd:,.2f}")
    return equity_usd

if __name__ == "__main__":
    converter_para_global()
