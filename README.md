# DevOps Lernplattform

Monorepo für eine DevOps/Linux Lernplattform ohne KI-Funktionen.

## Quickstart
1. `make dev` (bereinigt alte Docker-Builder-Caches und baut alle Images frisch)
2. Frontend: http://localhost:3000
3. API: http://localhost:8080/docs

## Services
- frontend
- backend (FastAPI)
- terminal-gateway (WebSocket + PTY)
- grader
- postgres
- minio

## Kernkommandos
- `make test`
- `make e2e`
- `make deploy`
- `make backup`
- `make restore`

## Falls weiterhin alter Build-Kontext genutzt wird
- `git pull`
- `docker compose down --remove-orphans`
- `docker builder prune -af`
- `make dev`
