def expt(b, n):
    if n == 0:
        return 1
    return b * expt(b, n-1)

def expt_iter(b, n):
    powder = b
    for i in range(n-1):
        b *= powder
    return b

def ex(b, n):
    return ex_iter(b, n, 1)
    
def ex_iter(b, counter, product):
    if counter == 0:
        return product
    return ex_iter(b, counter - 1, b*product)

def fast_expt(b, n):
    if n == 0:
        return 1
    if even(n):
        return square(fast_expt(b, n/2))
    return b * fast_expt(b, n - 1) 
            
def even(n):
    return n % 2 == 0
    
def square(b):
    return b * b

print(expt(3, 6))

print(expt_iter(3, 6))

print(ex(3, 4))

print(fast_expt(3, 4))