#!/bin/bash

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v4.1.3 validate \
    -i http://localhost:8000/api/schema --recommend

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli:v4.1.3 generate \
    -i http://localhost:8000/api/schema \
    -g python-experimental \
    -o /local/clients/python \
    -c /local/clients/python.yaml \
    # --global-property debugOperations
    # --global-property OpenAPI 



rsync -r clients/ octoprint.local:~/projects/octoprint-nanny-plugin/print_nanny/clients

