#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput
python manage.py migrate
# initialize nsc operator and robot account(s)
python manage.py nsc_init --name=PrintNannyDjangoOperator || echo "DjangoOperator already created"

# initialize stripe product/shop models
python manage.py djstripe_sync_models Product
python manage.py djstripe_sync_models Price
python manage.py loaddata print_nanny_webapp/shop/fixtures/test_product.json --app shop.Product

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

python manage.py initrobots --name=firehose || echo "Firehose robot already exists"

uvicorn config.asgi:application --host 0.0.0.0 --port 8080 --reload --reload-dir print_nanny_webapp --timeout-keep-alive "$TIMEOUT_KEEP_ALIVE"
