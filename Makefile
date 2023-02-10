

.PHONY: mypy build prod-up dev-up python-client clean-python-client-build ui vue prod-up deploy cypress-open cypress-run local-creds janus-image djstripe-sync-local

# silence targets where credentials are passed
.SILENT: cypress-open cypress-run cypress-ci local-up local-creds

GCP_PROJECT ?= printnanny-sandbox
CLUSTER ?= www-sandbox
ZONE ?= us-central1-c

PRINTNANNY_NAMESPACE ?= beta
PRINT_NANNY_URL ?= http://localhost:8080/
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

JANUS_VERSION ?= 1.0.4

GIT_SHA ?= $(shell git rev-parse HEAD)
GIT_BRANCH ?= $(shell git rev-parse --abbrev-ref HEAD)
GHA_ENVIRONMENT ?= sandbox

DOCKER_COMPOSE_PROJECT_NAME="print_nanny_webapp"
GHOST_VERSION ?=4.32-alpine

TMPDIR ?= .tmp
WORKDIR ?=$(PWD)
OPENAPI_GENERATOR_WORKDIR ?= $(HOME)/projects/openapi-generator
OPENAPI_GENERATOR_CLI_JAR ?= $(OPENAPI_GENERATOR_WORKDIR)/modules/openapi-generator-cli/target/openapi-generator-cli.jar
OPENAPI_CUSTOM_RUST_GENERATOR_JAR ?= $(HOME)/.m2/repository/org/openapitools/rust-client-openapi-generator/1.0.0/rust-client-openapi-generator-1.0.0.jar

PRINTNANNY_CONFIG_DEV ?= $(TMPDIR)/printnanny.toml

CDN_BUCKET ?= print-nanny-cdn
CDN_DEPLOY_PATH ?= $(CDN_BUCKET)/ui/
CDN_CACHE_INVALIDATE_PATH ?= /ui/index.html

DEV_MACHINE ?= pn-debug
DEV_CONFIG ?= $(TMPDIR)/printnanny-$(DEV_MACHINE).zip
HOSTNAME ?= $(shell cat /etc/hostname)


$(TMPDIR):
	mkdir $(TMPDIR)

$(DEV_CONFIG): $(TMPDIR)
	docker-compose -f local.yml run --rm django python manage.py devconfig --out $(DEV_CONFIG) --email $(DJANGO_SUPERUSER_EMAIL) --hostname $(HOSTNAME)

openapi-custom-rust-codegen:
	cd $(OPENAPI_GENERATOR_WORKDIR) && ./mvnw clean install -f ~/projects/octoprint-nanny-webapp/client-templates/rust-client-codegen
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

requirements/test.txt:
	pip-compile requirements/test.in --output-file requirements/test.txt

requirements-image:
	docker build -t bitsyai/python:3.9 -f requirements/requirements.Dockerfile requirements/

requirements-prod:
	pip-compile requirements/production.in --output-file requirements/production.txt

requirements-local:
	pip-compile --verbose requirements/local.in --output-file requirements/local.txt

requirements-test:
	pip-compile --verbose requirements/test.in --output-file requirements/test.txt


install-git-hooks:
	cp -a hooks/. .git/hooks/
# TODO:
# https://django-environ.readthedocs.io/en/latest/
# base.py requires certain env vars to be present ; move these or create an env harness for CI tests
mypy:
	docker-compose -f local.yml run -e DJANGO_SETTINGS_MODULE=config.settings.test --rm django mypy

token:
	${DJANGO_ADMIN_CMD} drf_create_token $(DJANGO_SUPERUSER_EMAIL)

octoprint-wait:
	OCTOPRINT_URL=$(OCTOPRINT_URL) \
		k8s/sandbox/octoprint-wait.sh

cypress-ci-run: 
	cd ui && npm run cypress:run

cypress-ci-open: 
	cd ui && npm run cypress:open

sandbox-logs:
	kubectl logs --all-containers -l branch=$(GIT_BRANCH)

ui-invalidate-cache:
	gcloud compute url-maps invalidate-cdn-cache $(CDN_BUCKET) --path $(CDN_CACHE_INVALIDATE_PATH)

ui: ts-build
	cd ui && npm install && npm run build

ui-deploy:
	cd ui/dist && gsutil rsync -R . gs://$(CDN_DEPLOY_PATH)

ui-install:
	cd ui/dist && npm run install

ui-lint:
	cd ui/dist && npm run lint

