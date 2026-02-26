import sqlite3, os, datetime

def fluxo_aprovacao(projeto, status_video):
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    cursor = conn.cursor()
    
    if status_video == "APROVADO":
        print(f"🌟 Projeto {projeto}: Vídeo Aprovado pelo Diretor.")
        # Atualiza o Pipeline automaticamente
        cursor.execute('UPDATE pipeline SET fase = "FINALIZADO" WHERE nome = ?', (projeto,))
        # Gera ordem de pagamento fictícia no log
        data = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"💰 FINANCEIRO: Ordem de pagamento liberada em {data} para equipe de {projeto}.")
    else:
        print(f"⚠️ Projeto {projeto}: Vídeo retornou para edição (NÚCLEO STUDIOS).")
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    proj = input("Nome do Projeto para aprovação: ").upper()
    status = input("Status (APROVADO/REPROVADO): ").upper()
    fluxo_aprovacao(proj, status)
