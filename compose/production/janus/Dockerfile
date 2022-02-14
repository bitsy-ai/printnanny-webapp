FROM ubuntu:20.04 AS builder

RUN DEBIAN_FRONTEND=non-interactive apt-get update \
    apt-get install -y \
        automake \
        build-essential \
        cmake \
        cmake-data \
        gengetopt \
        git \
        libconfig-dev \
        libcurl4-openssl-dev \
        libglib2.0-dev \
        libjansson-dev \
        liblua5.3-dev \
        libmicrohttpd-dev \
        libogg-dev \
        libopus-dev \
        libsofia-sip-ua-dev \
        libssl-dev \
        libsystemd-dev \
        libtool \
        ninja-build \
        pkg-config \
        wget \
        python3 \
        python3-pip \
        python3-venv
    # clean up cache + unused packages
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /buil/janus
RUN mkdir -p /build/libwebsockets
RUN mkdir -p /build/libnice
RUN mkdir -p /build/usrsctp
RUN mkdir -p /build/libsrtp