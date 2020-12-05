

.PHONY: build prod-up dev-up

build:
	npm run build
	docker-compose -f production.yml build

prod-up: build
	docker-compose -f production.yml up

dev-up:
	docker-compose -f local.yml up

deploy: build
	k8s/push.sh