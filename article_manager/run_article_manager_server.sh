#!/bin/bash -e

#fuser -n tcp -k 9998

source ../configure_environment.sh
PYTHONPATH="$PYTHONPATH:../" python3 article_manager.py --storage-path "$ARTICLE_REPO" --port 9999
