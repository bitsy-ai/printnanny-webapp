

.PHONY: build prod-up dev-up client clean-client-build

build:
	npm run build
	docker-compose -f production.yml build

prod-up: build
	docker-compose -f production.yml up

dev-up:
	docker-compose -f local.yml up

deploy: build
	k8s/push.sh


clean-client: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	sudo rm -fr clients/python
	rm -fr .eggs/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

client: clean-client
	docker run --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
		-i http://localhost:8000/api/schema --recommend

	docker run --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i http://localhost:8000/api/schema \
		-g python-legacy \
		-o /local/clients/python \
		-c /local/clients/python.yaml \
	

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


sdist: client ## builds source package
	python3 clients/python/setup.py sdist
	ls -l dist

bdist_wheel: client ## builds wheel package
	python3 clients/python/setup.py bdist_wheel
	ls -l dist
dist: sdist bdist_wheel

client-release: dist ## package and upload a release
	twine upload dist/*