docker-image:
	DOCKER_BUILDKIT=1 docker build \
	-f compose/production/django/Dockerfile \
	-t print_nanny_webapp:$(GIT_SHA) \
	.
build: vue docker-image

local-clean:
	rm -rf $(TMPDIR)
	rm .token || echo "Skipping .token cleanup"
	rm .password || echo "Skipping .password cleanup"
	docker-compose -f local.yml stop
	yes | docker-compose -f local.yml rm
	yes | docker volume rm \
		octoprint-nanny-webapp_local_nsc_data \
		octoprint-nanny-webapp_local_file_data \
		octoprint-nanny-webapp_local_octoprint_data \
		octoprint-nanny-webapp_local_postgres_data \
		octoprint-nanny-webapp_local_postgres_data_backups \
		octoprint-nanny-webapp_local_prometheus_data || echo "No volumes found"

.envs/.local/key.json:
	gcloud iam service-accounts keys create .envs/.local/key.json --iam-account=owner-service-account@printnanny-sandbox.iam.gserviceaccount.com

.envs/.local/oidc.key:
	openssl genrsa -out oidc.key 4096


local-creds: .envs/.local/key.json
	echo "Mounted Google Cloud Platform service account key from .envs/.local/key.json with id $(shell cat .envs/.local/key.json | jq .private_key_id)"

local-image-build:
	DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose -f local.yml build

local-build: local-image-build local-vue-build

down:
	docker-compose -f local.yml down


robots-init:
	docker-compose -f local.yml exec django python manage.py init_natsrobots

nsc-init:
	docker-compose -f local.yml exec django python manage.py nsc_init || echo "DjangoOperator already created" && docker-compose -f local.yml restart nats
	docker-compose -f local.yml exec django python manage.py initrobots --name=firehose

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

ci-callback-token:
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
	docker-compose -f test.yml run --rm django python manage.py drfpasswordless_callback_token $(ARGS)

ci-clean:
	rm -rf ui/dist
	docker-compose -f test.yml stop
	docker-compose -f test.yml rm

ci-ui-test:
	mkdir -p ui/dist
	cd clients/typescript && npm install && npm run build
	cd ui && npm install && npm run dev-build
	cd ui && npm run dev &

ci-webapp: ci-clean
	mkdir -p ui/dist
	make ci-up &
	cd ui && npm install && npm run ci-webapp-wait
	docker-compose -f test.yml restart nats
	docker-compose -f test.yml run --rm django python manage.py initrobots --name=firehose
	docker-compose -f test.yml restart firehose


ci-up:
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	DJANGO_SUPERUSER_EMAIL=$(DJANGO_SUPERUSER_EMAIL) \
	docker-compose -f test.yml up

ci-pytest:
	docker-compose -f test.yml run --rm django pytest

sandbox-config:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PRINT_NANNY_USER=$(PRINT_NANNY_USER) \
	DJANGO_SUPERUSER_PASSWORD=$(DJANGO_SUPERUSER_PASSWORD) \
	PRINT_NANNY_API_URL=$(PRINT_NANNY_API_URL) \
	DJANGO_WS_URL=$(DJANGO_WS_URL) \
	DJANGO_BASE_URL=$(DJANGO_BASE_URL) \
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
	DJANGO_WS_URL=$(DJANGO_WS_URL) \
	DJANGO_BASE_URL=$(DJANGO_BASE_URL) \
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

ns-k8s: clean-dist dist/k8s
	echo "Using namespace environment .envs/.$(PRINTNANNY_NAMESPACE)/.env"
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	dotenv -f .envs/.$(PRINTNANNY_NAMESPACE)/.env run k8s/templates/render.sh

ns-apply: ns-k8s
	echo "Using namespace environment .envs/.$(PRINTNANNY_NAMESPACE)/.env"
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		dotenv -f .envs/.$(PRINTNANNY_NAMESPACE)/.env run k8s/templates/apply.sh
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PROJECT=$(GCP_PROJECT) \
	CLUSTER=$(CLUSTER) \
	PRINTNANNY_NAMESPACE=$(PRINTNANNY_NAMESPACE) \
		dotenv -f .envs/.$(PRINTNANNY_NAMESPACE)/.env run k8s/templates/apply.sh

ns-rollout:
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PROJECT=$(GCP_PROJECT) \
	CLUSTER=$(CLUSTER) \
	PRINTNANNY_NAMESPACE=$(PRINTNANNY_NAMESPACE) \
		./tools/rollout.sh

