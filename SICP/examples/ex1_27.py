from random import randrange

def fast_prime(n, times):
    
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x
    random = randrange(1, n)
    test_it = lambda func, a, n: func(a, n, n) == a
    
    def check(n, start):
        if start < n:
            if test_it(expmod, start, n):
                check
    
    def fermat_test(n):
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
        checker(num, random)
        return fast_prime(n, times - 1)
    else:
        return False
    
def tester(n):
    
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x
    random = randrange(1, n)
    test_it = lambda func, a, n: func(a, n, n) == a    
    
    def expmod(base, exp, m):
    
        if exp == 0:
            return 1
        if even(exp):
            return remainder(square(expmod(base, exp / 2, m)), m)
        else:
            return remainder(base * (expmod(base, exp - 1, m)), m)    
    
    def test(a, n):
        return expmod(a, n, n) == a
    
    def test_all_from_start(n, start):
        if start < n:
            if test(start, n):
                return test_all_from_start(n, start+1)
            return False
        return True
    
    return test_all_from_start(n, 1)


Karmikle_numbers = [561, 1105, 1729, 2465, 2821, 6601]
Simple_numbers = [3, 5, 7, 11, 13, 17]

print("*** Karmikle_numbers ***")
for num in Karmikle_numbers:
    print(tester(num))
print("*** Karmikle_numbers ***")
print("*** Simple_numbers ***")
for num in Simple_numbers:
    print(tester(num))
print("*** Simple_numbers ***")
