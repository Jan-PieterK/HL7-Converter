format:
	isort --profile black . && black --line-length=79 . && flake8 .

test:
	pytest .

build:
	poetry build
