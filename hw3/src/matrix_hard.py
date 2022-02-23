class Hash:
    # matrix hash equals 42 multiplied by a size of a first dimension
    def __hash__(self):
        return 42 * len(self._matrix)


class Matrix(Hash):
    def __init__(self, value):
        self._matrix = value
        self._cache = {}

    __hash__ = Hash.__hash__

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
        key = (hash(self), hash(other))
        if key not in self._cache:
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
            self._cache[key] = Matrix(res)
        return self._cache[key]

# a = Matrix([[1, 2]])
# b = Matrix([[5], [6]])
# c = Matrix([[3, 4]])
# d = Matrix(b.matrix)
#
# ab = a @ b
# cd = c @ d
# print(a.matrix)
# print(b.matrix)
# print(c.matrix)
# print(d.matrix)
# print(ab.matrix)
# print(cd.matrix)
# print(hash(ab), hash(cd))
# print(hash(a), hash(b))
