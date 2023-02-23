package-install:
	python3 -m pip install --user dist/*.whl

check: selfcheck test lint

build: check
	poetry build

install:
	poetry install

gendiff:
	poetry run python gendiff.scripts.gendiff.py

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: install test lint selfcheck check build
