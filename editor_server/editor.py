import re
import json

from html_compiler.compile import compile_item


def validate_id(id):
    return re.match("^[qwertyuiopasdfghjklzxcvbnm_1234567890]*$", id)


class Editor:
    def __init__(self, article_storage):
        self.article_storage = article_storage

    def create_article_by_id(self, id):
        return self.article_storage.create_article(['editor', id])

    def update_article_meta(self, article_id, new_meta):
        return self.article_storage.update_meta(['editor', article_id], new_meta)

    def update_article_sections(self, article_id, new_sections):
        return self.article_storage.update_sections(['editor', article_id], new_sections)

    def compile(self, article_id):
        article_absolute_path = self.article_storage.path.split('/') + ['editor', article_id]
        article_relative_path = ['in_editing', article_id]
        static_absolute_path = self.article_storage.path.split('/')  + ['static']
        try:
            compile_item(article_absolute_path, article_relative_path, static_absolute_path)
            return True
        except Exception as e:
            print("[error] Exception:", e)
            return False

    def get(self, article_id):
        content_path = self.article_storage.path + '/editor/' + article_id + '/content.html'

        with open(content_path, 'r') as file:
            return file.read()

    def save(self, article_id):
        from distutils.dir_util import copy_tree

        from_article_path = self.article_storage.path + '/editor/' + article_id
        to_article_path = self.article_storage.path + '/in_editing/editor_result'

        copy_tree(from_article_path, to_article_path)
        return True


def main():
    import socketserver
    import json
    import argparse
    from storage.file_article_storage import FileArticleStorage

    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=9998, type=int)
    parser.add_argument('--max-request-length', default=4024)
    parser.add_argument('--storage-path')

    args = parser.parse_args()

    storage = FileArticleStorage(args.storage_path)
    editor = Editor(storage)

    class TCPHandler(socketserver.BaseRequestHandler):
        def handle(self):
            self.data = self.request.recv(args.max_request_length).strip()
            print('client: {}'.format(self.client_address[0]), 'request: {}', self.data)
            request = json.loads(self.data)

            response = '{error_message:"unsupported article id"}'
            if 'article_id' in request and validate_id(request['article_id']):
                response = '{error_message:"unsupported request type"}'
                if request['type'] == 'create_article':
                    response = '{error_message:"error while creating article"}'
                    if editor.create_article_by_id(request['article_id']):
                        response = '{result:"ok"}'

                elif request['type'] == 'update_meta':
                    input_meta = request['new_meta']
                    new_meta = {
                        'type': 'article',
                        'header': input_meta['header'],
                        'date': input_meta['date'],
                        'authors': input_meta['authors'],
                        'id': request['article_id']
                    }
                    response = '{error_message:"error while updating article meta"}'
                    if editor.update_article_meta(request['article_id'], new_meta):
                        response = '{result:"ok"}'

                elif request['type'] == 'update_sections':
                    response = '{error_message:"error while updating article sections"}'
                    if editor.update_article_sections(request['article_id'], request['new_sections']):
                        response = '{result:"ok"}'

                elif request['type'] == 'compile':
                    response = '{error_message:"error while compilation"}'
                    if editor.compile(request['article_id']):
                        response = '{result:"ok"}'

                elif request['type'] == 'get':
                    response = json.dumps({"result":editor.get(request['article_id'])})


                elif request['type'] == 'save':
                    response = '{error_message:"error while compilation"}'
                    if editor.save(request['article_id']):
                        response = '{result:"ok"}'



            print("response length:", len(response))
            self.request.sendall(str.encode(response))

    with socketserver.TCPServer((args.host, args.port), TCPHandler) as server:
        print('start server on', args.host, args.port)
        server.serve_forever()

if __name__ == '__main__':
    main()
