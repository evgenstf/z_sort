from markdown import markdown
from html_factories.base import *


class ErrorHtmlFactory:
    @staticmethod
    def create(error_code):
        html_template = open('templates/html/' + error_code + '_page.html', 'r').read()
        return BaseErrorHtmlFactory.create_from_content(html_template, error_code)
