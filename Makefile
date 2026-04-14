SHELL := /bin/bash

.PHONY: dev down test e2e lint build docker deploy backup restore

dev:
	docker compose up --build -d

down:
	docker compose down -v

test:
	docker compose run --rm backend pytest -q

e2e:
	docker compose run --rm e2e npm test

lint:
	docker compose run --rm backend ruff check app tests

build:
	docker compose build

docker: build

deploy:
	helm upgrade --install devops-platform ./deploy/helm/devops-platform -f ./deploy/helm/devops-platform/values-dev.yaml

backup:
	./scripts/backup.sh

restore:
	./scripts/restore.sh
