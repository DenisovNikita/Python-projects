__all__ = [
    'build_ast',
]

import ast


def build_ast(code, add_edge, get_label):
    def dfs(ast_object, tab, counter):
        a, counter = get_label(ast_object, counter)
        for child in ast.iter_child_nodes(ast_object):
            if len([x for x in ast.iter_fields(child)]) > 0:
                b, counter = get_label(child, counter)
                add_edge(a, b)
                counter = dfs(child, tab + '\t', counter - 1)
        return counter

    dfs(ast.parse(code), '', 0)
