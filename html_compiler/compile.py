import sys
sys.path.append(".")

import json

def get_meta_by_path(path):
    return json.loads(open('/'.join(path) + '/meta.json').read())

def compile_article(absolute_path, relative_path, article_static_path):
    from html_compiler.html_factories.article import ArticleHtmlFactory
    from html_compiler.html_factories.article_preview import ArticlePreviewHtmlFactory

    joined_absolute_path = '/'.join(absolute_path)
    with open(joined_absolute_path + '/content.html', 'w') as content_file:
        content_file.write(
                ArticleHtmlFactory.build_html(
                    meta=get_meta_by_path(absolute_path),
                    absolute_path=absolute_path,
                    relative_path=relative_path,
                    parent_meta=get_meta_by_path(absolute_path[:-1]),
                    static_storage_absolute_path=article_static_path))

    with open(joined_absolute_path + '/preview.html', 'w') as preview_file:
        preview_file.write(
                ArticlePreviewHtmlFactory.build_html(
                    meta=get_meta_by_path(absolute_path),
                    absolute_path=absolute_path,
                    relative_path=relative_path,
                    parent_meta=get_meta_by_path(absolute_path[:-1])))

    with open(joined_absolute_path + '/script.js', 'w') as script_file:
        script_file.write("""
            <script type="text/javascript"
                src="http://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
            </script>
            <script type="text/javascript" src="{% static 'js/article.js' %}"></script>""")

    with open(joined_absolute_path + '/style.css', 'w') as style_file:
        style_file.write("<link rel=\"stylesheet\" href=\"{% static 'css/article.css' %}\">")


def compile_item(absolute_path, relative_path, article_static_path):
    print(' ', '/'.join(absolute_path))

    meta = get_meta_by_path(absolute_path)
    if meta['type'] == 'article':
        return compile_article(absolute_path, relative_path, article_static_path)
    elif 'items' in meta:
        for item in meta['items']:
            compile_item(absolute_path + [item], relative_path + [item], article_static_path)

def main():
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('start compile:')

    absolute_path = os.path.abspath(args.path)
    absolute_article_static_path = absolute_path + '/static'
    compile_item(absolute_path.split('/'), [], absolute_article_static_path)

if __name__ == '__main__':
    main()
