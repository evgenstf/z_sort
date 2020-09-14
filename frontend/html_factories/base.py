class BaseHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(content):
        HEADER = open('static/html/base.html', 'r').read()
        return HEADER.format(content)
