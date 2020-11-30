import sys
sys.path.append(".")

import json

def get_meta_by_path(path):
    return json.loads(open('/'.join(path) + '/meta.json').read())

def compile_article(meta, path):
    from html_factories.article import ArticleHtmlFactory
    return ArticleHtmlFactory.create_from_article(get_meta_by_path(path), path, get_meta_by_path(path[:-1]))

def compile_item(meta, path):
    if meta['type'] == 'article':
        return compile_article(meta, path)

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    parser.add_argument('-r', '--recursive', action='store_true')

    args = parser.parse_args()

    print('path:', args.path, 'recursive:', args.recursive)

    splitted_path = args.path.split('/')
    meta = get_meta_by_path(splitted_path)
    print("meta:", json.dumps(meta, indent=2, sort_keys=True))

    html_result = compile_item(meta, splitted_path)

    with open(args.path + '/content.html', 'w') as html_file:
        html_file.write(html_result)

if __name__ == '__main__':
    main()
