import sys
sys.path.append(".")

import json
from html_compiler.html_factories.article import ArticleHtmlFactory
from html_compiler.html_factories.article_preview import ArticlePreviewHtmlFactory

def compile_item(absolute_path, relative_path, article_static_path):
    print(' ', '/'.join(absolute_path))

    meta = get_meta_by_path(absolute_path)
    if meta['type'] == 'article':
        return compile_article(absolute_path, relative_path, article_static_path)
    elif 'items' in meta:
        for item in meta['items']:
            compile_item(absolute_path + [item], relative_path + [item], article_static_path)


def compile_article(article_json):
    result = {}

    result['html'] = '{% load static %} ' + ArticleHtmlFactory.build_html(article_json=article_json)

    result['js'] = """
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>"""

    result['css'] = "<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">"

    return result

def main():
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('start compile:')

    absolute_path = os.path.abspath(args.path)
    absolute_article_static_path = absolute_path + '/static'
    compile_item(absolute_path.split('/'), [], absolute_article_static_path)

if __name__ == '__main__':
    main()
