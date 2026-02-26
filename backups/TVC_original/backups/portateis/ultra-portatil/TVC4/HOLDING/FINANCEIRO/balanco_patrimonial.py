import os, sqlite3

def calcular_equity():
    # Valor por vídeo finalizado: R$ 5.000,00 (Valor de mercado estimado)
    finalizados = len(os.listdir(os.path.expanduser("~/TVC4/TVC_STUDIOS/Finalizados")))
    valor_ativos = finalizados * 5000.00
    
    # Valor do Banco Raízes (Intangível): R$ 1.000,00 por talento cadastrado
    conn = sqlite3.connect(os.path.expanduser('~/TVC4/tvc_admin.db'))
    num_talentos = conn.execute('SELECT count(*) FROM talentos').fetchone()[0]
    valor_humano = num_talentos * 1000.00
    
    total_empresa = valor_ativos + valor_humano
    
    print(f"\n==== VALUATION TVC STUDIOS ====")
    print(f"Ativos Digitais: R$ {valor_ativos:,.2f}")
    print(f"Capital Humano: R$ {valor_humano:,.2f}")
    print(f"VALOR DE MERCADO (EST.): R$ {total_empresa:,.2f}")
    print(f"===============================\n")

if __name__ == "__main__":
    calcular_equity()
