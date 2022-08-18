#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput
python manage.py migrate


# set the nsc store directory
if [ -z "${NSC_STORE}" ]; then
    echo "WARNING: NSC_STORE variable is not set! The default nsc store location will be used"
else
    mkdir -p "$NSC_STORE"
    nsc env --store "$NSC_STORE"
fi

if [ "$DJANGO_SUPERUSER_EMAIL" ]
then
    python manage.py createsuperuser \
        --noinput \
        --email "$DJANGO_SUPERUSER_EMAIL" || \
    echo "User already exists: $DJANGO_SUPERUSER_EMAIL"
fi

uvicorn config.asgi:application --host 0.0.0.0 --reload --reload-dir print_nanny_webapp --timeout-keep-alive "$TIMEOUT_KEEP_ALIVE"
