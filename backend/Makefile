include ../.env

export CONNECTION_STRING=postgres://$(POSTGRES_USER):$(POSTGRES_PASSWORD)@$(POSTGRES_HOST):$(POSTGRES_PORT)/$(POSTGRES_DB)
export DATABASE_NAME=$(POSTGRES_DB)
export DATABASE_TYPE=postgres

# Run api
.PHONY: run-api
run-api:
	@echo "CONNECTION_STRING:" $(CONNECTION_STRING)
	@echo "DATABASE_TYPE:" $(DATABASE_TYPE)
	@echo "DATABASE_NAME" $(DATABASE_NAME)
	@uvicorn src.api.main:app --reload

# Run api
.PHONY: run-api-debug
run-api-debug:
	@echo "CONNECTION_STRING:" $(CONNECTION_STRING)
	@echo "DATABASE_TYPE:" $(DATABASE_TYPE)
	@echo "DATABASE_NAME" $(DATABASE_NAME)
	@uvicorn src.api.main:app --reload --log-level debug

#* Install
.PHONY: install
install:
	@pip install -r requirements.txt

#* Install-dev
.PHONY: install-dev
install-dev:
	@pip install -r requirements-dev.txt

#* Alembic current
.PHONY: alembic-current
alembic-current:
	@alembic current

#* Migration-run
.PHONY: migration-run
migration-run:
	@alembic upgrade head

#* Migration-downgrade
.PHONY: migration-downgrade
migration-downgrade:
	@alembic downgrade -1

#* Migration-create
.PHONY: migration-create
migration-create:
	@if [ -z "$(COMMENT)" ]; then \
		printf "\n\033[31mError: Need to inform migration message example:\033[0m\nmake migration-create COMMENT=\"first migration\"\n"; \
	else \
		alembic revision --autogenerate -m "$(COMMENT)"; \
	fi

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	@find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf