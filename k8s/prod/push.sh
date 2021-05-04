#!/bin/bash

##
# app base image
#
docker tag print_nanny_webapp:$(GIT_SHA) \
    us.gcr.io/print-nanny/print_nanny_webapp:latest

docker tag print_nanny_webapp:$(GIT_SHA) \
    us.gcr.io/print-nanny/print_nanny_webapp:$(git rev-parse HEAD)

docker push us.gcr.io/print-nanny/print_nanny_webapp:latest
docker push us.gcr.io/print-nanny/print_nanny_webapp:$(git rev-parse HEAD)


kubectl apply -f k8s/prod/configmap.yml
kubectl apply -f k8s/prod/octoprint-events.yml
kubectl apply -f k8s/prod/celery-worker.yml
kubectl apply -f k8s/prod/django.yml

kubectl set image deployment/django django=us.gcr.io/print-nanny/print_nanny_webapp:$(git rev-parse HEAD) --record
kubectl set image deployment/celery-worker celery-worker=us.gcr.io/print-nanny/print_nanny_webapp:$(git rev-parse HEAD) --record
kubectl set image deployment/octoprint-events octoprint-events=us.gcr.io/print-nanny/print_nanny_webapp:$(git rev-parse HEAD) --record
