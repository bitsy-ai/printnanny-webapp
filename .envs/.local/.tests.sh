#!/bin/bash

export DATABASE_URL="postgres://debug:debug@localhost:5432/print_nanny"
export REDIS_URL=redis://localhost:6379/0
export CELERY_BROKER_URL=redis://localhost:6379/0
export MAILGUN_API_KEY=""
export MAILGUN_DOMAIN=""
export DISCORD_TOKEN=""
export HONEYCOMB_API_KEY=""
export CELERY_FLOWER_USER=debug
export CELERY_FLOWER_PASSWORD=debug
export LOGLEVEL=debug
