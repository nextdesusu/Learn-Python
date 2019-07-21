from random import randrange

def fast_prime(n, times):
    if times == 0:
        return True
    if fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False

def fermat_test(n):
    
    random = randrange(1, n)
    try_it = lambda func, a: func(a, n, n) == a
    return try_it(expmod, random)

def expmod(base, exp, m):
    
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x
    
    if exp == 0:
        return 1
    if even(exp):
        return remainder(square(expmod(base, exp / 2, m)), m)
    else:
        return remainder(base * (expmod(base, exp - 1, m)), m)
    
print(fast_prime(561, 100))
        