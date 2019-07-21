from random import randrange
from timer import timer, show

@timer
def fast_prime(n, times):
    
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x    
    
    def fermat_test(n):
        random = randrange(1, n)
        try_it = lambda func, a: func(a, n, n) == a
        return try_it(expmod, random)
    
    def expmod(base, exp, m):
        
        if exp == 0:
            return 1
        if even(exp):
            return remainder(square(expmod(base, exp / 2, m)), m)
        else:
            return remainder(base * (expmod(base, exp - 1, m)), m)
        
    if times == 0:
        return True
    if fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False
    
@timer
def fast_prime_lisa(n, times):
        
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x    
        
    def fermat_test(n):
        random = randrange(1, n)
        try_it = lambda func, a: func(a, n, n) == a
        return try_it(expmod, random)
    
    def fast_expt(b, n):
    
        def even(num):
            return num % 2 == 0 
        
        def square(num):
            return num * num     
            
        def f_expt(a, b, n):
            if n == 0:
                return a
            if even(n):
                return f_expt(a, square(b), (n/2))
            return f_expt((a * b), b, (n-1))
            
            
        return f_expt(1, b, n)
    
        
    def expmod(base, exp, m):
        return remainder(fast_expt(base, exp), m)
            
    if times == 0:
        return True
    if fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False
    

for i in range(2, 50):
    fast_prime_lisa(i, 10)
    fast_prime(i, 10)
    
show()