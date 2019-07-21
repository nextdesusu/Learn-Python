def Akkerman(x, y):
    if y == 0:
        return 0
    elif x == 0:
        return y * 2
    elif y == 1:
        return 2
    else:
        return Akkerman(x - 1, Akkerman(x, y - 1))

def f(n):
    return Akkerman(0, n)

def g(n):
    return Akkerman(1, n)
    
def h(n):
    return Akkerman(2, n)

def k(n):
    return 5 * n * n

