from html_factories.base import *
from handlers import z_sort_handler

class RegisterHtmlFactory:
    @staticmethod
    def create():
        register_template_html = open('templates/html/register.html', 'r').read()
        z_sort_handler.register_page
        return BaseRegisterHtmlFactory.create_from_content(register_template_html)
