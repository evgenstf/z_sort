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

class MainHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_meta(meta):
        previews_html = ''

        for category_name, category_meta in meta['items'].items():
            previews_html += '<a href="{path}"><h1>{header}</h1></a>'.format(
                    path='/' + category_name,
                    header='<br>'.join(category_meta['header']))

        return BaseHtmlFactory.create_from_content(previews_html, '', '')
