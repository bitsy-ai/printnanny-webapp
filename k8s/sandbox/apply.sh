
#!/bin/bash

set -eu
echo "🌻 Creating sandbox environment from $GITHUB_SHA"
kubectl apply -f k8s/sandbox/configmap.yml
kubectl apply -f k8s/sandbox/monolith.yml
kubectl apply -f k8s/sandbox/certs.yml
kubectl apply -f k8s/sandbox/pv.yml
