import json, os

def registar_take(projeto, cena, take, status):
    log = {
        "projeto": projeto,
        "cena": cena,
        "take": take,
        "qualidade": status,
        "timestamp": time.ctime()
    }
    path = os.path.expanduser(f"~/TVC4/TVC_STUDIOS/Brutos/LOG_{projeto}_{cena}.json")
    with open(path, "w") as f:
        json.dump(log, f)
    print(f"📊 Metadado de cena guardado para o Editor.")

if __name__ == "__main__":
    import time
    registar_take("ESTELIONATO", "CENA_01", "TAKE_03", "APROVADO")
