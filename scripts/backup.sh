#!/usr/bin/env bash
set -euo pipefail
mkdir -p backups
TS=$(date +%Y%m%d%H%M%S)
docker compose exec -T postgres pg_dump -U postgres devops_platform > backups/db-$TS.sql
echo "backup written: backups/db-$TS.sql"
