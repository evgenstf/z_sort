import json

from markdown import markdown
from html_factories.base import *
from html_factories.category import get_article_by_path
# from html_factories.editor import *


def discover_articles_from_meta(meta, path):
    articles = []
    for item_name, item_meta in meta['items'].items():
        if item_meta['type'] == 'article':
            item_meta['path'] = path + [item_meta['id']]
            articles.append(item_meta)
        else:
            articles.extend(discover_articles_from_meta(item_meta, path + [item_meta['id']]))
    return articles


class MainHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_meta(meta):
        previews_html = ''

        js = """
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>"""
        css = "<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">"

        articles = discover_articles_from_meta(meta, [])

        for article_meta in articles:
            article_preview = open(get_article_by_path(article_meta['path'])['preview_html'], 'r').read()

            previews_html += article_preview

        return BaseHtmlFactory.create_from_content(previews_html, js, css)
