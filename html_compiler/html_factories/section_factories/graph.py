
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
        self.nodes_count = data['content']['nodes_count']
        self.edges = data['content']['edges']
        self.graph_type = data['content']['type']
        if 'show_labels' in data['content']:
            self.show_labels = data['content']['show_labels']
        else:
            self.show_labels = False

        if 'node_color' in data['content']:
            self.node_color = data['content']['node_color']
        else:
            self.node_color = '#BF00B0'

        if 'edge_color' in data['content']:
            self.edge_color = data['content']['edge_color']
        else:
            self.edge_color = '#BF00B0'

    def add_data_to_graph(self, graph):
        for node in range(self.nodes_count):
            graph.add_node(node)
        for edge in self.edges:
            graph.add_edge(*edge)

    def initialize_graph(self):
        graph = nx.Graph()
        self.add_data_to_graph(graph)
        return graph

    def calculate_node_diameter(self):
        if 16000 / self.nodes_count > 2000:
            return 2000
        return 16000 / self.nodes_count

    def draw(self, path):
        G = self.initialize_graph()
        plt.figure(figsize=(16,12))
        plt.axis('off')
        if self.graph_type == 'dot':
            pos = graphviz_layout(G, prog="dot")
        elif self.graph_type == 'twopi':
            pos = graphviz_layout(G, prog="twopi")
        elif self.graph_type == 'circle':
            pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=self.calculate_node_diameter(),\
                               node_color=self.node_color)
        nx.draw_networkx_edges(G, pos, edge_color=self.edge_color, width=4)
        if self.show_labels == True:
            nx.draw_networkx_labels(G, pos, font_size=18)
        plt.savefig(path, transparent=True)
        plt.close()


class GraphSectionFactory:
    graph_id = 0

    @staticmethod
    def build_html(section, article_relative_path, static_resources_path):
        article_static_resources_path = static_resources_path + '/articles/' + article_relative_path
        if not os.path.exists(article_static_resources_path):
            os.makedirs(article_static_resources_path)

        graph_absolute_path = article_static_resources_path + '/' + "graph_" + str(GraphSectionFactory.graph_id) + ".svg"
        graph_relative_path = article_relative_path + '/' + "graph_" + str(GraphSectionFactory.graph_id) + ".svg"
        graph = DrawGraph(section)
        graph.draw(graph_absolute_path)
        GraphSectionFactory.graph_id += 1

        return "<img src=\"{% static \"articles/" + graph_relative_path + "\" %}\" />"
