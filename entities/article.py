class Article:
    def __init__(self):
        self.text = None
        self.header = None
        self.date = None
        self.authors = None
        self.id = None

    def __init__(self, text, attributes):
        self.text = text
        self.header = attributes['header']
        self.date = attributes['date']
        self.authors = attributes['authors']
        self.id = attributes['id']

    def to_full_dict(self):
        return {
                'text': self.text,
                'header': self.header,
                'date': self.date,
                'authors': self.authors,
                'id': self.id
        }

    def to_preview_dict(self):
        return {
                'header': self.header,
                'date': self.date,
                'authors': self.authors,
                'id': self.id
        }
