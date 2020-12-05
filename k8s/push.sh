#!/bin/bash

docker tag print_nanny_webapp_production_django:latest \
    us.gcr.io/print-nanny/print_nanny_webapp_production_django:latest

docker tag print_nanny_webapp_redis:latest \
    us.gcr.io/print-nanny/print_nanny_webapp_redis:latest

docker push us.gcr.io/print-nanny/print_nanny_webapp_production_django:latest
docker push us.gcr.io/print-nanny/print_nanny_webapp_redis:latest

#kubectl create configmap webapp --from-file=k8s/configmap.yml --dry-run -o yaml | kubectl apply -f -
#kubectl create configmap postgres --from-file=.envs/.production/.postgres --dry-run -o yaml | kubectl apply -f -
kubectl apply -f k8s/configmap.yml
kubectl apply -f k8s/production.yml


# gcloud iam service-accounts add-iam-policy-binding \
#   --role roles/iam.workloadIdentityUser \
#   --member "serviceAccount:print-nanny.svc.id.goog[default/sql-webapp]" \
#   sql-webapp@print-nanny.iam.gserviceaccount.com


# kubectl annotate serviceaccount \
#    sql-webapp \
#    iam.gke.io/gcp-service-account=sql-webapp@print-nanny.iam.gserviceaccount.com