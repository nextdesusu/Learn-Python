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

def smooth(f, dx):
    return lambda x: (f(x - dx) + f(x) + f(x + dx)) / 3

def smooth_n(f, dx, n):
    return repeated_iter(lambda g: smooth(g, dx), n)(f)



square = lambda x: x * x
print(smooth(square, 0.5)(1))
print(smooth_n(square, 0.5, 2)(1))