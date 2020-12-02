import os

class GraphSectionFactory:
    @staticmethod
    def build_html(section, article_relative_path, static_resources_path):
        article_static_resources_path = static_resources_path + '/articles/' + article_relative_path
        if not os.path.exists(article_static_resources_path):
            os.makedirs(article_static_resources_path)

        with open(article_static_resources_path + '/' + "graph_1.svg", 'w') as graph_svg_file:
            graph_svg_file.write('123')

        return "<div></div>"
