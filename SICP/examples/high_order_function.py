average = lambda x, y: (x + y) / 2
square = lambda x: x * x

def average_dump(f):
    return lambda x: average(x, f(x))

def fixed_point(f, first_guess):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
    
    def try_(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
    
    return try_(first_guess)

def sqrt(x):
    return fixed_point(average_dump(lambda y: (x / y)), 1)

def cube_root(x):
    return fixed_point(average_dump(lambda y: (x / square(y))), 1)
    
print(average_dump(square)(10))
print(sqrt(100))
print(cube_root())