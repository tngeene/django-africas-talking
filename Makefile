.PHONY: runserver, deps, migrate

deps:
	poetry env use 3.9
	poetry install

runserver:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py migrate

superuser:
	poetry run python manage.py createsuperuser


deploy:
	docker-compose build
	docker-compose up -d

down:
	docker-compose down
