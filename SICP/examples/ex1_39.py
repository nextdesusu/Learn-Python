from math import tan

def tan_cf(x, k):
    
    def cont_frac(n, k):
    
        def iter_(i):
            if (i >= k):
                return 0
            return n(i) / (i - iter_(i + 2))
    
        return iter_(1)
    
    def D(i):
        if i < 2:
            return x
        return x * x
    
    return cont_frac(D, k)
for i in range(100):
    print("*" * 25)
    print(tan_cf(i, 300))
    print(tan(i))