#!/usr/bin/env python3
import os, json
with open(os.path.expanduser("~/TVC4/GESTAO/projetos.json")) as f:
    d = json.load(f)
print("\n📋 PROJETOS:")
for p in d['projetos']:
    print(f"   {p['nome']} - {p['status']} - {p['progresso']}%")
