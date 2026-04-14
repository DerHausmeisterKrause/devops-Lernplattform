FROM debian:bookworm-slim
WORKDIR /app
RUN apt-get update \
  && apt-get install -y --no-install-recommends python3 python3-websockets \
  && rm -rf /var/lib/apt/lists/*
COPY server.py .
CMD ["python3", "server.py"]
