from frontend.settings import DEBUG


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

    class TCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(args.max_request_length).strip()
            print('client: {}'.format(self.client_address[0]), 'request: {}', self.data)
            request = json.loads(self.data)

            response = '{error_message:"unsupported request type"}'
            if request['type'] == 'article':
                response = json.dumps(article_manager.article_by_path(request['path']).to_full_dict())
            elif request['type'] == 'meta':
                response = json.dumps(article_manager.meta_by_path(request['path']))
            elif request['type'] == 'path_tree':
                response = json.dumps(article_manager.path_tree())

            self.request.sendall(str.encode(response))

    with socketserver.TCPServer((args.host, args.port), TCPHandler) as server:
        print('start server on', args.host, args.port)
        server.serve_forever()

if __name__ == '__main__':
    main()
