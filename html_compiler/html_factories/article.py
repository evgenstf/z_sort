import json
import os

from html_compiler.html_factories.section_factories.markdown import MarkdownSectionFactory
from html_compiler.html_factories.section_factories.graph import GraphSectionFactory
from html_compiler.html_factories.section_factories.chart import ChartSectionFactory
from html_compiler.html_factories.section_factories.steps import StepSectionFactory

def calculate_reading_time(sections):
    total_length = 0
    for section in sections:
        total_length += len(json.dumps(section))

    return str(total_length // 2000) + " min"

class ArticleHtmlFactory:
    def __init__(self):
        self.template = None

    @staticmethod
    def compile_section(sections, absolute_path, relative_path, static_storage_absolute_path):
        section_html = ''
        if type(static_storage_absolute_path) == list:
            static_storage_absolute_path = '/'.join(static_storage_absolute_path)
        for section in sections:
            if section['type'] == 'markdown' or section['type'] == 'tldr':
                section_html += MarkdownSectionFactory.build_html(section)
            elif section['type'] == 'graph':
                section_html += GraphSectionFactory.build_html(
                        section,
                        '/'.join(relative_path),
                        static_storage_absolute_path
                )
            elif section['type'] == 'chart':
                section_html += ChartSectionFactory.build_html(
                        section,
                        '/'.join(relative_path),
                        static_storage_absolute_path)
            elif section['type'] == 'steps':
                section_html += StepSectionFactory.build_html(section['content'], absolute_path, relative_path, static_storage_absolute_path, ArticleHtmlFactory.compile_section)
            else:
                print("[warning] unknown section type:", section['type'])
        return section_html


    @staticmethod
    def build_html(*, meta, absolute_path, relative_path, parent_meta, static_storage_absolute_path):
        sections = json.loads(open('/'.join(absolute_path) + '/sections.json').read())

        article_header_html = '<br>'.join(meta['header'])

        article_body_html = ArticleHtmlFactory.compile_section(sections, absolute_path, relative_path, static_storage_absolute_path)

        article_html = open(os.path.dirname(os.path.realpath(__file__)) + '/../templates/html/article.html', 'r').read()
        article_html = article_html.replace('&article_header&', article_header_html)
        article_html = article_html.replace('&article_parent_link&', '/' + '/'.join(relative_path[:-1]))
        article_html = article_html.replace('&article_parent_header&', ' '.join(parent_meta['header']))
        article_html = article_html.replace('&article_parent_color&', parent_meta['color'] if 'color' in parent_meta else 'var(--gray-color)')
        article_html = article_html.replace('&article_reading_time&', calculate_reading_time(sections))
        article_html = article_html.replace('&article_body&', article_body_html)
        article_html = article_html.replace('&article_authors&', '<br>'.join(meta['authors']))
        article_html = article_html.replace('&article_date&', meta['date'])

        return article_html
