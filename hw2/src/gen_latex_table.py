def init():
    return LatexMaker('\\documentclass{article}\n'). \
        add_packages(). \
        add_title(). \
        add_author()


def make_latex(table):
    return init().write_document(table)


class LatexMaker:

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def add_packages(self):
        return LatexMaker(self.s + '\\usepackage[utf8]{inputenc}\n')

    def add_title(self):
        return LatexMaker(self.s + '\\title{Test}\n')

    def add_author(self):
        return LatexMaker(self.s + '\\author{Niktita Denisov}\n')

    def write_table(self, table):
        n = len(table)
        s = ''
        if n > 0:
            m = len(table[0])
            colons = '|' + 'c|' * m
            s = '\\begin{tabular}{' + colons + '}\n'
            s += '\\hline\n'
            for i in range(n):
                row = ''
                for j in range(m):
                    row = row + table[i][j]
                    if j + 1 < m:
                        row += ' & '
                    else:
                        row += '\\\\'
                s += row + '\n'
                s += '\\hline\n'
            s += '\\end{tabular}\n'
        return LatexMaker(self.s + s)

    def add_begin(self, name):
        return LatexMaker(self.s + '\\begin{' + name + '}\n')

    def add_end(self, name):
        return LatexMaker(self.s + '\\end{' + name + '}\n')

    def make_title(self):
        return LatexMaker(self.s + '\\maketitle\n')

    def write_document(self, table):
        return self.add_begin('document'). \
            make_title(). \
            write_table(table). \
            add_end('document')


input_table = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

latex = make_latex(input_table)

with open('../artefacts/easy/table.tex', 'w') as f:
    f.write(str(latex))
