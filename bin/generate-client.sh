#!/bin/bash

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli validate \
    -i http://localhost:8000/api/schema --recommend

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i http://localhost:8000/api/schema \
    -g python-legacy \
    -o /local/clients/python \
    -c /local/clients/python.yaml \
    # --global-property debugOperations
    # --global-property OpenAPI 



rsync -r clients/ octoprint.local:~/projects/octoprint-nanny-plugin/print_nanny/clients

