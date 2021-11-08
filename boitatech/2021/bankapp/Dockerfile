FROM alpine AS builder

USER root

FROM alpine/socat

EXPOSE 20101

RUN adduser -D user

RUN apk --no-cache add  \
        wget            \
        ca-certificates \
        libstdc++
# Get and install glibc for alpine
ARG APK_GLIBC_VERSION=2.31-r0
ARG APK_GLIBC_FILE="glibc-${APK_GLIBC_VERSION}.apk"
ARG APK_GLIBC_BIN_FILE="glibc-bin-${APK_GLIBC_VERSION}.apk"
ARG APK_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${APK_GLIBC_VERSION}"
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub \
    && wget "${APK_GLIBC_BASE_URL}/${APK_GLIBC_FILE}"       \
    && apk --no-cache add "${APK_GLIBC_FILE}"               \
    && wget "${APK_GLIBC_BASE_URL}/${APK_GLIBC_BIN_FILE}"   \
    && apk --no-cache add "${APK_GLIBC_BIN_FILE}"           \
    && rm glibc-*

COPY bankapp /home/user/
COPY libc-2.31.so /home/user/
COPY ld-linux-x86-64.so.2 /home/user/
COPY flag.txt /home/user/

USER user

ENTRYPOINT []
CMD cd /home/user && socat -dd TCP4-LISTEN:20101,fork,reuseaddr EXEC:./bankapp,pty,echo=0,raw,iexten=0