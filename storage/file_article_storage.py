import json
import os

from entities.article import Article

def discover_meta_tree(path):
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
            sections = json.loads(open(self.path + '/' + relative_path + '/sections.json').read())

            """
            content_html = open(self.path + '/' + relative_path + '/content.html').read()
            js = open(self.path + '/' + relative_path + '/script.js').read()
            css = open(self.path + '/' + relative_path + '/style.css').read()
            preview_html = open(self.path + '/' + relative_path + '/preview.html').read()
            """

            content_html = self.path + '/' + relative_path + '/content.html'
            js = self.path + '/' + relative_path + '/script.js'
            css = self.path + '/' + relative_path + '/style.css'
            preview_html = self.path + '/' + relative_path + '/preview.html'

            self.articles[relative_path] = Article(
                    sections=sections,
                    content_html=content_html,
                    js=js,
                    css=css,
                    preview_html=preview_html,
                    meta=self.meta_by_path(path))
        return self.articles[relative_path]

    def create_article(self, path):
        article_absolute_path = self.path + '/' + '/'.join(path)
        if os.path.exists(article_absolute_path):
            print('[error] article already exists:', '/'.join(path))
            return False

        os.makedirs(article_absolute_path)

        open(article_absolute_path + '/meta.json', 'w').write('{"type": "article"}')
        open(article_absolute_path + '/sections.json', 'w').write('[{"type": "markdown", "content":"NEW ARTICLE"}]')

        return True


    def update_sections(self, path, new_sections):
        article_absolute_path = self.path + '/' + '/'.join(path)
        meta_absolute_path = article_absolute_path + '/sections.json'
        if not os.path.exists(article_absolute_path):
            print("[error] no article for path:", '/'.join(path))
            return False

        with open(meta_absolute_path, 'w') as meta_file:
            meta_file.write(json.dumps(new_sections, indent=2));

        return True


    def update_meta(self, path, new_meta):
        article_absolute_path = self.path + '/' + '/'.join(path)
        meta_absolute_path = article_absolute_path + '/meta.json'
        if not os.path.exists(article_absolute_path):
            print("[error] no article for path:", '/'.join(path))
            return False

        with open(meta_absolute_path, 'w') as meta_file:
            meta_file.write(json.dumps(new_meta, indent=2));

        return True

