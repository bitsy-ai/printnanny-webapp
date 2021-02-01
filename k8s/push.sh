#!/bin/bash

##
# app base image
#
docker tag print_nanny_webapp_production_django:latest \
    us.gcr.io/print-nanny/print_nanny_webapp_production_django:latest

docker tag print_nanny_webapp_production_django:latest \
    us.gcr.io/print-nanny/print_nanny_webapp_production_django:$(git rev-parse HEAD)

docker push us.gcr.io/print-nanny/print_nanny_webapp_production_django:latest
docker push us.gcr.io/print-nanny/print_nanny_webapp_production_django:$(git rev-parse HEAD)


kubectl apply -f k8s/configmap.yml
kubectl apply -f k8s/production.yml

kubectl set image deployment/django django=us.gcr.io/print-nanny/print_nanny_webapp_production_django:$(git rev-parse HEAD) --record
kubectl set image deployment/celery-worker celery-worker=us.gcr.io/print-nanny/print_nanny_webapp_production_django:$(git rev-parse HEAD) --record
kubectl set image deployment/octoprint-events octoprint-events=us.gcr.io/print-nanny/print_nanny_webapp_production_django:$(git rev-parse HEAD) --record
