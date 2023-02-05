package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

install:
	poetry install

gendiff:
	poetry run python gendiff.scripts.gendiff.py

lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest
