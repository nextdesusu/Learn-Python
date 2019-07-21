def fixed_point(f, first_guess):
    tolerance = 0.00001
    close_enough = lambda v1, v2: abs(v1 - v2) < tolerance
    
    def try_(guess):
        next_ = f(guess)
        if close_enough(guess, next_):
            return next_
        return try_(next_)
    
    return try_(first_guess)

def fa(x):
    return fixed_point(lambda x: 1 + 1 / x, 1)

F = fa(1)

def cont_frac_old(n, d, k):
    if k < 1:
        return 0
    return n() / (d() + cont_frac_old(n, d, k - 1))

#n() / (d() + n() / (d() + n() / d()))

def f1():
    return 1

def f2():
    return 1

print(cont_frac_old(f1, f2, 100))
print(1/F)

def cont_frac(n, d, k):
    
    def iter_(i):
        if (i >= k):
            return 0
        return n(i) / (d(i) + iter_(i + 1))
    
    return iter_(1)

def cont_frac_iter(n, d, k):
    accum = 0
    
    def iter_(i):
        accum = 0
        for num in range(k):
            accum = (n(i) / (d(i) + accum))
            i += 1
        return accum
    
    return iter_(1)

print(cont_frac(lambda i: 1, lambda i: 1, 200))
print(cont_frac_iter(lambda i: 1, lambda i: 1, 200))