run :
	@docker-compose up

underground:
	@docker-compose up -d

down:
	@docker-compose down

test:
	@docker-compose up -d
	@docker-compose exec data-provider poetry run pytest
	@docker-compose exec app           poetry run pytest
	@docker-compose down

clear:
	@docker-compose down -v --rmi all --remove-orphans

clean: clear

build:
	@docker-compose build
