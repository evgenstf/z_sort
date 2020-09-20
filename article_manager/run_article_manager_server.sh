#!/bin/bash -e

#fuser -n tcp -k 9998

PYTHONPATH="$PYTHONPATH:../" python3 article_manager.py --storage-path "/Users/evgenstf/articles" --port 9999