namespace-deploy: clean-dist dist/k8s cluster-config build ns-apply ns-rollout

namespace-apply: clean-dist dist/k8s cluster-config ns-apply

live-apply: PRINTNANNY_NAMESPACE:=live
live-apply: namespace-apply

live-janus-apply: PRINTNANNY_NAMESPACE:=live
live-janus-apply: clean-dist dist/k8s cluster-config ns-apply


live-deploy: PRINTNANNY_NAMESPACE:=live
live-deploy: namespace-deploy

beta-deploy: PRINTNANNY_NAMESPACE:=beta
beta-deploy: namespace-deploy

gh-namespace-deploy: clean-dist dist/k8s build cluster-config
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		./k8s/templates/render.sh
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
		./k8s/templates/apply.sh
	GIT_SHA=$(GIT_SHA) \
	GIT_BRANCH=$(GIT_BRANCH) \
	PROJECT=$(GCP_PROJECT) \
	CLUSTER=$(CLUSTER) \
	PRINTNANNY_NAMESPACE=$(PRINTNANNY_NAMESPACE) \
		./tools/rollout.sh

prod-apply: cluster-config
	GIT_SHA=$(GIT_SHA) k8s/prod/push.sh

prod-deploy: build cluster-config prod-config prod-apply

blog-deploy:
	k8s/push-blog.sh

lint:
	black print_nanny_webapp
	black config

clean-ts-client:
	find . -name '*.hot-update.js' -exec rm -fr {} +
	find . -name '*.hot-update.json' -exec rm -fr {} +
	sudo rm -rf clients/typescript

# clean-kotlin-client:
# 	sudo rm -rf clients/kotlin

clean-rust-client:
	sudo rm -rf clients/rust

ts-client: clean-ts-client
	java -jar $(OPENAPI_GENERATOR_CLI_JAR) validate \
		-i http://localhost:8080/api/schema/ --recommend

	java -jar $(HOME)/projects/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar  generate \
		-i http://localhost:8080/api/schema/ \
		-g typescript-axios \
		-o $(PWD)/clients/typescript \
		-c $(PWD)/clients/typescript.yaml

	cd clients/typescript && npm install && npm run build

ts-build: 
	cd clients/typescript && npm install && npm run build

# debugging info: https://openapi-generator.tech/docs/debugging#templates
rust-client: clean-rust-client openapi-custom-rust-codegen
	java -cp "$(OPENAPI_CUSTOM_RUST_GENERATOR_JAR):$(OPENAPI_GENERATOR_CLI_JAR)" \
		org.openapitools.codegen.OpenAPIGenerator validate \
		-i http://localhost:8080/api/schema/ --recommend 

	java -cp "$(OPENAPI_CUSTOM_RUST_GENERATOR_JAR):$(OPENAPI_GENERATOR_CLI_JAR)" \
		org.openapitools.codegen.OpenAPIGenerator generate \
		-i http://localhost:8080/api/schema/ \
		-g custom-rust-client \
		-o $(PWD)/clients/rust \
		-c $(PWD)/clients/rust.yaml


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
	java -jar $(HOME)/projects/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar  validate \
		-i http://localhost:8080/api/schema/ --recommend

	java -jar $(HOME)/projects/openapi-generator/modules/openapi-generator-cli/target/openapi-generator-cli.jar  generate \
		-i http://localhost:8080/api/schema/ \
		-g python-legacy \
		-o $(PWD)/clients/python \
		-c $(PWD)/clients/python.yaml \

# python-client: clean-python-client
# 	openapi-python-client generate --url http://localhost:8080/api/schema/ --config clients/python.yaml --meta setup
# 	mv printnanny-api-client clients/python

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' -exec rm -f {} \;


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


openapi-schema:
	docker-compose -f local.yml exec django python manage.py spectacular --file asyncapi/openapi.yaml


clients-release: js-client-release python-client-release rust-client-release openapi-schema

cloudsql:
	cloud_sql_proxy -dir=$(HOME)/cloudsql -instances=print-nanny:us-central1:print-nanny=tcp:5433

test:
	docker-compose -f local.yml run --rm django pytest

stripe-local-webhooks:
	stripe listen --forward-to localhost:8080/stripe/webhook/

djstripe-sync-local:
	docker-compose -f local.yml run --rm django python manage.py djstripe_sync_models
	docker-compose -f local.yml run --rm django python manage.py loaddata print_nanny_webapp/shop/fixtures/product.json --app shop.Product

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

