from markdown import markdown

"""
HTML_TEMPLATE = open('static/html/article.html', 'r').read()
CSS = open('static/css/article.css', 'r').read()
"""

def escape_django_macroses(article_html):
    return article_html.replace("{%", "DJANGO_MACROS_OPEN").replace("%}", "DJANGO_MACROS_CLOSE")

def deescape_django_macroses(article_html):
    return article_html.replace("DJANGO_MACROS_OPEN", "{%").replace("DJANGO_MACROS_CLOSE", "%}")

def patch_article_html(article_html):
    return article_html

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_article(article, path, parent_meta):
        HTML_TEMPLATE = open('static/html/article.html', 'r').read()
        CSS = open('static/css/article.css', 'r').read()
        JS = open('static/js/article.js', 'r').read()

        article_header_html = '<br>'.join(article['header'])
        article_body_html = patch_article_html(markdown(article['text']))

        article_html = escape_django_macroses(HTML_TEMPLATE).format(
                css=CSS,
                js=JS,
                article_header=article_header_html,
                article_parent_link='/' + '/'.join(path[:-1]),
                article_parent_header=' '.join(parent_meta['header']),
                article_parent_color=parent_meta['color'] if 'color' in parent_meta else 'var(--gray-color)',
                article_reading_time=article['reading_time'],
                article_body=article_body_html,
                article_authors='<br>'.join(article['authors']),
                article_date=article['date'])

        return deescape_django_macroses(article_html)
