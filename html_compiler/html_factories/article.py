import json
import os

from html_compiler.html_factories.section_factories.markdown import MarkdownSectionFactory
from html_compiler.html_factories.section_factories.graph import GraphSectionFactory
from html_compiler.html_factories.section_factories.chart import ChartSectionFactory
from html_compiler.html_factories.section_factories.steps import StepSectionFactory

STATIC_STORAGE_PATH = os.environ.get('ARTICLE_STATIC')

def calculate_reading_time(sections):
    total_length = 0
    for section in sections:
        total_length += len(json.dumps(section))

    return str(total_length // 2000) + " min"

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def compile_sections(article_url, sections):
        section_html = ''

        print("sections:", sections)
        for section in sections:
            print("section:", section)
            if section['type'] == 'markdown' or section['type'] == 'tldr':
                section_html += MarkdownSectionFactory.build_html(section)
            elif section['type'] == 'graph':
                section_html += GraphSectionFactory.build_html(
                        section,
                        article_url,
                        STATIC_STORAGE_PATH)
            elif section['type'] == 'chart':
                section_html += ChartSectionFactory.build_html(
                        section,
                        article_url,
                        STATIC_STORAGE_PATH)
            elif section['type'] == 'steps':
                section_html += StepSectionFactory.build_html(section['content'], article_url, ArticleHtmlFactory.compile_sections)
            else:
                print("[warning] unknown section type:", section['type'])
        return section_html


    @staticmethod
    def build_html(*, article_json):
        sections = article_json['sections']

        article_header_html = '<br>'.join(article_json['header'])

        article_body_html = ArticleHtmlFactory.compile_sections(article_json['url'], sections)

        article_html = open(os.path.dirname(os.path.realpath(__file__)) + '/../templates/html/article.html', 'r').read()
        article_html = article_html.replace('&article_header&', article_header_html)
        article_html = article_html.replace('&article_parent_link&', '/category/' + article_json['category'])
        article_html = article_html.replace('&article_parent_header&', ' '.join(article_json['category']))
        article_html = article_html.replace('&article_parent_color&', 'var(--gray-color)')
        article_html = article_html.replace('&article_reading_time&', calculate_reading_time(sections))
        article_html = article_html.replace('&article_body&', article_body_html)
        article_html = article_html.replace('&article_authors&', '<br>'.join(article_json['authors']))
        article_html = article_html.replace('&article_date&', article_json['date'])

        return article_html
