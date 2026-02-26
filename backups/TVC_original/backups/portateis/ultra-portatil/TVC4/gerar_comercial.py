import os
from gtts import gTTS

def criar_comercial(marca, slogan):
    base_dir = os.path.expanduser("~/TVC4/Assets/Comerciais")
    audio_path = os.path.join(base_dir, f"comercial_{marca}.mp3")
    
    texto_comercial = f"Este bloco é um oferecimento de {marca}. {slogan}. 
TVC 4.0, a imagem do Rio."
    
    print(f"💰 Gerando comercial para: {marca}")
    
    # Gerar Voz do Comercial
    tts = gTTS(text=texto_comercial, lang='pt', tld='com.br')
    tts.save(audio_path)
    
    # Aqui o sistema avisaria o Master Control para inserir o card da 
marca
    print(f"✅ Comercial pronto em: {audio_path}")

if __name__ == "__main__":
    # Exemplo: Patrocínio de uma marca de café do Rio
    criar_comercial("Café Carioca", "O sabor do despertar no Jardim 
Botânico")
