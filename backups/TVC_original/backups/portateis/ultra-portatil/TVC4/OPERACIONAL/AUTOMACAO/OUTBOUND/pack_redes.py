import os

def preparar_post(video_nome):
    pasta_redes = os.path.expanduser("~/TVC4/OPERACIONAL/AUTOMACAO/OUTBOUND/REDES_SOCIAIS")
    projeto_nome = video_nome.split("_")[2] # Extrai o nome do projeto do arquivo
    
    metadata = f"""
    --- POST CONFIG: {video_nome} ---
    PROJETO: {projeto_nome}
    LEGENDA: Assista agora a mais um original TVC STUDIOS. #TVC #RiodeJaneiro #Cinema
    CTA: Link na Bio para o TVC PLAY.
    ---------------------------------
    """
    
    with open(f"{pasta_redes}/POST_{video_nome}.txt", "w") as f:
        f.write(metadata)
    print(f"📱 Pack de Redes Sociais criado para {video_nome}")

if __name__ == "__main__":
    # Roda para o último vídeo entregue
    preparar_post("TVC_FINAL_ESTELIONATO_E01.mp4")
