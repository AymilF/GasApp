#!/bin/bash

set -euo pipefail;

IMAGENAME=${1:-gasapp:latest}
CONTAINERNAME=${2:-gasappcontainer}
PORT=${3:-8081}

docker run -d -p $PORT:8080 --rm --name $CONTAINERNAME $IMAGENAME
