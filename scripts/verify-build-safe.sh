#!/usr/bin/env bash
set -euo pipefail

if grep -qE 'pip install --no-cache-dir -r requirements.txt' backend/Dockerfile terminal-gateway/Dockerfile; then
  echo "ERROR: legacy pip install step detected in Dockerfile(s)." >&2
  exit 1
fi

if grep -qE 'npm install' frontend/Dockerfile; then
  echo "ERROR: legacy npm install step detected in frontend Dockerfile." >&2
  exit 1
fi

echo "Dockerfiles are in offline-safe mode (no pip/npm registry install at build time)."
