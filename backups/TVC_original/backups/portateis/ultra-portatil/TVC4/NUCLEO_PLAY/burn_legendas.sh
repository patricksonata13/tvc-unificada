# Exemplo de comando para queimar legenda em um vídeo finalizado
# Uso: ./burn_legendas.sh video.mp4 legenda.srt
ffmpeg -i $1 -vf "subtitles=$2:force_style='FontSize=24,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3'" -c:a copy output_legendado.mp4
