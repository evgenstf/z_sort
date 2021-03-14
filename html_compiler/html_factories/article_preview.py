from markdown import markdown
from html_compiler.html_factories.article import calculate_reading_time

import json
import os

class ArticlePreviewHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def build_html(article_json):
        print('start build preview')
        sections = article_json['sections']

        article_preview_html_template = open(os.path.dirname(os.path.realpath(__file__)) + '/../templates/html/article_preview.html', 'r').read()

        article_preview_html_template = article_preview_html_template.replace('&article_header&', '<br>'.join(article_json['header']))
        article_preview_html_template = article_preview_html_template.replace('&article_parent_color&', 'var(--gray-color)')
        article_preview_html_template = article_preview_html_template.replace('&article_link&', '/article/' + article_json['url'])
        article_preview_html_template = article_preview_html_template.replace('&article_parent_link&', '/category/'+article_json['category'])
        article_preview_html_template = article_preview_html_template.replace('&article_parent_header&', article_json['category'])
        article_preview_html_template = article_preview_html_template.replace('&article_reading_time&', calculate_reading_time(sections))
        article_preview_html_template = article_preview_html_template.replace('&article_body&', markdown(sections[0]['content']))
        article_preview_html_template = article_preview_html_template.replace('&article_authors&', '<br>'.join(article_json['authors']))
        article_preview_html_template = article_preview_html_template.replace('&article_date&', article_json['date'])

        print('preview builded')

        return article_preview_html_template
