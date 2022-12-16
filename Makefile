install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:	
	black *.py **/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py **/*.py

test: 
	python -m pytest -vv test_*.py

refactor: format lint

build: 
	docker build -t fastapi .

deploy:
	pip install awscli --upgrade --user
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 295479202713.dkr.ecr.us-east-1.amazonaws.com/proj4
	docker build -t proj4 .
	docker tag fastapi:latest 295479202713.dkr.ecr.us-east-1.amazonaws.com/proj4:latest
	docker push 295479202713.dkr.ecr.us-east-1.amazonaws.com/proj4:latest

run:
	python3 db_set_up.py
	uvicorn main:app --host 0.0.0.0 --port 8080
