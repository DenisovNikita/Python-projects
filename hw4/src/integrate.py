import math
import concurrent.futures
import multiprocessing as mp
import time

with open("../artefacts/medium.txt", "w") as file:
    ITERS = 10_000_000
    EPS = 1e-8


    def worker(f, a, step, acc, list_i):
        for i in list_i:
            acc += f(a + i * step) * step
        return acc


    def work_with_threads(f, a, step, acc, n_jobs, values_i):
        file.write(f"Threads with n_jobs = {n_jobs} is running\n")
        start_time = time.time()
        args = [(f, a, step, acc, i) for i in values_i]
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
            for args_i in args:
                res = executor.submit(worker, *args_i)
                acc += res.result()
        file.write(f"Finished in {time.time() - start_time} seconds\n\n")
        return acc

    def work_with_processes(f, a, step, acc, n_jobs, values_i):
        file.write(f"Processes with n_jobs = {n_jobs} is running\n")
        start_time = time.time()
        args = [(f, a, step, acc, i) for i in values_i]
        with concurrent.futures.ProcessPoolExecutor(max_workers=n_jobs) as executor:
            for args_i in args:
                res = executor.submit(worker, *args_i)
                acc += res.result()
        file.write(f"Finished in {time.time() - start_time} seconds\n\n")
        return acc

    def integrate(f, a, b, *, n_jobs=1, n_iter=1000):
        acc = 0
        step = (b - a) / n_iter
        values_i = [[]] * n_jobs
        k = (n_iter + n_jobs - 1) // n_jobs
        for i in range(n_jobs):
            values_i[i] = list(range(i * k, min(n_iter, (i + 1) * k)))

        acc = work_with_threads(f, a, step, acc, n_jobs, values_i)

        other_acc = 0
        other_acc = work_with_processes(f, a, step, other_acc, n_jobs, values_i)

        assert abs(acc - other_acc) < EPS

        return acc


    result = integrate(math.cos, 0, math.pi / 2, n_iter=ITERS)

    for workers in range(2, 2 * mp.cpu_count()):
        assert abs(integrate(math.cos, 0, math.pi / 2, n_jobs=workers, n_iter=ITERS) - result) < EPS
