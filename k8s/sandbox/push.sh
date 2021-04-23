##
# app base image
##

docker tag print_nanny_webapp_production_django:latest \
    us.gcr.io/print-nanny-sandbox/print_nanny_webapp_sandbox_django:$(git rev-parse --abbrev-ref HEAD)

docker tag print_nanny_webapp_production_django:latest \
    us.gcr.io/print-nanny-sandbox/print_nanny_webapp_sandbox_django:$(git rev-parse HEAD)

docker push us.gcr.io/print-nanny-sandbox/print_nanny_webapp_sandbox_django:$(git rev-parse --abbrev-ref HEAD)
docker push us.gcr.io/print-nanny-sandbox/print_nanny_webapp_sandbox_django:$(git rev-parse HEAD)

