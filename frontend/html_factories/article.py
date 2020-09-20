from markdown import markdown
from html_factories.base import *

def patch_article_html(article_html):
    return article_html

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_article(article, path, parent_meta):
        html_template = open('static/html/article.html', 'r').read()
        js = open('static/js/article.js', 'r').read()
        css = open('static/css/article.css', 'r').read()

        article_header_html = '<br>'.join(article['header'])
        article_body_html = patch_article_html(markdown(article['text']))

        article_html = deescape_django_macroses(escape_django_macroses(html_template).format(
                article_header=article_header_html,
                article_parent_link='/' + '/'.join(path[:-1]),
                article_parent_header=' '.join(parent_meta['header']),
                article_parent_color=parent_meta['color'] if 'color' in parent_meta else 'var(--gray-color)',
                article_reading_time=article['reading_time'],
                article_body=article_body_html,
                article_authors='<br>'.join(article['authors']),
                article_date=article['date']))

        return BaseHtmlFactory.create_from_content(article_html, js, css)
