class BaseHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content, content_js, content_css):
        html_template = open('static/html/base.html', 'r').read()
        base_js = open('static/js/base.js', 'r').read()
        base_css = open('static/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)
        html_template = html_template.replace('&content_js&', content_js)
        html_template = html_template.replace('&content_css&', content_css)

        return html_template
