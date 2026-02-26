#!/usr/bin/env python3
# API da TVC Studios - VERSÃO CORRIGIDA

from flask import Flask, jsonify, send_file, request, send_from_directory
from flask_cors import CORS
import os
import json
import datetime
from pathlib import Path

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

BASE = os.path.expanduser("~/TVC4")

# ============================================
# ROTAS DA API
# ============================================

@app.route('/')
def serve_frontend():
    """Serve o frontend"""
    return send_file(os.path.join(BASE, 'PLATAFORMA_WEB', 'frontend', 'index.html'))

@app.route('/api')
def api_home():
    return jsonify({
        "nome": "TVC Studios API",
        "versao": "1.0.0",
        "status": "online",
        "data": datetime.datetime.now().isoformat(),
        "endpoints": [
            "/api/stats - Estatísticas",
            "/api/videos - Lista de vídeos",
            "/api/projetos - Projetos",
            "/api/financeiro - Dados financeiros",
            "/api/status - Status do hardware"
        ]
    })

# ===== PROJETOS =====
@app.route('/api/projetos')
def listar_projetos():
    try:
        with open(f"{BASE}/GESTAO/projetos.json", 'r') as f:
            projetos = json.load(f)
        return jsonify(projetos)
    except Exception as e:
        return jsonify({"erro": str(e), "arquivo": "projetos.json"}), 404

# ===== FINANCEIRO =====
@app.route('/api/financeiro')
def get_financeiro():
    try:
        with open(f"{BASE}/GESTAO/dados_financeiros.json", 'r') as f:
            fin = json.load(f)
        return jsonify(fin)
    except Exception as e:
        return jsonify({"erro": str(e), "arquivo": "dados_financeiros.json"}), 404

# ===== HARDWARE =====
@app.route('/api/status')
def get_status():
    try:
        import psutil
        status = {
            "cpu": psutil.cpu_percent(),
            "memoria": psutil.virtual_memory().percent,
            "disco": psutil.disk_usage('/').percent,
            "tempo": datetime.datetime.now().strftime("%H:%M:%S"),
            "data": datetime.datetime.now().strftime("%d/%m/%Y")
        }
        return jsonify(status)
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ===== LISTAR VÍDEOS =====
@app.route('/api/videos')
def listar_videos():
    videos = []
    
    # Vídeos brutos
    brutos = f"{BASE}/TVC_STUDIOS/Brutos"
    if os.path.exists(brutos):
        for f in os.listdir(brutos):
            if f.endswith('.mp4'):
                videos.append({
                    "nome": f,
                    "tipo": "bruto",
                    "caminho": f"/api/video/bruto/{f}"
                })
    
    # Vídeos finalizados
    finalizados = f"{BASE}/TVC_STUDIOS/Finalizados"
    if os.path.exists(finalizados):
        for f in os.listdir(finalizados):
            if f.endswith('.mp4'):
                videos.append({
                    "nome": f,
                    "tipo": "finalizado",
                    "caminho": f"/api/video/finalizado/{f}"
                })
    
    return jsonify(videos)

# ===== SERVIR VÍDEOS =====
@app.route('/api/video/<tipo>/<nome>')
def servir_video(tipo, nome):
    if tipo == 'bruto':
        pasta = f"{BASE}/TVC_STUDIOS/Brutos"
    elif tipo == 'finalizado':
        pasta = f"{BASE}/TVC_STUDIOS/Finalizados"
    else:
        return jsonify({"erro": "Tipo inválido"}), 404
    
    caminho = os.path.join(pasta, nome)
    if os.path.exists(caminho):
        return send_file(caminho, mimetype='video/mp4')
    else:
        return jsonify({"erro": "Arquivo não encontrado"}), 404

# ===== LEGENDAS =====
@app.route('/api/legendas/<idioma>/<nome>')
def servir_legenda(idioma, nome):
    nome_srt = nome.replace('.mp4', f'.{idioma}.srt')
    caminho = f"{BASE}/TVC_STUDIOS/LEGENDAS/{idioma.upper()}/{nome_srt}"
    
    if os.path.exists(caminho):
        return send_file(caminho, mimetype='text/plain')
    else:
        return jsonify({"erro": "Legenda não encontrada"}), 404

# ===== ESTATÍSTICAS =====
@app.route('/api/stats')
def get_stats():
    stats = {
        "videos": {
            "brutos": len(os.listdir(f"{BASE}/TVC_STUDIOS/Brutos")) if os.path.exists(f"{BASE}/TVC_STUDIOS/Brutos") else 0,
            "finalizados": len(os.listdir(f"{BASE}/TVC_STUDIOS/Finalizados")) if os.path.exists(f"{BASE}/TVC_STUDIOS/Finalizados") else 0
        },
        "projetos": 0,
        "equity": 0,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    try:
        with open(f"{BASE}/GESTAO/projetos.json", 'r') as f:
            proj = json.load(f)
            stats["projetos"] = len(proj.get('projetos', []))
    except:
        pass
        
    try:
        with open(f"{BASE}/GESTAO/dados_financeiros.json", 'r') as f:
            fin = json.load(f)
            stats["equity"] = fin.get('equity_brl', 0)
    except:
        pass
    
    return jsonify(stats)

if __name__ == '__main__':
    print(f"\n{'='*50}")
    print("🚀 TVC Studios API")
    print(f"{'='*50}")
    print(f"📁 Base path: {BASE}")
    print(f"📊 Stats: {BASE}/GESTAO/")
    print(f"🎬 Vídeos: {BASE}/TVC_STUDIOS/")
    print(f"{'='*50}\n")
    app.run(host='0.0.0.0', port=5001, debug=True)

# ===== PROCESSAR VÍDEO =====
@app.route('/api/processar', methods=['POST'])
def processar_video():
    import subprocess
    dados = request.get_json()
    video = dados.get('video')
    
    cmd = ['python3', f"{BASE}/tvc_processor.py"]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "processando", "video": video})

