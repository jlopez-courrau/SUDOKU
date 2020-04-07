run : build
	docker-compose up

underground: build
	docker-compose up -d

down:
	@docker-compose down

test:
	@echo
	@echo ======testing not implemented yet======
	@echo ======     but will be        ...======
	@echo

clear:
	@docker-compose down -v --rmi all --remove-orphans

clean: clear

build:
	docker-compose build
