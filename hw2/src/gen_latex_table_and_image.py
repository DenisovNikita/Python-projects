def init(graphics_paths):
    return LatexMaker('\\documentclass{article}\n'). \
        add_packages(graphics_paths). \
        add_title(). \
        add_author()


def make_latex(graphics_paths, table, image_path):
    return init(graphics_paths).write_document(table, image_path)


class LatexMaker:

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def add_packages(self, graphics_paths):
        paths = ''.join([' {' + name + '} ' for name in graphics_paths])
        return LatexMaker(self.s +
                          '\\usepackage[utf8]{inputenc}\n' +
                          '\\usepackage{graphicx}\n' +
                          '\\usepackage[margin=0.5in]{geometry}\n' +
                          '\\graphicspath{' + paths + '}\n')

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

    def write_center_table(self, table):
        return self.add_begin('center'). \
            write_table(table). \
            add_end('center')

    def write_image(self, image_path):
        return LatexMaker(self.s +
                          '\\includegraphics[scale=0.15]{' + image_path + '}\n')

    def write_center_image(self, image_path):
        return self.add_begin('center'). \
            write_image(image_path). \
            add_end('center')

    def add_begin(self, name):
        return LatexMaker(self.s + '\\begin{' + name + '}\n')

    def add_end(self, name):
        return LatexMaker(self.s + '\\end{' + name + '}\n')

    def make_title(self):
        return LatexMaker(self.s + '\\maketitle\n')

    def write_document(self, table, image_path):
        return self.add_begin('document'). \
            make_title(). \
            write_center_table(table). \
            write_center_image(image_path). \
            add_end('document')


input_table = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]
paths_to_directory_with_image = ['../../resources/']
path_to_image = 'fibonacci_ast'

latex = make_latex(paths_to_directory_with_image, input_table, path_to_image)

with open('../artefacts/medium/table_and_image.tex', 'w') as f:
    f.write(str(latex))
