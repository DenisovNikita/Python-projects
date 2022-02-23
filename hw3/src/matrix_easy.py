from test_matrix import test


class Matrix:
    def __init__(self, value):
        self._matrix = value

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

    def getDimensions(self):
        n = len(self._matrix)
        if n == 0:
            return 0, 0
        return n, len(self._matrix[0])

    def getElement(self, i, j):
        return self._matrix[i][j]

    def checkDimensions(self, n, m):
        nn, mm = self.getDimensions()
        if n != nn or m != mm:
            raise Exception("Dimensions do not match!")

    def __add__(self, other):
        n, m = self.getDimensions()
        other.checkDimensions(n, m)
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(self.getElement(i, j) + other.getElement(i, j))
            res.append(row)
        return Matrix(res)

    def __mul__(self, other):
        n, m = self.getDimensions()
        other.checkDimensions(n, m)
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(self.getElement(i, j) * other.getElement(i, j))
            res.append(row)
        return Matrix(res)

    def __matmul__(self, other):
        n, k1 = self.getDimensions()
        k2, m = other.getDimensions()
        if k1 != k2:
            raise Exception("Matrices cannot be multiplied!")
        res = []
        for i in range(n):
            row = [0] * m
            for j in range(m):
                for t in range(k1):
                    row[j] += self.getElement(i, t) * other.getElement(t, j)
            res.append(row)
        return Matrix(res)


test(Matrix, "../artefacts/easy")
