def calculate(n):
    if n < 0:
        print('n is negative')
        exit(-1)
    fib = [0] * n
    if n >= 2:
        fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    print(*fib)

