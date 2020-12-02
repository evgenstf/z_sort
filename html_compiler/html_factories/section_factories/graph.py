
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
        self.show_labels = data['content']['labels']

    def add_data_to_graph(self, graph):
        for node in range(self.nodes_count):
            graph.add_node(node)
        for edge in self.edges:
            graph.add_edge(*edge)

    def initialize_graph(self):
        graph = nx.Graph()
        self.add_data_to_graph(graph)
        return graph

    def node_size(self):
        if 16000 / self.nodes_count > 2000:
            return 2000
        return 16000 / self.nodes_count

    def draw(self, path):
        G = self.initialize_graph()
        plt.figure(figsize=(10,10))
        if self.graph_type == 'dot':
            pos = graphviz_layout(G, prog="dot")
        elif self.graph_type == 'twopi':
            pos = graphviz_layout(G, prog="twopi")
        elif self.graph_type == 'circle':
            pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=self.node_size(), node_color='#BF00B0')
        nx.draw_networkx_edges(G, pos, edge_color='black', width=4)
        if self.show_labels == 'True':
            nx.draw_networkx_labels(G, pos, font_size=18)
        plt.savefig(path)


class GraphSectionFactory:
    @staticmethod
    def build_html(section, article_relative_path, static_resources_path):
        article_static_resources_path = static_resources_path + '/articles/' + article_relative_path
        if not os.path.exists(article_static_resources_path):
            os.makedirs(article_static_resources_path)

        path = article_static_resources_path + '/' + "graph_1.svg"
        graph = DrawGraph(section)
        graph.draw(path)

        return "<div> {% static " + path + " %} </div>"
