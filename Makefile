install:
	python3 -m venv venv
	venv/bin/pip install -U pip setuptools wheel
	venv/bin/pip install -r requirements.txt

start:
	venv/bin/python -m datavizta.web.main

format:
	venv/bin/black datavizta
	venv/bin/ruff check --fix datavizta

check:
	venv/bin/black --check --diff datavizta
	venv/bin/ruff check datavizta
