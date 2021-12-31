FROM golang:1.17.5-alpine AS gcsfuse

RUN apk add --no-cache git
ENV GOPATH /go
RUN apk add --no-cache ca-certificates fuse

RUN go get -u github.com/googlecloudplatform/gcsfuse

FROM nginx:alpine
RUN apk add --no-cache ca-certificates fuse

COPY --from=gcsfuse /go/bin/gcsfuse /usr/local/bin

ADD nginx.conf /etc/nginx/nginx.conf
RUN mkdir -p /usr/share/nginx/public-data

EXPOSE 8080

CMD ["nginx"]