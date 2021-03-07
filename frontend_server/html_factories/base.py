class BaseHtmlFactory:
    @staticmethod
    def create_from_content(content, content_js, content_css):
        html_template = open('templates/html/base.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)


        html_template = html_template.replace('&content&', content)
        html_template = html_template.replace('&content_js&', content_js)
        html_template = html_template.replace('&content_css&', content_css)

        return html_template

class BaseCustomPageHtmlFactory:
    @staticmethod
    def create(html_name, js_name, css_name, content, content_js, content_css):
        html_template = open('templates/html/' + html_name + '.html', 'r').read()
        base_js = open('templates/js/' + js_name + '.js', 'r').read()
        base_css = open('templates/css/' + css_name + '.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)
        html_template = html_template.replace('&content_js&', content_js)
        html_template = html_template.replace('&content_css&', content_css)

        return html_template


class BaseEditorHtmlFactory:
    @staticmethod
    def create_from_content(content, content_js, content_css):
        html_template = open('templates/html/base_editor.html', 'r').read()
        base_js = open('templates/js/base_editor.js', 'r').read()
        base_css = open('templates/css/base_editor.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)
        html_template = html_template.replace('&content_js&', content_js)
        html_template = html_template.replace('&content_css&', content_css)

        return html_template

class BaseUserPageHtmlFactory:
    @staticmethod
    def create_from_content(content):
        html_template = open('templates/html/base_user_page.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)

        html_template = html_template.replace('&tittle&', '{{ owner }}')
        html_template = html_template.replace('&header_name&', '{{ owner }}')

        return html_template
