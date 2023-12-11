ifneq ($(wildcard docker/.env.example),)
	ENV_FILE = .env.example
endif
ifneq ($(wildcard .env.example),)
	ifeq ($(COMPOSE_PROJECT_NAME),)
		include .env.example
	endif
endif
ifneq ($(wildcard docker/.env),)
	ENV_FILE = .env
endif
ifneq ($(wildcard .env),)
	ifeq ($(COMPOSE_PROJECT_NAME),)
		include .env
	endif
endif

export

.SILENT:
.PHONY: help
help: ## Display this help screen
	awk 'BEGIN {FS = ":.*##"; printf "Usage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) }' $(MAKEFILE_LIST)

.PHONY: install
install: ## Installations
	poetry env use python
	poetry install

.PHONY: lint
lint: ## Run linters
	poetry run isort .
	poetry run flake8
	poetry run mypy .

.PHONY: run
run: ## Run applications
	make migrate-up
	make -j 2 run-backend


.PHONY: run-backend
run-backend: ## Run backend
	poetry run gunicorn --reload --bind $(HOST):$(BACKEND_PORT) \
	--worker-class uvicorn.workers.UvicornWorker \
	--workers $(WORKERS) --log-level $(LEVEL) --chdir cmd/app main:app

.PHONY: migrate-create
migrate-create: ## Create a new revision file
	poetry run alembic revision --autogenerate -m $(name)

.PHONY: migrate-up
migrate-up: ## Upgrade to a later version
	poetry run alembic upgrade head

.PHONY: migrate-down
migrate-down: ## Revert to a previous version
	poetry run alembic downgrade $(revision)

