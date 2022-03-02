#!/bin/bash

set -u

kubectl apply -f dist/k8s/ns.yml
kubectl apply -f dist/k8s/ara.yml
kubectl apply -f dist/k8s/cloud-sql-proxy.yml
kubectl apply -f dist/k8s/cluster-issuer.yml
kubectl apply -f dist/k8s/django.yml
kubectl apply -f dist/k8s/janus.yml