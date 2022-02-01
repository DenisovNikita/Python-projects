import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import ast
import matplotlib.pyplot as plt

# G = nx.Graph()
# G.add_edge('A', 'B', weight=4)
# G.add_edge('B', 'D', weight=2)
# G.add_edge('A', 'C', weight=3)
# G.add_edge('C', 'D', weight=4)
# path = nx.shortest_path(G, 'A', 'D', weight='weight')


# G = nx.petersen_graph()
# pos = nx.spring_layout(G)
# nx.draw_networkx(G, pos)
# labels = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# subax1 = plt.subplot(121)
# nx.draw(G, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()

# print(path)

# exit(0)

with open('simple.py', 'r') as f:
    code = f.read()

with open('ast.out', 'w') as f:
    G = nx.DiGraph()


    def label(ast_object, counter):
        return (ast_object._fields[0] + '_' + str(counter), counter + 1)
        # return 'kek'
        # fileds = [x for x in ast.iter_fields(ast_object)]
        # print(fileds)
        # print(fileds[0])
        # exit(0)
        # counter += 1
        # return fileds[0][0] + '_' + str(counter)


    def dfs(ast_object, tab, counter):
        print(tab, ast_object._fields)
        # print(tab, [x for x in ast.iter_fields(ast_object)], sep='')
        # print(tab, , sep='')
        f.write('\n' + tab)
        f.write(str(ast_object))
        A, counter = label(ast_object, counter)
        for child in ast.iter_child_nodes(ast_object):
            if len([x for x in ast.iter_fields(child)]) > 0:
                B, counter = label(child, counter)
                G.add_edge(A, B)
                dfs(child, tab + '\t', counter - 1)


    ast_object = ast.parse(code)
    f.write(ast.dump(ast_object, indent=4))
    # exit(0)

    ast_unparse = ast.unparse(ast_object)
    print(ast_unparse)
    # exit(0)

    path = ast.walk(ast_object)

    # bfs_result = [ast.dump(x, indent=4) for x in path]
    counterr = 0
    dfs(ast_object, '', counterr)
    # f.write(l + '\n\n')

    nx.draw(G, with_labels=True)
    plt.show()

    # write_dot(G, 'test.dot')
    #
    # # same layout using matplotlib with no labels
    # plt.title('draw_networkx')
    # pos = graphviz_layout(G, prog='dot')
    # nx.draw(G, pos, with_labels=True, arrows=True)
    # plt.savefig('nx_test.png')