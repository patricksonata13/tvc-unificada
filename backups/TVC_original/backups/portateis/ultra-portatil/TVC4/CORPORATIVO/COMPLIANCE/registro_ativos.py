import hashlib, time

def registrar_ip(nome_projeto, tipo_ativo):
    timestamp = str(time.time())
    ip_id = hashlib.sha256((nome_projeto + timestamp).encode()).hexdigest()[:12].upper()
    
    registro = f"ATTVC-{ip_id}"
    print(f"🛡️ Ativo Registrado: {nome_projeto} | ID: {registro} | TIPO: {tipo_ativo}")
    
    with open(os.path.expanduser("~/TVC4/CORPORATIVO/COMPLIANCE/livro_registro_ip.txt"), "a") as f:
        f.write(f"{datetime.date.today()} | {registro} | {nome_projeto} | {tipo_ativo}\n")

if __name__ == "__main__":
    import os, datetime
    registrar_ip("ESTELIONATO CARIOCA", "ROTEIRO_PILOTO")
