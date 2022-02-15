import networkx as nx
import matplotlib.pyplot as plt
from ast_builder_tools import build_ast

DEBUG = False

graph = nx.DiGraph()


def add_node(label, _):
    graph.add_node(label)
    

def add_edge(a, b):
    graph.add_edge(a, b)


filename = 'simple.py' if DEBUG else 'fibonacci.py'

build_ast(filename, add_node, add_edge)

nx.draw(graph, with_labels=True)
plt.savefig("../../artifacts/Medium/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
