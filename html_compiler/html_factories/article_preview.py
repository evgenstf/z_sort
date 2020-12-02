from markdown import markdown
from html_factories.article import calculate_reading_time

import json

class ArticlePreviewHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def build_html(*, meta, absolute_path, relative_path, parent_meta):
        sections = json.loads(open('/'.join(absolute_path) + '/sections.json').read())

        article_preview_html_template = open('static/html/article_preview.html', 'r').read()

        article_preview_html_template = article_preview_html_template.replace('&article_header&', '<br>'.join(meta['header']))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_color&', parent_meta['color'])
        article_preview_html_template = article_preview_html_template.replace('&article_link&', '/'+'/'.join(relative_path))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_link&', '/'+'/'.join(relative_path[:-1]))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_header&', ' '.join(parent_meta['header']))
        article_preview_html_template = article_preview_html_template.replace('&article_reading_time&', calculate_reading_time(sections))
        article_preview_html_template = article_preview_html_template.replace('&article_body&', markdown(sections[0]['content']))
        article_preview_html_template = article_preview_html_template.replace('&article_authors&', '<br>'.join(meta['authors']))
        article_preview_html_template = article_preview_html_template.replace('&article_date&', meta['date'])

        return article_preview_html_template
