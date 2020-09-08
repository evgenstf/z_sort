class ArticleManager:
    def __init__(self, article_storage, image_storage=None):
        self.article_storage = article_storage
        self.image_storage = image_storage

    def article_by_id(self, id):
        return self.article_storage.article_by_id(id)

def main():
    import socketserver
    import json
    from storage.file_article_storage import FileArticleStorage
    from html_factories.article import ArticleHtmlFactory

    HOST, PORT = 'localhost', 9999
    MAX_REQUEST_LENGTH = 4024

    storage = FileArticleStorage('/Users/evgenstf/nlogn_articles/file_article_storage_metafile.json')
    article_manager = ArticleManager(storage)

    html_factory = ArticleHtmlFactory()

    class TCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(MAX_REQUEST_LENGTH).strip()
            print('client: {}'.format(self.client_address[0]), 'request: {}', self.data)
            data = json.loads(self.data)

            markdown_content = article_manager.article_by_id(data['id']).text
            html = html_factory.create_from_markdown(markdown_content)

            self.request.sendall(str.encode(html))

    with socketserver.TCPServer((HOST, PORT), TCPHandler) as server:
        print('start server on', HOST, PORT)
        server.serve_forever()

if __name__ == '__main__':
    main()
