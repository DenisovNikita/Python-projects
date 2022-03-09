import time
import fibonacci
import multiprocessing as mp
start_time = time.time()

NUM_ITERS = 10
N = 10000

processes = []
for _ in range(NUM_ITERS):
    p = mp.Process(target=fibonacci.calculate, args=(N, ))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

with open("../artefacts/easy.txt", "a") as f:
    f.write(f"seconds processes: {str(time.time() - start_time)}\n")
