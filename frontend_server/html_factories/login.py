from html_factories.base import *

class LoginHtmlFactory:
    @staticmethod
    def create():
        login_template_html = open('templates/html/login.html', 'r').read()
        return BaseCustomHeaderHtmlFactory.create(login_template_html, 'Login', 'login')
