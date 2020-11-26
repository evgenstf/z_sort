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
        article_preview_html_template = open('static/html/article_preview.html', 'r').read()
        js = open('static/js/article.js', 'r').read()
        css = open('static/css/article.css', 'r').read() + open('static/css/article_preview.css', 'r').read()

        previews_html = ''

        for article_name, article_meta in meta['items'].items():
            article = get_article_by_path(path + [article_name])

            article_preview_html_template = article_preview_html_template.replace('&article_header&', '<br>'.join(article_meta['header']))
            article_preview_html_template = article_preview_html_template.replace('&article_parent_color&', meta['color'])
            article_preview_html_template = article_preview_html_template.replace('&article_link&', '/'+'/'.join(path) + '/' + article_name)
            article_preview_html_template = article_preview_html_template.replace('&article_parent_link&', '/'+'/'.join(path))
            article_preview_html_template = article_preview_html_template.replace('&article_parent_header&', ' '.join(meta['header']))
            article_preview_html_template = article_preview_html_template.replace('&article_reading_time&', article_meta['reading_time'])
            article_preview_html_template = article_preview_html_template.replace('&article_body&', markdown(article['items'][0]['content']))
            article_preview_html_template = article_preview_html_template.replace('&article_authors&', '<br>'.join(article_meta['authors']))
            article_preview_html_template = article_preview_html_template.replace('&article_date&', article_meta['date'])

            previews_html += article_preview_html_template

        return BaseHtmlFactory.create_from_content(previews_html, js, css)
