def compose(f, g):
    return lambda x: f(g(x))

def repeated_compose(f, n):
    if n > 1:
        return lambda x: compose(repeated_compose(f, n - 1), f)(x)
    return f

def repeated(f, n):
    
    def iter_(x):
        def rec_(num):
            if num < 1:
                return x
            return f(rec_(num - 1))
        
        return rec_(n)
    return iter_

def repeated_iter(f, n):
    
    def iter_(x):
        for i in range(n):
            x = f(x)
        return x
    
    return iter_

square = lambda x: x * x
inc = lambda x: x + 1

for i in range(1, 10):
    print("*" * 25)
    print(repeated_compose(square, i)(5))
    print(repeated(square, i)(5))
    print(repeated_iter(square, i)(5))
#3 390625
    