def double(f):
    return lambda x: f(f(x))

inc = lambda x: x + 1

print(double(double)(double)(inc)(5))