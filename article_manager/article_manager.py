from storage.sql_article_connector import SQLArticleConnector

from frontend_server.settings import DEBUG

def create_path_tree(meta_tree):
    try:
        path_tree = None
        if 'items' in meta_tree:
            path_tree = {}
            for item_name, item_meta in meta_tree['items'].items():
                path_tree[item_name] = create_path_tree(item_meta)
        return path_tree
    except:
        import sys
        print('[error] create path tree unexpected error:', sys.exc_info()[0])
        return None


class ArticleManager:
    def __init__(self, article_storage):
        self.article_storage = article_storage

    def article_by_path(self, path):
        if DEBUG:
            self.article_storage.reload()
        return self.article_storage.article_by_path(path)

    def meta_by_path(self, path):
        if DEBUG:
            self.article_storage.reload()
        return self.article_storage.meta_by_path(path)

    def path_tree(self):
        if DEBUG:
            self.article_storage.reload()
        return create_path_tree(self.article_storage.meta_tree)


paths = []

def dive_articles(tree, path):
    if tree == None:
        paths.append(path)
        return

    for node, subtree in tree.items():
        dive_articles(subtree, path + [node])


def main():
    import socketserver
    import json
    import argparse
    from storage.file_article_storage import FileArticleStorage

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=9999, type=int)
    parser.add_argument('--max-request-length', default=4024)
    parser.add_argument('--storage-path')

    args = parser.parse_args()

    storage = FileArticleStorage(args.storage_path)
    article_manager = ArticleManager(storage)

    path_tree = create_path_tree(storage.meta_tree)

    print('path_tree:', path_tree)

    dive_articles(path_tree, [])

    SQLArticleConnector

    for path in paths:
        print('load:', path)
        article = article_manager.article_by_path(path)

        print('article header:', article.header)

        article_dict = {}
        article_dict['id'] = SQLArticleConnector.get_next_article_id()
        article_dict['header'] = json.dumps(article.header)
        article_dict['date'] = article.date
        article_dict['authors'] = json.dumps(article.authors)
        article_dict['sections'] = json.dumps(article.sections)
        article_dict['tags'] = json.dumps([path[-1]])

        html = open(args.storage_path + '/' + '/'.join(path) + '/content.html').read()
        preview_html = open(args.storage_path + '/' + '/'.join(path) + '/preview.html').read()

        article_dict['html'] = html
        article_dict['preview_html'] = preview_html

        res = SQLArticleConnector.add_new_article(article_dict)

        print(' added article with id:', article_dict['id'])


if __name__ == '__main__':
    main()
