import time
import fibonacci
from threading import Thread
start_time = time.time()

NUM_ITERS = 10
N = 10000

threads = []
for _ in range(NUM_ITERS):
    t = Thread(target=fibonacci.calculate, args=(N, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

with open("../artefacts/easy.txt", "a") as f:
    f.write(f"seconds threads: {str(time.time() - start_time)}\n")
