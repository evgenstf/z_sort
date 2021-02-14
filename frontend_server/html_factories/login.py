from html_factories.base import *
from handlers import z_sort_handler

class LoginHtmlFactory:
    @staticmethod
    def create():
        login_template_html = open('templates/html/login.html', 'r').read()
        z_sort_handler.login_page
        return BaseLoginHtmlFactory.create_from_content(login_template_html)
