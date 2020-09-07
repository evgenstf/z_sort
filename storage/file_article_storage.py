import json

from entities.article import Article

class FileArticleStorage:
    def __init__(self, metafile_path):
        self.articles = None
        self.reload(metafile_path)

    def reload(self, metafile_path):
        article_paths = json.load(open(metafile_path))['article_paths']
        self.articles = dict()
        for path in article_paths:
            text = open(path + '/article.md').readlines()
            attributes = json.load(open(path + '/attributes.json'))
            self.articles[attributes['id']] = Article(text, attributes)

    def article_by_id(self, id):
        return self.articles[id]