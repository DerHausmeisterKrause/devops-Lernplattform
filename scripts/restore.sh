#!/usr/bin/env bash
set -euo pipefail
LATEST=$(ls -1 backups/db-*.sql | tail -n1)
cat "$LATEST" | docker compose exec -T postgres psql -U postgres -d devops_platform
echo "restored from $LATEST"
