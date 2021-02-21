from html_factories.base import *

class EditorHtmlFactory:
    @staticmethod
    def create(editor_article_html, editor_js, editor_css):
        editor_template_html = open('templates/html/editor.html', 'r').read()
        editor_template_html = editor_template_html.replace('&editor_article&', editor_article_html)
        return BaseEditorHtmlFactory.create_from_content(editor_template_html, editor_js, editor_css)
