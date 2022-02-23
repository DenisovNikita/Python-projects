import numpy as np
import os


def test(Matrix, path):
    np.random.seed(0)
    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    with open(os.path.join(path, "matrix+.txt"), "w") as f:
        res = a + b
        f.write(str(res.matrix))

    with open(os.path.join(path, "matrix*.txt"), "w") as f:
        res = a * b
        f.write(str(res.matrix))

    with open(os.path.join(path, "matrix@.txt"), "w") as f:
        res = a @ b
        f.write(str(res.matrix))
