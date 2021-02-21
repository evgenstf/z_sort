from markdown import markdown
from html_factories.base import *

from storage.sql_article_connector import SQLArticleConnector

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create(url):
        article = SQLArticleConnector.get_article_by_url(url)

        return BaseHtmlFactory.create_from_content(article['html'], article['js'], article['css'])
