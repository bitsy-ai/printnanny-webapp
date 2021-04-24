#!/bin/bash

set -eux

wait-for-url() {
    echo "Checking availability: $1"
    timeout -s TERM 300 bash -c \
    'while [[ "$(curl -s -o /dev/null -L -w ''%{http_code}'' ${0})" != "200" ]];\
    do echo "Waiting 30s for ${0}" && sleep 30;\
    done' ${1}
    echo "OK!"
    curl -I $1
}
wait-for-url $OCTOPRINT_URL