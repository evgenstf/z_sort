import sys
sys.path.append(".")

import json

def get_meta_by_path(path):
    return json.loads(open('/'.join(path) + '/meta.json').read())

def compile_article(path):
    from html_factories.article import ArticleHtmlFactory
    from html_factories.article_preview import ArticlePreviewHtmlFactory

    joined_path = '/'.join(path)
    with open(joined_path + '/content.html', 'w') as content_file:
        content_file.write(
                ArticleHtmlFactory.create_from_article(
                    get_meta_by_path(path), path, get_meta_by_path(path[:-1])))

    with open(joined_path + '/preview.html', 'w') as preview_file:
        preview_file.write(
                ArticlePreviewHtmlFactory.create_from_article(
                    get_meta_by_path(path), path, get_meta_by_path(path[:-1])))

    with open(joined_path + '/script.js', 'w') as script_file:
        script_file.write('{% static js/article.js %}')

    with open(joined_path + '/style.css', 'w') as style_file:
        style_file.write('{% static css/article.css %}')

def compile_item(path):
    print(' ', '/'.join(path))

    meta = get_meta_by_path(path)

    if meta['type'] == 'article':
        return compile_article(path)
    elif 'items' in meta:
        for item in meta['items']:
            compile_item(path + [item])

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('start compile:')
    compile_item(args.path.split('/'))

if __name__ == '__main__':
    main()
