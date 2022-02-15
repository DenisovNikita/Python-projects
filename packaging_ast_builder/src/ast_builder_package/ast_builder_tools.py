__all__ = [
    "build_ast",
]

import ast


def build_ast(code, add_node, add_edge):
    def get_label(ast_object, counter):
        token_type = list(ast.iter_fields(ast_object))[0][0]
        label = "Node #" + str(counter) + "\n" + token_type
        if token_type != "body":
            label += ": " + ast.unparse(ast_object)
        add_node(label, token_type)
        return label, counter + 1

    def dfs(ast_object, counter):
        a, counter = get_label(ast_object, counter)
        for child in ast.iter_child_nodes(ast_object):
            if len(list(ast.iter_fields(child))) > 0:
                b, counter = get_label(child, counter)
                add_edge(a, b)
                counter = dfs(child, counter - 1)
        return counter

    dfs(ast.parse(code), 0)
