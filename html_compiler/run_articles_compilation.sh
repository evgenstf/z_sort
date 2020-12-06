#/bin/bash -e

source ../configure_environment.sh
python3 compile.py "$ARTICLE_REPO"
