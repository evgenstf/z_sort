from markdown import markdown

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    def create_from_markdown(self, markdown_content):
        joined_content = '\n'.join(markdown_content)
        return markdown(joined_content)
