#!/bin/bash

set -euo pipefail;

if [ $# -lt 3 ]; then
  echo "Usage `basename $0` imagename containername port"
  exit 1
fi

IMAGENAME=${1:-gasapp:latest}
CONTAINERNAME=${2:-gasappcontainer}
PORT=${3:-8081}

docker run -d -p $PORT:8080 --rm --name $CONTAINERNAME $IMAGENAME
docker logs -f $CONTAINERNAME
