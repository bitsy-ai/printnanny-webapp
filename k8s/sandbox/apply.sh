
#!/bin/bash

kubectl apply -f k8s/sandbox/configmap.yml
kubectl apply -f k8s/sandbox/monolith.yml

