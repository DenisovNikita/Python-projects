__all__ = [
    "draw_pretty_ast",
]

import pygraphviz as pgv
from ast_builder_package.ast_builder_tools import build_ast
import inspect
from ast_builder_package import fibonacci


def draw_pretty_ast(path):
    graph = pgv.AGraph(directed=True)

    def add_node(label, token_type):
        color_type = {
            'body': 'black',
            'target': 'blue',
            'targets': 'blue',
            'left': 'blue',
            'value': 'red',
            'id': 'green',
            'func': 'purple',
            'test': 'orange',
        }
        graph.add_node(label, color=color_type.get(token_type, 'pink'))

    def add_edge(a, b):
        graph.add_edge(a, b)

    code = inspect.getsource(fibonacci)

    build_ast(code, add_node, add_edge)

    graph.layout(prog="dot")
    graph.draw(path)
