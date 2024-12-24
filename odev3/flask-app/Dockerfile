# Python tabanlı bir imaj kullanarak başla
FROM python:3.9-slim

# Çalışma dizinini oluştur
WORKDIR /app

# Gereksinim dosyasını kopyala
COPY requirements.txt /app/requirements.txt

# Gerekli paketleri yükle
RUN pip install -r requirements.txt

# Flask uygulama dosyasını kopyala
COPY . /app

# Uygulamayı çalıştır
CMD ["python", "app.py"]
