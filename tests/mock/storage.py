from entities.article import Article
from entities.image import Image

class MockStorage:
    def __init__(self, article_count, image_count):
        self.articles = [Article() for i in range(article_count)]
        self.images = [Image() for i in range(image_count)]

    def article_by_id(self, id):
        return self.articles[id]

    def image_by_id(self, id):
        return self.images[id]