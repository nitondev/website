FROM python:3.11-slim

LABEL maintainer="lordhck@niton.dev"
LABEL org.opencontainers.image.source="https://github.com/nitondev/website"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:create_app()"]
