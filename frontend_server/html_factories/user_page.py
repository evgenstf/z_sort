from html_factories.base import *

from storage.sql_article_connector import SQLArticleConnector

class UserPageHtmlFactory:
    @staticmethod
    def create(username):
        user_page_template_html = open('templates/html/user_page.html', 'r').read()
        articles = SQLArticleConnector.get_articles_by_author(username)
        articles_num = len(articles)
        html_articles = ""
        for article in articles:
            html_articles += article['html']
        user_page_template_html = user_page_template_html.replace('&content&', html_articles)

        return articles_num, BaseUserPageHtmlFactory.create_from_content(user_page_template_html)
