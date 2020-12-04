#!/bin/bash

gcloud docker push print_nanny_webapp_production_django:latest
kubectl apply configmap django --from-file=.envs/.production/.django
kubectl apply configmap postgres --from-file=.envs/.production/.postgres
kubectl apply k8s/production.yml