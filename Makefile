.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml

test_xunit:
	PYTHONPATH=. py.test -s --cov=. --junit-xml=test_results.xml

lint:
	flake8 hello_world test

run:
	PYTHONPATH=. FLASK_APP=hello_world flask run

docker_build:
	docker build -t hello-world-printer .

USERNAME=kbalko
TAG=$(USERNAME)/hello-world-printer

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;
