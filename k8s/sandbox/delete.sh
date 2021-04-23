#!/bin/bash
kubectl delete -f k8s/sandbox/configmap.yml
kubectl delete -f k8s/sandbox/monolith.yml

