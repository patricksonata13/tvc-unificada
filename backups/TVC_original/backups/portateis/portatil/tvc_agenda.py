import json
import os

AGENDA_FILE = os.path.expanduser('~/TVC4/tvc_agenda.json')

def carregar_agenda():
    if not os.path.exists(AGENDA_FILE): return {}
    with open(AGENDA_FILE, 'r') as f: return json.load(f)

def agendar_gravacao(data, projeto, local):
    agenda = carregar_agenda()
    if data in agenda:
        print(f"⚠️ CONFLITO! O projeto '{agenda[data]['projeto']}' já está no set em {data}.")
    else:
        agenda[data] = {"projeto": projeto, "local": local}
        with open(AGENDA_FILE, 'w') as f: json.dump(agenda, f, indent=4)
        print(f"📅 Gravado! {projeto} confirmado para {data} em {local}.")

if __name__ == "__main__":
    d = input("Data (DD/MM/AAAA): ")
    p = input("Nome do Projeto: ")
    l = input("Locação: ")
    agendar_gravacao(d, p, l)
