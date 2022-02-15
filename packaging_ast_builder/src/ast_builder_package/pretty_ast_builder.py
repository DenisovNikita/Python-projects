import pygraphviz as pgv
from ast_builder_tools import build_ast

DEBUG = False

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


filename = 'simple.py' if DEBUG else 'fibonacci.py'

build_ast(filename, add_node, add_edge)

graph.layout(prog="dot")
graph.draw("../artifacts/Hard/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
