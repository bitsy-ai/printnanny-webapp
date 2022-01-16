#!/bin/bash

set -uo pipefail

kubectl delete --ignore-not-found=true -f "$@"