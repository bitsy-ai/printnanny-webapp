#!/bin/bash

set -euo pipefail

curl -s --user "api:$MAILGUN_API_KEY" \
    "https://api.mailgun.net/v3/$MAILGUN_DOMAIN/messages" \
    -F from='robots@print-nanny.com' \
    -F to="$PRINT_NANNY_EMAIL" \
    -F subject="🚀 Print Nanny sandbox ready: $GIT_BRANCH" \
    -F text="$body" << EOF
Your sandbox is ready! 💪

Version Info
--------
sha: $GIT_SHA
branch: $GIT_BRANCH
channel: $PRINT_NANNY_RELEASE_CHANNEL

Django
--------
url: $PRINT_NANNY_URL
admin: $PRINT_NANNY_URL/admin
api: $PRINT_NANNY_URL/api
user: $PRINT_NANNY_EMAIL
password: $PRINT_NANNY_PASSWORD

OctoPrint
--------
url: $OCTOPRINT_URL
user: $PRINT_NANNY_EMAIL
password: $PRINT_NANNY_PASSWORD

Google Cloud Platform
--------
project: $PROJECT
cluster: $CLUSTER
zone: $ZONE

WARNING: sandbox is deployed to a preemptible instance, which last no longer than 24 hours.
EOF