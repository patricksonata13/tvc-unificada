import os
import sqlite3

def auditoria():
    os_dir = os.path.expanduser("~/TVC4/NUCLEO_ECO/ORDENS_SERVICO")
    num_os = len(os.listdir(os_dir))
    custo_estimado_os = num_os * 250.00  # Valor médio de diária base
    
    orcamento_total = 45000.00
    saldo = orcamento_total - custo_estimado_os
    
    print("\n" + "💰" * 20)
    print("      AUDITORIA DE CUSTOS TVC")
    print("💰" * 20)
    print(f"O.S. EMITIDAS: {num_os}")
    print(f"COMPROMETIDO: R$ {custo_estimado_os:,.2f}")
    print(f"SALDO RESTANTE: R$ {saldo:,.2f}")
    
    if saldo < 5000:
        print("⚠️ ALERTA: Orçamento em nível crítico!")
        os.system('say -v Luciana "Diretor, atenção ao orçamento. O saldo está baixo."')
    print("💰" * 20 + "\n")

if __name__ == "__main__":
    auditoria()
