#!/bin/bash

set -eux

wait-for-url() {
    echo "Checking availability: $1"
    timeout -s TERM 45 bash -c \
    'while [[ "$(curl -s -o /dev/null -L -w ''%{http_code}'' ${0})" != "200" ]];\
    do echo "Waiting for ${0}" && sleep 5;\
    done' ${1}
    echo "OK!"
    curl -I $1
}
wait-for-url $OCTOPRINT_URL