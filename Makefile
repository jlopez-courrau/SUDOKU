run :
	docker-compose up

test:
	echo testing not implemented yet

clear:
	docker-compose down -v --rmi all --remove-orphans

clean: clear

build:
	docker-compose up --build
