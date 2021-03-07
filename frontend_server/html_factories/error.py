from markdown import markdown
from html_factories.base import *


class ErrorHtmlFactory:
    @staticmethod
    def create(error_code):
        html_template = open('templates/html/' + error_code + '_page.html', 'r').read()
        return BaseCustomHeaderHtmlFactory.create(html_template, error_code, error_code)
