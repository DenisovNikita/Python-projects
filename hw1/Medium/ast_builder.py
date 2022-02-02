import networkx as nx
import ast
import matplotlib.pyplot as plt

DEBUG = False

with open('simple.py' if DEBUG else '../Easy/fibonacci.py', 'r') as f:
    code = f.read()

with open('../artifacts/Medium/' + ('simple_ast.out' if DEBUG else 'fibonacci_ast.out'), 'w') as f:
    G = nx.DiGraph()


    def get_label(ast_object, counter):
        fields = [x for x in ast.iter_fields(ast_object)]
        label = fields[0][0]
        if fields[0][0] != 'body':
            label += ': ' + ast.unparse(ast_object)
        label += '_' + str(counter)
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
                dfs(child, tab + '\t', counter - 1)


    ast_object = ast.parse(code)

    counter = 0
    dfs(ast_object, '', counter)

    nx.draw(G, with_labels=True)
    plt.savefig("../artifacts/Medium/" + ("simple_ast.png" if DEBUG else "fibonacci_ast.png"))
