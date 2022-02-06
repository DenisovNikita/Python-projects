import pygraphviz as pgv
import ast

DEBUG = True

with open('simple.py' if DEBUG else 'fibonacci.py', 'r') as f:
    code = f.read()

G = pgv.AGraph(directed=True)


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
    G.add_node(label, color=color_type.get(fields[0][0], 'pink'))
    return label, counter + 1


def dfs(ast_object, tab, counter):
    A, counter = get_label(ast_object, counter)
    for child in ast.iter_child_nodes(ast_object):
        if len([x for x in ast.iter_fields(child)]) > 0:
            B, counter = get_label(child, counter)
            G.add_edge(A, B)
            counter = dfs(child, tab + '\t', counter - 1)
    return counter


ast_object = ast.parse(code)

dfs(ast_object, '', 0)

G.layout(prog="dot")

G.draw("../artifacts/Hard/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
