#/bin/bash -e

source ../configure_environment.sh
PYTHONPATH="$PYTHONPATH:../" python3 compile.py "$ARTICLE_REPO"
