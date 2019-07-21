from random import randrange
from math import sqrt
import time

work_times = {}

class recursion():
    """ I need to use this because i want to turn recursion in to a cycle """
    
    __slots__ = ["func"]
        
    "Can call other methods inside..."
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        while callable(result):
            result = result()
        return result

    def call(self, *args, **kwargs):
        return lambda: self.func(*args, **kwargs)
      
def fast_prime(n, times):
    
    def fermat_test(n):
        random = randrange(1, n)
        try_it = lambda func, a: func(a, n, n) == a
        return try_it(expmod, random)
    
    @recursion
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
        
    if times == 0:
        return True
    if fermat_test(n):
        return fast_prime(n, times - 1)
    else:
        return False
    
def save_time(time):
    cash.append(time)
    
def timer(func):
    
    def wrapper(arg):
        start = time.time()
        func(arg)
        end = time.time()
        work_times[arg] = end - start
        
    
    return wrapper

@timer
def timed_prime_test(num):
    
    even = lambda x: x % 2 == 0
    
    numbers = []
    
    while len(numbers) < 3:
        if not even(num):
            if fast_prime(num, 5):
                numbers.append(num)
        num += 1
    
    print(numbers)

timed_prime_test(1000)
timed_prime_test(10000)
timed_prime_test(100000)
timed_prime_test(1000000)
print((work_times[10000] * sqrt(10)) - work_times[100000])

