#!/bin/bash

docker build --tag=pwn_midenios . && \
docker run --privileged -p 1337:1337 --rm --name=pwn_midenios pwn_midenios
