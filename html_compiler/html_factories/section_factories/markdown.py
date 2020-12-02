from markdown import markdown
from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension

import xml.etree.ElementTree as etree

class FootnoteInlineProcessor(InlineProcessor):
    footnote_id = 0
    def __init__(self, pattern, md):
        super(FootnoteInlineProcessor, self).__init__(pattern, md)

    def handleMatch(self, m, data):
        el = etree.Element('span class="footnote_link" id="{id}" onclick=\'showFootnote("{id}")\' footnote-title="{title}" footnote-text="{text}"'.format(
            id=FootnoteInlineProcessor.footnote_id, title=m.group(2), text=markdown(m.group(3))))
        el.text = f'{m.group(1)}'
        FootnoteInlineProcessor.footnote_id += 1
        return el, m.start(0), m.end(0)

class FootnoteExtension(Extension):
    def extendMarkdown(self, md):
        FOOTNOTE_PATTERN = r'<!(.*?)!>\((.*?)\){(.*?)}'
        md.inlinePatterns.register(FootnoteInlineProcessor(FOOTNOTE_PATTERN, md), 'footnote', 175)

class MarkdownSectionFactory:
    @staticmethod
    def build_html(section):
        return markdown(section['content'], extensions=['fenced_code', FootnoteExtension()])
