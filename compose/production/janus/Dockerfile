FROM ubuntu:20.04 AS builder

ARG LIBWEBSOCKETS_REPO=https://github.com/warmcat/libwebsockets.git
ARG LIBWEBSOCKETS_VERSION=v3.2-stable

ARG LIBNICE_REPO=https://github.com/libnice/libnice
ARG LIBNICE_VERSION=0.1.18

ARG USRSCTP_REPO=https://github.com/sctplab/usrsctp
ARG USRSCTP_VERSION=0.9.5.0

ARG LIBSRTP_VERSION=2.2.0
ARG LIBSRTP_TARBALL="https://github.com/cisco/libsrtp/archive/v${LIBSRTP_VERSION}.tar.gz"

ARG JANUS_REPO=https://github.com/meetecho/janus-gateway.git
ARG JANUS_VERSION=0.11.8

ARG LIB_PREFIX=/usr/local
ARG JANUS_INSTALL=/opt/janus

RUN DEBIAN_FRONTEND=noninteractive apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
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
    # clean up cache + unused packages
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /build/janus
RUN mkdir -p /build/libwebsockets
RUN mkdir -p /build/libnice
RUN mkdir -p /build/usrsctp
RUN mkdir -p /build/libsrtp
RUN mkdir -p /opt/janus

# clone source repos
RUN git clone --single-branch --branch ${LIBWEBSOCKETS_VERSION} ${LIBWEBSOCKETS_REPO} /build/libwebsockets
RUN git clone --single-branch --branch ${LIBNICE_VERSION} ${LIBNICE_REPO} /build/libnice
RUN git clone --single-branch --branch ${USRSCTP_VERSION} ${USRSCTP_REPO} /build/libusrsctp
RUN git clone --single-branch --branch v${JANUS_VERSION} ${JANUS_REPO} /build/janus
# download + extract source tarball
RUN wget -qO- ${LIBSRTP_TARBALL} | tar -xvz -C /build/

# build + install libnice
RUN pip3 install --upgrade pip wheel setuptools
RUN pip3 install meson ninja
WORKDIR /build/libnice
RUN meson --prefix=${LIB_PREFIX} build
RUN ninja -C build
RUN ninja -C build install

# build + install libsrtp
WORKDIR /build/libsrtp-${LIBSRTP_VERSION}
RUN ./configure --prefix=${LIB_PREFIX} --enable-openssl
RUN make shared_library
RUN make install

# build + install libwebsockets
WORKDIR /build/libwebsockets
RUN cmake -DLWS_MAX_SMP=1 -DLWS_WITHOUT_EXTENSIONS=0 -DCMAKE_INSTALL_PREFIX:PATH=${LIB_PREFIX} -DCMAKE_C_FLAGS="-fpic" .
RUN make
RUN make install

# build + install libusrsctp
WORKDIR /build/libusrsctp
RUN ./bootstrap
RUN ./configure --prefix=${LIB_PREFIX} --disable-programs --disable-inet --disable-inet6

# build + install janus
WORKDIR /build/janus
RUN sh autogen.sh
RUN ./configure --prefix=${JANUS_INSTALL} --disable-rabbitmq --disable-mqtt --disable-nanomsg --disable-plugin-recordplay --disable-plugin-sip
RUN make
RUN make install

# copy artifacts into runtime container
FROM ubuntu:20.04 AS runtime
COPY --from=builder /usr/local/lib /usr/local/lib
COPY --from=builder /opt/janus /opt/janus
# /etc/janus mounted from external volume, sample configs provided for demonstration purposes only
COPY --from=builder /opt/janus/etc/janus/janus.jcfg.sample /etc/janus/janus.jcfg
COPY --from=builder /opt/janus/etc/janus/janus.transport.http.jcfg.sample /etc/janus/janus.transport.http.jcfg
COPY --from=builder /opt/janus/etc/janus/janus.transport.websockets.jcfg.sample /etc/janus/janus.transport.websockets.jcfg
COPY --from=builder /opt/janus/etc/janus/janus.plugin.streaming.jcfg.sample /etc/janus/janus.plugin.streaming.jcfg

ENTRYPOINT /opt/janus/bin/janus
CMD ["--configs-folder", "/etc/janus"]