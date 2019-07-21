from math import sqrt

def accumulate(filter_, combiner, null_value, term, a, next_, b):
    if a > b:
        return null_value
    if filter_(a):
        return combiner(term(a), accumulate(filter_, combiner, null_value, term, next_(a), next_, b))
    return accumulate(filter_, combiner, null_value, term, next_(a), next_, b)

def cube(*args):
    res = 0
    for num in args:
        res += num * num 
    return res
        
print(cube(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113))


def prime_cubes_sum(from_, to):
    
    square = lambda x: x * x
    inc = lambda x: x + 1
    combiner = lambda x, y: x + y
    
    def prime_test(num):
        if num <= 1:
            return False
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    return accumulate(prime_test, combiner, 0, square, from_, inc, to)

print(prime_cubes_sum(1, 113))

def prime_to_num_cubes_sum(from_, margin):
    square = lambda x: x * x
    inc = lambda x: x + 1
    combiner = lambda x, y: x + y
    
    def prime_to_num(n):
        to = margin
        if n > to:
            return False
        while to!=0 and n!=0:
            if to > n:
                to = to % n
            else:
                n = n % to
        return to + n == 1
        
    return accumulate(prime_to_num, combiner, 0, square, from_, inc, margin)
        
    #return accumulate(prime_test, combiner, 0, square, from_, inc, to)
print(cube(1, 5, 7, 11))
print(prime_to_num_cubes_sum(1, 12))
