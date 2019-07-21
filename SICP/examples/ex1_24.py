from random import randrange
import time

cash = []
work_times = {}

def fast_prime(n, times):
    
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
                numbers.append(True)
        num += 1
    
test_list = [1009, 1013, 1019, 10007, 10009, 10037, 100003, 100019, 100043, 1000003, 1000033, 1000037]
for num in test_list:
    timed_prime_test(num)
print(work_times)
