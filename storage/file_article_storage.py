class FileArticleStorage:
    def __init__(self, metapath):
        self.metapath = metapath
        self.article_paths = None

        self.reload()

    def reload(self):
        article_paths = [path.strip() for path in open(self.metapath).readlines()]
        self.article_paths = set(article_paths)