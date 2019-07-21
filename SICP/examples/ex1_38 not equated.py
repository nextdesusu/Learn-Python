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
        for num in range(k - 1):
            accum = (n(i) / (d(i) + accum))
            i += 1
        return accum
    
    return iter_(1)

def D(i):
    pass
    
print(cont_frac(lambda i: 1, D, 8))
print(cont_frac_iter(lambda i: 1, D, 8))