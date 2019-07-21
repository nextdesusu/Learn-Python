def compose(f, g):
    return lambda x: f(g(x))

def repeated_compose(f, n):
    if n > 1:
        return lambda x: compose(repeated_compose(f, n - 1), f)(x)
    return f

def repeated_iter(f, n):
    
    def iter_(x):
        for i in range(n):
            x = f(x)
        return x
    
    return iter_

def average_dump(f):
    average = lambda x, y: (x + y) / 2
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


def root(x, pw):
    pw -= 1
    times = 1
    if pw > 2:
        times *= 26    
        
    
    def root_finder(x, pw, times):
        average = lambda x, y: (x + y) / 2
        average_dump = lambda y: average(y, (x / pow(y, pw)))
        return fixed_point(repeated_iter(average_dump, times), 1)
    
    return root_finder(x, pw, times)


print(root(16, 4))

