up:
	docker-compose up --build
down:
	docker-compose down
restart:
	docker-compose restart
runserver: up
	docker-compose run django python3 manage.py runserver 0.0.0.0:8000
migrate: up
	docker-compose run django python3 manage.py migrate
run_and_migrate: migrate
	docker-compose run django python3 manage.py runserver 0.0.0.0:8000
