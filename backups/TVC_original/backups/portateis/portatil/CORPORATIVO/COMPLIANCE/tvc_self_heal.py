import os, stat

def check_and_repair():
    paths = [
        "~/TVC4/CORPORATIVO/COMPLIANCE/tvc_master.key",
        "~/TVC4/tvc_admin.db"
    ]
    
    print("🛠️ Iniciando Auto-Reparo de Infraestrutura...")
    for p in paths:
        full_path = os.path.expanduser(p)
        if os.path.exists(full_path):
            # Garante que apenas o dono do Mac (Diretor) pode ler a chave
            os.chmod(full_path, stat.S_IRUSR | stat.S_IWUSR)
            print(f"✅ Permissões blindadas: {p}")
        else:
            print(f"❌ Alerta: {p} não encontrado. Notificando Direção.")

if __name__ == "__main__":
    check_and_repair()
