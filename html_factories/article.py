from markdown import markdown
from html_factories import MainHtmlFactory

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    def create_from_markdown(self, markdown_content):
        joined_content = '\n'.join(markdown_content)
        return MainHtmlFactory.create_from_content(markdown(joined_content))