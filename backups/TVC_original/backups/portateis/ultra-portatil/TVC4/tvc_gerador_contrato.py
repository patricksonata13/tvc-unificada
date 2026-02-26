import sqlite3
import os
from datetime import datetime

def gerar_contrato_txt(talento_id):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    cursor.execute('SELECT nome, bairro, funcao FROM talentos WHERE id = ?', (talento_id,))
    talento = cursor.fetchone()
    conn.close()

    if not talento:
        print("❌ Talento não encontrado no Banco Raízes.")
        return

    nome, bairro, funcao = talento
    data_hoje = datetime.now().strftime('%d/%m/%Y')
    
    contrato = f"""
    ====================================================
    CONTRATO DE PRESTAÇÃO DE SERVIÇOS - TVC STUDIOS
    ====================================================
    CONTRATADA: {nome}
    FUNÇÃO: {funcao}
    BAIRRO DE ATUAÇÃO: {bairro}
    
    Pelo presente instrumento, a TVC (Mini Projac Integrado) 
    autoriza a prestação de serviços para produções do 
    catálogo original sob as normas de segurança e 
    identidade cultural da emissora.
    
    DATA DE EMISSÃO: {data_hoje}
    ----------------------------------------------------
    Assinatura Direção TVC: ____________________________
    Assinatura Contratado: _____________________________
    ====================================================
    """
    
    nome_arquivo = f"Contrato_TVC_{nome.replace(' ', '_')}.txt"
    caminho = os.path.expanduser(f'~/TVC4/TVC_STUDIOS/Contratos/{nome_arquivo}')
    
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    
    with open(caminho, 'w') as f:
        f.write(contrato)
    
    print(f"📄 Contrato gerado com sucesso: {nome_arquivo}")

if __name__ == "__main__":
    print("--- GERADOR DE CONTRATOS TVC ---")
    id_busca = input("Digite o ID do talento no Banco Raízes: ")
    gerar_contrato_txt(id_busca)
