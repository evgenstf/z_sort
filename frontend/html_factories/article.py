from markdown import markdown
from html_factories.base import BaseHtmlFactory

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_article(article):
        return BaseHtmlFactory.create_from_content(markdown(article['text']))
