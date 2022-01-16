#!/bin/bash
set -eu

ATTEMPTS=0
MAX_ATTEMPTS=30
SLEEP=10
DEPLOYMENT="deployment/webapp"
ROLLOUT_STATUS_CMD="kubectl rollout status $DEPLOYMENT"
until $ROLLOUT_STATUS_CMD || [ $ATTEMPTS -eq $MAX_ATTEMPTS ]; do
  $ROLLOUT_STATUS_CMD
  ATTEMPTS=$((ATTEMPTS + 1))
  echo "Waiting $SLEEP sec for $DEPLOYMENT rollout to complete"
  sleep $SLEEP
done
