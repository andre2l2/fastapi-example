install:
	pip install -r requirements.txt

run:
	fastapi run ./src/main.py

save-deps:
	pip freeze > requirements.txt