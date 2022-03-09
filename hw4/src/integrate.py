import math


def worker(f, a, step, acc, list_i):
    for i in list_i:
        acc += f(a + i * step) * step
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
    acc = 0
    step = (b - a) / n_iter
    values_i = [[]] * n_jobs
    k = (n_iter + n_jobs - 1) // n_jobs
    for i in range(n_jobs):
        values_i[i] = list(range(i * k, min(n_iter, (i + 1) * k)))
    for list_i in values_i:
        acc += worker(f, a, step, acc, list_i)
    return acc
