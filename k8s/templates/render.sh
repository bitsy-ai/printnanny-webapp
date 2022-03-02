#!/bin/bash

set -u

pip install j2cli[yaml]

j2 k8s/templates/ns.j2 -o dist/k8s/ns.yml
j2 k8s/templates/ara.j2 -o dist/k8s/ara.yml
j2 k8s/templates/cloud-sql-proxy.j2 -o dist/k8s/cloud-sql-proxy.yml
j2 k8s/templates/cluster-issuer.j2 -o dist/k8s/cluster-issuer.yml
j2 k8s/templates/django.j2 -o dist/k8s/django.yml
j2 k8s/templates/janus.j2 -o dist/k8s/janus.yml
