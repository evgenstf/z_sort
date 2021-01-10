from html_factories.base import *

class EditorHtmlFactory:
    @staticmethod
    def create(editor_html, editor_js, editor_css):
        editor_template_html = open('templates/html/editor.html', 'r').read()
        # editor_template_js = open('templates/js/editor.js', 'r').read()
        editor_template_css = open('templates/css/editor.css', 'r').read()

        # editor_template_html = editor_template_html.replace('&editor_js&', editor_template_js)
        editor_template_html = editor_template_html.replace('&editor_css&', editor_template_css)

        # html_template = html_template.replace('&content&', editor_html)
        # html_template = html_template.replace('&content_js&', editor_js)
        # html_template = html_template.replace('&content_css&', editor_css)

        return BaseHtmlFactory.create_from_content(editor_template_html, editor_js, editor_css)
