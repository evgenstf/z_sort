from html_factories.base import *

class RegisterHtmlFactory:
    @staticmethod
    def create():
        register_template_html = open('templates/html/register.html', 'r').read()
        return BaseCustomHeaderHtmlFactory.create(register_template_html, 'Register', 'register')
