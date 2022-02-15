__all__ = [
    "draw_ast",
]

import networkx as nx
import matplotlib.pyplot as plt
from ast_builder_package.ast_builder_tools import build_ast
import inspect
from ast_builder_package import fibonacci


def draw_ast():
    graph = nx.DiGraph()

    def add_node(label, _):
        graph.add_node(label)

    def add_edge(a, b):
        graph.add_edge(a, b)

    code = inspect.getsource(fibonacci)

    build_ast(code, add_node, add_edge)

    nx.draw(graph, with_labels=True)
    plt.savefig("fibonacci_ast.png")
