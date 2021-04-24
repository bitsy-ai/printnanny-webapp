

.PHONY: build prod-up dev-up python-client clean-python-client-build ui vue prod-up deploy sandbox-credentials cypress-local-dev cypress-local-run

PROJECT ?= "print-nanny-sandbox"
CLUSTER ?= "www-sandbox"
ZONE ?= "us-central1-c"

PRINT_NANNY_URL ?= "http://localhost:8000/"
OCTOPRINT_URL ?= "http://localhost:5005/"
PRINT_NANNY_RELEASE_CHANNEL ?= "devel"
PRINT_NANNY_PLUGIN_ARCHIVE ?= "https://github.com/bitsy-ai/octoprint-nanny-plugin/archive/devel.zip"
GIT_SHA ?= $(shell git rev-parse HEAD)
GIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)

cypress-local-dev:
	CYPRESS_PRINT_NANNY_PLUGIN_ARCHIVE=$(PRINT_NANNY_PLUGIN_ARCHIVE) \
	CYPRESS_PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	CYPRESS_OCTOPRINT_USERPASS=$(OCTOPRINT_USERPASS) \
	CYPRESS_PRINT_NANNY_URL=$(PRINT_NANNY_URL) \
	CYPRESS_OCTOPRINT_URL=$(OCTOPRINT_URL) \
	CYPRESS_PRINT_NANNY_EMAIL=$(PRINT_NANNY_EMAIL \
	CYPRESS_PRINT_NANNY_PASSWORD=$(PRINT_NANNY_PASSWORD) \
	node_modules/.bin/cypress open
cypress-local-run:
	CYPRESS_PRINT_NANNY_PLUGIN_ARCHIVE=$(PRINT_NANNY_PLUGIN_ARCHIVE) \
	CYPRESS_PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	CYPRESS_OCTOPRINT_USERPASS=$(OCTOPRINT_USERPASS) \
	CYPRESS_PRINT_NANNY_URL=$(PRINT_NANNY_URL) \
	CYPRESS_OCTOPRINT_URL=$(OCTOPRINT_URL) \
	CYPRESS_PRINT_NANNY_EMAIL=$(PRINT_NANNY_EMAIL \
	CYPRESS_PRINT_NANNY_PASSWORD=$(PRINT_NANNY_PASSWORD) \
	node_modules/.bin/cypress run

ui:
	npm install && npm run build

vue:
	cd print_nanny_vue && npm install && npm run build

docker-image:
	DOCKER_BUILDKIT=1 docker build \
	-f compose/production/django/Dockerfile \
	-t print_nanny_webapp:$(GIT_SHA) \
	.
build: vue ui docker-image

prod-up: build
	docker-compose -f production.yml up

dev-up:
	docker-compose -f local.yml up

sandbox-owner-credentials:
	gcloud iam service-accounts keys create .envs/.local/key.json --iam-account=owner-service-account@print-nanny-sandbox.iam.gserviceaccount.com

cluster-config:
	gcloud container clusters get-credentials $(CLUSTER) --zone $(ZONE) --project $(PROJECT)

sandbox-deploy: cluster-config build
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		k8s/sandbox/push.sh && \
		k8s/sandbox/render.sh && \
		k8s/sandbox/apply.sh

sandbox-email:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		k8s/sandbox/email.sh

sandbox: sandbox-deploy 

prod-deploy: build cluster-config
	k8s/prod/push.sh

blog-deploy:
	k8s/push-blog.sh

lint:
	black print_nanny_webapp

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


python-flatbuffer:
	~/projects/flatbuffers/flatc -b -t --python --gen-object-api -o clients/python/ clients/flatbuffers/telemetry_event.fbs


python-client: clean-python-client python-flatbuffer
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

clients-release: python-client-release ts-client

cloudsql:
	cloud_sql_proxy -dir=$(HOME)/cloudsql -instances=print-nanny:us-central1:print-nanny=tcp:5433

test:
	docker-compose -f local.yml run --rm django pytest