# ===== CRIAR LEGENDA =====
@app.route('/api/legendas/criar', methods=['POST'])
def criar_legenda():
    import subprocess
    dados = request.get_json()
    video = dados.get('video')
    
    cmd = ['python3', f"{BASE}/AUTOMACOES/legendas_simples.py"]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "gerando legendas", "video": video})

# ===== BACKUP =====
@app.route('/api/backup', methods=['POST'])
def fazer_backup():
    import subprocess
    cmd = ['python3', f"{BASE}/AUTOMACOES/backup_automatico.py", 'agora']
    subprocess.Popen(cmd)
    return jsonify({"status": "backup iniciado"})

# ===== RELATÓRIOS =====
@app.route('/api/relatorios/gerar', methods=['POST'])
def gerar_relatorio():
    import subprocess
    cmd = ['python3', f"{BASE}/AUTOMACOES/relatorios_automaticos.py", 'agora']
    subprocess.Popen(cmd)
    return jsonify({"status": "relatório gerado"})

# ===== DOWNLOAD VÍDEO =====
@app.route('/api/download', methods=['POST'])
def download_video():
    import subprocess
    dados = request.get_json()
    url = dados.get('url')
    
    cmd = ['yt-dlp', '-o', f"{BASE}/TVC_STUDIOS/Brutos/%(title)s.%(ext)s", url]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "download iniciado"})

# ===== FERRAMENTAS =====
@app.route('/api/ferramentas/<nome>')
def abrir_ferramenta(nome):
    import subprocess
    apps = {
        'obs': 'OBS',
        'gimp': 'GIMP',
        'audacity': 'Audacity',
        'handbrake': 'HandBrake'
    }
    if nome in apps:
        subprocess.Popen(['open', '-a', apps[nome]])
    return jsonify({"status": "aberto"})

# ===== PROCESSAR VÍDEO =====
@app.route('/api/processar', methods=['POST'])
def processar_video():
    import subprocess
    dados = request.get_json()
    video = dados.get('video')
    
    cmd = ['python3', f"{BASE}/tvc_processor.py"]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "processando", "video": video})

# ===== CRIAR LEGENDA =====
@app.route('/api/legendas/criar', methods=['POST'])
def criar_legenda():
    import subprocess
    dados = request.get_json()
    video = dados.get('video')
    
    cmd = ['python3', f"{BASE}/AUTOMACOES/legendas_simples.py"]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "gerando legendas", "video": video})

# ===== BACKUP =====
@app.route('/api/backup', methods=['POST'])
def fazer_backup():
    import subprocess
    cmd = ['python3', f"{BASE}/AUTOMACOES/backup_automatico.py", 'agora']
    subprocess.Popen(cmd)
    return jsonify({"status": "backup iniciado"})

# ===== RELATÓRIOS =====
@app.route('/api/relatorios/gerar', methods=['POST'])
def gerar_relatorio():
    import subprocess
    cmd = ['python3', f"{BASE}/AUTOMACOES/relatorios_automaticos.py", 'agora']
    subprocess.Popen(cmd)
    return jsonify({"status": "relatório gerado"})

# ===== DOWNLOAD VÍDEO =====
@app.route('/api/download', methods=['POST'])
def download_video():
    import subprocess
    dados = request.get_json()
    url = dados.get('url')
    
    cmd = ['yt-dlp', '-o', f"{BASE}/TVC_STUDIOS/Brutos/%(title)s.%(ext)s", url]
    subprocess.Popen(cmd)
    
    return jsonify({"status": "download iniciado"})

# ===== FERRAMENTAS =====
@app.route('/api/ferramentas/<nome>')
def abrir_ferramenta(nome):
    import subprocess
    apps = {
        'obs': 'OBS',
        'gimp': 'GIMP',
        'audacity': 'Audacity',
        'handbrake': 'HandBrake'
    }
    if nome in apps:
        subprocess.Popen(['open', '-a', apps[nome]])
    return jsonify({"status": "aberto"})

# ===== AÇÕES DOS MÓDULOS =====
@app.route('/api/processar', methods=['POST'])
def processar_videos():
    import subprocess
    subprocess.Popen(['python3', f"{BASE}/tvc_processor.py"])
    return jsonify({"status": "processando"})

@app.route('/api/legendas/criar', methods=['POST'])
def criar_legendas():
    import subprocess
    subprocess.Popen(['python3', f"{BASE}/AUTOMACOES/legendas_simples.py"])
    return jsonify({"status": "gerando legendas"})

@app.route('/api/backup', methods=['POST'])
def fazer_backup():
    import subprocess
    subprocess.Popen(['python3', f"{BASE}/AUTOMACOES/backup_automatico.py", 'agora'])
    return jsonify({"status": "backup iniciado"})

@app.route('/hud')
def hud():
    return send_file(os.path.join(BASE, 'GESTAO', 'hud_tvc_deluxe.py'))

# ===== ROTA PARA DADOS DOS PROJETOS =====
@app.route('/api/projetos/completo')
def projetos_completo():
    return send_file(os.path.join(BASE, 'PLATAFORMA_WEB', 'frontend', 'index.html'))
