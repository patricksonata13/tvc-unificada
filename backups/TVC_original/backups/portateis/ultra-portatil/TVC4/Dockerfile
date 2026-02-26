FROM python:3.11-slim

WORKDIR /app

# Instalar dependências
RUN pip install flask flask-cors psutil

# Copiar projeto
COPY . .

# Expor porta
EXPOSE 5001

# Comando para iniciar
CMD ["python3", "PLATAFORMA_WEB/backend/app.py"]
