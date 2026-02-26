# Este módulo prepara o arquivo .srt para ser "queimado" no vídeo via FFmpeg
def criar_legenda_teste(projeto):
    path = os.path.expanduser(f"~/TVC4/TVC_STUDIOS/Assets/{projeto}.srt")
    conteudo = """
1
00:00:01,000 --> 00:00:04,000
TVC STUDIOS APRESENTA:
    """
    with open(path, "w") as f:
        f.write(conteudo)
    print(f"📝 Template de legenda criado para {projeto}.")

# Integrado ao FFmpeg: -vf "subtitles=legenda.srt"
