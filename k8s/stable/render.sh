#!/bin/bash

set -u

pip install j2cli[yaml]

j2 k8s/stable/configmap.j2 -o k8s/prod/configmap.yml
j2 k8s/stable/ara-config.j2 -o k8s/prod/ara-config.yml
echo "🌳 Generated deployment config for $PRINT_NANNY_USER"
