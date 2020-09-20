import json
import os

from entities.article import Article

def discover_meta_tree(path):
    print('discover meta tree from path:', path)
    try:
        meta = json.load(open(path + '/meta.json'))
    except FileNotFoundError:
        print('[error] cannot open meta for:', path)
        return None

    if 'items' in meta:
        items = {}
        for item in meta['items']:
            meta_subtree = discover_meta_tree(path + '/'+ item)
            if meta_subtree:
                items[item] = meta_subtree
        meta['items'] = items
    return meta


class FileArticleStorage:
    def __init__(self, path):
        self.path = path
        self.reload()

    def reload(self):
        self.articles = dict()
        self.meta_tree = discover_meta_tree(self.path)

    def meta_by_path(self, path):
        try:
            meta = self.meta_tree
            for node in path:
                meta = meta['items'][node]
            return meta
        except:
            import sys
            print('[error] meta by path unexpected error:', sys.exc_info()[0], "path:", path)
            return None


    def article_by_path(self, path):
        relative_path = '/'.join(path)
        if relative_path not in self.articles:
            text = open(self.path + '/' + relative_path + '/article.md').read()
            self.articles[relative_path] = Article(text, self.meta_by_path(path))
        return self.articles[relative_path]
