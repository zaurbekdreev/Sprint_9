FROM python:3.13
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y chromium chromium-driver
ENV CHROME_BIN=/usr/bin/chromium
ENV DISPLAY=:99
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
