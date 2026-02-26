import json, os

def taguear_conteudo(arquivo, categoria, tags):
    metadados = {
        "arquivo": arquivo,
        "categoria": categoria,
        "tags": tags.split(","),
        "plataforma": "TVC PLAY 1.0"
    }
    
    nome_meta = arquivo.split(".")[0] + "_meta.json"
    path = os.path.expanduser(f"~/TVC4/NUCLEO_PLAY/CONTEUDO_PUBLICADO/{nome_meta}")
    
    with open(path, "w") as f:
        json.dump(metadados, f, indent=4)
    print(f"🏷️ Metadados criados para {arquivo}. Pronto para o algoritmo!")

if __name__ == "__main__":
    arq = input("Nome do arquivo de vídeo: ")
    cat = input("Categoria (Drama/Comédia/Documentário): ")
    t = input("Tags (separadas por vírgula): ")
    taguear_conteudo(arq, cat, t)
