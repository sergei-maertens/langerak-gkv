#!/bin/bash

set -ex

CONTAINER_REPO=regexit/kerkwebsite

tag=${1:-latest}

push=${PUSH:-}

toplevel=$(git rev-parse --show-toplevel)
cd $toplevel

docker build \
    --target production \
    -t ${CONTAINER_REPO}:$tag \
    -f Dockerfile .
echo "Image built"

if [[ $PUSH ]]; then
    docker push ${CONTAINER_REPO}:$tag
    echo "Image pushed"
fi

