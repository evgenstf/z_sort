class ArticleManager:
    def __init__(self):
        self.storage = None
        self.articles = None

    def article_by_it(self, id):
        return self.articles[id]
