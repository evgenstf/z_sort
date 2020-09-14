class ArticleManager:
    def __init__(self, article_storage, image_storage=None):
        self.article_storage = article_storage
        self.image_storage = image_storage

    def article_by_id(self, id):
        self.article_storage.reload() # TODO(evgenstf): remove
        return self.article_storage.article_by_id(id)

    def all_article_previews(self):
        previews = []
        for id, article in self.article_storage.articles.items():
            previews.append(article.to_preview_dict())
        return previews

def main():
    import socketserver
    import json
    from storage.file_article_storage import FileArticleStorage

    HOST, PORT = 'localhost', 9999
    MAX_REQUEST_LENGTH = 4024

    storage = FileArticleStorage('/Users/evgenstf/articles/metafile.json')
    article_manager = ArticleManager(storage)

    class TCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(MAX_REQUEST_LENGTH).strip()
            print('client: {}'.format(self.client_address[0]), 'request: {}', self.data)
            request = json.loads(self.data)

            response = '{error_message:"unsupported request type"}'
            if request['type'] == 'article':
                response = json.dumps(article_manager.article_by_id(request['id']).to_full_dict())
            elif request['type'] == 'all_article_previews':
                response = json.dumps(article_manager.all_article_previews())

            self.request.sendall(str.encode(response))

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        print('start server on', HOST, PORT)
        server.serve_forever()

if __name__ == '__main__':
    main()
