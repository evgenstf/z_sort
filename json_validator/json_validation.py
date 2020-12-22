import json
import jsonschema
import sys


class JsonValidator:
    @staticmethod
    def json_string_to_dict(json_string):
        if sys.getsizeof(json_string) > 500 * 1024:
            raise KeyboardInterrupt("The size of the article is too large")
        try:
            json_dict = json.loads(json_string)
        except:
            raise KeyboardInterrupt("Invalid json string")

        return json_dict

    def validate_sections(json_string):
        json_dict = JsonValidator.json_string_to_dict(json_string)
        for section in json_dict:
            with open("schemas/sections/section_schema.json", "r") as graph_schema:
                jsonschema.validate(section, json.load(graph_schema))

            if section['type'] == 'graph':
                with open("schemas/sections/graph_schema.json", "r") as graph_schema:
                    jsonschema.validate(section['content'], json.load(graph_schema))

            elif section['type'] == 'chart':
                if 'type' in section['content'] and section['content']['type'] == 'pie':
                    with open("schemas/sections/pie_schema.json", "r") as chart_schema:
                        jsonschema.validate(section['content'], json.load(chart_schema))
                elif 'type' in section['content'] and section['content']['type'] in ['scatter', 'bar', 'line']:
                    with open("schemas/sections/chart_schema.json", "r") as chart_schema:
                        jsonschema.validate(section['content'], json.load(chart_schema))
                else:
                    raise KeyboardInterrupt("Unrecognize chart type")

            elif section['type'] == 'steps':
                JsonValidator.validate_sections(str(section['content']).replace("\'", "\""))

    def validate_meta(json_string):
        meta_file = JsonValidator.json_string_to_dict(json_string)
        with open("schemas/meta_schema.json", "r") as chart_schema:
            jsonschema.validate(meta_file, json.load(chart_schema))
        if len(meta_file['header']) > 100:
            raise KeyboardInterrupt("The size of the article name is too large")

def main():
    import argparse
    import os

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)

    args = parser.parse_args()

    print('Start validate:')
    absolute_path = os.path.abspath(args.path)

    try:
        input_file = open(absolute_path, 'r')
    except FileNotFoundError:
        return print("File not found")

    json_string = input_file.read()

    if 'meta.json' in absolute_path:
        JsonValidator.validate_meta(json_string)
    elif 'sections.json' in absolute_path:
        JsonValidator.validate_sections(json_string)
    else:
        return print("Incorrect path")

    input_file.close()

    print('Successful validation!')


if __name__ == '__main__':
    main()
