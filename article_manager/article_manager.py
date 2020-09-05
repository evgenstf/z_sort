class ArticleManager:
    def __init__(self, article_storage, image_storage=None):
        self.article_storage = article_storage
        self.image_storage = image_storage

    def article_by_it(self, id):
        return self.articles[id]
