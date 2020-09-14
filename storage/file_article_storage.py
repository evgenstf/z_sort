import json

from entities.article import Article

class FileArticleStorage:
    def __init__(self, metafile_path):
        self.articles = None
        self.metafile_path = metafile_path
        self.reload()

    def reload(self):
        article_paths = json.load(open(self.metafile_path))['article_paths']
        self.articles = dict()
        for path in article_paths:
            text = open(path + '/article.md').read()
            attributes = json.load(open(path + '/attributes.json'))
            self.articles[attributes['id']] = Article(text, attributes)

    def article_by_id(self, id):
        return self.articles[id]
