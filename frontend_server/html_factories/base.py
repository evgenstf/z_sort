class BaseHtmlFactory:
    def __init__(self):
        self.template = None

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

class BaseEditorHtmlFactory:
    def __init__(self):
        self.template = None

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

class BaseRegisterHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content):
        html_template = open('templates/html/base_register.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)

        return html_template

class BaseLoginHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content):
        html_template = open('templates/html/base_login.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)

        return html_template

class BaseUserPageHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content):
        html_template = open('templates/html/base_user_page.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)

        return html_template

class BaseErrorHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content, error_code):
        html_template = open('templates/html/base_error.html', 'r').read()
        base_js = open('templates/js/base.js', 'r').read()
        base_css = open('templates/css/base.css', 'r').read()

        html_template = html_template.replace('&base_js&', base_js)
        html_template = html_template.replace('&base_css&', base_css)

        html_template = html_template.replace('&content&', content)

        html_template = html_template.replace('&error_code&', error_code)

        return html_template
