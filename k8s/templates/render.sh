#!/bin/bash

set -u

pip install j2cli[yaml]

j2 k8s/templates/ns.j2 -o dist/k8s/ns.yml
j2 k8s/templates/configmap.j2 -o dist/k8s/configmap.yml
j2 k8s/templates/cluster-issuer.j2 -o dist/k8s/cluster-issuer.yml
j2 k8s/templates/cert.j2 -o dist/k8s/cert.yml
j2 k8s/templates/ingress.j2 -o dist/k8s/ingress.yml
j2 k8s/templates/django.j2 -o dist/k8s/django.yml
j2 k8s/templates/janus.j2 -o dist/k8s/janus.yml
j2 k8s/templates/gcsfuse.j2 -o dist/k8s/gcsfuse.yml
j2 k8s/templates/metabase.j2 -o dist/k8s/metabase.yml