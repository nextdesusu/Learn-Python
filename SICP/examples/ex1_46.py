def iterative_improve(check, improve):
    
    def iter_(value):
        old_val = value
        new_val = improve(value)        
        while not check(old_val, new_val, value):
            old_val = new_val
            new_val = improve(old_val)
        return new_val
        
    return iter_

def fixed_point(f, first_guess):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
        
    def try_(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
        
    return try_(first_guess)

def sqrt_old(x):
    average = lambda x, y: (x + y) / 2
    return fixed_point(lambda y: average(y, (x / y)), 1)

def sqrt_new(x):
    average = lambda x, y: (x + y) / 2
    return iterative_improve(lambda v1, v2, v3: abs(v1 - v2) < v3, lambda y: average(y, (x / y)))(0.0001)


print(sqrt_old(100))
print(sqrt_new(100))