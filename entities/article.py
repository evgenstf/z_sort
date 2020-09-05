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
