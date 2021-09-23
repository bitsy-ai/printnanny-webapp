#!/bin/bash

set -u

pip install j2cli[yaml]

j2 k8s/sandbox/configmap.j2 -o k8s/sandbox/configmap.yml
j2 k8s/sandbox/monolith.j2 -o k8s/sandbox/monolith.yml
echo "🌳 Generated deployment config for $PRINT_NANNY_USER"
cat k8s/sandbox/monolith.yml