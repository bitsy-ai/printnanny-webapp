#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

python manage.py collectstatic --noinput

compress_enabled() {
python << END
import sys

from environ import Env

env = Env(COMPRESS_ENABLED=(bool, True))
if env('COMPRESS_ENABLED'):
    sys.exit(0)
else:
    sys.exit(1)

END
}

python manage.py migrate

# if compress_enabled; then
#   # NOTE this command will fail if django-compressor is disabled
#   python /app/manage.py compress
# fi
set +u
if [ "$DJANGO_SUPERUSER_EMAIL" ]
then
    python manage.py createsuperuser \
        --noinput \
        --email "$DJANGO_SUPERUSER_EMAIL" || \
    echo "User already exists: $DJANGO_SUPERUSER_EMAIL"
fi
set -u

uvicorn config.asgi:application --host 0.0.0.0
