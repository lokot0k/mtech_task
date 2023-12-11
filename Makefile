ifneq ($(wildcard backend/docker/.env),)
	ENV_FILE = .env
endif
ifneq ($(wildcard backend/.env),)
	ifeq ($(COMPOSE_PROJECT_NAME),)
		include backend/.env
	endif
endif

export

.SILENT:
.PHONY: compose-up
compose-up: ## Create and start containers
	echo $(ENV_FILE)
	docker-compose -f docker-compose.yml --env-file backend/docker/$(ENV_FILE) up -d
