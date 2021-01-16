

.PHONY: build prod-up dev-up python-client clean-python-client-build

ui:
	npm run build
build: ui
	docker-compose -f production.yml build

prod-up: build
	docker-compose -f production.yml up

dev-up:
	docker-compose -f local.yml up

deploy: build
	k8s/push.sh

blog-deploy:
	k8s/push-blog.sh

lint:
	black print_nanny_webapp

helm-install:
	helm install -f k8s/ghost-values.yml print-nanny-blog ./k8s/bitnami/ghost/ghost

helm-delete:
	helm delete print-nanny-blog

vue-dev:
	cd print_nanny_vue && npm run dev

clean-ts-client:
	find . -name '*.hot-update.js' -exec rm -fr {} +
	find . -name '*.hot-update.json' -exec rm -fr {} +
	sudo rm -rf clients/typescript

ts-client: clean-ts-client
	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
		-i http://localhost:8000/api/schema --recommend

	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i http://localhost:8000/api/schema \
		-g typescript-axios \
		-o /local/clients/typescript \
		-c /local/clients/typescript.yaml \

clean-python-client: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	sudo rm -fr clients/python
	rm -fr .eggs/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +

python-client: clean-python-client
	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
		-i http://localhost:8000/api/schema --recommend

	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i http://localhost:8000/api/schema \
		-g python-legacy \
		-o /local/clients/python \
		-c /local/clients/python.yaml \
	

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +


sdist: python-client ## builds source package
	cd clients/python && python3 setup.py sdist && ls -l dist

bdist_wheel: python-client ## builds wheel package
	cd clients/python && python3 setup.py bdist_wheel && ls -l dist
dist: sdist bdist_wheel

python-client-release: dist ## package and upload a release
	cd clients/python && twine upload dist/* && cd -

cloudsql:
	cloud_sql_proxy -dir=$(HOME)/cloudsql -instances=print-nanny:us-central1:print-nanny=tcp:5433

test:
	docker-compose -f local.yml run --rm django pytest

ghost-push:
