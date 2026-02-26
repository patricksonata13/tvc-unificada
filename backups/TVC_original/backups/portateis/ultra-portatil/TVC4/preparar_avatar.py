from gtts import gTTS
import os

noticia = "Sou a apresentadora virtual da TVC 4.0. No Diz Que de hoje: o 
Rio amanhece sob névoa cinza e muita música."
tts = gTTS(text=noticia, lang='pt', tld='com.br')
tts.save("audio_avatar.mp3")
print("✅ Áudio para o Avatar gerado! Suba este arquivo no HeyGen com a 
foto da TVC.")
