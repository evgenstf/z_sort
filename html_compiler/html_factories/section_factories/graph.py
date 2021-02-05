
'''
HOW TO CONFIGURATE?

https://stackoverflow.com/questions/40528048/pip-install-pygraphviz-no-package-libcgraph-found

sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config
pip install pygraphviz


TYPES OF GRAPHS:

https://stackoverflow.com/questions/57512155/how-to-draw-a-tree-more-beautifully-in-networkx

- twopi: circle tree
- dot: top-dorn tree
- circle: vertecies in a circle

'''

import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import os

class DrawGraph:
    def __init__(self, data):
        self.edges = data['content']['edges']
        self.node_count = data['content']['node_count']
        self.node_attributes = data['content']['node_attributes']
        self.graph_type = data['content']['type']

        self.show_default_labels = data['content'].get('show_default_labels', False)
        self.node_color = data['content'].get('node_color', '#BF00B0')
        self.edge_color = data['content'].get('edge_color', '#BF00B0')

    def add_data_to_graph(self, graph):
        for id in range(self.node_count):
            graph.add_node(id)
        for edge in self.edges:
            graph.add_edge(edge['from'], edge['to'])

    def initialize_graph(self):
        graph = nx.Graph()
        self.add_data_to_graph(graph)
        return graph

    def calculate_node_diameter(self):
        if 16000 / self.node_count > 2000:
            return 2000
        return 16000 / self.node_count

    def draw(self, path):
        G = self.initialize_graph()
        plt.figure(figsize=(16,9))
        plt.axis('off')
        if self.graph_type == 'dot':
            pos = graphviz_layout(G, prog="dot")
        elif self.graph_type == 'twopi':
            pos = graphviz_layout(G, prog="twopi")
        elif self.graph_type == 'circle':
            pos = nx.circular_layout(G)

        node_labels = {}
        node_colors = {id: self.node_color for id in range(self.node_count)}

        for id in range(self.node_count):
            str_id = str(id)
            if str_id in self.node_attributes:
                if 'label' in self.node_attributes[str_id]:
                    node_labels[id] = self.node_attributes[str_id]['label']
                if 'color' in self.node_attributes[str_id]:
                    node_colors[id] = self.node_attributes[str_id]['color']


        nx.draw_networkx_nodes(G, pos, node_size=self.calculate_node_diameter(),
            node_color=[node_colors[id] for id in range(self.node_count)])
        nx.draw_networkx_edges(G, pos, edge_color=self.edge_color, width=4)

        if self.show_default_labels == True:
            nx.draw_networkx_labels(G, pos, font_size=18,
                    labels={id: node_labels.get(id, id) for id in range(self.node_count)})
        else:
            nx.draw_networkx_labels(G, pos, labels=node_labels)

        plt.savefig(path, transparent=True)
        plt.close()


class GraphSectionFactory:
    graph_id = 0

    @staticmethod
    def build_html(section, article_relative_path, static_resources_path):
        import json
        if type(section['content']) == str:
            section['content'] = json.loads(''.join(str(section['content']).split()))
        article_static_resources_path = static_resources_path + '/articles/' + article_relative_path
        if not os.path.exists(article_static_resources_path):
            os.makedirs(article_static_resources_path)

        graph_absolute_path = article_static_resources_path + '/' + "graph_" + str(GraphSectionFactory.graph_id) + ".svg"
        graph_relative_path = article_relative_path + '/' + "graph_" + str(GraphSectionFactory.graph_id) + ".svg"
        graph = DrawGraph(section)
        graph.draw(graph_absolute_path)
        GraphSectionFactory.graph_id += 1

        return "<img src=\"{% static \"articles/" + graph_relative_path + "\" %}\" />"
