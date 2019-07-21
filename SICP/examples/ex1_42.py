def compose(f, g):
    return lambda x: f(g(x))

square = lambda x: x * x
inc = lambda x: x + 1

print(compose(square, inc)(5))