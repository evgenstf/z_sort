class EditorHtmlFactory:
    @staticmethod
    def create(editor_html, editor_js, editor_css):
        html_template = open('templates/html/editor.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/editor.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        # html_template = html_template.replace('&content&', editor_html)
        # html_template = html_template.replace('&content_js&', editor_js)
        # html_template = html_template.replace('&content_css&', editor_css)

        return html_template