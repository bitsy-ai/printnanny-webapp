#!/bin/bash

export DATABASE_URL="postgres://debug:debug@postgres:5432/print_nanny"
export COTURN_SECRET_KEY="testsecret1234"
export COTURN_REALM="turn.test.com"
export COTURN_DATABASE_URL="postgres://debug:debug@postgres:5432/coturn"
export REDIS_URL=redis://redis:6379/0
export MAILGUN_API_KEY=""
export MAILGUN_DOMAIN=""
export DISCORD_TOKEN=""
export HONEYCOMB_API_KEY=""
export LOGLEVEL=debug