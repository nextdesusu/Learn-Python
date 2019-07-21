def cons(x, y):
    return lambda m: (m(x, y))

def car(z):
    return z(lambda p, q: p)

def cdr(z):
    return z(lambda p, q: q)

b = cons(10, 3)
print(car(b))
print(cdr(b))
