run :
	@docker-compose up

underground:
	@docker-compose up -d

down:
	@docker-compose down

test:
	@docker-compose exec data-provider poetry run pytest
	# add app testing when done

clear:
	@docker-compose down -v --rmi all --remove-orphans

clean: clear

build:
	@docker-compose build
