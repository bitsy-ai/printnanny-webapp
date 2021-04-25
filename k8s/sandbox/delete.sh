#!/bin/bash

set -uo pipefail

echo "💥 Tearing down sandbox environment for $PRINT_NANNY_USER"
kubectl delete --ignore-not-found=true -f k8s/sandbox/configmap.yml
kubectl delete --ignore-not-found=true -f k8s/sandbox/monolith.yml
