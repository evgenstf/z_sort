def escape_django_macroses(article_html):
    return article_html.replace("{%", "DJANGO_MACROS_OPEN").replace("%}", "DJANGO_MACROS_CLOSE")

def deescape_django_macroses(article_html):
    return article_html.replace("DJANGO_MACROS_OPEN", "{%").replace("DJANGO_MACROS_CLOSE", "%}")

class BaseHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content, content_js, content_css):
        html_template = open('static/html/base.html', 'r').read()
        base_js = open('static/js/base.js', 'r').read()
        base_css = open('static/css/base.css', 'r').read()

        return deescape_django_macroses(escape_django_macroses(html_template).format(
            base_js=base_js,
            base_css=base_css,

            content=content,
            content_js=content_js,
            content_css=content_css
        ))
