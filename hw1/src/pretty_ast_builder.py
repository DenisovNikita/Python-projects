import pygraphviz as pgv
import ast
from ast_builder_tools import build_ast

DEBUG = True

graph = pgv.AGraph(directed=True)


def get_label(ast_object, counter):
    fields = [x for x in ast.iter_fields(ast_object)]
    label = "Node #" + str(counter) + ": " + fields[0][0]
    if fields[0][0] != 'body':
        label += ' - ' + ast.unparse(ast_object)
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
    graph.add_node(label, color=color_type.get(fields[0][0], 'pink'))
    return label, counter + 1


def add_edge(a, b):
    graph.add_edge(a, b)


with open('simple.py' if DEBUG else 'fibonacci.py', 'r') as f:
    code = f.read()

build_ast(code, add_edge, get_label)

graph.layout(prog="dot")
graph.draw("../artifacts/Hard/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
