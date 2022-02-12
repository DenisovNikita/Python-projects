def add_packages(s):
    return s + '\\usepackage[utf8]{inputenc}\n'


def add_title(s):
    return s + '\\title{Test}\n'


def add_author(s):
    return s + '\\author{Niktita Denisov}\n'


def init():
    s = '\\documentclass{article}\n'
    return add_author(add_title(add_packages(s)))


def write_table(table):
    n = len(table)
    s = ''
    if n == 0:
        return s
    m = len(table[0])
    colons = '|' + 'c|' * m
    s = '\\begin{tabular}{' + colons + '}\n'
    s = s + '\\hline\n'
    for i in range(n):
        row = ''
        for j in range(m):
            row = row + table[i][j]
            if j + 1 < m:
                row = row + ' & '
            else:
                row = row + '\\\\'
        s = s + row + '\n'
        s = s + '\\hline\n'
    s = s + '\\end{tabular}\n'
    return s


def write_document(s, table):
    t = s + '\\begin{document}\n'
    t = t + '\\maketitle\n'
    t = t + write_table(table)
    t = t + '\\end{document}\n'
    return t


input_table = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

latex = init()
latex = write_document(latex, input_table)

with open('../artefacts/easy/table.tex', 'w') as f:
    f.write(latex)
