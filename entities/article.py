class Article:
    def __init__(self):
        self.sections = None
        self.header = None
        self.date = None
        self.authors = None
        self.id = None
        self.url = None
        self.reading_time = None

        self.content_html = None
        self.js = None
        self.css = None
        self.preview_html = None

    def __init__(self, *, sections, content_html, js, css, preview_html, meta):
        self.sections = sections
        self.header = meta['header']
        self.date = meta['date']
        self.authors = meta['authors']
        self.id = meta['id']
        self.url = meta['url']

        self.reading_time = None
        if 'reading_time' in meta:
            self.reading_time = meta['reading_time']

        self.content_html = content_html
        self.js = js
        self.css = css
        self.preview_html = preview_html

    def to_full_dict(self):
        return {
                # 'sections': self.sections,
                'header': self.header,
                'date': self.date,
                'authors': self.authors,
                'id': self.id,
                'reading_time': self.reading_time,

                'content_html': self.content_html,
                'js': self.js,
                'css': self.css,
                'preview_html': self.preview_html
        }

    def to_preview_dict(self):
        return {
                'header': self.header,
                'date': self.date,
                'authors': self.authors,
                'id': self.id,
                'reading_time': self.reading_time,

                'css': self.css,
                'preview_html': self.preview_html
        }
