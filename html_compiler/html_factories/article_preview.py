from markdown import markdown

import json

class ArticlePreviewHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def create_from_article(meta, path, parent_meta):
        sections = json.loads(open('/'.join(path) + '/sections.json').read())

        article_preview_html_template = open('static/html/article_preview.html', 'r').read()

        article_preview_html_template = article_preview_html_template.replace('&article_header&', '<br>'.join(meta['header']))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_color&', parent_meta['color'])
        article_preview_html_template = article_preview_html_template.replace('&article_link&', '/'+'/'.join(path) + '/' + meta['id'])
        article_preview_html_template = article_preview_html_template.replace('&article_parent_link&', '/'+'/'.join(path))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_header&', ' '.join(parent_meta['header']))
        article_preview_html_template = article_preview_html_template.replace('&article_reading_time&', meta['reading_time'])
        article_preview_html_template = article_preview_html_template.replace('&article_body&', markdown(sections[0]['content']))
        article_preview_html_template = article_preview_html_template.replace('&article_authors&', '<br>'.join(meta['authors']))
        article_preview_html_template = article_preview_html_template.replace('&article_date&', meta['date'])

        return article_preview_html_template
