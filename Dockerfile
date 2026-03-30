FROM python:3.11-slim

# Configuraciones de entorno (evita que Python escriba binarios y mantenga stdin abierto para debug)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Primero las dependencias para que se cacheen si no se alteran
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el todo lo demás de la aplicación
COPY . .

# Exponer el puerto por el que corre Uvicorn (8000)
EXPOSE 8000

# El default, sobreescrito frecuentemente por el docker-compose
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
