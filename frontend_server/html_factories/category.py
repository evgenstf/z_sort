from markdown import markdown
from html_factories.base import *

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
    def create_from_meta(meta, path):
        previews_html = ''

        js = """
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>"""
        css = "<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">"


        for article_name, article_meta in meta['items'].items():
            article_preview = open(get_article_by_path(path + [article_name])['preview_html'], 'r').read()

            previews_html += article_preview

        return BaseHtmlFactory.create_from_content(previews_html, js, css)
