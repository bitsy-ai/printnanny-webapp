#!/bin/bash

set -uo pipefail

echo "💥 Deleting resource $@"
kubectl delete --ignore-not-found=true -f "$@"