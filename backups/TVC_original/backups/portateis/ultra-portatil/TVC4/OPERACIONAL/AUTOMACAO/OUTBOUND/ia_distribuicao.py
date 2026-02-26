import datetime, os

def agendar_postagem_ia(video_nome):
    agora = datetime.datetime.now()
    # IA sugere postagem no horário nobre (20:00) do dia seguinte
    data_post = (agora + datetime.timedelta(days=1)).replace(hour=20, minute=0)
    
    log_dist = f"🚀 [TVC DIST] Video: {video_nome} | Agendado para: {data_post.strftime('%d/%m %H:%M')}\n"
    
    with open(os.path.expanduser("~/TVC4/.system_logs/distribuicao.log"), "a") as f:
        f.write(log_dist)
    
    print(f"📡 IA de Distribuição: {video_nome} programado para o pico de audiência.")
    os.system(f'say -v Luciana "Diretor, o algoritmo de distribuição agendou o lançamento para amanhã."')

if __name__ == "__main__":
    agendar_postagem_ia("ESTELIONATO_CARIOCA_PILOTO.mp4")
