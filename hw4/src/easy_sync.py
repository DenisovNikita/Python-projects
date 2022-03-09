import time
import fibonacci
start_time = time.time()

NUM_ITERS = 10
N = 10000

for _ in range(NUM_ITERS):
    fibonacci.calculate(N)

with open("../artefacts/easy.txt", "a") as f:
    f.write(f"seconds sync: {str(time.time() - start_time)}\n")
