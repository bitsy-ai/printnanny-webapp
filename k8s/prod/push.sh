#!/bin/bash

set -euo pipefail
##
# app base image
#
docker tag "print_nanny_webapp:${GIT_SHA}" \
    us.gcr.io/print-nanny/print_nanny_webapp:latest

docker tag "print_nanny_webapp:${GIT_SHA}" \
    "us.gcr.io/print-nanny/print_nanny_webapp:${GIT_SHA}"

docker push us.gcr.io/print-nanny/print_nanny_webapp:latest
docker push "us.gcr.io/print-nanny/print_nanny_webapp:${GIT_SHA}"


kubectl apply -f k8s/stable/configmap.yml
kubectl apply -f k8s/stable/ara-config.yml
kubectl apply -f k8s/prod/ara.yml
# TODO re-enable after event version cutover
# kubectl apply -f k8s/prod/octoprint-events.yml
kubectl apply -f k8s/prod/celery-worker.yml
kubectl apply -f k8s/prod/django.yml

kubectl set image deployment/ara "ara=us.gcr.io/print-nanny/ara:${GIT_SHA}" --record
kubectl set image deployment/django "django=us.gcr.io/print-nanny/print_nanny_webapp:${GIT_SHA}" --record
ATTEMPTS=0
MAX_ATTEMPTS=30
SLEEP=10
DEPLOYMENT="deployment/django"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((ATTEMPTS + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done

kubectl set image deployment/celery-worker "celery-worker=us.gcr.io/print-nanny/print_nanny_webapp:06b6fe3f7f13839b430d6b820004805c07078a4b" --record
kubectl set image deployment/octoprint-events "octoprint-events=us.gcr.io/print-nanny/print_nanny_webapp:${GIT_SHA}" --record
# kubectl set image deployment/octoprint-events "alerts=us.gcr.io/print-nanny/print_nanny_webapp:${GIT_SHA}" --record
