from markdown import markdown
from html_factories.base import *

from storage.sql_article_connector import SQLArticleConnector

def get_article_by_path(path):
    import socket
    import json

    sock = socket.socket()
    sock.connect(('localhost', 9999))
    sock.send(json.dumps({"type": 'article', "path": path}).encode())
    response = sock.recv(100000).decode("utf-8")
    sock.close()
    return json.loads(response)

class CategoryHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create(category):
        previews_html = ''

        js = """
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/mathjax.js?config=tex-ams-mml_htmlormml">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>"""
        css = "<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">"

        articles = SQLArticleConnector.get_articles_by_category(category)

        print('articles:', articles)
        for article in articles:
            previews_html += article['preview_html']

        return BaseHtmlFactory.create_from_content(previews_html, js, css)
