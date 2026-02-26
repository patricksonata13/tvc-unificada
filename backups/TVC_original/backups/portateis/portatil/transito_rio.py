import os
def salvar():
    msg = "PONTE: Fluxo Normal | LINHA VERMELHA: Retencao no Caju | AV. BRASIL: Livre"
    path = os.path.expanduser("~/TVC4/Assets/status_transito.txt")
    with open(path, "w") as f:
        f.write(msg)
    print("🚗 Transito atualizado!")
if __name__ == "__main__":
    salvar()
