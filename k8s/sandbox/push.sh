#!/bin/bash
##
# app base image
##

set -eu

docker tag "print_nanny_webapp:$(git rev-parse HEAD)" \
    "us.gcr.io/printnanny-sandbox/print_nanny_webapp:$(git rev-parse --abbrev-ref HEAD)"

docker tag "print_nanny_webapp:$(git rev-parse HEAD)" \
    "us.gcr.io/printnanny-sandbox/print_nanny_webapp:$(git rev-parse HEAD)"

docker push "us.gcr.io/printnanny-sandbox/print_nanny_webapp:$(git rev-parse --abbrev-ref HEAD)"
docker push "us.gcr.io/printnanny-sandbox/print_nanny_webapp:$(git rev-parse HEAD)"

