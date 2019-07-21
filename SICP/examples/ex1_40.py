import Newton_transform as n

def cubic(a, b, c):
    return lambda x: n.cube(x) + a * n.square(x) + b * x + c

print(n.Newtons_method(cubic(0, 0, -8), 1))

