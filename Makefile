

.PHONY: mypy build prod-up dev-up python-client clean-python-client-build ui vue prod-up deploy cypress-open cypress-run local-creds janus-image

# silence targets where credentials are passed
.SILENT: cypress-open cypress-run cypress-ci local-up local-creds

GCP_PROJECT ?= print-nanny-sandbox
CLUSTER ?= www-sandbox
ZONE ?= us-central1-c

PRINT_NANNY_URL ?= http://localhost:8000/
PRINT_NANNY_API_URL ?= ${PRINT_NANNY_URL}api/
OCTOPRINT_URL ?= http://localhost:5005/
PRINT_NANNY_USER ?= ${USER}
DJANGO_SUPERUSER_EMAIL ?= ${USER}@print-nanny.com
DJANGO_SUPERUSER_PASSWORD ?= $(shell test -f .password && cat .password || (makepasswd --chars=42 > .password && cat .password) )
DJANGO_ADMIN_CMD ?= docker-compose -f local.yml run --rm django python manage.py
NEBULA_VERSION ?= v1.4.0
PRINT_NANNY_TOKEN ?= $(shell test -f .token && cat .token || (${DJANGO_ADMIN_CMD} drf_create_token $(DJANGO_SUPERUSER_EMAIL) | tail -n 1 | awk '{print $$3}'> .token && cat .token))
PRINT_NANNY_RELEASE_CHANNEL ?= devel
PRINT_NANNY_PLUGIN_ARCHIVE ?= "https://github.com/bitsy-ai/octoprint-nanny-plugin/archive/$(PRINT_NANNY_RELEASE_CHANNEL).zip"
PRINT_NANNY_PLUGIN_SHA ?= $(shell curl https://api.github.com/repos/bitsy-ai/octoprint-nanny-plugin/branches/$(PRINT_NANNY_RELEASE_CHANNEL) | jq .commit.sha)
PRINT_NANNY_DATAFLOW_SHA ?= $(shell curl https://api.github.com/repos/bitsy-ai/octoprint-nanny-dataflow/branches/$(PRINT_NANNY_RELEASE_CHANNEL) | jq .commit.sha)

JANUS_VERSION ?= 0.11.8

GIT_SHA ?= $(shell git rev-parse HEAD)
GIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)
GHA_ENVIRONMENT ?= sandbox

DOCKER_COMPOSE_PROJECT_NAME="print_nanny_webapp"
GHOST_VERSION ?=4.32-alpine

clean-local-requirements:
	rm -f requirements/local.txt

clean-test-requirements:
	rm -rf requirements/test.txt

clean-prod-requirements:
	rm -rf requirements/production.txt

clean-requirements: clean-local-requirements clean-test-requirements clean-prod-requirements
	rm -f requirements/local.txt

requirements/production.txt:
	pip-compile requirements/production.in --output-file requirements/production.txt

requirements/local.txt:
	pip-compile requirements/local.in --output-file requirements/local.txt

requirements/test-local.txt:
	pip-compile requirements/test-local.in --output-file requirements/test-local.txt

requirements/test-production.txt:
	pip-compile requirements/test-production.in --output-file requirements/test-production.txt

install-git-hooks:
	cp -a hooks/. .git/hooks/
# TODO:
# https://django-environ.readthedocs.io/en/latest/
# base.py requires certain env vars to be present ; move these or create an env harness for CI tests
docker-mypy:
	docker-compose -f local.yml run --rm django mypy -m print_nanny_webapp.telemetry

mypy: clean-pyc
	. .envs/.local/.tests.sh && \
	mypy print_nanny_webapp/telemetry/**/*

token:
	@echo $(PRINT_NANNY_TOKEN)

nebula-image:
	docker build -f compose/production/nebula/nebula.Dockerfile \
		-t nebula:$(NEBULA_VERSION) \
		--build-arg NEBULA_VERSION=$(NEBULA_VERSION) \
		compose/production/nebula/

push-nebula-image: nebula-image
	docker tag nebula:$(NEBULA_VERSION) \
		us.gcr.io/$(GCP_PROJECT)/nebula:$(NEBULA_VERSION)
	docker push us.gcr.io/$(GCP_PROJECT)/nebula:$(NEBULA_VERSION)

octoprint-wait:
	OCTOPRINT_URL=$(OCTOPRINT_URL) \
		k8s/sandbox/octoprint-wait.sh

cypress-open: octoprint-wait
	CYPRESS_PRINT_NANNY_PLUGIN_ARCHIVE=$(PRINT_NANNY_PLUGIN_ARCHIVE) \
	CYPRESS_PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	CYPRESS_OCTOPRINT_USERPASS=$(OCTOPRINT_USERPASS) \
	CYPRESS_PRINT_NANNY_URL=$(PRINT_NANNY_URL) \
	CYPRESS_OCTOPRINT_URL=$(OCTOPRINT_URL) \
	CYPRESS_DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
	CYPRESS_DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	CYPRESS_PRINT_NANNY_TOKEN=$(PRINT_NANNY_TOKEN) \
	node_modules/.bin/cypress open

cypress-run: octoprint-wait
	CYPRESS_PRINT_NANNY_PLUGIN_ARCHIVE=$(PRINT_NANNY_PLUGIN_ARCHIVE) \
	CYPRESS_PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	CYPRESS_OCTOPRINT_USERPASS=$(OCTOPRINT_USERPASS) \
	CYPRESS_PRINT_NANNY_URL=$(PRINT_NANNY_URL) \
	CYPRESS_OCTOPRINT_URL=$(OCTOPRINT_URL) \
	CYPRESS_DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
	CYPRESS_DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	CYPRESS_PRINT_NANNY_TOKEN=$(PRINT_NANNY_TOKEN) \
	node_modules/.bin/cypress run

cypress-ci: octoprint-wait
	CYPRESS_PRINT_NANNY_PLUGIN_ARCHIVE=$(PRINT_NANNY_PLUGIN_ARCHIVE) \
	CYPRESS_PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	CYPRESS_OCTOPRINT_USERPASS=$(OCTOPRINT_USERPASS) \
	CYPRESS_PRINT_NANNY_URL=$(PRINT_NANNY_URL) \
	CYPRESS_OCTOPRINT_URL=$(OCTOPRINT_URL) \
	CYPRESS_DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
	CYPRESS_DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	CYPRESS_PRINT_NANNY_TOKEN=$(PRINT_NANNY_TOKEN) \
	node_modules/.bin/cypress run --record

sandbox-logs:
	kubectl logs --all-containers -l branch=$(GIT_BRANCH)
ui:
	npm install && npm run build

vue:
	cd print_nanny_vue && yarn install && yarn run build

docker-image:
	DOCKER_BUILDKIT=1 docker build \
	-f compose/production/django/Dockerfile \
	-t print_nanny_webapp:$(GIT_SHA) \
	.
build: vue docker-image

local-clean: 
	rm .token || echo "Skipping .token cleanup"
	rm .password || echo "Skipping .password cleanup"
	docker-compose -f local.yml stop
	yes | docker-compose -f local.yml rm
	yes | docker volume rm \
		octoprint-nanny-webapp_local_file_data \
		octoprint-nanny-webapp_local_octoprint_data \
		octoprint-nanny-webapp_local_postgres_data \
		octoprint-nanny-webapp_local_postgres_data_backups \
		octoprint-nanny-webapp_local_prometheus_data || echo "No volumes found"

.envs/.local/key.json:
	gcloud iam service-accounts keys create .envs/.local/key.json --iam-account=owner-service-account@print-nanny-sandbox.iam.gserviceaccount.com

local-creds: .envs/.local/key.json
	echo "Mounted Google Cloud Platform service account key from .envs/.local/key.json with id $(shell cat .envs/.local/key.json | jq .private_key_id)"

local-vue-build:
	cd print_nanny_vue && yarn install && yarn run dev

local-image-build:
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f local.yml build

local-build: local-image-build local-vue-build

local-up: local-image-build local-creds
	. .envs/.sandbox/.env && PROJECT=$(GCP_PROJECT) \
	PRINT_NANNY_IOT_DEVICE_REGISTRY=$(PRINT_NANNY_IOT_DEVICE_REGISTRY) \
	PRINT_NANNY_HONEYCOMB_DATASET=$(PRINT_NANNY_HONEYCOMB_DATASET) \
	PRINT_NANNY_HONEYCOMB_API_KEY=$(PRINT_NANNY_HONEYCOMB_API_KEY) \
	PRINT_NANNY_HONEYCOMB_DEBUG=$(PRINT_NANNY_HONEYCOMB_DEBUG) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
		docker-compose -f local.yml up

local-up-d: local-image-build local-creds
	. .envs/.sandbox/.env && PROJECT=$(GCP_PROJECT) \
	PRINT_NANNY_IOT_DEVICE_REGISTRY=$(PRINT_NANNY_IOT_DEVICE_REGISTRY) \
	PRINT_NANNY_HONEYCOMB_DATASET=$(PRINT_NANNY_HONEYCOMB_DATASET) \
	PRINT_NANNY_HONEYCOMB_API_KEY=$(PRINT_NANNY_HONEYCOMB_API_KEY) \
	PRINT_NANNY_HONEYCOMB_DEBUG=$(PRINT_NANNY_HONEYCOMB_DEBUG) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
		docker-compose -f -d local.yml up

local-up-clean: local-clean local-image-build local-up

cluster-config:
	gcloud container clusters get-credentials $(CLUSTER) --zone $(ZONE) --project $(GCP_PROJECT)

sandbox-config:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PRINT_NANNY_USER=$(PRINT_NANNY_USER) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	PRINT_NANNY_API_URL=$(PRINT_NANNY_API_URL) \
	PRINT_NANNY_WS_URL=$(PRINT_NANNY_WS_URL) \
	PRINT_NANNY_BASE_URL=$(PRINT_NANNY_BASE_URL) \
	PRINT_NANNY_IOT_DEVICE_REGISTRY=$(PRINT_NANNY_IOT_DEVICE_REGISTRY) \
	PRINT_NANNY_HONEYCOMB_DATASET=$(PRINT_NANNY_HONEYCOMB_DATASET) \
	PRINT_NANNY_HONEYCOMB_API_KEY=$(PRINT_NANNY_HONEYCOMB_API_KEY) \
	PRINT_NANNY_HONEYCOMB_DEBUG=$(PRINT_NANNY_HONEYCOMB_DEBUG) \
		k8s/sandbox/render.sh

prod-config:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PRINT_NANNY_USER=$(PRINT_NANNY_USER) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	PRINT_NANNY_API_URL=$(PRINT_NANNY_API_URL) \
	PRINT_NANNY_WS_URL=$(PRINT_NANNY_WS_URL) \
	PRINT_NANNY_BASE_URL=$(PRINT_NANNY_BASE_URL) \
	PRINT_NANNY_IOT_DEVICE_REGISTRY=$(PRINT_NANNY_IOT_DEVICE_REGISTRY) \
	PRINT_NANNY_HONEYCOMB_DATASET=$(PRINT_NANNY_HONEYCOMB_DATASET) \
	PRINT_NANNY_HONEYCOMB_API_KEY=$(PRINT_NANNY_HONEYCOMB_API_KEY) \
	PRINT_NANNY_HONEYCOMB_DEBUG=$(PRINT_NANNY_HONEYCOMB_DEBUG) \
		k8s/stable/render.sh

sandbox-pv-clean: sandbox-config
	k8s/sandbox/delete-resource.sh k8s/sandbox/pv.yml

sandbox-deploy: cluster-config sandbox-config build
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		k8s/sandbox/push.sh && \
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		k8s/sandbox/apply.sh && \
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		k8s/sandbox/rollout-wait.sh

sandbox-email:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PLUGIN_SHA=$(PRINT_NANNY_PLUGIN_SHA) \
	DATAFLOW_SHA=$(PRINT_NANNY_DATAFLOW_SHA) \
	PRINT_NANNY_RELEASE_CHANNEL=$(PRINT_NANNY_RELEASE_CHANNEL) \
	PROJECT=$(GCP_PROJECT) \
	CLUSTER=$(CLUSTER) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	ZONE=$(ZONE) \
		k8s/sandbox/email.sh

sandbox-ci: sandbox-deploy sandbox-email cypress-ci

prod-apply: cluster-config
	GIT_SHA=$(GIT_SHA) k8s/prod/push.sh

prod-deploy: build cluster-config prod-config prod-apply

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

# clean-kotlin-client:
# 	sudo rm -rf clients/kotlin

clean-rust-client:
	sudo rm -rf clients/rust

# kotlin-client: clean-kotlin-client
# 	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
# 		-i http://localhost:8000/api/schema --recommend

# 	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
# 		-i http://localhost:8000/api/schema \
# 		-g kotlin \
# 		-o /local/clients/kotlin \
# 		-c /local/clients/kotlin.yaml

ts-client: clean-ts-client
	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
		-i http://localhost:8000/api/schema --recommend

	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i http://localhost:8000/api/schema \
		-g typescript-axios \
		-o /local/clients/typescript \
		-c /local/clients/typescript.yaml

	cd clients/typescript && npm install && npm build

# debugging info: https://openapi-generator.tech/docs/debugging#templates
rust-client: clean-rust-client
	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli validate \
		-i http://localhost:8000/api/schema --recommend 

	docker run -u `id -u` --net=host --rm -v "$${PWD}:/local" openapitools/openapi-generator-cli generate \
		-i http://localhost:8000/api/schema \
		-g rust \
		-o /local/clients/rust \
		-c /local/clients/rust.yaml \
		-t /local/client-templates/rust

rust-build: rust-client
	cd clients/rust && cargo build

clean-python-client: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	sudo rm -fr clients/python
	rm -fr .eggs/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -rf {} +


# python-flatbuffer:
# 	~/projects/flatbuffers/flatc -b -t --python --gen-object-api -o clients/python/ clients/flatbuffers/*.fbs

python-protobuf:
	mkdir -p clients/python/print_nanny_client/protobuf && touch clients/python/print_nanny_client/protobuf/modinit__.py
	protoc --python_out=clients/python/print_nanny_client/protobuf --mypy_out=clients/python/print_nanny_client/protobuf --proto_path=clients/protobuf clients/protobuf/*.proto
	find clients/python/print_nanny_client/protobuf -name '*.py*' | xargs sed -i 's/import common_pb2/from . import common_pb2/'
	find clients/python/print_nanny_client/protobuf -name '*.py*' | xargs sed -i 's/from common_pb2/from .common_pb2/'
	sed -i 's/alert_pb2/print_nanny_client.protobuf.alert_pb2/' clients/python/print_nanny_client/protobuf/alert_pb2.py
	sed -i 's/common_pb2/print_nanny_client.protobuf.common_pb2/' clients/python/print_nanny_client/protobuf/common_pb2.py
	sed -i 's/monitoring_pb2/print_nanny_client.protobuf.monitoring_pb2/' clients/python/print_nanny_client/protobuf/monitoring_pb2.py


python-client: clean-python-client # python-flatbuffer python-protobuf
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

python-client-release: dist
	cd clients/python && twine upload dist/* && cd -

rust-client-release: rust-client
	cd clients/rust && cargo publish

js-client-release: ts-client
	cd clients/typescript && npm publish

clients-release: js-client-release python-client-release rust-client-release 

cloudsql:
	cloud_sql_proxy -dir=$(HOME)/cloudsql -instances=print-nanny:us-central1:print-nanny=tcp:5433

test:
	docker-compose -f local.yml run --rm django pytest

stripe-local-webhooks:
	stripe listen --forward-to localhost:8000/stripe/webhook/

ara-image:
	docker build \
		--tag us.gcr.io/print-nanny/ara:${GIT_SHA} \
		-f compose/production/ara/Dockerfile compose/production/ara
	docker tag us.gcr.io/print-nanny/ara:${GIT_SHA} us.gcr.io/print-nanny/ara:fedora33-source-latest
	docker push us.gcr.io/print-nanny/ara:fedora33-source-latest
	docker push us.gcr.io/print-nanny/ara:${GIT_SHA}

ara-rollout: ara-image
	kubectl set image deployment/ara ara=us.gcr.io/print-nanny/ara:${GIT_SHA} --record

gcs-fuse-image:
	docker build \
		--tag bitsyai/nginx-gcsfuse \
		-f compose/production/gcsfuse/Dockerfile compose/production/gcsfuse
	docker push bitsyai/nginx-gcsfuse


upgrade-ghost:
	docker pull ghost:$(GHOST_VERSION)
	docker tag ghost:$(GHOST_VERSION) us.gcr.io/print-nanny/ghost:$(GHOST_VERSION)
	docker tag ghost:$(GHOST_VERSION) us.gcr.io/print-nanny/ghost:latest
	docker push us.gcr.io/print-nanny/ghost:$(GHOST_VERSION)
	docker push us.gcr.io/print-nanny/ghost:latest

	kubectl set image statefulset/bitsy-ai-blog ghost=us.gcr.io/print-nanny/ghost:$(GHOST_VERSION) --record
	kubectl set image statefulset/print-nanny-blog ghost=us.gcr.io/print-nanny/ghost:$(GHOST_VERSION) --record
	kubectl set image statefulset/print-nanny-help ghost=us.gcr.io/print-nanny/ghost:$(GHOST_VERSION) --record

##
# Janus
##
JANUS_NAMESPACE ?= default
dist/k8s:
	mkdir -p dist/k8s

dist/k8s/janus.yml: dist/k8s
	j2 k8s/templates/janus.j2 -o dist/k8s/janus.yml

janus-deploy: dist/k8s/janus.yml cluster-config
	kubectl -n $(JANUS_NAMESPACE) apply -f dist/k8s/janus.yml

janus-image:
	docker build --tag us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION) \
		-f compose/production/janus/Dockerfile compose/production/janus
	docker tag us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION) bitsyai/janus:$(JANUS_VERSION)
	docker push us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION)
	docker push bitsyai/janus:$(JANUS_VERSION)