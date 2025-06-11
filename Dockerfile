# Etap 1: build obrazu
FROM python:3.11-slim

# Zmienna środowiskowa
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Aktualizacja i podstawowe pakiety
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki
COPY . .

# Instalacja zależności
RUN pip install --upgrade pip && pip install -r requirements.txt

# Zbierz statyczne pliki
RUN python manage.py collectstatic --noinput

# Otwórz port
EXPOSE 8000

# Uruchom aplikację Django przez gunicorn
CMD ["gunicorn", "marmurshop.wsgi:application", "--bind", "0.0.0.0:8000"]
