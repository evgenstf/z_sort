from html_factories.base import *
from handlers import z_sort_handler

class UserPageHtmlFactory:
    @staticmethod
    def create():
        register_template_html = open('templates/html/user_page.html', 'r').read()
        z_sort_handler.user_page
        return BaseUserPageHtmlFactory.create_from_content(register_template_html)
