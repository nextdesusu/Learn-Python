def accumulate(combiner, null_value, term, a, next_, b):
    if a > b:
        return null_value
    return combiner(term(a), accumulate(combiner, null_value, term, next_(a), next_, b))

def accumulate_iter(combiner, null_value, term, a, next_, b):
    res = null_value
    while a <= b:
        res = combiner(res, term(a))
        a = next_(a)
    return res

def cube_sum(a, b):
    
    null_value = 0
    combiner = lambda x, y: x + y
    cube = lambda x: x * x * x
    inc = lambda x: x + 1
    
    return accumulate(combiner, null_value, cube, a, inc, b)

def cube_sum_iter(a, b):
    
    null_value = 0
    combiner = lambda x, y: x + y
    cube = lambda x: x * x * x
    inc = lambda x: x + 1
    
    return accumulate_iter(combiner, null_value, cube, a, inc, b)

def factorial(n):
    
    null_value = 1
    inc = lambda x: x + 1
    combiner = lambda x, y: x * y
    term = lambda x: x  #lol
    
    return accumulate_iter(combiner, null_value, term, null_value, inc, n)


print(cube_sum(1, 10))
print(cube_sum_iter(1, 10))
print(factorial(5))