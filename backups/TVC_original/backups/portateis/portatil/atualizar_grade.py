import os

def atualizar_playlist():
    caminho_grade = os.path.expanduser("~/TVC4/grade.txt")
    base = "Assets"
    
    # Definindo a sequência
    playlist = [
        f"file '{base}/Novelas/cap05.mp4'",
        f"file 'ESTREIA_TVC4.mp4'", # O plantão do Diz Que
        f"file 'Comercial_Padrao.mp4'" # Vinheta de patrocínio
    ]
    
    with open(caminho_grade, "w") as f:
        for item in playlist:
            f.write(f"{item}\n")
    
    print("📅 Grade de programação atualizada!")

if __name__ == "__main__":
    atualizar_playlist()
