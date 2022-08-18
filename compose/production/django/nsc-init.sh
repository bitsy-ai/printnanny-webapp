#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

NATS_SERVER_URI="${NATS_SERVER_URI:-nats://nats:4222}"
NKEYS_IMPORT_DIR="${NKEYS_IMPORT_DIR:-/etc/django-operator-nkeys}"
DJANGO_OPERATOR_JWT="${DJANGO_OPERATOR_JWT:-/etc/django-operator-nkeys/operator.jwt}"
SYSTEM_ACCOUNT="${NATS_SYSTEM_ACCOUNT:-SYS}"
SYSTEM_ACCOUNT_USER="${NATS_SYSTEM_ACCOUNT_USER:-sys}"
SYSTEM_ACCOUNT_JWT="${SYSTEM_ACCOUNT_JWT:-/etc/django-operator-nkeys/SYS.jwt}"
SYSTEM_USER_JWT="${SYSTEM_USER_JWT:-/etc/django-operator-nkeys/sys.jwt}"

# set the nsc store directory
if [ -z "${NSC_STORE}" ]; then
    echo "WARNING: NSC_STORE variable is not set! The default nsc store location will be used"
else
    mkdir -p "$NSC_STORE"
    nsc env --store "$NSC_STORE"
fi

# import operator.jwt if /etc/django-operator-nkeys/ mount available
if [ -f "$DJANGO_OPERATOR_JWT" ] && [ -f "$SYSTEM_ACCOUNT_JWT" ] && [ -f "$SYSTEM_USER_JWT"  ]
then
    echo "Importing nkeys from $NKEYS_IMPORT_DIR"
    nsc import keys --dir "$NKEYS_IMPORT_DIR" --keystore-dir=/var/lib/nats/nsc/keys --config-dir=/var/lib/nats/nsc/config --data-dir=/var/lib/nats/nsc/stores
    echo "Loading Operator JWT from $DJANGO_OPERATOR_JWT"
    python manage.py nsc_operator_jwt --import "$DJANGO_OPERATOR_JWT"
    echo "Setting operator --account-jwt-server-url $NATS_SERVER_URI"
    nsc edit operator --account-jwt-server-url "$NATS_SERVER_URI" --keystore-dir=/var/lib/nats/nsc/keys --config-dir=/var/lib/nats/nsc/config --data-dir=/var/lib/nats/nsc/stores
    echo "Loading account JWT from $SYSTEM_ACCOUNT_JWT"
    python manage.py nsc_account_jwt --import "$SYSTEM_ACCOUNT_JWT"
    echo "Loading user JWT from $SYSTEM_USER_JWT"
    python manage.py nsc_user_jwt --import "$SYSTEM_USER_JWT"
    nsc pull --all --overwrite-newer --keystore-dir=/var/lib/nats/nsc/keys --config-dir=/var/lib/nats/nsc/config --data-dir=/var/lib/nats/nsc/stores --system-account "$SYSTEM_ACCOUNT" --system-user "$SYSTEM_ACCOUNT_USER"
fi
