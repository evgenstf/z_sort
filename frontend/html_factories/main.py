from markdown import markdown
from html_factories.base import *
from html_factories.category import get_article_by_path


def discover_articles_from_meta(meta, path):
    articles = []
    for item_name, item_meta in meta['items'].items():
        if item_meta['type'] == 'article':
            item_meta['path'] = path + [item_meta['id']]
            item_meta['link'] = '/' + '/'.join(path) + '/' + item_meta['id']
            item_meta['parent_link'] = '/' + '/'.join(path)
            item_meta['parent_color'] = meta['color']
            item_meta['parent_header'] = meta['header']
            articles.append(item_meta)
        else:
            articles.extend(discover_articles_from_meta(item_meta, path + [item_meta['id']]))
    return articles


class MainHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_meta(meta):
        article_preview_html_template = open('static/html/article_preview.html', 'r').read()
        js = open('static/js/article.js', 'r').read()
        css = open('static/css/article.css', 'r').read() + open('static/css/article_preview.css', 'r').read()

        previews_html = ''

        articles = discover_articles_from_meta(meta, [])

        for article_meta in articles:
            article = get_article_by_path(article_meta['path'])
            previews_html += deescape_django_macroses(escape_django_macroses(article_preview_html_template).format(
                    article_header='<br>'.join(article_meta['header']),
                    article_parent_color=article_meta['parent_color'],
                    article_link=article_meta['link'],
                    article_parent_link=article_meta['parent_link'],
                    article_parent_header=' '.join(article_meta['parent_header']),
                    article_reading_time=article_meta['reading_time'],
                    article_body=markdown(article['text'][:article['text'].find('\n', 100)]),
                    article_authors='<br>'.join(article_meta['authors']),
                    article_date=article_meta['date']))

        return BaseHtmlFactory.create_from_content(previews_html, js, css)