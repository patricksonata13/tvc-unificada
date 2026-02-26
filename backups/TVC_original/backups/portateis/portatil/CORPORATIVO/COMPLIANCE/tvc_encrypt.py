import os
from cryptography.fernet import Fernet

# Gerar ou carregar a chave mestra
key_path = os.path.expanduser("~/TVC4/CORPORATIVO/COMPLIANCE/tvc_master.key")
if not os.path.exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as f: f.write(key)
else:
    with open(key_path, "rb") as f: key = f.read()

fernet = Fernet(key)

def proteger_arquivo(caminho):
    with open(caminho, "rb") as f: data = f.read()
    encrypted = fernet.encrypt(data)
    with open(caminho + ".tvc", "wb") as f: f.write(encrypted)
    os.remove(caminho) # Remove o original aberto
    print(f"🔒 Ficheiro blindado: {os.path.basename(caminho)}")

if __name__ == "__main__":
    # Exemplo: Protege a Bíblia do Estelionato
    biblia = os.path.expanduser("~/TVC4/NUCLEO_PRO/BIBLIA_ESTELIONATO_CARIOCA.txt")
    if os.path.exists(biblia): proteger_arquivo(biblia)
