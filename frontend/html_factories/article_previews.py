from markdown import markdown
from html_factories.base import BaseHtmlFactory

class ArticlePreviewsHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_content(article_previews):
        content = ''
        for preview in article_previews:
            content += '<a href="a/{0}"><div>{1}</div></a>\n'.format(preview['id'], preview['header'])
        return BaseHtmlFactory.create_from_content(content)
