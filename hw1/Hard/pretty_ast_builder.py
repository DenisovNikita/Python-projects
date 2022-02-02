import pygraphviz as pgv
import ast

DEBUG = False

with open('../Medium/simple.py' if DEBUG else '../Easy/fibonacci.py', 'r') as f:
    code = f.read()

with open('../artifacts/Hard/' + ('simple_ast.out' if DEBUG else 'fibonacci_ast.out'), 'w') as f:
    G = pgv.AGraph(directed=True)

    def get_label(ast_object, counter):
        fields = [x for x in ast.iter_fields(ast_object)]
        label = "Node #" + str(counter) + ": " + fields[0][0]
        if fields[0][0] != 'body':
            label += ' - ' + ast.unparse(ast_object)
        # label += '|' + str(counter)
        color_type = {
            'body': 'black',
            'targets': 'blue',
            'value': 'red',
            'id': 'green',
            'func': 'purple'
        }
        G.add_node(label, color=color_type.get(fields[0][0], 'pink'))
        return label, counter + 1


    def dfs(ast_object, tab, counter):
        f.write(tab)
        f.write(str([x for x in ast.iter_fields(ast_object)]))
        f.write('\n')
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
