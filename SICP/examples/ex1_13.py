import math

def fib(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def nFib(n):
    f = math.pow((1 + math.sqrt(5)) / 2, n)
    F = math.pow((1 - math.sqrt(5)) / 2, n)
    return int((f - F) / math.sqrt(5))

for i in range(0, 16):
    print("nFib: ", nFib(i), end = ", ")
    print("fib:  ", fib(i))
    print("Equal?: ",nFib(i) == fib(i))
    if not nFib(i) == fib(i):
        print("NOT EQUAL")
        break