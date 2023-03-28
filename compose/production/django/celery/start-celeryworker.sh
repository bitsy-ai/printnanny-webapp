#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


exec celery -A config.celery_app worker -l INFO