clean-dist:
	rm -rf dist
dist/k8s:
	mkdir -p dist/k8s

dist/k8s/janus.yml: dist/k8s
	j2 k8s/templates/janus.j2 -o dist/k8s/janus.yml

janus-deploy: clean-dist dist/k8s/janus.yml cluster-config
	kubectl apply -f dist/k8s/janus.yml

janus-image:
	docker build --tag us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION) \
		-f compose/production/janus/Dockerfile compose/production/janus
	docker tag us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION) bitsyai/janus:$(JANUS_VERSION)
	docker push us.gcr.io/$(GCP_PROJECT)/janus:$(JANUS_VERSION)
	docker push bitsyai/janus:$(JANUS_VERSION)

cert-manager:
	helm upgrade -i \
		cert-manager jetstack/cert-manager \
		--namespace cert-manager \
		--create-namespace \
		--version v1.7.1 \
		--set installCRDs=true \
		--set prometheus.enabled=false \
		--set ingressShim.defaultIssuerName=letsencrypt-dns-issuer \
		--set ingressShim.defaultIssuerKind=ClusterIssuer \
		--set ingressShim.defaultIssuerGroup=cert-manager.io

cert-manager-dns:
	gcloud projects add-iam-policy-binding $(GCP_PROJECT) \
		--member serviceAccount:dns01-solver@$(GCP_PROJECT).iam.gserviceaccount.com \
		--role roles/dns.admin
	gcloud iam service-accounts add-iam-policy-binding \
		--role roles/iam.workloadIdentityUser \
		--member "serviceAccount:$(GCP_PROJECT).svc.id.goog[cert-manager/cert-manager]" \
		dns01-solver@$(GCP_PROJECT).iam.gserviceaccount.com
	kubectl annotate serviceaccount --namespace=cert-manager cert-manager \
    "iam.gke.io/gcp-service-account=dns01-solver@$(GCP_PROJECT).iam.gserviceaccount.com"

migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

ci-collectstatic:
	docker-compose -f test.yml run --rm django python manage.py collectstatic --noinput

collectstatic:
	docker-compose -f local.yml run --rm django python manage.py collectstatic --noinput

dev-config: $(TMPDIR)
	docker-compose -f local.yml exec django python manage.py devconfig \
		--email=$(DJANGO_SUPERUSER_EMAIL) \
		--hostname=$(shell hostname) \
		--out=$(PRINTNANNY_CONFIG_DEV) \
		--port=8000

windmill-install:
	helm install printnanny-windmill k8s/windmill/windmill-helm-charts/charts/windmill \
		-f k8s/windmill/values.yaml \
		--namespace=live \
		--create-namespace \
		--set windmill.databaseUrl=${WINDMILL_DATABASE_URL} \
		--set windmill.oauthConfig=$(shell cat compose/production/windmill/oauth.json)

windmill-upgrade-values:
	helm upgrade printnanny-windmill --debug --install k8s/windmill/windmill-helm-charts/charts/windmill \
		-f k8s/windmill/values.yaml \
		--namespace=live \
		--set windmill.databaseUrl=${WINDMILL_DATABASE_URL}


nats-install:
	helm install --create-namespace --namespace nats -f k8s/nats/values.yaml \
		printnanny-nats nats/nats \
		--set auth.resolver.operator=${NATS_OPERATOR_NKEY} \
		--set auth.resolver.systemAccount=${NATS_SYSTEM_ACCOUNT} \
		--set auth.resolver.resolverPreload.${NATS_SYSTEM_ACCOUNT}=${NATS_RESOLVER_PRELOAD}

nats-upgrade:
	helm upgrade --namespace nats \
		printnanny-nats nats/nats \
		--reuse-values

nats-upgrade-values:
	helm upgrade --namespace nats \
		--debug \
		--install \
		printnanny-nats nats/nats \
		--values k8s/nats/values.yaml \
		--set auth.resolver.operator=${NATS_OPERATOR_NKEY} \
		--set auth.resolver.systemAccount=${NATS_SYSTEM_ACCOUNT} \
		--set auth.resolver.resolverPreload.${NATS_SYSTEM_ACCOUNT}=${NATS_RESOLVER_PRELOAD}


shellcheck:
	find -name '*.sh' -not -path './.venv/*' -not -path './clients/*' | xargs shellcheck

janus_stream_clean:
	docker-compose -f local.yml run --rm django python manage.py janus_stream_clean
