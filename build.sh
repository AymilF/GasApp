#!/bin/bash

set -euo pipefail;

IMAGENAME=${1:-gasapp}
TAGNAME=${2:-latest}

docker build . --tag $IMAGENAME:$TAGNAME
