from math import cos, sin, pow, ceil
from math import sqrt as sq

def fixed_point(f, first_guess):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
    
    def try_(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
    
    return try_(first_guess)

print(fixed_point(lambda y: sin(y) + cos(y), 1))

def sqrt(x):
    average = lambda x, y: (x + y) / 2
    return fixed_point(lambda y: average(y, (x / y)), 1)

print(sqrt(10))

def fa(x):
    return fixed_point(lambda x: 1 + 1 / x, 1)

def Fib(n):
    return ceil((pow(fa(5), n) - pow(-fa(5), -n)) / (fa(5) - pow(-fa(5), -1)))

def nFib(n):
    f = pow((1 + sq(5)) / 2, n)
    F = pow((1 - sq(5)) / 2, n)
    return int((f - F) / sq(5))

print("*" * 20)
for num in range(20):
    print("New: ", Fib(num), end = " ")
    print("Old: ", nFib(num))