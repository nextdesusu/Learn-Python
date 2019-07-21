def cons(x, y):
    
    def dispatch(m):
        if m == 0:
            return x
        if m == 1:
            return y
        else:
            raise Exception("m = {}, not 0 or 1".format(m))
        
    return dispatch

b = cons(2, 4)

def car(z):
    return z(0)

def cdr(z):
    return z(1)

#print(cdr(b))