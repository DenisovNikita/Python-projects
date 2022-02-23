import numpy as np
from test_matrix import test


class Matrix(np.lib.mixins.NDArrayOperatorsMixin):
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
