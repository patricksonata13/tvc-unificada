#!/bin/bash
echo "🎬 INICIANDO OPERAÇÃO TOTAL - TVC 4.0 🚀"

# 1. Gerar Ativos Mentais
python3 ~/TVC4/gerar_cenario.py
python3 ~/TVC4/gerar_comercial.py

# 2. Processar Notícia do 'Diz Que'
python3 ~/TVC4/voz_tvc.py

# 3. Montar Vídeo de Estreia (FFmpeg)
python3 ~/TVC4/tvc_maker.py

# 4. Atualizar Grade do NovelFlix
python3 ~/TVC4/atualizar_grade.py

echo "✅ SISTEMA ONLINE. VÍDEO GERADO: ESTREIA_TVC4.mp4"
open ESTREIA_TVC4.mp4
