def gerar_checkout(projeto):
    base_url = "https://play.tvc.com.br/assine?ref="
    link = f"{base_url}{projeto.lower()}"
    
    print("\n" + "="*40)
    print(f"🚀 LINK DE VENDA GERADO: {projeto}")
    print("="*40)
    print(f"Link: {link}")
    print("Encaminhe para o núcleo de Social Media.")
    print("="*40 + "\n")

if __name__ == "__main__":
    p = input("Nome do Projeto para Venda: ")
    gerar_checkout(p)
