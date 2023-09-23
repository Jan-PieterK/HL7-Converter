format:
	isort . && black . && flake8 .

test:
	pytest .

build:
	poetry build
