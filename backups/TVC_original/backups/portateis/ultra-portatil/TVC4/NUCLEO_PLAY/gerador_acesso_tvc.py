import sqlite3
import os
import qrcode

def gerar_qr_acessos():
    db_path = os.path.expanduser('~/TVC4/tvc_admin.db')
    output_dir = os.path.expanduser("~/TVC4/NUCLEO_PLAY/QR_CODES_ACESSO")
    os.makedirs(output_dir, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT nome, funcao FROM talentos')
    talentos = cursor.fetchall()
    
    print(f"🎟️ Gerando {len(talentos)} credenciais de acesso...")
    
    for nome, funcao in talentos:
        # Dados que estarão dentro do QR Code
        dados = f"TVC_STUDIOS_2026\nAUTORIZADO: {nome}\nFUNCAO: {funcao}\nSTATUS: ATIVO"
        
        # Criação do QR
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(dados)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        nome_arquivo = f"QR_{nome.replace(' ', '_')}.png"
        img.save(os.path.join(output_dir, nome_arquivo))
        
    print(f"✅ Sucesso! QR Codes salvos em: {output_dir}")
    conn.close()

if __name__ == "__main__":
    gerar_acesso_tvc()
