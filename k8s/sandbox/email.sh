#!/bin/bash
set -e
set -uo pipefail

read -r -d '' body << EOF
Your sandbox is ready! 💪

Version Info
-----------------------
sha: $GIT_SHA
branch: $GIT_BRANCH
release channel: $PRINT_NANNY_RELEASE_CHANNEL

Django
-----------------------
url: $PRINT_NANNY_URL
admin: $PRINT_NANNY_URL/admin
api: $PRINT_NANNY_URL/api
user: $PRINT_NANNY_EMAIL
password: $PRINT_NANNY_PASSWORD

OctoPrint
-----------------------
url: $OCTOPRINT_URL
user: $PRINT_NANNY_EMAIL
password: $PRINT_NANNY_PASSWORD

Google Cloud Platform
-----------------------
project: $PROJECT
cluster: $CLUSTER
zone: $ZONE

WARNING: sandbox is deployed to a preemptible node! Availability is not guaranteed. Max lifetime is generally 24 hours. Local data will be deleted.

OctoPrint and Postgres deployment use a PersistentVolumeClaim to persist data.
https://cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms
EOF

echo $PRINT_NANNY_EMAIL
curl -s --user "api:$MAILGUN_API_KEY" \
    "https://api.mailgun.net/v3/$MAILGUN_DOMAIN/messages" \
    -F from='robots@print-nanny.com' \
    -F to="$PRINT_NANNY_EMAIL" \
    -F subject="🚀 Print Nanny sandbox ready: $GIT_BRANCH" \
    -F text="$body"

echo "📮 Sandbox is ready! Sent details to email: $PRINT_NANNY_EMAIL"