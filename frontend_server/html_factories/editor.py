from html_factories.base import *

class EditorHtmlFactory:
    @staticmethod
    def create(editor_html, editor_js, editor_css):
        editor_template_html = open('templates/html/editor.html', 'r').read()
        return BaseHtmlFactory.create_from_content(editor_template_html, editor_js, editor_css)
