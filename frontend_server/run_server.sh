source ../configure_environment.sh
PYTHONPATH="$PYTHONPATH:../" ARTICLE_STATIC="$ARTICLE_REPO/static" python3 manage.py runserver localhost:2345 --insecure
