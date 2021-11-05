FROM ubuntu:20.04
ARG NEBULA_VERSION=v1.4.0

RUN apt-get update && \
    apt-get install -y \
    wget && \
    apt-get clean

RUN wget https://github.com/slackhq/nebula/releases/download/${NEBULA_VERSION}/nebula-linux-amd64.tar.gz
RUN tar -xvf nebula-linux-amd64.tar.gz -C /usr/local/bin/

ENTRYPOINT /usr/local/nebula