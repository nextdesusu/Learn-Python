def fixed_point(f, first_guess):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
    
    def try_(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
    
    return try_(first_guess)

def fixed_point_of_transform(g, transform, guess):
    return fixed_point(transform(g), guess)

def average_dump(f):
    return lambda x: average(x, f(x))

def cube_root(x):
    return fixed_point_of_transform(lambda y: (x /(y * y)), average_dump, 1)

def deriv(g):
    dx = 0.00001
    return lambda x: (g(x + dx) - g(x)) / dx

average = lambda x, y: (x + y) / 2
square = lambda x: x * x
cube = lambda x: x * x * x
#print(deriv(cube)(5))

def Newton_transform(g):
    return lambda x: (x - (g(x) / (deriv(g)(x))))

def Newtons_method(g, guess):
    return fixed_point(Newton_transform(g), guess)

def sqrt_old(x):
    return Newtons_method(lambda y: (square(y) - x), 1)

#print(sqrt_old(100))

def sqrt1(x):
    return fixed_point_of_transform(lambda y: x /y, average_dump, 1)

#print("sqrt1: ", sqrt1(100))

def sqrt2():
    return fixed_point_of_transform(lambda y: square(y) - x, Newton_transform, 1)
                                    
#print(cube_root(1000))


#print("sqrt2: ", sqrt1(100))


