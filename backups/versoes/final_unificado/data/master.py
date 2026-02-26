# data/master.py
import random

MASTER_FINANCEIRO = {
    "equity_brl": 8240000,
    "equity_usd": 1650000,
    "receitas_2026": 12400000,
    "despesas_2026": 8900000,
    "lucro_2026": 3500000,
    "projetos": {
        "CATIÇO": {"orcamento": 800000, "gasto": 720000},
        "TEU SAMBA": {"orcamento": 410000, "gasto": 123000},
        "TRÊM": {"orcamento": 1200000, "gasto": 540000},
    }
}

def get_status():
    return {
        "cpu": random.randint(30, 70),
        "memoria": random.randint(40, 80),
        "disco": 78,
        "servicos": ["API", "Streaming", "Banco"],
        "tempo_ativo": "15 dias",
    }
