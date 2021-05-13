from html_factories.base import *
from django.conf import settings
from django.contrib.staticfiles import finders

from storage.sql_article_connector import SQLArticleConnector

class UserPageHtmlFactory:
    @staticmethod
    def create(username):
        user_page_template_html = open('templates/html/user_page.html', 'r').read()
        articles = SQLArticleConnector.get_articles_by_author(username)
        articles_num = len(articles)
        html_articles = ""
        for article in articles:
            html_articles += article['preview_html']
        user_page_template_html = user_page_template_html.replace('&content&', html_articles)
        user_page_profile_pic_path = UserPageHtmlFactory.__generateUserPageProfilePicPath(username)
        user_page_template_html = user_page_template_html.replace(
            '<!-- user profile picture -->', 
            user_page_profile_pic_path,
        )

        return articles_num, BaseUserPageHtmlFactory.create_from_content(user_page_template_html)

    @staticmethod
    def __generateUserPageProfilePicPath(username: str) -> str:
        expected_profile_picture_relative_path = 'media/profile_pictures/' + username
        return settings.STATIC_URL + \
            finders.find(expected_profile_picture_relative_path) 
                ? expected_profile_picture_relative_path 
                : 'svg/user_ico.svg'
