def sum_(term, a, next_, b):
    if a > b:
        return 0
    return term(a) + sum_(term, next_(a), next_, b)

def new_sum(term, a, next_, b):
    res = 0
    while a <= b:
        res += term(a)
        a = next_(a)
    return res
        

#cube = lambda x: x * x * x

def cube(x):
    return x * x * x

def integral(f, a, b, dx):
    
    #add_dx = lambda x: x + dx
    def add_dx(x):
        return x + dx
    
    return sum_(f, (a + (dx / 2)), add_dx, b) * dx

def new_integral(f, a, b, dx):
        
    #add_dx = lambda x: x + dx
    def add_dx(x):
        return x + dx
        
    return new_sum(f, (a + (dx / 2)), add_dx, b) * dx

def sum_cubes(a, b):
    inc = lambda x: x + 1
    return new_sum(cube, a, inc, b)
    


print("old: ", integral(cube, 0, 1, 0.01))
print("new: ", new_integral(cube, 0, 1, 0.01))