#!/bin/bash

set -euo pipefail

kubectl  -n "$PRINTNANNY_NAMESPACE" set image deployment/django "django=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-worker=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-beat=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" --record
ATTEMPTS=0
MAX_ATTEMPTS=300
SLEEP=10
DEPLOYMENT="deployment/django"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT -n $PRINTNANNY_NAMESPACE"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((ATTEMPTS + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done
