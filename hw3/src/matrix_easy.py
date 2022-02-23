import numpy as np

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
        return len(self._matrix), len(self._matrix[0])

    def getElement(self, i, j):
        return self._matrix[i][j]

    def __add__(self, other):
        n, m = self.getDimensions()
        # other.checkDimensions(n, m)
        res = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(self.getElement(i, j) + other.getElement(i, j))
            res.append(row)
        return Matrix(res)

    def __mul__(self, other):
        n, m = self.getDimensions()
        # other.checkDimensions(n, m)
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
        # checkEqual(k1, k2)
        res = []
        for i in range(n):
            row = [0] * m
            for j in range(m):
                for t in range(k1):
                    row[j] += self.getElement(i, t) * other.getElement(t, j)
            res.append(row)
        return Matrix(res)


np.random.seed(0)
a = Matrix(np.random.randint(0, 10, (10, 10)))
b = Matrix(np.random.randint(0, 10, (10, 10)))

with open("../artefacts/easy/matrix+.txt", "w") as f:
    res = a + b
    f.write(str(res.matrix))

with open("../artefacts/easy/matrix*.txt", "w") as f:
    res = a * b
    f.write(str(res.matrix))

with open("../artefacts/easy/matrix@.txt", "w") as f:
    res = a @ b
    f.write(str(res.matrix))
