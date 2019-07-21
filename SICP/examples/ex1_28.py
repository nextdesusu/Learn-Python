from random import randrange

def tester(n):
    
    even = lambda x: x % 2 == 0
    remainder = lambda x, y: x % y
    square = lambda x: x * x
    random = randrange(1, n)
    test_it = lambda func, a, n: func(a, n, n) == a
    
    def apply_trival_check(k, m, r):
        if not k == 1 and not k == m - 1 and r == 1:
            return 0
        return r    
    
    def remainder_or_trivial(k, m):
        return apply_trival_check(k, m, remainder(square(k), m))    
    
    def modified_expmod(base, exp, m):
        if exp == 0:
            return 1
        if even(exp):
            return remainder_or_trivial(modified_expmod(base, exp / 2, m), m)
        else:
            return remainder(base * modified_expmod(base, exp - 1, m), m)  
    
    def test(a, n):
        return modified_expmod(a, n, n) == a
    
    def test_all_from_start(n, start):
        if start < n:
            if test(start, n):
                return test_all_from_start(n, start+1)
            return False
        return True
    
    return test_all_from_start(n, 1)

Simple_numbers = [3, 5, 7, 11, 13, 17]
Karmikle_numbers = [561, 1105, 1729, 2465, 2821, 6601]

print("*** Simple_numbers ***")
for i in Simple_numbers:
    print(i, tester(i))
print("*** Karmikle_numbers ***")
for i in Karmikle_numbers:
    print(i, tester(i))
