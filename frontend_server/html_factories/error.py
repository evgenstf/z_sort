from markdown import markdown
from html_factories.base import *


class Error404HtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create():
        html_template = open('templates/html/404_page.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)
        return html_template
