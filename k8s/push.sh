#!/bin/bash

docker tag print_nanny_webapp_production_django:latest us.gcr.io/print-nanny/print_nanny_webapp_production_django

docker push us.gcr.io/print-nanny/print_nanny_webapp_production_django
kubectl apply configmap django --from-file=.envs/.production/.django
kubectl apply configmap postgres --from-file=.envs/.production/.postgres
kubectl apply k8s/production.yml