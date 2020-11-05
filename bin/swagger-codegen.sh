#!/bin/bash

java -jar bin/swagger-codegen-cli.jar generate \
   -i http://localhost:8080/api/swagger.json \
   -l python \
   -o tmp/print_nanny_api.py