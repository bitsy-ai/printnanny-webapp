#!/bin/bash

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli validate \
    -i http://localhost:8000/api/schema --recommend

docker run --net=host --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i http://localhost:8000/api/schema \
    -g python-experimental \
    -o /local/clients/python \
    -c /local/clients/python.yaml \
    #--verbose

rsync -r clients/python octoprint.local:~/projects/octoprint-nanny-plugin/print_nanny/clients