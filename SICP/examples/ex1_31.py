from math import pi

def product1(sp, proc, term, a, next_, b):
    if a > b:
        return 1
    return term(a, sp) * product1(proc(sp), proc, term, next_(a), next_, b)

def new_product(sp, proc, term, a, next_, b):
    res = 1
    while a <= b:
        res *= term(a, sp)
        a = next_(a)
        sp = proc(sp)
    return res

sig = lambda x: -x
dividor = lambda x, on: x / (x + on)
    
two = lambda x: x + 2
fact = lambda x, y: x + y
inc = lambda x: x + 1

#print(new_product(1, sig, dividor, 2, two, 15))
#print(product1(1, sig, dividor, 2, two, 15))
#print(product1(0, sig, fact, 1, inc, 4))
#print(pi/4)

def product(term, a, next_, b):
    if a > b:
        return 1
    return term(a) * product(term, next_(a), next_, b)

def product_iter(term, a, next_, b):
    res = 1
    while a <= b:
        res *= term(a)
        a = next_(a)
    return res

on = -1
def pi_founder(b):
    sig = lambda x: -x
    two = lambda x: x + 2

    def dividor(x):
        global on
        on = sig(on)
        return x / (x + on)    
    
    return product_iter(dividor, 2, two, b)

print(pi_founder(10))
print(pi/4)