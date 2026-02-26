#!/usr/bin/env python3
import os, json
with open(os.path.expanduser("~/TVC4/GESTAO/dados_financeiros.json")) as f:
    d = json.load(f)
print(f"\n💰 Equity: R$ {d['equity_brl']:,.2f}")
