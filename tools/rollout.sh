#!/bin/bash

set -euo pipefail

kubectl  -n "$PRINTNANNY_NAMESPACE" set image deployment/django "django=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-worker=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-beat=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" --record

kubectl rollout status $DEPLOYMENT -n $PRINTNANNY_NAMESPACE --wait --timeout=20m
