import random

def analisar_prioridade(noticia):
    # Lógica de IA para decidir se vira plantão
    palavras_chave = ["urgente", "interditado", "tiroteio", "temporal"]
    if any(palavra in noticia.lower() for palabra in palavras_chave):
        return "ALTA"
    return "NORMAL"

# Simulação de banco de dados do seu app 'Diz Que'
denuncias_recentes = [
    "Trânsito lento na Lapa",
    "URGENTE: Linha Amarela interditada por acidente grave",
    "Céu limpo no Arpoador"
]

for d in denuncias_recentes:
    prioridade = analisar_prioridade(d)
    print(f"🔍 Analisando: '{d}' | Prioridade: {prioridade}")
    if prioridade == "ALTA":
        print("🚨 Disparando Gatilho de Plantão na TVC 4.0!")
