#!/bin/bash

set -euo pipefail

docker tag "print_nanny_webapp:${GIT_SHA}" \
    "us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:latest"

docker tag "print_nanny_webapp:${GIT_SHA}" \
    "us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}"

docker push us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:latest
docker push "us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}"

kubectl  -n "$PRINTNANNY_NAMESPACE" set image deployment/django "django=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" --record
ATTEMPTS=0
MAX_ATTEMPTS=30
SLEEP=10
DEPLOYMENT="deployment/django"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT -n $PRINTNANNY_NAMESPACE"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((ATTEMPTS + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done