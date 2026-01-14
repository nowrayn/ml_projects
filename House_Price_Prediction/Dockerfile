FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port ${PORT:-8000}"]







###### for local, it works #####

# FROM python:3.10-slim

# # Set working directory
# WORKDIR /app

# # Copy requirements first (better caching)
# COPY requirements.txt .

# # Install dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy application files
# COPY . .

# # Expose FastAPI port
# EXPOSE 8000

# # Run FastAPI app
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
