from markdown import markdown
from html_factories.base import *


class Error404HtmlFactory:
    @staticmethod
    def create():
        html_template = open('templates/html/404_page.html', 'r').read()
        return Base404PageHtmlFactory.create_from_content(html_template)

class Error500HtmlFactory:
    @staticmethod
    def create():
        html_template = open('templates/html/500_page.html', 'r').read()
        return Base500PageHtmlFactory.create_from_content(html_template)
