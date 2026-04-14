FROM debian:bookworm-slim
WORKDIR /app
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
     python3 \
     python3-fastapi \
     python3-uvicorn \
     python3-pydantic \
     python3-httpx \
     python3-psycopg2 \
     python3-pytest \
  && rm -rf /var/lib/apt/lists/*
COPY app ./app
COPY tests ./tests
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
