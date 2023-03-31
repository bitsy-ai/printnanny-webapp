#!/bin/bash

set -euo pipefail

DEPLOYMENT="deployment/django"

kubectl  -n "$PRINTNANNY_NAMESPACE" set image "$DEPLOYMENT" "django=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-worker=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" "celery-beat=us.gcr.io/${GCP_PROJECT}/print_nanny_webapp:${GIT_SHA}" --record

kubectl rollout status "$DEPLOYMENT" -n "$PRINTNANNY_NAMESPACE" --wait
