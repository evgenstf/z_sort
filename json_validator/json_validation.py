import json
import jsonschema
import os


class JsonValidator:
    def __init__(self, json_path):
        with open(json_path, "r") as input_json:
            self.data = json.load(input_json)
        if isinstance(self.data, dict):
            self.data = [self.data]
        self.file_size = os.stat(json_path).st_size

    def sections_validate(self, sections):
        if self.file_size > 500 * 1024:
            raise KeyboardInterrupt("The size of the article is too large")

        for section in sections:
            if section['type'] == 'graph':
                with open("json_schemas/graph.json", "r") as graph_schema:
                    jsonschema.validate(section['content'], json.load(graph_schema))
            elif section['type'] == 'chart':
                with open("json_schemas/chart.json", "r") as chart_schema:
                    jsonschema.validate(section['content'], json.load(chart_schema))
            elif section['type'] == 'steps':
                self.sections_validate(section['content'])
            elif section['type'] == 'article':
                self.meta_validate()

    def meta_validate(self):
        if len(self.data['header']) > 50:
            raise KeyboardInterrupt("The size of the article header is too large")

    def validate(self):
        self.sections_validate(self.data)

    @staticmethod
    def run(path):
        validator = JsonValidator(path)
        validator.validate()
