
#!/bin/bash

set -eu
echo "🌻 Creating sandbox environment for $PRINT_NANNY_USER"
kubectl apply -f k8s/sandbox/configmap.yml
kubectl apply -f k8s/sandbox/monolith.yml
kubectl apply -f k8s/sandbox/certs.yml
