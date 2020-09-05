class Storage:
    def __init__(self):
        self.articles = None
        self.images = None

    def article_by_id(self, id):
        return self.articles[id]

    def image_by_id(self, id):
        return self.images[id]