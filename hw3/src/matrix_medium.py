import numpy as np
from test_matrix import test


class FileWriter:
    def write(self, path):
        with open(path, "w") as f:
            f.write(str(self))


class PrettyView:
    def __str__(self):
        return "Matrix:\n" + str(self._matrix)


class Getter:
    def get(self):
        return self._matrix


class Setter:
    def set(self, value):
        self._matrix = value


class Matrix(
    np.lib.mixins.NDArrayOperatorsMixin,
    FileWriter,
    PrettyView,
    Getter,
    Setter
):
    def __init__(self, value):
        self._matrix = value

    @property
    def matrix(self):
        return self._matrix

    def __sub__(self, other):
        return Matrix(np.lib.mixins.NDArrayOperatorsMixin.__sub__(self._matrix, other._matrix))

    def __add__(self, other):
        return Matrix(np.lib.mixins.NDArrayOperatorsMixin.__add__(self._matrix, other._matrix))

    def __mul__(self, other):
        return Matrix(np.lib.mixins.NDArrayOperatorsMixin.__mul__(self._matrix, other._matrix))

    def __matmul__(self, other):
        return Matrix(np.lib.mixins.NDArrayOperatorsMixin.__matmul__(self._matrix, other._matrix))


test(Matrix, "../artefacts/medium")

# mixins tests:
#
# a = Matrix([1, 2])
# a.write("../artefacts/medium/kek.txt")
# print(str(a))
# a.set([3, 4, 5])
# print(a.get())
# print(a)
