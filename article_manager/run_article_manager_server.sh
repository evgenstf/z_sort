#!/bin/bash -e

#fuser -n tcp -k 9999

PYTHONPATH="$PYTHONPATH:../" python3 article_manager.py
