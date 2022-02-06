import networkx as nx
import ast
import matplotlib.pyplot as plt
from ast_builder_tools import build_ast

DEBUG = True

G = nx.DiGraph()


def get_label(ast_object, counter):
    fields = [x for x in ast.iter_fields(ast_object)]
    label = fields[0][0]
    if fields[0][0] != 'body':
        label += ': ' + ast.unparse(ast_object)
    label += '_' + str(counter)
    return label, counter + 1


def add_edge(a, b):
    G.add_edge(a, b)


with open('simple.py' if DEBUG else 'fibonacci.py', 'r') as f:
    code = f.read()

build_ast(code, add_edge, get_label)

nx.draw(G, with_labels=True)
plt.savefig("../artifacts/Medium/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
