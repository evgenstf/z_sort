from markdown import markdown
from html_factories.base import *
from markdown_extensions.footnote import FootnoteExtension

import json

def patch_article_html(article_html):
    return article_html

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_article(meta, path, parent_meta):
        sections = json.loads(open('/'.join(path) + '/sections.json').read())

        js = open('static/js/article.js', 'r').read()
        css = open('static/css/article.css', 'r').read()

        article_header_html = '<br>'.join(meta['header'])

        article_body_html = ''
        for section in sections:
            article_body_html += patch_article_html(markdown(section['content'], extensions=['fenced_code', FootnoteExtension()]))

        article_html = open('static/html/article.html', 'r').read()
        article_html = article_html.replace('&article_header&', article_header_html)
        article_html = article_html.replace('&article_parent_link&', '/' + '/'.join(path[:-1]))
        article_html = article_html.replace('&article_parent_header&', ' '.join(parent_meta['header']))
        article_html = article_html.replace('&article_parent_color&', parent_meta['color'] if 'color' in parent_meta else 'var(--gray-color)')
        article_html = article_html.replace('&article_reading_time&', meta['reading_time'])
        article_html = article_html.replace('&article_body&', article_body_html)
        article_html = article_html.replace('&article_authors&', '<br>'.join(meta['authors']))
        article_html = article_html.replace('&article_date&', meta['date'])

        return BaseHtmlFactory.create_from_content(article_html, js, css)
