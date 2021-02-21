import json

from markdown import markdown
from html_factories.base import *

from storage.sql_article_connector import SQLArticleConnector

class MainHtmlFactory:
    @staticmethod
    def create():
        previews_html = ''

        js = """
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/mathjax.js?config=tex-ams-mml_htmlormml">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>"""
        css = "<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">"

        articles = SQLArticleConnector.get_top10_articles()

        for article in articles:
            previews_html += article['preview_html']

        return BaseHtmlFactory.create_from_content(previews_html, js, css)
