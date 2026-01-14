FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Render exposes PORT env var — MUST use it
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:$PORT"]

